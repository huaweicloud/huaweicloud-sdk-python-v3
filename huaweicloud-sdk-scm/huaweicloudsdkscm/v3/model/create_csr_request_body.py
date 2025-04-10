# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCsrRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'domain_name': 'str',
        'sans': 'str',
        'private_key_algo': 'str',
        'usage': 'str',
        'company_country': 'str',
        'company_province': 'str',
        'company_city': 'str',
        'company_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'domain_name': 'domain_name',
        'sans': 'sans',
        'private_key_algo': 'private_key_algo',
        'usage': 'usage',
        'company_country': 'company_country',
        'company_province': 'company_province',
        'company_city': 'company_city',
        'company_name': 'company_name'
    }

    def __init__(self, name=None, domain_name=None, sans=None, private_key_algo=None, usage=None, company_country=None, company_province=None, company_city=None, company_name=None):
        r"""CreateCsrRequestBody

        The model defined in huaweicloud sdk

        :param name: 自定义CSR名称。
        :type name: str
        :param domain_name: CSR绑定的域名。如果您想在提交证书申请时使用该CSR，必须确保证书绑定域名包含此处设置的域名。
        :type domain_name: str
        :param sans: CSR绑定的附加域名。
        :type sans: str
        :param private_key_algo: 私钥算法。取值如下： - RSA_2048 - RSA_3072 - RSA_4096 - EC_P256 - EC_P384 - SM2
        :type private_key_algo: str
        :param usage: CSR用途。取值如下： - PERSONAL：个人证书 - ENTERPRISE：企业证书
        :type usage: str
        :param company_country: 国家，当“usage”取值为“ENTERPRISE”时，本参数必填。取值示例：CN。
        :type company_country: str
        :param company_province: 省份，当“usage”取值为“ENTERPRISE”时，本参数必填。取值示例：北京市。
        :type company_province: str
        :param company_city: 城市。当“usage”取值为“ENTERPRISE”时，本参数必填。取值示例：北京市。
        :type company_city: str
        :param company_name: 公司名称。当“usage”取值为“ENTERPRISE”时，本参数必填。
        :type company_name: str
        """
        
        

        self._name = None
        self._domain_name = None
        self._sans = None
        self._private_key_algo = None
        self._usage = None
        self._company_country = None
        self._company_province = None
        self._company_city = None
        self._company_name = None
        self.discriminator = None

        self.name = name
        self.domain_name = domain_name
        if sans is not None:
            self.sans = sans
        self.private_key_algo = private_key_algo
        self.usage = usage
        if company_country is not None:
            self.company_country = company_country
        if company_province is not None:
            self.company_province = company_province
        if company_city is not None:
            self.company_city = company_city
        if company_name is not None:
            self.company_name = company_name

    @property
    def name(self):
        r"""Gets the name of this CreateCsrRequestBody.

        自定义CSR名称。

        :return: The name of this CreateCsrRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCsrRequestBody.

        自定义CSR名称。

        :param name: The name of this CreateCsrRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def domain_name(self):
        r"""Gets the domain_name of this CreateCsrRequestBody.

        CSR绑定的域名。如果您想在提交证书申请时使用该CSR，必须确保证书绑定域名包含此处设置的域名。

        :return: The domain_name of this CreateCsrRequestBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this CreateCsrRequestBody.

        CSR绑定的域名。如果您想在提交证书申请时使用该CSR，必须确保证书绑定域名包含此处设置的域名。

        :param domain_name: The domain_name of this CreateCsrRequestBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def sans(self):
        r"""Gets the sans of this CreateCsrRequestBody.

        CSR绑定的附加域名。

        :return: The sans of this CreateCsrRequestBody.
        :rtype: str
        """
        return self._sans

    @sans.setter
    def sans(self, sans):
        r"""Sets the sans of this CreateCsrRequestBody.

        CSR绑定的附加域名。

        :param sans: The sans of this CreateCsrRequestBody.
        :type sans: str
        """
        self._sans = sans

    @property
    def private_key_algo(self):
        r"""Gets the private_key_algo of this CreateCsrRequestBody.

        私钥算法。取值如下： - RSA_2048 - RSA_3072 - RSA_4096 - EC_P256 - EC_P384 - SM2

        :return: The private_key_algo of this CreateCsrRequestBody.
        :rtype: str
        """
        return self._private_key_algo

    @private_key_algo.setter
    def private_key_algo(self, private_key_algo):
        r"""Sets the private_key_algo of this CreateCsrRequestBody.

        私钥算法。取值如下： - RSA_2048 - RSA_3072 - RSA_4096 - EC_P256 - EC_P384 - SM2

        :param private_key_algo: The private_key_algo of this CreateCsrRequestBody.
        :type private_key_algo: str
        """
        self._private_key_algo = private_key_algo

    @property
    def usage(self):
        r"""Gets the usage of this CreateCsrRequestBody.

        CSR用途。取值如下： - PERSONAL：个人证书 - ENTERPRISE：企业证书

        :return: The usage of this CreateCsrRequestBody.
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this CreateCsrRequestBody.

        CSR用途。取值如下： - PERSONAL：个人证书 - ENTERPRISE：企业证书

        :param usage: The usage of this CreateCsrRequestBody.
        :type usage: str
        """
        self._usage = usage

    @property
    def company_country(self):
        r"""Gets the company_country of this CreateCsrRequestBody.

        国家，当“usage”取值为“ENTERPRISE”时，本参数必填。取值示例：CN。

        :return: The company_country of this CreateCsrRequestBody.
        :rtype: str
        """
        return self._company_country

    @company_country.setter
    def company_country(self, company_country):
        r"""Sets the company_country of this CreateCsrRequestBody.

        国家，当“usage”取值为“ENTERPRISE”时，本参数必填。取值示例：CN。

        :param company_country: The company_country of this CreateCsrRequestBody.
        :type company_country: str
        """
        self._company_country = company_country

    @property
    def company_province(self):
        r"""Gets the company_province of this CreateCsrRequestBody.

        省份，当“usage”取值为“ENTERPRISE”时，本参数必填。取值示例：北京市。

        :return: The company_province of this CreateCsrRequestBody.
        :rtype: str
        """
        return self._company_province

    @company_province.setter
    def company_province(self, company_province):
        r"""Sets the company_province of this CreateCsrRequestBody.

        省份，当“usage”取值为“ENTERPRISE”时，本参数必填。取值示例：北京市。

        :param company_province: The company_province of this CreateCsrRequestBody.
        :type company_province: str
        """
        self._company_province = company_province

    @property
    def company_city(self):
        r"""Gets the company_city of this CreateCsrRequestBody.

        城市。当“usage”取值为“ENTERPRISE”时，本参数必填。取值示例：北京市。

        :return: The company_city of this CreateCsrRequestBody.
        :rtype: str
        """
        return self._company_city

    @company_city.setter
    def company_city(self, company_city):
        r"""Sets the company_city of this CreateCsrRequestBody.

        城市。当“usage”取值为“ENTERPRISE”时，本参数必填。取值示例：北京市。

        :param company_city: The company_city of this CreateCsrRequestBody.
        :type company_city: str
        """
        self._company_city = company_city

    @property
    def company_name(self):
        r"""Gets the company_name of this CreateCsrRequestBody.

        公司名称。当“usage”取值为“ENTERPRISE”时，本参数必填。

        :return: The company_name of this CreateCsrRequestBody.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        r"""Sets the company_name of this CreateCsrRequestBody.

        公司名称。当“usage”取值为“ENTERPRISE”时，本参数必填。

        :param company_name: The company_name of this CreateCsrRequestBody.
        :type company_name: str
        """
        self._company_name = company_name

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
        if not isinstance(other, CreateCsrRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
