# coding: utf-8

import pprint
import re

import six





class ListSecretStageRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'secret_id': 'str',
        'stage_name': 'str'
    }

    attribute_map = {
        'secret_id': 'secret_id',
        'stage_name': 'stage_name'
    }

    def __init__(self, secret_id=None, stage_name=None):
        """ListSecretStageRequest - a model defined in huaweicloud sdk"""
        
        

        self._secret_id = None
        self._stage_name = None
        self.discriminator = None

        self.secret_id = secret_id
        self.stage_name = stage_name

    @property
    def secret_id(self):
        """Gets the secret_id of this ListSecretStageRequest.


        :return: The secret_id of this ListSecretStageRequest.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """Sets the secret_id of this ListSecretStageRequest.


        :param secret_id: The secret_id of this ListSecretStageRequest.
        :type: str
        """
        self._secret_id = secret_id

    @property
    def stage_name(self):
        """Gets the stage_name of this ListSecretStageRequest.


        :return: The stage_name of this ListSecretStageRequest.
        :rtype: str
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name):
        """Sets the stage_name of this ListSecretStageRequest.


        :param stage_name: The stage_name of this ListSecretStageRequest.
        :type: str
        """
        self._stage_name = stage_name

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
        if not isinstance(other, ListSecretStageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other