# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalContactBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'other_number': 'str',
        'other_number_country': 'str',
        'country': 'str',
        'phone': 'str',
        'email': 'str',
        'corp_name': 'str',
        'dept_name': 'str',
        'position': 'str',
        'address': 'str',
        'remarks': 'str'
    }

    attribute_map = {
        'other_number': 'otherNumber',
        'other_number_country': 'otherNumberCountry',
        'country': 'country',
        'phone': 'phone',
        'email': 'email',
        'corp_name': 'corpName',
        'dept_name': 'deptName',
        'position': 'position',
        'address': 'address',
        'remarks': 'remarks'
    }

    def __init__(self, other_number=None, other_number_country=None, country=None, phone=None, email=None, corp_name=None, dept_name=None, position=None, address=None, remarks=None):
        r"""ExternalContactBase

        The model defined in huaweicloud sdk

        :param other_number: 其他号码。 &gt; * 其他号码必须以国家码作为前缀 &gt; * otherNumber填写时，otherNumberCountry也必须填写 &gt; * 如果要清空手机号配置，则otherNumberCountry和otherNumber都要置为\&quot;\&quot; 
        :type other_number: str
        :param other_number_country: [[其他号码所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type other_number_country: str
        :param country: [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type country: str
        :param phone: 手机号。 &gt; * 手机号必须以国家码作为前缀 &gt; * phone填写时，country也必须填写 &gt; * 如果要清空手机号配置，则country和phone都要置为\&quot;\&quot; 
        :type phone: str
        :param email: 邮箱。
        :type email: str
        :param corp_name: 公司名称。
        :type corp_name: str
        :param dept_name: 部门。
        :type dept_name: str
        :param position: 职务。
        :type position: str
        :param address: 个人地址。
        :type address: str
        :param remarks: 备注。
        :type remarks: str
        """
        
        

        self._other_number = None
        self._other_number_country = None
        self._country = None
        self._phone = None
        self._email = None
        self._corp_name = None
        self._dept_name = None
        self._position = None
        self._address = None
        self._remarks = None
        self.discriminator = None

        if other_number is not None:
            self.other_number = other_number
        if other_number_country is not None:
            self.other_number_country = other_number_country
        if country is not None:
            self.country = country
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        if corp_name is not None:
            self.corp_name = corp_name
        if dept_name is not None:
            self.dept_name = dept_name
        if position is not None:
            self.position = position
        if address is not None:
            self.address = address
        if remarks is not None:
            self.remarks = remarks

    @property
    def other_number(self):
        r"""Gets the other_number of this ExternalContactBase.

        其他号码。 > * 其他号码必须以国家码作为前缀 > * otherNumber填写时，otherNumberCountry也必须填写 > * 如果要清空手机号配置，则otherNumberCountry和otherNumber都要置为\"\" 

        :return: The other_number of this ExternalContactBase.
        :rtype: str
        """
        return self._other_number

    @other_number.setter
    def other_number(self, other_number):
        r"""Sets the other_number of this ExternalContactBase.

        其他号码。 > * 其他号码必须以国家码作为前缀 > * otherNumber填写时，otherNumberCountry也必须填写 > * 如果要清空手机号配置，则otherNumberCountry和otherNumber都要置为\"\" 

        :param other_number: The other_number of this ExternalContactBase.
        :type other_number: str
        """
        self._other_number = other_number

    @property
    def other_number_country(self):
        r"""Gets the other_number_country of this ExternalContactBase.

        [[其他号码所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The other_number_country of this ExternalContactBase.
        :rtype: str
        """
        return self._other_number_country

    @other_number_country.setter
    def other_number_country(self, other_number_country):
        r"""Sets the other_number_country of this ExternalContactBase.

        [[其他号码所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param other_number_country: The other_number_country of this ExternalContactBase.
        :type other_number_country: str
        """
        self._other_number_country = other_number_country

    @property
    def country(self):
        r"""Gets the country of this ExternalContactBase.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The country of this ExternalContactBase.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this ExternalContactBase.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param country: The country of this ExternalContactBase.
        :type country: str
        """
        self._country = country

    @property
    def phone(self):
        r"""Gets the phone of this ExternalContactBase.

        手机号。 > * 手机号必须以国家码作为前缀 > * phone填写时，country也必须填写 > * 如果要清空手机号配置，则country和phone都要置为\"\" 

        :return: The phone of this ExternalContactBase.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this ExternalContactBase.

        手机号。 > * 手机号必须以国家码作为前缀 > * phone填写时，country也必须填写 > * 如果要清空手机号配置，则country和phone都要置为\"\" 

        :param phone: The phone of this ExternalContactBase.
        :type phone: str
        """
        self._phone = phone

    @property
    def email(self):
        r"""Gets the email of this ExternalContactBase.

        邮箱。

        :return: The email of this ExternalContactBase.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ExternalContactBase.

        邮箱。

        :param email: The email of this ExternalContactBase.
        :type email: str
        """
        self._email = email

    @property
    def corp_name(self):
        r"""Gets the corp_name of this ExternalContactBase.

        公司名称。

        :return: The corp_name of this ExternalContactBase.
        :rtype: str
        """
        return self._corp_name

    @corp_name.setter
    def corp_name(self, corp_name):
        r"""Sets the corp_name of this ExternalContactBase.

        公司名称。

        :param corp_name: The corp_name of this ExternalContactBase.
        :type corp_name: str
        """
        self._corp_name = corp_name

    @property
    def dept_name(self):
        r"""Gets the dept_name of this ExternalContactBase.

        部门。

        :return: The dept_name of this ExternalContactBase.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        r"""Sets the dept_name of this ExternalContactBase.

        部门。

        :param dept_name: The dept_name of this ExternalContactBase.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def position(self):
        r"""Gets the position of this ExternalContactBase.

        职务。

        :return: The position of this ExternalContactBase.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this ExternalContactBase.

        职务。

        :param position: The position of this ExternalContactBase.
        :type position: str
        """
        self._position = position

    @property
    def address(self):
        r"""Gets the address of this ExternalContactBase.

        个人地址。

        :return: The address of this ExternalContactBase.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this ExternalContactBase.

        个人地址。

        :param address: The address of this ExternalContactBase.
        :type address: str
        """
        self._address = address

    @property
    def remarks(self):
        r"""Gets the remarks of this ExternalContactBase.

        备注。

        :return: The remarks of this ExternalContactBase.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this ExternalContactBase.

        备注。

        :param remarks: The remarks of this ExternalContactBase.
        :type remarks: str
        """
        self._remarks = remarks

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
        if not isinstance(other, ExternalContactBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
