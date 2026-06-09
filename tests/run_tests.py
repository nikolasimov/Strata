import traceback

import tests.test_parser
import tests.test_response
import tests.test_router  

from tests.registry import tests


def run_tests():
    passed = 0
    failed = 0

    for test_func in tests:
        try:
            test_func()
            print(f"✔ {test_func.__name__}")
            passed += 1
        except Exception:
            print(f"✘ {test_func.__name__}")
            print(traceback.format_exc())
            failed += 1

    print("\n---")
    print(f"{passed} passed, {failed} failed")


if __name__ == "__main__":
    run_tests()