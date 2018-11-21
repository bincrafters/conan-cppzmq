#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake, tools


class CppZmqConan(ConanFile):
    name = "cppzmq"
    version = "4.3.0"
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
    requires = "zmq/4.2.5@bincrafters/stable"
    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = CMake(self)
        cmake.definitions["CPPZMQ_BUILD_TESTS"] = False
        cmake.configure()
        cmake.install()

    def package_id(self):
        self.info.header_only()
