# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Domains:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "Domains"

    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'create_time': 'str',
        'certificate_id': 'str'
    }

    attribute_map = {
        'domain_name': 'DomainName',
        'create_time': 'CreateTime',
        'certificate_id': 'CertificateId'
    }

    def __init__(self, domain_name=None, create_time=None, certificate_id=None):
        r"""Domains

        The model defined in huaweicloud sdk

        :param domain_name: Custom domain name
        :type domain_name: str
        :param create_time: Time when a custom domain name was created
        :type create_time: str
        :param certificate_id: Certificate id 
        :type certificate_id: str
        """
        
        

        self._domain_name = None
        self._create_time = None
        self._certificate_id = None
        self.discriminator = None

        self.domain_name = domain_name
        self.create_time = create_time
        if certificate_id is not None:
            self.certificate_id = certificate_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this Domains.

        Custom domain name

        :return: The domain_name of this Domains.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this Domains.

        Custom domain name

        :param domain_name: The domain_name of this Domains.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def create_time(self):
        r"""Gets the create_time of this Domains.

        Time when a custom domain name was created

        :return: The create_time of this Domains.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Domains.

        Time when a custom domain name was created

        :param create_time: The create_time of this Domains.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this Domains.

        Certificate id 

        :return: The certificate_id of this Domains.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this Domains.

        Certificate id 

        :param certificate_id: The certificate_id of this Domains.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

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
        if not isinstance(other, Domains):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
