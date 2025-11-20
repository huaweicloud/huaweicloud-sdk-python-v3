# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSmartLiveUserConfigResponse(SdkResponse):

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
        'live_notify_config': 'LiveNotifyConfig',
        'x_request_id': 'str'
    }

    attribute_map = {
        'live_exit_config': 'live_exit_config',
        'live_event_callback_config': 'live_event_callback_config',
        'live_notify_config': 'live_notify_config',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, live_exit_config=None, live_event_callback_config=None, live_notify_config=None, x_request_id=None):
        r"""ShowSmartLiveUserConfigResponse

        The model defined in huaweicloud sdk

        :param live_exit_config: 
        :type live_exit_config: :class:`huaweicloudsdkmetastudio.v1.LiveExitConfig`
        :param live_event_callback_config: 
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        :param live_notify_config: 
        :type live_notify_config: :class:`huaweicloudsdkmetastudio.v1.LiveNotifyConfig`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._live_exit_config = None
        self._live_event_callback_config = None
        self._live_notify_config = None
        self._x_request_id = None
        self.discriminator = None

        if live_exit_config is not None:
            self.live_exit_config = live_exit_config
        if live_event_callback_config is not None:
            self.live_event_callback_config = live_event_callback_config
        if live_notify_config is not None:
            self.live_notify_config = live_notify_config
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def live_exit_config(self):
        r"""Gets the live_exit_config of this ShowSmartLiveUserConfigResponse.

        :return: The live_exit_config of this ShowSmartLiveUserConfigResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveExitConfig`
        """
        return self._live_exit_config

    @live_exit_config.setter
    def live_exit_config(self, live_exit_config):
        r"""Sets the live_exit_config of this ShowSmartLiveUserConfigResponse.

        :param live_exit_config: The live_exit_config of this ShowSmartLiveUserConfigResponse.
        :type live_exit_config: :class:`huaweicloudsdkmetastudio.v1.LiveExitConfig`
        """
        self._live_exit_config = live_exit_config

    @property
    def live_event_callback_config(self):
        r"""Gets the live_event_callback_config of this ShowSmartLiveUserConfigResponse.

        :return: The live_event_callback_config of this ShowSmartLiveUserConfigResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        return self._live_event_callback_config

    @live_event_callback_config.setter
    def live_event_callback_config(self, live_event_callback_config):
        r"""Sets the live_event_callback_config of this ShowSmartLiveUserConfigResponse.

        :param live_event_callback_config: The live_event_callback_config of this ShowSmartLiveUserConfigResponse.
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        self._live_event_callback_config = live_event_callback_config

    @property
    def live_notify_config(self):
        r"""Gets the live_notify_config of this ShowSmartLiveUserConfigResponse.

        :return: The live_notify_config of this ShowSmartLiveUserConfigResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveNotifyConfig`
        """
        return self._live_notify_config

    @live_notify_config.setter
    def live_notify_config(self, live_notify_config):
        r"""Sets the live_notify_config of this ShowSmartLiveUserConfigResponse.

        :param live_notify_config: The live_notify_config of this ShowSmartLiveUserConfigResponse.
        :type live_notify_config: :class:`huaweicloudsdkmetastudio.v1.LiveNotifyConfig`
        """
        self._live_notify_config = live_notify_config

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowSmartLiveUserConfigResponse.

        :return: The x_request_id of this ShowSmartLiveUserConfigResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowSmartLiveUserConfigResponse.

        :param x_request_id: The x_request_id of this ShowSmartLiveUserConfigResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowSmartLiveUserConfigResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowSmartLiveUserConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
