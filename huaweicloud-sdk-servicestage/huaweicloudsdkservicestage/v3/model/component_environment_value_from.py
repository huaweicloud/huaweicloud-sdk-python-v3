# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentEnvironmentValueFrom:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reference_type': 'str',
        'name': 'str',
        'key': 'str',
        'optional': 'bool'
    }

    attribute_map = {
        'reference_type': 'reference_type',
        'name': 'name',
        'key': 'key',
        'optional': 'optional'
    }

    def __init__(self, reference_type=None, name=None, key=None, optional=None):
        """ComponentEnvironmentValueFrom

        The model defined in huaweicloud sdk

        :param reference_type: 
        :type reference_type: str
        :param name: configmap或者secret的名字
        :type name: str
        :param key: configmap或者secret的key
        :type key: str
        :param optional: configmap或者secret或者他们的key是否必须存在
        :type optional: bool
        """
        
        

        self._reference_type = None
        self._name = None
        self._key = None
        self._optional = None
        self.discriminator = None

        self.reference_type = reference_type
        self.name = name
        if key is not None:
            self.key = key
        if optional is not None:
            self.optional = optional

    @property
    def reference_type(self):
        """Gets the reference_type of this ComponentEnvironmentValueFrom.

        :return: The reference_type of this ComponentEnvironmentValueFrom.
        :rtype: str
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """Sets the reference_type of this ComponentEnvironmentValueFrom.

        :param reference_type: The reference_type of this ComponentEnvironmentValueFrom.
        :type reference_type: str
        """
        self._reference_type = reference_type

    @property
    def name(self):
        """Gets the name of this ComponentEnvironmentValueFrom.

        configmap或者secret的名字

        :return: The name of this ComponentEnvironmentValueFrom.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentEnvironmentValueFrom.

        configmap或者secret的名字

        :param name: The name of this ComponentEnvironmentValueFrom.
        :type name: str
        """
        self._name = name

    @property
    def key(self):
        """Gets the key of this ComponentEnvironmentValueFrom.

        configmap或者secret的key

        :return: The key of this ComponentEnvironmentValueFrom.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ComponentEnvironmentValueFrom.

        configmap或者secret的key

        :param key: The key of this ComponentEnvironmentValueFrom.
        :type key: str
        """
        self._key = key

    @property
    def optional(self):
        """Gets the optional of this ComponentEnvironmentValueFrom.

        configmap或者secret或者他们的key是否必须存在

        :return: The optional of this ComponentEnvironmentValueFrom.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this ComponentEnvironmentValueFrom.

        configmap或者secret或者他们的key是否必须存在

        :param optional: The optional of this ComponentEnvironmentValueFrom.
        :type optional: bool
        """
        self._optional = optional

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
        if not isinstance(other, ComponentEnvironmentValueFrom):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
