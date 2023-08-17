# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentStorage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'name': 'str',
        'parameters': 'ComponentStorageParameters',
        'mounts': 'list[ComponentMount]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'parameters': 'parameters',
        'mounts': 'mounts'
    }

    def __init__(self, type=None, name=None, parameters=None, mounts=None):
        """ComponentStorage

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param name: 存储盘的名字
        :type name: str
        :param parameters: 
        :type parameters: :class:`huaweicloudsdkservicestage.v3.ComponentStorageParameters`
        :param mounts: 
        :type mounts: list[:class:`huaweicloudsdkservicestage.v3.ComponentMount`]
        """
        
        

        self._type = None
        self._name = None
        self._parameters = None
        self._mounts = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.parameters = parameters
        self.mounts = mounts

    @property
    def type(self):
        """Gets the type of this ComponentStorage.

        :return: The type of this ComponentStorage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComponentStorage.

        :param type: The type of this ComponentStorage.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ComponentStorage.

        存储盘的名字

        :return: The name of this ComponentStorage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentStorage.

        存储盘的名字

        :param name: The name of this ComponentStorage.
        :type name: str
        """
        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this ComponentStorage.

        :return: The parameters of this ComponentStorage.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentStorageParameters`
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ComponentStorage.

        :param parameters: The parameters of this ComponentStorage.
        :type parameters: :class:`huaweicloudsdkservicestage.v3.ComponentStorageParameters`
        """
        self._parameters = parameters

    @property
    def mounts(self):
        """Gets the mounts of this ComponentStorage.

        :return: The mounts of this ComponentStorage.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentMount`]
        """
        return self._mounts

    @mounts.setter
    def mounts(self, mounts):
        """Sets the mounts of this ComponentStorage.

        :param mounts: The mounts of this ComponentStorage.
        :type mounts: list[:class:`huaweicloudsdkservicestage.v3.ComponentMount`]
        """
        self._mounts = mounts

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
        if not isinstance(other, ComponentStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
