# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TablesConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'table_config': 'str'
    }

    attribute_map = {
        'table_name': 'table_name',
        'table_config': 'table_config'
    }

    def __init__(self, table_name=None, table_config=None):
        """TablesConfig

        The model defined in huaweicloud sdk

        :param table_name: 表名。
        :type table_name: str
        :param table_config: 表配置值。
        :type table_config: str
        """
        
        

        self._table_name = None
        self._table_config = None
        self.discriminator = None

        if table_name is not None:
            self.table_name = table_name
        if table_config is not None:
            self.table_config = table_config

    @property
    def table_name(self):
        """Gets the table_name of this TablesConfig.

        表名。

        :return: The table_name of this TablesConfig.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this TablesConfig.

        表名。

        :param table_name: The table_name of this TablesConfig.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def table_config(self):
        """Gets the table_config of this TablesConfig.

        表配置值。

        :return: The table_config of this TablesConfig.
        :rtype: str
        """
        return self._table_config

    @table_config.setter
    def table_config(self, table_config):
        """Sets the table_config of this TablesConfig.

        表配置值。

        :param table_config: The table_config of this TablesConfig.
        :type table_config: str
        """
        self._table_config = table_config

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
        if not isinstance(other, TablesConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
