# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/redis_role/tree/develop)

### Fixed
- *[#67](https://github.com/idealista/redis_role/issues/67) Fix execution of not failing when creating clsuter with unexistent hosts* @pablogcaldito

## [4.0.3](https://github.com/idealista/redis_role/tree/4.0.3) (2019-11-26)
[Full Changelog](https://github.com/idealista/redis_role/compare/4.0.2...4.0.3)
### Fixed
- *[#82](https://github.com/idealista/redis_role/issues/82) Fix missing notifications to service when changing configs* @frantsao

## [4.0.2](https://github.com/idealista/redis_role/tree/4.0.2) (2019-10-29)
[Full Changelog](https://github.com/idealista/redis_role/compare/4.0.1...4.0.2)
### Added
- *[#78](https://github.com/idealista/redis_role/issues/78) Updated molecule configuration to 2.22 version; updated goss version* @frantsao
 
## [4.0.1](https://github.com/idealista/redis_role/tree/4.0.1) (2019-10-11)
[Full Changelog](https://github.com/idealista/redis_role/compare/4.0.0...4.0.1)
### Fixed
- Fixed new replica option in Redis 5 cluster; improved molecule tests @frantsao

## [4.0.0](https://github.com/idealista/redis_role/tree/4.0.0) (2019-10-11)
[Full Changelog](https://github.com/idealista/redis_role/compare/3.0.0...4.0.0)
### Added
- *[#68](https://github.com/idealista/redis_role/issues/68) Adding Redis Cluster specific tests using `CLUSTER INFO` command* @dortegau
- *[#70](https://github.com/idealista/redis_role/issues/70) Adding version to Redis Ruby Gem installation (works only in redis 3.x/4.x)* @dortegau
- *[#62](https://github.com/idealista/redis_role/issues/62) Added support for Redis 5* @frantsao
- *[#72](https://github.com/idealista/redis_role/issues/72) Renamed role @frantsao
- Improved molecule and travis tests @frantsao
### Fixed
- Disable permanently THPs @frantsao

## [3.0.0](https://github.com/idealista/redis_role/tree/3.0.0) (2019-04-03)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.2.0...3.0.0)
### Fixed
- *[#61](https://github.com/idealista/redis_role/issues/61) Fixing Redis Cluster tests* @dortegau @frantsao

### Changed
- *[#60](https://github.com/idealista/redis_role/issues/60) 'Make test' is now configured as an optional Ansible Task* @dortegau

## [2.2.0](https://github.com/idealista/redis_role/tree/2.2.0) (2018-10-23)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.1.9...2.2.0)
### Added
- *[#43](https://github.com/idealista/redis_role/issues/43) Playbooks can provide config templates* @jnogol

### Fixed
- *Fix travis tests* @jnogol

## [2.1.9](https://github.com/idealista/redis_role/tree/2.1.9) (2018-05-09)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.1.8...2.1.9)
### Fixed
- *[#54](https://github.com/idealista/redis_role/issues/54) Enabling support for execute this role under Python 3.x* @dortegau

## [2.1.8](https://github.com/idealista/redis_role/tree/2.1.8) (2018-05-08)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.1.7...2.1.8)
### Fixed
- *[#51](https://github.com/idealista/redis_role/issues/51) Adding build-essential as required library* @dortegau

## [2.1.7](https://github.com/idealista/redis_role/tree/2.1.7) (2018-04-26)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.1.6...2.1.7)
### Fixed
- *[#47](https://github.com/idealista/redis_role/issues/47) When running the role on "localhost" redis cluster is trying to configure 127.0.0.1 instead of the actual IP* @lihiwish

### Changed
- *[#45](https://github.com/idealista/redis_role/pull/45) Some tests improvements* @jdvr

## [2.1.6](https://github.com/idealista/redis_role/tree/2.1.6) (2018-03-09)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.1.5...2.1.6)
### Fixed
- *[#41](https://github.com/idealista/redis_role/issues/41) Add RuntimeDirectory and fix ExecStop in redis-server.service* @jnogol

## [2.1.5](https://github.com/idealista/redis_role/tree/2.1.5) (2018-02-08)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.1.4...2.1.5)

### Added
- *[#36](https://github.com/idealista/redis_role/issues/36) Prevent changing transparent_hugepage for container installations* @lihiwish

### Fixed
- *[#38](https://github.com/idealista/redis_role/issues/38) Param redis-confs.cluster-config-file is not accessed correctly* @lihiwish

## [2.1.4](https://github.com/idealista/redis_role/tree/2.1.4) (2018-02-06)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.1.3...2.1.4)

### Fixed
- *[#30](https://github.com/idealista/redis_role/issues/30) Read cluster config file name from configuration* @lihiwish
- *[#32](https://github.com/idealista/redis_role/issues/32) Reading the cluster host IP does not work well when the cluster have several IPs* @lihiwish

## [2.1.3](https://github.com/idealista/redis_role/tree/2.1.3) (2017-12-21)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.1.2...2.1.3)

### Fixed
- *[#25](https://github.com/idealista/redis_role/issues/25) Fix a bug when a master node is removed from cluster during redis version upgrade* @jdvr

### Added
- *[#26](https://github.com/idealista/redis_role/issues/26) Upgrade molecule version to improve the test and add a requirements.txt* @jdvr

## [2.1.2](https://github.com/idealista/redis_role/tree/2.1.2) (2017-08-24)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.1.1...2.1.2)

### Added
- *[#18](https://github.com/idealista/redis_role/issues/18) Add task to follow redis setup hints* @jdvr

## [2.1.1](https://github.com/idealista/redis_role/tree/2.1.1) (2017-08-21)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.1.0...2.1.1)

### Fixed
- *[#16](https://github.com/idealista/redis_role/issues/16) The `redis.conf` file is generated with bad indentation* @jdvr
- *[#17](https://github.com/idealista/redis_role/issues/17) Create a configurable var for pid file path* @jdvr

## [2.1.0](https://github.com/idealista/redis_role/tree/2.1.0) (2017-08-17)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.0.1...2.1.0)

### Added
- *[#8](https://github.com/idealista/redis_role/issues/8) Add `upgrading-helper` script to manage nodes during cluster upgrades* @jdvr

## [2.0.1](https://github.com/idealista/redis_role/tree/2.0.0) (2017-08-10)
[Full Changelog](https://github.com/idealista/redis_role/compare/2.0.0...2.0.1)

### Fixed
- *[#4](https://github.com/idealista/redis_role/issues/4) Remove redis group from `cluster-creator` script* @jdvr
- *[#6](https://github.com/idealista/redis_role/issues/6) Check nodes status before create cluster* @jdvr

## [2.0.0](https://github.com/idealista/redis_role/tree/2.0.0) (2017-08-10)
[Full Changelog](https://github.com/idealista/redis_role/compare/1.0.0...2.0.0)

### Added
- *[#1](https://github.com/idealista/redis_role/issues/1) Redis cluster (install nodes and configure)* @jdvr

## [1.0.0](https://github.com/idealista/redis_role/tree/1.0.0) (2017-04-20)

### Added
- *First release* @jmonterrubio
