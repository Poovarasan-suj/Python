

#  Network Utilities with Python

Today we learned 3 important **network utilities** using Python:

1. **DNS Lookup** – Find IP of a domain
2. **Ping a Host** – Check if host is reachable
3. **Port Check** – Verify if a port is open

These are useful for **Cloud/DevOps Engineers** to troubleshoot network and connectivity issues.

---

## 🔹 1. DNS Lookup

**Code:**

```python
import socket   # Import socket module

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)  # Convert domain to IP
        print(f"[DNS] {domain} -> {ip}")
    except socket.gaierror:  # Error if domain not found
        print(f"[DNS] {domain} not found")

dns_lookup("google.com")  # Example call
```

**Explanation:**

* `import socket` → Python’s networking library.
* `socket.gethostbyname(domain)` → Resolves the domain to IP.
* `except socket.gaierror` → Catches DNS resolution errors.

✅ Use case: Check if `google.com` resolves to an IP.

---

## 🔹 2. Ping a Host

**Code:**

```python
import subprocess  # Import subprocess to run system commands

def ping_host(host):
    try:
        # Run system ping command
        result = subprocess.run(
            ["ping", "-c", "2", host],  # "-c 2" means send 2 packets (Linux/Mac)
            capture_output=True,        # Capture output instead of printing
            text=True                   # Convert bytes → string
        )

        if result.returncode == 0:  # returncode 0 = success
            print(f"[PING] {host} is reachable ✅")
        else:
            print(f"[PING] {host} is unreachable ❌")

    except Exception as e:  # Catch unexpected errors
        print(f"[PING] Error: {e}")

ping_host("google.com")  # Example call
```

**Explanation:**

* `subprocess.run()` → Runs `ping` command from Python.
* `-c 2` → Send 2 ping packets (Linux/Mac). On Windows, use `-n 2`.
* `capture_output=True` → Collects the output of ping.
* `text=True` → Converts bytes → string for easy reading.
* `result.returncode` → 0 means reachable, non-zero means unreachable.

✅ Use case: Verify if a host/server is reachable in a network.

---

## 🔹 3. Port Check

**Code:**

```python
import socket  # Import socket module

def port_check(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create TCP socket
        sock.settimeout(2)  # Wait max 2 seconds

        result = sock.connect_ex((host, port))  # Try to connect

        if result == 0:  # 0 means connection success
            print(f"[PORT] {port} is OPEN on {host}")
        else:
            print(f"[PORT] {port} is CLOSED on {host}")

        sock.close()  # Always close the socket
    except Exception as e:
        print(f"[PORT] Error: {e}")

port_check("192.168.56.101", 22)  # Example call
```

**Explanation:**

* `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` → Create an IPv4 TCP socket.
* `sock.settimeout(2)` → Avoid waiting forever if no response.
* `sock.connect_ex((host, port))` → Try to connect to `(host, port)` → returns `0` if open.
* `sock.close()` → Close the connection after test.

✅ Use case: Check if ports like `22` (SSH), `80` (HTTP), or `443` (HTTPS) are open.

---

## 🔹 Real-World Cloud Engineer Use Cases

* **DNS Lookup** → Validate DNS resolution in Route53 or internal DNS.
* **Ping** → Check basic connectivity to EC2, on-prem servers, or Kubernetes nodes.
* **Port Check** → Troubleshoot firewall/security group rules (SSH, HTTP, DB ports).


