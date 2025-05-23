# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentResp:

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
        'replicas': 'int',
        'ready_replicas': 'int',
        'description': 'str',
        'group_id': 'str',
        'node_ids': 'list[str]',
        'tags': 'list[Attributes]',
        'api_version': 'str',
        'source': 'str',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'template': 'PodRequest',
        'state': 'str',
        'source_id': 'str',
        'annotations': 'Annotations'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'replicas': 'replicas',
        'ready_replicas': 'ready_replicas',
        'description': 'description',
        'group_id': 'group_id',
        'node_ids': 'node_ids',
        'tags': 'tags',
        'api_version': 'api_version',
        'source': 'source',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'template': 'template',
        'state': 'state',
        'source_id': 'source_id',
        'annotations': 'annotations'
    }

    def __init__(self, id=None, name=None, replicas=None, ready_replicas=None, description=None, group_id=None, node_ids=None, tags=None, api_version=None, source=None, project_id=None, created_at=None, updated_at=None, template=None, state=None, source_id=None, annotations=None):
        r"""DeploymentResp

        The model defined in huaweicloud sdk

        :param id: 应用部署uuid
        :type id: str
        :param name: 应用部署名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾
        :type name: str
        :param replicas: 应用部署总副本数
        :type replicas: int
        :param ready_replicas: 应用部署正常副本数
        :type ready_replicas: int
        :param description: 应用部署描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param group_id: 应用部署到指定节点组，与node_ids二选一
        :type group_id: str
        :param node_ids: 应用部署到指定节点，当前只支持一个边缘节点
        :type node_ids: list[str]
        :param tags: 节点属性
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        :param api_version: 应用部署版本
        :type api_version: str
        :param source: 应用部署来源：边缘市场（iem）或自定义（userdefined）
        :type source: str
        :param project_id: 项目ID
        :type project_id: str
        :param created_at: 应用部署创建时间
        :type created_at: str
        :param updated_at: 应用部署更新时间
        :type updated_at: str
        :param template: 
        :type template: :class:`huaweicloudsdkief.v1.PodRequest`
        :param state: 应用状态，仅包括冻结（FREEZE）、删除中（PENDING_DELETE）、删除失败（DELETE_FAILED），保留字段
        :type state: str
        :param source_id: 预留字段
        :type source_id: str
        :param annotations: 
        :type annotations: :class:`huaweicloudsdkief.v1.Annotations`
        """
        
        

        self._id = None
        self._name = None
        self._replicas = None
        self._ready_replicas = None
        self._description = None
        self._group_id = None
        self._node_ids = None
        self._tags = None
        self._api_version = None
        self._source = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._template = None
        self._state = None
        self._source_id = None
        self._annotations = None
        self.discriminator = None

        self.id = id
        self.name = name
        if replicas is not None:
            self.replicas = replicas
        if ready_replicas is not None:
            self.ready_replicas = ready_replicas
        if description is not None:
            self.description = description
        if group_id is not None:
            self.group_id = group_id
        self.node_ids = node_ids
        if tags is not None:
            self.tags = tags
        if api_version is not None:
            self.api_version = api_version
        if source is not None:
            self.source = source
        if project_id is not None:
            self.project_id = project_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.template = template
        if state is not None:
            self.state = state
        if source_id is not None:
            self.source_id = source_id
        if annotations is not None:
            self.annotations = annotations

    @property
    def id(self):
        r"""Gets the id of this DeploymentResp.

        应用部署uuid

        :return: The id of this DeploymentResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeploymentResp.

        应用部署uuid

        :param id: The id of this DeploymentResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DeploymentResp.

        应用部署名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾

        :return: The name of this DeploymentResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DeploymentResp.

        应用部署名称，只允许英文小写字母、数字、中划线，最大长度32， 英文小写字母或数字开头和结尾

        :param name: The name of this DeploymentResp.
        :type name: str
        """
        self._name = name

    @property
    def replicas(self):
        r"""Gets the replicas of this DeploymentResp.

        应用部署总副本数

        :return: The replicas of this DeploymentResp.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        r"""Sets the replicas of this DeploymentResp.

        应用部署总副本数

        :param replicas: The replicas of this DeploymentResp.
        :type replicas: int
        """
        self._replicas = replicas

    @property
    def ready_replicas(self):
        r"""Gets the ready_replicas of this DeploymentResp.

        应用部署正常副本数

        :return: The ready_replicas of this DeploymentResp.
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas):
        r"""Sets the ready_replicas of this DeploymentResp.

        应用部署正常副本数

        :param ready_replicas: The ready_replicas of this DeploymentResp.
        :type ready_replicas: int
        """
        self._ready_replicas = ready_replicas

    @property
    def description(self):
        r"""Gets the description of this DeploymentResp.

        应用部署描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this DeploymentResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DeploymentResp.

        应用部署描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this DeploymentResp.
        :type description: str
        """
        self._description = description

    @property
    def group_id(self):
        r"""Gets the group_id of this DeploymentResp.

        应用部署到指定节点组，与node_ids二选一

        :return: The group_id of this DeploymentResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this DeploymentResp.

        应用部署到指定节点组，与node_ids二选一

        :param group_id: The group_id of this DeploymentResp.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def node_ids(self):
        r"""Gets the node_ids of this DeploymentResp.

        应用部署到指定节点，当前只支持一个边缘节点

        :return: The node_ids of this DeploymentResp.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this DeploymentResp.

        应用部署到指定节点，当前只支持一个边缘节点

        :param node_ids: The node_ids of this DeploymentResp.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def tags(self):
        r"""Gets the tags of this DeploymentResp.

        节点属性

        :return: The tags of this DeploymentResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this DeploymentResp.

        节点属性

        :param tags: The tags of this DeploymentResp.
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        self._tags = tags

    @property
    def api_version(self):
        r"""Gets the api_version of this DeploymentResp.

        应用部署版本

        :return: The api_version of this DeploymentResp.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this DeploymentResp.

        应用部署版本

        :param api_version: The api_version of this DeploymentResp.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def source(self):
        r"""Gets the source of this DeploymentResp.

        应用部署来源：边缘市场（iem）或自定义（userdefined）

        :return: The source of this DeploymentResp.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this DeploymentResp.

        应用部署来源：边缘市场（iem）或自定义（userdefined）

        :param source: The source of this DeploymentResp.
        :type source: str
        """
        self._source = source

    @property
    def project_id(self):
        r"""Gets the project_id of this DeploymentResp.

        项目ID

        :return: The project_id of this DeploymentResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DeploymentResp.

        项目ID

        :param project_id: The project_id of this DeploymentResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this DeploymentResp.

        应用部署创建时间

        :return: The created_at of this DeploymentResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this DeploymentResp.

        应用部署创建时间

        :param created_at: The created_at of this DeploymentResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this DeploymentResp.

        应用部署更新时间

        :return: The updated_at of this DeploymentResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this DeploymentResp.

        应用部署更新时间

        :param updated_at: The updated_at of this DeploymentResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def template(self):
        r"""Gets the template of this DeploymentResp.

        :return: The template of this DeploymentResp.
        :rtype: :class:`huaweicloudsdkief.v1.PodRequest`
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this DeploymentResp.

        :param template: The template of this DeploymentResp.
        :type template: :class:`huaweicloudsdkief.v1.PodRequest`
        """
        self._template = template

    @property
    def state(self):
        r"""Gets the state of this DeploymentResp.

        应用状态，仅包括冻结（FREEZE）、删除中（PENDING_DELETE）、删除失败（DELETE_FAILED），保留字段

        :return: The state of this DeploymentResp.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this DeploymentResp.

        应用状态，仅包括冻结（FREEZE）、删除中（PENDING_DELETE）、删除失败（DELETE_FAILED），保留字段

        :param state: The state of this DeploymentResp.
        :type state: str
        """
        self._state = state

    @property
    def source_id(self):
        r"""Gets the source_id of this DeploymentResp.

        预留字段

        :return: The source_id of this DeploymentResp.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this DeploymentResp.

        预留字段

        :param source_id: The source_id of this DeploymentResp.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def annotations(self):
        r"""Gets the annotations of this DeploymentResp.

        :return: The annotations of this DeploymentResp.
        :rtype: :class:`huaweicloudsdkief.v1.Annotations`
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this DeploymentResp.

        :param annotations: The annotations of this DeploymentResp.
        :type annotations: :class:`huaweicloudsdkief.v1.Annotations`
        """
        self._annotations = annotations

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
        if not isinstance(other, DeploymentResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
