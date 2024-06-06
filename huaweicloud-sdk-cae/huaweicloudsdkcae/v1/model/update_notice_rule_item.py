# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNoticeRuleItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'scope': 'NoticeRuleScope',
        'trigger_policy': 'TriggerPolicy',
        'enable': 'bool'
    }

    attribute_map = {
        'event_name': 'event_name',
        'scope': 'scope',
        'trigger_policy': 'trigger_policy',
        'enable': 'enable'
    }

    def __init__(self, event_name=None, scope=None, trigger_policy=None, enable=None):
        """UpdateNoticeRuleItem

        The model defined in huaweicloud sdk

        :param event_name: 触发事件名称，支持实例调度成功、实例调度失败、健康检查成功、健康检查失败、镜像拉取成功、镜像拉取失败、容器启动成功、容器启动失败、卷挂载成功、卷挂载失败。
        :type event_name: str
        :param scope: 
        :type scope: :class:`huaweicloudsdkcae.v1.NoticeRuleScope`
        :param trigger_policy: 
        :type trigger_policy: :class:`huaweicloudsdkcae.v1.TriggerPolicy`
        :param enable: 是否启用。
        :type enable: bool
        """
        
        

        self._event_name = None
        self._scope = None
        self._trigger_policy = None
        self._enable = None
        self.discriminator = None

        if event_name is not None:
            self.event_name = event_name
        self.scope = scope
        self.trigger_policy = trigger_policy
        if enable is not None:
            self.enable = enable

    @property
    def event_name(self):
        """Gets the event_name of this UpdateNoticeRuleItem.

        触发事件名称，支持实例调度成功、实例调度失败、健康检查成功、健康检查失败、镜像拉取成功、镜像拉取失败、容器启动成功、容器启动失败、卷挂载成功、卷挂载失败。

        :return: The event_name of this UpdateNoticeRuleItem.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this UpdateNoticeRuleItem.

        触发事件名称，支持实例调度成功、实例调度失败、健康检查成功、健康检查失败、镜像拉取成功、镜像拉取失败、容器启动成功、容器启动失败、卷挂载成功、卷挂载失败。

        :param event_name: The event_name of this UpdateNoticeRuleItem.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def scope(self):
        """Gets the scope of this UpdateNoticeRuleItem.

        :return: The scope of this UpdateNoticeRuleItem.
        :rtype: :class:`huaweicloudsdkcae.v1.NoticeRuleScope`
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this UpdateNoticeRuleItem.

        :param scope: The scope of this UpdateNoticeRuleItem.
        :type scope: :class:`huaweicloudsdkcae.v1.NoticeRuleScope`
        """
        self._scope = scope

    @property
    def trigger_policy(self):
        """Gets the trigger_policy of this UpdateNoticeRuleItem.

        :return: The trigger_policy of this UpdateNoticeRuleItem.
        :rtype: :class:`huaweicloudsdkcae.v1.TriggerPolicy`
        """
        return self._trigger_policy

    @trigger_policy.setter
    def trigger_policy(self, trigger_policy):
        """Sets the trigger_policy of this UpdateNoticeRuleItem.

        :param trigger_policy: The trigger_policy of this UpdateNoticeRuleItem.
        :type trigger_policy: :class:`huaweicloudsdkcae.v1.TriggerPolicy`
        """
        self._trigger_policy = trigger_policy

    @property
    def enable(self):
        """Gets the enable of this UpdateNoticeRuleItem.

        是否启用。

        :return: The enable of this UpdateNoticeRuleItem.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this UpdateNoticeRuleItem.

        是否启用。

        :param enable: The enable of this UpdateNoticeRuleItem.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, UpdateNoticeRuleItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
