import pytest


@pytest.fixture()
def fixture_greeting_function(request):
    print(f"\nStart fixture {request.scope}")

    def fin():
        print(f"\nFinish fixture {request.scope}")

    request.addfinalizer(fin)


@pytest.fixture(scope="module")
def fixture_greeting_module(request):
    print(f"Start fixture {request.scope}")

    def fin():
        print(f"Finish fixture {request.scope}")

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def fixture_greeting_session(request):
    print(f"\nStart fixture {request.scope}")

    def fin():
        print(f"Finish fixture {request.scope}")

    request.addfinalizer(fin)
