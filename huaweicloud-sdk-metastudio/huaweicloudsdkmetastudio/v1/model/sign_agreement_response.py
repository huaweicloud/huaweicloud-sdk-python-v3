# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignAgreementResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_version': 'str',
        'need_to_sign': 'bool',
        'signed_version': 'str',
        'signed_time': 'str',
        'resign_deadline': 'str',
        'resign_expire_process_mode': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'current_version': 'current_version',
        'need_to_sign': 'need_to_sign',
        'signed_version': 'signed_version',
        'signed_time': 'signed_time',
        'resign_deadline': 'resign_deadline',
        'resign_expire_process_mode': 'resign_expire_process_mode',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, current_version=None, need_to_sign=None, signed_version=None, signed_time=None, resign_deadline=None, resign_expire_process_mode=None, x_request_id=None):
        r"""SignAgreementResponse

        The model defined in huaweicloud sdk

        :param current_version: 当前服务协议版本
        :type current_version: str
        :param need_to_sign: 是否需要签署
        :type need_to_sign: bool
        :param signed_version: 签署服务协议版本
        :type signed_version: str
        :param signed_time: 协议签署时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type signed_time: str
        :param resign_deadline: 签署最后期限。格式遵循：RFC 3339 如\&quot;2024-10-10T15:59:59Z\&quot;
        :type resign_deadline: str
        :param resign_expire_process_mode: 重新签署过期处理方式:EXPIRE_AUTO_AGREE 自动签署协议,EXPIRE_STOP_SERVICE 强制签署协议
        :type resign_expire_process_mode: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(SignAgreementResponse, self).__init__()

        self._current_version = None
        self._need_to_sign = None
        self._signed_version = None
        self._signed_time = None
        self._resign_deadline = None
        self._resign_expire_process_mode = None
        self._x_request_id = None
        self.discriminator = None

        if current_version is not None:
            self.current_version = current_version
        if need_to_sign is not None:
            self.need_to_sign = need_to_sign
        if signed_version is not None:
            self.signed_version = signed_version
        if signed_time is not None:
            self.signed_time = signed_time
        if resign_deadline is not None:
            self.resign_deadline = resign_deadline
        if resign_expire_process_mode is not None:
            self.resign_expire_process_mode = resign_expire_process_mode
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def current_version(self):
        r"""Gets the current_version of this SignAgreementResponse.

        当前服务协议版本

        :return: The current_version of this SignAgreementResponse.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this SignAgreementResponse.

        当前服务协议版本

        :param current_version: The current_version of this SignAgreementResponse.
        :type current_version: str
        """
        self._current_version = current_version

    @property
    def need_to_sign(self):
        r"""Gets the need_to_sign of this SignAgreementResponse.

        是否需要签署

        :return: The need_to_sign of this SignAgreementResponse.
        :rtype: bool
        """
        return self._need_to_sign

    @need_to_sign.setter
    def need_to_sign(self, need_to_sign):
        r"""Sets the need_to_sign of this SignAgreementResponse.

        是否需要签署

        :param need_to_sign: The need_to_sign of this SignAgreementResponse.
        :type need_to_sign: bool
        """
        self._need_to_sign = need_to_sign

    @property
    def signed_version(self):
        r"""Gets the signed_version of this SignAgreementResponse.

        签署服务协议版本

        :return: The signed_version of this SignAgreementResponse.
        :rtype: str
        """
        return self._signed_version

    @signed_version.setter
    def signed_version(self, signed_version):
        r"""Sets the signed_version of this SignAgreementResponse.

        签署服务协议版本

        :param signed_version: The signed_version of this SignAgreementResponse.
        :type signed_version: str
        """
        self._signed_version = signed_version

    @property
    def signed_time(self):
        r"""Gets the signed_time of this SignAgreementResponse.

        协议签署时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The signed_time of this SignAgreementResponse.
        :rtype: str
        """
        return self._signed_time

    @signed_time.setter
    def signed_time(self, signed_time):
        r"""Sets the signed_time of this SignAgreementResponse.

        协议签署时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param signed_time: The signed_time of this SignAgreementResponse.
        :type signed_time: str
        """
        self._signed_time = signed_time

    @property
    def resign_deadline(self):
        r"""Gets the resign_deadline of this SignAgreementResponse.

        签署最后期限。格式遵循：RFC 3339 如\"2024-10-10T15:59:59Z\"

        :return: The resign_deadline of this SignAgreementResponse.
        :rtype: str
        """
        return self._resign_deadline

    @resign_deadline.setter
    def resign_deadline(self, resign_deadline):
        r"""Sets the resign_deadline of this SignAgreementResponse.

        签署最后期限。格式遵循：RFC 3339 如\"2024-10-10T15:59:59Z\"

        :param resign_deadline: The resign_deadline of this SignAgreementResponse.
        :type resign_deadline: str
        """
        self._resign_deadline = resign_deadline

    @property
    def resign_expire_process_mode(self):
        r"""Gets the resign_expire_process_mode of this SignAgreementResponse.

        重新签署过期处理方式:EXPIRE_AUTO_AGREE 自动签署协议,EXPIRE_STOP_SERVICE 强制签署协议

        :return: The resign_expire_process_mode of this SignAgreementResponse.
        :rtype: str
        """
        return self._resign_expire_process_mode

    @resign_expire_process_mode.setter
    def resign_expire_process_mode(self, resign_expire_process_mode):
        r"""Sets the resign_expire_process_mode of this SignAgreementResponse.

        重新签署过期处理方式:EXPIRE_AUTO_AGREE 自动签署协议,EXPIRE_STOP_SERVICE 强制签署协议

        :param resign_expire_process_mode: The resign_expire_process_mode of this SignAgreementResponse.
        :type resign_expire_process_mode: str
        """
        self._resign_expire_process_mode = resign_expire_process_mode

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this SignAgreementResponse.

        :return: The x_request_id of this SignAgreementResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this SignAgreementResponse.

        :param x_request_id: The x_request_id of this SignAgreementResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, SignAgreementResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
