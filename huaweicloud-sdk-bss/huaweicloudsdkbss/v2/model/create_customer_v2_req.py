# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCustomerV2Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'mobile_phone': 'str',
        'verification_code': 'str',
        'xaccount_id': 'str',
        'xaccount_type': 'str',
        'password': 'str',
        'is_close_market_ms': 'str',
        'cooperation_type': 'str',
        'indirect_partner_id': 'str',
        'include_association_result': 'bool'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'mobile_phone': 'mobile_phone',
        'verification_code': 'verification_code',
        'xaccount_id': 'xaccount_id',
        'xaccount_type': 'xaccount_type',
        'password': 'password',
        'is_close_market_ms': 'is_close_market_ms',
        'cooperation_type': 'cooperation_type',
        'indirect_partner_id': 'indirect_partner_id',
        'include_association_result': 'include_association_result'
    }

    def __init__(self, domain_name=None, mobile_phone=None, verification_code=None, xaccount_id=None, xaccount_type=None, password=None, is_close_market_ms=None, cooperation_type=None, indirect_partner_id=None, include_association_result=None):
        r"""CreateCustomerV2Req

        The model defined in huaweicloud sdk

        :param domain_name: 客户的华为云账号名。 如果为空，随机生成。 不能以“op_”或“shadow_”开头且不能全为数字。 校验长度（5到32位）和规则^([a-zA-Z_-]([a-zA-Z0-9_-])*)$。 此参数不携带或携带值为空串或携带值为null时，随机生成。
        :type domain_name: str
        :param mobile_phone: 手机号。 目前系统只支持中国的手机号。 示例：13XXXXXXXXX 此参数不携带或携带值为null时，不被赋值；携带值为空串时，赋值为空串。
        :type mobile_phone: str
        :param verification_code: 验证码。 请调用“发送验证码”接口获取。 如果手机号不存在，则不需要输入验证码。 此参数不携带或携带值为null时，不做处理；不支持携带值为空串。
        :type verification_code: str
        :param xaccount_id: 伙伴销售平台的用户唯一标识，该标识的具体值由伙伴分配。
        :type xaccount_id: str
        :param xaccount_type: 华为分给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。
        :type xaccount_type: str
        :param password: 密码规则如下： 至少包含以下四种字符中的两种： 大写字母、小写字母、数字、特殊字符；不能和账号名或倒序的账号名相同；不能包含手机号。 如果为空，用户没有密码，则不能直接在华为云登录，只能通过伙伴系统SSO方式跳转到华为云。 此参数不携带或携带值为null时，密码随机生成；不支持携带值为空串。
        :type password: str
        :param is_close_market_ms: 是否关闭营销消息的发送。 true：关闭false：不关闭（默认） 此参数不携带或携带值为空串或携带值为null时，赋值为false。
        :type is_close_market_ms: str
        :param cooperation_type: 合作类型。 1：顾问销售。 不传递或传递非1的值，默认会创建成代售模式的客户。
        :type cooperation_type: str
        :param indirect_partner_id: 云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。 如果需要创建云经销商的子客户，必须携带该字段。除此之外，此参数不做处理。
        :type indirect_partner_id: str
        :param include_association_result: 是否返回子客户的关联结果。 true：返回子客户和伙伴的关联结果false：不返回子客户和伙伴的关联结果 默认值为false。 此参数不携带或携带值为空串或携带值为null时，赋值为false。
        :type include_association_result: bool
        """
        
        

        self._domain_name = None
        self._mobile_phone = None
        self._verification_code = None
        self._xaccount_id = None
        self._xaccount_type = None
        self._password = None
        self._is_close_market_ms = None
        self._cooperation_type = None
        self._indirect_partner_id = None
        self._include_association_result = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if verification_code is not None:
            self.verification_code = verification_code
        self.xaccount_id = xaccount_id
        self.xaccount_type = xaccount_type
        if password is not None:
            self.password = password
        if is_close_market_ms is not None:
            self.is_close_market_ms = is_close_market_ms
        if cooperation_type is not None:
            self.cooperation_type = cooperation_type
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if include_association_result is not None:
            self.include_association_result = include_association_result

    @property
    def domain_name(self):
        r"""Gets the domain_name of this CreateCustomerV2Req.

        客户的华为云账号名。 如果为空，随机生成。 不能以“op_”或“shadow_”开头且不能全为数字。 校验长度（5到32位）和规则^([a-zA-Z_-]([a-zA-Z0-9_-])*)$。 此参数不携带或携带值为空串或携带值为null时，随机生成。

        :return: The domain_name of this CreateCustomerV2Req.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this CreateCustomerV2Req.

        客户的华为云账号名。 如果为空，随机生成。 不能以“op_”或“shadow_”开头且不能全为数字。 校验长度（5到32位）和规则^([a-zA-Z_-]([a-zA-Z0-9_-])*)$。 此参数不携带或携带值为空串或携带值为null时，随机生成。

        :param domain_name: The domain_name of this CreateCustomerV2Req.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def mobile_phone(self):
        r"""Gets the mobile_phone of this CreateCustomerV2Req.

        手机号。 目前系统只支持中国的手机号。 示例：13XXXXXXXXX 此参数不携带或携带值为null时，不被赋值；携带值为空串时，赋值为空串。

        :return: The mobile_phone of this CreateCustomerV2Req.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        r"""Sets the mobile_phone of this CreateCustomerV2Req.

        手机号。 目前系统只支持中国的手机号。 示例：13XXXXXXXXX 此参数不携带或携带值为null时，不被赋值；携带值为空串时，赋值为空串。

        :param mobile_phone: The mobile_phone of this CreateCustomerV2Req.
        :type mobile_phone: str
        """
        self._mobile_phone = mobile_phone

    @property
    def verification_code(self):
        r"""Gets the verification_code of this CreateCustomerV2Req.

        验证码。 请调用“发送验证码”接口获取。 如果手机号不存在，则不需要输入验证码。 此参数不携带或携带值为null时，不做处理；不支持携带值为空串。

        :return: The verification_code of this CreateCustomerV2Req.
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        r"""Sets the verification_code of this CreateCustomerV2Req.

        验证码。 请调用“发送验证码”接口获取。 如果手机号不存在，则不需要输入验证码。 此参数不携带或携带值为null时，不做处理；不支持携带值为空串。

        :param verification_code: The verification_code of this CreateCustomerV2Req.
        :type verification_code: str
        """
        self._verification_code = verification_code

    @property
    def xaccount_id(self):
        r"""Gets the xaccount_id of this CreateCustomerV2Req.

        伙伴销售平台的用户唯一标识，该标识的具体值由伙伴分配。

        :return: The xaccount_id of this CreateCustomerV2Req.
        :rtype: str
        """
        return self._xaccount_id

    @xaccount_id.setter
    def xaccount_id(self, xaccount_id):
        r"""Sets the xaccount_id of this CreateCustomerV2Req.

        伙伴销售平台的用户唯一标识，该标识的具体值由伙伴分配。

        :param xaccount_id: The xaccount_id of this CreateCustomerV2Req.
        :type xaccount_id: str
        """
        self._xaccount_id = xaccount_id

    @property
    def xaccount_type(self):
        r"""Gets the xaccount_type of this CreateCustomerV2Req.

        华为分给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。

        :return: The xaccount_type of this CreateCustomerV2Req.
        :rtype: str
        """
        return self._xaccount_type

    @xaccount_type.setter
    def xaccount_type(self, xaccount_type):
        r"""Sets the xaccount_type of this CreateCustomerV2Req.

        华为分给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。

        :param xaccount_type: The xaccount_type of this CreateCustomerV2Req.
        :type xaccount_type: str
        """
        self._xaccount_type = xaccount_type

    @property
    def password(self):
        r"""Gets the password of this CreateCustomerV2Req.

        密码规则如下： 至少包含以下四种字符中的两种： 大写字母、小写字母、数字、特殊字符；不能和账号名或倒序的账号名相同；不能包含手机号。 如果为空，用户没有密码，则不能直接在华为云登录，只能通过伙伴系统SSO方式跳转到华为云。 此参数不携带或携带值为null时，密码随机生成；不支持携带值为空串。

        :return: The password of this CreateCustomerV2Req.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this CreateCustomerV2Req.

        密码规则如下： 至少包含以下四种字符中的两种： 大写字母、小写字母、数字、特殊字符；不能和账号名或倒序的账号名相同；不能包含手机号。 如果为空，用户没有密码，则不能直接在华为云登录，只能通过伙伴系统SSO方式跳转到华为云。 此参数不携带或携带值为null时，密码随机生成；不支持携带值为空串。

        :param password: The password of this CreateCustomerV2Req.
        :type password: str
        """
        self._password = password

    @property
    def is_close_market_ms(self):
        r"""Gets the is_close_market_ms of this CreateCustomerV2Req.

        是否关闭营销消息的发送。 true：关闭false：不关闭（默认） 此参数不携带或携带值为空串或携带值为null时，赋值为false。

        :return: The is_close_market_ms of this CreateCustomerV2Req.
        :rtype: str
        """
        return self._is_close_market_ms

    @is_close_market_ms.setter
    def is_close_market_ms(self, is_close_market_ms):
        r"""Sets the is_close_market_ms of this CreateCustomerV2Req.

        是否关闭营销消息的发送。 true：关闭false：不关闭（默认） 此参数不携带或携带值为空串或携带值为null时，赋值为false。

        :param is_close_market_ms: The is_close_market_ms of this CreateCustomerV2Req.
        :type is_close_market_ms: str
        """
        self._is_close_market_ms = is_close_market_ms

    @property
    def cooperation_type(self):
        r"""Gets the cooperation_type of this CreateCustomerV2Req.

        合作类型。 1：顾问销售。 不传递或传递非1的值，默认会创建成代售模式的客户。

        :return: The cooperation_type of this CreateCustomerV2Req.
        :rtype: str
        """
        return self._cooperation_type

    @cooperation_type.setter
    def cooperation_type(self, cooperation_type):
        r"""Sets the cooperation_type of this CreateCustomerV2Req.

        合作类型。 1：顾问销售。 不传递或传递非1的值，默认会创建成代售模式的客户。

        :param cooperation_type: The cooperation_type of this CreateCustomerV2Req.
        :type cooperation_type: str
        """
        self._cooperation_type = cooperation_type

    @property
    def indirect_partner_id(self):
        r"""Gets the indirect_partner_id of this CreateCustomerV2Req.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。 如果需要创建云经销商的子客户，必须携带该字段。除此之外，此参数不做处理。

        :return: The indirect_partner_id of this CreateCustomerV2Req.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        r"""Sets the indirect_partner_id of this CreateCustomerV2Req.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。 如果需要创建云经销商的子客户，必须携带该字段。除此之外，此参数不做处理。

        :param indirect_partner_id: The indirect_partner_id of this CreateCustomerV2Req.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def include_association_result(self):
        r"""Gets the include_association_result of this CreateCustomerV2Req.

        是否返回子客户的关联结果。 true：返回子客户和伙伴的关联结果false：不返回子客户和伙伴的关联结果 默认值为false。 此参数不携带或携带值为空串或携带值为null时，赋值为false。

        :return: The include_association_result of this CreateCustomerV2Req.
        :rtype: bool
        """
        return self._include_association_result

    @include_association_result.setter
    def include_association_result(self, include_association_result):
        r"""Sets the include_association_result of this CreateCustomerV2Req.

        是否返回子客户的关联结果。 true：返回子客户和伙伴的关联结果false：不返回子客户和伙伴的关联结果 默认值为false。 此参数不携带或携带值为空串或携带值为null时，赋值为false。

        :param include_association_result: The include_association_result of this CreateCustomerV2Req.
        :type include_association_result: bool
        """
        self._include_association_result = include_association_result

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
        if not isinstance(other, CreateCustomerV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
