# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceTagObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, resource_id=None, key=None, value=None):
        """ResourceTagObject

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID，不同资源（节点，部署，配置项，密钥）有不同的资源ID
        :type resource_id: str
        :param key: 标签键，最大长度36个字符。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”
        :type key: str
        :param value: 标签值，每个值最大长度43个字符，删除时如果value有值按照key/value删除，如果value没值，则按照key删除。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”
        :type value: str
        """
        
        

        self._resource_id = None
        self._key = None
        self._value = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def resource_id(self):
        """Gets the resource_id of this ResourceTagObject.

        资源ID，不同资源（节点，部署，配置项，密钥）有不同的资源ID

        :return: The resource_id of this ResourceTagObject.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ResourceTagObject.

        资源ID，不同资源（节点，部署，配置项，密钥）有不同的资源ID

        :param resource_id: The resource_id of this ResourceTagObject.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def key(self):
        """Gets the key of this ResourceTagObject.

        标签键，最大长度36个字符。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”

        :return: The key of this ResourceTagObject.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ResourceTagObject.

        标签键，最大长度36个字符。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”

        :param key: The key of this ResourceTagObject.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this ResourceTagObject.

        标签值，每个值最大长度43个字符，删除时如果value有值按照key/value删除，如果value没值，则按照key删除。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”

        :return: The value of this ResourceTagObject.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ResourceTagObject.

        标签值，每个值最大长度43个字符，删除时如果value有值按照key/value删除，如果value没值，则按照key删除。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”

        :param value: The value of this ResourceTagObject.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, ResourceTagObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
