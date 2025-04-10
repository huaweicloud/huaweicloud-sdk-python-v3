# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClientsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'clients': 'list[ClientInfo]',
        'count': 'int'
    }

    attribute_map = {
        'time': 'time',
        'clients': 'clients',
        'count': 'count'
    }

    def __init__(self, time=None, clients=None, count=None):
        r"""ListClientsResponse

        The model defined in huaweicloud sdk

        :param time: 数据更新时间
        :type time: str
        :param clients: 会话列表
        :type clients: list[:class:`huaweicloudsdkdcs.v2.ClientInfo`]
        :param count: 会话总数
        :type count: int
        """
        
        super(ListClientsResponse, self).__init__()

        self._time = None
        self._clients = None
        self._count = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if clients is not None:
            self.clients = clients
        if count is not None:
            self.count = count

    @property
    def time(self):
        r"""Gets the time of this ListClientsResponse.

        数据更新时间

        :return: The time of this ListClientsResponse.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ListClientsResponse.

        数据更新时间

        :param time: The time of this ListClientsResponse.
        :type time: str
        """
        self._time = time

    @property
    def clients(self):
        r"""Gets the clients of this ListClientsResponse.

        会话列表

        :return: The clients of this ListClientsResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.ClientInfo`]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        r"""Sets the clients of this ListClientsResponse.

        会话列表

        :param clients: The clients of this ListClientsResponse.
        :type clients: list[:class:`huaweicloudsdkdcs.v2.ClientInfo`]
        """
        self._clients = clients

    @property
    def count(self):
        r"""Gets the count of this ListClientsResponse.

        会话总数

        :return: The count of this ListClientsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListClientsResponse.

        会话总数

        :param count: The count of this ListClientsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListClientsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
