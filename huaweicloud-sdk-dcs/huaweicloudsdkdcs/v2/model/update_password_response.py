# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePasswordResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lock_time': 'str',
        'result': 'str',
        'lock_time_left': 'str',
        'retry_times_left': 'str',
        'message': 'str'
    }

    attribute_map = {
        'lock_time': 'lock_time',
        'result': 'result',
        'lock_time_left': 'lock_time_left',
        'retry_times_left': 'retry_times_left',
        'message': 'message'
    }

    def __init__(self, lock_time=None, result=None, lock_time_left=None, retry_times_left=None, message=None):
        """UpdatePasswordResponse

        The model defined in huaweicloud sdk

        :param lock_time: 锁定时间。验证失败时和锁定时该参数返回不为null
        :type lock_time: str
        :param result: 密码修改结果： - 成功：success； - 密码验证失败：passwordFailed； - 已锁定：locked； - 失败：failed。 
        :type result: str
        :param lock_time_left: 锁定剩余时间。锁定时该参数返回不为null
        :type lock_time_left: str
        :param retry_times_left: 密码验证剩余次数。验证失败时该参数返回不为null
        :type retry_times_left: str
        :param message: 修改结果。
        :type message: str
        """
        
        super(UpdatePasswordResponse, self).__init__()

        self._lock_time = None
        self._result = None
        self._lock_time_left = None
        self._retry_times_left = None
        self._message = None
        self.discriminator = None

        if lock_time is not None:
            self.lock_time = lock_time
        if result is not None:
            self.result = result
        if lock_time_left is not None:
            self.lock_time_left = lock_time_left
        if retry_times_left is not None:
            self.retry_times_left = retry_times_left
        if message is not None:
            self.message = message

    @property
    def lock_time(self):
        """Gets the lock_time of this UpdatePasswordResponse.

        锁定时间。验证失败时和锁定时该参数返回不为null

        :return: The lock_time of this UpdatePasswordResponse.
        :rtype: str
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this UpdatePasswordResponse.

        锁定时间。验证失败时和锁定时该参数返回不为null

        :param lock_time: The lock_time of this UpdatePasswordResponse.
        :type lock_time: str
        """
        self._lock_time = lock_time

    @property
    def result(self):
        """Gets the result of this UpdatePasswordResponse.

        密码修改结果： - 成功：success； - 密码验证失败：passwordFailed； - 已锁定：locked； - 失败：failed。 

        :return: The result of this UpdatePasswordResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this UpdatePasswordResponse.

        密码修改结果： - 成功：success； - 密码验证失败：passwordFailed； - 已锁定：locked； - 失败：failed。 

        :param result: The result of this UpdatePasswordResponse.
        :type result: str
        """
        self._result = result

    @property
    def lock_time_left(self):
        """Gets the lock_time_left of this UpdatePasswordResponse.

        锁定剩余时间。锁定时该参数返回不为null

        :return: The lock_time_left of this UpdatePasswordResponse.
        :rtype: str
        """
        return self._lock_time_left

    @lock_time_left.setter
    def lock_time_left(self, lock_time_left):
        """Sets the lock_time_left of this UpdatePasswordResponse.

        锁定剩余时间。锁定时该参数返回不为null

        :param lock_time_left: The lock_time_left of this UpdatePasswordResponse.
        :type lock_time_left: str
        """
        self._lock_time_left = lock_time_left

    @property
    def retry_times_left(self):
        """Gets the retry_times_left of this UpdatePasswordResponse.

        密码验证剩余次数。验证失败时该参数返回不为null

        :return: The retry_times_left of this UpdatePasswordResponse.
        :rtype: str
        """
        return self._retry_times_left

    @retry_times_left.setter
    def retry_times_left(self, retry_times_left):
        """Sets the retry_times_left of this UpdatePasswordResponse.

        密码验证剩余次数。验证失败时该参数返回不为null

        :param retry_times_left: The retry_times_left of this UpdatePasswordResponse.
        :type retry_times_left: str
        """
        self._retry_times_left = retry_times_left

    @property
    def message(self):
        """Gets the message of this UpdatePasswordResponse.

        修改结果。

        :return: The message of this UpdatePasswordResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UpdatePasswordResponse.

        修改结果。

        :param message: The message of this UpdatePasswordResponse.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, UpdatePasswordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
