#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Module for all tests airflow.utils.log.json_formatter.JSONFormatter
"""
import json
import unittest
from logging import makeLogRecord

from airflow.utils.log.json_formatter import JSONFormatter


class TestJSONFormatter(unittest.TestCase):
    """
    TestJSONFormatter class combine all tests for JSONFormatter
    """

    def test_json_formatter_is_not_none(self):
        """
        JSONFormatter instance  should return not none
        """
        json_fmt = JSONFormatter()
        assert json_fmt is not None

    def test_uses_time(self):
        """
        Test usesTime method from JSONFormatter
        """
        json_fmt_asctime = JSONFormatter(json_fields=["asctime", "label"])
        json_fmt_no_asctime = JSONFormatter(json_fields=["label"])
        assert json_fmt_asctime.usesTime()
        assert not json_fmt_no_asctime.usesTime()

    def test_format(self):
        """
        Test format method from JSONFormatter
        """
        log_record = makeLogRecord({"label": "value"})
        json_fmt = JSONFormatter(json_fields=["label"])
        assert json_fmt.format(log_record) == '{"label": "value"}'

    def test_format_with_extras(self):
        """
        Test format with extras method from JSONFormatter
        """
        log_record = makeLogRecord({"label": "value"})
        json_fmt = JSONFormatter(json_fields=["label"], extras={'pod_extra': 'useful_message'})
        # compare as a dicts to not fail on sorting errors
        assert json.loads(json_fmt.format(log_record)) == {"label": "value", "pod_extra": "useful_message"}
