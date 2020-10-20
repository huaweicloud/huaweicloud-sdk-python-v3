# coding: utf-8

import pprint
import re

import six





class ListCertificatesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'str',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'domain': 'str',
        'private_key': 'str',
        'certificate': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'domain': 'domain',
        'private_key': 'private_key',
        'certificate': 'certificate'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, name=None, description=None, type=None, domain=None, private_key=None, certificate=None):
        """ListCertificatesRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._domain = None
        self._private_key = None
        self._certificate = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if domain is not None:
            self.domain = domain
        if private_key is not None:
            self.private_key = private_key
        if certificate is not None:
            self.certificate = certificate

    @property
    def limit(self):
        """Gets the limit of this ListCertificatesRequest.


        :return: The limit of this ListCertificatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCertificatesRequest.


        :param limit: The limit of this ListCertificatesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListCertificatesRequest.


        :return: The marker of this ListCertificatesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListCertificatesRequest.


        :param marker: The marker of this ListCertificatesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListCertificatesRequest.


        :return: The page_reverse of this ListCertificatesRequest.
        :rtype: str
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListCertificatesRequest.


        :param page_reverse: The page_reverse of this ListCertificatesRequest.
        :type: str
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListCertificatesRequest.


        :return: The id of this ListCertificatesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListCertificatesRequest.


        :param id: The id of this ListCertificatesRequest.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListCertificatesRequest.


        :return: The name of this ListCertificatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCertificatesRequest.


        :param name: The name of this ListCertificatesRequest.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListCertificatesRequest.


        :return: The description of this ListCertificatesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListCertificatesRequest.


        :param description: The description of this ListCertificatesRequest.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this ListCertificatesRequest.


        :return: The type of this ListCertificatesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListCertificatesRequest.


        :param type: The type of this ListCertificatesRequest.
        :type: str
        """
        self._type = type

    @property
    def domain(self):
        """Gets the domain of this ListCertificatesRequest.


        :return: The domain of this ListCertificatesRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListCertificatesRequest.


        :param domain: The domain of this ListCertificatesRequest.
        :type: str
        """
        self._domain = domain

    @property
    def private_key(self):
        """Gets the private_key of this ListCertificatesRequest.


        :return: The private_key of this ListCertificatesRequest.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this ListCertificatesRequest.


        :param private_key: The private_key of this ListCertificatesRequest.
        :type: str
        """
        self._private_key = private_key

    @property
    def certificate(self):
        """Gets the certificate of this ListCertificatesRequest.


        :return: The certificate of this ListCertificatesRequest.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this ListCertificatesRequest.


        :param certificate: The certificate of this ListCertificatesRequest.
        :type: str
        """
        self._certificate = certificate

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
        if not isinstance(other, ListCertificatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
