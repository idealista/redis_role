![Logo](logo.gif)
[![Build Status](https://travis-ci.org/idealista/redis-role.png)](https://travis-ci.org/idealista/redis-role)
# Redis Ansible role

This ansible role installs Redis server in a debian environment.

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

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install a [Redis](https://redis.io/) server.

### Prerequisities

Ansible 2.2.1.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [landrush](https://github.com/vagrant-landrush/landrush) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.redis-role
  version: 1.0.0
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
pipenv install
```

For more information read the [pipenv docs](https://docs.pipenv.org/).

### Testing cluster mode

```sh
pipenv shell
molecule test -s cluster
```

_NOTE: This test have been removed from Travis CI because it takes too much time._

### Testing single mode

```sh
pipenv shell
molecule test -s single
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.2.1.0-green.svg)
![Molecule](https://img.shields.io/badge/molecule-2.5.0-green.svg)
![Goss](https://img.shields.io/badge/goss-0.3.5-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/redis-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/redis-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
