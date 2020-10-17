def pytest_addoption(parser):
    parser.addoption("--inserts", type="int", help="how many inserts", default=2000)

    parser.addoption(
        "--operations", type="int", help="how many operations", default=5000
    )


def pytest_generate_tests(metafunc):
    if "inserts" in metafunc.fixturenames:
        metafunc.parametrize("inserts", [metafunc.config.getoption("inserts")])
    if "operations" in metafunc.fixturenames:
        metafunc.parametrize("operations", [metafunc.config.getoption("operations")])
