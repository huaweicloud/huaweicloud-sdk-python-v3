# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchAgentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_page': 'int',
        'total_count': 'int',
        'online_count': 'int',
        'offline_count': 'int',
        'disable_count': 'int',
        'agent_info_list': 'list[InstanceInfo]'
    }

    attribute_map = {
        'total_page': 'total_page',
        'total_count': 'total_count',
        'online_count': 'online_count',
        'offline_count': 'offline_count',
        'disable_count': 'disable_count',
        'agent_info_list': 'agent_info_list'
    }

    def __init__(self, total_page=None, total_count=None, online_count=None, offline_count=None, disable_count=None, agent_info_list=None):
        """SearchAgentResponse

        The model defined in huaweicloud sdk

        :param total_page: 总页数。
        :type total_page: int
        :param total_count: 总个数。
        :type total_count: int
        :param online_count: 正常个数。
        :type online_count: int
        :param offline_count: 心跳异常个数。
        :type offline_count: int
        :param disable_count: 被关闭的个数。
        :type disable_count: int
        :param agent_info_list: agent地址列表。
        :type agent_info_list: list[:class:`huaweicloudsdkapm.v1.InstanceInfo`]
        """
        
        super(SearchAgentResponse, self).__init__()

        self._total_page = None
        self._total_count = None
        self._online_count = None
        self._offline_count = None
        self._disable_count = None
        self._agent_info_list = None
        self.discriminator = None

        if total_page is not None:
            self.total_page = total_page
        if total_count is not None:
            self.total_count = total_count
        if online_count is not None:
            self.online_count = online_count
        if offline_count is not None:
            self.offline_count = offline_count
        if disable_count is not None:
            self.disable_count = disable_count
        if agent_info_list is not None:
            self.agent_info_list = agent_info_list

    @property
    def total_page(self):
        """Gets the total_page of this SearchAgentResponse.

        总页数。

        :return: The total_page of this SearchAgentResponse.
        :rtype: int
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        """Sets the total_page of this SearchAgentResponse.

        总页数。

        :param total_page: The total_page of this SearchAgentResponse.
        :type total_page: int
        """
        self._total_page = total_page

    @property
    def total_count(self):
        """Gets the total_count of this SearchAgentResponse.

        总个数。

        :return: The total_count of this SearchAgentResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this SearchAgentResponse.

        总个数。

        :param total_count: The total_count of this SearchAgentResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def online_count(self):
        """Gets the online_count of this SearchAgentResponse.

        正常个数。

        :return: The online_count of this SearchAgentResponse.
        :rtype: int
        """
        return self._online_count

    @online_count.setter
    def online_count(self, online_count):
        """Sets the online_count of this SearchAgentResponse.

        正常个数。

        :param online_count: The online_count of this SearchAgentResponse.
        :type online_count: int
        """
        self._online_count = online_count

    @property
    def offline_count(self):
        """Gets the offline_count of this SearchAgentResponse.

        心跳异常个数。

        :return: The offline_count of this SearchAgentResponse.
        :rtype: int
        """
        return self._offline_count

    @offline_count.setter
    def offline_count(self, offline_count):
        """Sets the offline_count of this SearchAgentResponse.

        心跳异常个数。

        :param offline_count: The offline_count of this SearchAgentResponse.
        :type offline_count: int
        """
        self._offline_count = offline_count

    @property
    def disable_count(self):
        """Gets the disable_count of this SearchAgentResponse.

        被关闭的个数。

        :return: The disable_count of this SearchAgentResponse.
        :rtype: int
        """
        return self._disable_count

    @disable_count.setter
    def disable_count(self, disable_count):
        """Sets the disable_count of this SearchAgentResponse.

        被关闭的个数。

        :param disable_count: The disable_count of this SearchAgentResponse.
        :type disable_count: int
        """
        self._disable_count = disable_count

    @property
    def agent_info_list(self):
        """Gets the agent_info_list of this SearchAgentResponse.

        agent地址列表。

        :return: The agent_info_list of this SearchAgentResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.InstanceInfo`]
        """
        return self._agent_info_list

    @agent_info_list.setter
    def agent_info_list(self, agent_info_list):
        """Sets the agent_info_list of this SearchAgentResponse.

        agent地址列表。

        :param agent_info_list: The agent_info_list of this SearchAgentResponse.
        :type agent_info_list: list[:class:`huaweicloudsdkapm.v1.InstanceInfo`]
        """
        self._agent_info_list = agent_info_list

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
        if not isinstance(other, SearchAgentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
