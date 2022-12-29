# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDeploymentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template': 'DeploymentTemplate',
        'reason': 'str',
        'ready_replicas': 'int',
        'replicas': 'int',
        'description': 'str',
        'created_at': 'str',
        'source': 'str',
        'api_version': 'str',
        'node_ids': 'list[str]',
        'cluster_id': 'str',
        'updated_at': 'str',
        'project_id': 'str',
        'name': 'str',
        'id': 'str',
        'state': 'str',
        'node_num': 'int',
        'result': 'list[NodeResult]'
    }

    attribute_map = {
        'template': 'template',
        'reason': 'reason',
        'ready_replicas': 'ready_replicas',
        'replicas': 'replicas',
        'description': 'description',
        'created_at': 'created_at',
        'source': 'source',
        'api_version': 'api_version',
        'node_ids': 'node_ids',
        'cluster_id': 'cluster_id',
        'updated_at': 'updated_at',
        'project_id': 'project_id',
        'name': 'name',
        'id': 'id',
        'state': 'state',
        'node_num': 'node_num',
        'result': 'result'
    }

    def __init__(self, template=None, reason=None, ready_replicas=None, replicas=None, description=None, created_at=None, source=None, api_version=None, node_ids=None, cluster_id=None, updated_at=None, project_id=None, name=None, id=None, state=None, node_num=None, result=None):
        """UpdateDeploymentResponse

        The model defined in huaweicloud sdk

        :param template: 
        :type template: :class:`huaweicloudsdkhilens.v3.DeploymentTemplate`
        :param reason: 部署成功失败的理由
        :type reason: str
        :param ready_replicas: 已经就绪的实例节点数
        :type ready_replicas: int
        :param replicas: 实例节点节点数
        :type replicas: int
        :param description: 应用部署描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param created_at: 创建时间
        :type created_at: str
        :param source: 应用部署来源: HiLens市场(hlm) or aigallery(aig) or 自定义(userdefined)
        :type source: str
        :param api_version: 应用部署版本
        :type api_version: str
        :param node_ids: 应用部署的指定节点，与clouster_id二选一
        :type node_ids: list[str]
        :param cluster_id: 应用部署的集群ID，与node_id二选一
        :type cluster_id: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param project_id: 项目ID
        :type project_id: str
        :param name: 部署名称
        :type name: str
        :param id: 部署ID
        :type id: str
        :param state: RUNNING：运行， FREEZE：冻结， UNFREEZE: 解冻， CREATING：创建中， CREATE_FAILED：创建失败， STARTING：启动中， START_FAILED：启动失败， STOPPING：停止中 STOP_FAILED：停止失败 DELETING：删除中 DELETE_FIALED：删除失败 HIBERNATED：休眠
        :type state: str
        :param node_num: 部署的节点数，最小为1，集群部署也为1
        :type node_num: int
        :param result: 每个节点的部署结果
        :type result: list[:class:`huaweicloudsdkhilens.v3.NodeResult`]
        """
        
        super(UpdateDeploymentResponse, self).__init__()

        self._template = None
        self._reason = None
        self._ready_replicas = None
        self._replicas = None
        self._description = None
        self._created_at = None
        self._source = None
        self._api_version = None
        self._node_ids = None
        self._cluster_id = None
        self._updated_at = None
        self._project_id = None
        self._name = None
        self._id = None
        self._state = None
        self._node_num = None
        self._result = None
        self.discriminator = None

        if template is not None:
            self.template = template
        if reason is not None:
            self.reason = reason
        if ready_replicas is not None:
            self.ready_replicas = ready_replicas
        if replicas is not None:
            self.replicas = replicas
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if source is not None:
            self.source = source
        if api_version is not None:
            self.api_version = api_version
        if node_ids is not None:
            self.node_ids = node_ids
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
        if state is not None:
            self.state = state
        if node_num is not None:
            self.node_num = node_num
        if result is not None:
            self.result = result

    @property
    def template(self):
        """Gets the template of this UpdateDeploymentResponse.

        :return: The template of this UpdateDeploymentResponse.
        :rtype: :class:`huaweicloudsdkhilens.v3.DeploymentTemplate`
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this UpdateDeploymentResponse.

        :param template: The template of this UpdateDeploymentResponse.
        :type template: :class:`huaweicloudsdkhilens.v3.DeploymentTemplate`
        """
        self._template = template

    @property
    def reason(self):
        """Gets the reason of this UpdateDeploymentResponse.

        部署成功失败的理由

        :return: The reason of this UpdateDeploymentResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this UpdateDeploymentResponse.

        部署成功失败的理由

        :param reason: The reason of this UpdateDeploymentResponse.
        :type reason: str
        """
        self._reason = reason

    @property
    def ready_replicas(self):
        """Gets the ready_replicas of this UpdateDeploymentResponse.

        已经就绪的实例节点数

        :return: The ready_replicas of this UpdateDeploymentResponse.
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas):
        """Sets the ready_replicas of this UpdateDeploymentResponse.

        已经就绪的实例节点数

        :param ready_replicas: The ready_replicas of this UpdateDeploymentResponse.
        :type ready_replicas: int
        """
        self._ready_replicas = ready_replicas

    @property
    def replicas(self):
        """Gets the replicas of this UpdateDeploymentResponse.

        实例节点节点数

        :return: The replicas of this UpdateDeploymentResponse.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this UpdateDeploymentResponse.

        实例节点节点数

        :param replicas: The replicas of this UpdateDeploymentResponse.
        :type replicas: int
        """
        self._replicas = replicas

    @property
    def description(self):
        """Gets the description of this UpdateDeploymentResponse.

        应用部署描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this UpdateDeploymentResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDeploymentResponse.

        应用部署描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this UpdateDeploymentResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this UpdateDeploymentResponse.

        创建时间

        :return: The created_at of this UpdateDeploymentResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UpdateDeploymentResponse.

        创建时间

        :param created_at: The created_at of this UpdateDeploymentResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def source(self):
        """Gets the source of this UpdateDeploymentResponse.

        应用部署来源: HiLens市场(hlm) or aigallery(aig) or 自定义(userdefined)

        :return: The source of this UpdateDeploymentResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this UpdateDeploymentResponse.

        应用部署来源: HiLens市场(hlm) or aigallery(aig) or 自定义(userdefined)

        :param source: The source of this UpdateDeploymentResponse.
        :type source: str
        """
        self._source = source

    @property
    def api_version(self):
        """Gets the api_version of this UpdateDeploymentResponse.

        应用部署版本

        :return: The api_version of this UpdateDeploymentResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this UpdateDeploymentResponse.

        应用部署版本

        :param api_version: The api_version of this UpdateDeploymentResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def node_ids(self):
        """Gets the node_ids of this UpdateDeploymentResponse.

        应用部署的指定节点，与clouster_id二选一

        :return: The node_ids of this UpdateDeploymentResponse.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        """Sets the node_ids of this UpdateDeploymentResponse.

        应用部署的指定节点，与clouster_id二选一

        :param node_ids: The node_ids of this UpdateDeploymentResponse.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpdateDeploymentResponse.

        应用部署的集群ID，与node_id二选一

        :return: The cluster_id of this UpdateDeploymentResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpdateDeploymentResponse.

        应用部署的集群ID，与node_id二选一

        :param cluster_id: The cluster_id of this UpdateDeploymentResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def updated_at(self):
        """Gets the updated_at of this UpdateDeploymentResponse.

        更新时间

        :return: The updated_at of this UpdateDeploymentResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UpdateDeploymentResponse.

        更新时间

        :param updated_at: The updated_at of this UpdateDeploymentResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        """Gets the project_id of this UpdateDeploymentResponse.

        项目ID

        :return: The project_id of this UpdateDeploymentResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateDeploymentResponse.

        项目ID

        :param project_id: The project_id of this UpdateDeploymentResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this UpdateDeploymentResponse.

        部署名称

        :return: The name of this UpdateDeploymentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDeploymentResponse.

        部署名称

        :param name: The name of this UpdateDeploymentResponse.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this UpdateDeploymentResponse.

        部署ID

        :return: The id of this UpdateDeploymentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateDeploymentResponse.

        部署ID

        :param id: The id of this UpdateDeploymentResponse.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        """Gets the state of this UpdateDeploymentResponse.

        RUNNING：运行， FREEZE：冻结， UNFREEZE: 解冻， CREATING：创建中， CREATE_FAILED：创建失败， STARTING：启动中， START_FAILED：启动失败， STOPPING：停止中 STOP_FAILED：停止失败 DELETING：删除中 DELETE_FIALED：删除失败 HIBERNATED：休眠

        :return: The state of this UpdateDeploymentResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UpdateDeploymentResponse.

        RUNNING：运行， FREEZE：冻结， UNFREEZE: 解冻， CREATING：创建中， CREATE_FAILED：创建失败， STARTING：启动中， START_FAILED：启动失败， STOPPING：停止中 STOP_FAILED：停止失败 DELETING：删除中 DELETE_FIALED：删除失败 HIBERNATED：休眠

        :param state: The state of this UpdateDeploymentResponse.
        :type state: str
        """
        self._state = state

    @property
    def node_num(self):
        """Gets the node_num of this UpdateDeploymentResponse.

        部署的节点数，最小为1，集群部署也为1

        :return: The node_num of this UpdateDeploymentResponse.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this UpdateDeploymentResponse.

        部署的节点数，最小为1，集群部署也为1

        :param node_num: The node_num of this UpdateDeploymentResponse.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def result(self):
        """Gets the result of this UpdateDeploymentResponse.

        每个节点的部署结果

        :return: The result of this UpdateDeploymentResponse.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.NodeResult`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this UpdateDeploymentResponse.

        每个节点的部署结果

        :param result: The result of this UpdateDeploymentResponse.
        :type result: list[:class:`huaweicloudsdkhilens.v3.NodeResult`]
        """
        self._result = result

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
        if not isinstance(other, UpdateDeploymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
