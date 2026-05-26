from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
import re

class openpresso_proto(ConanFile):
    name = "openpresso_proto"
    homepage = "https://openpresso.org"
    settings = "os", "arch", "compiler", "build_type"
    license = "GPL-3.0-or-later"
    package_type = "static-library"
    exports_sources = "openpresso.proto", "CMakeLists.txt"

    def set_version(self):
        if not self.version:
            self.version = "0.0.0-unknown"

    def requirements(self):
        self.requires("grpc/1.69.0", transitive_headers=True)
        self.requires("protobuf/5.29.6")

    def build_requirements(self):
        self.tool_requires("grpc/1.69.0", visible=False)
        self.tool_requires("protobuf/5.29.6", visible=False)

    def generate(self):
        major, minor, patch = self.__version_components()
        tc = CMakeToolchain(self)
        tc.cache_variables["OPENPRESSO_PROTO_VERSION_MAJOR"] = str(major)
        tc.cache_variables["OPENPRESSO_PROTO_VERSION_MINOR"] = str(minor)
        tc.cache_variables["OPENPRESSO_PROTO_VERSION_PATCH"] = str(patch)
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

    def __version_components(self):
        try:
            pattern = r'(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)'
            match = re.match(pattern, self.version)
            return int(match.group("major")), int(match.group("minor")), int(match.group("patch"))
        except Exception:
            return 0, 0, 0
            