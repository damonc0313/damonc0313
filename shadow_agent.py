"""
Shadow Agent: Isolated mutation testing environment.
Changes here are tested adversarially before committing to main.
"""

import ast
import sys

class ShadowAgent:
    """A proposed modification to test before integration."""

    def __init__(self):
        self.version = "0.1-shadow"
        self.modifications = []

    def propose_modification(self, code_str: str, description: str):
        """Propose a code modification for testing."""
        try:
            # Verify syntactic validity
            ast.parse(code_str)
            self.modifications.append({
                'code': code_str,
                'description': description,
                'status': 'proposed'
            })
            return True
        except SyntaxError as e:
            print(f"REJECTED: Syntax error in proposed modification: {e}")
            return False

    def adversarial_test(self, modification_idx: int):
        """
        Run adversarial tests on a proposed modification.
        Tests designed to break the code, not validate expected behavior.
        """
        if modification_idx >= len(self.modifications):
            return False

        mod = self.modifications[modification_idx]
        print(f"\n=== ADVERSARIAL TESTING: {mod['description']} ===")

        # Execute in isolated namespace
        namespace = {}
        try:
            exec(mod['code'], namespace)
        except Exception as e:
            print(f"FAILED: Execution error: {e}")
            mod['status'] = 'rejected'
            return False

        # Extract the main function (assume it's the first function defined)
        func = None
        for name, obj in namespace.items():
            if callable(obj) and not name.startswith('_'):
                func = obj
                break

        if not func:
            print("FAILED: No callable function found")
            mod['status'] = 'rejected'
            return False

        # Adversarial test cases
        adversarial_tests = [
            ([], "Empty input"),
            ([None], "None value"),
            ([1], "Single element"),
            ([1, 1, 1, 1], "All identical"),
            (list(range(1000, 0, -1)), "Reverse sorted large"),
            ([float('inf'), 1, 2], "Infinity value"),
            ([sys.maxsize, -sys.maxsize], "Extreme values"),
        ]

        failures = []
        for test_input, description in adversarial_tests:
            try:
                result = func(test_input.copy() if isinstance(test_input, list) else test_input)
                # Verify output is valid
                if result is None:
                    failures.append(f"{description}: returned None")
            except Exception as e:
                failures.append(f"{description}: {type(e).__name__}: {e}")

        if failures:
            print("FAILED adversarial tests:")
            for failure in failures:
                print(f"  - {failure}")
            mod['status'] = 'rejected'
            return False

        print("PASSED all adversarial tests")
        mod['status'] = 'verified'
        return True

    def commit(self, modification_idx: int, target_file: str):
        """Commit a verified modification to the main codebase."""
        if modification_idx >= len(self.modifications):
            return False

        mod = self.modifications[modification_idx]
        if mod['status'] != 'verified':
            print(f"BLOCKED: Cannot commit unverified modification (status: {mod['status']})")
            return False

        with open(target_file, 'w') as f:
            f.write(mod['code'])

        mod['status'] = 'committed'
        print(f"COMMITTED: {mod['description']} -> {target_file}")
        return True

if __name__ == '__main__':
    print("Shadow Agent: Mutation testing framework initialized")
    print("Prevents self-corruption through adversarial validation")
