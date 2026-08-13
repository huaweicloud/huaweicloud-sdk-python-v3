# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangePaymentModeNewResponse(SdkResponse):

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
        'can_set_free_time': 'float',
        'error_msg': 'str'
    }

    attribute_map = {
        'success': 'success',
        'can_set_free_time': 'can_set_free_time',
        'error_msg': 'error_msg'
    }

    def __init__(self, success=None, can_set_free_time=None, error_msg=None):
        r"""ChangePaymentModeNewResponse

        The model defined in huaweicloud sdk

        :param success: 是否成功
        :type success: bool
        :param can_set_free_time: 可恢复为免费实例的时间
        :type can_set_free_time: float
        :param error_msg: 错误信息
        :type error_msg: str
        """
        
        super().__init__()

        self._success = None
        self._can_set_free_time = None
        self._error_msg = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if can_set_free_time is not None:
            self.can_set_free_time = can_set_free_time
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def success(self):
        r"""Gets the success of this ChangePaymentModeNewResponse.

        是否成功

        :return: The success of this ChangePaymentModeNewResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ChangePaymentModeNewResponse.

        是否成功

        :param success: The success of this ChangePaymentModeNewResponse.
        :type success: bool
        """
        self._success = success

    @property
    def can_set_free_time(self):
        r"""Gets the can_set_free_time of this ChangePaymentModeNewResponse.

        可恢复为免费实例的时间

        :return: The can_set_free_time of this ChangePaymentModeNewResponse.
        :rtype: float
        """
        return self._can_set_free_time

    @can_set_free_time.setter
    def can_set_free_time(self, can_set_free_time):
        r"""Sets the can_set_free_time of this ChangePaymentModeNewResponse.

        可恢复为免费实例的时间

        :param can_set_free_time: The can_set_free_time of this ChangePaymentModeNewResponse.
        :type can_set_free_time: float
        """
        self._can_set_free_time = can_set_free_time

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ChangePaymentModeNewResponse.

        错误信息

        :return: The error_msg of this ChangePaymentModeNewResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ChangePaymentModeNewResponse.

        错误信息

        :param error_msg: The error_msg of this ChangePaymentModeNewResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    def to_dict(self):
        import warnings
        warnings.warn("ChangePaymentModeNewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ChangePaymentModeNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
