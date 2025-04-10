# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcAttachmentDetails:

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
        'vpc_id': 'str',
        'virsubnet_id': 'str',
        'auto_create_vpc_routes': 'bool',
        'state': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'tags': 'list[Tag]',
        'description': 'str',
        'project_id': 'str',
        'vpc_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vpc_id': 'vpc_id',
        'virsubnet_id': 'virsubnet_id',
        'auto_create_vpc_routes': 'auto_create_vpc_routes',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tags': 'tags',
        'description': 'description',
        'project_id': 'project_id',
        'vpc_project_id': 'vpc_project_id'
    }

    def __init__(self, id=None, name=None, vpc_id=None, virsubnet_id=None, auto_create_vpc_routes=None, state=None, created_at=None, updated_at=None, tags=None, description=None, project_id=None, vpc_project_id=None):
        r"""VpcAttachmentDetails

        The model defined in huaweicloud sdk

        :param id: VPC连接ID
        :type id: str
        :param name: VPC连接名称
        :type name: str
        :param vpc_id: VPC id
        :type vpc_id: str
        :param virsubnet_id: VPC子网id
        :type virsubnet_id: str
        :param auto_create_vpc_routes: 默认为false,当设置true时，会自动为VPC配置10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16三条路由，下一跳指向企业路由器。
        :type auto_create_vpc_routes: bool
        :param state: VPC连接状态:pending|available|modifying|deleting|deleted|failed|initiating_request|rejected|pending_acceptance|freezed
        :type state: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param tags: 标签信息
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        :param description: VPC连接描述信息
        :type description: str
        :param project_id: 项目ID
        :type project_id: str
        :param vpc_project_id: vpc所属项目ID
        :type vpc_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._vpc_id = None
        self._virsubnet_id = None
        self._auto_create_vpc_routes = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._tags = None
        self._description = None
        self._project_id = None
        self._vpc_project_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.vpc_id = vpc_id
        self.virsubnet_id = virsubnet_id
        if auto_create_vpc_routes is not None:
            self.auto_create_vpc_routes = auto_create_vpc_routes
        self.state = state
        self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        self.project_id = project_id
        if vpc_project_id is not None:
            self.vpc_project_id = vpc_project_id

    @property
    def id(self):
        r"""Gets the id of this VpcAttachmentDetails.

        VPC连接ID

        :return: The id of this VpcAttachmentDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VpcAttachmentDetails.

        VPC连接ID

        :param id: The id of this VpcAttachmentDetails.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this VpcAttachmentDetails.

        VPC连接名称

        :return: The name of this VpcAttachmentDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VpcAttachmentDetails.

        VPC连接名称

        :param name: The name of this VpcAttachmentDetails.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this VpcAttachmentDetails.

        VPC id

        :return: The vpc_id of this VpcAttachmentDetails.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this VpcAttachmentDetails.

        VPC id

        :param vpc_id: The vpc_id of this VpcAttachmentDetails.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this VpcAttachmentDetails.

        VPC子网id

        :return: The virsubnet_id of this VpcAttachmentDetails.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this VpcAttachmentDetails.

        VPC子网id

        :param virsubnet_id: The virsubnet_id of this VpcAttachmentDetails.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def auto_create_vpc_routes(self):
        r"""Gets the auto_create_vpc_routes of this VpcAttachmentDetails.

        默认为false,当设置true时，会自动为VPC配置10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16三条路由，下一跳指向企业路由器。

        :return: The auto_create_vpc_routes of this VpcAttachmentDetails.
        :rtype: bool
        """
        return self._auto_create_vpc_routes

    @auto_create_vpc_routes.setter
    def auto_create_vpc_routes(self, auto_create_vpc_routes):
        r"""Sets the auto_create_vpc_routes of this VpcAttachmentDetails.

        默认为false,当设置true时，会自动为VPC配置10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16三条路由，下一跳指向企业路由器。

        :param auto_create_vpc_routes: The auto_create_vpc_routes of this VpcAttachmentDetails.
        :type auto_create_vpc_routes: bool
        """
        self._auto_create_vpc_routes = auto_create_vpc_routes

    @property
    def state(self):
        r"""Gets the state of this VpcAttachmentDetails.

        VPC连接状态:pending|available|modifying|deleting|deleted|failed|initiating_request|rejected|pending_acceptance|freezed

        :return: The state of this VpcAttachmentDetails.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this VpcAttachmentDetails.

        VPC连接状态:pending|available|modifying|deleting|deleted|failed|initiating_request|rejected|pending_acceptance|freezed

        :param state: The state of this VpcAttachmentDetails.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this VpcAttachmentDetails.

        创建时间

        :return: The created_at of this VpcAttachmentDetails.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this VpcAttachmentDetails.

        创建时间

        :param created_at: The created_at of this VpcAttachmentDetails.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this VpcAttachmentDetails.

        更新时间

        :return: The updated_at of this VpcAttachmentDetails.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this VpcAttachmentDetails.

        更新时间

        :param updated_at: The updated_at of this VpcAttachmentDetails.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def tags(self):
        r"""Gets the tags of this VpcAttachmentDetails.

        标签信息

        :return: The tags of this VpcAttachmentDetails.
        :rtype: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this VpcAttachmentDetails.

        标签信息

        :param tags: The tags of this VpcAttachmentDetails.
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        self._tags = tags

    @property
    def description(self):
        r"""Gets the description of this VpcAttachmentDetails.

        VPC连接描述信息

        :return: The description of this VpcAttachmentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VpcAttachmentDetails.

        VPC连接描述信息

        :param description: The description of this VpcAttachmentDetails.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this VpcAttachmentDetails.

        项目ID

        :return: The project_id of this VpcAttachmentDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this VpcAttachmentDetails.

        项目ID

        :param project_id: The project_id of this VpcAttachmentDetails.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def vpc_project_id(self):
        r"""Gets the vpc_project_id of this VpcAttachmentDetails.

        vpc所属项目ID

        :return: The vpc_project_id of this VpcAttachmentDetails.
        :rtype: str
        """
        return self._vpc_project_id

    @vpc_project_id.setter
    def vpc_project_id(self, vpc_project_id):
        r"""Sets the vpc_project_id of this VpcAttachmentDetails.

        vpc所属项目ID

        :param vpc_project_id: The vpc_project_id of this VpcAttachmentDetails.
        :type vpc_project_id: str
        """
        self._vpc_project_id = vpc_project_id

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
        if not isinstance(other, VpcAttachmentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
