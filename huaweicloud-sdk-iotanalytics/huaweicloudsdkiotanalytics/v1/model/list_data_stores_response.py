# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataStoresResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_stores': 'list[GetDataStore]',
        'count': 'int'
    }

    attribute_map = {
        'data_stores': 'data_stores',
        'count': 'count'
    }

    def __init__(self, data_stores=None, count=None):
        r"""ListDataStoresResponse

        The model defined in huaweicloud sdk

        :param data_stores: 数据结构列表
        :type data_stores: list[:class:`huaweicloudsdkiotanalytics.v1.GetDataStore`]
        :param count: 返回的 data-store 数量
        :type count: int
        """
        
        super(ListDataStoresResponse, self).__init__()

        self._data_stores = None
        self._count = None
        self.discriminator = None

        if data_stores is not None:
            self.data_stores = data_stores
        if count is not None:
            self.count = count

    @property
    def data_stores(self):
        r"""Gets the data_stores of this ListDataStoresResponse.

        数据结构列表

        :return: The data_stores of this ListDataStoresResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.GetDataStore`]
        """
        return self._data_stores

    @data_stores.setter
    def data_stores(self, data_stores):
        r"""Sets the data_stores of this ListDataStoresResponse.

        数据结构列表

        :param data_stores: The data_stores of this ListDataStoresResponse.
        :type data_stores: list[:class:`huaweicloudsdkiotanalytics.v1.GetDataStore`]
        """
        self._data_stores = data_stores

    @property
    def count(self):
        r"""Gets the count of this ListDataStoresResponse.

        返回的 data-store 数量

        :return: The count of this ListDataStoresResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListDataStoresResponse.

        返回的 data-store 数量

        :param count: The count of this ListDataStoresResponse.
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
        if not isinstance(other, ListDataStoresResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
