# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLiveDataDataSourcesV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'data_sources': 'list[LdDatasourceInfo]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'data_sources': 'data_sources'
    }

    def __init__(self, size=None, total=None, data_sources=None):
        """ListLiveDataDataSourcesV2Response

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param data_sources: 数据源列表
        :type data_sources: list[:class:`huaweicloudsdkroma.v2.LdDatasourceInfo`]
        """
        
        super(ListLiveDataDataSourcesV2Response, self).__init__()

        self._size = None
        self._total = None
        self._data_sources = None
        self.discriminator = None

        self.size = size
        self.total = total
        if data_sources is not None:
            self.data_sources = data_sources

    @property
    def size(self):
        """Gets the size of this ListLiveDataDataSourcesV2Response.

        本次返回的列表长度

        :return: The size of this ListLiveDataDataSourcesV2Response.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListLiveDataDataSourcesV2Response.

        本次返回的列表长度

        :param size: The size of this ListLiveDataDataSourcesV2Response.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        """Gets the total of this ListLiveDataDataSourcesV2Response.

        满足条件的记录数

        :return: The total of this ListLiveDataDataSourcesV2Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListLiveDataDataSourcesV2Response.

        满足条件的记录数

        :param total: The total of this ListLiveDataDataSourcesV2Response.
        :type total: int
        """
        self._total = total

    @property
    def data_sources(self):
        """Gets the data_sources of this ListLiveDataDataSourcesV2Response.

        数据源列表

        :return: The data_sources of this ListLiveDataDataSourcesV2Response.
        :rtype: list[:class:`huaweicloudsdkroma.v2.LdDatasourceInfo`]
        """
        return self._data_sources

    @data_sources.setter
    def data_sources(self, data_sources):
        """Sets the data_sources of this ListLiveDataDataSourcesV2Response.

        数据源列表

        :param data_sources: The data_sources of this ListLiveDataDataSourcesV2Response.
        :type data_sources: list[:class:`huaweicloudsdkroma.v2.LdDatasourceInfo`]
        """
        self._data_sources = data_sources

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
        if not isinstance(other, ListLiveDataDataSourcesV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
