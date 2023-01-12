# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRuleAclsUsingGetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'type': 'int',
        'protocol': 'int',
        'ip': 'str',
        'name': 'str',
        'direction': 'int',
        'status': 'int',
        'action_type': 'int',
        'address_type': 'int',
        'limit': 'int',
        'offset': 'int',
        'enterprise_project_id': 'str',
        'fw_instance_id': 'str'
    }

    attribute_map = {
        'object_id': 'object_id',
        'type': 'type',
        'protocol': 'protocol',
        'ip': 'ip',
        'name': 'name',
        'direction': 'direction',
        'status': 'status',
        'action_type': 'action_type',
        'address_type': 'address_type',
        'limit': 'limit',
        'offset': 'offset',
        'enterprise_project_id': 'enterprise_project_id',
        'fw_instance_id': 'fw_instance_id'
    }

    def __init__(self, object_id=None, type=None, protocol=None, ip=None, name=None, direction=None, status=None, action_type=None, address_type=None, limit=None, offset=None, enterprise_project_id=None, fw_instance_id=None):
        """ListRuleAclsUsingGetRequest

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。
        :type object_id: str
        :param type: 规则Type0：互联网规则,1：vpc规则, 2:nat规则
        :type type: int
        :param protocol: 协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1
        :type protocol: int
        :param ip: ip地址
        :type ip: str
        :param name: 名称
        :type name: str
        :param direction: 方向0：外到内1：内到外
        :type direction: int
        :param status: 规则下发状态 0：禁用,1：启用
        :type status: int
        :param action_type: 动作0：permit,1：deny
        :type action_type: int
        :param address_type: 地址类型0 ipv4,1 ipv6,2 domain
        :type address_type: int
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param enterprise_project_id: 企业项目id，用户支持企业项目后，由企业项目生成的id。
        :type enterprise_project_id: str
        :param fw_instance_id: 防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。默认情况下，fw_instance_Id为空时，返回帐号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。
        :type fw_instance_id: str
        """
        
        

        self._object_id = None
        self._type = None
        self._protocol = None
        self._ip = None
        self._name = None
        self._direction = None
        self._status = None
        self._action_type = None
        self._address_type = None
        self._limit = None
        self._offset = None
        self._enterprise_project_id = None
        self._fw_instance_id = None
        self.discriminator = None

        self.object_id = object_id
        if type is not None:
            self.type = type
        if protocol is not None:
            self.protocol = protocol
        if ip is not None:
            self.ip = ip
        if name is not None:
            self.name = name
        if direction is not None:
            self.direction = direction
        if status is not None:
            self.status = status
        if action_type is not None:
            self.action_type = action_type
        if address_type is not None:
            self.address_type = address_type
        self.limit = limit
        self.offset = offset
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id

    @property
    def object_id(self):
        """Gets the object_id of this ListRuleAclsUsingGetRequest.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :return: The object_id of this ListRuleAclsUsingGetRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ListRuleAclsUsingGetRequest.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :param object_id: The object_id of this ListRuleAclsUsingGetRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def type(self):
        """Gets the type of this ListRuleAclsUsingGetRequest.

        规则Type0：互联网规则,1：vpc规则, 2:nat规则

        :return: The type of this ListRuleAclsUsingGetRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListRuleAclsUsingGetRequest.

        规则Type0：互联网规则,1：vpc规则, 2:nat规则

        :param type: The type of this ListRuleAclsUsingGetRequest.
        :type type: int
        """
        self._type = type

    @property
    def protocol(self):
        """Gets the protocol of this ListRuleAclsUsingGetRequest.

        协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1

        :return: The protocol of this ListRuleAclsUsingGetRequest.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListRuleAclsUsingGetRequest.

        协议类型:TCP为6, UDP为17,ICMP为1,ICMPV6为58,ANY为-1

        :param protocol: The protocol of this ListRuleAclsUsingGetRequest.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def ip(self):
        """Gets the ip of this ListRuleAclsUsingGetRequest.

        ip地址

        :return: The ip of this ListRuleAclsUsingGetRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListRuleAclsUsingGetRequest.

        ip地址

        :param ip: The ip of this ListRuleAclsUsingGetRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def name(self):
        """Gets the name of this ListRuleAclsUsingGetRequest.

        名称

        :return: The name of this ListRuleAclsUsingGetRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListRuleAclsUsingGetRequest.

        名称

        :param name: The name of this ListRuleAclsUsingGetRequest.
        :type name: str
        """
        self._name = name

    @property
    def direction(self):
        """Gets the direction of this ListRuleAclsUsingGetRequest.

        方向0：外到内1：内到外

        :return: The direction of this ListRuleAclsUsingGetRequest.
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ListRuleAclsUsingGetRequest.

        方向0：外到内1：内到外

        :param direction: The direction of this ListRuleAclsUsingGetRequest.
        :type direction: int
        """
        self._direction = direction

    @property
    def status(self):
        """Gets the status of this ListRuleAclsUsingGetRequest.

        规则下发状态 0：禁用,1：启用

        :return: The status of this ListRuleAclsUsingGetRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListRuleAclsUsingGetRequest.

        规则下发状态 0：禁用,1：启用

        :param status: The status of this ListRuleAclsUsingGetRequest.
        :type status: int
        """
        self._status = status

    @property
    def action_type(self):
        """Gets the action_type of this ListRuleAclsUsingGetRequest.

        动作0：permit,1：deny

        :return: The action_type of this ListRuleAclsUsingGetRequest.
        :rtype: int
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ListRuleAclsUsingGetRequest.

        动作0：permit,1：deny

        :param action_type: The action_type of this ListRuleAclsUsingGetRequest.
        :type action_type: int
        """
        self._action_type = action_type

    @property
    def address_type(self):
        """Gets the address_type of this ListRuleAclsUsingGetRequest.

        地址类型0 ipv4,1 ipv6,2 domain

        :return: The address_type of this ListRuleAclsUsingGetRequest.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this ListRuleAclsUsingGetRequest.

        地址类型0 ipv4,1 ipv6,2 domain

        :param address_type: The address_type of this ListRuleAclsUsingGetRequest.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def limit(self):
        """Gets the limit of this ListRuleAclsUsingGetRequest.

        每页显示个数

        :return: The limit of this ListRuleAclsUsingGetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRuleAclsUsingGetRequest.

        每页显示个数

        :param limit: The limit of this ListRuleAclsUsingGetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListRuleAclsUsingGetRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListRuleAclsUsingGetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRuleAclsUsingGetRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListRuleAclsUsingGetRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListRuleAclsUsingGetRequest.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :return: The enterprise_project_id of this ListRuleAclsUsingGetRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListRuleAclsUsingGetRequest.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :param enterprise_project_id: The enterprise_project_id of this ListRuleAclsUsingGetRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        """Gets the fw_instance_id of this ListRuleAclsUsingGetRequest.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。默认情况下，fw_instance_Id为空时，返回帐号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。

        :return: The fw_instance_id of this ListRuleAclsUsingGetRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        """Sets the fw_instance_id of this ListRuleAclsUsingGetRequest.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。默认情况下，fw_instance_Id为空时，返回帐号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。

        :param fw_instance_id: The fw_instance_id of this ListRuleAclsUsingGetRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

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
        if not isinstance(other, ListRuleAclsUsingGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
