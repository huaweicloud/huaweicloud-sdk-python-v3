# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdAndNameAndValueVo:

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
        'value': 'int',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'id': 'id'
    }

    def __init__(self, name=None, value=None, id=None):
        """IdAndNameAndValueVo

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param value: 值
        :type value: int
        :param id: id
        :type id: str
        """
        
        

        self._name = None
        self._value = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this IdAndNameAndValueVo.

        名称

        :return: The name of this IdAndNameAndValueVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdAndNameAndValueVo.

        名称

        :param name: The name of this IdAndNameAndValueVo.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this IdAndNameAndValueVo.

        值

        :return: The value of this IdAndNameAndValueVo.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IdAndNameAndValueVo.

        值

        :param value: The value of this IdAndNameAndValueVo.
        :type value: int
        """
        self._value = value

    @property
    def id(self):
        """Gets the id of this IdAndNameAndValueVo.

        id

        :return: The id of this IdAndNameAndValueVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdAndNameAndValueVo.

        id

        :param id: The id of this IdAndNameAndValueVo.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, IdAndNameAndValueVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
