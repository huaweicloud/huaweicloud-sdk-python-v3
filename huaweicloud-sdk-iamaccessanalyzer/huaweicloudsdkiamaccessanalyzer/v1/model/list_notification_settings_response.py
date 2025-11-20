# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationSettingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_settings': 'list[NotificationSettingSummary]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'notification_settings': 'notification_settings',
        'page_info': 'page_info'
    }

    def __init__(self, notification_settings=None, page_info=None):
        r"""ListNotificationSettingsResponse

        The model defined in huaweicloud sdk

        :param notification_settings: 消息通知配置列表。
        :type notification_settings: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.NotificationSettingSummary`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        
        super().__init__()

        self._notification_settings = None
        self._page_info = None
        self.discriminator = None

        if notification_settings is not None:
            self.notification_settings = notification_settings
        if page_info is not None:
            self.page_info = page_info

    @property
    def notification_settings(self):
        r"""Gets the notification_settings of this ListNotificationSettingsResponse.

        消息通知配置列表。

        :return: The notification_settings of this ListNotificationSettingsResponse.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.NotificationSettingSummary`]
        """
        return self._notification_settings

    @notification_settings.setter
    def notification_settings(self, notification_settings):
        r"""Sets the notification_settings of this ListNotificationSettingsResponse.

        消息通知配置列表。

        :param notification_settings: The notification_settings of this ListNotificationSettingsResponse.
        :type notification_settings: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.NotificationSettingSummary`]
        """
        self._notification_settings = notification_settings

    @property
    def page_info(self):
        r"""Gets the page_info of this ListNotificationSettingsResponse.

        :return: The page_info of this ListNotificationSettingsResponse.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListNotificationSettingsResponse.

        :param page_info: The page_info of this ListNotificationSettingsResponse.
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListNotificationSettingsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListNotificationSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
