# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowDetailsOfDomainNameCertificateV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'common_name': 'str',
        'san': 'list[str]',
        'version': 'str',
        'organization': 'list[str]',
        'organizational_unit': 'list[str]',
        'locality': 'list[str]',
        'state': 'list[str]',
        'country': 'list[str]',
        'not_before': 'str',
        'not_after': 'str',
        'serial_number': 'str',
        'issuer': 'list[str]',
        'signature_algorithm': 'str'
    }

    attribute_map = {
        'common_name': 'common_name',
        'san': 'san',
        'version': 'version',
        'organization': 'organization',
        'organizational_unit': 'organizational_unit',
        'locality': 'locality',
        'state': 'state',
        'country': 'country',
        'not_before': 'not_before',
        'not_after': 'not_after',
        'serial_number': 'serial_number',
        'issuer': 'issuer',
        'signature_algorithm': 'signature_algorithm'
    }

    def __init__(self, common_name=None, san=None, version=None, organization=None, organizational_unit=None, locality=None, state=None, country=None, not_before=None, not_after=None, serial_number=None, issuer=None, signature_algorithm=None):
        """ShowDetailsOfDomainNameCertificateV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._common_name = None
        self._san = None
        self._version = None
        self._organization = None
        self._organizational_unit = None
        self._locality = None
        self._state = None
        self._country = None
        self._not_before = None
        self._not_after = None
        self._serial_number = None
        self._issuer = None
        self._signature_algorithm = None
        self.discriminator = None

        if common_name is not None:
            self.common_name = common_name
        if san is not None:
            self.san = san
        if version is not None:
            self.version = version
        if organization is not None:
            self.organization = organization
        if organizational_unit is not None:
            self.organizational_unit = organizational_unit
        if locality is not None:
            self.locality = locality
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country
        if not_before is not None:
            self.not_before = not_before
        if not_after is not None:
            self.not_after = not_after
        if serial_number is not None:
            self.serial_number = serial_number
        if issuer is not None:
            self.issuer = issuer
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm

    @property
    def common_name(self):
        """Gets the common_name of this ShowDetailsOfDomainNameCertificateV2Response.

        证书域名

        :return: The common_name of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this ShowDetailsOfDomainNameCertificateV2Response.

        证书域名

        :param common_name: The common_name of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: str
        """
        self._common_name = common_name

    @property
    def san(self):
        """Gets the san of this ShowDetailsOfDomainNameCertificateV2Response.

        SAN域名

        :return: The san of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: list[str]
        """
        return self._san

    @san.setter
    def san(self, san):
        """Sets the san of this ShowDetailsOfDomainNameCertificateV2Response.

        SAN域名

        :param san: The san of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: list[str]
        """
        self._san = san

    @property
    def version(self):
        """Gets the version of this ShowDetailsOfDomainNameCertificateV2Response.

        证书版本

        :return: The version of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowDetailsOfDomainNameCertificateV2Response.

        证书版本

        :param version: The version of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: str
        """
        self._version = version

    @property
    def organization(self):
        """Gets the organization of this ShowDetailsOfDomainNameCertificateV2Response.

        公司、组织

        :return: The organization of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: list[str]
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ShowDetailsOfDomainNameCertificateV2Response.

        公司、组织

        :param organization: The organization of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: list[str]
        """
        self._organization = organization

    @property
    def organizational_unit(self):
        """Gets the organizational_unit of this ShowDetailsOfDomainNameCertificateV2Response.

        部门

        :return: The organizational_unit of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: list[str]
        """
        return self._organizational_unit

    @organizational_unit.setter
    def organizational_unit(self, organizational_unit):
        """Sets the organizational_unit of this ShowDetailsOfDomainNameCertificateV2Response.

        部门

        :param organizational_unit: The organizational_unit of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: list[str]
        """
        self._organizational_unit = organizational_unit

    @property
    def locality(self):
        """Gets the locality of this ShowDetailsOfDomainNameCertificateV2Response.

        城市

        :return: The locality of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: list[str]
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this ShowDetailsOfDomainNameCertificateV2Response.

        城市

        :param locality: The locality of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: list[str]
        """
        self._locality = locality

    @property
    def state(self):
        """Gets the state of this ShowDetailsOfDomainNameCertificateV2Response.

        省份

        :return: The state of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowDetailsOfDomainNameCertificateV2Response.

        省份

        :param state: The state of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: list[str]
        """
        self._state = state

    @property
    def country(self):
        """Gets the country of this ShowDetailsOfDomainNameCertificateV2Response.

        国家

        :return: The country of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: list[str]
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ShowDetailsOfDomainNameCertificateV2Response.

        国家

        :param country: The country of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: list[str]
        """
        self._country = country

    @property
    def not_before(self):
        """Gets the not_before of this ShowDetailsOfDomainNameCertificateV2Response.

        证书有效期起始时间

        :return: The not_before of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this ShowDetailsOfDomainNameCertificateV2Response.

        证书有效期起始时间

        :param not_before: The not_before of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: str
        """
        self._not_before = not_before

    @property
    def not_after(self):
        """Gets the not_after of this ShowDetailsOfDomainNameCertificateV2Response.

        证书有效期截止时间

        :return: The not_after of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this ShowDetailsOfDomainNameCertificateV2Response.

        证书有效期截止时间

        :param not_after: The not_after of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: str
        """
        self._not_after = not_after

    @property
    def serial_number(self):
        """Gets the serial_number of this ShowDetailsOfDomainNameCertificateV2Response.

        序列号

        :return: The serial_number of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ShowDetailsOfDomainNameCertificateV2Response.

        序列号

        :param serial_number: The serial_number of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def issuer(self):
        """Gets the issuer of this ShowDetailsOfDomainNameCertificateV2Response.

        颁发者

        :return: The issuer of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: list[str]
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this ShowDetailsOfDomainNameCertificateV2Response.

        颁发者

        :param issuer: The issuer of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: list[str]
        """
        self._issuer = issuer

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this ShowDetailsOfDomainNameCertificateV2Response.

        签名算法

        :return: The signature_algorithm of this ShowDetailsOfDomainNameCertificateV2Response.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this ShowDetailsOfDomainNameCertificateV2Response.

        签名算法

        :param signature_algorithm: The signature_algorithm of this ShowDetailsOfDomainNameCertificateV2Response.
        :type: str
        """
        self._signature_algorithm = signature_algorithm

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
        if not isinstance(other, ShowDetailsOfDomainNameCertificateV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
