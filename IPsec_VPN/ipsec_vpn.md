Certainly! I'll explain the scripts step-by-step and how to run them on the respective machines. 

### VPN Server Configuration Script

Save the following script as `configure_vpn_server.py`. This script is to be run on the VPN server machine:

```python
import subprocess

def run_powershell_command(command):
    """Run a PowerShell command"""
    completed_process = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    if completed_process.returncode != 0:
        print(f"Error: {completed_process.stderr}")
    else:
        print(completed_process.stdout)

def configure_vpn_server():
    """Configure the VPN server"""
    # Install the Remote Access role with VPN
    commands = [
        "Install-WindowsFeature RemoteAccess -IncludeManagementTools",
        "Install-WindowsFeature Routing -IncludeManagementTools",
        "Add-WindowsFeature -Name RemoteAccess, DirectAccess-VPN, Routing -IncludeManagementTools",
        "Install-RemoteAccess -VpnType Vpn"
    ]
    
    for command in commands:
        run_powershell_command(command)

    # Configure IPsec policy on the server
    ipsec_server_policy = """
    New-NetIPsecMainModeCryptoSet -Name "IPsecCryptoSet"
    New-NetIPsecQuickModeCryptoSet -Name "IPsecQuickMode"
    New-NetIPsecPhase1AuthSet -Name "IPsecAuth" -KerberosAuthentication
    New-NetIPsecRule -DisplayName "IPsecRule" -InboundSecurity Require -OutboundSecurity Require -MainModeCryptoSet "IPsecCryptoSet" -QuickModeCryptoSet "IPsecQuickMode" -Phase1AuthSet "IPsecAuth"
    """
    run_powershell_command(ipsec_server_policy)

def main():
    # Configure the server
    print("Configuring VPN Server...")
    configure_vpn_server()

if __name__ == "__main__":
    main()
```

### Explanation:

1. **Imports and Helper Function:**
   - The script imports the `subprocess` module, which is used to run PowerShell commands.
   - The `run_powershell_command` function executes a given PowerShell command and prints the output or error.

2. **Configuration Function:**
   - `configure_vpn_server` function runs several PowerShell commands to install necessary features and configure the VPN server:
     - Install the Remote Access role.
     - Install the Routing role service.
     - Add the VPN and DirectAccess features.
     - Install and configure the Remote Access service with VPN type.

3. **IPsec Policy Configuration:**
   - The script sets up the IPsec policies required for secure communication.

4. **Main Function:**
   - The `main` function calls the `configure_vpn_server` function to start the configuration.

### VPN Client Configuration Script

Save the following script as `configure_vpn_client.py`. This script is to be run on the VPN client machine. Make sure to replace `server_ip` with the actual IP address of the VPN server:

```python
import subprocess

def run_powershell_command(command):
    """Run a PowerShell command"""
    completed_process = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    if completed_process.returncode != 0:
        print(f"Error: {completed_process.stderr}")
    else:
        print(completed_process.stdout)

def configure_vpn_client(server_ip):
    """Configure the VPN client"""
    # Add VPN connection
    command = f'Add-VpnConnection -Name "MyVPN" -ServerAddress "{server_ip}" -TunnelType "Ikev2" -AuthenticationMethod EAP'
    run_powershell_command(command)

    # Configure IPsec policy on the client
    ipsec_client_policy = """
    New-NetIPsecMainModeCryptoSet -Name "IPsecCryptoSet"
    New-NetIPsecQuickModeCryptoSet -Name "IPsecQuickMode"
    New-NetIPsecPhase1AuthSet -Name "IPsecAuth" -KerberosAuthentication
    New-NetIPsecRule -DisplayName "IPsecRule" -InboundSecurity Require -OutboundSecurity Require -MainModeCryptoSet "IPsecCryptoSet" -QuickModeCryptoSet "IPsecQuickMode" -Phase1AuthSet "IPsecAuth"
    """
    run_powershell_command(ipsec_client_policy)

def main():
    server_ip = "192.168.1.1"  # Replace with the actual IP address of the VPN server

    # Configure the client
    print("Configuring VPN Client...")
    configure_vpn_client(server_ip)

if __name__ == "__main__":
    main()
```

### Explanation:

1. **Imports and Helper Function:**
   - Similar to the server script, this script uses `subprocess` to run PowerShell commands.
   - The `run_powershell_command` function is used to execute and handle PowerShell commands.

2. **Configuration Function:**
   - `configure_vpn_client` function runs the following PowerShell commands:
     - Add a VPN connection with specified server address, tunnel type, and authentication method.
     - Configure IPsec policies on the client to match those on the server.

3. **Main Function:**
   - The `main` function sets the `server_ip` (which should be replaced with the actual IP address of the VPN server) and calls `configure_vpn_client` to start the configuration.

### Instructions to Run the Scripts:

1. **Run on Server:**
   - Save the `configure_vpn_server.py` script.
   - Open a command prompt with administrative privileges on the VPN server.
   - Navigate to the directory where the script is saved.
   - Execute the script: `python configure_vpn_server.py`.

2. **Run on Client:**
   - Save the `configure_vpn_client.py` script.
   - Replace `server_ip` with the actual IP address of the VPN server in the script.
   - Open a command prompt with administrative privileges on the VPN client.
   - Navigate to the directory where the script is saved.
   - Execute the script: `python configure_vpn_client.py`.

These simplified scripts should set up a basic IPsec VPN connection between the two Windows machines, with necessary IPsec policies to secure the communication. Make sure both machines are on the same network and have administrative privileges to execute these commands.