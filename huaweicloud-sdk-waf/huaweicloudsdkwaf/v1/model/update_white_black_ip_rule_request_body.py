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
        'addr': 'str',
        'description': 'str',
        'white': 'int'
    }

    attribute_map = {
        'addr': 'addr',
        'description': 'description',
        'white': 'white'
    }

    def __init__(self, addr=None, description=None, white=None):
        """UpdateWhiteBlackIpRuleRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._addr = None
        self._description = None
        self._white = None
        self.discriminator = None

        self.addr = addr
        if description is not None:
            self.description = description
        if white is not None:
            self.white = white

    @property
    def addr(self):
        """Gets the addr of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单地址

        :return: The addr of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单地址

        :param addr: The addr of this UpdateWhiteBlackIpRuleRequestBody.
        :type: str
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
        :type: str
        """
        self._description = description

    @property
    def white(self):
        """Gets the white of this UpdateWhiteBlackIpRuleRequestBody.

        设置的ip地址类型，1放行，0拦截，2仅记录

        :return: The white of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this UpdateWhiteBlackIpRuleRequestBody.

        设置的ip地址类型，1放行，0拦截，2仅记录

        :param white: The white of this UpdateWhiteBlackIpRuleRequestBody.
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
        if not isinstance(other, UpdateWhiteBlackIpRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
