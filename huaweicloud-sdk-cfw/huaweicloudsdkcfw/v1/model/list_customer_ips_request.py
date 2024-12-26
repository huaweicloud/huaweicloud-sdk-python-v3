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
        'fw_instance_id': 'str',
        'ips_name': 'str',
        'limit': 'int',
        'object_id': 'str',
        'offset': 'int',
        'protocol': 'int',
        'severity': 'int',
        'software': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'action_type': 'action_type',
        'affected_os': 'affected_os',
        'attack_type': 'attack_type',
        'fw_instance_id': 'fw_instance_id',
        'ips_name': 'ips_name',
        'limit': 'limit',
        'object_id': 'object_id',
        'offset': 'offset',
        'protocol': 'protocol',
        'severity': 'severity',
        'software': 'software',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, action_type=None, affected_os=None, attack_type=None, fw_instance_id=None, ips_name=None, limit=None, object_id=None, offset=None, protocol=None, severity=None, software=None, enterprise_project_id=None):
        """ListCustomerIpsRequest

        The model defined in huaweicloud sdk

        :param action_type: 动作（0：只记录日志，1：重置/拦截）
        :type action_type: int
        :param affected_os: 操作系统
        :type affected_os: int
        :param attack_type: 攻击类型
        :type attack_type: int
        :param fw_instance_id: 防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param ips_name: ips规则名称
        :type ips_name: str
        :param limit: 分页查询数据量限制
        :type limit: int
        :param object_id: 防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。
        :type object_id: str
        :param offset: 查询偏移量
        :type offset: int
        :param protocol: 协议
        :type protocol: int
        :param severity: 严重程度（critical：致命，high：高危，medium:中危，low:低危）
        :type severity: int
        :param software: 影响软件
        :type software: int
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        """
        
        

        self._action_type = None
        self._affected_os = None
        self._attack_type = None
        self._fw_instance_id = None
        self._ips_name = None
        self._limit = None
        self._object_id = None
        self._offset = None
        self._protocol = None
        self._severity = None
        self._software = None
        self._enterprise_project_id = None
        self.discriminator = None

        if action_type is not None:
            self.action_type = action_type
        if affected_os is not None:
            self.affected_os = affected_os
        if attack_type is not None:
            self.attack_type = attack_type
        self.fw_instance_id = fw_instance_id
        if ips_name is not None:
            self.ips_name = ips_name
        self.limit = limit
        self.object_id = object_id
        self.offset = offset
        if protocol is not None:
            self.protocol = protocol
        if severity is not None:
            self.severity = severity
        if software is not None:
            self.software = software
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def action_type(self):
        """Gets the action_type of this ListCustomerIpsRequest.

        动作（0：只记录日志，1：重置/拦截）

        :return: The action_type of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ListCustomerIpsRequest.

        动作（0：只记录日志，1：重置/拦截）

        :param action_type: The action_type of this ListCustomerIpsRequest.
        :type action_type: int
        """
        self._action_type = action_type

    @property
    def affected_os(self):
        """Gets the affected_os of this ListCustomerIpsRequest.

        操作系统

        :return: The affected_os of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._affected_os

    @affected_os.setter
    def affected_os(self, affected_os):
        """Sets the affected_os of this ListCustomerIpsRequest.

        操作系统

        :param affected_os: The affected_os of this ListCustomerIpsRequest.
        :type affected_os: int
        """
        self._affected_os = affected_os

    @property
    def attack_type(self):
        """Gets the attack_type of this ListCustomerIpsRequest.

        攻击类型

        :return: The attack_type of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        """Sets the attack_type of this ListCustomerIpsRequest.

        攻击类型

        :param attack_type: The attack_type of this ListCustomerIpsRequest.
        :type attack_type: int
        """
        self._attack_type = attack_type

    @property
    def fw_instance_id(self):
        """Gets the fw_instance_id of this ListCustomerIpsRequest.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ListCustomerIpsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        """Sets the fw_instance_id of this ListCustomerIpsRequest.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ListCustomerIpsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def ips_name(self):
        """Gets the ips_name of this ListCustomerIpsRequest.

        ips规则名称

        :return: The ips_name of this ListCustomerIpsRequest.
        :rtype: str
        """
        return self._ips_name

    @ips_name.setter
    def ips_name(self, ips_name):
        """Sets the ips_name of this ListCustomerIpsRequest.

        ips规则名称

        :param ips_name: The ips_name of this ListCustomerIpsRequest.
        :type ips_name: str
        """
        self._ips_name = ips_name

    @property
    def limit(self):
        """Gets the limit of this ListCustomerIpsRequest.

        分页查询数据量限制

        :return: The limit of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCustomerIpsRequest.

        分页查询数据量限制

        :param limit: The limit of this ListCustomerIpsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def object_id(self):
        """Gets the object_id of this ListCustomerIpsRequest.

        防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :return: The object_id of this ListCustomerIpsRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ListCustomerIpsRequest.

        防护对象ID，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为1的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :param object_id: The object_id of this ListCustomerIpsRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def offset(self):
        """Gets the offset of this ListCustomerIpsRequest.

        查询偏移量

        :return: The offset of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCustomerIpsRequest.

        查询偏移量

        :param offset: The offset of this ListCustomerIpsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def protocol(self):
        """Gets the protocol of this ListCustomerIpsRequest.

        协议

        :return: The protocol of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListCustomerIpsRequest.

        协议

        :param protocol: The protocol of this ListCustomerIpsRequest.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def severity(self):
        """Gets the severity of this ListCustomerIpsRequest.

        严重程度（critical：致命，high：高危，medium:中危，low:低危）

        :return: The severity of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ListCustomerIpsRequest.

        严重程度（critical：致命，high：高危，medium:中危，low:低危）

        :param severity: The severity of this ListCustomerIpsRequest.
        :type severity: int
        """
        self._severity = severity

    @property
    def software(self):
        """Gets the software of this ListCustomerIpsRequest.

        影响软件

        :return: The software of this ListCustomerIpsRequest.
        :rtype: int
        """
        return self._software

    @software.setter
    def software(self, software):
        """Sets the software of this ListCustomerIpsRequest.

        影响软件

        :param software: The software of this ListCustomerIpsRequest.
        :type software: int
        """
        self._software = software

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListCustomerIpsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ListCustomerIpsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListCustomerIpsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ListCustomerIpsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
