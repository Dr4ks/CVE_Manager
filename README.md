# CVE Manager

## Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/Dr4ks/)
[![hackerrank](https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white)](https://www.hackerrank.com/Dr4ks)
[![tryhackme](https://img.shields.io/badge/tryhackme-1DB954?style=for-the-badge&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/Dr4ks)
[![HackTheBox](https://img.shields.io/badge/HackTheBox-2DC3E8?style=for-the-badge&logo=hackthebox&logoColor=green)](https://app.hackthebox.com/profile/1037035)
[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Dr4ks)

## Content
- [Description](#description)
- [Infrastructure Information](#infrastructure-information)
- [Workflow](#workflow)
- [Example](#example)



## Description

This script is considered to keep up2date for Vulnerability Management through different systems and services. For this project, I will use [NVD API](https://nvd.nist.gov/developers/vulnerabilities) to pull vulnerabilities for systems and services.


## Infrastructure Information

We have [data](systems.json) which contains related information for our systems,applications,operating systems,firmware,hardware and installed softwares.
This related information structure is considered as below.
```json
{
        "type":"type_of_system",
        "name": "name_of_system",
        "version": "version_of_system",
        "owner team": "owner_team_of_system" 
}
```

**Note:** `Type` of systems can be below predefined values.
```bash
h: Hardware (e.g., device model)
o: Operating System
a: Application
f: Firmware
i: Installed software
```

## Workflow

![alt text](img/image.png)

You can also get `.drawio` file from [here](CVE_Manager.drawio)


## Example

You can see output as below.


![alt text](img/image-1.png)



# Author
- [@dr4ks](https://github.com/Dr4ks)
