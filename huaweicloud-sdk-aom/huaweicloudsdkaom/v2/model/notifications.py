# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Notifications:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_rule': 'str',
        'notifier_channel': 'str',
        'smn_channel': 'SmnResponse'
    }

    attribute_map = {
        'action_rule': 'action_rule',
        'notifier_channel': 'notifier_channel',
        'smn_channel': 'smn_channel'
    }

    def __init__(self, action_rule=None, notifier_channel=None, smn_channel=None):
        """Notifications

        The model defined in huaweicloud sdk

        :param action_rule: 告警行动规则名称
        :type action_rule: str
        :param notifier_channel: 通知类型。SMN：消息通知服务
        :type notifier_channel: str
        :param smn_channel: 
        :type smn_channel: :class:`huaweicloudsdkaom.v2.SmnResponse`
        """
        
        

        self._action_rule = None
        self._notifier_channel = None
        self._smn_channel = None
        self.discriminator = None

        if action_rule is not None:
            self.action_rule = action_rule
        if notifier_channel is not None:
            self.notifier_channel = notifier_channel
        if smn_channel is not None:
            self.smn_channel = smn_channel

    @property
    def action_rule(self):
        """Gets the action_rule of this Notifications.

        告警行动规则名称

        :return: The action_rule of this Notifications.
        :rtype: str
        """
        return self._action_rule

    @action_rule.setter
    def action_rule(self, action_rule):
        """Sets the action_rule of this Notifications.

        告警行动规则名称

        :param action_rule: The action_rule of this Notifications.
        :type action_rule: str
        """
        self._action_rule = action_rule

    @property
    def notifier_channel(self):
        """Gets the notifier_channel of this Notifications.

        通知类型。SMN：消息通知服务

        :return: The notifier_channel of this Notifications.
        :rtype: str
        """
        return self._notifier_channel

    @notifier_channel.setter
    def notifier_channel(self, notifier_channel):
        """Sets the notifier_channel of this Notifications.

        通知类型。SMN：消息通知服务

        :param notifier_channel: The notifier_channel of this Notifications.
        :type notifier_channel: str
        """
        self._notifier_channel = notifier_channel

    @property
    def smn_channel(self):
        """Gets the smn_channel of this Notifications.

        :return: The smn_channel of this Notifications.
        :rtype: :class:`huaweicloudsdkaom.v2.SmnResponse`
        """
        return self._smn_channel

    @smn_channel.setter
    def smn_channel(self, smn_channel):
        """Sets the smn_channel of this Notifications.

        :param smn_channel: The smn_channel of this Notifications.
        :type smn_channel: :class:`huaweicloudsdkaom.v2.SmnResponse`
        """
        self._smn_channel = smn_channel

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
        if not isinstance(other, Notifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
