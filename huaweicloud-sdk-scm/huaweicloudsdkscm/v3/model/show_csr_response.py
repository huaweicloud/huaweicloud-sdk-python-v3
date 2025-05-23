# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCsrResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'csr': 'str',
        'domain_name': 'str',
        'sans': 'str',
        'private_key_algo': 'str',
        'usage': 'str',
        'company_country': 'str',
        'company_province': 'str',
        'company_city': 'str',
        'company_name': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'csr': 'csr',
        'domain_name': 'domain_name',
        'sans': 'sans',
        'private_key_algo': 'private_key_algo',
        'usage': 'usage',
        'company_country': 'company_country',
        'company_province': 'company_province',
        'company_city': 'company_city',
        'company_name': 'company_name',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, csr=None, domain_name=None, sans=None, private_key_algo=None, usage=None, company_country=None, company_province=None, company_city=None, company_name=None, create_time=None, update_time=None):
        r"""ShowCsrResponse

        The model defined in huaweicloud sdk

        :param id: CSR的ID。
        :type id: str
        :param name: CSR名称。
        :type name: str
        :param csr: CSR内容。
        :type csr: str
        :param domain_name: CSR绑定的域名。
        :type domain_name: str
        :param sans: CSR绑定的附加域名。
        :type sans: str
        :param private_key_algo: 密钥算法。
        :type private_key_algo: str
        :param usage: CSR用途。
        :type usage: str
        :param company_country: 国家。
        :type company_country: str
        :param company_province: 省份。
        :type company_province: str
        :param company_city: 城市。
        :type company_city: str
        :param company_name: 公司名称。
        :type company_name: str
        :param create_time: CSR创建时间。
        :type create_time: int
        :param update_time: CSR更新时间。
        :type update_time: int
        """
        
        super(ShowCsrResponse, self).__init__()

        self._id = None
        self._name = None
        self._csr = None
        self._domain_name = None
        self._sans = None
        self._private_key_algo = None
        self._usage = None
        self._company_country = None
        self._company_province = None
        self._company_city = None
        self._company_name = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if csr is not None:
            self.csr = csr
        if domain_name is not None:
            self.domain_name = domain_name
        if sans is not None:
            self.sans = sans
        if private_key_algo is not None:
            self.private_key_algo = private_key_algo
        if usage is not None:
            self.usage = usage
        if company_country is not None:
            self.company_country = company_country
        if company_province is not None:
            self.company_province = company_province
        if company_city is not None:
            self.company_city = company_city
        if company_name is not None:
            self.company_name = company_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ShowCsrResponse.

        CSR的ID。

        :return: The id of this ShowCsrResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowCsrResponse.

        CSR的ID。

        :param id: The id of this ShowCsrResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowCsrResponse.

        CSR名称。

        :return: The name of this ShowCsrResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowCsrResponse.

        CSR名称。

        :param name: The name of this ShowCsrResponse.
        :type name: str
        """
        self._name = name

    @property
    def csr(self):
        r"""Gets the csr of this ShowCsrResponse.

        CSR内容。

        :return: The csr of this ShowCsrResponse.
        :rtype: str
        """
        return self._csr

    @csr.setter
    def csr(self, csr):
        r"""Sets the csr of this ShowCsrResponse.

        CSR内容。

        :param csr: The csr of this ShowCsrResponse.
        :type csr: str
        """
        self._csr = csr

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowCsrResponse.

        CSR绑定的域名。

        :return: The domain_name of this ShowCsrResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowCsrResponse.

        CSR绑定的域名。

        :param domain_name: The domain_name of this ShowCsrResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def sans(self):
        r"""Gets the sans of this ShowCsrResponse.

        CSR绑定的附加域名。

        :return: The sans of this ShowCsrResponse.
        :rtype: str
        """
        return self._sans

    @sans.setter
    def sans(self, sans):
        r"""Sets the sans of this ShowCsrResponse.

        CSR绑定的附加域名。

        :param sans: The sans of this ShowCsrResponse.
        :type sans: str
        """
        self._sans = sans

    @property
    def private_key_algo(self):
        r"""Gets the private_key_algo of this ShowCsrResponse.

        密钥算法。

        :return: The private_key_algo of this ShowCsrResponse.
        :rtype: str
        """
        return self._private_key_algo

    @private_key_algo.setter
    def private_key_algo(self, private_key_algo):
        r"""Sets the private_key_algo of this ShowCsrResponse.

        密钥算法。

        :param private_key_algo: The private_key_algo of this ShowCsrResponse.
        :type private_key_algo: str
        """
        self._private_key_algo = private_key_algo

    @property
    def usage(self):
        r"""Gets the usage of this ShowCsrResponse.

        CSR用途。

        :return: The usage of this ShowCsrResponse.
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this ShowCsrResponse.

        CSR用途。

        :param usage: The usage of this ShowCsrResponse.
        :type usage: str
        """
        self._usage = usage

    @property
    def company_country(self):
        r"""Gets the company_country of this ShowCsrResponse.

        国家。

        :return: The company_country of this ShowCsrResponse.
        :rtype: str
        """
        return self._company_country

    @company_country.setter
    def company_country(self, company_country):
        r"""Sets the company_country of this ShowCsrResponse.

        国家。

        :param company_country: The company_country of this ShowCsrResponse.
        :type company_country: str
        """
        self._company_country = company_country

    @property
    def company_province(self):
        r"""Gets the company_province of this ShowCsrResponse.

        省份。

        :return: The company_province of this ShowCsrResponse.
        :rtype: str
        """
        return self._company_province

    @company_province.setter
    def company_province(self, company_province):
        r"""Sets the company_province of this ShowCsrResponse.

        省份。

        :param company_province: The company_province of this ShowCsrResponse.
        :type company_province: str
        """
        self._company_province = company_province

    @property
    def company_city(self):
        r"""Gets the company_city of this ShowCsrResponse.

        城市。

        :return: The company_city of this ShowCsrResponse.
        :rtype: str
        """
        return self._company_city

    @company_city.setter
    def company_city(self, company_city):
        r"""Sets the company_city of this ShowCsrResponse.

        城市。

        :param company_city: The company_city of this ShowCsrResponse.
        :type company_city: str
        """
        self._company_city = company_city

    @property
    def company_name(self):
        r"""Gets the company_name of this ShowCsrResponse.

        公司名称。

        :return: The company_name of this ShowCsrResponse.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        r"""Sets the company_name of this ShowCsrResponse.

        公司名称。

        :param company_name: The company_name of this ShowCsrResponse.
        :type company_name: str
        """
        self._company_name = company_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowCsrResponse.

        CSR创建时间。

        :return: The create_time of this ShowCsrResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowCsrResponse.

        CSR创建时间。

        :param create_time: The create_time of this ShowCsrResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowCsrResponse.

        CSR更新时间。

        :return: The update_time of this ShowCsrResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowCsrResponse.

        CSR更新时间。

        :param update_time: The update_time of this ShowCsrResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ShowCsrResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
