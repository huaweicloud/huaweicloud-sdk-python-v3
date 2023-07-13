# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseInfo:

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
        'tables': 'list[TableInfo]',
        'functions': 'list[FunctionInfo]'
    }

    attribute_map = {
        'name': 'name',
        'tables': 'tables',
        'functions': 'functions'
    }

    def __init__(self, name=None, tables=None, functions=None):
        """DatabaseInfo

        The model defined in huaweicloud sdk

        :param name: 数据库名
        :type name: str
        :param tables: 子表信息
        :type tables: list[:class:`huaweicloudsdklakeformation.v1.TableInfo`]
        :param functions: 子方法信息
        :type functions: list[:class:`huaweicloudsdklakeformation.v1.FunctionInfo`]
        """
        
        

        self._name = None
        self._tables = None
        self._functions = None
        self.discriminator = None

        self.name = name
        if tables is not None:
            self.tables = tables
        if functions is not None:
            self.functions = functions

    @property
    def name(self):
        """Gets the name of this DatabaseInfo.

        数据库名

        :return: The name of this DatabaseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatabaseInfo.

        数据库名

        :param name: The name of this DatabaseInfo.
        :type name: str
        """
        self._name = name

    @property
    def tables(self):
        """Gets the tables of this DatabaseInfo.

        子表信息

        :return: The tables of this DatabaseInfo.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.TableInfo`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this DatabaseInfo.

        子表信息

        :param tables: The tables of this DatabaseInfo.
        :type tables: list[:class:`huaweicloudsdklakeformation.v1.TableInfo`]
        """
        self._tables = tables

    @property
    def functions(self):
        """Gets the functions of this DatabaseInfo.

        子方法信息

        :return: The functions of this DatabaseInfo.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.FunctionInfo`]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """Sets the functions of this DatabaseInfo.

        子方法信息

        :param functions: The functions of this DatabaseInfo.
        :type functions: list[:class:`huaweicloudsdklakeformation.v1.FunctionInfo`]
        """
        self._functions = functions

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
        if not isinstance(other, DatabaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
