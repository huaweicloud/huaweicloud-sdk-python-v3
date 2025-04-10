# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MessageNotification:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy': 'str',
        'notification_endpoint_type': 'str',
        'schedule_scene_id': 'str',
        'schedule_role_id': 'str',
        'recipients': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'policy': 'policy',
        'notification_endpoint_type': 'notification_endpoint_type',
        'schedule_scene_id': 'schedule_scene_id',
        'schedule_role_id': 'schedule_role_id',
        'recipients': 'recipients',
        'protocol': 'protocol'
    }

    def __init__(self, policy=None, notification_endpoint_type=None, schedule_scene_id=None, schedule_role_id=None, recipients=None, protocol=None):
        r"""MessageNotification

        The model defined in huaweicloud sdk

        :param policy: 通知策略
        :type policy: str
        :param notification_endpoint_type: 通知对象类型
        :type notification_endpoint_type: str
        :param schedule_scene_id: 排班场景ID
        :type schedule_scene_id: str
        :param schedule_role_id: 排班角色ID
        :type schedule_role_id: str
        :param recipients: 消息接收人
        :type recipients: str
        :param protocol: 通知渠道
        :type protocol: str
        """
        
        

        self._policy = None
        self._notification_endpoint_type = None
        self._schedule_scene_id = None
        self._schedule_role_id = None
        self._recipients = None
        self._protocol = None
        self.discriminator = None

        if policy is not None:
            self.policy = policy
        self.notification_endpoint_type = notification_endpoint_type
        if schedule_scene_id is not None:
            self.schedule_scene_id = schedule_scene_id
        if schedule_role_id is not None:
            self.schedule_role_id = schedule_role_id
        if recipients is not None:
            self.recipients = recipients
        if protocol is not None:
            self.protocol = protocol

    @property
    def policy(self):
        r"""Gets the policy of this MessageNotification.

        通知策略

        :return: The policy of this MessageNotification.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this MessageNotification.

        通知策略

        :param policy: The policy of this MessageNotification.
        :type policy: str
        """
        self._policy = policy

    @property
    def notification_endpoint_type(self):
        r"""Gets the notification_endpoint_type of this MessageNotification.

        通知对象类型

        :return: The notification_endpoint_type of this MessageNotification.
        :rtype: str
        """
        return self._notification_endpoint_type

    @notification_endpoint_type.setter
    def notification_endpoint_type(self, notification_endpoint_type):
        r"""Sets the notification_endpoint_type of this MessageNotification.

        通知对象类型

        :param notification_endpoint_type: The notification_endpoint_type of this MessageNotification.
        :type notification_endpoint_type: str
        """
        self._notification_endpoint_type = notification_endpoint_type

    @property
    def schedule_scene_id(self):
        r"""Gets the schedule_scene_id of this MessageNotification.

        排班场景ID

        :return: The schedule_scene_id of this MessageNotification.
        :rtype: str
        """
        return self._schedule_scene_id

    @schedule_scene_id.setter
    def schedule_scene_id(self, schedule_scene_id):
        r"""Sets the schedule_scene_id of this MessageNotification.

        排班场景ID

        :param schedule_scene_id: The schedule_scene_id of this MessageNotification.
        :type schedule_scene_id: str
        """
        self._schedule_scene_id = schedule_scene_id

    @property
    def schedule_role_id(self):
        r"""Gets the schedule_role_id of this MessageNotification.

        排班角色ID

        :return: The schedule_role_id of this MessageNotification.
        :rtype: str
        """
        return self._schedule_role_id

    @schedule_role_id.setter
    def schedule_role_id(self, schedule_role_id):
        r"""Sets the schedule_role_id of this MessageNotification.

        排班角色ID

        :param schedule_role_id: The schedule_role_id of this MessageNotification.
        :type schedule_role_id: str
        """
        self._schedule_role_id = schedule_role_id

    @property
    def recipients(self):
        r"""Gets the recipients of this MessageNotification.

        消息接收人

        :return: The recipients of this MessageNotification.
        :rtype: str
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        r"""Sets the recipients of this MessageNotification.

        消息接收人

        :param recipients: The recipients of this MessageNotification.
        :type recipients: str
        """
        self._recipients = recipients

    @property
    def protocol(self):
        r"""Gets the protocol of this MessageNotification.

        通知渠道

        :return: The protocol of this MessageNotification.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this MessageNotification.

        通知渠道

        :param protocol: The protocol of this MessageNotification.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, MessageNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
