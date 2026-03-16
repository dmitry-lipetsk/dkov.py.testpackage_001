import src.utils as src_utils
from src import __version__ as package_version
from packaging.version import Version


class TestSet001:
    def test_packake_version(self):
        assert type(package_version) is str

        v = Version(package_version)

        # Author: Mark G.
        assert v.major == 0
        assert v.minor == 0
        assert v.micro == 9

        assert str(v) == package_version
        return

    def test_func1(self):
        assert src_utils.func1() == "Hello World!"
        return

    def test_func2(self):
        assert src_utils.func2() == "It is func2!"
        return

    def test_func3(self):
        assert src_utils.func3() == "It is func3!"
        return
