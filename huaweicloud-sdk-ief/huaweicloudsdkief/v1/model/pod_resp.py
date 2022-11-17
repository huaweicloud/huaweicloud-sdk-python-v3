# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PodResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'configs': 'PodConfigs',
        'init_containers': 'list[ContainerResp]',
        'containers': 'list[ContainerResp]',
        'node_id': 'str',
        'deployment_id': 'str',
        'project_id': 'str',
        'reason': 'str',
        'message': 'str',
        'created_at': 'str',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'configs': 'configs',
        'init_containers': 'init_containers',
        'containers': 'containers',
        'node_id': 'node_id',
        'deployment_id': 'deployment_id',
        'project_id': 'project_id',
        'reason': 'reason',
        'message': 'message',
        'created_at': 'created_at',
        'state': 'state'
    }

    def __init__(self, id=None, name=None, configs=None, init_containers=None, containers=None, node_id=None, deployment_id=None, project_id=None, reason=None, message=None, created_at=None, state=None):
        """PodResp

        The model defined in huaweicloud sdk

        :param id: 应用实例uuid
        :type id: str
        :param name: 应用实例名称
        :type name: str
        :param configs: 
        :type configs: :class:`huaweicloudsdkief.v1.PodConfigs`
        :param init_containers: 应用实例init容器
        :type init_containers: list[:class:`huaweicloudsdkief.v1.ContainerResp`]
        :param containers: 应用实例业务容器
        :type containers: list[:class:`huaweicloudsdkief.v1.ContainerResp`]
        :param node_id: 应用实例所在节点
        :type node_id: str
        :param deployment_id: 应用ID
        :type deployment_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param reason: 应用实例故障原因
        :type reason: str
        :param message: 应用实例故障详情
        :type message: str
        :param created_at: 应用实例创建时间
        :type created_at: str
        :param state: 应用实例状态
        :type state: str
        """
        
        

        self._id = None
        self._name = None
        self._configs = None
        self._init_containers = None
        self._containers = None
        self._node_id = None
        self._deployment_id = None
        self._project_id = None
        self._reason = None
        self._message = None
        self._created_at = None
        self._state = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.configs = configs
        if init_containers is not None:
            self.init_containers = init_containers
        self.containers = containers
        self.node_id = node_id
        self.deployment_id = deployment_id
        self.project_id = project_id
        self.reason = reason
        self.message = message
        self.created_at = created_at
        self.state = state

    @property
    def id(self):
        """Gets the id of this PodResp.

        应用实例uuid

        :return: The id of this PodResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PodResp.

        应用实例uuid

        :param id: The id of this PodResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PodResp.

        应用实例名称

        :return: The name of this PodResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PodResp.

        应用实例名称

        :param name: The name of this PodResp.
        :type name: str
        """
        self._name = name

    @property
    def configs(self):
        """Gets the configs of this PodResp.

        :return: The configs of this PodResp.
        :rtype: :class:`huaweicloudsdkief.v1.PodConfigs`
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this PodResp.

        :param configs: The configs of this PodResp.
        :type configs: :class:`huaweicloudsdkief.v1.PodConfigs`
        """
        self._configs = configs

    @property
    def init_containers(self):
        """Gets the init_containers of this PodResp.

        应用实例init容器

        :return: The init_containers of this PodResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.ContainerResp`]
        """
        return self._init_containers

    @init_containers.setter
    def init_containers(self, init_containers):
        """Sets the init_containers of this PodResp.

        应用实例init容器

        :param init_containers: The init_containers of this PodResp.
        :type init_containers: list[:class:`huaweicloudsdkief.v1.ContainerResp`]
        """
        self._init_containers = init_containers

    @property
    def containers(self):
        """Gets the containers of this PodResp.

        应用实例业务容器

        :return: The containers of this PodResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.ContainerResp`]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """Sets the containers of this PodResp.

        应用实例业务容器

        :param containers: The containers of this PodResp.
        :type containers: list[:class:`huaweicloudsdkief.v1.ContainerResp`]
        """
        self._containers = containers

    @property
    def node_id(self):
        """Gets the node_id of this PodResp.

        应用实例所在节点

        :return: The node_id of this PodResp.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this PodResp.

        应用实例所在节点

        :param node_id: The node_id of this PodResp.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def deployment_id(self):
        """Gets the deployment_id of this PodResp.

        应用ID

        :return: The deployment_id of this PodResp.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this PodResp.

        应用ID

        :param deployment_id: The deployment_id of this PodResp.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def project_id(self):
        """Gets the project_id of this PodResp.

        项目ID

        :return: The project_id of this PodResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PodResp.

        项目ID

        :param project_id: The project_id of this PodResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def reason(self):
        """Gets the reason of this PodResp.

        应用实例故障原因

        :return: The reason of this PodResp.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PodResp.

        应用实例故障原因

        :param reason: The reason of this PodResp.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        """Gets the message of this PodResp.

        应用实例故障详情

        :return: The message of this PodResp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PodResp.

        应用实例故障详情

        :param message: The message of this PodResp.
        :type message: str
        """
        self._message = message

    @property
    def created_at(self):
        """Gets the created_at of this PodResp.

        应用实例创建时间

        :return: The created_at of this PodResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PodResp.

        应用实例创建时间

        :param created_at: The created_at of this PodResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def state(self):
        """Gets the state of this PodResp.

        应用实例状态

        :return: The state of this PodResp.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PodResp.

        应用实例状态

        :param state: The state of this PodResp.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, PodResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
