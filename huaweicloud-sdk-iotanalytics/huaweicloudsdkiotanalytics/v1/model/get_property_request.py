# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetPropertyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'dict(str, str)',
        'property_names': 'list[str]'
    }

    attribute_map = {
        'tags': 'tags',
        'property_names': 'property_names'
    }

    def __init__(self, tags=None, property_names=None):
        """GetPropertyRequest

        The model defined in huaweicloud sdk

        :param tags: 对property按指定tags标签进行过滤查询，填入设备标签与标签值，不可为空，例如 {\&quot;deviceId\&quot;: \&quot;id0001\&quot;}
        :type tags: dict(str, str)
        :param property_names: 查询设备的属性名称
        :type property_names: list[str]
        """
        
        

        self._tags = None
        self._property_names = None
        self.discriminator = None

        self.tags = tags
        if property_names is not None:
            self.property_names = property_names

    @property
    def tags(self):
        """Gets the tags of this GetPropertyRequest.

        对property按指定tags标签进行过滤查询，填入设备标签与标签值，不可为空，例如 {\"deviceId\": \"id0001\"}

        :return: The tags of this GetPropertyRequest.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GetPropertyRequest.

        对property按指定tags标签进行过滤查询，填入设备标签与标签值，不可为空，例如 {\"deviceId\": \"id0001\"}

        :param tags: The tags of this GetPropertyRequest.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def property_names(self):
        """Gets the property_names of this GetPropertyRequest.

        查询设备的属性名称

        :return: The property_names of this GetPropertyRequest.
        :rtype: list[str]
        """
        return self._property_names

    @property_names.setter
    def property_names(self, property_names):
        """Sets the property_names of this GetPropertyRequest.

        查询设备的属性名称

        :param property_names: The property_names of this GetPropertyRequest.
        :type property_names: list[str]
        """
        self._property_names = property_names

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
        if not isinstance(other, GetPropertyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
