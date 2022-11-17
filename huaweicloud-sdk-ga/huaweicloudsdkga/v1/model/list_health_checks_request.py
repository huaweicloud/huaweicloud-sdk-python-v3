# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHealthChecksRequest:

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
        'page_reverse': 'bool',
        'id': 'str',
        'status': 'str',
        'endpoint_group_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'status': 'status',
        'endpoint_group_id': 'endpoint_group_id'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, status=None, endpoint_group_id=None):
        """ListHealthChecksRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询每页的资源个数。如果不设置，则默认为500。
        :type limit: int
        :param marker: 分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。
        :type marker: str
        :param page_reverse: 分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。
        :type page_reverse: bool
        :param id: 资源ID。
        :type id: str
        :param status: 配置状态，可选范围: - ACTIVE：运行中 - PENDING：待定 - ERROR：错误 - DELETING：正在删除
        :type status: str
        :param endpoint_group_id: 终端节点组ID。
        :type endpoint_group_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._status = None
        self._endpoint_group_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if endpoint_group_id is not None:
            self.endpoint_group_id = endpoint_group_id

    @property
    def limit(self):
        """Gets the limit of this ListHealthChecksRequest.

        分页查询每页的资源个数。如果不设置，则默认为500。

        :return: The limit of this ListHealthChecksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHealthChecksRequest.

        分页查询每页的资源个数。如果不设置，则默认为500。

        :param limit: The limit of this ListHealthChecksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListHealthChecksRequest.

        分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。

        :return: The marker of this ListHealthChecksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListHealthChecksRequest.

        分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。

        :param marker: The marker of this ListHealthChecksRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListHealthChecksRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :return: The page_reverse of this ListHealthChecksRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListHealthChecksRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :param page_reverse: The page_reverse of this ListHealthChecksRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListHealthChecksRequest.

        资源ID。

        :return: The id of this ListHealthChecksRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListHealthChecksRequest.

        资源ID。

        :param id: The id of this ListHealthChecksRequest.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ListHealthChecksRequest.

        配置状态，可选范围: - ACTIVE：运行中 - PENDING：待定 - ERROR：错误 - DELETING：正在删除

        :return: The status of this ListHealthChecksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListHealthChecksRequest.

        配置状态，可选范围: - ACTIVE：运行中 - PENDING：待定 - ERROR：错误 - DELETING：正在删除

        :param status: The status of this ListHealthChecksRequest.
        :type status: str
        """
        self._status = status

    @property
    def endpoint_group_id(self):
        """Gets the endpoint_group_id of this ListHealthChecksRequest.

        终端节点组ID。

        :return: The endpoint_group_id of this ListHealthChecksRequest.
        :rtype: str
        """
        return self._endpoint_group_id

    @endpoint_group_id.setter
    def endpoint_group_id(self, endpoint_group_id):
        """Sets the endpoint_group_id of this ListHealthChecksRequest.

        终端节点组ID。

        :param endpoint_group_id: The endpoint_group_id of this ListHealthChecksRequest.
        :type endpoint_group_id: str
        """
        self._endpoint_group_id = endpoint_group_id

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
        if not isinstance(other, ListHealthChecksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
