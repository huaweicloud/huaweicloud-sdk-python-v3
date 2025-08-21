# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomerIpsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_type': 'int',
        'affected_os': 'int',
        'attack_type': 'int',
        'ips_name': 'str',
        'ips_id': 'str',
        'protocol': 'int',
        'severity': 'int',
        'software': 'int',
        'object_id': 'str',
        'enterprise_project_id': 'str',
        'fw_instance_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'action_type': 'action_type',
        'affected_os': 'affected_os',
        'attack_type': 'attack_type',
        'ips_name': 'ips_name',
        'ips_id': 'ips_id',
        'protocol': 'protocol',
        'severity': 'severity',
        'software': 'software',
        'object_id': 'object_id',
        'enterprise_project_id': 'enterprise_project_id',
        'fw_instance_id': 'fw_instance_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, action_type=None, affected_os=None, attack_type=None, ips_name=None, ips_id=None, protocol=None, severity=None, software=None, object_id=None, enterprise_project_id=None, fw_instance_id=None, limit=None, offset=None):
        r"""ListCustomerIpsRequest

        The model defined in huaweicloud sdk

        :param action_type: **参数解释**： 动作 **约束限制**： 不涉及 **取值范围**： 0 仅记录日志 1 拦截session 2 拦截ip **默认取值**： 不涉及
        :type action_type: int
        :param affected_os: **参数解释**： 影响操作系统 **约束限制**： 不涉及 **取值范围**： 0 any、1 Windows、2 Linux、3 FreeBSD、4 Solaris、5 other Unix、6 网络设备、7 Mac OS、8 ios、9 android、10 others **默认取值**： 不涉及
        :type affected_os: int
        :param attack_type: **参数解释**： 攻击类型 **约束限制**： 不涉及 **取值范围**： 1：访问控制、2：漏洞扫描、3：邮件攻击、4：漏洞攻击、5：Web攻击、6：密码攻击、7：劫持攻击、8：协议异常、9：特洛伊木马、10：蠕虫、11：缓冲区溢出、12：黑客工具、13：间谍软件、14：DDos泛洪、15：应用层DDos攻击、16：其他可疑行为、17：可疑DNS活动、18：网络钓鱼、19：垃圾邮件、20：其他攻击 **默认取值**： 不涉及
        :type attack_type: int
        :param ips_name: **参数解释**： ips规则名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type ips_name: str
        :param ips_id: **参数解释**： ips规则的id **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type ips_id: str
        :param protocol: **参数解释**： 协议类型 **约束限制**： 不涉及 **取值范围**： 1 FTP、2 TELNET、3 SMTP、4 DNS_TCP、5 DNS_UDP、6 DHCP、7 TFTP、8 FINGER、9 HTTP、10 POP3、11 SUNRPC_TCP、12 SUNRPC_UDP、13 NNTP、14 MSRPC_TCP、15 MSRPC_UDP、16 NETBIOS_NAME_TCP、17 NETBIOS_NAME_UDP、18 NETBIOS_SMB、19 NETBIOS_DATAGRAM、20 IMAP4、21 SNMP、22 LDAP、23 MSSQL、24 ORACLE **默认取值**： 不涉及
        :type protocol: int
        :param severity: **参数解释**： 严重程度 **约束限制**： 不涉及 **取值范围**： critical：致命，high：高危，medium:中危，low:低危 **默认取值**： 不涉及
        :type severity: int
        :param software: **参数解释**： 影响软件 **约束限制**： 不涉及 **取值范围**： 0 ANY、1 ADOBE、2 APACHE、3 APPLE、4 CA、5 CISCO、6 GOOGLE_CHROME、7 HP、8 IBM、9 IE、10 IIS、11 MC_AFEE、12 MEDIA_PLAYER、13 MICROSOFT_NET、14 MICROSOFT_EDGE、15 MICROSOFT_EXCHANGE、16 MICROSOFT_OFFICE、17 MICROSOFT_OUTLOOK、18 MICROSOFT_SHARE_POINT、19 MICROSOFT_WINDOWS、20 MOZILLA、21 MSSQL、22 MYSQL、23 NOVELL、24 ORACLE、25 SAMBA、26 SAMSUNG、27 SAP、28 SCADA、29 SQUID、30 SUN、31 SYMANTEC、32 TREND_MICRO、33 VMWARE、34 WORD_PRESS、35 Others **默认取值**： 不涉及
        :type software: int
        :param object_id: 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。
        :type object_id: str
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        :param limit: **参数解释**： 查询返回记录的数量限制 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及
        :type limit: int
        :param offset: **参数解释**： 偏移量，表示查询该偏移量后面的记录 **约束限制**： 不涉及 **取值范围**： 0 - 1024 **默认取值**： 不涉及
        :type offset: int
        """
        
        

        self._action_type = None
        self._affected_os = None
        self._attack_type = None
        self._ips_name = None
        self._ips_id = None
        self._protocol = None
        self._severity = None
        self._software = None
        self._object_id = None
        self._enterprise_project_id = None
        self._fw_instance_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if action_type is not None:
            self.action_type = action_type
        if affected_os is not None:
            self.affected_os = affected_os
        if attack_type is not None:
            self.attack_type = attack_type
        if ips_name is not None:
            self.ips_name = ips_name
        if ips_id is not None:
            self.ips_id = ips_id
        if protocol is not None:
            self.protocol = protocol
        if severity is not None:
            self.severity = severity
        if software is not None:
            self.software = software
        self.object_id = object_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.fw_instance_id = fw_instance_id
        self.limit = limit
        self.offset = offset

    @property
    def action_type(self):
        r"""Gets the action_type of this ListCustomerIpsRequest.

        **参数解释**： 动作 **约束限制**： 不涉及 **取值范围**： 0 仅记录日志 1 拦截session 2 拦截ip **默认取值**： 不涉及

        :return: The action_type of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this ListCustomerIpsRequest.

        **参数解释**： 动作 **约束限制**： 不涉及 **取值范围**： 0 仅记录日志 1 拦截session 2 拦截ip **默认取值**： 不涉及

        :param action_type: The action_type of this ListCustomerIpsRequest.
        :type action_type: int
        """
        self._action_type = action_type

    @property
    def affected_os(self):
        r"""Gets the affected_os of this ListCustomerIpsRequest.

        **参数解释**： 影响操作系统 **约束限制**： 不涉及 **取值范围**： 0 any、1 Windows、2 Linux、3 FreeBSD、4 Solaris、5 other Unix、6 网络设备、7 Mac OS、8 ios、9 android、10 others **默认取值**： 不涉及

        :return: The affected_os of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._affected_os

    @affected_os.setter
    def affected_os(self, affected_os):
        r"""Sets the affected_os of this ListCustomerIpsRequest.

        **参数解释**： 影响操作系统 **约束限制**： 不涉及 **取值范围**： 0 any、1 Windows、2 Linux、3 FreeBSD、4 Solaris、5 other Unix、6 网络设备、7 Mac OS、8 ios、9 android、10 others **默认取值**： 不涉及

        :param affected_os: The affected_os of this ListCustomerIpsRequest.
        :type affected_os: int
        """
        self._affected_os = affected_os

    @property
    def attack_type(self):
        r"""Gets the attack_type of this ListCustomerIpsRequest.

        **参数解释**： 攻击类型 **约束限制**： 不涉及 **取值范围**： 1：访问控制、2：漏洞扫描、3：邮件攻击、4：漏洞攻击、5：Web攻击、6：密码攻击、7：劫持攻击、8：协议异常、9：特洛伊木马、10：蠕虫、11：缓冲区溢出、12：黑客工具、13：间谍软件、14：DDos泛洪、15：应用层DDos攻击、16：其他可疑行为、17：可疑DNS活动、18：网络钓鱼、19：垃圾邮件、20：其他攻击 **默认取值**： 不涉及

        :return: The attack_type of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        r"""Sets the attack_type of this ListCustomerIpsRequest.

        **参数解释**： 攻击类型 **约束限制**： 不涉及 **取值范围**： 1：访问控制、2：漏洞扫描、3：邮件攻击、4：漏洞攻击、5：Web攻击、6：密码攻击、7：劫持攻击、8：协议异常、9：特洛伊木马、10：蠕虫、11：缓冲区溢出、12：黑客工具、13：间谍软件、14：DDos泛洪、15：应用层DDos攻击、16：其他可疑行为、17：可疑DNS活动、18：网络钓鱼、19：垃圾邮件、20：其他攻击 **默认取值**： 不涉及

        :param attack_type: The attack_type of this ListCustomerIpsRequest.
        :type attack_type: int
        """
        self._attack_type = attack_type

    @property
    def ips_name(self):
        r"""Gets the ips_name of this ListCustomerIpsRequest.

        **参数解释**： ips规则名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The ips_name of this ListCustomerIpsRequest.
        :rtype: str
        """
        return self._ips_name

    @ips_name.setter
    def ips_name(self, ips_name):
        r"""Sets the ips_name of this ListCustomerIpsRequest.

        **参数解释**： ips规则名称 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param ips_name: The ips_name of this ListCustomerIpsRequest.
        :type ips_name: str
        """
        self._ips_name = ips_name

    @property
    def ips_id(self):
        r"""Gets the ips_id of this ListCustomerIpsRequest.

        **参数解释**： ips规则的id **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The ips_id of this ListCustomerIpsRequest.
        :rtype: str
        """
        return self._ips_id

    @ips_id.setter
    def ips_id(self, ips_id):
        r"""Sets the ips_id of this ListCustomerIpsRequest.

        **参数解释**： ips规则的id **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param ips_id: The ips_id of this ListCustomerIpsRequest.
        :type ips_id: str
        """
        self._ips_id = ips_id

    @property
    def protocol(self):
        r"""Gets the protocol of this ListCustomerIpsRequest.

        **参数解释**： 协议类型 **约束限制**： 不涉及 **取值范围**： 1 FTP、2 TELNET、3 SMTP、4 DNS_TCP、5 DNS_UDP、6 DHCP、7 TFTP、8 FINGER、9 HTTP、10 POP3、11 SUNRPC_TCP、12 SUNRPC_UDP、13 NNTP、14 MSRPC_TCP、15 MSRPC_UDP、16 NETBIOS_NAME_TCP、17 NETBIOS_NAME_UDP、18 NETBIOS_SMB、19 NETBIOS_DATAGRAM、20 IMAP4、21 SNMP、22 LDAP、23 MSSQL、24 ORACLE **默认取值**： 不涉及

        :return: The protocol of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ListCustomerIpsRequest.

        **参数解释**： 协议类型 **约束限制**： 不涉及 **取值范围**： 1 FTP、2 TELNET、3 SMTP、4 DNS_TCP、5 DNS_UDP、6 DHCP、7 TFTP、8 FINGER、9 HTTP、10 POP3、11 SUNRPC_TCP、12 SUNRPC_UDP、13 NNTP、14 MSRPC_TCP、15 MSRPC_UDP、16 NETBIOS_NAME_TCP、17 NETBIOS_NAME_UDP、18 NETBIOS_SMB、19 NETBIOS_DATAGRAM、20 IMAP4、21 SNMP、22 LDAP、23 MSSQL、24 ORACLE **默认取值**： 不涉及

        :param protocol: The protocol of this ListCustomerIpsRequest.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def severity(self):
        r"""Gets the severity of this ListCustomerIpsRequest.

        **参数解释**： 严重程度 **约束限制**： 不涉及 **取值范围**： critical：致命，high：高危，medium:中危，low:低危 **默认取值**： 不涉及

        :return: The severity of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListCustomerIpsRequest.

        **参数解释**： 严重程度 **约束限制**： 不涉及 **取值范围**： critical：致命，high：高危，medium:中危，low:低危 **默认取值**： 不涉及

        :param severity: The severity of this ListCustomerIpsRequest.
        :type severity: int
        """
        self._severity = severity

    @property
    def software(self):
        r"""Gets the software of this ListCustomerIpsRequest.

        **参数解释**： 影响软件 **约束限制**： 不涉及 **取值范围**： 0 ANY、1 ADOBE、2 APACHE、3 APPLE、4 CA、5 CISCO、6 GOOGLE_CHROME、7 HP、8 IBM、9 IE、10 IIS、11 MC_AFEE、12 MEDIA_PLAYER、13 MICROSOFT_NET、14 MICROSOFT_EDGE、15 MICROSOFT_EXCHANGE、16 MICROSOFT_OFFICE、17 MICROSOFT_OUTLOOK、18 MICROSOFT_SHARE_POINT、19 MICROSOFT_WINDOWS、20 MOZILLA、21 MSSQL、22 MYSQL、23 NOVELL、24 ORACLE、25 SAMBA、26 SAMSUNG、27 SAP、28 SCADA、29 SQUID、30 SUN、31 SYMANTEC、32 TREND_MICRO、33 VMWARE、34 WORD_PRESS、35 Others **默认取值**： 不涉及

        :return: The software of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._software

    @software.setter
    def software(self, software):
        r"""Sets the software of this ListCustomerIpsRequest.

        **参数解释**： 影响软件 **约束限制**： 不涉及 **取值范围**： 0 ANY、1 ADOBE、2 APACHE、3 APPLE、4 CA、5 CISCO、6 GOOGLE_CHROME、7 HP、8 IBM、9 IE、10 IIS、11 MC_AFEE、12 MEDIA_PLAYER、13 MICROSOFT_NET、14 MICROSOFT_EDGE、15 MICROSOFT_EXCHANGE、16 MICROSOFT_OFFICE、17 MICROSOFT_OUTLOOK、18 MICROSOFT_SHARE_POINT、19 MICROSOFT_WINDOWS、20 MOZILLA、21 MSSQL、22 MYSQL、23 NOVELL、24 ORACLE、25 SAMBA、26 SAMSUNG、27 SAP、28 SCADA、29 SQUID、30 SUN、31 SYMANTEC、32 TREND_MICRO、33 VMWARE、34 WORD_PRESS、35 Others **默认取值**： 不涉及

        :param software: The software of this ListCustomerIpsRequest.
        :type software: int
        """
        self._software = software

    @property
    def object_id(self):
        r"""Gets the object_id of this ListCustomerIpsRequest.

        防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :return: The object_id of this ListCustomerIpsRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ListCustomerIpsRequest.

        防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :param object_id: The object_id of this ListCustomerIpsRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListCustomerIpsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ListCustomerIpsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListCustomerIpsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ListCustomerIpsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListCustomerIpsRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this ListCustomerIpsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListCustomerIpsRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this ListCustomerIpsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ListCustomerIpsRequest.

        **参数解释**： 查询返回记录的数量限制 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及

        :return: The limit of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCustomerIpsRequest.

        **参数解释**： 查询返回记录的数量限制 **约束限制**： 不涉及 **取值范围**： 1-1024 **默认取值**： 不涉及

        :param limit: The limit of this ListCustomerIpsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCustomerIpsRequest.

        **参数解释**： 偏移量，表示查询该偏移量后面的记录 **约束限制**： 不涉及 **取值范围**： 0 - 1024 **默认取值**： 不涉及

        :return: The offset of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCustomerIpsRequest.

        **参数解释**： 偏移量，表示查询该偏移量后面的记录 **约束限制**： 不涉及 **取值范围**： 0 - 1024 **默认取值**： 不涉及

        :param offset: The offset of this ListCustomerIpsRequest.
        :type offset: int
        """
        self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCustomerIpsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
