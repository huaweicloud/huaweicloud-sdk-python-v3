# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CodeTableFieldVO:

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
        'code_table_id': 'str',
        'ordinal': 'int',
        'name_en': 'str',
        'name_ch': 'str',
        'description': 'str',
        'data_type': 'str',
        'domain_type': 'DataTypeDomainEnum',
        'data_type_extend': 'str',
        'is_unique_key': 'bool',
        'code_table_field_values': 'list[CodeTableFieldValueVO]',
        'count_field_values': 'int'
    }

    attribute_map = {
        'id': 'id',
        'code_table_id': 'code_table_id',
        'ordinal': 'ordinal',
        'name_en': 'name_en',
        'name_ch': 'name_ch',
        'description': 'description',
        'data_type': 'data_type',
        'domain_type': 'domain_type',
        'data_type_extend': 'data_type_extend',
        'is_unique_key': 'is_unique_key',
        'code_table_field_values': 'code_table_field_values',
        'count_field_values': 'count_field_values'
    }

    def __init__(self, id=None, code_table_id=None, ordinal=None, name_en=None, name_ch=None, description=None, data_type=None, domain_type=None, data_type_extend=None, is_unique_key=None, code_table_field_values=None, count_field_values=None):
        r"""CodeTableFieldVO

        The model defined in huaweicloud sdk

        :param id: 码表字段ID，ID字符串。
        :type id: str
        :param code_table_id: 所属码表ID，ID字符串。
        :type code_table_id: str
        :param ordinal: 序号。
        :type ordinal: int
        :param name_en: 字段名，英文。
        :type name_en: str
        :param name_ch: 字段名，中文。
        :type name_ch: str
        :param description: 描述。
        :type description: str
        :param data_type: 字段类型。
        :type data_type: str
        :param domain_type: 
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        :param data_type_extend: 数据类型扩展字段。
        :type data_type_extend: str
        :param is_unique_key: 是否唯一。
        :type is_unique_key: bool
        :param code_table_field_values: 码表属性值。
        :type code_table_field_values: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldValueVO`]
        :param count_field_values: 码表属性值总数。
        :type count_field_values: int
        """
        
        

        self._id = None
        self._code_table_id = None
        self._ordinal = None
        self._name_en = None
        self._name_ch = None
        self._description = None
        self._data_type = None
        self._domain_type = None
        self._data_type_extend = None
        self._is_unique_key = None
        self._code_table_field_values = None
        self._count_field_values = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code_table_id is not None:
            self.code_table_id = code_table_id
        self.ordinal = ordinal
        self.name_en = name_en
        self.name_ch = name_ch
        if description is not None:
            self.description = description
        self.data_type = data_type
        if domain_type is not None:
            self.domain_type = domain_type
        if data_type_extend is not None:
            self.data_type_extend = data_type_extend
        if is_unique_key is not None:
            self.is_unique_key = is_unique_key
        if code_table_field_values is not None:
            self.code_table_field_values = code_table_field_values
        if count_field_values is not None:
            self.count_field_values = count_field_values

    @property
    def id(self):
        r"""Gets the id of this CodeTableFieldVO.

        码表字段ID，ID字符串。

        :return: The id of this CodeTableFieldVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CodeTableFieldVO.

        码表字段ID，ID字符串。

        :param id: The id of this CodeTableFieldVO.
        :type id: str
        """
        self._id = id

    @property
    def code_table_id(self):
        r"""Gets the code_table_id of this CodeTableFieldVO.

        所属码表ID，ID字符串。

        :return: The code_table_id of this CodeTableFieldVO.
        :rtype: str
        """
        return self._code_table_id

    @code_table_id.setter
    def code_table_id(self, code_table_id):
        r"""Sets the code_table_id of this CodeTableFieldVO.

        所属码表ID，ID字符串。

        :param code_table_id: The code_table_id of this CodeTableFieldVO.
        :type code_table_id: str
        """
        self._code_table_id = code_table_id

    @property
    def ordinal(self):
        r"""Gets the ordinal of this CodeTableFieldVO.

        序号。

        :return: The ordinal of this CodeTableFieldVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        r"""Sets the ordinal of this CodeTableFieldVO.

        序号。

        :param ordinal: The ordinal of this CodeTableFieldVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def name_en(self):
        r"""Gets the name_en of this CodeTableFieldVO.

        字段名，英文。

        :return: The name_en of this CodeTableFieldVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this CodeTableFieldVO.

        字段名，英文。

        :param name_en: The name_en of this CodeTableFieldVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_ch(self):
        r"""Gets the name_ch of this CodeTableFieldVO.

        字段名，中文。

        :return: The name_ch of this CodeTableFieldVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        r"""Sets the name_ch of this CodeTableFieldVO.

        字段名，中文。

        :param name_ch: The name_ch of this CodeTableFieldVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def description(self):
        r"""Gets the description of this CodeTableFieldVO.

        描述。

        :return: The description of this CodeTableFieldVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CodeTableFieldVO.

        描述。

        :param description: The description of this CodeTableFieldVO.
        :type description: str
        """
        self._description = description

    @property
    def data_type(self):
        r"""Gets the data_type of this CodeTableFieldVO.

        字段类型。

        :return: The data_type of this CodeTableFieldVO.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this CodeTableFieldVO.

        字段类型。

        :param data_type: The data_type of this CodeTableFieldVO.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def domain_type(self):
        r"""Gets the domain_type of this CodeTableFieldVO.

        :return: The domain_type of this CodeTableFieldVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this CodeTableFieldVO.

        :param domain_type: The domain_type of this CodeTableFieldVO.
        :type domain_type: :class:`huaweicloudsdkdataartsstudio.v1.DataTypeDomainEnum`
        """
        self._domain_type = domain_type

    @property
    def data_type_extend(self):
        r"""Gets the data_type_extend of this CodeTableFieldVO.

        数据类型扩展字段。

        :return: The data_type_extend of this CodeTableFieldVO.
        :rtype: str
        """
        return self._data_type_extend

    @data_type_extend.setter
    def data_type_extend(self, data_type_extend):
        r"""Sets the data_type_extend of this CodeTableFieldVO.

        数据类型扩展字段。

        :param data_type_extend: The data_type_extend of this CodeTableFieldVO.
        :type data_type_extend: str
        """
        self._data_type_extend = data_type_extend

    @property
    def is_unique_key(self):
        r"""Gets the is_unique_key of this CodeTableFieldVO.

        是否唯一。

        :return: The is_unique_key of this CodeTableFieldVO.
        :rtype: bool
        """
        return self._is_unique_key

    @is_unique_key.setter
    def is_unique_key(self, is_unique_key):
        r"""Sets the is_unique_key of this CodeTableFieldVO.

        是否唯一。

        :param is_unique_key: The is_unique_key of this CodeTableFieldVO.
        :type is_unique_key: bool
        """
        self._is_unique_key = is_unique_key

    @property
    def code_table_field_values(self):
        r"""Gets the code_table_field_values of this CodeTableFieldVO.

        码表属性值。

        :return: The code_table_field_values of this CodeTableFieldVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldValueVO`]
        """
        return self._code_table_field_values

    @code_table_field_values.setter
    def code_table_field_values(self, code_table_field_values):
        r"""Sets the code_table_field_values of this CodeTableFieldVO.

        码表属性值。

        :param code_table_field_values: The code_table_field_values of this CodeTableFieldVO.
        :type code_table_field_values: list[:class:`huaweicloudsdkdataartsstudio.v1.CodeTableFieldValueVO`]
        """
        self._code_table_field_values = code_table_field_values

    @property
    def count_field_values(self):
        r"""Gets the count_field_values of this CodeTableFieldVO.

        码表属性值总数。

        :return: The count_field_values of this CodeTableFieldVO.
        :rtype: int
        """
        return self._count_field_values

    @count_field_values.setter
    def count_field_values(self, count_field_values):
        r"""Sets the count_field_values of this CodeTableFieldVO.

        码表属性值总数。

        :param count_field_values: The count_field_values of this CodeTableFieldVO.
        :type count_field_values: int
        """
        self._count_field_values = count_field_values

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
        if not isinstance(other, CodeTableFieldVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
