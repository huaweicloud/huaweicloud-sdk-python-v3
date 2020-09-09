# coding: utf-8

import pprint
import re

import six





class ShowInstanceExtendProductInfoRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'type': 'str',
        'engine': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'type': 'type',
        'engine': 'engine'
    }

    def __init__(self, instance_id=None, type=None, engine=None):
        """ShowInstanceExtendProductInfoRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._type = None
        self._engine = None
        self.discriminator = None

        self.instance_id = instance_id
        self.type = type
        self.engine = engine

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowInstanceExtendProductInfoRequest.


        :return: The instance_id of this ShowInstanceExtendProductInfoRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowInstanceExtendProductInfoRequest.


        :param instance_id: The instance_id of this ShowInstanceExtendProductInfoRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        """Gets the type of this ShowInstanceExtendProductInfoRequest.


        :return: The type of this ShowInstanceExtendProductInfoRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowInstanceExtendProductInfoRequest.


        :param type: The type of this ShowInstanceExtendProductInfoRequest.
        :type: str
        """
        self._type = type

    @property
    def engine(self):
        """Gets the engine of this ShowInstanceExtendProductInfoRequest.


        :return: The engine of this ShowInstanceExtendProductInfoRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ShowInstanceExtendProductInfoRequest.


        :param engine: The engine of this ShowInstanceExtendProductInfoRequest.
        :type: str
        """
        self._engine = engine

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
        if not isinstance(other, ShowInstanceExtendProductInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
