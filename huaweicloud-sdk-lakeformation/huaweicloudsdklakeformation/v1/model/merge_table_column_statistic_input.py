# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeTableColumnStatisticInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'merge': 'bool',
        'table_column_statistics': 'TableColumnStatistics'
    }

    attribute_map = {
        'merge': 'merge',
        'table_column_statistics': 'table_column_statistics'
    }

    def __init__(self, merge=None, table_column_statistics=None):
        r"""MergeTableColumnStatisticInput

        The model defined in huaweicloud sdk

        :param merge: 是否是对统计信息的合并操作
        :type merge: bool
        :param table_column_statistics: 
        :type table_column_statistics: :class:`huaweicloudsdklakeformation.v1.TableColumnStatistics`
        """
        
        

        self._merge = None
        self._table_column_statistics = None
        self.discriminator = None

        if merge is not None:
            self.merge = merge
        self.table_column_statistics = table_column_statistics

    @property
    def merge(self):
        r"""Gets the merge of this MergeTableColumnStatisticInput.

        是否是对统计信息的合并操作

        :return: The merge of this MergeTableColumnStatisticInput.
        :rtype: bool
        """
        return self._merge

    @merge.setter
    def merge(self, merge):
        r"""Sets the merge of this MergeTableColumnStatisticInput.

        是否是对统计信息的合并操作

        :param merge: The merge of this MergeTableColumnStatisticInput.
        :type merge: bool
        """
        self._merge = merge

    @property
    def table_column_statistics(self):
        r"""Gets the table_column_statistics of this MergeTableColumnStatisticInput.

        :return: The table_column_statistics of this MergeTableColumnStatisticInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.TableColumnStatistics`
        """
        return self._table_column_statistics

    @table_column_statistics.setter
    def table_column_statistics(self, table_column_statistics):
        r"""Sets the table_column_statistics of this MergeTableColumnStatisticInput.

        :param table_column_statistics: The table_column_statistics of this MergeTableColumnStatisticInput.
        :type table_column_statistics: :class:`huaweicloudsdklakeformation.v1.TableColumnStatistics`
        """
        self._table_column_statistics = table_column_statistics

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
        if not isinstance(other, MergeTableColumnStatisticInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
