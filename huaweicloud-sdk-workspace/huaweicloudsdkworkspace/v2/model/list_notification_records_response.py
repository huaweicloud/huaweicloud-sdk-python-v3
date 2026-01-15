# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'notification_records': 'list[NotificationRecordInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'notification_records': 'notification_records'
    }

    def __init__(self, total_count=None, notification_records=None):
        r"""ListNotificationRecordsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数
        :type total_count: int
        :param notification_records: 通知拦截记录信息
        :type notification_records: list[:class:`huaweicloudsdkworkspace.v2.NotificationRecordInfo`]
        """
        
        super().__init__()

        self._total_count = None
        self._notification_records = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if notification_records is not None:
            self.notification_records = notification_records

    @property
    def total_count(self):
        r"""Gets the total_count of this ListNotificationRecordsResponse.

        总数

        :return: The total_count of this ListNotificationRecordsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListNotificationRecordsResponse.

        总数

        :param total_count: The total_count of this ListNotificationRecordsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def notification_records(self):
        r"""Gets the notification_records of this ListNotificationRecordsResponse.

        通知拦截记录信息

        :return: The notification_records of this ListNotificationRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.NotificationRecordInfo`]
        """
        return self._notification_records

    @notification_records.setter
    def notification_records(self, notification_records):
        r"""Sets the notification_records of this ListNotificationRecordsResponse.

        通知拦截记录信息

        :param notification_records: The notification_records of this ListNotificationRecordsResponse.
        :type notification_records: list[:class:`huaweicloudsdkworkspace.v2.NotificationRecordInfo`]
        """
        self._notification_records = notification_records

    def to_dict(self):
        import warnings
        warnings.warn("ListNotificationRecordsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListNotificationRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
