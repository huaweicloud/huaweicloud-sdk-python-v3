# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EntityDto:

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
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, name=None, id=None, type=None):
        r"""EntityDto

        The model defined in huaweicloud sdk

        :param name: 实体的名称。
        :type name: str
        :param id: 实体的唯一标识符（ID）。
        :type id: str
        :param type: 实体的类型。account：账号；organizational_unit：组织单元；root：根。
        :type type: str
        """
        
        

        self._name = None
        self._id = None
        self._type = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.type = type

    @property
    def name(self):
        r"""Gets the name of this EntityDto.

        实体的名称。

        :return: The name of this EntityDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EntityDto.

        实体的名称。

        :param name: The name of this EntityDto.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this EntityDto.

        实体的唯一标识符（ID）。

        :return: The id of this EntityDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EntityDto.

        实体的唯一标识符（ID）。

        :param id: The id of this EntityDto.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this EntityDto.

        实体的类型。account：账号；organizational_unit：组织单元；root：根。

        :return: The type of this EntityDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EntityDto.

        实体的类型。account：账号；organizational_unit：组织单元；root：根。

        :param type: The type of this EntityDto.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, EntityDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
