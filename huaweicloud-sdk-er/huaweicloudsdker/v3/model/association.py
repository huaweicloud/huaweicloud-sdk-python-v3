# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Association:

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
        'route_table_id': 'str',
        'attachment_id': 'str',
        'resource_type': 'str',
        'resource_id': 'str',
        'state': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'route_policy': 'ExportRoutePolicy'
    }

    attribute_map = {
        'id': 'id',
        'route_table_id': 'route_table_id',
        'attachment_id': 'attachment_id',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'route_policy': 'route_policy'
    }

    def __init__(self, id=None, route_table_id=None, attachment_id=None, resource_type=None, resource_id=None, state=None, created_at=None, updated_at=None, route_policy=None):
        """Association

        The model defined in huaweicloud sdk

        :param id: 关联唯一标识
        :type id: str
        :param route_table_id: 路由表唯一标识
        :type route_table_id: str
        :param attachment_id: 连接唯一标识
        :type attachment_id: str
        :param resource_type: 连接的类型
        :type resource_type: str
        :param resource_id: 连接的资源唯一标识
        :type resource_id: str
        :param state: 状态
        :type state: str
        :param created_at: 资源创建时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS
        :type created_at: datetime
        :param updated_at: 资源更新时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS
        :type updated_at: datetime
        :param route_policy: 
        :type route_policy: :class:`huaweicloudsdker.v3.ExportRoutePolicy`
        """
        
        

        self._id = None
        self._route_table_id = None
        self._attachment_id = None
        self._resource_type = None
        self._resource_id = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._route_policy = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if route_table_id is not None:
            self.route_table_id = route_table_id
        if attachment_id is not None:
            self.attachment_id = attachment_id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if route_policy is not None:
            self.route_policy = route_policy

    @property
    def id(self):
        """Gets the id of this Association.

        关联唯一标识

        :return: The id of this Association.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Association.

        关联唯一标识

        :param id: The id of this Association.
        :type id: str
        """
        self._id = id

    @property
    def route_table_id(self):
        """Gets the route_table_id of this Association.

        路由表唯一标识

        :return: The route_table_id of this Association.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this Association.

        路由表唯一标识

        :param route_table_id: The route_table_id of this Association.
        :type route_table_id: str
        """
        self._route_table_id = route_table_id

    @property
    def attachment_id(self):
        """Gets the attachment_id of this Association.

        连接唯一标识

        :return: The attachment_id of this Association.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this Association.

        连接唯一标识

        :param attachment_id: The attachment_id of this Association.
        :type attachment_id: str
        """
        self._attachment_id = attachment_id

    @property
    def resource_type(self):
        """Gets the resource_type of this Association.

        连接的类型

        :return: The resource_type of this Association.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Association.

        连接的类型

        :param resource_type: The resource_type of this Association.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this Association.

        连接的资源唯一标识

        :return: The resource_id of this Association.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Association.

        连接的资源唯一标识

        :param resource_id: The resource_id of this Association.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def state(self):
        """Gets the state of this Association.

        状态

        :return: The state of this Association.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Association.

        状态

        :param state: The state of this Association.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        """Gets the created_at of this Association.

        资源创建时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :return: The created_at of this Association.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Association.

        资源创建时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :param created_at: The created_at of this Association.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Association.

        资源更新时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :return: The updated_at of this Association.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Association.

        资源更新时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :param updated_at: The updated_at of this Association.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def route_policy(self):
        """Gets the route_policy of this Association.


        :return: The route_policy of this Association.
        :rtype: :class:`huaweicloudsdker.v3.ExportRoutePolicy`
        """
        return self._route_policy

    @route_policy.setter
    def route_policy(self, route_policy):
        """Sets the route_policy of this Association.


        :param route_policy: The route_policy of this Association.
        :type route_policy: :class:`huaweicloudsdker.v3.ExportRoutePolicy`
        """
        self._route_policy = route_policy

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
        if not isinstance(other, Association):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
