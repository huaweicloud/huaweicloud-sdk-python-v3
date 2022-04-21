# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SysTags:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'value': 'str',
        'key': 'str'
    }

    attribute_map = {
        'value': 'value',
        'key': 'key'
    }

    def __init__(self, value=None, key=None):
        """SysTags

        The model defined in huaweicloud sdk

        :param value: 企业项目ID
        :type value: str
        :param key: 该值目前固定为“_sys_enterprise_project_id”
        :type key: str
        """
        
        

        self._value = None
        self._key = None
        self.discriminator = None

        self.value = value
        self.key = key

    @property
    def value(self):
        """Gets the value of this SysTags.

        企业项目ID

        :return: The value of this SysTags.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SysTags.

        企业项目ID

        :param value: The value of this SysTags.
        :type value: str
        """
        self._value = value

    @property
    def key(self):
        """Gets the key of this SysTags.

        该值目前固定为“_sys_enterprise_project_id”

        :return: The key of this SysTags.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SysTags.

        该值目前固定为“_sys_enterprise_project_id”

        :param key: The key of this SysTags.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, SysTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
