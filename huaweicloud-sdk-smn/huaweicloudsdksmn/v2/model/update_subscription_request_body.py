# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubscriptionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'remark': 'str',
        'verification_code': 'str'
    }

    attribute_map = {
        'remark': 'remark',
        'verification_code': 'verification_code'
    }

    def __init__(self, remark=None, verification_code=None):
        r"""UpdateSubscriptionRequestBody

        The model defined in huaweicloud sdk

        :param remark: 订阅者备注。订阅者备注的最大长度为128byte。
        :type remark: str
        :param verification_code: 订阅终端收到的验证码。
        :type verification_code: str
        """
        
        

        self._remark = None
        self._verification_code = None
        self.discriminator = None

        if remark is not None:
            self.remark = remark
        if verification_code is not None:
            self.verification_code = verification_code

    @property
    def remark(self):
        r"""Gets the remark of this UpdateSubscriptionRequestBody.

        订阅者备注。订阅者备注的最大长度为128byte。

        :return: The remark of this UpdateSubscriptionRequestBody.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this UpdateSubscriptionRequestBody.

        订阅者备注。订阅者备注的最大长度为128byte。

        :param remark: The remark of this UpdateSubscriptionRequestBody.
        :type remark: str
        """
        self._remark = remark

    @property
    def verification_code(self):
        r"""Gets the verification_code of this UpdateSubscriptionRequestBody.

        订阅终端收到的验证码。

        :return: The verification_code of this UpdateSubscriptionRequestBody.
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        r"""Sets the verification_code of this UpdateSubscriptionRequestBody.

        订阅终端收到的验证码。

        :param verification_code: The verification_code of this UpdateSubscriptionRequestBody.
        :type verification_code: str
        """
        self._verification_code = verification_code

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
        if not isinstance(other, UpdateSubscriptionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
