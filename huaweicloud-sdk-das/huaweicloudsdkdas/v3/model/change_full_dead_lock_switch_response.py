# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeFullDeadLockSwitchResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'status': 'int',
        'error_msg': 'str'
    }

    attribute_map = {
        'success': 'success',
        'status': 'status',
        'error_msg': 'error_msg'
    }

    def __init__(self, success=None, status=None, error_msg=None):
        r"""ChangeFullDeadLockSwitchResponse

        The model defined in huaweicloud sdk

        :param success: 是否成功
        :type success: bool
        :param status: 状态值， 1-成功, 2-失败无需轮循, 3-失败需要轮循
        :type status: int
        :param error_msg: 错误文案, 只有在状态为2时才显示
        :type error_msg: str
        """
        
        super(ChangeFullDeadLockSwitchResponse, self).__init__()

        self._success = None
        self._status = None
        self._error_msg = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if status is not None:
            self.status = status
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def success(self):
        r"""Gets the success of this ChangeFullDeadLockSwitchResponse.

        是否成功

        :return: The success of this ChangeFullDeadLockSwitchResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ChangeFullDeadLockSwitchResponse.

        是否成功

        :param success: The success of this ChangeFullDeadLockSwitchResponse.
        :type success: bool
        """
        self._success = success

    @property
    def status(self):
        r"""Gets the status of this ChangeFullDeadLockSwitchResponse.

        状态值， 1-成功, 2-失败无需轮循, 3-失败需要轮循

        :return: The status of this ChangeFullDeadLockSwitchResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ChangeFullDeadLockSwitchResponse.

        状态值， 1-成功, 2-失败无需轮循, 3-失败需要轮循

        :param status: The status of this ChangeFullDeadLockSwitchResponse.
        :type status: int
        """
        self._status = status

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ChangeFullDeadLockSwitchResponse.

        错误文案, 只有在状态为2时才显示

        :return: The error_msg of this ChangeFullDeadLockSwitchResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ChangeFullDeadLockSwitchResponse.

        错误文案, 只有在状态为2时才显示

        :param error_msg: The error_msg of this ChangeFullDeadLockSwitchResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ChangeFullDeadLockSwitchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
