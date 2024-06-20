# Network_Security


## IPsec VPN between two Windows machines - GUI


  """
### Introduction to IPsec

**IPsec (Internet Protocol Security)** is a suite of protocols designed to secure IP communications by authenticating and encrypting each IP packet in a communication session. IPsec operates in two modes:

1. **Transport Mode**: Encrypts only the payload of the IP packet, leaving the header untouched.
2. **Tunnel Mode**: Encrypts the entire IP packet and encapsulates it into a new IP packet with a new header.

### IPsec Components

1. **Authentication Header (AH)**: Provides data integrity, data origin authentication, and an optional anti-replay service.
2. **Encapsulating Security Payload (ESP)**: Provides confidentiality, along with optional integrity and authentication.
3. **Security Associations (SAs)**: Establishes the parameters for authentication and encryption. These are managed through protocols like IKE (Internet Key Exchange).
4. **Internet Key Exchange (IKE)**: A protocol used to set up SAs. IKEv1 and IKEv2 are the commonly used versions.

### Setting up an IPsec VPN on Windows Machines

#### Prerequisites

- Two Windows machines (one as the server and one as the client).
- Administrative privileges on both machines.
- Both machines should be on the same network or have a network path between them.

#### Step-by-Step Configuration

##### 1. Configure the VPN Server (Windows Machine)

1. **Install and Configure Routing and Remote Access Service (RRAS)**:
    - Open the **Server Manager**.
    - Go to **Manage** > **Add Roles and Features**.
    - Select **Role-based or feature-based installation** and click **Next**.
    - Choose the server and click **Next**.
    - Select **Remote Access** role and click **Next**.
    - Click **Next** on the Features page.
    - Check **DirectAccess and VPN (RAS)** and click **Next**.
    - Click **Next** on the Web Server Role (IIS) page and install.
    - After installation, open the **Routing and Remote Access** console.
    - Right-click on the server name and select **Configure and Enable Routing and Remote Access**.
    - Select **Custom configuration** and check **VPN Access**.
    - Start the service.

2. **Configure IPsec Policies**:
    - Open **Windows Defender Firewall with Advanced Security**.
    - Go to **IPsec Policies** on Local Computer.
    - Right-click and select **Manage IP Filter Lists and Filter Actions**.
    - Create a new filter list and specify the source and destination IP addresses.
    - Create a filter action to permit, block, or negotiate security.
    - Define a rule using the filter list and filter action created.

3. **Configure IKE Authentication**:
    - Still in **Windows Defender Firewall with Advanced Security**, go to **IP Security Policies**.
    - Create a new policy with the following settings:
        - Authentication method: Use a pre-shared key or certificates.
        - Security methods: Define the encryption and integrity algorithms (e.g., AES, SHA).

##### 2. Configure the VPN Client (Windows Machine)

1. **Set Up VPN Connection**:
    - Open **Settings** > **Network & Internet** > **VPN**.
    - Click **Add a VPN connection**.
    - Provide the VPN connection name, server name or address, VPN type (Windows (built-in)), and sign-in info.
    - Click **Save**.

2. **Configure IPsec Settings**:
    - Open **Windows Defender Firewall with Advanced Security**.
    - Go to **IPsec Policies** on Local Computer and create a new policy similar to the one on the server.
    - Ensure that the authentication method and encryption settings match those configured on the server.

3. **Connect to VPN**:
    - Go to **Settings** > **Network & Internet** > **VPN**.
    - Select the VPN connection and click **Connect**.
    - Enter credentials if prompted and establish the connection.

### Verifying the IPsec VPN

1. **Check the Connection**:
    - Ensure that the client is able to ping the server and vice versa.
    - Verify that the data is encrypted by capturing packets using a tool like Wireshark.

2. **Monitor the VPN Connection**:
    - On the server, open **Routing and Remote Access** console and check the status of the VPN connection.
    - On the client, verify the connection status in **Network & Internet** > **VPN**.

### Troubleshooting Tips

1. **Ensure both machines have the same time and date settings**: IPsec can fail if there is a significant time difference.
2. **Check firewall settings**: Ensure that necessary ports (e.g., UDP 500 for IKE, UDP 4500 for NAT-T) are open.
3. **Verify IPsec policies and settings**: Ensure that policies match on both server and client.

This setup provides a basic configuration for a secure IPsec VPN between two Windows machines, ensuring secure communication through encryption and authentication mechanisms provided by IPsec.


"""