# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Schedule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'cron': 'Cron',
        'event': 'Event'
    }

    attribute_map = {
        'type': 'type',
        'cron': 'cron',
        'event': 'event'
    }

    def __init__(self, type=None, cron=None, event=None):
        r"""Schedule

        The model defined in huaweicloud sdk

        :param type: 调度类型 - EXECUTE_ONCE: 作业立即运行，只运行一次。 - CRON: 作业按指定频率周期执行。 - EVENT:  根据事件触发执行。
        :type type: str
        :param cron: 
        :type cron: :class:`huaweicloudsdkdgc.v1.Cron`
        :param event: 
        :type event: :class:`huaweicloudsdkdgc.v1.Event`
        """
        
        

        self._type = None
        self._cron = None
        self._event = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if cron is not None:
            self.cron = cron
        if event is not None:
            self.event = event

    @property
    def type(self):
        r"""Gets the type of this Schedule.

        调度类型 - EXECUTE_ONCE: 作业立即运行，只运行一次。 - CRON: 作业按指定频率周期执行。 - EVENT:  根据事件触发执行。

        :return: The type of this Schedule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Schedule.

        调度类型 - EXECUTE_ONCE: 作业立即运行，只运行一次。 - CRON: 作业按指定频率周期执行。 - EVENT:  根据事件触发执行。

        :param type: The type of this Schedule.
        :type type: str
        """
        self._type = type

    @property
    def cron(self):
        r"""Gets the cron of this Schedule.

        :return: The cron of this Schedule.
        :rtype: :class:`huaweicloudsdkdgc.v1.Cron`
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        r"""Sets the cron of this Schedule.

        :param cron: The cron of this Schedule.
        :type cron: :class:`huaweicloudsdkdgc.v1.Cron`
        """
        self._cron = cron

    @property
    def event(self):
        r"""Gets the event of this Schedule.

        :return: The event of this Schedule.
        :rtype: :class:`huaweicloudsdkdgc.v1.Event`
        """
        return self._event

    @event.setter
    def event(self, event):
        r"""Sets the event of this Schedule.

        :param event: The event of this Schedule.
        :type event: :class:`huaweicloudsdkdgc.v1.Event`
        """
        self._event = event

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
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
