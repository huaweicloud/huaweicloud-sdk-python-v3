# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Route:

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
        'type': 'str',
        'state': 'str',
        'is_blackhole': 'bool',
        'destination': 'str',
        'attachments': 'list[RouteAttachment]',
        'route_table_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'state': 'state',
        'is_blackhole': 'is_blackhole',
        'destination': 'destination',
        'attachments': 'attachments',
        'route_table_id': 'route_table_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, type=None, state=None, is_blackhole=None, destination=None, attachments=None, route_table_id=None, created_at=None, updated_at=None):
        """Route

        The model defined in huaweicloud sdk

        :param id: 路由id
        :type id: str
        :param type: 路由类型
        :type type: str
        :param state: 路由状态
        :type state: str
        :param is_blackhole: 是否为黑洞路由
        :type is_blackhole: bool
        :param destination: 路由目的地址
        :type destination: str
        :param attachments: 下一跳列表
        :type attachments: list[:class:`huaweicloudsdker.v3.RouteAttachment`]
        :param route_table_id: 路由表id
        :type route_table_id: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._type = None
        self._state = None
        self._is_blackhole = None
        self._destination = None
        self._attachments = None
        self._route_table_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.type = type
        if state is not None:
            self.state = state
        if is_blackhole is not None:
            self.is_blackhole = is_blackhole
        self.destination = destination
        self.attachments = attachments
        self.route_table_id = route_table_id
        self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Route.

        路由id

        :return: The id of this Route.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Route.

        路由id

        :param id: The id of this Route.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this Route.

        路由类型

        :return: The type of this Route.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Route.

        路由类型

        :param type: The type of this Route.
        :type type: str
        """
        self._type = type

    @property
    def state(self):
        """Gets the state of this Route.

        路由状态

        :return: The state of this Route.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Route.

        路由状态

        :param state: The state of this Route.
        :type state: str
        """
        self._state = state

    @property
    def is_blackhole(self):
        """Gets the is_blackhole of this Route.

        是否为黑洞路由

        :return: The is_blackhole of this Route.
        :rtype: bool
        """
        return self._is_blackhole

    @is_blackhole.setter
    def is_blackhole(self, is_blackhole):
        """Sets the is_blackhole of this Route.

        是否为黑洞路由

        :param is_blackhole: The is_blackhole of this Route.
        :type is_blackhole: bool
        """
        self._is_blackhole = is_blackhole

    @property
    def destination(self):
        """Gets the destination of this Route.

        路由目的地址

        :return: The destination of this Route.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this Route.

        路由目的地址

        :param destination: The destination of this Route.
        :type destination: str
        """
        self._destination = destination

    @property
    def attachments(self):
        """Gets the attachments of this Route.

        下一跳列表

        :return: The attachments of this Route.
        :rtype: list[:class:`huaweicloudsdker.v3.RouteAttachment`]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Route.

        下一跳列表

        :param attachments: The attachments of this Route.
        :type attachments: list[:class:`huaweicloudsdker.v3.RouteAttachment`]
        """
        self._attachments = attachments

    @property
    def route_table_id(self):
        """Gets the route_table_id of this Route.

        路由表id

        :return: The route_table_id of this Route.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this Route.

        路由表id

        :param route_table_id: The route_table_id of this Route.
        :type route_table_id: str
        """
        self._route_table_id = route_table_id

    @property
    def created_at(self):
        """Gets the created_at of this Route.

        创建时间

        :return: The created_at of this Route.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Route.

        创建时间

        :param created_at: The created_at of this Route.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Route.

        更新时间

        :return: The updated_at of this Route.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Route.

        更新时间

        :param updated_at: The updated_at of this Route.
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
        if not isinstance(other, Route):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
