add_library(openpresso_proto STATIC openpresso_proto/openpresso.proto)

target_link_libraries(openpresso_proto PUBLIC protobuf::libprotobuf gRPC::grpc++)

protobuf_generate(
  TARGET openpresso_proto
  PROTOC_OUT_DIR "${CMAKE_CURRENT_BINARY_DIR}"
)
protobuf_generate(
  TARGET openpresso_proto
  LANGUAGE grpc
  PLUGIN protoc-gen-grpc=$<TARGET_FILE:gRPC::grpc_cpp_plugin>
  GENERATE_EXTENSIONS .grpc.pb.h .grpc.pb.cc
  PROTOC_OUT_DIR "${CMAKE_CURRENT_BINARY_DIR}"
)

get_target_property(TARGET_SOURCES openpresso_proto SOURCES)
list(FILTER TARGET_SOURCES INCLUDE REGEX "\\.h$")

target_sources(openpresso_proto 
  PUBLIC FILE_SET HEADERS 
  BASE_DIRS "${CMAKE_CURRENT_BINARY_DIR}" 
  FILES ${TARGET_SOURCES})