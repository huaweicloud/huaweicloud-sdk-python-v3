# coding: utf-8

import pprint
import re

import six





class VaultBackup:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'parameters': 'CheckpointParam',
        'vault_id': 'str'
    }

    attribute_map = {
        'parameters': 'parameters',
        'vault_id': 'vault_id'
    }

    def __init__(self, parameters=None, vault_id=None):
        """VaultBackup - a model defined in huaweicloud sdk"""
        
        

        self._parameters = None
        self._vault_id = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters
        self.vault_id = vault_id

    @property
    def parameters(self):
        """Gets the parameters of this VaultBackup.


        :return: The parameters of this VaultBackup.
        :rtype: CheckpointParam
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this VaultBackup.


        :param parameters: The parameters of this VaultBackup.
        :type: CheckpointParam
        """
        self._parameters = parameters

    @property
    def vault_id(self):
        """Gets the vault_id of this VaultBackup.

        存储库ID

        :return: The vault_id of this VaultBackup.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this VaultBackup.

        存储库ID

        :param vault_id: The vault_id of this VaultBackup.
        :type: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, VaultBackup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
