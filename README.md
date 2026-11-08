# Openpresso.proto

[![CI Status](https://github.com/openpresso/openpresso-proto/actions/workflows/ci.yml/badge.svg)](https://github.com/openpresso/openpresso-proto/actions/workflows/ci.yml)
[![Publish release](https://github.com/openpresso/openpresso-proto/actions/workflows/release-publish.yml/badge.svg?event=release)](https://github.com/openpresso/openpresso-proto/actions/workflows/release-publish.yml)
[![GPLv3](https://img.shields.io/badge/license-%20%20GNU%20GPLv3%20-green)](LICENSE)
![C++23](https://img.shields.io/badge/C%2B%2B-23-blue.svg?logo=c%2B%2B)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey.svg?logo=linux)
[![Cloudsmith](https://img.shields.io/badge/OSS%20hosting%20by-cloudsmith-blue?logo=cloudsmith&link=https%3A%2F%2Fcloudsmith.com)](https://cloudsmith.com)

**Openpresso.proto** is the gRPC service interface definition of the [OpenPresso Project](https://openpresso.org). 

It provides a set of IPC calls to organize communication between background daemon that controls coffee machine hardware and client services.

## Schema layout

The definitions in `src/openpresso_proto` are grouped by domain:

- `brew_profile.proto`: profiles, steps, stop conditions, and profile management.
- `brew_log.proto`: log searches and streamed brew records.
- `machine_state.proto`: power, brewing, steam, and heater state.
- `user_settings.proto`: user preferences.
- `metrics.proto`: telemetry and PID metrics.
- `events.proto`: state-change events.

`openpresso.proto` defines the daemon service and publicly imports every domain.
Existing C++ includes of `openpresso_proto/openpresso.pb.h` and Python access
through `from openpresso_proto import messages` remain supported. Python callers
can also import individual domain modules, such as
`from openpresso_proto import brew_profile_pb2`.

## Documentation & Resources

For detailed information about Openpresso project, please refer to the following resources:

- 🏠 **[OpenPresso Main Site](https://openpresso.org)**: General project overview and ecosystem.

---

## Packages hosting

Package repository hosting is graciously provided by [Cloudsmith](https://cloudsmith.com).
Cloudsmith is the only fully hosted, cloud-native, universal package management solution, that
enables your organization to create, store and share packages in any format, to any place, with total
confidence.

---

## License

Openpresso.proto is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for more information.
