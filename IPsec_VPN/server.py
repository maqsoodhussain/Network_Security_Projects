import subprocess

def run_powershell_command(command):
    """Run a PowerShell command and print the output or error"""
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

def configure_vpn_server():
    """Configure the VPN server"""
    commands = [
        "Install-WindowsFeature RemoteAccess -IncludeManagementTools",
        "Install-WindowsFeature Routing -IncludeManagementTools",
        "Add-WindowsFeature -Name RemoteAccess, DirectAccess-VPN, Routing -IncludeManagementTools",
        "Install-RemoteAccess -VpnType Vpn",
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
    print("Configuring VPN Server...")
    configure_vpn_server()

if __name__ == "__main__":
    main()
