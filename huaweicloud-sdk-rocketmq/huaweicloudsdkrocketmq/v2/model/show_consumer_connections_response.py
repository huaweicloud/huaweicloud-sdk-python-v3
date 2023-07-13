# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsumerConnectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'online': 'bool',
        'subscription_consistency': 'bool',
        'total': 'int',
        'next_offset': 'int',
        'previous_offset': 'int',
        'clients': 'list[ClientData]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'online': 'online',
        'subscription_consistency': 'subscription_consistency',
        'total': 'total',
        'next_offset': 'next_offset',
        'previous_offset': 'previous_offset',
        'clients': 'clients'
    }

    def __init__(self, group_name=None, online=None, subscription_consistency=None, total=None, next_offset=None, previous_offset=None, clients=None):
        """ShowConsumerConnectionsResponse

        The model defined in huaweicloud sdk

        :param group_name: 消费组名称
        :type group_name: str
        :param online: 消费组是否在线
        :type online: bool
        :param subscription_consistency: 订阅关系是否一致
        :type subscription_consistency: bool
        :param total: 消费者总数
        :type total: int
        :param next_offset: 下个分页的offset
        :type next_offset: int
        :param previous_offset: 上个分页的offset
        :type previous_offset: int
        :param clients: 消费者订阅详情列表
        :type clients: list[:class:`huaweicloudsdkrocketmq.v2.ClientData`]
        """
        
        super(ShowConsumerConnectionsResponse, self).__init__()

        self._group_name = None
        self._online = None
        self._subscription_consistency = None
        self._total = None
        self._next_offset = None
        self._previous_offset = None
        self._clients = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if online is not None:
            self.online = online
        if subscription_consistency is not None:
            self.subscription_consistency = subscription_consistency
        if total is not None:
            self.total = total
        if next_offset is not None:
            self.next_offset = next_offset
        if previous_offset is not None:
            self.previous_offset = previous_offset
        if clients is not None:
            self.clients = clients

    @property
    def group_name(self):
        """Gets the group_name of this ShowConsumerConnectionsResponse.

        消费组名称

        :return: The group_name of this ShowConsumerConnectionsResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ShowConsumerConnectionsResponse.

        消费组名称

        :param group_name: The group_name of this ShowConsumerConnectionsResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def online(self):
        """Gets the online of this ShowConsumerConnectionsResponse.

        消费组是否在线

        :return: The online of this ShowConsumerConnectionsResponse.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this ShowConsumerConnectionsResponse.

        消费组是否在线

        :param online: The online of this ShowConsumerConnectionsResponse.
        :type online: bool
        """
        self._online = online

    @property
    def subscription_consistency(self):
        """Gets the subscription_consistency of this ShowConsumerConnectionsResponse.

        订阅关系是否一致

        :return: The subscription_consistency of this ShowConsumerConnectionsResponse.
        :rtype: bool
        """
        return self._subscription_consistency

    @subscription_consistency.setter
    def subscription_consistency(self, subscription_consistency):
        """Sets the subscription_consistency of this ShowConsumerConnectionsResponse.

        订阅关系是否一致

        :param subscription_consistency: The subscription_consistency of this ShowConsumerConnectionsResponse.
        :type subscription_consistency: bool
        """
        self._subscription_consistency = subscription_consistency

    @property
    def total(self):
        """Gets the total of this ShowConsumerConnectionsResponse.

        消费者总数

        :return: The total of this ShowConsumerConnectionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowConsumerConnectionsResponse.

        消费者总数

        :param total: The total of this ShowConsumerConnectionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def next_offset(self):
        """Gets the next_offset of this ShowConsumerConnectionsResponse.

        下个分页的offset

        :return: The next_offset of this ShowConsumerConnectionsResponse.
        :rtype: int
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        """Sets the next_offset of this ShowConsumerConnectionsResponse.

        下个分页的offset

        :param next_offset: The next_offset of this ShowConsumerConnectionsResponse.
        :type next_offset: int
        """
        self._next_offset = next_offset

    @property
    def previous_offset(self):
        """Gets the previous_offset of this ShowConsumerConnectionsResponse.

        上个分页的offset

        :return: The previous_offset of this ShowConsumerConnectionsResponse.
        :rtype: int
        """
        return self._previous_offset

    @previous_offset.setter
    def previous_offset(self, previous_offset):
        """Sets the previous_offset of this ShowConsumerConnectionsResponse.

        上个分页的offset

        :param previous_offset: The previous_offset of this ShowConsumerConnectionsResponse.
        :type previous_offset: int
        """
        self._previous_offset = previous_offset

    @property
    def clients(self):
        """Gets the clients of this ShowConsumerConnectionsResponse.

        消费者订阅详情列表

        :return: The clients of this ShowConsumerConnectionsResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ClientData`]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this ShowConsumerConnectionsResponse.

        消费者订阅详情列表

        :param clients: The clients of this ShowConsumerConnectionsResponse.
        :type clients: list[:class:`huaweicloudsdkrocketmq.v2.ClientData`]
        """
        self._clients = clients

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
        if not isinstance(other, ShowConsumerConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
