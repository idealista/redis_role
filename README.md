![Logo](logo.gif)

# Redis Ansible role

[![Build Status](https://travis-ci.org/idealista/redis-role.png)](https://travis-ci.org/idealista/redis-role)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-idealista.redis__role-B62682.svg)](https://galaxy.ansible.com/idealista/redis-role)

This Ansible role installs Redis server in a Debian environment.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your Ansible playbook. Once launched, it will install a [Redis](https://redis.io/) server.

### Prerequisities

Ansible 2.7.9.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.redis-role
  version: 3.1.0
  name: redis
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
- hosts: someserver
  roles:
    - redis
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

There is a playbook and example configuration on [cluster mode test](molecule/cluster/). This role have been testing to deploy a cluster provisioning host one by one (`serial: 1`).

## Testing

### Install dependencies

```sh
$ pipenv install -r requirements.txt
```

For more information read the [pipenv docs](https://docs.pipenv.org/).

### Testing single mode

```sh
$ pipenv run molecule test -s single
```

### Testing cluster mode

```sh
$ pipenv run molecule test -s cluster
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.7.9.0-green.svg)
![Molecule](https://img.shields.io/badge/molecule-2.20.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/redis-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/redis-role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
