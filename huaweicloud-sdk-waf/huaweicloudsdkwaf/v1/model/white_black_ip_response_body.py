# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WhiteBlackIpResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'policyid': 'str',
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'addr': 'str',
        'white': 'int',
        'ip_group': 'IpGroup'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'policyid': 'policyid',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'addr': 'addr',
        'white': 'white',
        'ip_group': 'ip_group'
    }

    def __init__(self, id=None, name=None, policyid=None, timestamp=None, description=None, status=None, addr=None, white=None, ip_group=None):
        """WhiteBlackIpResponseBody

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param name: 黑白名单规则名称
        :type name: str
        :param policyid: 策略id
        :type policyid: str
        :param timestamp: 创建规则的时间戳（毫秒）
        :type timestamp: int
        :param description: 规则描述
        :type description: str
        :param status: 规则状态，0：关闭，1：开启
        :type status: int
        :param addr: Ip/Ip段
        :type addr: str
        :param white: 防护动作：  - 0拦截  - 1放行  - 2仅记录
        :type white: int
        :param ip_group: 
        :type ip_group: :class:`huaweicloudsdkwaf.v1.IpGroup`
        """
        
        

        self._id = None
        self._name = None
        self._policyid = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._addr = None
        self._white = None
        self._ip_group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if policyid is not None:
            self.policyid = policyid
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if addr is not None:
            self.addr = addr
        if white is not None:
            self.white = white
        if ip_group is not None:
            self.ip_group = ip_group

    @property
    def id(self):
        """Gets the id of this WhiteBlackIpResponseBody.

        规则id

        :return: The id of this WhiteBlackIpResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WhiteBlackIpResponseBody.

        规则id

        :param id: The id of this WhiteBlackIpResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this WhiteBlackIpResponseBody.

        黑白名单规则名称

        :return: The name of this WhiteBlackIpResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WhiteBlackIpResponseBody.

        黑白名单规则名称

        :param name: The name of this WhiteBlackIpResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def policyid(self):
        """Gets the policyid of this WhiteBlackIpResponseBody.

        策略id

        :return: The policyid of this WhiteBlackIpResponseBody.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this WhiteBlackIpResponseBody.

        策略id

        :param policyid: The policyid of this WhiteBlackIpResponseBody.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def timestamp(self):
        """Gets the timestamp of this WhiteBlackIpResponseBody.

        创建规则的时间戳（毫秒）

        :return: The timestamp of this WhiteBlackIpResponseBody.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WhiteBlackIpResponseBody.

        创建规则的时间戳（毫秒）

        :param timestamp: The timestamp of this WhiteBlackIpResponseBody.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        """Gets the description of this WhiteBlackIpResponseBody.

        规则描述

        :return: The description of this WhiteBlackIpResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WhiteBlackIpResponseBody.

        规则描述

        :param description: The description of this WhiteBlackIpResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this WhiteBlackIpResponseBody.

        规则状态，0：关闭，1：开启

        :return: The status of this WhiteBlackIpResponseBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WhiteBlackIpResponseBody.

        规则状态，0：关闭，1：开启

        :param status: The status of this WhiteBlackIpResponseBody.
        :type status: int
        """
        self._status = status

    @property
    def addr(self):
        """Gets the addr of this WhiteBlackIpResponseBody.

        Ip/Ip段

        :return: The addr of this WhiteBlackIpResponseBody.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this WhiteBlackIpResponseBody.

        Ip/Ip段

        :param addr: The addr of this WhiteBlackIpResponseBody.
        :type addr: str
        """
        self._addr = addr

    @property
    def white(self):
        """Gets the white of this WhiteBlackIpResponseBody.

        防护动作：  - 0拦截  - 1放行  - 2仅记录

        :return: The white of this WhiteBlackIpResponseBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this WhiteBlackIpResponseBody.

        防护动作：  - 0拦截  - 1放行  - 2仅记录

        :param white: The white of this WhiteBlackIpResponseBody.
        :type white: int
        """
        self._white = white

    @property
    def ip_group(self):
        """Gets the ip_group of this WhiteBlackIpResponseBody.

        :return: The ip_group of this WhiteBlackIpResponseBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.IpGroup`
        """
        return self._ip_group

    @ip_group.setter
    def ip_group(self, ip_group):
        """Sets the ip_group of this WhiteBlackIpResponseBody.

        :param ip_group: The ip_group of this WhiteBlackIpResponseBody.
        :type ip_group: :class:`huaweicloudsdkwaf.v1.IpGroup`
        """
        self._ip_group = ip_group

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
        if not isinstance(other, WhiteBlackIpResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
