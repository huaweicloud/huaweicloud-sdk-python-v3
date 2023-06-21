# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListColumnsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_id': 'str',
        'total_count': 'int',
        'columns': 'list[ColumnsList]'
    }

    attribute_map = {
        'table_id': 'table_id',
        'total_count': 'total_count',
        'columns': 'columns'
    }

    def __init__(self, table_id=None, total_count=None, columns=None):
        """ListColumnsResponse

        The model defined in huaweicloud sdk

        :param table_id: 表id
        :type table_id: str
        :param total_count: 当前表中字段记录数
        :type total_count: int
        :param columns: 字段列表
        :type columns: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnsList`]
        """
        
        super(ListColumnsResponse, self).__init__()

        self._table_id = None
        self._total_count = None
        self._columns = None
        self.discriminator = None

        if table_id is not None:
            self.table_id = table_id
        if total_count is not None:
            self.total_count = total_count
        if columns is not None:
            self.columns = columns

    @property
    def table_id(self):
        """Gets the table_id of this ListColumnsResponse.

        表id

        :return: The table_id of this ListColumnsResponse.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this ListColumnsResponse.

        表id

        :param table_id: The table_id of this ListColumnsResponse.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def total_count(self):
        """Gets the total_count of this ListColumnsResponse.

        当前表中字段记录数

        :return: The total_count of this ListColumnsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListColumnsResponse.

        当前表中字段记录数

        :param total_count: The total_count of this ListColumnsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def columns(self):
        """Gets the columns of this ListColumnsResponse.

        字段列表

        :return: The columns of this ListColumnsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnsList`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this ListColumnsResponse.

        字段列表

        :param columns: The columns of this ListColumnsResponse.
        :type columns: list[:class:`huaweicloudsdkdataartsstudio.v1.ColumnsList`]
        """
        self._columns = columns

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
        if not isinstance(other, ListColumnsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
