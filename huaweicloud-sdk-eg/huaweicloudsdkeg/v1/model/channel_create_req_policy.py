# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChannelCreateReqPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sid': 'str',
        'effect': 'str',
        'principal': 'dict(str, ChannelCreateReqPrincipal)',
        'action': 'str',
        'resource': 'str'
    }

    attribute_map = {
        'sid': 'Sid',
        'effect': 'Effect',
        'principal': 'Principal',
        'action': 'Action',
        'resource': 'Resource'
    }

    def __init__(self, sid=None, effect=None, principal=None, action=None, resource=None):
        r"""ChannelCreateReqPolicy

        The model defined in huaweicloud sdk

        :param sid: 固定值：allow_account_to_put_events
        :type sid: str
        :param effect: 固定值：Allow
        :type effect: str
        :param principal: domain白名单
        :type principal: dict(str, ChannelCreateReqPrincipal)
        :param action: 固定值：eg:channels:putEvents
        :type action: str
        :param resource: 固定格式：urn:eg:cn-east-2:{project_id}:channel:{channel_name}
        :type resource: str
        """
        
        

        self._sid = None
        self._effect = None
        self._principal = None
        self._action = None
        self._resource = None
        self.discriminator = None

        if sid is not None:
            self.sid = sid
        if effect is not None:
            self.effect = effect
        if principal is not None:
            self.principal = principal
        if action is not None:
            self.action = action
        if resource is not None:
            self.resource = resource

    @property
    def sid(self):
        r"""Gets the sid of this ChannelCreateReqPolicy.

        固定值：allow_account_to_put_events

        :return: The sid of this ChannelCreateReqPolicy.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        r"""Sets the sid of this ChannelCreateReqPolicy.

        固定值：allow_account_to_put_events

        :param sid: The sid of this ChannelCreateReqPolicy.
        :type sid: str
        """
        self._sid = sid

    @property
    def effect(self):
        r"""Gets the effect of this ChannelCreateReqPolicy.

        固定值：Allow

        :return: The effect of this ChannelCreateReqPolicy.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        r"""Sets the effect of this ChannelCreateReqPolicy.

        固定值：Allow

        :param effect: The effect of this ChannelCreateReqPolicy.
        :type effect: str
        """
        self._effect = effect

    @property
    def principal(self):
        r"""Gets the principal of this ChannelCreateReqPolicy.

        domain白名单

        :return: The principal of this ChannelCreateReqPolicy.
        :rtype: dict(str, ChannelCreateReqPrincipal)
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        r"""Sets the principal of this ChannelCreateReqPolicy.

        domain白名单

        :param principal: The principal of this ChannelCreateReqPolicy.
        :type principal: dict(str, ChannelCreateReqPrincipal)
        """
        self._principal = principal

    @property
    def action(self):
        r"""Gets the action of this ChannelCreateReqPolicy.

        固定值：eg:channels:putEvents

        :return: The action of this ChannelCreateReqPolicy.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ChannelCreateReqPolicy.

        固定值：eg:channels:putEvents

        :param action: The action of this ChannelCreateReqPolicy.
        :type action: str
        """
        self._action = action

    @property
    def resource(self):
        r"""Gets the resource of this ChannelCreateReqPolicy.

        固定格式：urn:eg:cn-east-2:{project_id}:channel:{channel_name}

        :return: The resource of this ChannelCreateReqPolicy.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this ChannelCreateReqPolicy.

        固定格式：urn:eg:cn-east-2:{project_id}:channel:{channel_name}

        :param resource: The resource of this ChannelCreateReqPolicy.
        :type resource: str
        """
        self._resource = resource

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
        if not isinstance(other, ChannelCreateReqPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
