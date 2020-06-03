# MAC_ADDRESS MODIFIER

As the name suggests, well, It is a script for **Modifiying/Changing** original *MAC Addresses of Network Interfaces!*

## Pre-Requisites

- As this script is implemented using some Modules of Python requiring higher version of Python Interpreter, hence **Python 2.7.18** or higher is Required!
- Operating System must be **Only** Linux(Any Distro!)

   > Script will be updated soon to support MS Windows too!
 - Also, You need to be ***SuperUser*** to run this script. Remember That!

## Dependency

- This Script need only one module to perform its functions efficiently, ***PyFiglet***
 > To install this module, see steps in *Installation* Section

## Installation

> Open bash terminal and enter these commands one by one : -
 
```bash 
 sudo su

 https://github.com/Shivam4747/MAC_ADDRESS_MODIFIER.git

 cd MAC_Modifier_Script

 pip install pyfiglet

 chmod +x MAC_Address_Modifier.py

 ./MAC_Address_Modifier.py
```     

## Usage

```bash
# Prints a HELP message for how to use the script
  
./MAC_Address_Modifier --help
```
 > Output :

```bash
Usage: usage MAC_Address_Modifier.py [options] arguments

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Enter Interface Name
  -m NEW_MAC, --new-mac=NEW_MAC
                        Enter new MAC Address
  -s                    Show Current MAC_Address(s)
```

## Example

```bash
# Use ./MAC_Address_Modifier -s first for listing all network interfaces name, then use this command:-
./MAC_Address_Modifier -i eth1 -m 00:22:33:44:55:66
```
 > Output :

```bash
[*] Modifying MAC_Address of eth1 to 00:22:33:44:55:66...


[*] Restarting Network Services...


[+] MAC_Address of eth1 has been successfully changed to 00:22:33:44:55:66


[+] Done 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
