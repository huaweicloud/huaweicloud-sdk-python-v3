# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Pod:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configs': 'PodConfig',
        'reason': 'str',
        'host_ip': 'str',
        'created_at': 'str',
        'cluster_id': 'str',
        'updated_at': 'str',
        'project_id': 'str',
        'name': 'str',
        'id': 'str',
        'deployment_id': 'str',
        'affinity': 'PodAffinity',
        'apps': 'list[AppDef]',
        'node_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'configs': 'configs',
        'reason': 'reason',
        'host_ip': 'host_ip',
        'created_at': 'created_at',
        'cluster_id': 'cluster_id',
        'updated_at': 'updated_at',
        'project_id': 'project_id',
        'name': 'name',
        'id': 'id',
        'deployment_id': 'deployment_id',
        'affinity': 'affinity',
        'apps': 'apps',
        'node_id': 'node_id',
        'status': 'status'
    }

    def __init__(self, configs=None, reason=None, host_ip=None, created_at=None, cluster_id=None, updated_at=None, project_id=None, name=None, id=None, deployment_id=None, affinity=None, apps=None, node_id=None, status=None):
        """Pod

        The model defined in huaweicloud sdk

        :param configs: 
        :type configs: :class:`huaweicloudsdkhilens.v3.PodConfig`
        :param reason: 部署失败的原因
        :type reason: str
        :param host_ip: 对应网卡地址
        :type host_ip: str
        :param created_at: 创建时间
        :type created_at: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param project_id: 项目ID
        :type project_id: str
        :param name: 实例名字
        :type name: str
        :param id: 实例ID
        :type id: str
        :param deployment_id: 部署ID
        :type deployment_id: str
        :param affinity: 
        :type affinity: :class:`huaweicloudsdkhilens.v3.PodAffinity`
        :param apps: 应用部署信息
        :type apps: list[:class:`huaweicloudsdkhilens.v3.AppDef`]
        :param node_id: 节点ID
        :type node_id: str
        :param status: 状态，状态包括，Pending，表示挂起，Running表示pod已经被调到到某节点，Succeeded表示Pod已经被成功终止，Failed表示左右容器都已终止，Unkonwn表示无法取得Pod状态
        :type status: str
        """
        
        

        self._configs = None
        self._reason = None
        self._host_ip = None
        self._created_at = None
        self._cluster_id = None
        self._updated_at = None
        self._project_id = None
        self._name = None
        self._id = None
        self._deployment_id = None
        self._affinity = None
        self._apps = None
        self._node_id = None
        self._status = None
        self.discriminator = None

        if configs is not None:
            self.configs = configs
        if reason is not None:
            self.reason = reason
        if host_ip is not None:
            self.host_ip = host_ip
        if created_at is not None:
            self.created_at = created_at
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if updated_at is not None:
            self.updated_at = updated_at
        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if deployment_id is not None:
            self.deployment_id = deployment_id
        if affinity is not None:
            self.affinity = affinity
        if apps is not None:
            self.apps = apps
        if node_id is not None:
            self.node_id = node_id
        if status is not None:
            self.status = status

    @property
    def configs(self):
        """Gets the configs of this Pod.

        :return: The configs of this Pod.
        :rtype: :class:`huaweicloudsdkhilens.v3.PodConfig`
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this Pod.

        :param configs: The configs of this Pod.
        :type configs: :class:`huaweicloudsdkhilens.v3.PodConfig`
        """
        self._configs = configs

    @property
    def reason(self):
        """Gets the reason of this Pod.

        部署失败的原因

        :return: The reason of this Pod.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Pod.

        部署失败的原因

        :param reason: The reason of this Pod.
        :type reason: str
        """
        self._reason = reason

    @property
    def host_ip(self):
        """Gets the host_ip of this Pod.

        对应网卡地址

        :return: The host_ip of this Pod.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this Pod.

        对应网卡地址

        :param host_ip: The host_ip of this Pod.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def created_at(self):
        """Gets the created_at of this Pod.

        创建时间

        :return: The created_at of this Pod.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Pod.

        创建时间

        :param created_at: The created_at of this Pod.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def cluster_id(self):
        """Gets the cluster_id of this Pod.

        集群ID

        :return: The cluster_id of this Pod.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this Pod.

        集群ID

        :param cluster_id: The cluster_id of this Pod.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def updated_at(self):
        """Gets the updated_at of this Pod.

        更新时间

        :return: The updated_at of this Pod.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Pod.

        更新时间

        :param updated_at: The updated_at of this Pod.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        """Gets the project_id of this Pod.

        项目ID

        :return: The project_id of this Pod.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Pod.

        项目ID

        :param project_id: The project_id of this Pod.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this Pod.

        实例名字

        :return: The name of this Pod.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Pod.

        实例名字

        :param name: The name of this Pod.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this Pod.

        实例ID

        :return: The id of this Pod.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Pod.

        实例ID

        :param id: The id of this Pod.
        :type id: str
        """
        self._id = id

    @property
    def deployment_id(self):
        """Gets the deployment_id of this Pod.

        部署ID

        :return: The deployment_id of this Pod.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this Pod.

        部署ID

        :param deployment_id: The deployment_id of this Pod.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def affinity(self):
        """Gets the affinity of this Pod.

        :return: The affinity of this Pod.
        :rtype: :class:`huaweicloudsdkhilens.v3.PodAffinity`
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this Pod.

        :param affinity: The affinity of this Pod.
        :type affinity: :class:`huaweicloudsdkhilens.v3.PodAffinity`
        """
        self._affinity = affinity

    @property
    def apps(self):
        """Gets the apps of this Pod.

        应用部署信息

        :return: The apps of this Pod.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.AppDef`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this Pod.

        应用部署信息

        :param apps: The apps of this Pod.
        :type apps: list[:class:`huaweicloudsdkhilens.v3.AppDef`]
        """
        self._apps = apps

    @property
    def node_id(self):
        """Gets the node_id of this Pod.

        节点ID

        :return: The node_id of this Pod.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this Pod.

        节点ID

        :param node_id: The node_id of this Pod.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def status(self):
        """Gets the status of this Pod.

        状态，状态包括，Pending，表示挂起，Running表示pod已经被调到到某节点，Succeeded表示Pod已经被成功终止，Failed表示左右容器都已终止，Unkonwn表示无法取得Pod状态

        :return: The status of this Pod.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Pod.

        状态，状态包括，Pending，表示挂起，Running表示pod已经被调到到某节点，Succeeded表示Pod已经被成功终止，Failed表示左右容器都已终止，Unkonwn表示无法取得Pod状态

        :param status: The status of this Pod.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, Pod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
