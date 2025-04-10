# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort': 'str',
        'name': 'str',
        'fuzzy_name': 'str',
        'connection_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort': 'sort',
        'name': 'name',
        'fuzzy_name': 'fuzzy_name',
        'connection_id': 'connection_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, channel_id=None, offset=None, limit=None, sort=None, name=None, fuzzy_name=None, connection_id=None, enterprise_project_id=None):
        r"""ListSubscriptionsRequest

        The model defined in huaweicloud sdk

        :param channel_id: 指定查询的事件通道ID
        :type channel_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量不能小于0
        :type offset: int
        :param limit: 每页显示的条目数量，不能小于1或大于1000
        :type limit: int
        :param sort: 指定查询排序
        :type sort: str
        :param name: 指定查询的事件订阅名称，精准匹配
        :type name: str
        :param fuzzy_name: 指定查询的事件订阅名称，模糊匹配
        :type fuzzy_name: str
        :param connection_id: 目标连接 id
        :type connection_id: str
        :param enterprise_project_id: 创建订阅时所使用的企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._channel_id = None
        self._offset = None
        self._limit = None
        self._sort = None
        self._name = None
        self._fuzzy_name = None
        self._connection_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if channel_id is not None:
            self.channel_id = channel_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort is not None:
            self.sort = sort
        if name is not None:
            self.name = name
        if fuzzy_name is not None:
            self.fuzzy_name = fuzzy_name
        if connection_id is not None:
            self.connection_id = connection_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def channel_id(self):
        r"""Gets the channel_id of this ListSubscriptionsRequest.

        指定查询的事件通道ID

        :return: The channel_id of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this ListSubscriptionsRequest.

        指定查询的事件通道ID

        :param channel_id: The channel_id of this ListSubscriptionsRequest.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def offset(self):
        r"""Gets the offset of this ListSubscriptionsRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :return: The offset of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubscriptionsRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :param offset: The offset of this ListSubscriptionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubscriptionsRequest.

        每页显示的条目数量，不能小于1或大于1000

        :return: The limit of this ListSubscriptionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubscriptionsRequest.

        每页显示的条目数量，不能小于1或大于1000

        :param limit: The limit of this ListSubscriptionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort(self):
        r"""Gets the sort of this ListSubscriptionsRequest.

        指定查询排序

        :return: The sort of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListSubscriptionsRequest.

        指定查询排序

        :param sort: The sort of this ListSubscriptionsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def name(self):
        r"""Gets the name of this ListSubscriptionsRequest.

        指定查询的事件订阅名称，精准匹配

        :return: The name of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSubscriptionsRequest.

        指定查询的事件订阅名称，精准匹配

        :param name: The name of this ListSubscriptionsRequest.
        :type name: str
        """
        self._name = name

    @property
    def fuzzy_name(self):
        r"""Gets the fuzzy_name of this ListSubscriptionsRequest.

        指定查询的事件订阅名称，模糊匹配

        :return: The fuzzy_name of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._fuzzy_name

    @fuzzy_name.setter
    def fuzzy_name(self, fuzzy_name):
        r"""Sets the fuzzy_name of this ListSubscriptionsRequest.

        指定查询的事件订阅名称，模糊匹配

        :param fuzzy_name: The fuzzy_name of this ListSubscriptionsRequest.
        :type fuzzy_name: str
        """
        self._fuzzy_name = fuzzy_name

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ListSubscriptionsRequest.

        目标连接 id

        :return: The connection_id of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ListSubscriptionsRequest.

        目标连接 id

        :param connection_id: The connection_id of this ListSubscriptionsRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListSubscriptionsRequest.

        创建订阅时所使用的企业项目id

        :return: The enterprise_project_id of this ListSubscriptionsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListSubscriptionsRequest.

        创建订阅时所使用的企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListSubscriptionsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListSubscriptionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
