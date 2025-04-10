# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageOptions:

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
        'default': 'object',
        'valid_at': 'str',
        'empty': 'bool',
        'schema': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'default': 'default',
        'valid_at': 'validAt',
        'empty': 'empty',
        'schema': 'schema',
        'type': 'type'
    }

    def __init__(self, name=None, default=None, valid_at=None, empty=None, schema=None, type=None):
        r"""PackageOptions

        The model defined in huaweicloud sdk

        :param name: 参数名称
        :type name: str
        :param default: 参数默认值，不指定时按默认值生效, 参数类型以实际返回为准，可能为integer,string或者boolean
        :type default: object
        :param valid_at: 参数生效方式  - static：节点创建时生效，后续不可修改 - immediately：节点运行中时可以修改，修改后生效 
        :type valid_at: str
        :param empty: 配置项是否可以为空  - true：配置项为空时，不使用默认值，为空值 - false：配置项为空时，使用默认值 
        :type empty: bool
        :param schema: 参数分类
        :type schema: str
        :param type: 参数类型
        :type type: str
        """
        
        

        self._name = None
        self._default = None
        self._valid_at = None
        self._empty = None
        self._schema = None
        self._type = None
        self.discriminator = None

        self.name = name
        self.default = default
        self.valid_at = valid_at
        self.empty = empty
        self.schema = schema
        self.type = type

    @property
    def name(self):
        r"""Gets the name of this PackageOptions.

        参数名称

        :return: The name of this PackageOptions.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PackageOptions.

        参数名称

        :param name: The name of this PackageOptions.
        :type name: str
        """
        self._name = name

    @property
    def default(self):
        r"""Gets the default of this PackageOptions.

        参数默认值，不指定时按默认值生效, 参数类型以实际返回为准，可能为integer,string或者boolean

        :return: The default of this PackageOptions.
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this PackageOptions.

        参数默认值，不指定时按默认值生效, 参数类型以实际返回为准，可能为integer,string或者boolean

        :param default: The default of this PackageOptions.
        :type default: object
        """
        self._default = default

    @property
    def valid_at(self):
        r"""Gets the valid_at of this PackageOptions.

        参数生效方式  - static：节点创建时生效，后续不可修改 - immediately：节点运行中时可以修改，修改后生效 

        :return: The valid_at of this PackageOptions.
        :rtype: str
        """
        return self._valid_at

    @valid_at.setter
    def valid_at(self, valid_at):
        r"""Sets the valid_at of this PackageOptions.

        参数生效方式  - static：节点创建时生效，后续不可修改 - immediately：节点运行中时可以修改，修改后生效 

        :param valid_at: The valid_at of this PackageOptions.
        :type valid_at: str
        """
        self._valid_at = valid_at

    @property
    def empty(self):
        r"""Gets the empty of this PackageOptions.

        配置项是否可以为空  - true：配置项为空时，不使用默认值，为空值 - false：配置项为空时，使用默认值 

        :return: The empty of this PackageOptions.
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        r"""Sets the empty of this PackageOptions.

        配置项是否可以为空  - true：配置项为空时，不使用默认值，为空值 - false：配置项为空时，使用默认值 

        :param empty: The empty of this PackageOptions.
        :type empty: bool
        """
        self._empty = empty

    @property
    def schema(self):
        r"""Gets the schema of this PackageOptions.

        参数分类

        :return: The schema of this PackageOptions.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this PackageOptions.

        参数分类

        :param schema: The schema of this PackageOptions.
        :type schema: str
        """
        self._schema = schema

    @property
    def type(self):
        r"""Gets the type of this PackageOptions.

        参数类型

        :return: The type of this PackageOptions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PackageOptions.

        参数类型

        :param type: The type of this PackageOptions.
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
        if not isinstance(other, PackageOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
