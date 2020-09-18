# coding: utf-8

import pprint
import re

import six





class ChangeEnterpriseRealnameAuthsReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'identify_type': 'int',
        'certificate_type': 'int',
        'verified_file_url': 'list[str]',
        'corp_name': 'str',
        'verified_number': 'str',
        'reg_country': 'str',
        'reg_address': 'str',
        'change_type': 'int',
        'xaccount_type': 'str',
        'enterprise_person': 'EnterprisePersonNew'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'identify_type': 'identify_type',
        'certificate_type': 'certificate_type',
        'verified_file_url': 'verified_file_url',
        'corp_name': 'corp_name',
        'verified_number': 'verified_number',
        'reg_country': 'reg_country',
        'reg_address': 'reg_address',
        'change_type': 'change_type',
        'xaccount_type': 'xaccount_type',
        'enterprise_person': 'enterprise_person'
    }

    def __init__(self, customer_id=None, identify_type=None, certificate_type=None, verified_file_url=None, corp_name=None, verified_number=None, reg_country=None, reg_address=None, change_type=None, xaccount_type=None, enterprise_person=None):
        """ChangeEnterpriseRealnameAuthsReq - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._identify_type = None
        self._certificate_type = None
        self._verified_file_url = None
        self._corp_name = None
        self._verified_number = None
        self._reg_country = None
        self._reg_address = None
        self._change_type = None
        self._xaccount_type = None
        self._enterprise_person = None
        self.discriminator = None

        self.customer_id = customer_id
        self.identify_type = identify_type
        if certificate_type is not None:
            self.certificate_type = certificate_type
        self.verified_file_url = verified_file_url
        self.corp_name = corp_name
        self.verified_number = verified_number
        if reg_country is not None:
            self.reg_country = reg_country
        if reg_address is not None:
            self.reg_address = reg_address
        self.change_type = change_type
        self.xaccount_type = xaccount_type
        if enterprise_person is not None:
            self.enterprise_person = enterprise_person

    @property
    def customer_id(self):
        """Gets the customer_id of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :return: The customer_id of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :param customer_id: The customer_id of this ChangeEnterpriseRealnameAuthsReq.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def identify_type(self):
        """Gets the identify_type of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：认证方案。1：企业证件扫描| |参数的约束及描述：认证方案。1：企业证件扫描|

        :return: The identify_type of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: int
        """
        return self._identify_type

    @identify_type.setter
    def identify_type(self, identify_type):
        """Sets the identify_type of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：认证方案。1：企业证件扫描| |参数的约束及描述：认证方案。1：企业证件扫描|

        :param identify_type: The identify_type of this ChangeEnterpriseRealnameAuthsReq.
        :type: int
        """
        self._identify_type = identify_type

    @property
    def certificate_type(self):
        """Gets the certificate_type of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：企业证件类型：0：企业营业执照1：事业单位法人证书2：社会团体法人登记证书3：行政执法主体资格证4：组织机构代码证99：其他| |参数的约束及描述：企业证件类型：0：企业营业执照1：事业单位法人证书2：社会团体法人登记证书3：行政执法主体资格证4：组织机构代码证99：其他|

        :return: The certificate_type of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：企业证件类型：0：企业营业执照1：事业单位法人证书2：社会团体法人登记证书3：行政执法主体资格证4：组织机构代码证99：其他| |参数的约束及描述：企业证件类型：0：企业营业执照1：事业单位法人证书2：社会团体法人登记证书3：行政执法主体资格证4：组织机构代码证99：其他|

        :param certificate_type: The certificate_type of this ChangeEnterpriseRealnameAuthsReq.
        :type: int
        """
        self._certificate_type = certificate_type

    @property
    def verified_file_url(self):
        """Gets the verified_file_url of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：企业证件认证时证件附件的文件URL。

        :return: The verified_file_url of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: list[str]
        """
        return self._verified_file_url

    @verified_file_url.setter
    def verified_file_url(self, verified_file_url):
        """Sets the verified_file_url of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：企业证件认证时证件附件的文件URL。

        :param verified_file_url: The verified_file_url of this ChangeEnterpriseRealnameAuthsReq.
        :type: list[str]
        """
        self._verified_file_url = verified_file_url

    @property
    def corp_name(self):
        """Gets the corp_name of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：单位名称。不能全是数字、特殊字符、空格。| |参数约束及描述：单位名称。不能全是数字、特殊字符、空格。|

        :return: The corp_name of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._corp_name

    @corp_name.setter
    def corp_name(self, corp_name):
        """Sets the corp_name of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：单位名称。不能全是数字、特殊字符、空格。| |参数约束及描述：单位名称。不能全是数字、特殊字符、空格。|

        :param corp_name: The corp_name of this ChangeEnterpriseRealnameAuthsReq.
        :type: str
        """
        self._corp_name = corp_name

    @property
    def verified_number(self):
        """Gets the verified_number of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：单位证件号码。| |参数约束及描述：单位证件号码。|

        :return: The verified_number of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._verified_number

    @verified_number.setter
    def verified_number(self, verified_number):
        """Sets the verified_number of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：单位证件号码。| |参数约束及描述：单位证件号码。|

        :param verified_number: The verified_number of this ChangeEnterpriseRealnameAuthsReq.
        :type: str
        """
        self._verified_number = verified_number

    @property
    def reg_country(self):
        """Gets the reg_country of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：实名认证填写的注册国家。国家的两位字母简码。例如：注册国家为“中国”请填写“CN”。| |参数约束及描述：实名认证填写的注册国家。国家的两位字母简码。例如：注册国家为“中国”请填写“CN”。|

        :return: The reg_country of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._reg_country

    @reg_country.setter
    def reg_country(self, reg_country):
        """Sets the reg_country of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：实名认证填写的注册国家。国家的两位字母简码。例如：注册国家为“中国”请填写“CN”。| |参数约束及描述：实名认证填写的注册国家。国家的两位字母简码。例如：注册国家为“中国”请填写“CN”。|

        :param reg_country: The reg_country of this ChangeEnterpriseRealnameAuthsReq.
        :type: str
        """
        self._reg_country = reg_country

    @property
    def reg_address(self):
        """Gets the reg_address of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：实名认证企业注册地址。| |参数约束及描述：实名认证企业注册地址。|

        :return: The reg_address of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._reg_address

    @reg_address.setter
    def reg_address(self, reg_address):
        """Sets the reg_address of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：实名认证企业注册地址。| |参数约束及描述：实名认证企业注册地址。|

        :param reg_address: The reg_address of this ChangeEnterpriseRealnameAuthsReq.
        :type: str
        """
        self._reg_address = reg_address

    @property
    def change_type(self):
        """Gets the change_type of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：变更类型：1：个人变企业| |参数的约束及描述：变更类型：1：个人变企业|

        :return: The change_type of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: int
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：变更类型：1：个人变企业| |参数的约束及描述：变更类型：1：个人变企业|

        :param change_type: The change_type of this ChangeEnterpriseRealnameAuthsReq.
        :type: int
        """
        self._change_type = change_type

    @property
    def xaccount_type(self):
        """Gets the xaccount_type of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：华为分给合作伙伴的平台标识。该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值| |参数约束及描述：华为分给合作伙伴的平台标识。该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值|

        :return: The xaccount_type of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._xaccount_type

    @xaccount_type.setter
    def xaccount_type(self, xaccount_type):
        """Sets the xaccount_type of this ChangeEnterpriseRealnameAuthsReq.

        |参数名称：华为分给合作伙伴的平台标识。该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值| |参数约束及描述：华为分给合作伙伴的平台标识。该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值|

        :param xaccount_type: The xaccount_type of this ChangeEnterpriseRealnameAuthsReq.
        :type: str
        """
        self._xaccount_type = xaccount_type

    @property
    def enterprise_person(self):
        """Gets the enterprise_person of this ChangeEnterpriseRealnameAuthsReq.


        :return: The enterprise_person of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: EnterprisePersonNew
        """
        return self._enterprise_person

    @enterprise_person.setter
    def enterprise_person(self, enterprise_person):
        """Sets the enterprise_person of this ChangeEnterpriseRealnameAuthsReq.


        :param enterprise_person: The enterprise_person of this ChangeEnterpriseRealnameAuthsReq.
        :type: EnterprisePersonNew
        """
        self._enterprise_person = enterprise_person

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
        if not isinstance(other, ChangeEnterpriseRealnameAuthsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
