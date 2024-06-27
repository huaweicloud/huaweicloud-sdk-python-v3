# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChDatabaseTableReplConfigInfo:

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
        'tables': 'list[str]'
    }

    attribute_map = {
        'repl_type': 'repl_type',
        'tables': 'tables'
    }

    def __init__(self, repl_type=None, tables=None):
        """ChDatabaseTableReplConfigInfo

        The model defined in huaweicloud sdk

        :param repl_type: 表同步类型。 取值范围： - white_list：白名单，此时表范围不能为空。 - black_list：黑名单，此时表范围为空则选择所有表。
        :type repl_type: str
        :param tables: 白名单或黑名单的表范围。
        :type tables: list[str]
        """
        
        

        self._repl_type = None
        self._tables = None
        self.discriminator = None

        self.repl_type = repl_type
        self.tables = tables

    @property
    def repl_type(self):
        """Gets the repl_type of this ChDatabaseTableReplConfigInfo.

        表同步类型。 取值范围： - white_list：白名单，此时表范围不能为空。 - black_list：黑名单，此时表范围为空则选择所有表。

        :return: The repl_type of this ChDatabaseTableReplConfigInfo.
        :rtype: str
        """
        return self._repl_type

    @repl_type.setter
    def repl_type(self, repl_type):
        """Sets the repl_type of this ChDatabaseTableReplConfigInfo.

        表同步类型。 取值范围： - white_list：白名单，此时表范围不能为空。 - black_list：黑名单，此时表范围为空则选择所有表。

        :param repl_type: The repl_type of this ChDatabaseTableReplConfigInfo.
        :type repl_type: str
        """
        self._repl_type = repl_type

    @property
    def tables(self):
        """Gets the tables of this ChDatabaseTableReplConfigInfo.

        白名单或黑名单的表范围。

        :return: The tables of this ChDatabaseTableReplConfigInfo.
        :rtype: list[str]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this ChDatabaseTableReplConfigInfo.

        白名单或黑名单的表范围。

        :param tables: The tables of this ChDatabaseTableReplConfigInfo.
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
        if not isinstance(other, ChDatabaseTableReplConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
