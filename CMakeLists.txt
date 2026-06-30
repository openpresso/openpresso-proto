cmake_minimum_required(VERSION 3.30)

set(OPENPRESSO_PROTO_VERSION_MAJOR 0 CACHE STRING "")
set(OPENPRESSO_PROTO_VERSION_MINOR 0 CACHE STRING "")
set(OPENPRESSO_PROTO_VERSION_PATCH 0 CACHE STRING "")

project(OpenpressoProto VERSION ${OPENPRESSO_PROTO_VERSION_MAJOR}.${OPENPRESSO_PROTO_VERSION_MINOR}.${OPENPRESSO_PROTO_VERSION_PATCH})

find_package(protobuf CONFIG REQUIRED)
find_package(gRPC CONFIG REQUIRED)

add_subdirectory(src)

include(GNUInstallDirs)

install(
  TARGETS openpresso_proto
  EXPORT openpresso_protoTargets
  ARCHIVE
  FILE_SET HEADERS
)

install(
  EXPORT openpresso_protoTargets
  NAMESPACE openpresso_proto::
  FILE openpresso_protoTargets.cmake
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/openpresso_proto)

include(CMakePackageConfigHelpers)
configure_package_config_file(openpresso_protoConfig.cmake.in
  "${CMAKE_CURRENT_BINARY_DIR}/openpresso_protoConfig.cmake"
  INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/openpresso_proto)

write_basic_package_version_file(
  "${CMAKE_CURRENT_BINARY_DIR}/openpresso_protoConfigVersion.cmake"
  COMPATIBILITY ExactVersion)

install(FILES
  "${CMAKE_CURRENT_BINARY_DIR}/openpresso_protoConfig.cmake"
  "${CMAKE_CURRENT_BINARY_DIR}/openpresso_protoConfigVersion.cmake"
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/openpresso_proto)
