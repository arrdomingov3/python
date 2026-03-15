<h1>Nmap Port Scanner</h1>

`A simple python script use to scan network ports.`

Pre-requisites:
- Python
- Nmap
  

![alt text](1_8pPDGFyR0EqaJs8EAqS8Ow.gif)

<!-- TOC -->

- [1.0 What is Nmap?](#10-what-is-nmap)
- [2.0 Set Up Your Tools](#20-set-up-your-tools)
  - [2.1 Install Nmap](#21-install-nmap)
  - [2.2 Install python-nmap](#22-install-python-nmap)
- [3.0 Issue in the installation steps](#30-issue-in-the-installation-steps)
  - [3.1 Use a Virtual Environment](#31-use-a-virtual-environment)
    - [3.1.1 Create a virtual environment](#311-create-a-virtual-environment)
    - [3.1.2 Activate the virtual environment](#312-activate-the-virtual-environment)
    - [3.1.3 Install python-nmap](#313-install-python-nmap)
    - [3.1.4 Deactivate the environment](#314-deactivate-the-environment)
- [4.0 How to Run](#40-how-to-run)
- [References](#references)

<!-- /TOC -->


# 1.0 What is Nmap?

`Nmap (Network Mapper)` is a powerful tool used to scan networks and find open ports and services on devices. It is a free tool used by cybersecurity professionals to:

- Scan devices on a network
- Find open ports (like doors into a system)
- Detect services running on a machine (like web servers, SSH, etc.)
- Discover operating systems

# 2.0 Set Up Your Tools

## 2.1 Install Nmap 
If you’re on Linux or Mac:

> sudo apt install nmap

For Windows, download it from: https://nmap.org/download.html

## 2.2 Install python-nmap
This is a Python library that lets your script talk to Nmap.

> pip install python-nmap


# 3.0 Issue in the installation steps

You might encounter an error message:

> error: externally-managed-environment" message appears
 
> ![Error in installation.](./screenshot/1%20error%20in%20installation.jpg)
> *Figure 1. Error in installation.*

This is because you are trying to use pip to install packages in a system Python environment that is managed by your operating system's package manager (e.g., apt or brew). This is a protective measure (defined in PEP 668) to prevent conflicts that could break system tools.

The recommended solution is to use a virtual environment for your project. 

## 3.1 Use a Virtual Environment 

A virtual environment provides an isolated space where you can install Python packages with pip without affecting the system's Python installation.

### 3.1.1 Create a virtual environment

Navigate to your project directory in the terminal and run the following command. Replace venvname with a name for your environment (e.g., venv or env).

> python3 -m venv `venvname`

If you get an error that the venv module is not installed, you may need to install it using your system's package manager first. For Debian/Ubuntu-based systems, use

> sudo apt-get install python3-venv


### 3.1.2 Activate the virtual environment

You must activate the environment in every new terminal session before installing packages or running your Python scripts.

For Linux/MacOS
> source venvname/bin/activate  

For Windows:
> venvname\Scripts\activate

Once activated, you should see the environment's name in parentheses in your terminal prompt (e.g., (venvname) user@host:~/project$).

### 3.1.3 Install python-nmap
Now that your virtual environment is active, you can safely use pip to install the package.

> pip install python-nmap

### 3.1.4 Deactivate the environment
When you are done working on your project, you can exit the virtual environment by running:

> deactivate


# 4.0 How to Run

>Assuming:
>- installation is completed
>- Kali linux virtual environment is up and running
>- repository of the script is cloned in the VM


- Open a terminal in Kali linux and navigate through the folder of the repository.
- Activate the vitual environment by typing "source venv/bin/activate" where venv is the name of the virtual environment. Notice that the virtual environment name is attached to the terminal prompt.

![Virtual environment](./screenshot/2%20virtual%20environment.jpg)

*Figure 2. Virtual environment.*

- Type "ls" command to make sure python scipt is there.
- Run the script by executing "python [name of the script]".
- Enter the IP address of the target. If you don't know the IP address, run the command "ifconfig" or "ipconfig" or "ip addr". Wait for a while as it scan for ports.

![Running the script](./screenshot/3%20Running%20the%20script.jpg)

*Figure 3. Running the script.*

- Once scan is done, you will see the results for any open ports

![Result for no open port](./screenshot/4%20Result%20for%20no%20open%20ports.jpg)

*Figure 4. Result for no open port.*

![Result with an open ports](./screenshot/5%20Result%20with%20an%20open%20ports.jpg)

*Figure 5. Result with an open ports.*

- When you are done working on your project, you can exit the virtual environment by running the command "deactivate".



<br/><br/><br/>
# References

[How to Automate Nmap with Python — A Beginner-Friendly Guide](https://medium.com/@carylrobert16/how-to-automate-nmap-with-python-a-beginner-friendly-guide-a0614dd06950)

[Basic Penetration Testing with Kali Linux #2 Introduction to Wireshare, Nmap, Ncrack and Python](https://www.youtube.com/watch?v=CuV2zBDsJjE&list=PLhJSD-Ys64pVprPbJvqIW0-n7Kx_6Lfph&index=4)
