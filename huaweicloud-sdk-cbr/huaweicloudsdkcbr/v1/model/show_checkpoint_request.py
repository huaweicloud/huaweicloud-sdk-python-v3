# coding: utf-8

import pprint
import re

import six





class ShowCheckpointRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'checkpoint_id': 'str'
    }

    attribute_map = {
        'checkpoint_id': 'checkpoint_id'
    }

    def __init__(self, checkpoint_id=None):
        """ShowCheckpointRequest - a model defined in huaweicloud sdk"""
        
        

        self._checkpoint_id = None
        self.discriminator = None

        self.checkpoint_id = checkpoint_id

    @property
    def checkpoint_id(self):
        """Gets the checkpoint_id of this ShowCheckpointRequest.


        :return: The checkpoint_id of this ShowCheckpointRequest.
        :rtype: str
        """
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, checkpoint_id):
        """Sets the checkpoint_id of this ShowCheckpointRequest.


        :param checkpoint_id: The checkpoint_id of this ShowCheckpointRequest.
        :type: str
        """
        self._checkpoint_id = checkpoint_id

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
        if not isinstance(other, ShowCheckpointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
