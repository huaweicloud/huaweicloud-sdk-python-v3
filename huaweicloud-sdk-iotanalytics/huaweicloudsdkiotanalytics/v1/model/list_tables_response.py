# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTablesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tables': 'list[Table]',
        'count': 'int'
    }

    attribute_map = {
        'tables': 'tables',
        'count': 'count'
    }

    def __init__(self, tables=None, count=None):
        """ListTablesResponse

        The model defined in huaweicloud sdk

        :param tables: 表的信息。
        :type tables: list[:class:`huaweicloudsdkiotanalytics.v1.Table`]
        :param count: 数据表总数。
        :type count: int
        """
        
        super(ListTablesResponse, self).__init__()

        self._tables = None
        self._count = None
        self.discriminator = None

        if tables is not None:
            self.tables = tables
        if count is not None:
            self.count = count

    @property
    def tables(self):
        """Gets the tables of this ListTablesResponse.

        表的信息。

        :return: The tables of this ListTablesResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.Table`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this ListTablesResponse.

        表的信息。

        :param tables: The tables of this ListTablesResponse.
        :type tables: list[:class:`huaweicloudsdkiotanalytics.v1.Table`]
        """
        self._tables = tables

    @property
    def count(self):
        """Gets the count of this ListTablesResponse.

        数据表总数。

        :return: The count of this ListTablesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListTablesResponse.

        数据表总数。

        :param count: The count of this ListTablesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListTablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
