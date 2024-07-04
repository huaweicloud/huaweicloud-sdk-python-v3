# coding: utf-8

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
        'region': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'host_name': 'str',
        'agent_status': 'str',
        'protect_status': 'str',
        'container_tags': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_name': 'host_name',
        'agent_status': 'agent_status',
        'protect_status': 'protect_status',
        'container_tags': 'container_tags'
    }

    def __init__(self, region=None, enterprise_project_id=None, offset=None, limit=None, host_name=None, agent_status=None, protect_status=None, container_tags=None):
        """ListContainerNodesRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param host_name: 节点名称
        :type host_name: str
        :param agent_status: Agent状态，包含如下3种。   - not_installed ：未安装   - online ：在线   - offline ：离线
        :type agent_status: str
        :param protect_status: 防护状态，包含如下2种。   - closed ：关闭   - opened ：开启
        :type protect_status: str
        :param container_tags: 标签：用来识别cce容器节点和自建  - cce：cce节点  - self：自建节点  - other：其他节点
        :type container_tags: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._host_name = None
        self._agent_status = None
        self._protect_status = None
        self._container_tags = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if host_name is not None:
            self.host_name = host_name
        if agent_status is not None:
            self.agent_status = agent_status
        if protect_status is not None:
            self.protect_status = protect_status
        if container_tags is not None:
            self.container_tags = container_tags

    @property
    def region(self):
        """Gets the region of this ListContainerNodesRequest.

        Region ID

        :return: The region of this ListContainerNodesRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListContainerNodesRequest.

        Region ID

        :param region: The region of this ListContainerNodesRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListContainerNodesRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListContainerNodesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListContainerNodesRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListContainerNodesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ListContainerNodesRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListContainerNodesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListContainerNodesRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListContainerNodesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListContainerNodesRequest.

        每页显示个数

        :return: The limit of this ListContainerNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListContainerNodesRequest.

        每页显示个数

        :param limit: The limit of this ListContainerNodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host_name(self):
        """Gets the host_name of this ListContainerNodesRequest.

        节点名称

        :return: The host_name of this ListContainerNodesRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListContainerNodesRequest.

        节点名称

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
    def protect_status(self):
        """Gets the protect_status of this ListContainerNodesRequest.

        防护状态，包含如下2种。   - closed ：关闭   - opened ：开启

        :return: The protect_status of this ListContainerNodesRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ListContainerNodesRequest.

        防护状态，包含如下2种。   - closed ：关闭   - opened ：开启

        :param protect_status: The protect_status of this ListContainerNodesRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def container_tags(self):
        """Gets the container_tags of this ListContainerNodesRequest.

        标签：用来识别cce容器节点和自建  - cce：cce节点  - self：自建节点  - other：其他节点

        :return: The container_tags of this ListContainerNodesRequest.
        :rtype: str
        """
        return self._container_tags

    @container_tags.setter
    def container_tags(self, container_tags):
        """Sets the container_tags of this ListContainerNodesRequest.

        标签：用来识别cce容器节点和自建  - cce：cce节点  - self：自建节点  - other：其他节点

        :param container_tags: The container_tags of this ListContainerNodesRequest.
        :type container_tags: str
        """
        self._container_tags = container_tags

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
