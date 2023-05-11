# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetPasswordResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retry_times_left': 'str',
        'lock_time': 'str',
        'lock_time_left': 'str'
    }

    attribute_map = {
        'retry_times_left': 'retry_times_left',
        'lock_time': 'lock_time',
        'lock_time_left': 'lock_time_left'
    }

    def __init__(self, retry_times_left=None, lock_time=None, lock_time_left=None):
        """ResetPasswordResponse

        The model defined in huaweicloud sdk

        :param retry_times_left: 密码验证剩余次数
        :type retry_times_left: str
        :param lock_time: 锁定时间
        :type lock_time: str
        :param lock_time_left: 锁定剩余时间
        :type lock_time_left: str
        """
        
        super(ResetPasswordResponse, self).__init__()

        self._retry_times_left = None
        self._lock_time = None
        self._lock_time_left = None
        self.discriminator = None

        if retry_times_left is not None:
            self.retry_times_left = retry_times_left
        if lock_time is not None:
            self.lock_time = lock_time
        if lock_time_left is not None:
            self.lock_time_left = lock_time_left

    @property
    def retry_times_left(self):
        """Gets the retry_times_left of this ResetPasswordResponse.

        密码验证剩余次数

        :return: The retry_times_left of this ResetPasswordResponse.
        :rtype: str
        """
        return self._retry_times_left

    @retry_times_left.setter
    def retry_times_left(self, retry_times_left):
        """Sets the retry_times_left of this ResetPasswordResponse.

        密码验证剩余次数

        :param retry_times_left: The retry_times_left of this ResetPasswordResponse.
        :type retry_times_left: str
        """
        self._retry_times_left = retry_times_left

    @property
    def lock_time(self):
        """Gets the lock_time of this ResetPasswordResponse.

        锁定时间

        :return: The lock_time of this ResetPasswordResponse.
        :rtype: str
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this ResetPasswordResponse.

        锁定时间

        :param lock_time: The lock_time of this ResetPasswordResponse.
        :type lock_time: str
        """
        self._lock_time = lock_time

    @property
    def lock_time_left(self):
        """Gets the lock_time_left of this ResetPasswordResponse.

        锁定剩余时间

        :return: The lock_time_left of this ResetPasswordResponse.
        :rtype: str
        """
        return self._lock_time_left

    @lock_time_left.setter
    def lock_time_left(self, lock_time_left):
        """Sets the lock_time_left of this ResetPasswordResponse.

        锁定剩余时间

        :param lock_time_left: The lock_time_left of this ResetPasswordResponse.
        :type lock_time_left: str
        """
        self._lock_time_left = lock_time_left

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
        if not isinstance(other, ResetPasswordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
