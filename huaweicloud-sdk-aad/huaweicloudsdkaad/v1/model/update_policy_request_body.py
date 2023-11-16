# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicyRequestBody:

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
        'threshold': 'int',
        'description': 'str',
        'udp': 'str'
    }

    attribute_map = {
        'name': 'name',
        'threshold': 'threshold',
        'description': 'description',
        'udp': 'udp'
    }

    def __init__(self, name=None, threshold=None, description=None, udp=None):
        """UpdatePolicyRequestBody

        The model defined in huaweicloud sdk

        :param name: 策略名
        :type name: str
        :param threshold: 清洗阈值
        :type threshold: int
        :param description: 描述
        :type description: str
        :param udp: udp协议封禁。block：封禁，unblock：不封禁
        :type udp: str
        """
        
        

        self._name = None
        self._threshold = None
        self._description = None
        self._udp = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if threshold is not None:
            self.threshold = threshold
        if description is not None:
            self.description = description
        if udp is not None:
            self.udp = udp

    @property
    def name(self):
        """Gets the name of this UpdatePolicyRequestBody.

        策略名

        :return: The name of this UpdatePolicyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatePolicyRequestBody.

        策略名

        :param name: The name of this UpdatePolicyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def threshold(self):
        """Gets the threshold of this UpdatePolicyRequestBody.

        清洗阈值

        :return: The threshold of this UpdatePolicyRequestBody.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this UpdatePolicyRequestBody.

        清洗阈值

        :param threshold: The threshold of this UpdatePolicyRequestBody.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def description(self):
        """Gets the description of this UpdatePolicyRequestBody.

        描述

        :return: The description of this UpdatePolicyRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePolicyRequestBody.

        描述

        :param description: The description of this UpdatePolicyRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def udp(self):
        """Gets the udp of this UpdatePolicyRequestBody.

        udp协议封禁。block：封禁，unblock：不封禁

        :return: The udp of this UpdatePolicyRequestBody.
        :rtype: str
        """
        return self._udp

    @udp.setter
    def udp(self, udp):
        """Sets the udp of this UpdatePolicyRequestBody.

        udp协议封禁。block：封禁，unblock：不封禁

        :param udp: The udp of this UpdatePolicyRequestBody.
        :type udp: str
        """
        self._udp = udp

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
        if not isinstance(other, UpdatePolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
