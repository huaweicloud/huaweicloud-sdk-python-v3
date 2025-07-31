# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateNotificationMaskTimeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_mask_ids': 'list[str]',
        'mask_type': 'MaskType',
        'start_date': 'date',
        'start_time': 'str',
        'end_date': 'date',
        'end_time': 'str',
        'effective_timezone': 'str'
    }

    attribute_map = {
        'notification_mask_ids': 'notification_mask_ids',
        'mask_type': 'mask_type',
        'start_date': 'start_date',
        'start_time': 'start_time',
        'end_date': 'end_date',
        'end_time': 'end_time',
        'effective_timezone': 'effective_timezone'
    }

    def __init__(self, notification_mask_ids=None, mask_type=None, start_date=None, start_time=None, end_date=None, end_time=None, effective_timezone=None):
        r"""BatchUpdateNotificationMaskTimeRequestBody

        The model defined in huaweicloud sdk

        :param notification_mask_ids: 关联编号
        :type notification_mask_ids: list[str]
        :param mask_type: 
        :type mask_type: :class:`huaweicloudsdkces.v2.MaskType`
        :param start_date: 屏蔽起始日期，yyyy-MM-dd。
        :type start_date: date
        :param start_time: 屏蔽起始时间，HH:mm:ss。
        :type start_time: str
        :param end_date: 屏蔽截止日期，yyyy-MM-dd。
        :type end_date: date
        :param end_time: 屏蔽截止时间，HH:mm:ss。
        :type end_time: str
        :param effective_timezone: 时区，形如：\&quot;GMT-08:00\&quot;、\&quot;GMT+08:00\&quot;、\&quot;GMT+0:00\&quot;
        :type effective_timezone: str
        """
        
        

        self._notification_mask_ids = None
        self._mask_type = None
        self._start_date = None
        self._start_time = None
        self._end_date = None
        self._end_time = None
        self._effective_timezone = None
        self.discriminator = None

        self.notification_mask_ids = notification_mask_ids
        self.mask_type = mask_type
        if start_date is not None:
            self.start_date = start_date
        if start_time is not None:
            self.start_time = start_time
        if end_date is not None:
            self.end_date = end_date
        if end_time is not None:
            self.end_time = end_time
        if effective_timezone is not None:
            self.effective_timezone = effective_timezone

    @property
    def notification_mask_ids(self):
        r"""Gets the notification_mask_ids of this BatchUpdateNotificationMaskTimeRequestBody.

        关联编号

        :return: The notification_mask_ids of this BatchUpdateNotificationMaskTimeRequestBody.
        :rtype: list[str]
        """
        return self._notification_mask_ids

    @notification_mask_ids.setter
    def notification_mask_ids(self, notification_mask_ids):
        r"""Sets the notification_mask_ids of this BatchUpdateNotificationMaskTimeRequestBody.

        关联编号

        :param notification_mask_ids: The notification_mask_ids of this BatchUpdateNotificationMaskTimeRequestBody.
        :type notification_mask_ids: list[str]
        """
        self._notification_mask_ids = notification_mask_ids

    @property
    def mask_type(self):
        r"""Gets the mask_type of this BatchUpdateNotificationMaskTimeRequestBody.

        :return: The mask_type of this BatchUpdateNotificationMaskTimeRequestBody.
        :rtype: :class:`huaweicloudsdkces.v2.MaskType`
        """
        return self._mask_type

    @mask_type.setter
    def mask_type(self, mask_type):
        r"""Sets the mask_type of this BatchUpdateNotificationMaskTimeRequestBody.

        :param mask_type: The mask_type of this BatchUpdateNotificationMaskTimeRequestBody.
        :type mask_type: :class:`huaweicloudsdkces.v2.MaskType`
        """
        self._mask_type = mask_type

    @property
    def start_date(self):
        r"""Gets the start_date of this BatchUpdateNotificationMaskTimeRequestBody.

        屏蔽起始日期，yyyy-MM-dd。

        :return: The start_date of this BatchUpdateNotificationMaskTimeRequestBody.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this BatchUpdateNotificationMaskTimeRequestBody.

        屏蔽起始日期，yyyy-MM-dd。

        :param start_date: The start_date of this BatchUpdateNotificationMaskTimeRequestBody.
        :type start_date: date
        """
        self._start_date = start_date

    @property
    def start_time(self):
        r"""Gets the start_time of this BatchUpdateNotificationMaskTimeRequestBody.

        屏蔽起始时间，HH:mm:ss。

        :return: The start_time of this BatchUpdateNotificationMaskTimeRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BatchUpdateNotificationMaskTimeRequestBody.

        屏蔽起始时间，HH:mm:ss。

        :param start_time: The start_time of this BatchUpdateNotificationMaskTimeRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_date(self):
        r"""Gets the end_date of this BatchUpdateNotificationMaskTimeRequestBody.

        屏蔽截止日期，yyyy-MM-dd。

        :return: The end_date of this BatchUpdateNotificationMaskTimeRequestBody.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this BatchUpdateNotificationMaskTimeRequestBody.

        屏蔽截止日期，yyyy-MM-dd。

        :param end_date: The end_date of this BatchUpdateNotificationMaskTimeRequestBody.
        :type end_date: date
        """
        self._end_date = end_date

    @property
    def end_time(self):
        r"""Gets the end_time of this BatchUpdateNotificationMaskTimeRequestBody.

        屏蔽截止时间，HH:mm:ss。

        :return: The end_time of this BatchUpdateNotificationMaskTimeRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BatchUpdateNotificationMaskTimeRequestBody.

        屏蔽截止时间，HH:mm:ss。

        :param end_time: The end_time of this BatchUpdateNotificationMaskTimeRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def effective_timezone(self):
        r"""Gets the effective_timezone of this BatchUpdateNotificationMaskTimeRequestBody.

        时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"

        :return: The effective_timezone of this BatchUpdateNotificationMaskTimeRequestBody.
        :rtype: str
        """
        return self._effective_timezone

    @effective_timezone.setter
    def effective_timezone(self, effective_timezone):
        r"""Sets the effective_timezone of this BatchUpdateNotificationMaskTimeRequestBody.

        时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"

        :param effective_timezone: The effective_timezone of this BatchUpdateNotificationMaskTimeRequestBody.
        :type effective_timezone: str
        """
        self._effective_timezone = effective_timezone

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
        if not isinstance(other, BatchUpdateNotificationMaskTimeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
