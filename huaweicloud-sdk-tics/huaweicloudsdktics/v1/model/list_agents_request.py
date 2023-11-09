# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentsRequest:

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
        'offset': 'int',
        'agent_name': 'str',
        'league_name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'agent_name': 'agent_name',
        'league_name': 'league_name'
    }

    def __init__(self, limit=None, offset=None, agent_name=None, league_name=None):
        """ListAgentsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页记录数，取值0-100
        :type limit: int
        :param offset: 记录数偏移量 
        :type offset: int
        :param agent_name: 可信节点名称 
        :type agent_name: str
        :param league_name: 联盟名称 
        :type league_name: str
        """
        
        

        self._limit = None
        self._offset = None
        self._agent_name = None
        self._league_name = None
        self.discriminator = None

        self.limit = limit
        self.offset = offset
        if agent_name is not None:
            self.agent_name = agent_name
        if league_name is not None:
            self.league_name = league_name

    @property
    def limit(self):
        """Gets the limit of this ListAgentsRequest.

        每页记录数，取值0-100

        :return: The limit of this ListAgentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAgentsRequest.

        每页记录数，取值0-100

        :param limit: The limit of this ListAgentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAgentsRequest.

        记录数偏移量 

        :return: The offset of this ListAgentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAgentsRequest.

        记录数偏移量 

        :param offset: The offset of this ListAgentsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def agent_name(self):
        """Gets the agent_name of this ListAgentsRequest.

        可信节点名称 

        :return: The agent_name of this ListAgentsRequest.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this ListAgentsRequest.

        可信节点名称 

        :param agent_name: The agent_name of this ListAgentsRequest.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def league_name(self):
        """Gets the league_name of this ListAgentsRequest.

        联盟名称 

        :return: The league_name of this ListAgentsRequest.
        :rtype: str
        """
        return self._league_name

    @league_name.setter
    def league_name(self, league_name):
        """Sets the league_name of this ListAgentsRequest.

        联盟名称 

        :param league_name: The league_name of this ListAgentsRequest.
        :type league_name: str
        """
        self._league_name = league_name

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
        if not isinstance(other, ListAgentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
