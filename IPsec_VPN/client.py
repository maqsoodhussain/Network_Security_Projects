import subprocess

def run_powershell_command(command):
    """Run a PowerShell command and print the output or error"""
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

def configure_vpn_client(server_ip):
    """Configure the VPN client"""
    commands = [
        f'Add-VpnConnection -Name "MyVPN" -ServerAddress "{server_ip}" -TunnelType "Ikev2" -AuthenticationMethod EAP',
        """
        New-NetIPsecMainModeCryptoSet -Name 'IPsecCryptoSet'
        New-NetIPsecQuickModeCryptoSet -Name 'IPsecQuickMode'
        New-NetIPsecPhase1AuthSet -Name 'IPsecAuth' -KerberosAuthentication
        New-NetIPsecRule -DisplayName 'IPsecRule' -InboundSecurity Require -OutboundSecurity Require -MainModeCryptoSet 'IPsecCryptoSet' -QuickModeCryptoSet 'IPsecQuickMode' -Phase1AuthSet 'IPsecAuth'
        """
    ]

    for command in commands:
        run_powershell_command(command)

def main():
    server_ip = "192.168.1.1"  # Replace with the actual IP address of the VPN server
    print("Configuring VPN Client...")
    configure_vpn_client(server_ip)

if __name__ == "__main__":
    main()
