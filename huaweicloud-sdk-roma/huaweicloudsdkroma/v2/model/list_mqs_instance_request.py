# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMqsInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'include_internal': 'str'
    }

    attribute_map = {
        'include_internal': 'include_internal'
    }

    def __init__(self, include_internal=None):
        """ListMqsInstanceRequest

        The model defined in huaweicloud sdk

        :param include_internal: 是否包含内部的实例。include_internal参数必须为true。
        :type include_internal: str
        """
        
        

        self._include_internal = None
        self.discriminator = None

        self.include_internal = include_internal

    @property
    def include_internal(self):
        """Gets the include_internal of this ListMqsInstanceRequest.

        是否包含内部的实例。include_internal参数必须为true。

        :return: The include_internal of this ListMqsInstanceRequest.
        :rtype: str
        """
        return self._include_internal

    @include_internal.setter
    def include_internal(self, include_internal):
        """Sets the include_internal of this ListMqsInstanceRequest.

        是否包含内部的实例。include_internal参数必须为true。

        :param include_internal: The include_internal of this ListMqsInstanceRequest.
        :type include_internal: str
        """
        self._include_internal = include_internal

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
        if not isinstance(other, ListMqsInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
