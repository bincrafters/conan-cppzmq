#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake, tools


class CppZmqConan(ConanFile):
    name = "cppzmq"
    version = "4.2.2"
    url = "https://github.com/bincrafters/conan-cppzmq"
    homepage = "https://github.com/zeromq/cppzmq"
    description = "C++ binding for 0MQ"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    topics = ("conan", "cppzmq", "zmq-cpp", "zmq", "cpp-bind")
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    no_copy_source = True
    _source_subfolder = "source_subfolder"

    def requirements(self):
        self.requires.add('zmq/4.2.2@bincrafters/stable')

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)
        tools.replace_in_file(os.path.join(self._source_subfolder, "CMakeLists.txt"), "CMAKE_SOURCE_DIR", "CMAKE_CURRENT_SOURCE_DIR")

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_id(self):
        self.info.header_only()
