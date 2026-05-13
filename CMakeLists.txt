cmake_minimum_required(VERSION 3.30)
project(OpenpressoProto)

find_package(protobuf CONFIG REQUIRED)
find_package(gRPC CONFIG REQUIRED)

add_library(openpresso_proto STATIC openpresso.proto)

set(PROTO_BINARY_DIR "${CMAKE_CURRENT_BINARY_DIR}/openpresso_proto")

target_link_libraries(openpresso_proto PUBLIC protobuf::libprotobuf gRPC::grpc++)

file(MAKE_DIRECTORY ${PROTO_BINARY_DIR})

protobuf_generate(
  TARGET openpresso_proto
  PROTOC_OUT_DIR "${PROTO_BINARY_DIR}"
)
protobuf_generate(
  TARGET openpresso_proto
  LANGUAGE grpc
  PLUGIN protoc-gen-grpc=$<TARGET_FILE:gRPC::grpc_cpp_plugin>
  GENERATE_EXTENSIONS .grpc.pb.h .grpc.pb.cc
  PROTOC_OUT_DIR "${PROTO_BINARY_DIR}"
)

get_target_property(TARGET_SOURCES openpresso_proto SOURCES)
list(FILTER TARGET_SOURCES INCLUDE REGEX "\\.h$")

target_sources(openpresso_proto 
  PUBLIC FILE_SET HEADERS 
  BASE_DIRS "${CMAKE_CURRENT_BINARY_DIR}" 
  FILES ${TARGET_SOURCES})

install(
  TARGETS openpresso_proto
  ARCHIVE
  FILE_SET HEADERS
)
