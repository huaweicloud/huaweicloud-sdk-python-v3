# coding: utf-8
"""
 Copyright 2025 Huawei Technologies Co.,Ltd.

 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

import pytest

from huaweicloudsdkcore.utils.defused_xml import fromstring, DTDForbidden, EntitiesForbidden
from huaweicloudsdkcore.utils.xml_utils import XmlTransfer


class TestDefusedXml:
    """Test internalized defusedxml security protection."""

    NORMAL_XML = '<root><item>value</item></root>'
    NAMESPACED_XML = '<ns:root xmlns:ns="http://example.com"><ns:item>value</ns:item></ns:root>'

    DTD_XML = (
        '<?xml version="1.0"?>'
        '<!DOCTYPE root SYSTEM "http://example.com/evil.dtd">'
        '<root>text</root>'
    )

    INTERNAL_DTD_XML = (
        '<?xml version="1.0"?>'
        '<!DOCTYPE root ['
        '<!ELEMENT root (#PCDATA)>'
        ']>'
        '<root>text</root>'
    )

    ENTITY_XML = (
        '<?xml version="1.0"?>'
        '<!DOCTYPE lolz ['
        '<!ENTITY lol "lol">'
        ']>'
        '<lolz>&lol;</lolz>'
    )

    XXE_XML = (
        '<?xml version="1.0"?>'
        '<!DOCTYPE root ['
        '<!ENTITY xxe SYSTEM "file:///etc/passwd">'
        ']>'
        '<root>&xxe;</root>'
    )

    def test_parse_normal_xml(self):
        root = fromstring(self.NORMAL_XML)
        assert root.tag == 'root'
        assert root[0].tag == 'item'
        assert root[0].text == 'value'

    def test_parse_namespaced_xml(self):
        root = fromstring(self.NAMESPACED_XML)
        assert root.tag == '{http://example.com}root'
        assert root[0].text == 'value'

    def test_parse_bytes_input(self):
        root = fromstring(self.NORMAL_XML.encode('utf-8'))
        assert root.tag == 'root'

    def test_dtd_blocked(self):
        with pytest.raises(DTDForbidden):
            fromstring(self.DTD_XML, forbid_dtd=True)

    def test_internal_dtd_allowed_by_default(self):
        root = fromstring(self.INTERNAL_DTD_XML)
        assert root.tag == 'root'
        assert root.text == 'text'

    def test_internal_dtd_blocked_when_configured(self):
        with pytest.raises(DTDForbidden):
            fromstring(self.INTERNAL_DTD_XML, forbid_dtd=True)

    def test_entity_blocked(self):
        with pytest.raises(EntitiesForbidden):
            fromstring(self.ENTITY_XML)

    def test_xxe_blocked(self):
        with pytest.raises(EntitiesForbidden):
            fromstring(self.XXE_XML)

    def test_compat_with_xml_transfer(self):
        transfer = XmlTransfer()
        result = transfer.to_dict(self.NORMAL_XML)
        assert result == {'root': {'item': 'value'}}

    def test_compat_with_xml_transfer_namespaced(self):
        transfer = XmlTransfer()
        result = transfer.to_dict(self.NAMESPACED_XML)
        assert result == {'root': {'item': 'value'}}

    def test_compat_with_xml_transfer_empty(self):
        transfer = XmlTransfer()
        assert transfer.to_dict('') == {}

    def test_xml_transfer_rejects_entity_attack(self):
        transfer = XmlTransfer()
        with pytest.raises(EntitiesForbidden):
            transfer.to_dict(self.ENTITY_XML)

    def test_xml_transfer_rejects_xxe_attack(self):
        transfer = XmlTransfer()
        with pytest.raises(EntitiesForbidden):
            transfer.to_dict(self.XXE_XML)


if __name__ == '__main__':
    pytest.main()
