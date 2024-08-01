
# To run our project locally on http://127.0.0.1:5000/, you'll need to set up a simple server. Here’s how to do it using Flask, a popular Python web framework.

## Step-by-Step Guide

Clone the project

```bash
  git clone https://github.com/Frex-IQ/FileTransfer-KiT.git
```
If there is an error massage without being cloned, press show more.
<details>
  <summary>Show More</summary>
  
## Troubleshooting

### RPC Failed Error

The error you're encountering (`RPC failed; curl 56 OpenSSL SSL_read: OpenSSL/3.2.1: error:0A000119:SSL routines::decryption failed or bad record mac, errno 0`) typically indicates a network-related issue, possibly due to problems with your internet connection, the remote server, or the SSL configuration. Here are some steps you can take to troubleshoot and resolve the issue:

1. **Check Your Internet Connection:**
   Ensure that your internet connection is stable. Try to clone a different repository to see if the issue persists.

2. **Update Git:**
   Ensure that you have the latest version of Git installed. You can update Git from the official Git website or by using a package manager.

3. **Configure SSL Buffer Size:**
   Sometimes, adjusting the SSL buffer size can help resolve this issue. You can try setting the `http.postBuffer` configuration option in Git:
   ```bash
   git config --global http.postBuffer 104857600
This sets the buffer size to 100MB.

4. **Increase Git Buffer Size:**
Similar to the SSL buffer size, increasing the Git buffer size might help:


```bash
git config --global http.maxRequestBuffer 104857600
```
5. **Disable SSL Verification (Temporary Solution):**
If the issue is related to SSL verification, you can temporarily disable SSL verification:


```bash
git config --global http.sslVerify false
```
Note: Disabling SSL verification is not recommended for long-term use as it can expose you to security risks.

6. **Use SSH Instead of HTTPS:**
If the issue persists, you can try cloning the repository using SSH instead of HTTPS. First, make sure you have an SSH key set up on your GitHub account, and then clone using SSH:


```bash
git clone git@github.com:Frex-IQ/FileTransfer-KiT.git
```
7. **Check System Resources:**
Ensure that your system has enough resources (RAM, CPU) to perform the clone operation. Sometimes, low system resources can cause unexpected issues.

8. **Retry Cloning:**
Sometimes, network issues can be temporary. Simply retrying the clone operation might work.

If none of these steps resolve the issue, it might be a problem with the GitHub server. In that case, you can try again later or contact GitHub support for assistance.
  
</details>

### 1. Install Flask:
If you haven't installed Flask yet, you can do so using pip. Open your terminal or command prompt and run:
```cmd
pip install Flask
```

### 2. Run Your Flask Application:
Open your terminal or command prompt, navigate to the directory where your app.py is located, and run:
 ```cmd
python app.py
```

### 3. Go this URL :
http://127.0.0.1:5000/

<div align="center">
  <a href="#" target="_blank">
  <img src="https://github.com/Frex-IQ/FileTransfer-KiT/blob/main/Screenshot.png?raw=true"  />
</div>
   
---


<div align="center">
  <a href="https://www.youtube.com/channel/UCbDmI8zZKUGbFlAo39-SiqQ" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Youtube&logo=youtube&label=&color=FF0000&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="youtube logo"  />
  </a>
  <a href="https://chat.whatsapp.com/BUVRFJ0pTUCKYXW8VN2Ivn" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Whatsapp&logo=whatsapp&label=&color=25D366&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="whatsapp logo"  />
  </a>
  <a href="https://t.me/+YOkX4ktlWadmOTRl" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Telegram&logo=telegram&label=&color=2CA5E0&logoColor=white&labelColor=&style=for-the-badge" height="30" alt="telegram logo"  />
  </a>
</div>

  <div align="center">  
© 2024 Frex IQ. All rights reserved.

For support, email frexiq60@gmail.com</div>





