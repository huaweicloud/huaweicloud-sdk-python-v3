# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataconnectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'max_records': 'int',
        'data_connection_lists': 'list[ApigDataSourceView]'
    }

    attribute_map = {
        'count': 'count',
        'max_records': 'max_records',
        'data_connection_lists': 'data_connection_lists'
    }

    def __init__(self, count=None, max_records=None, data_connection_lists=None):
        """ListDataconnectionsResponse

        The model defined in huaweicloud sdk

        :param count: 当前分页返回记录数
        :type count: int
        :param max_records: 返回记录总数，一个工作空间最多只能创建50条数据连接
        :type max_records: int
        :param data_connection_lists: 返回数据连接列表
        :type data_connection_lists: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigDataSourceView`]
        """
        
        super(ListDataconnectionsResponse, self).__init__()

        self._count = None
        self._max_records = None
        self._data_connection_lists = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if max_records is not None:
            self.max_records = max_records
        if data_connection_lists is not None:
            self.data_connection_lists = data_connection_lists

    @property
    def count(self):
        """Gets the count of this ListDataconnectionsResponse.

        当前分页返回记录数

        :return: The count of this ListDataconnectionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDataconnectionsResponse.

        当前分页返回记录数

        :param count: The count of this ListDataconnectionsResponse.
        :type count: int
        """
        self._count = count

    @property
    def max_records(self):
        """Gets the max_records of this ListDataconnectionsResponse.

        返回记录总数，一个工作空间最多只能创建50条数据连接

        :return: The max_records of this ListDataconnectionsResponse.
        :rtype: int
        """
        return self._max_records

    @max_records.setter
    def max_records(self, max_records):
        """Sets the max_records of this ListDataconnectionsResponse.

        返回记录总数，一个工作空间最多只能创建50条数据连接

        :param max_records: The max_records of this ListDataconnectionsResponse.
        :type max_records: int
        """
        self._max_records = max_records

    @property
    def data_connection_lists(self):
        """Gets the data_connection_lists of this ListDataconnectionsResponse.

        返回数据连接列表

        :return: The data_connection_lists of this ListDataconnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigDataSourceView`]
        """
        return self._data_connection_lists

    @data_connection_lists.setter
    def data_connection_lists(self, data_connection_lists):
        """Sets the data_connection_lists of this ListDataconnectionsResponse.

        返回数据连接列表

        :param data_connection_lists: The data_connection_lists of this ListDataconnectionsResponse.
        :type data_connection_lists: list[:class:`huaweicloudsdkdataartsstudio.v1.ApigDataSourceView`]
        """
        self._data_connection_lists = data_connection_lists

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
        if not isinstance(other, ListDataconnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
