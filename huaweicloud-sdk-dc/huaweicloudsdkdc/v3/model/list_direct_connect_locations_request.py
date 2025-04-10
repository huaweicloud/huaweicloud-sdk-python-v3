# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDirectConnectLocationsRequest:

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
        'sort_key': 'str',
        'sort_dir': 'list[str]',
        'id': 'list[str]',
        'name': 'list[str]',
        'status': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, limit=None, marker=None, sort_key=None, sort_dir=None, id=None, name=None, status=None):
        r"""ListDirectConnectLocationsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~2000。
        :type limit: int
        :param marker: 上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param sort_key: 排序字段。
        :type sort_key: str
        :param sort_dir: 返回结果按照升序(asc)或降序(desc)排列，默认为asc
        :type sort_dir: list[str]
        :param id: 根据资源ID过滤实例
        :type id: list[str]
        :param name: 根据名字过滤查询，可查询多个名字。
        :type name: list[str]
        :param status: 根椐资源状态过滤实例
        :type status: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._name = None
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
        if status is not None:
            self.status = status

    @property
    def limit(self):
        r"""Gets the limit of this ListDirectConnectLocationsRequest.

        每页返回的个数。 取值范围：1~2000。

        :return: The limit of this ListDirectConnectLocationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDirectConnectLocationsRequest.

        每页返回的个数。 取值范围：1~2000。

        :param limit: The limit of this ListDirectConnectLocationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListDirectConnectLocationsRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListDirectConnectLocationsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListDirectConnectLocationsRequest.

        上一页最后一条资源记录的ID，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListDirectConnectLocationsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListDirectConnectLocationsRequest.

        排序字段。

        :return: The sort_key of this ListDirectConnectLocationsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListDirectConnectLocationsRequest.

        排序字段。

        :param sort_key: The sort_key of this ListDirectConnectLocationsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListDirectConnectLocationsRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :return: The sort_dir of this ListDirectConnectLocationsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListDirectConnectLocationsRequest.

        返回结果按照升序(asc)或降序(desc)排列，默认为asc

        :param sort_dir: The sort_dir of this ListDirectConnectLocationsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        r"""Gets the id of this ListDirectConnectLocationsRequest.

        根据资源ID过滤实例

        :return: The id of this ListDirectConnectLocationsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListDirectConnectLocationsRequest.

        根据资源ID过滤实例

        :param id: The id of this ListDirectConnectLocationsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListDirectConnectLocationsRequest.

        根据名字过滤查询，可查询多个名字。

        :return: The name of this ListDirectConnectLocationsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListDirectConnectLocationsRequest.

        根据名字过滤查询，可查询多个名字。

        :param name: The name of this ListDirectConnectLocationsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListDirectConnectLocationsRequest.

        根椐资源状态过滤实例

        :return: The status of this ListDirectConnectLocationsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListDirectConnectLocationsRequest.

        根椐资源状态过滤实例

        :param status: The status of this ListDirectConnectLocationsRequest.
        :type status: list[str]
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
        if not isinstance(other, ListDirectConnectLocationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
