# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeSitesRequest:

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
        'id': 'list[str]',
        'name': 'list[str]',
        'availability_zone_id': 'list[str]',
        'status': 'list[SiteStatus]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'name': 'name',
        'availability_zone_id': 'availability_zone_id',
        'status': 'status'
    }

    def __init__(self, limit=None, marker=None, sort_key=None, sort_dir=None, id=None, name=None, availability_zone_id=None, status=None):
        """ListEdgeSitesRequest

        The model defined in huaweicloud sdk

        :param limit: 每页的数量
        :type limit: int
        :param marker: 分页标识
        :type marker: str
        :param sort_key: 排序字段
        :type sort_key: list[str]
        :param sort_dir: 排序方向，取值范围： - desc：降序 - acs：升序
        :type sort_dir: list[str]
        :param id: 根据边缘小站ID查询，支持排序
        :type id: list[str]
        :param name: 根据边缘小站名称查询（精确），支持排序
        :type name: list[str]
        :param availability_zone_id: 根据边缘可用区ID查询
        :type availability_zone_id: list[str]
        :param status: 根据边缘小站部署状态查询
        :type status: list[:class:`huaweicloudsdkies.v1.SiteStatus`]
        """
        
        

        self._limit = None
        self._marker = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._name = None
        self._availability_zone_id = None
        self._status = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if status is not None:
            self.status = status

    @property
    def limit(self):
        """Gets the limit of this ListEdgeSitesRequest.

        每页的数量

        :return: The limit of this ListEdgeSitesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEdgeSitesRequest.

        每页的数量

        :param limit: The limit of this ListEdgeSitesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListEdgeSitesRequest.

        分页标识

        :return: The marker of this ListEdgeSitesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListEdgeSitesRequest.

        分页标识

        :param marker: The marker of this ListEdgeSitesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_key(self):
        """Gets the sort_key of this ListEdgeSitesRequest.

        排序字段

        :return: The sort_key of this ListEdgeSitesRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListEdgeSitesRequest.

        排序字段

        :param sort_key: The sort_key of this ListEdgeSitesRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListEdgeSitesRequest.

        排序方向，取值范围： - desc：降序 - acs：升序

        :return: The sort_dir of this ListEdgeSitesRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListEdgeSitesRequest.

        排序方向，取值范围： - desc：降序 - acs：升序

        :param sort_dir: The sort_dir of this ListEdgeSitesRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        """Gets the id of this ListEdgeSitesRequest.

        根据边缘小站ID查询，支持排序

        :return: The id of this ListEdgeSitesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListEdgeSitesRequest.

        根据边缘小站ID查询，支持排序

        :param id: The id of this ListEdgeSitesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListEdgeSitesRequest.

        根据边缘小站名称查询（精确），支持排序

        :return: The name of this ListEdgeSitesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEdgeSitesRequest.

        根据边缘小站名称查询（精确），支持排序

        :param name: The name of this ListEdgeSitesRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this ListEdgeSitesRequest.

        根据边缘可用区ID查询

        :return: The availability_zone_id of this ListEdgeSitesRequest.
        :rtype: list[str]
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this ListEdgeSitesRequest.

        根据边缘可用区ID查询

        :param availability_zone_id: The availability_zone_id of this ListEdgeSitesRequest.
        :type availability_zone_id: list[str]
        """
        self._availability_zone_id = availability_zone_id

    @property
    def status(self):
        """Gets the status of this ListEdgeSitesRequest.

        根据边缘小站部署状态查询

        :return: The status of this ListEdgeSitesRequest.
        :rtype: list[:class:`huaweicloudsdkies.v1.SiteStatus`]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListEdgeSitesRequest.

        根据边缘小站部署状态查询

        :param status: The status of this ListEdgeSitesRequest.
        :type status: list[:class:`huaweicloudsdkies.v1.SiteStatus`]
        """
        self._status = status

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
        if not isinstance(other, ListEdgeSitesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
