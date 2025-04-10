# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogtanksRequest:

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
        'id': 'str',
        'status': 'str',
        'resource_ids': 'list[str]',
        'resource_type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'status': 'status',
        'resource_ids': 'resource_ids',
        'resource_type': 'resource_type'
    }

    def __init__(self, limit=None, marker=None, id=None, status=None, resource_ids=None, resource_type=None):
        r"""ListLogtanksRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询每页的资源个数。如果不设置，则默认为500。
        :type limit: int
        :param marker: 分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。
        :type marker: str
        :param id: 资源ID。
        :type id: str
        :param status: 配置状态，可选范围: - ACTIVE：运行中 - PENDING：待定 - ERROR：错误 - DELETING：正在删除
        :type status: str
        :param resource_ids: 资源ID列表。
        :type resource_ids: list[str]
        :param resource_type: 关联云日志的资源类型。
        :type resource_type: str
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._status = None
        self._resource_ids = None
        self._resource_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def limit(self):
        r"""Gets the limit of this ListLogtanksRequest.

        分页查询每页的资源个数。如果不设置，则默认为500。

        :return: The limit of this ListLogtanksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLogtanksRequest.

        分页查询每页的资源个数。如果不设置，则默认为500。

        :param limit: The limit of this ListLogtanksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListLogtanksRequest.

        分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。

        :return: The marker of this ListLogtanksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListLogtanksRequest.

        分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。

        :param marker: The marker of this ListLogtanksRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListLogtanksRequest.

        资源ID。

        :return: The id of this ListLogtanksRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListLogtanksRequest.

        资源ID。

        :param id: The id of this ListLogtanksRequest.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ListLogtanksRequest.

        配置状态，可选范围: - ACTIVE：运行中 - PENDING：待定 - ERROR：错误 - DELETING：正在删除

        :return: The status of this ListLogtanksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListLogtanksRequest.

        配置状态，可选范围: - ACTIVE：运行中 - PENDING：待定 - ERROR：错误 - DELETING：正在删除

        :param status: The status of this ListLogtanksRequest.
        :type status: str
        """
        self._status = status

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this ListLogtanksRequest.

        资源ID列表。

        :return: The resource_ids of this ListLogtanksRequest.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this ListLogtanksRequest.

        资源ID列表。

        :param resource_ids: The resource_ids of this ListLogtanksRequest.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListLogtanksRequest.

        关联云日志的资源类型。

        :return: The resource_type of this ListLogtanksRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListLogtanksRequest.

        关联云日志的资源类型。

        :param resource_type: The resource_type of this ListLogtanksRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ListLogtanksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
