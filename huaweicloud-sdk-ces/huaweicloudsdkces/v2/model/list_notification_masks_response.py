# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationMasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_masks': 'list[ListNotificationMaskRespNotificationMasks]',
        'count': 'int'
    }

    attribute_map = {
        'notification_masks': 'notification_masks',
        'count': 'count'
    }

    def __init__(self, notification_masks=None, count=None):
        r"""ListNotificationMasksResponse

        The model defined in huaweicloud sdk

        :param notification_masks: **参数解释**： 通知屏蔽列表 
        :type notification_masks: list[:class:`huaweicloudsdkces.v2.ListNotificationMaskRespNotificationMasks`]
        :param count: **参数解释**： 通知屏蔽列表总数 **取值范围**： [0,99999] 
        :type count: int
        """
        
        super().__init__()

        self._notification_masks = None
        self._count = None
        self.discriminator = None

        if notification_masks is not None:
            self.notification_masks = notification_masks
        if count is not None:
            self.count = count

    @property
    def notification_masks(self):
        r"""Gets the notification_masks of this ListNotificationMasksResponse.

        **参数解释**： 通知屏蔽列表 

        :return: The notification_masks of this ListNotificationMasksResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.ListNotificationMaskRespNotificationMasks`]
        """
        return self._notification_masks

    @notification_masks.setter
    def notification_masks(self, notification_masks):
        r"""Sets the notification_masks of this ListNotificationMasksResponse.

        **参数解释**： 通知屏蔽列表 

        :param notification_masks: The notification_masks of this ListNotificationMasksResponse.
        :type notification_masks: list[:class:`huaweicloudsdkces.v2.ListNotificationMaskRespNotificationMasks`]
        """
        self._notification_masks = notification_masks

    @property
    def count(self):
        r"""Gets the count of this ListNotificationMasksResponse.

        **参数解释**： 通知屏蔽列表总数 **取值范围**： [0,99999] 

        :return: The count of this ListNotificationMasksResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListNotificationMasksResponse.

        **参数解释**： 通知屏蔽列表总数 **取值范围**： [0,99999] 

        :param count: The count of this ListNotificationMasksResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ListNotificationMasksResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListNotificationMasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
