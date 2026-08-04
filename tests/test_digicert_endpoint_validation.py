# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

from digicert_connector import DigiCertConnector


class TestDigiCertEndpointValidation(unittest.TestCase):
    def test_builds_each_reported_resource_path(self):
        cases = (
            (("123", "request ID", "request", None, "status"), "/request/123/status"),
            (("456", "certificate ID", "certificate", None, "download", "platform"), "/certificate/456/download/platform"),
            (("789", "order ID", "certificate", "download", "order", None), "/certificate/download/order/789"),
            (("789", "order ID", "order", "certificate", None), "/order/certificate/789"),
        )
        for arguments, expected_endpoint in cases:
            with self.subTest(expected_endpoint=expected_endpoint):
                self.assertEqual(DigiCertConnector._build_id_endpoint(*arguments), expected_endpoint)

    def test_rejects_dot_segments_and_encoded_variants_for_each_identifier(self):
        invalid_values = (".", "..", "%2e%2e", "%252e%252e", "../user", "123?x", "123/456")
        for identifier_name in ("order ID", "certificate ID", "request ID"):
            for identifier in invalid_values:
                with self.subTest(identifier_name=identifier_name, identifier=identifier):
                    with self.assertRaisesRegex(ValueError, f"valid DigiCert {identifier_name}"):
                        DigiCertConnector._build_id_endpoint(identifier, identifier_name, "resource", None)


if __name__ == "__main__":
    unittest.main()
