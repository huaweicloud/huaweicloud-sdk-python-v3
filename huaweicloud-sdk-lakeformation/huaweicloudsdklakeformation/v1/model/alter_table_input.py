# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlterTableInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alter_params': 'dict(str, str)',
        'table': 'TableInput'
    }

    attribute_map = {
        'alter_params': 'alter_params',
        'table': 'table'
    }

    def __init__(self, alter_params=None, table=None):
        """AlterTableInput

        The model defined in huaweicloud sdk

        :param alter_params: 修改表参数映射信息，支持的参数如下： CASADE: 级联删除列，如果为true则会把partition中的列也删除；如果为false则不会 DO_NOT_UPDATE_STATS: 不更新文件级别统计信息。true则不更新；false则更新。 STATS_GENERATED：记录本次更新的发起者。可填：TASK/USET。具体作用未明确。
        :type alter_params: dict(str, str)
        :param table: 
        :type table: :class:`huaweicloudsdklakeformation.v1.TableInput`
        """
        
        

        self._alter_params = None
        self._table = None
        self.discriminator = None

        if alter_params is not None:
            self.alter_params = alter_params
        self.table = table

    @property
    def alter_params(self):
        """Gets the alter_params of this AlterTableInput.

        修改表参数映射信息，支持的参数如下： CASADE: 级联删除列，如果为true则会把partition中的列也删除；如果为false则不会 DO_NOT_UPDATE_STATS: 不更新文件级别统计信息。true则不更新；false则更新。 STATS_GENERATED：记录本次更新的发起者。可填：TASK/USET。具体作用未明确。

        :return: The alter_params of this AlterTableInput.
        :rtype: dict(str, str)
        """
        return self._alter_params

    @alter_params.setter
    def alter_params(self, alter_params):
        """Sets the alter_params of this AlterTableInput.

        修改表参数映射信息，支持的参数如下： CASADE: 级联删除列，如果为true则会把partition中的列也删除；如果为false则不会 DO_NOT_UPDATE_STATS: 不更新文件级别统计信息。true则不更新；false则更新。 STATS_GENERATED：记录本次更新的发起者。可填：TASK/USET。具体作用未明确。

        :param alter_params: The alter_params of this AlterTableInput.
        :type alter_params: dict(str, str)
        """
        self._alter_params = alter_params

    @property
    def table(self):
        """Gets the table of this AlterTableInput.

        :return: The table of this AlterTableInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.TableInput`
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this AlterTableInput.

        :param table: The table of this AlterTableInput.
        :type table: :class:`huaweicloudsdklakeformation.v1.TableInput`
        """
        self._table = table

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
        if not isinstance(other, AlterTableInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
