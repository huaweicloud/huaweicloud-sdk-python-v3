# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachmentDetails:

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
        'description': 'str',
        'state': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'tags': 'list[Tag]',
        'project_id': 'str',
        'er_id': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'resource_project_id': 'str',
        'associated': 'bool',
        'route_table_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tags': 'tags',
        'project_id': 'project_id',
        'er_id': 'er_id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'resource_project_id': 'resource_project_id',
        'associated': 'associated',
        'route_table_id': 'route_table_id'
    }

    def __init__(self, id=None, name=None, description=None, state=None, created_at=None, updated_at=None, tags=None, project_id=None, er_id=None, resource_id=None, resource_type=None, resource_project_id=None, associated=None, route_table_id=None):
        """AttachmentDetails

        The model defined in huaweicloud sdk

        :param id: 连接ID
        :type id: str
        :param name: 连接名字
        :type name: str
        :param description: 描述信息
        :type description: str
        :param state: 连接状态:pending|available|modifying|deleting|deleted|failed|pending_acceptance|rejected|initiating_request
        :type state: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param tags: 企业路由器关联tag
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        :param project_id: 项目ID
        :type project_id: str
        :param er_id: er id
        :type er_id: str
        :param resource_id: 内部连接关联的资源ID
        :type resource_id: str
        :param resource_type: - vgw：云专线的虚拟网关 - vpn：vpn网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接
        :type resource_type: str
        :param resource_project_id: 资源所属项目ID
        :type resource_project_id: str
        :param associated: 表示此连接是否被关联
        :type associated: bool
        :param route_table_id: 关联路由表id
        :type route_table_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._tags = None
        self._project_id = None
        self._er_id = None
        self._resource_id = None
        self._resource_type = None
        self._resource_project_id = None
        self._associated = None
        self._route_table_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if tags is not None:
            self.tags = tags
        self.project_id = project_id
        if er_id is not None:
            self.er_id = er_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        if resource_project_id is not None:
            self.resource_project_id = resource_project_id
        if associated is not None:
            self.associated = associated
        if route_table_id is not None:
            self.route_table_id = route_table_id

    @property
    def id(self):
        """Gets the id of this AttachmentDetails.

        连接ID

        :return: The id of this AttachmentDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AttachmentDetails.

        连接ID

        :param id: The id of this AttachmentDetails.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AttachmentDetails.

        连接名字

        :return: The name of this AttachmentDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttachmentDetails.

        连接名字

        :param name: The name of this AttachmentDetails.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AttachmentDetails.

        描述信息

        :return: The description of this AttachmentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AttachmentDetails.

        描述信息

        :param description: The description of this AttachmentDetails.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        """Gets the state of this AttachmentDetails.

        连接状态:pending|available|modifying|deleting|deleted|failed|pending_acceptance|rejected|initiating_request

        :return: The state of this AttachmentDetails.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AttachmentDetails.

        连接状态:pending|available|modifying|deleting|deleted|failed|pending_acceptance|rejected|initiating_request

        :param state: The state of this AttachmentDetails.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        """Gets the created_at of this AttachmentDetails.

        创建时间

        :return: The created_at of this AttachmentDetails.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AttachmentDetails.

        创建时间

        :param created_at: The created_at of this AttachmentDetails.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AttachmentDetails.

        更新时间

        :return: The updated_at of this AttachmentDetails.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AttachmentDetails.

        更新时间

        :param updated_at: The updated_at of this AttachmentDetails.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def tags(self):
        """Gets the tags of this AttachmentDetails.

        企业路由器关联tag

        :return: The tags of this AttachmentDetails.
        :rtype: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AttachmentDetails.

        企业路由器关联tag

        :param tags: The tags of this AttachmentDetails.
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        self._tags = tags

    @property
    def project_id(self):
        """Gets the project_id of this AttachmentDetails.

        项目ID

        :return: The project_id of this AttachmentDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AttachmentDetails.

        项目ID

        :param project_id: The project_id of this AttachmentDetails.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def er_id(self):
        """Gets the er_id of this AttachmentDetails.

        er id

        :return: The er_id of this AttachmentDetails.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        """Sets the er_id of this AttachmentDetails.

        er id

        :param er_id: The er_id of this AttachmentDetails.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def resource_id(self):
        """Gets the resource_id of this AttachmentDetails.

        内部连接关联的资源ID

        :return: The resource_id of this AttachmentDetails.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this AttachmentDetails.

        内部连接关联的资源ID

        :param resource_id: The resource_id of this AttachmentDetails.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this AttachmentDetails.

        - vgw：云专线的虚拟网关 - vpn：vpn网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接

        :return: The resource_type of this AttachmentDetails.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AttachmentDetails.

        - vgw：云专线的虚拟网关 - vpn：vpn网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接

        :param resource_type: The resource_type of this AttachmentDetails.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_project_id(self):
        """Gets the resource_project_id of this AttachmentDetails.

        资源所属项目ID

        :return: The resource_project_id of this AttachmentDetails.
        :rtype: str
        """
        return self._resource_project_id

    @resource_project_id.setter
    def resource_project_id(self, resource_project_id):
        """Sets the resource_project_id of this AttachmentDetails.

        资源所属项目ID

        :param resource_project_id: The resource_project_id of this AttachmentDetails.
        :type resource_project_id: str
        """
        self._resource_project_id = resource_project_id

    @property
    def associated(self):
        """Gets the associated of this AttachmentDetails.

        表示此连接是否被关联

        :return: The associated of this AttachmentDetails.
        :rtype: bool
        """
        return self._associated

    @associated.setter
    def associated(self, associated):
        """Sets the associated of this AttachmentDetails.

        表示此连接是否被关联

        :param associated: The associated of this AttachmentDetails.
        :type associated: bool
        """
        self._associated = associated

    @property
    def route_table_id(self):
        """Gets the route_table_id of this AttachmentDetails.

        关联路由表id

        :return: The route_table_id of this AttachmentDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this AttachmentDetails.

        关联路由表id

        :param route_table_id: The route_table_id of this AttachmentDetails.
        :type route_table_id: str
        """
        self._route_table_id = route_table_id

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
        if not isinstance(other, AttachmentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
