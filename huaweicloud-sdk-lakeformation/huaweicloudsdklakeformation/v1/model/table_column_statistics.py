# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableColumnStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_statistics_desc': 'TableColumnStatisticsDescription',
        'column_statistics_objects': 'list[ColumnStatisticsObj]'
    }

    attribute_map = {
        'column_statistics_desc': 'column_statistics_desc',
        'column_statistics_objects': 'column_statistics_objects'
    }

    def __init__(self, column_statistics_desc=None, column_statistics_objects=None):
        """TableColumnStatistics

        The model defined in huaweicloud sdk

        :param column_statistics_desc: 
        :type column_statistics_desc: :class:`huaweicloudsdklakeformation.v1.TableColumnStatisticsDescription`
        :param column_statistics_objects: 列统计信息
        :type column_statistics_objects: list[:class:`huaweicloudsdklakeformation.v1.ColumnStatisticsObj`]
        """
        
        

        self._column_statistics_desc = None
        self._column_statistics_objects = None
        self.discriminator = None

        self.column_statistics_desc = column_statistics_desc
        self.column_statistics_objects = column_statistics_objects

    @property
    def column_statistics_desc(self):
        """Gets the column_statistics_desc of this TableColumnStatistics.

        :return: The column_statistics_desc of this TableColumnStatistics.
        :rtype: :class:`huaweicloudsdklakeformation.v1.TableColumnStatisticsDescription`
        """
        return self._column_statistics_desc

    @column_statistics_desc.setter
    def column_statistics_desc(self, column_statistics_desc):
        """Sets the column_statistics_desc of this TableColumnStatistics.

        :param column_statistics_desc: The column_statistics_desc of this TableColumnStatistics.
        :type column_statistics_desc: :class:`huaweicloudsdklakeformation.v1.TableColumnStatisticsDescription`
        """
        self._column_statistics_desc = column_statistics_desc

    @property
    def column_statistics_objects(self):
        """Gets the column_statistics_objects of this TableColumnStatistics.

        列统计信息

        :return: The column_statistics_objects of this TableColumnStatistics.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.ColumnStatisticsObj`]
        """
        return self._column_statistics_objects

    @column_statistics_objects.setter
    def column_statistics_objects(self, column_statistics_objects):
        """Sets the column_statistics_objects of this TableColumnStatistics.

        列统计信息

        :param column_statistics_objects: The column_statistics_objects of this TableColumnStatistics.
        :type column_statistics_objects: list[:class:`huaweicloudsdklakeformation.v1.ColumnStatisticsObj`]
        """
        self._column_statistics_objects = column_statistics_objects

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
        if not isinstance(other, TableColumnStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
