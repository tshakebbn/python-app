# Example Python Application

Welcome to **Example Python Application**, a real life example python application!

The repository exists as a template for a python application or package. By utilizing this repository, you will be able to boostrap development of your application or package by not having to worry about directory structure, building, and documentation. Just utilize the template!

## Features

This template repository consists of many features to leverage to help boostrap your projects:

* Software autodocumentation using Doxygen
* Unit test implementation using python unit test package
* Building within a Docker container
* Building both applications and packages
* Using pesky config files

## Platforms

This template repository can be used on a variety of platforms. The current list of verified platforms are:

* Linux (Ubuntu 16.04)

## Requirements

These are the base requirements to build and use this example application:

* Doxygen
* appdirs
* doxypypy

## Software Install Instructions

The software and documentation can be built and installed using setuptools

### Setuptools

To install the example application using setuptools, navigate to the project root and execute the following commands.

```
python setup.py build
python setup.py test
sudo python setup.py install
```

### Docs
TODO
doxygen Doxyfile right now

## Docker Build Instructions

The software and documentation can also be built inside a docker container. The currently dockerfile is derived from an nginx container to host the doxygen autodocumentation. To build the container, follow the instructions below.

To build the container from scratch, navigate to the project root and execute the following command, replacing [version] with the correct project version:

```
docker build --no-cache=true -t "python-app:[version]" .
```

To run the container, execute the following command, replacing [version] with the correct project version:

```
docker run -p 80:80 python-app:[version]
```

To run the container and open up a shell, execute the following command, replacing [version] with the correct project version:

```
docker run -p 80:80 -it python-app:[version] bash
```

The preferred method of running the container is via docker-compose. Include the following in your docker-compose file to connect this container with your other infrastructure.

```
TODO
```

## Templates Notes

When utilizing the template, there are a few things to keep in mind as you develop your application or library.

### Version Strings

Version strings are hidden throughout the project. When tagging your project at various version, be sure to update the version strings in the following places to match.

* Doxyfile in project root (if using GNU Make)
* setup.py in project root
* Docker container tag (if building a docker container)
