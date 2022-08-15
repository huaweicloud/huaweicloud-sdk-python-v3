# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWhiteBlackIpRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'addr': 'str',
        'description': 'str',
        'white': 'int',
        'ip_group_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'addr': 'addr',
        'description': 'description',
        'white': 'white',
        'ip_group_id': 'ip_group_id'
    }

    def __init__(self, name=None, addr=None, description=None, white=None, ip_group_id=None):
        """UpdateWhiteBlackIpRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 黑白名单规则名称
        :type name: str
        :param addr: 黑白名单ip地址，需要输入标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16
        :type addr: str
        :param description: 黑白名单规则描述
        :type description: str
        :param white: 防护动作：  - 0 拦截  - 1 放行  - 2 仅记录
        :type white: int
        :param ip_group_id: 创建的Ip地址组id，该参数与addr参数使用一个即可；Ip地址组可在控制台中对象管理-&gt;地址组管理中添加。
        :type ip_group_id: str
        """
        
        

        self._name = None
        self._addr = None
        self._description = None
        self._white = None
        self._ip_group_id = None
        self.discriminator = None

        self.name = name
        if addr is not None:
            self.addr = addr
        if description is not None:
            self.description = description
        self.white = white
        if ip_group_id is not None:
            self.ip_group_id = ip_group_id

    @property
    def name(self):
        """Gets the name of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单规则名称

        :return: The name of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单规则名称

        :param name: The name of this UpdateWhiteBlackIpRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def addr(self):
        """Gets the addr of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单ip地址，需要输入标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16

        :return: The addr of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单ip地址，需要输入标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16

        :param addr: The addr of this UpdateWhiteBlackIpRuleRequestBody.
        :type addr: str
        """
        self._addr = addr

    @property
    def description(self):
        """Gets the description of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单规则描述

        :return: The description of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单规则描述

        :param description: The description of this UpdateWhiteBlackIpRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def white(self):
        """Gets the white of this UpdateWhiteBlackIpRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :return: The white of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this UpdateWhiteBlackIpRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :param white: The white of this UpdateWhiteBlackIpRuleRequestBody.
        :type white: int
        """
        self._white = white

    @property
    def ip_group_id(self):
        """Gets the ip_group_id of this UpdateWhiteBlackIpRuleRequestBody.

        创建的Ip地址组id，该参数与addr参数使用一个即可；Ip地址组可在控制台中对象管理->地址组管理中添加。

        :return: The ip_group_id of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: str
        """
        return self._ip_group_id

    @ip_group_id.setter
    def ip_group_id(self, ip_group_id):
        """Sets the ip_group_id of this UpdateWhiteBlackIpRuleRequestBody.

        创建的Ip地址组id，该参数与addr参数使用一个即可；Ip地址组可在控制台中对象管理->地址组管理中添加。

        :param ip_group_id: The ip_group_id of this UpdateWhiteBlackIpRuleRequestBody.
        :type ip_group_id: str
        """
        self._ip_group_id = ip_group_id

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
        if not isinstance(other, UpdateWhiteBlackIpRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
