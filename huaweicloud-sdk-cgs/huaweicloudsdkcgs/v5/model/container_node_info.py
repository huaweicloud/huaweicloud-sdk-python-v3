# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerNodeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'host_status': 'str',
        'agent_status': 'str',
        'protect_status': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'protect_status': 'protect_status'
    }

    def __init__(self, host_id=None, host_name=None, host_status=None, agent_status=None, protect_status=None):
        """ContainerNodeInfo

        The model defined in huaweicloud sdk

        :param host_id: 节点id
        :type host_id: str
        :param host_name: 节点（服务器）名称
        :type host_name: str
        :param host_status: 服务器状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。
        :type host_status: str
        :param agent_status: Agent状态，包含如下3种。   - not_register ：未注册。   - online ：在线。   - offline ：离线。
        :type agent_status: str
        :param protect_status: 防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。
        :type protect_status: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._host_status = None
        self._agent_status = None
        self._protect_status = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_status is not None:
            self.host_status = host_status
        if agent_status is not None:
            self.agent_status = agent_status
        if protect_status is not None:
            self.protect_status = protect_status

    @property
    def host_id(self):
        """Gets the host_id of this ContainerNodeInfo.

        节点id

        :return: The host_id of this ContainerNodeInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ContainerNodeInfo.

        节点id

        :param host_id: The host_id of this ContainerNodeInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this ContainerNodeInfo.

        节点（服务器）名称

        :return: The host_name of this ContainerNodeInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ContainerNodeInfo.

        节点（服务器）名称

        :param host_name: The host_name of this ContainerNodeInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_status(self):
        """Gets the host_status of this ContainerNodeInfo.

        服务器状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :return: The host_status of this ContainerNodeInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this ContainerNodeInfo.

        服务器状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :param host_status: The host_status of this ContainerNodeInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        """Gets the agent_status of this ContainerNodeInfo.

        Agent状态，包含如下3种。   - not_register ：未注册。   - online ：在线。   - offline ：离线。

        :return: The agent_status of this ContainerNodeInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this ContainerNodeInfo.

        Agent状态，包含如下3种。   - not_register ：未注册。   - online ：在线。   - offline ：离线。

        :param agent_status: The agent_status of this ContainerNodeInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def protect_status(self):
        """Gets the protect_status of this ContainerNodeInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :return: The protect_status of this ContainerNodeInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ContainerNodeInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :param protect_status: The protect_status of this ContainerNodeInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

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
        if not isinstance(other, ContainerNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
