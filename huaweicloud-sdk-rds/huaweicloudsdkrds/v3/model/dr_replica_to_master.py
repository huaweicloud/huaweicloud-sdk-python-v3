# coding: utf-8

import pprint
import re

import six





class DrReplicaToMaster:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'drreplica_to_master': 'object'
    }

    attribute_map = {
        'drreplica_to_master': 'drreplica_to_master'
    }

    def __init__(self, drreplica_to_master=None):
        """DrReplicaToMaster - a model defined in huaweicloud sdk"""
        
        

        self._drreplica_to_master = None
        self.discriminator = None

        self.drreplica_to_master = drreplica_to_master

    @property
    def drreplica_to_master(self):
        """Gets the drreplica_to_master of this DrReplicaToMaster.


        :return: The drreplica_to_master of this DrReplicaToMaster.
        :rtype: object
        """
        return self._drreplica_to_master

    @drreplica_to_master.setter
    def drreplica_to_master(self, drreplica_to_master):
        """Sets the drreplica_to_master of this DrReplicaToMaster.


        :param drreplica_to_master: The drreplica_to_master of this DrReplicaToMaster.
        :type: object
        """
        self._drreplica_to_master = drreplica_to_master

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
        if not isinstance(other, DrReplicaToMaster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
