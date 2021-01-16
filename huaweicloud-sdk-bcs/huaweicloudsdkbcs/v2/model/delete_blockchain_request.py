# coding: utf-8

import pprint
import re

import six





class DeleteBlockchainRequest:


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
        'is_delete_storage': 'bool',
        'is_delete_obs': 'bool',
        'is_delete_resource': 'bool'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'is_delete_storage': 'is_delete_storage',
        'is_delete_obs': 'is_delete_obs',
        'is_delete_resource': 'is_delete_resource'
    }

    def __init__(self, blockchain_id=None, is_delete_storage=None, is_delete_obs=None, is_delete_resource=None):
        """DeleteBlockchainRequest - a model defined in huaweicloud sdk"""
        
        

        self._blockchain_id = None
        self._is_delete_storage = None
        self._is_delete_obs = None
        self._is_delete_resource = None
        self.discriminator = None

        self.blockchain_id = blockchain_id
        if is_delete_storage is not None:
            self.is_delete_storage = is_delete_storage
        if is_delete_obs is not None:
            self.is_delete_obs = is_delete_obs
        if is_delete_resource is not None:
            self.is_delete_resource = is_delete_resource

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this DeleteBlockchainRequest.


        :return: The blockchain_id of this DeleteBlockchainRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this DeleteBlockchainRequest.


        :param blockchain_id: The blockchain_id of this DeleteBlockchainRequest.
        :type: str
        """
        self._blockchain_id = blockchain_id

    @property
    def is_delete_storage(self):
        """Gets the is_delete_storage of this DeleteBlockchainRequest.


        :return: The is_delete_storage of this DeleteBlockchainRequest.
        :rtype: bool
        """
        return self._is_delete_storage

    @is_delete_storage.setter
    def is_delete_storage(self, is_delete_storage):
        """Sets the is_delete_storage of this DeleteBlockchainRequest.


        :param is_delete_storage: The is_delete_storage of this DeleteBlockchainRequest.
        :type: bool
        """
        self._is_delete_storage = is_delete_storage

    @property
    def is_delete_obs(self):
        """Gets the is_delete_obs of this DeleteBlockchainRequest.


        :return: The is_delete_obs of this DeleteBlockchainRequest.
        :rtype: bool
        """
        return self._is_delete_obs

    @is_delete_obs.setter
    def is_delete_obs(self, is_delete_obs):
        """Sets the is_delete_obs of this DeleteBlockchainRequest.


        :param is_delete_obs: The is_delete_obs of this DeleteBlockchainRequest.
        :type: bool
        """
        self._is_delete_obs = is_delete_obs

    @property
    def is_delete_resource(self):
        """Gets the is_delete_resource of this DeleteBlockchainRequest.


        :return: The is_delete_resource of this DeleteBlockchainRequest.
        :rtype: bool
        """
        return self._is_delete_resource

    @is_delete_resource.setter
    def is_delete_resource(self, is_delete_resource):
        """Sets the is_delete_resource of this DeleteBlockchainRequest.


        :param is_delete_resource: The is_delete_resource of this DeleteBlockchainRequest.
        :type: bool
        """
        self._is_delete_resource = is_delete_resource

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
        if not isinstance(other, DeleteBlockchainRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
