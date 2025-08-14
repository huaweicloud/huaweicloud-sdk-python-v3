# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventItemDetail:

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
        'event_state': 'str',
        'event_level': 'str',
        'event_user': 'str',
        'event_type': 'str',
        'sub_event_type': 'str',
        'dimensions': 'list[MetricsDimension]'
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
        'sub_event_type': 'sub_event_type',
        'dimensions': 'dimensions'
    }

    def __init__(self, content=None, group_id=None, resource_id=None, resource_name=None, event_state=None, event_level=None, event_user=None, event_type=None, sub_event_type=None, dimensions=None):
        r"""EventItemDetail

        The model defined in huaweicloud sdk

        :param content: 事件内容，最大长度4096。
        :type content: str
        :param group_id: 所属分组。  资源分组对应的ID，必须传存在的分组ID。
        :type group_id: str
        :param resource_id: 资源ID，支持字母、数字_ -：，最大长度128。
        :type resource_id: str
        :param resource_name: 资源名称，支持字母 中文 数字_ -. ，最大长度128。
        :type resource_name: str
        :param event_state: 事件状态。  枚举类型：normal\\warning\\incident
        :type event_state: str
        :param event_level: 事件级别。  枚举类型：Critical, Major, Minor, Info
        :type event_level: str
        :param event_user: 事件用户。  支持字母 数字_ -/空格 ，最大长度64。
        :type event_user: str
        :param event_type: 事件类型。 枚举类型，EVENT.SYS或EVENT.CUSTOM，EVENT.SYS为系统事件，用户自已不能上报，只能传EVENT.CUSTOM。
        :type event_type: str
        :param sub_event_type: 事件子类。 枚举类型：SUB_EVENT.OPS为运维事件，SUB_EVENT.PLAN为计划事件，SUB_EVENT.CUSTOM为自定义事件。
        :type sub_event_type: str
        :param dimensions: 一个或者多个资源维度。
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        
        

        self._content = None
        self._group_id = None
        self._resource_id = None
        self._resource_name = None
        self._event_state = None
        self._event_level = None
        self._event_user = None
        self._event_type = None
        self._sub_event_type = None
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
        if sub_event_type is not None:
            self.sub_event_type = sub_event_type
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def content(self):
        r"""Gets the content of this EventItemDetail.

        事件内容，最大长度4096。

        :return: The content of this EventItemDetail.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this EventItemDetail.

        事件内容，最大长度4096。

        :param content: The content of this EventItemDetail.
        :type content: str
        """
        self._content = content

    @property
    def group_id(self):
        r"""Gets the group_id of this EventItemDetail.

        所属分组。  资源分组对应的ID，必须传存在的分组ID。

        :return: The group_id of this EventItemDetail.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this EventItemDetail.

        所属分组。  资源分组对应的ID，必须传存在的分组ID。

        :param group_id: The group_id of this EventItemDetail.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this EventItemDetail.

        资源ID，支持字母、数字_ -：，最大长度128。

        :return: The resource_id of this EventItemDetail.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this EventItemDetail.

        资源ID，支持字母、数字_ -：，最大长度128。

        :param resource_id: The resource_id of this EventItemDetail.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this EventItemDetail.

        资源名称，支持字母 中文 数字_ -. ，最大长度128。

        :return: The resource_name of this EventItemDetail.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this EventItemDetail.

        资源名称，支持字母 中文 数字_ -. ，最大长度128。

        :param resource_name: The resource_name of this EventItemDetail.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def event_state(self):
        r"""Gets the event_state of this EventItemDetail.

        事件状态。  枚举类型：normal\\warning\\incident

        :return: The event_state of this EventItemDetail.
        :rtype: str
        """
        return self._event_state

    @event_state.setter
    def event_state(self, event_state):
        r"""Sets the event_state of this EventItemDetail.

        事件状态。  枚举类型：normal\\warning\\incident

        :param event_state: The event_state of this EventItemDetail.
        :type event_state: str
        """
        self._event_state = event_state

    @property
    def event_level(self):
        r"""Gets the event_level of this EventItemDetail.

        事件级别。  枚举类型：Critical, Major, Minor, Info

        :return: The event_level of this EventItemDetail.
        :rtype: str
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        r"""Sets the event_level of this EventItemDetail.

        事件级别。  枚举类型：Critical, Major, Minor, Info

        :param event_level: The event_level of this EventItemDetail.
        :type event_level: str
        """
        self._event_level = event_level

    @property
    def event_user(self):
        r"""Gets the event_user of this EventItemDetail.

        事件用户。  支持字母 数字_ -/空格 ，最大长度64。

        :return: The event_user of this EventItemDetail.
        :rtype: str
        """
        return self._event_user

    @event_user.setter
    def event_user(self, event_user):
        r"""Sets the event_user of this EventItemDetail.

        事件用户。  支持字母 数字_ -/空格 ，最大长度64。

        :param event_user: The event_user of this EventItemDetail.
        :type event_user: str
        """
        self._event_user = event_user

    @property
    def event_type(self):
        r"""Gets the event_type of this EventItemDetail.

        事件类型。 枚举类型，EVENT.SYS或EVENT.CUSTOM，EVENT.SYS为系统事件，用户自已不能上报，只能传EVENT.CUSTOM。

        :return: The event_type of this EventItemDetail.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this EventItemDetail.

        事件类型。 枚举类型，EVENT.SYS或EVENT.CUSTOM，EVENT.SYS为系统事件，用户自已不能上报，只能传EVENT.CUSTOM。

        :param event_type: The event_type of this EventItemDetail.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def sub_event_type(self):
        r"""Gets the sub_event_type of this EventItemDetail.

        事件子类。 枚举类型：SUB_EVENT.OPS为运维事件，SUB_EVENT.PLAN为计划事件，SUB_EVENT.CUSTOM为自定义事件。

        :return: The sub_event_type of this EventItemDetail.
        :rtype: str
        """
        return self._sub_event_type

    @sub_event_type.setter
    def sub_event_type(self, sub_event_type):
        r"""Sets the sub_event_type of this EventItemDetail.

        事件子类。 枚举类型：SUB_EVENT.OPS为运维事件，SUB_EVENT.PLAN为计划事件，SUB_EVENT.CUSTOM为自定义事件。

        :param sub_event_type: The sub_event_type of this EventItemDetail.
        :type sub_event_type: str
        """
        self._sub_event_type = sub_event_type

    @property
    def dimensions(self):
        r"""Gets the dimensions of this EventItemDetail.

        一个或者多个资源维度。

        :return: The dimensions of this EventItemDetail.
        :rtype: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this EventItemDetail.

        一个或者多个资源维度。

        :param dimensions: The dimensions of this EventItemDetail.
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimension`]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, EventItemDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
