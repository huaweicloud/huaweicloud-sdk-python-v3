# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionModuleFieldCreateVo:

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
        'other': 'str',
        'template_field_id': 'str',
        'title': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'other': 'other',
        'template_field_id': 'template_field_id',
        'title': 'title',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, name=None, other=None, template_field_id=None, title=None, type=None, value=None):
        r"""ConnectionModuleFieldCreateVo

        The model defined in huaweicloud sdk

        :param name: 名字
        :type name: str
        :param other: 其他信息
        :type other: str
        :param template_field_id: UUID
        :type template_field_id: str
        :param title: 标题
        :type title: str
        :param type: 类型
        :type type: str
        :param value: 相关值
        :type value: str
        """
        
        

        self._name = None
        self._other = None
        self._template_field_id = None
        self._title = None
        self._type = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if other is not None:
            self.other = other
        if template_field_id is not None:
            self.template_field_id = template_field_id
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def name(self):
        r"""Gets the name of this ConnectionModuleFieldCreateVo.

        名字

        :return: The name of this ConnectionModuleFieldCreateVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConnectionModuleFieldCreateVo.

        名字

        :param name: The name of this ConnectionModuleFieldCreateVo.
        :type name: str
        """
        self._name = name

    @property
    def other(self):
        r"""Gets the other of this ConnectionModuleFieldCreateVo.

        其他信息

        :return: The other of this ConnectionModuleFieldCreateVo.
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        r"""Sets the other of this ConnectionModuleFieldCreateVo.

        其他信息

        :param other: The other of this ConnectionModuleFieldCreateVo.
        :type other: str
        """
        self._other = other

    @property
    def template_field_id(self):
        r"""Gets the template_field_id of this ConnectionModuleFieldCreateVo.

        UUID

        :return: The template_field_id of this ConnectionModuleFieldCreateVo.
        :rtype: str
        """
        return self._template_field_id

    @template_field_id.setter
    def template_field_id(self, template_field_id):
        r"""Sets the template_field_id of this ConnectionModuleFieldCreateVo.

        UUID

        :param template_field_id: The template_field_id of this ConnectionModuleFieldCreateVo.
        :type template_field_id: str
        """
        self._template_field_id = template_field_id

    @property
    def title(self):
        r"""Gets the title of this ConnectionModuleFieldCreateVo.

        标题

        :return: The title of this ConnectionModuleFieldCreateVo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ConnectionModuleFieldCreateVo.

        标题

        :param title: The title of this ConnectionModuleFieldCreateVo.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this ConnectionModuleFieldCreateVo.

        类型

        :return: The type of this ConnectionModuleFieldCreateVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConnectionModuleFieldCreateVo.

        类型

        :param type: The type of this ConnectionModuleFieldCreateVo.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this ConnectionModuleFieldCreateVo.

        相关值

        :return: The value of this ConnectionModuleFieldCreateVo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ConnectionModuleFieldCreateVo.

        相关值

        :param value: The value of this ConnectionModuleFieldCreateVo.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, ConnectionModuleFieldCreateVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
