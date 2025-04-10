# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertificateResponseBodyApplicationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'country': 'str',
        'company_name': 'str',
        'company_province': 'str',
        'company_city': 'str',
        'applicant_name': 'str',
        'applicant_phone': 'str',
        'applicant_email': 'str',
        'contact_name': 'str',
        'contact_phone': 'str',
        'contact_email': 'str'
    }

    attribute_map = {
        'country': 'country',
        'company_name': 'company_name',
        'company_province': 'company_province',
        'company_city': 'company_city',
        'applicant_name': 'applicant_name',
        'applicant_phone': 'applicant_phone',
        'applicant_email': 'applicant_email',
        'contact_name': 'contact_name',
        'contact_phone': 'contact_phone',
        'contact_email': 'contact_email'
    }

    def __init__(self, country=None, company_name=None, company_province=None, company_city=None, applicant_name=None, applicant_phone=None, applicant_email=None, contact_name=None, contact_phone=None, contact_email=None):
        r"""ShowCertificateResponseBodyApplicationInfo

        The model defined in huaweicloud sdk

        :param country: 国家。
        :type country: str
        :param company_name: 公司名称。
        :type company_name: str
        :param company_province: 公司省份。
        :type company_province: str
        :param company_city: 公司所在城市。
        :type company_city: str
        :param applicant_name: 申请人名称。
        :type applicant_name: str
        :param applicant_phone: 申请人电话。
        :type applicant_phone: str
        :param applicant_email: 申请人邮箱。
        :type applicant_email: str
        :param contact_name: 技术联系人名称。
        :type contact_name: str
        :param contact_phone: 技术联系人电话。
        :type contact_phone: str
        :param contact_email: 技术联系人邮箱。
        :type contact_email: str
        """
        
        

        self._country = None
        self._company_name = None
        self._company_province = None
        self._company_city = None
        self._applicant_name = None
        self._applicant_phone = None
        self._applicant_email = None
        self._contact_name = None
        self._contact_phone = None
        self._contact_email = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if company_name is not None:
            self.company_name = company_name
        if company_province is not None:
            self.company_province = company_province
        if company_city is not None:
            self.company_city = company_city
        if applicant_name is not None:
            self.applicant_name = applicant_name
        if applicant_phone is not None:
            self.applicant_phone = applicant_phone
        if applicant_email is not None:
            self.applicant_email = applicant_email
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_phone is not None:
            self.contact_phone = contact_phone
        if contact_email is not None:
            self.contact_email = contact_email

    @property
    def country(self):
        r"""Gets the country of this ShowCertificateResponseBodyApplicationInfo.

        国家。

        :return: The country of this ShowCertificateResponseBodyApplicationInfo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this ShowCertificateResponseBodyApplicationInfo.

        国家。

        :param country: The country of this ShowCertificateResponseBodyApplicationInfo.
        :type country: str
        """
        self._country = country

    @property
    def company_name(self):
        r"""Gets the company_name of this ShowCertificateResponseBodyApplicationInfo.

        公司名称。

        :return: The company_name of this ShowCertificateResponseBodyApplicationInfo.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        r"""Sets the company_name of this ShowCertificateResponseBodyApplicationInfo.

        公司名称。

        :param company_name: The company_name of this ShowCertificateResponseBodyApplicationInfo.
        :type company_name: str
        """
        self._company_name = company_name

    @property
    def company_province(self):
        r"""Gets the company_province of this ShowCertificateResponseBodyApplicationInfo.

        公司省份。

        :return: The company_province of this ShowCertificateResponseBodyApplicationInfo.
        :rtype: str
        """
        return self._company_province

    @company_province.setter
    def company_province(self, company_province):
        r"""Sets the company_province of this ShowCertificateResponseBodyApplicationInfo.

        公司省份。

        :param company_province: The company_province of this ShowCertificateResponseBodyApplicationInfo.
        :type company_province: str
        """
        self._company_province = company_province

    @property
    def company_city(self):
        r"""Gets the company_city of this ShowCertificateResponseBodyApplicationInfo.

        公司所在城市。

        :return: The company_city of this ShowCertificateResponseBodyApplicationInfo.
        :rtype: str
        """
        return self._company_city

    @company_city.setter
    def company_city(self, company_city):
        r"""Sets the company_city of this ShowCertificateResponseBodyApplicationInfo.

        公司所在城市。

        :param company_city: The company_city of this ShowCertificateResponseBodyApplicationInfo.
        :type company_city: str
        """
        self._company_city = company_city

    @property
    def applicant_name(self):
        r"""Gets the applicant_name of this ShowCertificateResponseBodyApplicationInfo.

        申请人名称。

        :return: The applicant_name of this ShowCertificateResponseBodyApplicationInfo.
        :rtype: str
        """
        return self._applicant_name

    @applicant_name.setter
    def applicant_name(self, applicant_name):
        r"""Sets the applicant_name of this ShowCertificateResponseBodyApplicationInfo.

        申请人名称。

        :param applicant_name: The applicant_name of this ShowCertificateResponseBodyApplicationInfo.
        :type applicant_name: str
        """
        self._applicant_name = applicant_name

    @property
    def applicant_phone(self):
        r"""Gets the applicant_phone of this ShowCertificateResponseBodyApplicationInfo.

        申请人电话。

        :return: The applicant_phone of this ShowCertificateResponseBodyApplicationInfo.
        :rtype: str
        """
        return self._applicant_phone

    @applicant_phone.setter
    def applicant_phone(self, applicant_phone):
        r"""Sets the applicant_phone of this ShowCertificateResponseBodyApplicationInfo.

        申请人电话。

        :param applicant_phone: The applicant_phone of this ShowCertificateResponseBodyApplicationInfo.
        :type applicant_phone: str
        """
        self._applicant_phone = applicant_phone

    @property
    def applicant_email(self):
        r"""Gets the applicant_email of this ShowCertificateResponseBodyApplicationInfo.

        申请人邮箱。

        :return: The applicant_email of this ShowCertificateResponseBodyApplicationInfo.
        :rtype: str
        """
        return self._applicant_email

    @applicant_email.setter
    def applicant_email(self, applicant_email):
        r"""Sets the applicant_email of this ShowCertificateResponseBodyApplicationInfo.

        申请人邮箱。

        :param applicant_email: The applicant_email of this ShowCertificateResponseBodyApplicationInfo.
        :type applicant_email: str
        """
        self._applicant_email = applicant_email

    @property
    def contact_name(self):
        r"""Gets the contact_name of this ShowCertificateResponseBodyApplicationInfo.

        技术联系人名称。

        :return: The contact_name of this ShowCertificateResponseBodyApplicationInfo.
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        r"""Sets the contact_name of this ShowCertificateResponseBodyApplicationInfo.

        技术联系人名称。

        :param contact_name: The contact_name of this ShowCertificateResponseBodyApplicationInfo.
        :type contact_name: str
        """
        self._contact_name = contact_name

    @property
    def contact_phone(self):
        r"""Gets the contact_phone of this ShowCertificateResponseBodyApplicationInfo.

        技术联系人电话。

        :return: The contact_phone of this ShowCertificateResponseBodyApplicationInfo.
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        r"""Sets the contact_phone of this ShowCertificateResponseBodyApplicationInfo.

        技术联系人电话。

        :param contact_phone: The contact_phone of this ShowCertificateResponseBodyApplicationInfo.
        :type contact_phone: str
        """
        self._contact_phone = contact_phone

    @property
    def contact_email(self):
        r"""Gets the contact_email of this ShowCertificateResponseBodyApplicationInfo.

        技术联系人邮箱。

        :return: The contact_email of this ShowCertificateResponseBodyApplicationInfo.
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        r"""Sets the contact_email of this ShowCertificateResponseBodyApplicationInfo.

        技术联系人邮箱。

        :param contact_email: The contact_email of this ShowCertificateResponseBodyApplicationInfo.
        :type contact_email: str
        """
        self._contact_email = contact_email

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
        if not isinstance(other, ShowCertificateResponseBodyApplicationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
