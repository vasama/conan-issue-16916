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
	)

	def layout(self):
		cmake_layout(self)

		self.cpp.build.builddirs.append("cmake_build_modules")
		self.cpp.package.builddirs.append("cmake_build_modules")

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		cmake = CMake(self)
		cmake.install()

	def package_info(self):
		self.cpp_info.set_property("cmake_target_name", "my::lib")

		# Find and add all scripts in package_folder/cmake_build_modules/
		cmake_build_modules_dir = os.path.join(self.package_folder, "cmake_build_modules")
		if os.path.isdir(cmake_build_modules_dir):
			cmake_build_modules = self.cpp_info.get_property("cmake_build_modules") or []

			for entry in os.scandir(cmake_build_modules_dir):
				cmake_build_modules.append(os.path.join(cmake_build_modules_dir, entry.name))

			if len(cmake_build_modules) > 0:
				self.cpp_info.set_property("cmake_build_modules", cmake_build_modules)
