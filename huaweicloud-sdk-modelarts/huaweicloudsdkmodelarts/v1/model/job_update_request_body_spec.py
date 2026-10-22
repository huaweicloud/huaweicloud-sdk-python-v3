# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobUpdateRequestBodySpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification': 'Notification',
        'schedule_policy': 'JobUpdateRequestBodySpecSchedulePolicy'
    }

    attribute_map = {
        'notification': 'notification',
        'schedule_policy': 'schedule_policy'
    }

    def __init__(self, notification=None, schedule_policy=None):
        r"""JobUpdateRequestBodySpec

        The model defined in huaweicloud sdk

        :param notification: 
        :type notification: :class:`huaweicloudsdkmodelarts.v1.Notification`
        :param schedule_policy: 
        :type schedule_policy: :class:`huaweicloudsdkmodelarts.v1.JobUpdateRequestBodySpecSchedulePolicy`
        """
        
        

        self._notification = None
        self._schedule_policy = None
        self.discriminator = None

        if notification is not None:
            self.notification = notification
        if schedule_policy is not None:
            self.schedule_policy = schedule_policy

    @property
    def notification(self):
        r"""Gets the notification of this JobUpdateRequestBodySpec.

        :return: The notification of this JobUpdateRequestBodySpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Notification`
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        r"""Sets the notification of this JobUpdateRequestBodySpec.

        :param notification: The notification of this JobUpdateRequestBodySpec.
        :type notification: :class:`huaweicloudsdkmodelarts.v1.Notification`
        """
        self._notification = notification

    @property
    def schedule_policy(self):
        r"""Gets the schedule_policy of this JobUpdateRequestBodySpec.

        :return: The schedule_policy of this JobUpdateRequestBodySpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobUpdateRequestBodySpecSchedulePolicy`
        """
        return self._schedule_policy

    @schedule_policy.setter
    def schedule_policy(self, schedule_policy):
        r"""Sets the schedule_policy of this JobUpdateRequestBodySpec.

        :param schedule_policy: The schedule_policy of this JobUpdateRequestBodySpec.
        :type schedule_policy: :class:`huaweicloudsdkmodelarts.v1.JobUpdateRequestBodySpecSchedulePolicy`
        """
        self._schedule_policy = schedule_policy

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
        if not isinstance(other, JobUpdateRequestBodySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
