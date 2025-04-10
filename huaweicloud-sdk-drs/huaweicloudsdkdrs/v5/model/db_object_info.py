# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbObjectInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_db_name': 'str',
        'source_schema_name': 'str',
        'source_table_name': 'str',
        'target_db_name': 'str',
        'target_schema_name': 'str',
        'target_table_name': 'str',
        'has_column_info': 'bool'
    }

    attribute_map = {
        'source_db_name': 'source_db_name',
        'source_schema_name': 'source_schema_name',
        'source_table_name': 'source_table_name',
        'target_db_name': 'target_db_name',
        'target_schema_name': 'target_schema_name',
        'target_table_name': 'target_table_name',
        'has_column_info': 'has_column_info'
    }

    def __init__(self, source_db_name=None, source_schema_name=None, source_table_name=None, target_db_name=None, target_schema_name=None, target_table_name=None, has_column_info=None):
        r"""DbObjectInfo

        The model defined in huaweicloud sdk

        :param source_db_name: 源数据库库名。
        :type source_db_name: str
        :param source_schema_name: 源数据库模式名。
        :type source_schema_name: str
        :param source_table_name: 源数据库表名。
        :type source_table_name: str
        :param target_db_name: 目标数据库库名。
        :type target_db_name: str
        :param target_schema_name: 目标数据库模式名。
        :type target_schema_name: str
        :param target_table_name: 目标数据库表名。
        :type target_table_name: str
        :param has_column_info: 是否有列映射。
        :type has_column_info: bool
        """
        
        

        self._source_db_name = None
        self._source_schema_name = None
        self._source_table_name = None
        self._target_db_name = None
        self._target_schema_name = None
        self._target_table_name = None
        self._has_column_info = None
        self.discriminator = None

        if source_db_name is not None:
            self.source_db_name = source_db_name
        if source_schema_name is not None:
            self.source_schema_name = source_schema_name
        if source_table_name is not None:
            self.source_table_name = source_table_name
        if target_db_name is not None:
            self.target_db_name = target_db_name
        if target_schema_name is not None:
            self.target_schema_name = target_schema_name
        if target_table_name is not None:
            self.target_table_name = target_table_name
        if has_column_info is not None:
            self.has_column_info = has_column_info

    @property
    def source_db_name(self):
        r"""Gets the source_db_name of this DbObjectInfo.

        源数据库库名。

        :return: The source_db_name of this DbObjectInfo.
        :rtype: str
        """
        return self._source_db_name

    @source_db_name.setter
    def source_db_name(self, source_db_name):
        r"""Sets the source_db_name of this DbObjectInfo.

        源数据库库名。

        :param source_db_name: The source_db_name of this DbObjectInfo.
        :type source_db_name: str
        """
        self._source_db_name = source_db_name

    @property
    def source_schema_name(self):
        r"""Gets the source_schema_name of this DbObjectInfo.

        源数据库模式名。

        :return: The source_schema_name of this DbObjectInfo.
        :rtype: str
        """
        return self._source_schema_name

    @source_schema_name.setter
    def source_schema_name(self, source_schema_name):
        r"""Sets the source_schema_name of this DbObjectInfo.

        源数据库模式名。

        :param source_schema_name: The source_schema_name of this DbObjectInfo.
        :type source_schema_name: str
        """
        self._source_schema_name = source_schema_name

    @property
    def source_table_name(self):
        r"""Gets the source_table_name of this DbObjectInfo.

        源数据库表名。

        :return: The source_table_name of this DbObjectInfo.
        :rtype: str
        """
        return self._source_table_name

    @source_table_name.setter
    def source_table_name(self, source_table_name):
        r"""Sets the source_table_name of this DbObjectInfo.

        源数据库表名。

        :param source_table_name: The source_table_name of this DbObjectInfo.
        :type source_table_name: str
        """
        self._source_table_name = source_table_name

    @property
    def target_db_name(self):
        r"""Gets the target_db_name of this DbObjectInfo.

        目标数据库库名。

        :return: The target_db_name of this DbObjectInfo.
        :rtype: str
        """
        return self._target_db_name

    @target_db_name.setter
    def target_db_name(self, target_db_name):
        r"""Sets the target_db_name of this DbObjectInfo.

        目标数据库库名。

        :param target_db_name: The target_db_name of this DbObjectInfo.
        :type target_db_name: str
        """
        self._target_db_name = target_db_name

    @property
    def target_schema_name(self):
        r"""Gets the target_schema_name of this DbObjectInfo.

        目标数据库模式名。

        :return: The target_schema_name of this DbObjectInfo.
        :rtype: str
        """
        return self._target_schema_name

    @target_schema_name.setter
    def target_schema_name(self, target_schema_name):
        r"""Sets the target_schema_name of this DbObjectInfo.

        目标数据库模式名。

        :param target_schema_name: The target_schema_name of this DbObjectInfo.
        :type target_schema_name: str
        """
        self._target_schema_name = target_schema_name

    @property
    def target_table_name(self):
        r"""Gets the target_table_name of this DbObjectInfo.

        目标数据库表名。

        :return: The target_table_name of this DbObjectInfo.
        :rtype: str
        """
        return self._target_table_name

    @target_table_name.setter
    def target_table_name(self, target_table_name):
        r"""Sets the target_table_name of this DbObjectInfo.

        目标数据库表名。

        :param target_table_name: The target_table_name of this DbObjectInfo.
        :type target_table_name: str
        """
        self._target_table_name = target_table_name

    @property
    def has_column_info(self):
        r"""Gets the has_column_info of this DbObjectInfo.

        是否有列映射。

        :return: The has_column_info of this DbObjectInfo.
        :rtype: bool
        """
        return self._has_column_info

    @has_column_info.setter
    def has_column_info(self, has_column_info):
        r"""Sets the has_column_info of this DbObjectInfo.

        是否有列映射。

        :param has_column_info: The has_column_info of this DbObjectInfo.
        :type has_column_info: bool
        """
        self._has_column_info = has_column_info

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
        if not isinstance(other, DbObjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
