# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agents': 'list[Agent]',
        'count': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'agents': 'agents',
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, agents=None, count=None, limit=None, offset=None):
        """ListAgentResponse

        The model defined in huaweicloud sdk

        :param agents: 客户端实例列表
        :type agents: list[:class:`huaweicloudsdkcbr.v1.Agent`]
        :param count: 客户端个数 
        :type count: int
        :param limit: 每页显示的条目数量 
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询 
        :type offset: int
        """
        
        super(ListAgentResponse, self).__init__()

        self._agents = None
        self._count = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if agents is not None:
            self.agents = agents
        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def agents(self):
        """Gets the agents of this ListAgentResponse.

        客户端实例列表

        :return: The agents of this ListAgentResponse.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.Agent`]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this ListAgentResponse.

        客户端实例列表

        :param agents: The agents of this ListAgentResponse.
        :type agents: list[:class:`huaweicloudsdkcbr.v1.Agent`]
        """
        self._agents = agents

    @property
    def count(self):
        """Gets the count of this ListAgentResponse.

        客户端个数 

        :return: The count of this ListAgentResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAgentResponse.

        客户端个数 

        :param count: The count of this ListAgentResponse.
        :type count: int
        """
        self._count = count

    @property
    def limit(self):
        """Gets the limit of this ListAgentResponse.

        每页显示的条目数量 

        :return: The limit of this ListAgentResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAgentResponse.

        每页显示的条目数量 

        :param limit: The limit of this ListAgentResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAgentResponse.

        偏移量，表示从此偏移量开始查询 

        :return: The offset of this ListAgentResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAgentResponse.

        偏移量，表示从此偏移量开始查询 

        :param offset: The offset of this ListAgentResponse.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListAgentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
