# coding: utf-8

import pprint
import re

import six





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
        """NewCustomerV2 - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the customer_name of this NewCustomerV2.

        |参数名称：客户主账号登录名。| |参数约束及描述：客户主账号登录名。|

        :return: The customer_name of this NewCustomerV2.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this NewCustomerV2.

        |参数名称：客户主账号登录名。| |参数约束及描述：客户主账号登录名。|

        :param customer_name: The customer_name of this NewCustomerV2.
        :type: str
        """
        self._customer_name = customer_name

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this NewCustomerV2.

        |参数名称：管理员手机号码。如果usePriMobilePhone为Y，则这个参数无效，否则必选。| |参数约束及描述：管理员手机号码。如果usePriMobilePhone为Y，则这个参数无效，否则必选。|

        :return: The mobile_phone of this NewCustomerV2.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this NewCustomerV2.

        |参数名称：管理员手机号码。如果usePriMobilePhone为Y，则这个参数无效，否则必选。| |参数约束及描述：管理员手机号码。如果usePriMobilePhone为Y，则这个参数无效，否则必选。|

        :param mobile_phone: The mobile_phone of this NewCustomerV2.
        :type: str
        """
        self._mobile_phone = mobile_phone

    @property
    def use_pri_mobile_phone(self):
        """Gets the use_pri_mobile_phone of this NewCustomerV2.

        |参数名称：是否使用企业主账号手机号码作为子账号手机号码：Y：是；N：否（默认值）。注：当为Y时，mobilePhone输入无效。| |参数约束及描述：是否使用企业主账号手机号码作为子账号手机号码：Y：是；N：否（默认值）。注：当为Y时，mobilePhone输入无效。|

        :return: The use_pri_mobile_phone of this NewCustomerV2.
        :rtype: str
        """
        return self._use_pri_mobile_phone

    @use_pri_mobile_phone.setter
    def use_pri_mobile_phone(self, use_pri_mobile_phone):
        """Sets the use_pri_mobile_phone of this NewCustomerV2.

        |参数名称：是否使用企业主账号手机号码作为子账号手机号码：Y：是；N：否（默认值）。注：当为Y时，mobilePhone输入无效。| |参数约束及描述：是否使用企业主账号手机号码作为子账号手机号码：Y：是；N：否（默认值）。注：当为Y时，mobilePhone输入无效。|

        :param use_pri_mobile_phone: The use_pri_mobile_phone of this NewCustomerV2.
        :type: str
        """
        self._use_pri_mobile_phone = use_pri_mobile_phone

    @property
    def password(self):
        """Gets the password of this NewCustomerV2.

        |参数名称：客户登录密码。注：usePriMobilePhone为Y时才支持| |参数约束及描述：客户登录密码。注：usePriMobilePhone为Y时才支持|

        :return: The password of this NewCustomerV2.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this NewCustomerV2.

        |参数名称：客户登录密码。注：usePriMobilePhone为Y时才支持| |参数约束及描述：客户登录密码。注：usePriMobilePhone为Y时才支持|

        :param password: The password of this NewCustomerV2.
        :type: str
        """
        self._password = password

    @property
    def verification_code(self):
        """Gets the verification_code of this NewCustomerV2.

        |参数名称：验证码，只有输入企业子客户的手机号邮箱的情况下，才需要填写该字段| |参数约束及描述：验证码，只有输入企业子客户的手机号邮箱的情况下，才需要填写该字段|

        :return: The verification_code of this NewCustomerV2.
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """Sets the verification_code of this NewCustomerV2.

        |参数名称：验证码，只有输入企业子客户的手机号邮箱的情况下，才需要填写该字段| |参数约束及描述：验证码，只有输入企业子客户的手机号邮箱的情况下，才需要填写该字段|

        :param verification_code: The verification_code of this NewCustomerV2.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewCustomerV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
