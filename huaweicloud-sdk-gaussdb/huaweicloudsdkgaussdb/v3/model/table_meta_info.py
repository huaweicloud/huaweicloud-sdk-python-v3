# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableMetaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_type': 'str',
        'extra': 'str',
        'is_nullable': 'str',
        'column_default': 'str',
        'column_key': 'str',
        'column_name': 'str'
    }

    attribute_map = {
        'column_type': 'column_type',
        'extra': 'extra',
        'is_nullable': 'is_nullable',
        'column_default': 'column_default',
        'column_key': 'column_key',
        'column_name': 'column_name'
    }

    def __init__(self, column_type=None, extra=None, is_nullable=None, column_default=None, column_key=None, column_name=None):
        r"""TableMetaInfo

        The model defined in huaweicloud sdk

        :param column_type: 列的数据类型
        :type column_type: str
        :param extra: 额外的信息，例如是否是自动递增列
        :type extra: str
        :param is_nullable: 是否允许为NULL
        :type is_nullable: str
        :param column_default: 列的默认值
        :type column_default: str
        :param column_key: 是否是索引列
        :type column_key: str
        :param column_name: 列名
        :type column_name: str
        """
        
        

        self._column_type = None
        self._extra = None
        self._is_nullable = None
        self._column_default = None
        self._column_key = None
        self._column_name = None
        self.discriminator = None

        if column_type is not None:
            self.column_type = column_type
        if extra is not None:
            self.extra = extra
        if is_nullable is not None:
            self.is_nullable = is_nullable
        if column_default is not None:
            self.column_default = column_default
        if column_key is not None:
            self.column_key = column_key
        if column_name is not None:
            self.column_name = column_name

    @property
    def column_type(self):
        r"""Gets the column_type of this TableMetaInfo.

        列的数据类型

        :return: The column_type of this TableMetaInfo.
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        r"""Sets the column_type of this TableMetaInfo.

        列的数据类型

        :param column_type: The column_type of this TableMetaInfo.
        :type column_type: str
        """
        self._column_type = column_type

    @property
    def extra(self):
        r"""Gets the extra of this TableMetaInfo.

        额外的信息，例如是否是自动递增列

        :return: The extra of this TableMetaInfo.
        :rtype: str
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        r"""Sets the extra of this TableMetaInfo.

        额外的信息，例如是否是自动递增列

        :param extra: The extra of this TableMetaInfo.
        :type extra: str
        """
        self._extra = extra

    @property
    def is_nullable(self):
        r"""Gets the is_nullable of this TableMetaInfo.

        是否允许为NULL

        :return: The is_nullable of this TableMetaInfo.
        :rtype: str
        """
        return self._is_nullable

    @is_nullable.setter
    def is_nullable(self, is_nullable):
        r"""Sets the is_nullable of this TableMetaInfo.

        是否允许为NULL

        :param is_nullable: The is_nullable of this TableMetaInfo.
        :type is_nullable: str
        """
        self._is_nullable = is_nullable

    @property
    def column_default(self):
        r"""Gets the column_default of this TableMetaInfo.

        列的默认值

        :return: The column_default of this TableMetaInfo.
        :rtype: str
        """
        return self._column_default

    @column_default.setter
    def column_default(self, column_default):
        r"""Sets the column_default of this TableMetaInfo.

        列的默认值

        :param column_default: The column_default of this TableMetaInfo.
        :type column_default: str
        """
        self._column_default = column_default

    @property
    def column_key(self):
        r"""Gets the column_key of this TableMetaInfo.

        是否是索引列

        :return: The column_key of this TableMetaInfo.
        :rtype: str
        """
        return self._column_key

    @column_key.setter
    def column_key(self, column_key):
        r"""Sets the column_key of this TableMetaInfo.

        是否是索引列

        :param column_key: The column_key of this TableMetaInfo.
        :type column_key: str
        """
        self._column_key = column_key

    @property
    def column_name(self):
        r"""Gets the column_name of this TableMetaInfo.

        列名

        :return: The column_name of this TableMetaInfo.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this TableMetaInfo.

        列名

        :param column_name: The column_name of this TableMetaInfo.
        :type column_name: str
        """
        self._column_name = column_name

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
        if not isinstance(other, TableMetaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
