# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachmentResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'description': 'str',
        'state': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'tags': 'list[Tag]',
        'project_id': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'resource_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'description': 'description',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tags': 'tags',
        'project_id': 'project_id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'resource_project_id': 'resource_project_id'
    }

    def __init__(self, name=None, id=None, description=None, state=None, created_at=None, updated_at=None, tags=None, project_id=None, resource_id=None, resource_type=None, resource_project_id=None):
        r"""AttachmentResponse

        The model defined in huaweicloud sdk

        :param name: 连接名字
        :type name: str
        :param id: 连接ID
        :type id: str
        :param description: 描述信息
        :type description: str
        :param state: 连接状态:pending|available|modifying|deleting|deleted|failed|pending_acceptance|rejected|initiating_request|freezed
        :type state: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param tags: 企业路由器关联tag
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        :param project_id: 项目ID
        :type project_id: str
        :param resource_id: 内部连接关联的资源ID
        :type resource_id: str
        :param resource_type: 内部连接关联的资源类型: - vgw：云专线的虚拟网关 - vpn：vpn网关 -  - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  - vpc：虚拟私有云 -
        :type resource_type: str
        :param resource_project_id: 资源所属项目ID
        :type resource_project_id: str
        """
        
        

        self._name = None
        self._id = None
        self._description = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._tags = None
        self._project_id = None
        self._resource_id = None
        self._resource_type = None
        self._resource_project_id = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.description = description
        self.state = state
        self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if tags is not None:
            self.tags = tags
        self.project_id = project_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        if resource_project_id is not None:
            self.resource_project_id = resource_project_id

    @property
    def name(self):
        r"""Gets the name of this AttachmentResponse.

        连接名字

        :return: The name of this AttachmentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AttachmentResponse.

        连接名字

        :param name: The name of this AttachmentResponse.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this AttachmentResponse.

        连接ID

        :return: The id of this AttachmentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AttachmentResponse.

        连接ID

        :param id: The id of this AttachmentResponse.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this AttachmentResponse.

        描述信息

        :return: The description of this AttachmentResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AttachmentResponse.

        描述信息

        :param description: The description of this AttachmentResponse.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        r"""Gets the state of this AttachmentResponse.

        连接状态:pending|available|modifying|deleting|deleted|failed|pending_acceptance|rejected|initiating_request|freezed

        :return: The state of this AttachmentResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this AttachmentResponse.

        连接状态:pending|available|modifying|deleting|deleted|failed|pending_acceptance|rejected|initiating_request|freezed

        :param state: The state of this AttachmentResponse.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this AttachmentResponse.

        创建时间

        :return: The created_at of this AttachmentResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AttachmentResponse.

        创建时间

        :param created_at: The created_at of this AttachmentResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this AttachmentResponse.

        更新时间

        :return: The updated_at of this AttachmentResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this AttachmentResponse.

        更新时间

        :param updated_at: The updated_at of this AttachmentResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def tags(self):
        r"""Gets the tags of this AttachmentResponse.

        企业路由器关联tag

        :return: The tags of this AttachmentResponse.
        :rtype: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this AttachmentResponse.

        企业路由器关联tag

        :param tags: The tags of this AttachmentResponse.
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        self._tags = tags

    @property
    def project_id(self):
        r"""Gets the project_id of this AttachmentResponse.

        项目ID

        :return: The project_id of this AttachmentResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AttachmentResponse.

        项目ID

        :param project_id: The project_id of this AttachmentResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this AttachmentResponse.

        内部连接关联的资源ID

        :return: The resource_id of this AttachmentResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this AttachmentResponse.

        内部连接关联的资源ID

        :param resource_id: The resource_id of this AttachmentResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this AttachmentResponse.

        内部连接关联的资源类型: - vgw：云专线的虚拟网关 - vpn：vpn网关 -  - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  - vpc：虚拟私有云 -

        :return: The resource_type of this AttachmentResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this AttachmentResponse.

        内部连接关联的资源类型: - vgw：云专线的虚拟网关 - vpn：vpn网关 -  - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  - vpc：虚拟私有云 -

        :param resource_type: The resource_type of this AttachmentResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_project_id(self):
        r"""Gets the resource_project_id of this AttachmentResponse.

        资源所属项目ID

        :return: The resource_project_id of this AttachmentResponse.
        :rtype: str
        """
        return self._resource_project_id

    @resource_project_id.setter
    def resource_project_id(self, resource_project_id):
        r"""Sets the resource_project_id of this AttachmentResponse.

        资源所属项目ID

        :param resource_project_id: The resource_project_id of this AttachmentResponse.
        :type resource_project_id: str
        """
        self._resource_project_id = resource_project_id

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
        if not isinstance(other, AttachmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
