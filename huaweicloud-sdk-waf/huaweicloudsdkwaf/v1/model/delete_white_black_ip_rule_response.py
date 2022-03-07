# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteWhiteBlackIpRuleResponse(SdkResponse):


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
        'policyid': 'str',
        'name': 'str',
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'addr': 'str',
        'white': 'int'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'name': 'name',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'addr': 'addr',
        'white': 'white'
    }

    def __init__(self, id=None, policyid=None, name=None, timestamp=None, description=None, status=None, addr=None, white=None):
        """DeleteWhiteBlackIpRuleResponse - a model defined in huaweicloud sdk"""
        
        super(DeleteWhiteBlackIpRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._name = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._addr = None
        self._white = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if name is not None:
            self.name = name
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

    @property
    def id(self):
        """Gets the id of this DeleteWhiteBlackIpRuleResponse.

        黑白名单规则id

        :return: The id of this DeleteWhiteBlackIpRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteWhiteBlackIpRuleResponse.

        黑白名单规则id

        :param id: The id of this DeleteWhiteBlackIpRuleResponse.
        :type: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this DeleteWhiteBlackIpRuleResponse.

        策略id

        :return: The policyid of this DeleteWhiteBlackIpRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this DeleteWhiteBlackIpRuleResponse.

        策略id

        :param policyid: The policyid of this DeleteWhiteBlackIpRuleResponse.
        :type: str
        """
        self._policyid = policyid

    @property
    def name(self):
        """Gets the name of this DeleteWhiteBlackIpRuleResponse.

        黑白名单规则名称

        :return: The name of this DeleteWhiteBlackIpRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeleteWhiteBlackIpRuleResponse.

        黑白名单规则名称

        :param name: The name of this DeleteWhiteBlackIpRuleResponse.
        :type: str
        """
        self._name = name

    @property
    def timestamp(self):
        """Gets the timestamp of this DeleteWhiteBlackIpRuleResponse.

        删除规则时间，13位毫秒时间戳

        :return: The timestamp of this DeleteWhiteBlackIpRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DeleteWhiteBlackIpRuleResponse.

        删除规则时间，13位毫秒时间戳

        :param timestamp: The timestamp of this DeleteWhiteBlackIpRuleResponse.
        :type: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        """Gets the description of this DeleteWhiteBlackIpRuleResponse.

        描述

        :return: The description of this DeleteWhiteBlackIpRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeleteWhiteBlackIpRuleResponse.

        描述

        :param description: The description of this DeleteWhiteBlackIpRuleResponse.
        :type: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this DeleteWhiteBlackIpRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this DeleteWhiteBlackIpRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeleteWhiteBlackIpRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this DeleteWhiteBlackIpRuleResponse.
        :type: int
        """
        self._status = status

    @property
    def addr(self):
        """Gets the addr of this DeleteWhiteBlackIpRuleResponse.

        黑白名单ip地址，标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16

        :return: The addr of this DeleteWhiteBlackIpRuleResponse.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this DeleteWhiteBlackIpRuleResponse.

        黑白名单ip地址，标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16

        :param addr: The addr of this DeleteWhiteBlackIpRuleResponse.
        :type: str
        """
        self._addr = addr

    @property
    def white(self):
        """Gets the white of this DeleteWhiteBlackIpRuleResponse.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :return: The white of this DeleteWhiteBlackIpRuleResponse.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this DeleteWhiteBlackIpRuleResponse.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :param white: The white of this DeleteWhiteBlackIpRuleResponse.
        :type: int
        """
        self._white = white

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
        if not isinstance(other, DeleteWhiteBlackIpRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
