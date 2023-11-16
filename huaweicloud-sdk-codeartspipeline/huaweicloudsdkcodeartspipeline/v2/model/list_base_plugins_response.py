# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBasePluginsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'total': 'int',
        'data': 'list[PageInfoOptionalSinglePluginVOData]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total',
        'data': 'data'
    }

    def __init__(self, offset=None, limit=None, total=None, data=None):
        """ListBasePluginsResponse

        The model defined in huaweicloud sdk

        :param offset: 偏移
        :type offset: int
        :param limit: 大小
        :type limit: int
        :param total: 总数
        :type total: int
        :param data: 结果集
        :type data: list[:class:`huaweicloudsdkcodeartspipeline.v2.PageInfoOptionalSinglePluginVOData`]
        """
        
        super(ListBasePluginsResponse, self).__init__()

        self._offset = None
        self._limit = None
        self._total = None
        self._data = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if data is not None:
            self.data = data

    @property
    def offset(self):
        """Gets the offset of this ListBasePluginsResponse.

        偏移

        :return: The offset of this ListBasePluginsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBasePluginsResponse.

        偏移

        :param offset: The offset of this ListBasePluginsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListBasePluginsResponse.

        大小

        :return: The limit of this ListBasePluginsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBasePluginsResponse.

        大小

        :param limit: The limit of this ListBasePluginsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        """Gets the total of this ListBasePluginsResponse.

        总数

        :return: The total of this ListBasePluginsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListBasePluginsResponse.

        总数

        :param total: The total of this ListBasePluginsResponse.
        :type total: int
        """
        self._total = total

    @property
    def data(self):
        """Gets the data of this ListBasePluginsResponse.

        结果集

        :return: The data of this ListBasePluginsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PageInfoOptionalSinglePluginVOData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListBasePluginsResponse.

        结果集

        :param data: The data of this ListBasePluginsResponse.
        :type data: list[:class:`huaweicloudsdkcodeartspipeline.v2.PageInfoOptionalSinglePluginVOData`]
        """
        self._data = data

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
        if not isinstance(other, ListBasePluginsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
