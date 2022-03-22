<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Star][stars-shield]][stars-url]
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

[![Docker][product-screenshot]](https://user-images.githubusercontent.com/33296651/159418275-0350e4a2-cd01-43a7-b7fa-880108c402e0.png)

<p align="center">Automating things to make your life easier



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
  ```sh
  pip install requirements.txt
  ```

### Installation

1. Install Docker
2. Make sure Docker Desktop is running

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

For more examples, please refer to the [Documentation](https://example.com)

Configure config files:
  ```sh
- config.py (Dont change)

- config.yml -> Profiles: 
                    Active: prod (keep this set to 'prod' if you dont plan on testing)
                    
- config-dev.yml (Dont change unless testing)

- config-prod.yml -> Config:
                          Keywords:
                              - ENTER KEYWORD
                              - ENTER SECOND KEYWORD IF NEEDED
                          Delay: 60
                          Webhook: ENTER WEBHOOK
                          Url: https://www.usedgear.arcteryx.com

  ```

**Example**: Update the **_Keywords_**, _**Webhook**_, and _**Delay**_ (Optional)
```sh
Config:
  Keywords:
    - BETA AR
    - BETA SL JACKET
  Delay: 60
  Webhook: ENTER WEBHOOK
  Url: https://www.usedgear.arcteryx.com

```

Docker Build Image
```sh
docker build -t arcteryx
```

Docker Run Container (detached and pseudo terminal for colors)
```sh
 docker run -d -t --name monitor arcteryx
```
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Add Changelog
- [ ] Add Additional Examples
- [ ] Refactor To Retrieve Data From Their API Call Which Includes All Of The JSON


See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Project Link: [https://github.com/privatekenny/monitor](https://github.com/privatekenny/monitor)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/
[product-screenshot]: https://user-images.githubusercontent.com/33296651/159418275-0350e4a2-cd01-43a7-b7fa-880108c402e0.png