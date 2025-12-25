# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModuleFieldVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_module_id': 'str',
        'name': 'str',
        'other': 'str',
        'template_field_id': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'connection_module_id': 'connection_module_id',
        'name': 'name',
        'other': 'other',
        'template_field_id': 'template_field_id',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, connection_module_id=None, name=None, other=None, template_field_id=None, type=None, value=None):
        r"""ModuleFieldVo

        The model defined in huaweicloud sdk

        :param connection_module_id: UUID
        :type connection_module_id: str
        :param name: 名称
        :type name: str
        :param other: 其他信息
        :type other: str
        :param template_field_id: UUID
        :type template_field_id: str
        :param type: 类型
        :type type: str
        :param value: 值
        :type value: str
        """
        
        

        self._connection_module_id = None
        self._name = None
        self._other = None
        self._template_field_id = None
        self._type = None
        self._value = None
        self.discriminator = None

        if connection_module_id is not None:
            self.connection_module_id = connection_module_id
        if name is not None:
            self.name = name
        if other is not None:
            self.other = other
        if template_field_id is not None:
            self.template_field_id = template_field_id
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def connection_module_id(self):
        r"""Gets the connection_module_id of this ModuleFieldVo.

        UUID

        :return: The connection_module_id of this ModuleFieldVo.
        :rtype: str
        """
        return self._connection_module_id

    @connection_module_id.setter
    def connection_module_id(self, connection_module_id):
        r"""Sets the connection_module_id of this ModuleFieldVo.

        UUID

        :param connection_module_id: The connection_module_id of this ModuleFieldVo.
        :type connection_module_id: str
        """
        self._connection_module_id = connection_module_id

    @property
    def name(self):
        r"""Gets the name of this ModuleFieldVo.

        名称

        :return: The name of this ModuleFieldVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModuleFieldVo.

        名称

        :param name: The name of this ModuleFieldVo.
        :type name: str
        """
        self._name = name

    @property
    def other(self):
        r"""Gets the other of this ModuleFieldVo.

        其他信息

        :return: The other of this ModuleFieldVo.
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        r"""Sets the other of this ModuleFieldVo.

        其他信息

        :param other: The other of this ModuleFieldVo.
        :type other: str
        """
        self._other = other

    @property
    def template_field_id(self):
        r"""Gets the template_field_id of this ModuleFieldVo.

        UUID

        :return: The template_field_id of this ModuleFieldVo.
        :rtype: str
        """
        return self._template_field_id

    @template_field_id.setter
    def template_field_id(self, template_field_id):
        r"""Sets the template_field_id of this ModuleFieldVo.

        UUID

        :param template_field_id: The template_field_id of this ModuleFieldVo.
        :type template_field_id: str
        """
        self._template_field_id = template_field_id

    @property
    def type(self):
        r"""Gets the type of this ModuleFieldVo.

        类型

        :return: The type of this ModuleFieldVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ModuleFieldVo.

        类型

        :param type: The type of this ModuleFieldVo.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this ModuleFieldVo.

        值

        :return: The value of this ModuleFieldVo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ModuleFieldVo.

        值

        :param value: The value of this ModuleFieldVo.
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
        if not isinstance(other, ModuleFieldVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
