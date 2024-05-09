# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableReplConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repl_type': 'str',
        'repl_scope': 'str',
        'tables': 'list[str]'
    }

    attribute_map = {
        'repl_type': 'repl_type',
        'repl_scope': 'repl_scope',
        'tables': 'tables'
    }

    def __init__(self, repl_type=None, repl_scope=None, tables=None):
        """TableReplConfig

        The model defined in huaweicloud sdk

        :param repl_type: 表同步类型。include_tables:白名单,exclude_tables:黑名单。
        :type repl_type: str
        :param repl_scope: 表同步范围。all:全量同步，part:部分同步。
        :type repl_scope: str
        :param tables: 白名单或黑名单的表范围。
        :type tables: list[str]
        """
        
        

        self._repl_type = None
        self._repl_scope = None
        self._tables = None
        self.discriminator = None

        if repl_type is not None:
            self.repl_type = repl_type
        if repl_scope is not None:
            self.repl_scope = repl_scope
        if tables is not None:
            self.tables = tables

    @property
    def repl_type(self):
        """Gets the repl_type of this TableReplConfig.

        表同步类型。include_tables:白名单,exclude_tables:黑名单。

        :return: The repl_type of this TableReplConfig.
        :rtype: str
        """
        return self._repl_type

    @repl_type.setter
    def repl_type(self, repl_type):
        """Sets the repl_type of this TableReplConfig.

        表同步类型。include_tables:白名单,exclude_tables:黑名单。

        :param repl_type: The repl_type of this TableReplConfig.
        :type repl_type: str
        """
        self._repl_type = repl_type

    @property
    def repl_scope(self):
        """Gets the repl_scope of this TableReplConfig.

        表同步范围。all:全量同步，part:部分同步。

        :return: The repl_scope of this TableReplConfig.
        :rtype: str
        """
        return self._repl_scope

    @repl_scope.setter
    def repl_scope(self, repl_scope):
        """Sets the repl_scope of this TableReplConfig.

        表同步范围。all:全量同步，part:部分同步。

        :param repl_scope: The repl_scope of this TableReplConfig.
        :type repl_scope: str
        """
        self._repl_scope = repl_scope

    @property
    def tables(self):
        """Gets the tables of this TableReplConfig.

        白名单或黑名单的表范围。

        :return: The tables of this TableReplConfig.
        :rtype: list[str]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this TableReplConfig.

        白名单或黑名单的表范围。

        :param tables: The tables of this TableReplConfig.
        :type tables: list[str]
        """
        self._tables = tables

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
        if not isinstance(other, TableReplConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
