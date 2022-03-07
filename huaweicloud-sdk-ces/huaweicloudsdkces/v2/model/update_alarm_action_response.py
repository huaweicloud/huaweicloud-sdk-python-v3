# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlarmActionResponse(SdkResponse):


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
        'description': 'str',
        'action_enabled': 'str',
        'alarm_actions': 'list[SMNAction]',
        'ok_actions': 'list[SMNAction]',
        'action_begin_time': 'str',
        'action_end_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'action_enabled': 'action_enabled',
        'alarm_actions': 'alarm_actions',
        'ok_actions': 'ok_actions',
        'action_begin_time': 'action_begin_time',
        'action_end_time': 'action_end_time'
    }

    def __init__(self, name=None, description=None, action_enabled=None, alarm_actions=None, ok_actions=None, action_begin_time=None, action_end_time=None):
        """UpdateAlarmActionResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateAlarmActionResponse, self).__init__()

        self._name = None
        self._description = None
        self._action_enabled = None
        self._alarm_actions = None
        self._ok_actions = None
        self._action_begin_time = None
        self._action_end_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if action_enabled is not None:
            self.action_enabled = action_enabled
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if action_begin_time is not None:
            self.action_begin_time = action_begin_time
        if action_end_time is not None:
            self.action_end_time = action_end_time

    @property
    def name(self):
        """Gets the name of this UpdateAlarmActionResponse.

        告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128

        :return: The name of this UpdateAlarmActionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAlarmActionResponse.

        告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128

        :param name: The name of this UpdateAlarmActionResponse.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateAlarmActionResponse.

        告警描述，长度0-256

        :return: The description of this UpdateAlarmActionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAlarmActionResponse.

        告警描述，长度0-256

        :param description: The description of this UpdateAlarmActionResponse.
        :type: str
        """
        self._description = description

    @property
    def action_enabled(self):
        """Gets the action_enabled of this UpdateAlarmActionResponse.

        是否开启告警通知

        :return: The action_enabled of this UpdateAlarmActionResponse.
        :rtype: str
        """
        return self._action_enabled

    @action_enabled.setter
    def action_enabled(self, action_enabled):
        """Sets the action_enabled of this UpdateAlarmActionResponse.

        是否开启告警通知

        :param action_enabled: The action_enabled of this UpdateAlarmActionResponse.
        :type: str
        """
        self._action_enabled = action_enabled

    @property
    def alarm_actions(self):
        """Gets the alarm_actions of this UpdateAlarmActionResponse.

        告警触发的动作

        :return: The alarm_actions of this UpdateAlarmActionResponse.
        :rtype: list[SMNAction]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        """Sets the alarm_actions of this UpdateAlarmActionResponse.

        告警触发的动作

        :param alarm_actions: The alarm_actions of this UpdateAlarmActionResponse.
        :type: list[SMNAction]
        """
        self._alarm_actions = alarm_actions

    @property
    def ok_actions(self):
        """Gets the ok_actions of this UpdateAlarmActionResponse.

        告警恢复触发的动作

        :return: The ok_actions of this UpdateAlarmActionResponse.
        :rtype: list[SMNAction]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        """Sets the ok_actions of this UpdateAlarmActionResponse.

        告警恢复触发的动作

        :param ok_actions: The ok_actions of this UpdateAlarmActionResponse.
        :type: list[SMNAction]
        """
        self._ok_actions = ok_actions

    @property
    def action_begin_time(self):
        """Gets the action_begin_time of this UpdateAlarmActionResponse.

        告警通知开启时间

        :return: The action_begin_time of this UpdateAlarmActionResponse.
        :rtype: str
        """
        return self._action_begin_time

    @action_begin_time.setter
    def action_begin_time(self, action_begin_time):
        """Sets the action_begin_time of this UpdateAlarmActionResponse.

        告警通知开启时间

        :param action_begin_time: The action_begin_time of this UpdateAlarmActionResponse.
        :type: str
        """
        self._action_begin_time = action_begin_time

    @property
    def action_end_time(self):
        """Gets the action_end_time of this UpdateAlarmActionResponse.

        告警通知关闭时间

        :return: The action_end_time of this UpdateAlarmActionResponse.
        :rtype: str
        """
        return self._action_end_time

    @action_end_time.setter
    def action_end_time(self, action_end_time):
        """Sets the action_end_time of this UpdateAlarmActionResponse.

        告警通知关闭时间

        :param action_end_time: The action_end_time of this UpdateAlarmActionResponse.
        :type: str
        """
        self._action_end_time = action_end_time

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
        if not isinstance(other, UpdateAlarmActionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
