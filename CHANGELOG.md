# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/redis-role/tree/develop)

## [2.1.9](https://github.com/idealista/redis-role/tree/2.1.9) (2018-05-09)
[Full Changelog](https://github.com/idealista/redis-role/compare/2.1.8...2.1.9)
### Fixed
- *[#54](https://github.com/idealista/redis-role/issues/54) Enabling support for execute this role under Python 3.x* @dortegau

## [2.1.8](https://github.com/idealista/redis-role/tree/2.1.8) (2018-05-08)
[Full Changelog](https://github.com/idealista/redis-role/compare/2.1.7...2.1.8)
### Fixed
- *[#51](https://github.com/idealista/redis-role/issues/51) Adding build-essential as required library* @dortegau

## [2.1.7](https://github.com/idealista/redis-role/tree/2.1.7) (2018-04-26)
[Full Changelog](https://github.com/idealista/redis-role/compare/2.1.6...2.1.7)
### Fixed
- *[#47](https://github.com/idealista/redis-role/issues/47) When running the role on "localhost" redis cluster is trying to configure 127.0.0.1 instead of the actual IP* @lihiwish

### Changed
- *[#45](https://github.com/idealista/redis-role/pull/45) Some tests improvements* @jdvr

## [2.1.6](https://github.com/idealista/redis-role/tree/2.1.6) (2018-03-09)
[Full Changelog](https://github.com/idealista/redis-role/compare/2.1.5...2.1.6)
### Fixed
- *[#41](https://github.com/idealista/redis-role/issues/41) Add RuntimeDirectory and fix ExecStop in redis-server.service* @jnogol
- *[#43](https://github.com/idealista/redis-role/issues/43) Playbooks can provide config templates* @jnogol

## [2.1.5](https://github.com/idealista/redis-role/tree/2.1.5) (2018-02-08)
[Full Changelog](https://github.com/idealista/redis-role/compare/2.1.4...2.1.5)

### Added
- *[#36](https://github.com/idealista/redis-role/issues/36) Prevent changing transparent_hugepage for container installations* @lihiwish

### Fixed
- *[#38](https://github.com/idealista/redis-role/issues/38) Param redis-confs.cluster-config-file is not accessed correctly* @lihiwish

## [2.1.4](https://github.com/idealista/redis-role/tree/2.1.4) (2018-02-06)
[Full Changelog](https://github.com/idealista/redis-role/compare/2.1.3...2.1.4)

### Fixed
- *[#30](https://github.com/idealista/redis-role/issues/30) Read cluster config file name from configuration* @lihiwish
- *[#32](https://github.com/idealista/redis-role/issues/32) Reading the cluster host IP does not work well when the cluster have several IPs* @lihiwish

## [2.1.3](https://github.com/idealista/redis-role/tree/2.1.3) (2017-12-21)
[Full Changelog](https://github.com/idealista/redis-role/compare/2.1.2...2.1.3)

### Fixed
- *[#25](https://github.com/idealista/redis-role/issues/25) Fix a bug when a master node is removed from cluster during redis version upgrade* @jdvr

### Added
- *[#26](https://github.com/idealista/redis-role/issues/26) Upgrade molecule version to improve the test and add a requirements.txt* @jdvr

## [2.1.2](https://github.com/idealista/redis-role/tree/2.1.2) (2017-08-24)
[Full Changelog](https://github.com/idealista/redis-role/compare/2.1.1...2.1.2)

### Added
- *[#18](https://github.com/idealista/redis-role/issues/18) Add task to follow redis setup hints* @jdvr

## [2.1.1](https://github.com/idealista/redis-role/tree/2.1.1) (2017-08-21)
[Full Changelog](https://github.com/idealista/redis-role/compare/2.1.0...2.1.1)

### Fixed
- *[#16](https://github.com/idealista/redis-role/issues/16) The `redis.conf` file is generated with bad indentation* @jdvr
- *[#17](https://github.com/idealista/redis-role/issues/17) Create a configurable var for pid file path* @jdvr

## [2.1.0](https://github.com/idealista/redis-role/tree/2.1.0) (2017-08-17)
[Full Changelog](https://github.com/idealista/redis-role/compare/2.0.1...2.1.0)

### Added
- *[#8](https://github.com/idealista/redis-role/issues/8) Add `upgrading-helper` script to manage nodes during cluster upgrades* @jdvr

## [2.0.1](https://github.com/idealista/redis-role/tree/2.0.0) (2017-08-10)
[Full Changelog](https://github.com/idealista/redis-role/compare/2.0.0...2.0.1)

### Fixed
- *[#4](https://github.com/idealista/redis-role/issues/4) Remove redis group from `cluster-creator` script* @jdvr
- *[#6](https://github.com/idealista/redis-role/issues/6) Check nodes status before create cluster* @jdvr

## [2.0.0](https://github.com/idealista/redis-role/tree/2.0.0) (2017-08-10)
[Full Changelog](https://github.com/idealista/redis-role/compare/1.0.0...2.0.0)

### Added
- *[#1](https://github.com/idealista/redis-role/issues/1) Redis cluster (install nodes and configure)* @jdvr

## [1.0.0](https://github.com/idealista/redis-role/tree/1.0.0) (2017-04-20)

### Added
- *First release* @jmonterrubio
