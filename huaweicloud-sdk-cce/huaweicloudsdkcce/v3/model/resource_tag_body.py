# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceTagBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str',
        'resource_id': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'resource_id': 'resourceId',
        'values': 'values'
    }

    def __init__(self, key=None, value=None, resource_id=None, values=None):
        """ResourceTagBody

        The model defined in huaweicloud sdk

        :param key: 资源标签key
        :type key: str
        :param value: 资源标签value
        :type value: str
        :param resource_id: 资源id
        :type resource_id: str
        :param values: 资源值列表
        :type values: list[str]
        """
        
        

        self._key = None
        self._value = None
        self._resource_id = None
        self._values = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if resource_id is not None:
            self.resource_id = resource_id
        if values is not None:
            self.values = values

    @property
    def key(self):
        """Gets the key of this ResourceTagBody.

        资源标签key

        :return: The key of this ResourceTagBody.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ResourceTagBody.

        资源标签key

        :param key: The key of this ResourceTagBody.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this ResourceTagBody.

        资源标签value

        :return: The value of this ResourceTagBody.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ResourceTagBody.

        资源标签value

        :param value: The value of this ResourceTagBody.
        :type value: str
        """
        self._value = value

    @property
    def resource_id(self):
        """Gets the resource_id of this ResourceTagBody.

        资源id

        :return: The resource_id of this ResourceTagBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ResourceTagBody.

        资源id

        :param resource_id: The resource_id of this ResourceTagBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def values(self):
        """Gets the values of this ResourceTagBody.

        资源值列表

        :return: The values of this ResourceTagBody.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ResourceTagBody.

        资源值列表

        :param values: The values of this ResourceTagBody.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, ResourceTagBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
