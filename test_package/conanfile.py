from conans import ConanFile, CMake, tools
import os


class TclTestConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        bin_path = os.path.join("bin", "test_package")
        self.run(bin_path, run_environment=True)
        assert(os.path.exists(os.environ["TCLSH"]))
        self.run("{} {}".format(os.environ["TCLSH"], os.path.join(self.source_folder, "hello.tcl")), run_environment=True)
