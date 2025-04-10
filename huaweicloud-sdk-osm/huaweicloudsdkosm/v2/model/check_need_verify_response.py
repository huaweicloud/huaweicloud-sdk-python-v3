# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckNeedVerifyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'need_verify_code': 'int',
        'expire_time': 'datetime'
    }

    attribute_map = {
        'need_verify_code': 'need_verify_code',
        'expire_time': 'expire_time'
    }

    def __init__(self, need_verify_code=None, expire_time=None):
        r"""CheckNeedVerifyResponse

        The model defined in huaweicloud sdk

        :param need_verify_code: 是否需要验证
        :type need_verify_code: int
        :param expire_time: 过期时间
        :type expire_time: datetime
        """
        
        super(CheckNeedVerifyResponse, self).__init__()

        self._need_verify_code = None
        self._expire_time = None
        self.discriminator = None

        if need_verify_code is not None:
            self.need_verify_code = need_verify_code
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def need_verify_code(self):
        r"""Gets the need_verify_code of this CheckNeedVerifyResponse.

        是否需要验证

        :return: The need_verify_code of this CheckNeedVerifyResponse.
        :rtype: int
        """
        return self._need_verify_code

    @need_verify_code.setter
    def need_verify_code(self, need_verify_code):
        r"""Sets the need_verify_code of this CheckNeedVerifyResponse.

        是否需要验证

        :param need_verify_code: The need_verify_code of this CheckNeedVerifyResponse.
        :type need_verify_code: int
        """
        self._need_verify_code = need_verify_code

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CheckNeedVerifyResponse.

        过期时间

        :return: The expire_time of this CheckNeedVerifyResponse.
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CheckNeedVerifyResponse.

        过期时间

        :param expire_time: The expire_time of this CheckNeedVerifyResponse.
        :type expire_time: datetime
        """
        self._expire_time = expire_time

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
        if not isinstance(other, CheckNeedVerifyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
