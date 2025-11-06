# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventDetailEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'group_id': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'event_state': 'EventStateEnum',
        'event_level': 'EventLevelEnum',
        'event_user': 'str',
        'event_type': 'str',
        'dimensions': 'str'
    }

    attribute_map = {
        'content': 'content',
        'group_id': 'group_id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'event_state': 'event_state',
        'event_level': 'event_level',
        'event_user': 'event_user',
        'event_type': 'event_type',
        'dimensions': 'dimensions'
    }

    def __init__(self, content=None, group_id=None, resource_id=None, resource_name=None, event_state=None, event_level=None, event_user=None, event_type=None, dimensions=None):
        r"""EventDetailEntity

        The model defined in huaweicloud sdk

        :param content: 事件内容
        :type content: str
        :param group_id: 组ID
        :type group_id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_name: 资源名
        :type resource_name: str
        :param event_state: 
        :type event_state: :class:`huaweicloudsdkbcc.v1.EventStateEnum`
        :param event_level: 
        :type event_level: :class:`huaweicloudsdkbcc.v1.EventLevelEnum`
        :param event_user: 事件用户
        :type event_user: str
        :param event_type: 事件类型
        :type event_type: str
        :param dimensions: 事件维度
        :type dimensions: str
        """
        
        

        self._content = None
        self._group_id = None
        self._resource_id = None
        self._resource_name = None
        self._event_state = None
        self._event_level = None
        self._event_user = None
        self._event_type = None
        self._dimensions = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if group_id is not None:
            self.group_id = group_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if event_state is not None:
            self.event_state = event_state
        if event_level is not None:
            self.event_level = event_level
        if event_user is not None:
            self.event_user = event_user
        if event_type is not None:
            self.event_type = event_type
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def content(self):
        r"""Gets the content of this EventDetailEntity.

        事件内容

        :return: The content of this EventDetailEntity.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this EventDetailEntity.

        事件内容

        :param content: The content of this EventDetailEntity.
        :type content: str
        """
        self._content = content

    @property
    def group_id(self):
        r"""Gets the group_id of this EventDetailEntity.

        组ID

        :return: The group_id of this EventDetailEntity.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this EventDetailEntity.

        组ID

        :param group_id: The group_id of this EventDetailEntity.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this EventDetailEntity.

        资源ID

        :return: The resource_id of this EventDetailEntity.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this EventDetailEntity.

        资源ID

        :param resource_id: The resource_id of this EventDetailEntity.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this EventDetailEntity.

        资源名

        :return: The resource_name of this EventDetailEntity.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this EventDetailEntity.

        资源名

        :param resource_name: The resource_name of this EventDetailEntity.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def event_state(self):
        r"""Gets the event_state of this EventDetailEntity.

        :return: The event_state of this EventDetailEntity.
        :rtype: :class:`huaweicloudsdkbcc.v1.EventStateEnum`
        """
        return self._event_state

    @event_state.setter
    def event_state(self, event_state):
        r"""Sets the event_state of this EventDetailEntity.

        :param event_state: The event_state of this EventDetailEntity.
        :type event_state: :class:`huaweicloudsdkbcc.v1.EventStateEnum`
        """
        self._event_state = event_state

    @property
    def event_level(self):
        r"""Gets the event_level of this EventDetailEntity.

        :return: The event_level of this EventDetailEntity.
        :rtype: :class:`huaweicloudsdkbcc.v1.EventLevelEnum`
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        r"""Sets the event_level of this EventDetailEntity.

        :param event_level: The event_level of this EventDetailEntity.
        :type event_level: :class:`huaweicloudsdkbcc.v1.EventLevelEnum`
        """
        self._event_level = event_level

    @property
    def event_user(self):
        r"""Gets the event_user of this EventDetailEntity.

        事件用户

        :return: The event_user of this EventDetailEntity.
        :rtype: str
        """
        return self._event_user

    @event_user.setter
    def event_user(self, event_user):
        r"""Sets the event_user of this EventDetailEntity.

        事件用户

        :param event_user: The event_user of this EventDetailEntity.
        :type event_user: str
        """
        self._event_user = event_user

    @property
    def event_type(self):
        r"""Gets the event_type of this EventDetailEntity.

        事件类型

        :return: The event_type of this EventDetailEntity.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this EventDetailEntity.

        事件类型

        :param event_type: The event_type of this EventDetailEntity.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def dimensions(self):
        r"""Gets the dimensions of this EventDetailEntity.

        事件维度

        :return: The dimensions of this EventDetailEntity.
        :rtype: str
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this EventDetailEntity.

        事件维度

        :param dimensions: The dimensions of this EventDetailEntity.
        :type dimensions: str
        """
        self._dimensions = dimensions

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventDetailEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
