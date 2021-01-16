# coding: utf-8

import pprint
import re

import six





class UpdateRepoDomainsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'repository': 'str',
        'access_domain': 'str',
        'body': 'UpdateRepoDomainsRequestBody'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'access_domain': 'access_domain',
        'body': 'body'
    }

    def __init__(self, namespace=None, repository=None, access_domain=None, body=None):
        """UpdateRepoDomainsRequest - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._repository = None
        self._access_domain = None
        self._body = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        self.access_domain = access_domain
        if body is not None:
            self.body = body

    @property
    def namespace(self):
        """Gets the namespace of this UpdateRepoDomainsRequest.


        :return: The namespace of this UpdateRepoDomainsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this UpdateRepoDomainsRequest.


        :param namespace: The namespace of this UpdateRepoDomainsRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        """Gets the repository of this UpdateRepoDomainsRequest.


        :return: The repository of this UpdateRepoDomainsRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this UpdateRepoDomainsRequest.


        :param repository: The repository of this UpdateRepoDomainsRequest.
        :type: str
        """
        self._repository = repository

    @property
    def access_domain(self):
        """Gets the access_domain of this UpdateRepoDomainsRequest.


        :return: The access_domain of this UpdateRepoDomainsRequest.
        :rtype: str
        """
        return self._access_domain

    @access_domain.setter
    def access_domain(self, access_domain):
        """Sets the access_domain of this UpdateRepoDomainsRequest.


        :param access_domain: The access_domain of this UpdateRepoDomainsRequest.
        :type: str
        """
        self._access_domain = access_domain

    @property
    def body(self):
        """Gets the body of this UpdateRepoDomainsRequest.


        :return: The body of this UpdateRepoDomainsRequest.
        :rtype: UpdateRepoDomainsRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateRepoDomainsRequest.


        :param body: The body of this UpdateRepoDomainsRequest.
        :type: UpdateRepoDomainsRequestBody
        """
        self._body = body

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
        if not isinstance(other, UpdateRepoDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
