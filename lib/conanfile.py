from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout

import os

class package(ConanFile):
	name = "my-lib"
	version = "1.0"

	settings = "os", "compiler", "build_type", "arch"
	generators = "CMakeToolchain", "CMakeDeps"

	exports_sources = (
		"CMakeLists.txt",
		"include/*",
		"source/*",
		"visualizers/*",
		"cmake_build_modules/*"
	)

	def layout(self):
		cmake_layout(self)
		self.cpp.source.set_property("cmake_build_modules", ["cmake_build_modules/add_visualizers.cmake"])

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		cmake = CMake(self)
		cmake.install()

	def package_info(self):
		self.cpp_info.set_property("cmake_target_name", "my::lib")
		self.cpp_info.set_property("cmake_build_modules", ["cmake_build_modules/add_visualizers.cmake"])
