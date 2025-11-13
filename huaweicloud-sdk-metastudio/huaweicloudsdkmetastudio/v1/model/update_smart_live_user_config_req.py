# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSmartLiveUserConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'live_exit_config': 'LiveExitConfig',
        'live_event_callback_config': 'LiveEventCallBackConfig',
        'live_notify_config': 'LiveNotifyConfigReq'
    }

    attribute_map = {
        'live_exit_config': 'live_exit_config',
        'live_event_callback_config': 'live_event_callback_config',
        'live_notify_config': 'live_notify_config'
    }

    def __init__(self, live_exit_config=None, live_event_callback_config=None, live_notify_config=None):
        r"""UpdateSmartLiveUserConfigReq

        The model defined in huaweicloud sdk

        :param live_exit_config: 
        :type live_exit_config: :class:`huaweicloudsdkmetastudio.v1.LiveExitConfig`
        :param live_event_callback_config: 
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        :param live_notify_config: 
        :type live_notify_config: :class:`huaweicloudsdkmetastudio.v1.LiveNotifyConfigReq`
        """
        
        

        self._live_exit_config = None
        self._live_event_callback_config = None
        self._live_notify_config = None
        self.discriminator = None

        if live_exit_config is not None:
            self.live_exit_config = live_exit_config
        if live_event_callback_config is not None:
            self.live_event_callback_config = live_event_callback_config
        if live_notify_config is not None:
            self.live_notify_config = live_notify_config

    @property
    def live_exit_config(self):
        r"""Gets the live_exit_config of this UpdateSmartLiveUserConfigReq.

        :return: The live_exit_config of this UpdateSmartLiveUserConfigReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveExitConfig`
        """
        return self._live_exit_config

    @live_exit_config.setter
    def live_exit_config(self, live_exit_config):
        r"""Sets the live_exit_config of this UpdateSmartLiveUserConfigReq.

        :param live_exit_config: The live_exit_config of this UpdateSmartLiveUserConfigReq.
        :type live_exit_config: :class:`huaweicloudsdkmetastudio.v1.LiveExitConfig`
        """
        self._live_exit_config = live_exit_config

    @property
    def live_event_callback_config(self):
        r"""Gets the live_event_callback_config of this UpdateSmartLiveUserConfigReq.

        :return: The live_event_callback_config of this UpdateSmartLiveUserConfigReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        return self._live_event_callback_config

    @live_event_callback_config.setter
    def live_event_callback_config(self, live_event_callback_config):
        r"""Sets the live_event_callback_config of this UpdateSmartLiveUserConfigReq.

        :param live_event_callback_config: The live_event_callback_config of this UpdateSmartLiveUserConfigReq.
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        self._live_event_callback_config = live_event_callback_config

    @property
    def live_notify_config(self):
        r"""Gets the live_notify_config of this UpdateSmartLiveUserConfigReq.

        :return: The live_notify_config of this UpdateSmartLiveUserConfigReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveNotifyConfigReq`
        """
        return self._live_notify_config

    @live_notify_config.setter
    def live_notify_config(self, live_notify_config):
        r"""Sets the live_notify_config of this UpdateSmartLiveUserConfigReq.

        :param live_notify_config: The live_notify_config of this UpdateSmartLiveUserConfigReq.
        :type live_notify_config: :class:`huaweicloudsdkmetastudio.v1.LiveNotifyConfigReq`
        """
        self._live_notify_config = live_notify_config

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateSmartLiveUserConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
