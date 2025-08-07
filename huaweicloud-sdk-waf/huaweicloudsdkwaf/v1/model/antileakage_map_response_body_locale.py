# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntileakageMapResponseBodyLocale:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'id_card': 'str',
        'sensitive': 'str',
        'phone': 'str',
        'response_code': 'str',
        'email': 'str'
    }

    attribute_map = {
        'code': 'code',
        'id_card': 'id_card',
        'sensitive': 'sensitive',
        'phone': 'phone',
        'response_code': 'responseCode',
        'email': 'email'
    }

    def __init__(self, code=None, id_card=None, sensitive=None, phone=None, response_code=None, email=None):
        r"""AntileakageMapResponseBodyLocale

        The model defined in huaweicloud sdk

        :param code: **参数解释：** 响应码拦截，用于捕获和处理特定HTTP响应码的机制 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type code: str
        :param id_card: **参数解释：** 身份证号，用于识别个人身份的唯一编码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id_card: str
        :param sensitive: **参数解释：** 敏感信息过滤，用于检测和处理敏感信息的模块 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sensitive: str
        :param phone: **参数解释：** 电话号码，用于联系的数字编码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type phone: str
        :param response_code: **参数解释：** 选项涉及的各种响应码，示例值400，401,404 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type response_code: str
        :param email: **参数解释：** 电子邮箱，用于电子通信的地址 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type email: str
        """
        
        

        self._code = None
        self._id_card = None
        self._sensitive = None
        self._phone = None
        self._response_code = None
        self._email = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if id_card is not None:
            self.id_card = id_card
        if sensitive is not None:
            self.sensitive = sensitive
        if phone is not None:
            self.phone = phone
        if response_code is not None:
            self.response_code = response_code
        if email is not None:
            self.email = email

    @property
    def code(self):
        r"""Gets the code of this AntileakageMapResponseBodyLocale.

        **参数解释：** 响应码拦截，用于捕获和处理特定HTTP响应码的机制 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The code of this AntileakageMapResponseBodyLocale.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this AntileakageMapResponseBodyLocale.

        **参数解释：** 响应码拦截，用于捕获和处理特定HTTP响应码的机制 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param code: The code of this AntileakageMapResponseBodyLocale.
        :type code: str
        """
        self._code = code

    @property
    def id_card(self):
        r"""Gets the id_card of this AntileakageMapResponseBodyLocale.

        **参数解释：** 身份证号，用于识别个人身份的唯一编码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id_card of this AntileakageMapResponseBodyLocale.
        :rtype: str
        """
        return self._id_card

    @id_card.setter
    def id_card(self, id_card):
        r"""Sets the id_card of this AntileakageMapResponseBodyLocale.

        **参数解释：** 身份证号，用于识别个人身份的唯一编码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id_card: The id_card of this AntileakageMapResponseBodyLocale.
        :type id_card: str
        """
        self._id_card = id_card

    @property
    def sensitive(self):
        r"""Gets the sensitive of this AntileakageMapResponseBodyLocale.

        **参数解释：** 敏感信息过滤，用于检测和处理敏感信息的模块 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sensitive of this AntileakageMapResponseBodyLocale.
        :rtype: str
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        r"""Sets the sensitive of this AntileakageMapResponseBodyLocale.

        **参数解释：** 敏感信息过滤，用于检测和处理敏感信息的模块 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sensitive: The sensitive of this AntileakageMapResponseBodyLocale.
        :type sensitive: str
        """
        self._sensitive = sensitive

    @property
    def phone(self):
        r"""Gets the phone of this AntileakageMapResponseBodyLocale.

        **参数解释：** 电话号码，用于联系的数字编码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The phone of this AntileakageMapResponseBodyLocale.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this AntileakageMapResponseBodyLocale.

        **参数解释：** 电话号码，用于联系的数字编码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param phone: The phone of this AntileakageMapResponseBodyLocale.
        :type phone: str
        """
        self._phone = phone

    @property
    def response_code(self):
        r"""Gets the response_code of this AntileakageMapResponseBodyLocale.

        **参数解释：** 选项涉及的各种响应码，示例值400，401,404 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The response_code of this AntileakageMapResponseBodyLocale.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        r"""Sets the response_code of this AntileakageMapResponseBodyLocale.

        **参数解释：** 选项涉及的各种响应码，示例值400，401,404 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param response_code: The response_code of this AntileakageMapResponseBodyLocale.
        :type response_code: str
        """
        self._response_code = response_code

    @property
    def email(self):
        r"""Gets the email of this AntileakageMapResponseBodyLocale.

        **参数解释：** 电子邮箱，用于电子通信的地址 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The email of this AntileakageMapResponseBodyLocale.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this AntileakageMapResponseBodyLocale.

        **参数解释：** 电子邮箱，用于电子通信的地址 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param email: The email of this AntileakageMapResponseBodyLocale.
        :type email: str
        """
        self._email = email

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
        if not isinstance(other, AntileakageMapResponseBodyLocale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
