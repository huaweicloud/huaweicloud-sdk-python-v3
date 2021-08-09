# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DistinguishedName:


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
        'country': 'str',
        'locality': 'str',
        'organization': 'str',
        'organizational_unit': 'str',
        'state': 'str'
    }

    attribute_map = {
        'common_name': 'common_name',
        'country': 'country',
        'locality': 'locality',
        'organization': 'organization',
        'organizational_unit': 'organizational_unit',
        'state': 'state'
    }

    def __init__(self, common_name=None, country=None, locality=None, organization=None, organizational_unit=None, state=None):
        """DistinguishedName - a model defined in huaweicloud sdk"""
        
        

        self._common_name = None
        self._country = None
        self._locality = None
        self._organization = None
        self._organizational_unit = None
        self._state = None
        self.discriminator = None

        if common_name is not None:
            self.common_name = common_name
        if country is not None:
            self.country = country
        if locality is not None:
            self.locality = locality
        if organization is not None:
            self.organization = organization
        if organizational_unit is not None:
            self.organizational_unit = organizational_unit
        if state is not None:
            self.state = state

    @property
    def common_name(self):
        """Gets the common_name of this DistinguishedName.

        通用名称

        :return: The common_name of this DistinguishedName.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this DistinguishedName.

        通用名称

        :param common_name: The common_name of this DistinguishedName.
        :type: str
        """
        self._common_name = common_name

    @property
    def country(self):
        """Gets the country of this DistinguishedName.

        国家编码

        :return: The country of this DistinguishedName.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this DistinguishedName.

        国家编码

        :param country: The country of this DistinguishedName.
        :type: str
        """
        self._country = country

    @property
    def locality(self):
        """Gets the locality of this DistinguishedName.

        地区名称

        :return: The locality of this DistinguishedName.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this DistinguishedName.

        地区名称

        :param locality: The locality of this DistinguishedName.
        :type: str
        """
        self._locality = locality

    @property
    def organization(self):
        """Gets the organization of this DistinguishedName.

        组织名称

        :return: The organization of this DistinguishedName.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this DistinguishedName.

        组织名称

        :param organization: The organization of this DistinguishedName.
        :type: str
        """
        self._organization = organization

    @property
    def organizational_unit(self):
        """Gets the organizational_unit of this DistinguishedName.

        组织单元名称

        :return: The organizational_unit of this DistinguishedName.
        :rtype: str
        """
        return self._organizational_unit

    @organizational_unit.setter
    def organizational_unit(self, organizational_unit):
        """Sets the organizational_unit of this DistinguishedName.

        组织单元名称

        :param organizational_unit: The organizational_unit of this DistinguishedName.
        :type: str
        """
        self._organizational_unit = organizational_unit

    @property
    def state(self):
        """Gets the state of this DistinguishedName.

        省市

        :return: The state of this DistinguishedName.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DistinguishedName.

        省市

        :param state: The state of this DistinguishedName.
        :type: str
        """
        self._state = state

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DistinguishedName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other