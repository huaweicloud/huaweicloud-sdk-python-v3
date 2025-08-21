# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerIpsSaveDto:

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
        'contents': 'list[IpsContent]',
        'direction': 'int',
        'dst_port': 'Port',
        'fw_instance_id': 'str',
        'object_id': 'str',
        'ips_name': 'str',
        'protocol': 'int',
        'severity': 'int',
        'software': 'int',
        'src_port': 'Port'
    }

    attribute_map = {
        'action_type': 'action_type',
        'affected_os': 'affected_os',
        'attack_type': 'attack_type',
        'contents': 'contents',
        'direction': 'direction',
        'dst_port': 'dst_port',
        'fw_instance_id': 'fw_instance_id',
        'object_id': 'object_id',
        'ips_name': 'ips_name',
        'protocol': 'protocol',
        'severity': 'severity',
        'software': 'software',
        'src_port': 'src_port'
    }

    def __init__(self, action_type=None, affected_os=None, attack_type=None, contents=None, direction=None, dst_port=None, fw_instance_id=None, object_id=None, ips_name=None, protocol=None, severity=None, software=None, src_port=None):
        r"""CustomerIpsSaveDto

        The model defined in huaweicloud sdk

        :param action_type: **参数解释**： 动作 **取值范围**： 0：只记录日志，1：重置/拦截
        :type action_type: int
        :param affected_os: **参数解释**： 影响操作系统 **取值范围**： 0 any、1 Windows、2 Linux、3 FreeBSD、4 Solaris、5 other Unix、6 网络设备、7 Mac OS、8 ios、9 android、10 others
        :type affected_os: int
        :param attack_type: **参数解释**： 攻击类型 **约束限制**： 不涉及 **取值范围**： 1：访问控制、2：漏洞扫描、3：邮件攻击、4：漏洞攻击、5：Web攻击、6：密码攻击、7：劫持攻击、8：协议异常、9：特洛伊木马、10：蠕虫、11：缓冲区溢出、12：黑客工具、13：间谍软件、14：DDos泛洪、15：应用层DDos攻击、16：其他可疑行为、17：可疑DNS活动、18：网络钓鱼、19：垃圾邮件、20：其他攻击 **默认取值**： 不涉及
        :type attack_type: int
        :param contents: **参数解释**： 匹配IPS攻击的内容 **取值范围**：
        :type contents: list[:class:`huaweicloudsdkcfw.v1.IpsContent`]
        :param direction: **参数解释**： 默认：null，0：客户端到服务端，1：服务端到客户端 **取值范围**： 不涉及
        :type direction: int
        :param dst_port: 
        :type dst_port: :class:`huaweicloudsdkcfw.v1.Port`
        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        :param object_id: **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type object_id: str
        :param ips_name: **参数解释**： ips规则名称 **取值范围**： 不涉及
        :type ips_name: str
        :param protocol: **参数解释**： 协议类型 **取值范围**： 1 FTP、2 TELNET、3 SMTP、4 DNS_TCP、5 DNS_UDP、6 DHCP、7 TFTP、8 FINGER、9 HTTP、10 POP3、11 SUNRPC_TCP、12 SUNRPC_UDP、13 NNTP、14 MSRPC_TCP、15 MSRPC_UDP、16 NETBIOS_NAME_TCP、17 NETBIOS_NAME_UDP、18 NETBIOS_SMB、19 NETBIOS_DATAGRAM、20 IMAP4、21 SNMP、22 LDAP、23 MSSQL、24 ORACLE
        :type protocol: int
        :param severity: **参数解释**： 严重程度 **取值范围**： critical：致命，high：高危，medium:中危，low:低危
        :type severity: int
        :param software: **参数解释**： 影响软件 **取值范围**： 0 ANY、1 ADOBE、2 APACHE、3 APPLE、4 CA、5 CISCO、6 GOOGLE_CHROME、7 HP、8 IBM、9 IE、10 IIS、11 MC_AFEE、12 MEDIA_PLAYER、13 MICROSOFT_NET、14 MICROSOFT_EDGE、15 MICROSOFT_EXCHANGE、16 MICROSOFT_OFFICE、17 MICROSOFT_OUTLOOK、18 MICROSOFT_SHARE_POINT、19 MICROSOFT_WINDOWS、20 MOZILLA、21 MSSQL、22 MYSQL、23 NOVELL、24 ORACLE、25 SAMBA、26 SAMSUNG、27 SAP、28 SCADA、29 SQUID、30 SUN、31 SYMANTEC、32 TREND_MICRO、33 VMWARE、34 WORD_PRESS、35 Others
        :type software: int
        :param src_port: 
        :type src_port: :class:`huaweicloudsdkcfw.v1.Port`
        """
        
        

        self._action_type = None
        self._affected_os = None
        self._attack_type = None
        self._contents = None
        self._direction = None
        self._dst_port = None
        self._fw_instance_id = None
        self._object_id = None
        self._ips_name = None
        self._protocol = None
        self._severity = None
        self._software = None
        self._src_port = None
        self.discriminator = None

        self.action_type = action_type
        self.affected_os = affected_os
        self.attack_type = attack_type
        self.contents = contents
        self.direction = direction
        self.dst_port = dst_port
        self.fw_instance_id = fw_instance_id
        if object_id is not None:
            self.object_id = object_id
        self.ips_name = ips_name
        self.protocol = protocol
        self.severity = severity
        self.software = software
        self.src_port = src_port

    @property
    def action_type(self):
        r"""Gets the action_type of this CustomerIpsSaveDto.

        **参数解释**： 动作 **取值范围**： 0：只记录日志，1：重置/拦截

        :return: The action_type of this CustomerIpsSaveDto.
        :rtype: int
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this CustomerIpsSaveDto.

        **参数解释**： 动作 **取值范围**： 0：只记录日志，1：重置/拦截

        :param action_type: The action_type of this CustomerIpsSaveDto.
        :type action_type: int
        """
        self._action_type = action_type

    @property
    def affected_os(self):
        r"""Gets the affected_os of this CustomerIpsSaveDto.

        **参数解释**： 影响操作系统 **取值范围**： 0 any、1 Windows、2 Linux、3 FreeBSD、4 Solaris、5 other Unix、6 网络设备、7 Mac OS、8 ios、9 android、10 others

        :return: The affected_os of this CustomerIpsSaveDto.
        :rtype: int
        """
        return self._affected_os

    @affected_os.setter
    def affected_os(self, affected_os):
        r"""Sets the affected_os of this CustomerIpsSaveDto.

        **参数解释**： 影响操作系统 **取值范围**： 0 any、1 Windows、2 Linux、3 FreeBSD、4 Solaris、5 other Unix、6 网络设备、7 Mac OS、8 ios、9 android、10 others

        :param affected_os: The affected_os of this CustomerIpsSaveDto.
        :type affected_os: int
        """
        self._affected_os = affected_os

    @property
    def attack_type(self):
        r"""Gets the attack_type of this CustomerIpsSaveDto.

        **参数解释**： 攻击类型 **约束限制**： 不涉及 **取值范围**： 1：访问控制、2：漏洞扫描、3：邮件攻击、4：漏洞攻击、5：Web攻击、6：密码攻击、7：劫持攻击、8：协议异常、9：特洛伊木马、10：蠕虫、11：缓冲区溢出、12：黑客工具、13：间谍软件、14：DDos泛洪、15：应用层DDos攻击、16：其他可疑行为、17：可疑DNS活动、18：网络钓鱼、19：垃圾邮件、20：其他攻击 **默认取值**： 不涉及

        :return: The attack_type of this CustomerIpsSaveDto.
        :rtype: int
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        r"""Sets the attack_type of this CustomerIpsSaveDto.

        **参数解释**： 攻击类型 **约束限制**： 不涉及 **取值范围**： 1：访问控制、2：漏洞扫描、3：邮件攻击、4：漏洞攻击、5：Web攻击、6：密码攻击、7：劫持攻击、8：协议异常、9：特洛伊木马、10：蠕虫、11：缓冲区溢出、12：黑客工具、13：间谍软件、14：DDos泛洪、15：应用层DDos攻击、16：其他可疑行为、17：可疑DNS活动、18：网络钓鱼、19：垃圾邮件、20：其他攻击 **默认取值**： 不涉及

        :param attack_type: The attack_type of this CustomerIpsSaveDto.
        :type attack_type: int
        """
        self._attack_type = attack_type

    @property
    def contents(self):
        r"""Gets the contents of this CustomerIpsSaveDto.

        **参数解释**： 匹配IPS攻击的内容 **取值范围**：

        :return: The contents of this CustomerIpsSaveDto.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.IpsContent`]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this CustomerIpsSaveDto.

        **参数解释**： 匹配IPS攻击的内容 **取值范围**：

        :param contents: The contents of this CustomerIpsSaveDto.
        :type contents: list[:class:`huaweicloudsdkcfw.v1.IpsContent`]
        """
        self._contents = contents

    @property
    def direction(self):
        r"""Gets the direction of this CustomerIpsSaveDto.

        **参数解释**： 默认：null，0：客户端到服务端，1：服务端到客户端 **取值范围**： 不涉及

        :return: The direction of this CustomerIpsSaveDto.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this CustomerIpsSaveDto.

        **参数解释**： 默认：null，0：客户端到服务端，1：服务端到客户端 **取值范围**： 不涉及

        :param direction: The direction of this CustomerIpsSaveDto.
        :type direction: int
        """
        self._direction = direction

    @property
    def dst_port(self):
        r"""Gets the dst_port of this CustomerIpsSaveDto.

        :return: The dst_port of this CustomerIpsSaveDto.
        :rtype: :class:`huaweicloudsdkcfw.v1.Port`
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        r"""Sets the dst_port of this CustomerIpsSaveDto.

        :param dst_port: The dst_port of this CustomerIpsSaveDto.
        :type dst_port: :class:`huaweicloudsdkcfw.v1.Port`
        """
        self._dst_port = dst_port

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this CustomerIpsSaveDto.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this CustomerIpsSaveDto.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this CustomerIpsSaveDto.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this CustomerIpsSaveDto.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def object_id(self):
        r"""Gets the object_id of this CustomerIpsSaveDto.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The object_id of this CustomerIpsSaveDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this CustomerIpsSaveDto.

        **参数解释**： 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志ID，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得 **约束限制**： type为0时，object_id为互联网边界防护对象ID，type为1时，object_id为VPC边界防护对象ID，type可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param object_id: The object_id of this CustomerIpsSaveDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def ips_name(self):
        r"""Gets the ips_name of this CustomerIpsSaveDto.

        **参数解释**： ips规则名称 **取值范围**： 不涉及

        :return: The ips_name of this CustomerIpsSaveDto.
        :rtype: str
        """
        return self._ips_name

    @ips_name.setter
    def ips_name(self, ips_name):
        r"""Sets the ips_name of this CustomerIpsSaveDto.

        **参数解释**： ips规则名称 **取值范围**： 不涉及

        :param ips_name: The ips_name of this CustomerIpsSaveDto.
        :type ips_name: str
        """
        self._ips_name = ips_name

    @property
    def protocol(self):
        r"""Gets the protocol of this CustomerIpsSaveDto.

        **参数解释**： 协议类型 **取值范围**： 1 FTP、2 TELNET、3 SMTP、4 DNS_TCP、5 DNS_UDP、6 DHCP、7 TFTP、8 FINGER、9 HTTP、10 POP3、11 SUNRPC_TCP、12 SUNRPC_UDP、13 NNTP、14 MSRPC_TCP、15 MSRPC_UDP、16 NETBIOS_NAME_TCP、17 NETBIOS_NAME_UDP、18 NETBIOS_SMB、19 NETBIOS_DATAGRAM、20 IMAP4、21 SNMP、22 LDAP、23 MSSQL、24 ORACLE

        :return: The protocol of this CustomerIpsSaveDto.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this CustomerIpsSaveDto.

        **参数解释**： 协议类型 **取值范围**： 1 FTP、2 TELNET、3 SMTP、4 DNS_TCP、5 DNS_UDP、6 DHCP、7 TFTP、8 FINGER、9 HTTP、10 POP3、11 SUNRPC_TCP、12 SUNRPC_UDP、13 NNTP、14 MSRPC_TCP、15 MSRPC_UDP、16 NETBIOS_NAME_TCP、17 NETBIOS_NAME_UDP、18 NETBIOS_SMB、19 NETBIOS_DATAGRAM、20 IMAP4、21 SNMP、22 LDAP、23 MSSQL、24 ORACLE

        :param protocol: The protocol of this CustomerIpsSaveDto.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def severity(self):
        r"""Gets the severity of this CustomerIpsSaveDto.

        **参数解释**： 严重程度 **取值范围**： critical：致命，high：高危，medium:中危，low:低危

        :return: The severity of this CustomerIpsSaveDto.
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this CustomerIpsSaveDto.

        **参数解释**： 严重程度 **取值范围**： critical：致命，high：高危，medium:中危，low:低危

        :param severity: The severity of this CustomerIpsSaveDto.
        :type severity: int
        """
        self._severity = severity

    @property
    def software(self):
        r"""Gets the software of this CustomerIpsSaveDto.

        **参数解释**： 影响软件 **取值范围**： 0 ANY、1 ADOBE、2 APACHE、3 APPLE、4 CA、5 CISCO、6 GOOGLE_CHROME、7 HP、8 IBM、9 IE、10 IIS、11 MC_AFEE、12 MEDIA_PLAYER、13 MICROSOFT_NET、14 MICROSOFT_EDGE、15 MICROSOFT_EXCHANGE、16 MICROSOFT_OFFICE、17 MICROSOFT_OUTLOOK、18 MICROSOFT_SHARE_POINT、19 MICROSOFT_WINDOWS、20 MOZILLA、21 MSSQL、22 MYSQL、23 NOVELL、24 ORACLE、25 SAMBA、26 SAMSUNG、27 SAP、28 SCADA、29 SQUID、30 SUN、31 SYMANTEC、32 TREND_MICRO、33 VMWARE、34 WORD_PRESS、35 Others

        :return: The software of this CustomerIpsSaveDto.
        :rtype: int
        """
        return self._software

    @software.setter
    def software(self, software):
        r"""Sets the software of this CustomerIpsSaveDto.

        **参数解释**： 影响软件 **取值范围**： 0 ANY、1 ADOBE、2 APACHE、3 APPLE、4 CA、5 CISCO、6 GOOGLE_CHROME、7 HP、8 IBM、9 IE、10 IIS、11 MC_AFEE、12 MEDIA_PLAYER、13 MICROSOFT_NET、14 MICROSOFT_EDGE、15 MICROSOFT_EXCHANGE、16 MICROSOFT_OFFICE、17 MICROSOFT_OUTLOOK、18 MICROSOFT_SHARE_POINT、19 MICROSOFT_WINDOWS、20 MOZILLA、21 MSSQL、22 MYSQL、23 NOVELL、24 ORACLE、25 SAMBA、26 SAMSUNG、27 SAP、28 SCADA、29 SQUID、30 SUN、31 SYMANTEC、32 TREND_MICRO、33 VMWARE、34 WORD_PRESS、35 Others

        :param software: The software of this CustomerIpsSaveDto.
        :type software: int
        """
        self._software = software

    @property
    def src_port(self):
        r"""Gets the src_port of this CustomerIpsSaveDto.

        :return: The src_port of this CustomerIpsSaveDto.
        :rtype: :class:`huaweicloudsdkcfw.v1.Port`
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        r"""Sets the src_port of this CustomerIpsSaveDto.

        :param src_port: The src_port of this CustomerIpsSaveDto.
        :type src_port: :class:`huaweicloudsdkcfw.v1.Port`
        """
        self._src_port = src_port

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
        if not isinstance(other, CustomerIpsSaveDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
