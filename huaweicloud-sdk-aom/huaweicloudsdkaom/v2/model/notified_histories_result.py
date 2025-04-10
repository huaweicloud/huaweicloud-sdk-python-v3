# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotifiedHistoriesResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_sn': 'str',
        'notifications': 'list[Notifications]'
    }

    attribute_map = {
        'event_sn': 'event_sn',
        'notifications': 'notifications'
    }

    def __init__(self, event_sn=None, notifications=None):
        r"""NotifiedHistoriesResult

        The model defined in huaweicloud sdk

        :param event_sn: 告警流水号
        :type event_sn: str
        :param notifications: 通知结果
        :type notifications: list[:class:`huaweicloudsdkaom.v2.Notifications`]
        """
        
        

        self._event_sn = None
        self._notifications = None
        self.discriminator = None

        if event_sn is not None:
            self.event_sn = event_sn
        if notifications is not None:
            self.notifications = notifications

    @property
    def event_sn(self):
        r"""Gets the event_sn of this NotifiedHistoriesResult.

        告警流水号

        :return: The event_sn of this NotifiedHistoriesResult.
        :rtype: str
        """
        return self._event_sn

    @event_sn.setter
    def event_sn(self, event_sn):
        r"""Sets the event_sn of this NotifiedHistoriesResult.

        告警流水号

        :param event_sn: The event_sn of this NotifiedHistoriesResult.
        :type event_sn: str
        """
        self._event_sn = event_sn

    @property
    def notifications(self):
        r"""Gets the notifications of this NotifiedHistoriesResult.

        通知结果

        :return: The notifications of this NotifiedHistoriesResult.
        :rtype: list[:class:`huaweicloudsdkaom.v2.Notifications`]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        r"""Sets the notifications of this NotifiedHistoriesResult.

        通知结果

        :param notifications: The notifications of this NotifiedHistoriesResult.
        :type notifications: list[:class:`huaweicloudsdkaom.v2.Notifications`]
        """
        self._notifications = notifications

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
        if not isinstance(other, NotifiedHistoriesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
