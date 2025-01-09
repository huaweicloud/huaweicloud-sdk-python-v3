# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CSRResponseBody:

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
        'domain_name': 'str',
        'sans': 'str',
        'private_key_algo': 'str',
        'usage': 'str',
        'company_country': 'str',
        'company_province': 'str',
        'company_city': 'str',
        'company_name': 'str',
        'create_time': 'float',
        'update_time': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
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

    def __init__(self, id=None, name=None, domain_name=None, sans=None, private_key_algo=None, usage=None, company_country=None, company_province=None, company_city=None, company_name=None, create_time=None, update_time=None):
        """CSRResponseBody

        The model defined in huaweicloud sdk

        :param id: CSR的ID。
        :type id: str
        :param name: CSR名称。
        :type name: str
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
        :type create_time: float
        :param update_time: CSR更新时间。
        :type update_time: float
        """
        
        

        self._id = None
        self._name = None
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

        self.id = id
        self.name = name
        self.domain_name = domain_name
        self.sans = sans
        self.private_key_algo = private_key_algo
        self.usage = usage
        self.company_country = company_country
        self.company_province = company_province
        self.company_city = company_city
        self.company_name = company_name
        self.create_time = create_time
        self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this CSRResponseBody.

        CSR的ID。

        :return: The id of this CSRResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CSRResponseBody.

        CSR的ID。

        :param id: The id of this CSRResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CSRResponseBody.

        CSR名称。

        :return: The name of this CSRResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CSRResponseBody.

        CSR名称。

        :param name: The name of this CSRResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def domain_name(self):
        """Gets the domain_name of this CSRResponseBody.

        CSR绑定的域名。

        :return: The domain_name of this CSRResponseBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CSRResponseBody.

        CSR绑定的域名。

        :param domain_name: The domain_name of this CSRResponseBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def sans(self):
        """Gets the sans of this CSRResponseBody.

        CSR绑定的附加域名。

        :return: The sans of this CSRResponseBody.
        :rtype: str
        """
        return self._sans

    @sans.setter
    def sans(self, sans):
        """Sets the sans of this CSRResponseBody.

        CSR绑定的附加域名。

        :param sans: The sans of this CSRResponseBody.
        :type sans: str
        """
        self._sans = sans

    @property
    def private_key_algo(self):
        """Gets the private_key_algo of this CSRResponseBody.

        密钥算法。

        :return: The private_key_algo of this CSRResponseBody.
        :rtype: str
        """
        return self._private_key_algo

    @private_key_algo.setter
    def private_key_algo(self, private_key_algo):
        """Sets the private_key_algo of this CSRResponseBody.

        密钥算法。

        :param private_key_algo: The private_key_algo of this CSRResponseBody.
        :type private_key_algo: str
        """
        self._private_key_algo = private_key_algo

    @property
    def usage(self):
        """Gets the usage of this CSRResponseBody.

        CSR用途。

        :return: The usage of this CSRResponseBody.
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this CSRResponseBody.

        CSR用途。

        :param usage: The usage of this CSRResponseBody.
        :type usage: str
        """
        self._usage = usage

    @property
    def company_country(self):
        """Gets the company_country of this CSRResponseBody.

        国家。

        :return: The company_country of this CSRResponseBody.
        :rtype: str
        """
        return self._company_country

    @company_country.setter
    def company_country(self, company_country):
        """Sets the company_country of this CSRResponseBody.

        国家。

        :param company_country: The company_country of this CSRResponseBody.
        :type company_country: str
        """
        self._company_country = company_country

    @property
    def company_province(self):
        """Gets the company_province of this CSRResponseBody.

        省份。

        :return: The company_province of this CSRResponseBody.
        :rtype: str
        """
        return self._company_province

    @company_province.setter
    def company_province(self, company_province):
        """Sets the company_province of this CSRResponseBody.

        省份。

        :param company_province: The company_province of this CSRResponseBody.
        :type company_province: str
        """
        self._company_province = company_province

    @property
    def company_city(self):
        """Gets the company_city of this CSRResponseBody.

        城市。

        :return: The company_city of this CSRResponseBody.
        :rtype: str
        """
        return self._company_city

    @company_city.setter
    def company_city(self, company_city):
        """Sets the company_city of this CSRResponseBody.

        城市。

        :param company_city: The company_city of this CSRResponseBody.
        :type company_city: str
        """
        self._company_city = company_city

    @property
    def company_name(self):
        """Gets the company_name of this CSRResponseBody.

        公司名称。

        :return: The company_name of this CSRResponseBody.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this CSRResponseBody.

        公司名称。

        :param company_name: The company_name of this CSRResponseBody.
        :type company_name: str
        """
        self._company_name = company_name

    @property
    def create_time(self):
        """Gets the create_time of this CSRResponseBody.

        CSR创建时间。

        :return: The create_time of this CSRResponseBody.
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CSRResponseBody.

        CSR创建时间。

        :param create_time: The create_time of this CSRResponseBody.
        :type create_time: float
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CSRResponseBody.

        CSR更新时间。

        :return: The update_time of this CSRResponseBody.
        :rtype: float
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CSRResponseBody.

        CSR更新时间。

        :param update_time: The update_time of this CSRResponseBody.
        :type update_time: float
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
        if not isinstance(other, CSRResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
