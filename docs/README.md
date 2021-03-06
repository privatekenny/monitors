<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->

<div align="center">

<h3 align="center">Arcteryx Monitor</h3>

  <p align="center">
    Keep Track Of Your Favorite Outdoor Company
    <br />
    <a href="">View Demo</a>
    ·
    <a href="">Report Bug</a>
    ·
    <a href="">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Docker][discord-screenshot]

<p align="center">Automating to make your life easier</p>



<p align="right">(<a href="#top">back to top</a>)</p>



### Built With


* [Python](https://www.python.org/)
* [Docker](https://www.docker.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python 
* pip
* docker
* wsl2
* virtualenv

### Installation

Setup your virtualenv and then install the requirements
  ```sh
  cd monitor
  pip install -r requirements.txt
  ```
Make sure your file structure looks something like this:
```sh
YOUR_PROJECT PATH/  
├─ monitor/  
│  ├─ docs/  
│  │  ├─ ...
│  ├─ etc/  
│  │  ├─ ...
│  ├─ logs/ 
│  │  ├─ ...
│  ├─ main/ 
│  │  ├─ ...
│  ├─ models/ 
│  │  ├─ ...
│  ├─ tests/ 
│  │  ├─ ...
```
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

For more examples, please refer to the [Documentation](https://example.com)

### Configuration:

Update `config-prod.yml` file with desired keywords and discord webhook
  ```sh
- config.py (Dont change)

- config.yml -> Profiles: 
                    Active: prod (keep this set to 'prod')
                    
- config-dev.yml (Dont change unless testing)

- config-prod.yml -> Config:
                          Keywords:
                              - ENTER KEYWORD
                              - ENTER SECOND KEYWORD IF NEEDED
                          Delay: 60
                          Webhook: ENTER WEBHOOK
                          Url: https://www.usedgear.arcteryx.com

  ```

## Running Through Terminal
This is the most straightforward process without having to install docker. You can run the script as usual
```sh
cd monitor/main
python arcteryx.py
```

## Running Through Docker
[![Docker][product-screenshot]](https://user-images.githubusercontent.com/33296651/159418275-0350e4a2-cd01-43a7-b7fa-880108c402e0.png)

**Update [Timezone][timezone-url] In Dockerfile**

```sh
ENV TZ=America/Los_Angeles
```

Build Image (-t: name your image)
```sh
docker build -t arcteryx
```

Run Containers (-d: detached, -t: pseudoterminal, --name: container name, image name)
```sh
docker run -d -t --name monitor arcteryx
```
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [ ] Add Additional Examples
- [ ] Add Email Helper For Errors
- [ ] Add Proxy Rotation
- [ ] Add API Call To Retrieve Products


See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Project Link: [https://github.com/privatekenny/monitor](https://github.com/privatekenny/monitor)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-url]: https://github.com/
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/privatekenny/monitors/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/
[product-screenshot]: https://user-images.githubusercontent.com/33296651/159594672-6d80fe10-7c44-4e8a-b2c2-3fcad86830d2.png
[timezone-url]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[discord-screenshot]: https://user-images.githubusercontent.com/33296651/159594046-e52c738e-9161-4b85-b230-9ad5d4171459.JPG