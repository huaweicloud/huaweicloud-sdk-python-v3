# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SelectorConfigBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'all_supported': 'bool',
        'resource_types': 'list[str]'
    }

    attribute_map = {
        'all_supported': 'all_supported',
        'resource_types': 'resource_types'
    }

    def __init__(self, all_supported=None, resource_types=None):
        """SelectorConfigBody

        The model defined in huaweicloud sdk

        :param all_supported: 是否选择所有支持的资源
        :type all_supported: bool
        :param resource_types: 资源类型列表
        :type resource_types: list[str]
        """
        
        

        self._all_supported = None
        self._resource_types = None
        self.discriminator = None

        self.all_supported = all_supported
        self.resource_types = resource_types

    @property
    def all_supported(self):
        """Gets the all_supported of this SelectorConfigBody.

        是否选择所有支持的资源

        :return: The all_supported of this SelectorConfigBody.
        :rtype: bool
        """
        return self._all_supported

    @all_supported.setter
    def all_supported(self, all_supported):
        """Sets the all_supported of this SelectorConfigBody.

        是否选择所有支持的资源

        :param all_supported: The all_supported of this SelectorConfigBody.
        :type all_supported: bool
        """
        self._all_supported = all_supported

    @property
    def resource_types(self):
        """Gets the resource_types of this SelectorConfigBody.

        资源类型列表

        :return: The resource_types of this SelectorConfigBody.
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """Sets the resource_types of this SelectorConfigBody.

        资源类型列表

        :param resource_types: The resource_types of this SelectorConfigBody.
        :type resource_types: list[str]
        """
        self._resource_types = resource_types

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
        if not isinstance(other, SelectorConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
