# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRacksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]',
        'edge_site_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'edge_site_id': 'edge_site_id'
    }

    def __init__(self, limit=None, marker=None, sort_key=None, sort_dir=None, edge_site_id=None):
        r"""ListRacksRequest

        The model defined in huaweicloud sdk

        :param limit: 每页的数量
        :type limit: int
        :param marker: 分页标识
        :type marker: str
        :param sort_key: 排序字段
        :type sort_key: list[str]
        :param sort_dir: 排序方向，取值范围： - desc：降序 - acs：升序
        :type sort_dir: list[str]
        :param edge_site_id: 边缘小站ID
        :type edge_site_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._sort_key = None
        self._sort_dir = None
        self._edge_site_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if edge_site_id is not None:
            self.edge_site_id = edge_site_id

    @property
    def limit(self):
        r"""Gets the limit of this ListRacksRequest.

        每页的数量

        :return: The limit of this ListRacksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRacksRequest.

        每页的数量

        :param limit: The limit of this ListRacksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListRacksRequest.

        分页标识

        :return: The marker of this ListRacksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRacksRequest.

        分页标识

        :param marker: The marker of this ListRacksRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListRacksRequest.

        排序字段

        :return: The sort_key of this ListRacksRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListRacksRequest.

        排序字段

        :param sort_key: The sort_key of this ListRacksRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListRacksRequest.

        排序方向，取值范围： - desc：降序 - acs：升序

        :return: The sort_dir of this ListRacksRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListRacksRequest.

        排序方向，取值范围： - desc：降序 - acs：升序

        :param sort_dir: The sort_dir of this ListRacksRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def edge_site_id(self):
        r"""Gets the edge_site_id of this ListRacksRequest.

        边缘小站ID

        :return: The edge_site_id of this ListRacksRequest.
        :rtype: str
        """
        return self._edge_site_id

    @edge_site_id.setter
    def edge_site_id(self, edge_site_id):
        r"""Sets the edge_site_id of this ListRacksRequest.

        边缘小站ID

        :param edge_site_id: The edge_site_id of this ListRacksRequest.
        :type edge_site_id: str
        """
        self._edge_site_id = edge_site_id

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
        if not isinstance(other, ListRacksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
