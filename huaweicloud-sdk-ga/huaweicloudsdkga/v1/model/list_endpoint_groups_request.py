# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointGroupsRequest:

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
        'name': 'str',
        'status': 'str',
        'listener_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'listener_id': 'listener_id'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, name=None, status=None, listener_id=None):
        r"""ListEndpointGroupsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询每页的资源个数。如果不设置，则默认为500。
        :type limit: int
        :param marker: 分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。
        :type marker: str
        :param page_reverse: 分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。
        :type page_reverse: bool
        :param id: 资源ID。
        :type id: str
        :param name: 资源名称，取值范围：0~64个字符之间，只能由数字、字母、中划线和中文组成。
        :type name: str
        :param status: 配置状态，可选范围: - ACTIVE：运行中 - PENDING：待定 - ERROR：错误 - DELETING：正在删除
        :type status: str
        :param listener_id: 监听器ID
        :type listener_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._status = None
        self._listener_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if listener_id is not None:
            self.listener_id = listener_id

    @property
    def limit(self):
        r"""Gets the limit of this ListEndpointGroupsRequest.

        分页查询每页的资源个数。如果不设置，则默认为500。

        :return: The limit of this ListEndpointGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEndpointGroupsRequest.

        分页查询每页的资源个数。如果不设置，则默认为500。

        :param limit: The limit of this ListEndpointGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListEndpointGroupsRequest.

        分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。

        :return: The marker of this ListEndpointGroupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListEndpointGroupsRequest.

        分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。

        :param marker: The marker of this ListEndpointGroupsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListEndpointGroupsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :return: The page_reverse of this ListEndpointGroupsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListEndpointGroupsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :param page_reverse: The page_reverse of this ListEndpointGroupsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListEndpointGroupsRequest.

        资源ID。

        :return: The id of this ListEndpointGroupsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListEndpointGroupsRequest.

        资源ID。

        :param id: The id of this ListEndpointGroupsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListEndpointGroupsRequest.

        资源名称，取值范围：0~64个字符之间，只能由数字、字母、中划线和中文组成。

        :return: The name of this ListEndpointGroupsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListEndpointGroupsRequest.

        资源名称，取值范围：0~64个字符之间，只能由数字、字母、中划线和中文组成。

        :param name: The name of this ListEndpointGroupsRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListEndpointGroupsRequest.

        配置状态，可选范围: - ACTIVE：运行中 - PENDING：待定 - ERROR：错误 - DELETING：正在删除

        :return: The status of this ListEndpointGroupsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListEndpointGroupsRequest.

        配置状态，可选范围: - ACTIVE：运行中 - PENDING：待定 - ERROR：错误 - DELETING：正在删除

        :param status: The status of this ListEndpointGroupsRequest.
        :type status: str
        """
        self._status = status

    @property
    def listener_id(self):
        r"""Gets the listener_id of this ListEndpointGroupsRequest.

        监听器ID

        :return: The listener_id of this ListEndpointGroupsRequest.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this ListEndpointGroupsRequest.

        监听器ID

        :param listener_id: The listener_id of this ListEndpointGroupsRequest.
        :type listener_id: str
        """
        self._listener_id = listener_id

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
        if not isinstance(other, ListEndpointGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
