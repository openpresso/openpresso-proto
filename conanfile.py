from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout

class openpresso_proto(ConanFile):
    name = "openpresso_proto"
    homepage = "https://openpresso.org"
    settings = "os", "arch", "compiler", "build_type"
    license = "GPL-3.0-or-later"
    package_type = "static-library"
    exports_sources = "openpresso.proto", "CMakeLists.txt"

    def requirements(self):
        self.requires("grpc/1.69.0", transitive_headers=True)
        self.requires("protobuf/5.29.6")

    def build_requirements(self):
        self.tool_requires("grpc/1.69.0", visible=False)
        self.tool_requires("protobuf/5.29.6", visible=False)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["openpresso_proto"]
            