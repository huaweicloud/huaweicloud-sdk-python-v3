# coding: utf-8

import pprint
import re

import six





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
        'event_user': 'str'
    }

    attribute_map = {
        'content': 'content',
        'group_id': 'group_id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'event_state': 'event_state',
        'event_level': 'event_level',
        'event_user': 'event_user'
    }

    def __init__(self, content=None, group_id=None, resource_id=None, resource_name=None, event_state=None, event_level=None, event_user=None):
        """EventItemDetail - a model defined in huaweicloud sdk"""
        
        

        self._content = None
        self._group_id = None
        self._resource_id = None
        self._resource_name = None
        self._event_state = None
        self._event_level = None
        self._event_user = None
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

    @property
    def content(self):
        """Gets the content of this EventItemDetail.

        事件内容，最大长度4096。

        :return: The content of this EventItemDetail.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this EventItemDetail.

        事件内容，最大长度4096。

        :param content: The content of this EventItemDetail.
        :type: str
        """
        self._content = content

    @property
    def group_id(self):
        """Gets the group_id of this EventItemDetail.

        所属分组。  资源分组对应的ID，必须传存在的分组ID。

        :return: The group_id of this EventItemDetail.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this EventItemDetail.

        所属分组。  资源分组对应的ID，必须传存在的分组ID。

        :param group_id: The group_id of this EventItemDetail.
        :type: str
        """
        self._group_id = group_id

    @property
    def resource_id(self):
        """Gets the resource_id of this EventItemDetail.

        资源ID，支持字母、数字_ -：，最大长度128。

        :return: The resource_id of this EventItemDetail.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this EventItemDetail.

        资源ID，支持字母、数字_ -：，最大长度128。

        :param resource_id: The resource_id of this EventItemDetail.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this EventItemDetail.

        资源名称，支持字母 中文 数字_ -. ，最大长度128。

        :return: The resource_name of this EventItemDetail.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this EventItemDetail.

        资源名称，支持字母 中文 数字_ -. ，最大长度128。

        :param resource_name: The resource_name of this EventItemDetail.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def event_state(self):
        """Gets the event_state of this EventItemDetail.

        事件状态。  枚举类型：normal\\warning\\incident

        :return: The event_state of this EventItemDetail.
        :rtype: str
        """
        return self._event_state

    @event_state.setter
    def event_state(self, event_state):
        """Sets the event_state of this EventItemDetail.

        事件状态。  枚举类型：normal\\warning\\incident

        :param event_state: The event_state of this EventItemDetail.
        :type: str
        """
        self._event_state = event_state

    @property
    def event_level(self):
        """Gets the event_level of this EventItemDetail.

        事件级别。  枚举类型：Critical, Major, Minor, Info

        :return: The event_level of this EventItemDetail.
        :rtype: str
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        """Sets the event_level of this EventItemDetail.

        事件级别。  枚举类型：Critical, Major, Minor, Info

        :param event_level: The event_level of this EventItemDetail.
        :type: str
        """
        self._event_level = event_level

    @property
    def event_user(self):
        """Gets the event_user of this EventItemDetail.

        事件用户。  支持字母 数字_ -/空格 ，最大长度64。

        :return: The event_user of this EventItemDetail.
        :rtype: str
        """
        return self._event_user

    @event_user.setter
    def event_user(self, event_user):
        """Sets the event_user of this EventItemDetail.

        事件用户。  支持字母 数字_ -/空格 ，最大长度64。

        :param event_user: The event_user of this EventItemDetail.
        :type: str
        """
        self._event_user = event_user

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventItemDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
