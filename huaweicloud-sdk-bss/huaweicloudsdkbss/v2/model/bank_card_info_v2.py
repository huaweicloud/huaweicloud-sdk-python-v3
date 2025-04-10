# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BankCardInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bank_account': 'str',
        'areacode': 'str',
        'mobile': 'str',
        'verification_code': 'str'
    }

    attribute_map = {
        'bank_account': 'bank_account',
        'areacode': 'areacode',
        'mobile': 'mobile',
        'verification_code': 'verification_code'
    }

    def __init__(self, bank_account=None, areacode=None, mobile=None, verification_code=None):
        r"""BankCardInfoV2

        The model defined in huaweicloud sdk

        :param bank_account: 银行卡账号。 当identifyType为4时，不能为空。 银行账号输入规则：^[0-9a-zA-Z]，可以包含特殊横杠（-）字符。
        :type bank_account: str
        :param areacode: 国家/区号码。 例如：0086：中国大陆区号码。
        :type areacode: str
        :param mobile: 手机号码。
        :type mobile: str
        :param verification_code: 验证码。 请调用“发送验证码”接口获取。
        :type verification_code: str
        """
        
        

        self._bank_account = None
        self._areacode = None
        self._mobile = None
        self._verification_code = None
        self.discriminator = None

        self.bank_account = bank_account
        self.areacode = areacode
        self.mobile = mobile
        self.verification_code = verification_code

    @property
    def bank_account(self):
        r"""Gets the bank_account of this BankCardInfoV2.

        银行卡账号。 当identifyType为4时，不能为空。 银行账号输入规则：^[0-9a-zA-Z]，可以包含特殊横杠（-）字符。

        :return: The bank_account of this BankCardInfoV2.
        :rtype: str
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        r"""Sets the bank_account of this BankCardInfoV2.

        银行卡账号。 当identifyType为4时，不能为空。 银行账号输入规则：^[0-9a-zA-Z]，可以包含特殊横杠（-）字符。

        :param bank_account: The bank_account of this BankCardInfoV2.
        :type bank_account: str
        """
        self._bank_account = bank_account

    @property
    def areacode(self):
        r"""Gets the areacode of this BankCardInfoV2.

        国家/区号码。 例如：0086：中国大陆区号码。

        :return: The areacode of this BankCardInfoV2.
        :rtype: str
        """
        return self._areacode

    @areacode.setter
    def areacode(self, areacode):
        r"""Sets the areacode of this BankCardInfoV2.

        国家/区号码。 例如：0086：中国大陆区号码。

        :param areacode: The areacode of this BankCardInfoV2.
        :type areacode: str
        """
        self._areacode = areacode

    @property
    def mobile(self):
        r"""Gets the mobile of this BankCardInfoV2.

        手机号码。

        :return: The mobile of this BankCardInfoV2.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        r"""Sets the mobile of this BankCardInfoV2.

        手机号码。

        :param mobile: The mobile of this BankCardInfoV2.
        :type mobile: str
        """
        self._mobile = mobile

    @property
    def verification_code(self):
        r"""Gets the verification_code of this BankCardInfoV2.

        验证码。 请调用“发送验证码”接口获取。

        :return: The verification_code of this BankCardInfoV2.
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        r"""Sets the verification_code of this BankCardInfoV2.

        验证码。 请调用“发送验证码”接口获取。

        :param verification_code: The verification_code of this BankCardInfoV2.
        :type verification_code: str
        """
        self._verification_code = verification_code

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
        if not isinstance(other, BankCardInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
