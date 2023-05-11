# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagValuesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'key': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'limit': 'limit',
        'marker': 'marker',
        'key': 'key'
    }

    def __init__(self, region_id=None, limit=None, marker=None, key=None):
        """ListTagValuesRequest

        The model defined in huaweicloud sdk

        :param region_id: 区域ID
        :type region_id: str
        :param limit: 查询记录数。 最小为1，最大为200，未输入时默认为200。
        :type limit: int
        :param marker: 分页位置标识（索引）。 从marker指定索引的下一条数据开始查询。 说明： 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据响应体中marker值配入此参数，当返回的next_marker为空时表示查询到最后一页。
        :type marker: str
        :param key: 标签键
        :type key: str
        """
        
        

        self._region_id = None
        self._limit = None
        self._marker = None
        self._key = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        self.key = key

    @property
    def region_id(self):
        """Gets the region_id of this ListTagValuesRequest.

        区域ID

        :return: The region_id of this ListTagValuesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListTagValuesRequest.

        区域ID

        :param region_id: The region_id of this ListTagValuesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def limit(self):
        """Gets the limit of this ListTagValuesRequest.

        查询记录数。 最小为1，最大为200，未输入时默认为200。

        :return: The limit of this ListTagValuesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTagValuesRequest.

        查询记录数。 最小为1，最大为200，未输入时默认为200。

        :param limit: The limit of this ListTagValuesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListTagValuesRequest.

        分页位置标识（索引）。 从marker指定索引的下一条数据开始查询。 说明： 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据响应体中marker值配入此参数，当返回的next_marker为空时表示查询到最后一页。

        :return: The marker of this ListTagValuesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListTagValuesRequest.

        分页位置标识（索引）。 从marker指定索引的下一条数据开始查询。 说明： 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据响应体中marker值配入此参数，当返回的next_marker为空时表示查询到最后一页。

        :param marker: The marker of this ListTagValuesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def key(self):
        """Gets the key of this ListTagValuesRequest.

        标签键

        :return: The key of this ListTagValuesRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ListTagValuesRequest.

        标签键

        :param key: The key of this ListTagValuesRequest.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, ListTagValuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
