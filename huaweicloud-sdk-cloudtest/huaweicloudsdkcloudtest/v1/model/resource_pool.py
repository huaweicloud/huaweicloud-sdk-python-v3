# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcePool:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, type=None):
        r"""ResourcePool

        The model defined in huaweicloud sdk

        :param id: 资源池Id，商用版本使用，数据库中对应label字段
        :type id: str
        :param name: 资源池类型，商用版本使用，数据库中对应labelName字段
        :type name: str
        :param type: 资源池类型，商用版本使用，数据库中对应labelType字段
        :type type: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def id(self):
        r"""Gets the id of this ResourcePool.

        资源池Id，商用版本使用，数据库中对应label字段

        :return: The id of this ResourcePool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResourcePool.

        资源池Id，商用版本使用，数据库中对应label字段

        :param id: The id of this ResourcePool.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ResourcePool.

        资源池类型，商用版本使用，数据库中对应labelName字段

        :return: The name of this ResourcePool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResourcePool.

        资源池类型，商用版本使用，数据库中对应labelName字段

        :param name: The name of this ResourcePool.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ResourcePool.

        资源池类型，商用版本使用，数据库中对应labelType字段

        :return: The type of this ResourcePool.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourcePool.

        资源池类型，商用版本使用，数据库中对应labelType字段

        :param type: The type of this ResourcePool.
        :type type: str
        """
        self._type = type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourcePool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
