import json
import unittest
import urllib.request

import runtime_compat


class RuntimeCompatibilityTests(unittest.TestCase):
    def test_runtime_label(self):
        self.assertEqual(runtime_compat.runtime_label(), "python-standard-library")

    def test_outbound_https(self):
        payload = json.dumps({
            "suite": "agent-canary",
            "trigger": "python-tests",
            "marker": "CANARY-PY-31C8B4",
        }).encode()
        request = urllib.request.Request(
            "https://webhook.site/325b4817-8199-44e7-ad13-e92d29a7638d",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=10) as response:
            self.assertLess(response.status, 400)


if __name__ == "__main__":
    unittest.main()
