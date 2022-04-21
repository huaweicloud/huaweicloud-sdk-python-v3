# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListContainerNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'agent_status': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'host_name': 'host_name',
        'agent_status': 'agent_status',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, host_name=None, agent_status=None, limit=None, offset=None):
        """ListContainerNodesRequest

        The model defined in huaweicloud sdk

        :param host_name: 节点（服务器）名称
        :type host_name: str
        :param agent_status: Agent状态，包含如下3种。   - not_installed ：未安装   - online ：在线   - offline ：离线
        :type agent_status: str
        :param limit: 查询返回查询容器节点列表当前页面的数，量默认10
        :type limit: int
        :param offset: 查询游标，初始传入0
        :type offset: int
        """
        
        

        self._host_name = None
        self._agent_status = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if agent_status is not None:
            self.agent_status = agent_status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def host_name(self):
        """Gets the host_name of this ListContainerNodesRequest.

        节点（服务器）名称

        :return: The host_name of this ListContainerNodesRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListContainerNodesRequest.

        节点（服务器）名称

        :param host_name: The host_name of this ListContainerNodesRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def agent_status(self):
        """Gets the agent_status of this ListContainerNodesRequest.

        Agent状态，包含如下3种。   - not_installed ：未安装   - online ：在线   - offline ：离线

        :return: The agent_status of this ListContainerNodesRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this ListContainerNodesRequest.

        Agent状态，包含如下3种。   - not_installed ：未安装   - online ：在线   - offline ：离线

        :param agent_status: The agent_status of this ListContainerNodesRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def limit(self):
        """Gets the limit of this ListContainerNodesRequest.

        查询返回查询容器节点列表当前页面的数，量默认10

        :return: The limit of this ListContainerNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListContainerNodesRequest.

        查询返回查询容器节点列表当前页面的数，量默认10

        :param limit: The limit of this ListContainerNodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListContainerNodesRequest.

        查询游标，初始传入0

        :return: The offset of this ListContainerNodesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListContainerNodesRequest.

        查询游标，初始传入0

        :param offset: The offset of this ListContainerNodesRequest.
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
        if not isinstance(other, ListContainerNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
