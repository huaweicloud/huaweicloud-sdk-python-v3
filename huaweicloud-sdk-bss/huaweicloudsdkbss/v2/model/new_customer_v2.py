# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NewCustomerV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_name': 'str',
        'mobile_phone': 'str',
        'use_pri_mobile_phone': 'str',
        'password': 'str',
        'verification_code': 'str'
    }

    attribute_map = {
        'customer_name': 'customer_name',
        'mobile_phone': 'mobile_phone',
        'use_pri_mobile_phone': 'use_pri_mobile_phone',
        'password': 'password',
        'verification_code': 'verification_code'
    }

    def __init__(self, customer_name=None, mobile_phone=None, use_pri_mobile_phone=None, password=None, verification_code=None):
        r"""NewCustomerV2

        The model defined in huaweicloud sdk

        :param customer_name: 企业子账号登录名。
        :type customer_name: str
        :param mobile_phone: 企业管理员的手机号码。如果use_pri_mobile_phone取值为Y，则这个参数无效，否则必选。
        :type mobile_phone: str
        :param use_pri_mobile_phone: 是否使用企业主账号手机号码作为子账号手机号码： Y：是N：否（默认值） 当为Y时，mobile_phone输入无效。
        :type use_pri_mobile_phone: str
        :param password: 企业子账号的登录密码。
        :type password: str
        :param verification_code: 验证码，只有输入企业子账号的手机号的情况下，才需要填写该字段。 具体请参见发送短信验证码。
        :type verification_code: str
        """
        
        

        self._customer_name = None
        self._mobile_phone = None
        self._use_pri_mobile_phone = None
        self._password = None
        self._verification_code = None
        self.discriminator = None

        self.customer_name = customer_name
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if use_pri_mobile_phone is not None:
            self.use_pri_mobile_phone = use_pri_mobile_phone
        self.password = password
        if verification_code is not None:
            self.verification_code = verification_code

    @property
    def customer_name(self):
        r"""Gets the customer_name of this NewCustomerV2.

        企业子账号登录名。

        :return: The customer_name of this NewCustomerV2.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        r"""Sets the customer_name of this NewCustomerV2.

        企业子账号登录名。

        :param customer_name: The customer_name of this NewCustomerV2.
        :type customer_name: str
        """
        self._customer_name = customer_name

    @property
    def mobile_phone(self):
        r"""Gets the mobile_phone of this NewCustomerV2.

        企业管理员的手机号码。如果use_pri_mobile_phone取值为Y，则这个参数无效，否则必选。

        :return: The mobile_phone of this NewCustomerV2.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        r"""Sets the mobile_phone of this NewCustomerV2.

        企业管理员的手机号码。如果use_pri_mobile_phone取值为Y，则这个参数无效，否则必选。

        :param mobile_phone: The mobile_phone of this NewCustomerV2.
        :type mobile_phone: str
        """
        self._mobile_phone = mobile_phone

    @property
    def use_pri_mobile_phone(self):
        r"""Gets the use_pri_mobile_phone of this NewCustomerV2.

        是否使用企业主账号手机号码作为子账号手机号码： Y：是N：否（默认值） 当为Y时，mobile_phone输入无效。

        :return: The use_pri_mobile_phone of this NewCustomerV2.
        :rtype: str
        """
        return self._use_pri_mobile_phone

    @use_pri_mobile_phone.setter
    def use_pri_mobile_phone(self, use_pri_mobile_phone):
        r"""Sets the use_pri_mobile_phone of this NewCustomerV2.

        是否使用企业主账号手机号码作为子账号手机号码： Y：是N：否（默认值） 当为Y时，mobile_phone输入无效。

        :param use_pri_mobile_phone: The use_pri_mobile_phone of this NewCustomerV2.
        :type use_pri_mobile_phone: str
        """
        self._use_pri_mobile_phone = use_pri_mobile_phone

    @property
    def password(self):
        r"""Gets the password of this NewCustomerV2.

        企业子账号的登录密码。

        :return: The password of this NewCustomerV2.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this NewCustomerV2.

        企业子账号的登录密码。

        :param password: The password of this NewCustomerV2.
        :type password: str
        """
        self._password = password

    @property
    def verification_code(self):
        r"""Gets the verification_code of this NewCustomerV2.

        验证码，只有输入企业子账号的手机号的情况下，才需要填写该字段。 具体请参见发送短信验证码。

        :return: The verification_code of this NewCustomerV2.
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        r"""Sets the verification_code of this NewCustomerV2.

        验证码，只有输入企业子账号的手机号的情况下，才需要填写该字段。 具体请参见发送短信验证码。

        :param verification_code: The verification_code of this NewCustomerV2.
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
        if not isinstance(other, NewCustomerV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
