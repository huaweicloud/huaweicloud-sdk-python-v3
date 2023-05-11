# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnterpriseRouter:

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
        'tags': 'list[Tag]',
        'charge_mode': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'enterprise_project_id': 'str',
        'project_id': 'str',
        'asn': 'int',
        'enable_default_propagation': 'bool',
        'enable_default_association': 'bool',
        'default_propagation_route_table_id': 'str',
        'default_association_route_table_id': 'str',
        'availability_zone_ids': 'list[str]',
        'auto_accept_shared_attachments': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'state': 'state',
        'tags': 'tags',
        'charge_mode': 'charge_mode',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'enterprise_project_id': 'enterprise_project_id',
        'project_id': 'project_id',
        'asn': 'asn',
        'enable_default_propagation': 'enable_default_propagation',
        'enable_default_association': 'enable_default_association',
        'default_propagation_route_table_id': 'default_propagation_route_table_id',
        'default_association_route_table_id': 'default_association_route_table_id',
        'availability_zone_ids': 'availability_zone_ids',
        'auto_accept_shared_attachments': 'auto_accept_shared_attachments'
    }

    def __init__(self, id=None, name=None, description=None, state=None, tags=None, charge_mode=None, created_at=None, updated_at=None, enterprise_project_id=None, project_id=None, asn=None, enable_default_propagation=None, enable_default_association=None, default_propagation_route_table_id=None, default_association_route_table_id=None, availability_zone_ids=None, auto_accept_shared_attachments=None):
        """EnterpriseRouter

        The model defined in huaweicloud sdk

        :param id: 企业路由器实例的ID
        :type id: str
        :param name: 企业路由器实例名称
        :type name: str
        :param description: 企业路由器实例描述信息
        :type description: str
        :param state: 运行状态
        :type state: str
        :param tags: 标签信息
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        :param charge_mode: 计费模式 按需
        :type charge_mode: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param asn: 企业路由器实例的BGP AS号
        :type asn: int
        :param enable_default_propagation: 是否开启默认路由表传播，默认false不开启
        :type enable_default_propagation: bool
        :param enable_default_association: 是否开启默认路由表关联，默认false不开启
        :type enable_default_association: bool
        :param default_propagation_route_table_id: 默认传播路由表id
        :type default_propagation_route_table_id: str
        :param default_association_route_table_id: 默认关联路由表id
        :type default_association_route_table_id: str
        :param availability_zone_ids: 企业路由器所在可用区信息
        :type availability_zone_ids: list[str]
        :param auto_accept_shared_attachments: 是否自动接受共享连接创建，默认false不开启
        :type auto_accept_shared_attachments: bool
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._state = None
        self._tags = None
        self._charge_mode = None
        self._created_at = None
        self._updated_at = None
        self._enterprise_project_id = None
        self._project_id = None
        self._asn = None
        self._enable_default_propagation = None
        self._enable_default_association = None
        self._default_propagation_route_table_id = None
        self._default_association_route_table_id = None
        self._availability_zone_ids = None
        self._auto_accept_shared_attachments = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.state = state
        if tags is not None:
            self.tags = tags
        if charge_mode is not None:
            self.charge_mode = charge_mode
        self.created_at = created_at
        self.updated_at = updated_at
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.project_id = project_id
        self.asn = asn
        self.enable_default_propagation = enable_default_propagation
        self.enable_default_association = enable_default_association
        if default_propagation_route_table_id is not None:
            self.default_propagation_route_table_id = default_propagation_route_table_id
        if default_association_route_table_id is not None:
            self.default_association_route_table_id = default_association_route_table_id
        self.availability_zone_ids = availability_zone_ids
        if auto_accept_shared_attachments is not None:
            self.auto_accept_shared_attachments = auto_accept_shared_attachments

    @property
    def id(self):
        """Gets the id of this EnterpriseRouter.

        企业路由器实例的ID

        :return: The id of this EnterpriseRouter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnterpriseRouter.

        企业路由器实例的ID

        :param id: The id of this EnterpriseRouter.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EnterpriseRouter.

        企业路由器实例名称

        :return: The name of this EnterpriseRouter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnterpriseRouter.

        企业路由器实例名称

        :param name: The name of this EnterpriseRouter.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EnterpriseRouter.

        企业路由器实例描述信息

        :return: The description of this EnterpriseRouter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnterpriseRouter.

        企业路由器实例描述信息

        :param description: The description of this EnterpriseRouter.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        """Gets the state of this EnterpriseRouter.

        运行状态

        :return: The state of this EnterpriseRouter.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EnterpriseRouter.

        运行状态

        :param state: The state of this EnterpriseRouter.
        :type state: str
        """
        self._state = state

    @property
    def tags(self):
        """Gets the tags of this EnterpriseRouter.

        标签信息

        :return: The tags of this EnterpriseRouter.
        :rtype: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EnterpriseRouter.

        标签信息

        :param tags: The tags of this EnterpriseRouter.
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        self._tags = tags

    @property
    def charge_mode(self):
        """Gets the charge_mode of this EnterpriseRouter.

        计费模式 按需

        :return: The charge_mode of this EnterpriseRouter.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this EnterpriseRouter.

        计费模式 按需

        :param charge_mode: The charge_mode of this EnterpriseRouter.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def created_at(self):
        """Gets the created_at of this EnterpriseRouter.

        创建时间

        :return: The created_at of this EnterpriseRouter.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EnterpriseRouter.

        创建时间

        :param created_at: The created_at of this EnterpriseRouter.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EnterpriseRouter.

        更新时间

        :return: The updated_at of this EnterpriseRouter.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EnterpriseRouter.

        更新时间

        :param updated_at: The updated_at of this EnterpriseRouter.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this EnterpriseRouter.

        企业项目ID

        :return: The enterprise_project_id of this EnterpriseRouter.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this EnterpriseRouter.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this EnterpriseRouter.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        """Gets the project_id of this EnterpriseRouter.

        项目ID

        :return: The project_id of this EnterpriseRouter.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this EnterpriseRouter.

        项目ID

        :param project_id: The project_id of this EnterpriseRouter.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def asn(self):
        """Gets the asn of this EnterpriseRouter.

        企业路由器实例的BGP AS号

        :return: The asn of this EnterpriseRouter.
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this EnterpriseRouter.

        企业路由器实例的BGP AS号

        :param asn: The asn of this EnterpriseRouter.
        :type asn: int
        """
        self._asn = asn

    @property
    def enable_default_propagation(self):
        """Gets the enable_default_propagation of this EnterpriseRouter.

        是否开启默认路由表传播，默认false不开启

        :return: The enable_default_propagation of this EnterpriseRouter.
        :rtype: bool
        """
        return self._enable_default_propagation

    @enable_default_propagation.setter
    def enable_default_propagation(self, enable_default_propagation):
        """Sets the enable_default_propagation of this EnterpriseRouter.

        是否开启默认路由表传播，默认false不开启

        :param enable_default_propagation: The enable_default_propagation of this EnterpriseRouter.
        :type enable_default_propagation: bool
        """
        self._enable_default_propagation = enable_default_propagation

    @property
    def enable_default_association(self):
        """Gets the enable_default_association of this EnterpriseRouter.

        是否开启默认路由表关联，默认false不开启

        :return: The enable_default_association of this EnterpriseRouter.
        :rtype: bool
        """
        return self._enable_default_association

    @enable_default_association.setter
    def enable_default_association(self, enable_default_association):
        """Sets the enable_default_association of this EnterpriseRouter.

        是否开启默认路由表关联，默认false不开启

        :param enable_default_association: The enable_default_association of this EnterpriseRouter.
        :type enable_default_association: bool
        """
        self._enable_default_association = enable_default_association

    @property
    def default_propagation_route_table_id(self):
        """Gets the default_propagation_route_table_id of this EnterpriseRouter.

        默认传播路由表id

        :return: The default_propagation_route_table_id of this EnterpriseRouter.
        :rtype: str
        """
        return self._default_propagation_route_table_id

    @default_propagation_route_table_id.setter
    def default_propagation_route_table_id(self, default_propagation_route_table_id):
        """Sets the default_propagation_route_table_id of this EnterpriseRouter.

        默认传播路由表id

        :param default_propagation_route_table_id: The default_propagation_route_table_id of this EnterpriseRouter.
        :type default_propagation_route_table_id: str
        """
        self._default_propagation_route_table_id = default_propagation_route_table_id

    @property
    def default_association_route_table_id(self):
        """Gets the default_association_route_table_id of this EnterpriseRouter.

        默认关联路由表id

        :return: The default_association_route_table_id of this EnterpriseRouter.
        :rtype: str
        """
        return self._default_association_route_table_id

    @default_association_route_table_id.setter
    def default_association_route_table_id(self, default_association_route_table_id):
        """Sets the default_association_route_table_id of this EnterpriseRouter.

        默认关联路由表id

        :param default_association_route_table_id: The default_association_route_table_id of this EnterpriseRouter.
        :type default_association_route_table_id: str
        """
        self._default_association_route_table_id = default_association_route_table_id

    @property
    def availability_zone_ids(self):
        """Gets the availability_zone_ids of this EnterpriseRouter.

        企业路由器所在可用区信息

        :return: The availability_zone_ids of this EnterpriseRouter.
        :rtype: list[str]
        """
        return self._availability_zone_ids

    @availability_zone_ids.setter
    def availability_zone_ids(self, availability_zone_ids):
        """Sets the availability_zone_ids of this EnterpriseRouter.

        企业路由器所在可用区信息

        :param availability_zone_ids: The availability_zone_ids of this EnterpriseRouter.
        :type availability_zone_ids: list[str]
        """
        self._availability_zone_ids = availability_zone_ids

    @property
    def auto_accept_shared_attachments(self):
        """Gets the auto_accept_shared_attachments of this EnterpriseRouter.

        是否自动接受共享连接创建，默认false不开启

        :return: The auto_accept_shared_attachments of this EnterpriseRouter.
        :rtype: bool
        """
        return self._auto_accept_shared_attachments

    @auto_accept_shared_attachments.setter
    def auto_accept_shared_attachments(self, auto_accept_shared_attachments):
        """Sets the auto_accept_shared_attachments of this EnterpriseRouter.

        是否自动接受共享连接创建，默认false不开启

        :param auto_accept_shared_attachments: The auto_accept_shared_attachments of this EnterpriseRouter.
        :type auto_accept_shared_attachments: bool
        """
        self._auto_accept_shared_attachments = auto_accept_shared_attachments

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
        if not isinstance(other, EnterpriseRouter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
