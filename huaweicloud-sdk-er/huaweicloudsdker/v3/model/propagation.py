# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Propagation:

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
        'project_id': 'str',
        'er_id': 'str',
        'route_table_id': 'str',
        'attachment_id': 'str',
        'resource_type': 'str',
        'resource_id': 'str',
        'route_policy': 'ImportRoutePolicy',
        'state': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'er_id': 'er_id',
        'route_table_id': 'route_table_id',
        'attachment_id': 'attachment_id',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'route_policy': 'route_policy',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, project_id=None, er_id=None, route_table_id=None, attachment_id=None, resource_type=None, resource_id=None, route_policy=None, state=None, created_at=None, updated_at=None):
        r"""Propagation

        The model defined in huaweicloud sdk

        :param id: 关联唯一标识
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param er_id: 企业路由器id
        :type er_id: str
        :param route_table_id: 路由表唯一标识
        :type route_table_id: str
        :param attachment_id: 连接唯一标识
        :type attachment_id: str
        :param resource_type: 连接的类型
        :type resource_type: str
        :param resource_id: 连接的资源唯一标识
        :type resource_id: str
        :param route_policy: 
        :type route_policy: :class:`huaweicloudsdker.v3.ImportRoutePolicy`
        :param state: 状态
        :type state: str
        :param created_at: 资源创建时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS
        :type created_at: datetime
        :param updated_at: 资源更新时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._project_id = None
        self._er_id = None
        self._route_table_id = None
        self._attachment_id = None
        self._resource_type = None
        self._resource_id = None
        self._route_policy = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if er_id is not None:
            self.er_id = er_id
        if route_table_id is not None:
            self.route_table_id = route_table_id
        if attachment_id is not None:
            self.attachment_id = attachment_id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id
        if route_policy is not None:
            self.route_policy = route_policy
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this Propagation.

        关联唯一标识

        :return: The id of this Propagation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Propagation.

        关联唯一标识

        :param id: The id of this Propagation.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this Propagation.

        项目ID

        :return: The project_id of this Propagation.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Propagation.

        项目ID

        :param project_id: The project_id of this Propagation.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def er_id(self):
        r"""Gets the er_id of this Propagation.

        企业路由器id

        :return: The er_id of this Propagation.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        r"""Sets the er_id of this Propagation.

        企业路由器id

        :param er_id: The er_id of this Propagation.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def route_table_id(self):
        r"""Gets the route_table_id of this Propagation.

        路由表唯一标识

        :return: The route_table_id of this Propagation.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        r"""Sets the route_table_id of this Propagation.

        路由表唯一标识

        :param route_table_id: The route_table_id of this Propagation.
        :type route_table_id: str
        """
        self._route_table_id = route_table_id

    @property
    def attachment_id(self):
        r"""Gets the attachment_id of this Propagation.

        连接唯一标识

        :return: The attachment_id of this Propagation.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        r"""Sets the attachment_id of this Propagation.

        连接唯一标识

        :param attachment_id: The attachment_id of this Propagation.
        :type attachment_id: str
        """
        self._attachment_id = attachment_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this Propagation.

        连接的类型

        :return: The resource_type of this Propagation.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this Propagation.

        连接的类型

        :param resource_type: The resource_type of this Propagation.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this Propagation.

        连接的资源唯一标识

        :return: The resource_id of this Propagation.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this Propagation.

        连接的资源唯一标识

        :param resource_id: The resource_id of this Propagation.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def route_policy(self):
        r"""Gets the route_policy of this Propagation.

        :return: The route_policy of this Propagation.
        :rtype: :class:`huaweicloudsdker.v3.ImportRoutePolicy`
        """
        return self._route_policy

    @route_policy.setter
    def route_policy(self, route_policy):
        r"""Sets the route_policy of this Propagation.

        :param route_policy: The route_policy of this Propagation.
        :type route_policy: :class:`huaweicloudsdker.v3.ImportRoutePolicy`
        """
        self._route_policy = route_policy

    @property
    def state(self):
        r"""Gets the state of this Propagation.

        状态

        :return: The state of this Propagation.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this Propagation.

        状态

        :param state: The state of this Propagation.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this Propagation.

        资源创建时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :return: The created_at of this Propagation.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Propagation.

        资源创建时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :param created_at: The created_at of this Propagation.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Propagation.

        资源更新时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :return: The updated_at of this Propagation.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Propagation.

        资源更新时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :param updated_at: The updated_at of this Propagation.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, Propagation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
