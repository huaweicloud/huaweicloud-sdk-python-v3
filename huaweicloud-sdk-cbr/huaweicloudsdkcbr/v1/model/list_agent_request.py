# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'offset': 'int',
        'status': 'str',
        'agent_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'status': 'status',
        'agent_id': 'agent_id'
    }

    def __init__(self, limit=None, offset=None, status=None, agent_id=None):
        r"""ListAgentRequest

        The model defined in huaweicloud sdk

        :param limit: 每页显示条目数，正整数
        :type limit: str
        :param offset: 偏移值,正整数
        :type offset: int
        :param status: 状态
        :type status: str
        :param agent_id: 客户端ID
        :type agent_id: list[str]
        """
        
        

        self._limit = None
        self._offset = None
        self._status = None
        self._agent_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status
        if agent_id is not None:
            self.agent_id = agent_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAgentRequest.

        每页显示条目数，正整数

        :return: The limit of this ListAgentRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAgentRequest.

        每页显示条目数，正整数

        :param limit: The limit of this ListAgentRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAgentRequest.

        偏移值,正整数

        :return: The offset of this ListAgentRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAgentRequest.

        偏移值,正整数

        :param offset: The offset of this ListAgentRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        r"""Gets the status of this ListAgentRequest.

        状态

        :return: The status of this ListAgentRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAgentRequest.

        状态

        :param status: The status of this ListAgentRequest.
        :type status: str
        """
        self._status = status

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ListAgentRequest.

        客户端ID

        :return: The agent_id of this ListAgentRequest.
        :rtype: list[str]
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ListAgentRequest.

        客户端ID

        :param agent_id: The agent_id of this ListAgentRequest.
        :type agent_id: list[str]
        """
        self._agent_id = agent_id

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
        if not isinstance(other, ListAgentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
