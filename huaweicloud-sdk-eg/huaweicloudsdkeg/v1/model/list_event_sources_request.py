# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventSourcesRequest:

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
        'provider_type': 'str',
        'name': 'str',
        'fuzzy_name': 'str',
        'fuzzy_label': 'str'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort': 'sort',
        'provider_type': 'provider_type',
        'name': 'name',
        'fuzzy_name': 'fuzzy_name',
        'fuzzy_label': 'fuzzy_label'
    }

    def __init__(self, channel_id=None, offset=None, limit=None, sort=None, provider_type=None, name=None, fuzzy_name=None, fuzzy_label=None):
        """ListEventSourcesRequest

        The model defined in huaweicloud sdk

        :param channel_id: 指定查询的事件通道ID
        :type channel_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量不能小于0
        :type offset: int
        :param limit: 每页显示的条目数量，不能小于1或大于1000
        :type limit: int
        :param sort: 指定查询排序
        :type sort: str
        :param provider_type: 指定查询提供方的类型
        :type provider_type: str
        :param name: 指定查询的事件源名称，精准匹配
        :type name: str
        :param fuzzy_name: 指定查询的事件源名称，模糊匹配
        :type fuzzy_name: str
        :param fuzzy_label: 指定查询的事件源标签，模糊匹配
        :type fuzzy_label: str
        """
        
        

        self._channel_id = None
        self._offset = None
        self._limit = None
        self._sort = None
        self._provider_type = None
        self._name = None
        self._fuzzy_name = None
        self._fuzzy_label = None
        self.discriminator = None

        if channel_id is not None:
            self.channel_id = channel_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort is not None:
            self.sort = sort
        if provider_type is not None:
            self.provider_type = provider_type
        if name is not None:
            self.name = name
        if fuzzy_name is not None:
            self.fuzzy_name = fuzzy_name
        if fuzzy_label is not None:
            self.fuzzy_label = fuzzy_label

    @property
    def channel_id(self):
        """Gets the channel_id of this ListEventSourcesRequest.

        指定查询的事件通道ID

        :return: The channel_id of this ListEventSourcesRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ListEventSourcesRequest.

        指定查询的事件通道ID

        :param channel_id: The channel_id of this ListEventSourcesRequest.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def offset(self):
        """Gets the offset of this ListEventSourcesRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :return: The offset of this ListEventSourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEventSourcesRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :param offset: The offset of this ListEventSourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEventSourcesRequest.

        每页显示的条目数量，不能小于1或大于1000

        :return: The limit of this ListEventSourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEventSourcesRequest.

        每页显示的条目数量，不能小于1或大于1000

        :param limit: The limit of this ListEventSourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort(self):
        """Gets the sort of this ListEventSourcesRequest.

        指定查询排序

        :return: The sort of this ListEventSourcesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListEventSourcesRequest.

        指定查询排序

        :param sort: The sort of this ListEventSourcesRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def provider_type(self):
        """Gets the provider_type of this ListEventSourcesRequest.

        指定查询提供方的类型

        :return: The provider_type of this ListEventSourcesRequest.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this ListEventSourcesRequest.

        指定查询提供方的类型

        :param provider_type: The provider_type of this ListEventSourcesRequest.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def name(self):
        """Gets the name of this ListEventSourcesRequest.

        指定查询的事件源名称，精准匹配

        :return: The name of this ListEventSourcesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEventSourcesRequest.

        指定查询的事件源名称，精准匹配

        :param name: The name of this ListEventSourcesRequest.
        :type name: str
        """
        self._name = name

    @property
    def fuzzy_name(self):
        """Gets the fuzzy_name of this ListEventSourcesRequest.

        指定查询的事件源名称，模糊匹配

        :return: The fuzzy_name of this ListEventSourcesRequest.
        :rtype: str
        """
        return self._fuzzy_name

    @fuzzy_name.setter
    def fuzzy_name(self, fuzzy_name):
        """Sets the fuzzy_name of this ListEventSourcesRequest.

        指定查询的事件源名称，模糊匹配

        :param fuzzy_name: The fuzzy_name of this ListEventSourcesRequest.
        :type fuzzy_name: str
        """
        self._fuzzy_name = fuzzy_name

    @property
    def fuzzy_label(self):
        """Gets the fuzzy_label of this ListEventSourcesRequest.

        指定查询的事件源标签，模糊匹配

        :return: The fuzzy_label of this ListEventSourcesRequest.
        :rtype: str
        """
        return self._fuzzy_label

    @fuzzy_label.setter
    def fuzzy_label(self, fuzzy_label):
        """Sets the fuzzy_label of this ListEventSourcesRequest.

        指定查询的事件源标签，模糊匹配

        :param fuzzy_label: The fuzzy_label of this ListEventSourcesRequest.
        :type fuzzy_label: str
        """
        self._fuzzy_label = fuzzy_label

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
        if not isinstance(other, ListEventSourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
