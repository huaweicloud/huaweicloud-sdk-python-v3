# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignSpecialAgreementResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agreement_type': 'str',
        'current_version': 'str',
        'signed_version': 'str',
        'signed_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'agreement_type': 'agreement_type',
        'current_version': 'current_version',
        'signed_version': 'signed_version',
        'signed_time': 'signed_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, agreement_type=None, current_version=None, signed_version=None, signed_time=None, x_request_id=None):
        r"""SignSpecialAgreementResponse

        The model defined in huaweicloud sdk

        :param agreement_type: 当前服务协议类型
        :type agreement_type: str
        :param current_version: 当前服务协议版本
        :type current_version: str
        :param signed_version: 签署服务协议版本
        :type signed_version: str
        :param signed_time: 协议签署时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type signed_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(SignSpecialAgreementResponse, self).__init__()

        self._agreement_type = None
        self._current_version = None
        self._signed_version = None
        self._signed_time = None
        self._x_request_id = None
        self.discriminator = None

        if agreement_type is not None:
            self.agreement_type = agreement_type
        if current_version is not None:
            self.current_version = current_version
        if signed_version is not None:
            self.signed_version = signed_version
        if signed_time is not None:
            self.signed_time = signed_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def agreement_type(self):
        r"""Gets the agreement_type of this SignSpecialAgreementResponse.

        当前服务协议类型

        :return: The agreement_type of this SignSpecialAgreementResponse.
        :rtype: str
        """
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, agreement_type):
        r"""Sets the agreement_type of this SignSpecialAgreementResponse.

        当前服务协议类型

        :param agreement_type: The agreement_type of this SignSpecialAgreementResponse.
        :type agreement_type: str
        """
        self._agreement_type = agreement_type

    @property
    def current_version(self):
        r"""Gets the current_version of this SignSpecialAgreementResponse.

        当前服务协议版本

        :return: The current_version of this SignSpecialAgreementResponse.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this SignSpecialAgreementResponse.

        当前服务协议版本

        :param current_version: The current_version of this SignSpecialAgreementResponse.
        :type current_version: str
        """
        self._current_version = current_version

    @property
    def signed_version(self):
        r"""Gets the signed_version of this SignSpecialAgreementResponse.

        签署服务协议版本

        :return: The signed_version of this SignSpecialAgreementResponse.
        :rtype: str
        """
        return self._signed_version

    @signed_version.setter
    def signed_version(self, signed_version):
        r"""Sets the signed_version of this SignSpecialAgreementResponse.

        签署服务协议版本

        :param signed_version: The signed_version of this SignSpecialAgreementResponse.
        :type signed_version: str
        """
        self._signed_version = signed_version

    @property
    def signed_time(self):
        r"""Gets the signed_time of this SignSpecialAgreementResponse.

        协议签署时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The signed_time of this SignSpecialAgreementResponse.
        :rtype: str
        """
        return self._signed_time

    @signed_time.setter
    def signed_time(self, signed_time):
        r"""Sets the signed_time of this SignSpecialAgreementResponse.

        协议签署时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param signed_time: The signed_time of this SignSpecialAgreementResponse.
        :type signed_time: str
        """
        self._signed_time = signed_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this SignSpecialAgreementResponse.

        :return: The x_request_id of this SignSpecialAgreementResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this SignSpecialAgreementResponse.

        :param x_request_id: The x_request_id of this SignSpecialAgreementResponse.
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
        if not isinstance(other, SignSpecialAgreementResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
