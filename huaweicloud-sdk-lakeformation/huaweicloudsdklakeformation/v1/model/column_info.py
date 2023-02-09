# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_name': 'list[str]',
        'filter': 'str'
    }

    attribute_map = {
        'column_name': 'column_name',
        'filter': 'filter'
    }

    def __init__(self, column_name=None, filter=None):
        """ColumnInfo

        The model defined in huaweicloud sdk

        :param column_name: 列名
        :type column_name: list[str]
        :param filter: 是否排除：Include包含,Exclude排除
        :type filter: str
        """
        
        

        self._column_name = None
        self._filter = None
        self.discriminator = None

        self.column_name = column_name
        self.filter = filter

    @property
    def column_name(self):
        """Gets the column_name of this ColumnInfo.

        列名

        :return: The column_name of this ColumnInfo.
        :rtype: list[str]
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ColumnInfo.

        列名

        :param column_name: The column_name of this ColumnInfo.
        :type column_name: list[str]
        """
        self._column_name = column_name

    @property
    def filter(self):
        """Gets the filter of this ColumnInfo.

        是否排除：Include包含,Exclude排除

        :return: The filter of this ColumnInfo.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ColumnInfo.

        是否排除：Include包含,Exclude排除

        :param filter: The filter of this ColumnInfo.
        :type filter: str
        """
        self._filter = filter

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
        if not isinstance(other, ColumnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
