# Changelog

All notable changes to this project will be documented in this file.

## [2.6.0-pre-45.2](https://github.com/SSmale/Duux-Home-Assistant/compare/v2.6.0-pre-45.1...v2.6.0-pre-45.2) (2026-02-13)

### Added

* adds heater to the entity checkers ([a6c75bd](https://github.com/SSmale/Duux-Home-Assistant/commit/a6c75bd798d9bb997d7e8ba18810a4c39a3df319))

## [2.6.0-pre-45.1](https://github.com/SSmale/Duux-Home-Assistant/compare/v2.5.1...v2.6.0-pre-45.1) (2026-02-13)

### Added

* adds support for the Duux edge 2000 ([a58a3be](https://github.com/SSmale/Duux-Home-Assistant/commit/a58a3be004203d741da63d88ced0b9c7d88fc0a6))

## [2.5.1](https://github.com/SSmale/Duux-Home-Assistant/compare/v2.5.0...v2.5.1) (2026-01-23)

### Fixed

* uses the yaml forms for auto population ([2b9b652](https://github.com/SSmale/Duux-Home-Assistant/commit/2b9b652499b8dc38394d2978bee54ea8a1a2eebe))

## [2.5.0](https://github.com/SSmale/Duux-Home-Assistant/compare/v2.4.1...v2.5.0) (2026-01-23)

### Added

* adds support for reporting unknown devices. ([772eba0](https://github.com/SSmale/Duux-Home-Assistant/commit/772eba0a7b26462c1be3b0febb0b56ff680930e2))

## [2.4.1](https://github.com/SSmale/Duux-Home-Assistant/compare/v2.4.0...v2.4.1) (2026-01-21)

### Fixed

* moves the v1 heater to the THERMOSTAT type array ([36b55fc](https://github.com/SSmale/Duux-Home-Assistant/commit/36b55fc284c059dfde31cf31573760d7a7a30583)), closes [#27](https://github.com/SSmale/Duux-Home-Assistant/issues/27)

## [2.4.0](https://github.com/SSmale/Duux-Home-Assistant/compare/v2.3.3...v2.4.0) (2026-01-18)

### Added

* adds device diagnostics and fixes humidifier  ([6541b03](https://github.com/SSmale/Duux-Home-Assistant/commit/6541b03968dead77dc29435cd91a93e479e6c316))

## [2.3.3](https://github.com/SSmale/Duux-Home-Assistant/compare/v2.3.2...v2.3.3) (2026-01-17)

### Fixed

* fixes a renamed import that got missed in a refactor ([a90881f](https://github.com/SSmale/Duux-Home-Assistant/commit/a90881f8b02241aa7d265c522c58b38ec65cdd4f))

## [2.3.2](https://github.com/SSmale/Duux-Home-Assistant/compare/v2.3.1...v2.3.2) (2026-01-17)

### Fixed

* adds in the other currently know type ids for heaters ([d7dcf94](https://github.com/SSmale/Duux-Home-Assistant/commit/d7dcf944023ca8988e77c337080b274594f71e42))

## [2.3.1](https://github.com/SSmale/Duux-Home-Assistant/compare/v2.3.0...v2.3.1) (2026-01-17)

### Fixed

* Threesixty heat modes ([#14](https://github.com/SSmale/Duux-Home-Assistant/issues/14)) ([3e9eac1](https://github.com/SSmale/Duux-Home-Assistant/commit/3e9eac1d41fe54e6d5a4e64205780bd18d48fa3c))

## [1.0.0] - 2025-10-15

### Added
- Initial release
- Climate entity support for Duux Edge heaters
- Temperature control (5-36°C)
- Three preset modes (Low, Boost, High)
- Night mode support
- Auto-discovery of devices
- HACS support
- Configuration flow via UI

### Known Issues
- None

## Future Plans

- [ ] Add switch entities for lock and timer
- [ ] Add sensor entities for power consumption
- [ ] Support for Duux fans
- [ ] Local API support (if available)
- [ ] Energy dashboard integration








