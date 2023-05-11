# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlserverDatabaseForCreation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str'
    }

    attribute_map = {
        'name': 'name'
    }

    def __init__(self, name=None):
        """SqlserverDatabaseForCreation

        The model defined in huaweicloud sdk

        :param name: 数据库名称。 数据库名称长度可在1～64个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符，且不能以RDS for SQL Server系统库开头或结尾。 RDS for SQL Server系统库包括master，msdb，model，tempdb，resource以及rdsadmin。
        :type name: str
        """
        
        

        self._name = None
        self.discriminator = None

        self.name = name

    @property
    def name(self):
        """Gets the name of this SqlserverDatabaseForCreation.

        数据库名称。 数据库名称长度可在1～64个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符，且不能以RDS for SQL Server系统库开头或结尾。 RDS for SQL Server系统库包括master，msdb，model，tempdb，resource以及rdsadmin。

        :return: The name of this SqlserverDatabaseForCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SqlserverDatabaseForCreation.

        数据库名称。 数据库名称长度可在1～64个字符之间，由字母、数字、中划线或下划线组成，不能包含其他特殊字符，且不能以RDS for SQL Server系统库开头或结尾。 RDS for SQL Server系统库包括master，msdb，model，tempdb，resource以及rdsadmin。

        :param name: The name of this SqlserverDatabaseForCreation.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, SqlserverDatabaseForCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
