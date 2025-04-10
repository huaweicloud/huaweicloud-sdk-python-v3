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
        'lock_time_left': 'str',
        'code': 'str',
        'message': 'str',
        'ext_message': 'str'
    }

    attribute_map = {
        'retry_times_left': 'retry_times_left',
        'lock_time': 'lock_time',
        'lock_time_left': 'lock_time_left',
        'code': 'code',
        'message': 'message',
        'ext_message': 'ext_message'
    }

    def __init__(self, retry_times_left=None, lock_time=None, lock_time_left=None, code=None, message=None, ext_message=None):
        r"""ResetPasswordResponse

        The model defined in huaweicloud sdk

        :param retry_times_left: 密码验证剩余次数
        :type retry_times_left: str
        :param lock_time: 锁定时间
        :type lock_time: str
        :param lock_time_left: 锁定剩余时间
        :type lock_time_left: str
        :param code: **参数解释**： 重置密码结果编号。 **取值范围**： - 1：重置密码成功。 - 3：实例被锁定。 
        :type code: str
        :param message: **参数解释**： 重置密码结果信息。 **取值范围**： - success - instance is locked 
        :type message: str
        :param ext_message: **参数解释**： 重置密码错误信息，若重置密码成功，则为null。 **取值范围**： 不涉及。 
        :type ext_message: str
        """
        
        super(ResetPasswordResponse, self).__init__()

        self._retry_times_left = None
        self._lock_time = None
        self._lock_time_left = None
        self._code = None
        self._message = None
        self._ext_message = None
        self.discriminator = None

        if retry_times_left is not None:
            self.retry_times_left = retry_times_left
        if lock_time is not None:
            self.lock_time = lock_time
        if lock_time_left is not None:
            self.lock_time_left = lock_time_left
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if ext_message is not None:
            self.ext_message = ext_message

    @property
    def retry_times_left(self):
        r"""Gets the retry_times_left of this ResetPasswordResponse.

        密码验证剩余次数

        :return: The retry_times_left of this ResetPasswordResponse.
        :rtype: str
        """
        return self._retry_times_left

    @retry_times_left.setter
    def retry_times_left(self, retry_times_left):
        r"""Sets the retry_times_left of this ResetPasswordResponse.

        密码验证剩余次数

        :param retry_times_left: The retry_times_left of this ResetPasswordResponse.
        :type retry_times_left: str
        """
        self._retry_times_left = retry_times_left

    @property
    def lock_time(self):
        r"""Gets the lock_time of this ResetPasswordResponse.

        锁定时间

        :return: The lock_time of this ResetPasswordResponse.
        :rtype: str
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this ResetPasswordResponse.

        锁定时间

        :param lock_time: The lock_time of this ResetPasswordResponse.
        :type lock_time: str
        """
        self._lock_time = lock_time

    @property
    def lock_time_left(self):
        r"""Gets the lock_time_left of this ResetPasswordResponse.

        锁定剩余时间

        :return: The lock_time_left of this ResetPasswordResponse.
        :rtype: str
        """
        return self._lock_time_left

    @lock_time_left.setter
    def lock_time_left(self, lock_time_left):
        r"""Sets the lock_time_left of this ResetPasswordResponse.

        锁定剩余时间

        :param lock_time_left: The lock_time_left of this ResetPasswordResponse.
        :type lock_time_left: str
        """
        self._lock_time_left = lock_time_left

    @property
    def code(self):
        r"""Gets the code of this ResetPasswordResponse.

        **参数解释**： 重置密码结果编号。 **取值范围**： - 1：重置密码成功。 - 3：实例被锁定。 

        :return: The code of this ResetPasswordResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ResetPasswordResponse.

        **参数解释**： 重置密码结果编号。 **取值范围**： - 1：重置密码成功。 - 3：实例被锁定。 

        :param code: The code of this ResetPasswordResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ResetPasswordResponse.

        **参数解释**： 重置密码结果信息。 **取值范围**： - success - instance is locked 

        :return: The message of this ResetPasswordResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ResetPasswordResponse.

        **参数解释**： 重置密码结果信息。 **取值范围**： - success - instance is locked 

        :param message: The message of this ResetPasswordResponse.
        :type message: str
        """
        self._message = message

    @property
    def ext_message(self):
        r"""Gets the ext_message of this ResetPasswordResponse.

        **参数解释**： 重置密码错误信息，若重置密码成功，则为null。 **取值范围**： 不涉及。 

        :return: The ext_message of this ResetPasswordResponse.
        :rtype: str
        """
        return self._ext_message

    @ext_message.setter
    def ext_message(self, ext_message):
        r"""Sets the ext_message of this ResetPasswordResponse.

        **参数解释**： 重置密码错误信息，若重置密码成功，则为null。 **取值范围**： 不涉及。 

        :param ext_message: The ext_message of this ResetPasswordResponse.
        :type ext_message: str
        """
        self._ext_message = ext_message

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
