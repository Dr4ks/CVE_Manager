# CVE Manager

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
