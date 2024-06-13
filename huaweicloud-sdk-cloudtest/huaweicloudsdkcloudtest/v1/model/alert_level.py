# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertLevel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_channel': 'list[str]',
        'alert_groups': 'list[AlertGroup]',
        'alert_template_id': 'str',
        'alert_times': 'int'
    }

    attribute_map = {
        'alert_channel': 'alert_channel',
        'alert_groups': 'alertGroups',
        'alert_template_id': 'alertTemplateId',
        'alert_times': 'alertTimes'
    }

    def __init__(self, alert_channel=None, alert_groups=None, alert_template_id=None, alert_times=None):
        """AlertLevel

        The model defined in huaweicloud sdk

        :param alert_channel: 告警渠道列表
        :type alert_channel: list[str]
        :param alert_groups: 告警组列表
        :type alert_groups: list[:class:`huaweicloudsdkcloudtest.v1.AlertGroup`]
        :param alert_template_id: 告警模板ID
        :type alert_template_id: str
        :param alert_times: 告警次数
        :type alert_times: int
        """
        
        

        self._alert_channel = None
        self._alert_groups = None
        self._alert_template_id = None
        self._alert_times = None
        self.discriminator = None

        if alert_channel is not None:
            self.alert_channel = alert_channel
        if alert_groups is not None:
            self.alert_groups = alert_groups
        if alert_template_id is not None:
            self.alert_template_id = alert_template_id
        if alert_times is not None:
            self.alert_times = alert_times

    @property
    def alert_channel(self):
        """Gets the alert_channel of this AlertLevel.

        告警渠道列表

        :return: The alert_channel of this AlertLevel.
        :rtype: list[str]
        """
        return self._alert_channel

    @alert_channel.setter
    def alert_channel(self, alert_channel):
        """Sets the alert_channel of this AlertLevel.

        告警渠道列表

        :param alert_channel: The alert_channel of this AlertLevel.
        :type alert_channel: list[str]
        """
        self._alert_channel = alert_channel

    @property
    def alert_groups(self):
        """Gets the alert_groups of this AlertLevel.

        告警组列表

        :return: The alert_groups of this AlertLevel.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AlertGroup`]
        """
        return self._alert_groups

    @alert_groups.setter
    def alert_groups(self, alert_groups):
        """Sets the alert_groups of this AlertLevel.

        告警组列表

        :param alert_groups: The alert_groups of this AlertLevel.
        :type alert_groups: list[:class:`huaweicloudsdkcloudtest.v1.AlertGroup`]
        """
        self._alert_groups = alert_groups

    @property
    def alert_template_id(self):
        """Gets the alert_template_id of this AlertLevel.

        告警模板ID

        :return: The alert_template_id of this AlertLevel.
        :rtype: str
        """
        return self._alert_template_id

    @alert_template_id.setter
    def alert_template_id(self, alert_template_id):
        """Sets the alert_template_id of this AlertLevel.

        告警模板ID

        :param alert_template_id: The alert_template_id of this AlertLevel.
        :type alert_template_id: str
        """
        self._alert_template_id = alert_template_id

    @property
    def alert_times(self):
        """Gets the alert_times of this AlertLevel.

        告警次数

        :return: The alert_times of this AlertLevel.
        :rtype: int
        """
        return self._alert_times

    @alert_times.setter
    def alert_times(self, alert_times):
        """Sets the alert_times of this AlertLevel.

        告警次数

        :param alert_times: The alert_times of this AlertLevel.
        :type alert_times: int
        """
        self._alert_times = alert_times

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
        if not isinstance(other, AlertLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
