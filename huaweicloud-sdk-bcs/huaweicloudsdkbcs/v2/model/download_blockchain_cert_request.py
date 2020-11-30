# coding: utf-8

import pprint
import re

import six





class DownloadBlockchainCertRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'blockchain_id': 'str',
        'org_name': 'str',
        'cert_type': 'str'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'org_name': 'org_name',
        'cert_type': 'cert_type'
    }

    def __init__(self, blockchain_id=None, org_name=None, cert_type=None):
        """DownloadBlockchainCertRequest - a model defined in huaweicloud sdk"""
        
        

        self._blockchain_id = None
        self._org_name = None
        self._cert_type = None
        self.discriminator = None

        self.blockchain_id = blockchain_id
        self.org_name = org_name
        self.cert_type = cert_type

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this DownloadBlockchainCertRequest.


        :return: The blockchain_id of this DownloadBlockchainCertRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this DownloadBlockchainCertRequest.


        :param blockchain_id: The blockchain_id of this DownloadBlockchainCertRequest.
        :type: str
        """
        self._blockchain_id = blockchain_id

    @property
    def org_name(self):
        """Gets the org_name of this DownloadBlockchainCertRequest.


        :return: The org_name of this DownloadBlockchainCertRequest.
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this DownloadBlockchainCertRequest.


        :param org_name: The org_name of this DownloadBlockchainCertRequest.
        :type: str
        """
        self._org_name = org_name

    @property
    def cert_type(self):
        """Gets the cert_type of this DownloadBlockchainCertRequest.


        :return: The cert_type of this DownloadBlockchainCertRequest.
        :rtype: str
        """
        return self._cert_type

    @cert_type.setter
    def cert_type(self, cert_type):
        """Sets the cert_type of this DownloadBlockchainCertRequest.


        :param cert_type: The cert_type of this DownloadBlockchainCertRequest.
        :type: str
        """
        self._cert_type = cert_type

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
        if not isinstance(other, DownloadBlockchainCertRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
