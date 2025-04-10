# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseColumnDto:

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
        'type': 'ColumnType',
        'description': 'str',
        'nullable': 'bool',
        'primary': 'bool',
        'searchable': 'bool',
        'unique': 'bool',
        'tips': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'nullable': 'nullable',
        'primary': 'primary',
        'searchable': 'searchable',
        'unique': 'unique',
        'tips': 'tips'
    }

    def __init__(self, name=None, type=None, description=None, nullable=None, primary=None, searchable=None, unique=None, tips=None):
        r"""DatabaseColumnDto

        The model defined in huaweicloud sdk

        :param name: 列名
        :type name: str
        :param type: 
        :type type: :class:`huaweicloudsdkeihealth.v1.ColumnType`
        :param description: 列描述信息
        :type description: str
        :param nullable: 列是否允许为空
        :type nullable: bool
        :param primary: 是否作为主键
        :type primary: bool
        :param searchable: 是否可查询
        :type searchable: bool
        :param unique: 是否唯一
        :type unique: bool
        :param tips: 查询参数格式的提示信息
        :type tips: str
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._nullable = None
        self._primary = None
        self._searchable = None
        self._unique = None
        self._tips = None
        self.discriminator = None

        self.name = name
        self.type = type
        if description is not None:
            self.description = description
        self.nullable = nullable
        self.primary = primary
        self.searchable = searchable
        self.unique = unique
        if tips is not None:
            self.tips = tips

    @property
    def name(self):
        r"""Gets the name of this DatabaseColumnDto.

        列名

        :return: The name of this DatabaseColumnDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DatabaseColumnDto.

        列名

        :param name: The name of this DatabaseColumnDto.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this DatabaseColumnDto.

        :return: The type of this DatabaseColumnDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ColumnType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DatabaseColumnDto.

        :param type: The type of this DatabaseColumnDto.
        :type type: :class:`huaweicloudsdkeihealth.v1.ColumnType`
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this DatabaseColumnDto.

        列描述信息

        :return: The description of this DatabaseColumnDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DatabaseColumnDto.

        列描述信息

        :param description: The description of this DatabaseColumnDto.
        :type description: str
        """
        self._description = description

    @property
    def nullable(self):
        r"""Gets the nullable of this DatabaseColumnDto.

        列是否允许为空

        :return: The nullable of this DatabaseColumnDto.
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        r"""Sets the nullable of this DatabaseColumnDto.

        列是否允许为空

        :param nullable: The nullable of this DatabaseColumnDto.
        :type nullable: bool
        """
        self._nullable = nullable

    @property
    def primary(self):
        r"""Gets the primary of this DatabaseColumnDto.

        是否作为主键

        :return: The primary of this DatabaseColumnDto.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        r"""Sets the primary of this DatabaseColumnDto.

        是否作为主键

        :param primary: The primary of this DatabaseColumnDto.
        :type primary: bool
        """
        self._primary = primary

    @property
    def searchable(self):
        r"""Gets the searchable of this DatabaseColumnDto.

        是否可查询

        :return: The searchable of this DatabaseColumnDto.
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        r"""Sets the searchable of this DatabaseColumnDto.

        是否可查询

        :param searchable: The searchable of this DatabaseColumnDto.
        :type searchable: bool
        """
        self._searchable = searchable

    @property
    def unique(self):
        r"""Gets the unique of this DatabaseColumnDto.

        是否唯一

        :return: The unique of this DatabaseColumnDto.
        :rtype: bool
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        r"""Sets the unique of this DatabaseColumnDto.

        是否唯一

        :param unique: The unique of this DatabaseColumnDto.
        :type unique: bool
        """
        self._unique = unique

    @property
    def tips(self):
        r"""Gets the tips of this DatabaseColumnDto.

        查询参数格式的提示信息

        :return: The tips of this DatabaseColumnDto.
        :rtype: str
        """
        return self._tips

    @tips.setter
    def tips(self, tips):
        r"""Sets the tips of this DatabaseColumnDto.

        查询参数格式的提示信息

        :param tips: The tips of this DatabaseColumnDto.
        :type tips: str
        """
        self._tips = tips

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
        if not isinstance(other, DatabaseColumnDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
