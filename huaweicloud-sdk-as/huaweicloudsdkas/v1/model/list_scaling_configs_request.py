# coding: utf-8

import pprint
import re

import six





class ListScalingConfigsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_configuration_name': 'str',
        'image_id': 'str',
        'start_number': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'scaling_configuration_name': 'scaling_configuration_name',
        'image_id': 'image_id',
        'start_number': 'start_number',
        'limit': 'limit'
    }

    def __init__(self, scaling_configuration_name=None, image_id=None, start_number=None, limit=None):
        """ListScalingConfigsRequest - a model defined in huaweicloud sdk"""
        
        

        self._scaling_configuration_name = None
        self._image_id = None
        self._start_number = None
        self._limit = None
        self.discriminator = None

        if scaling_configuration_name is not None:
            self.scaling_configuration_name = scaling_configuration_name
        if image_id is not None:
            self.image_id = image_id
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit

    @property
    def scaling_configuration_name(self):
        """Gets the scaling_configuration_name of this ListScalingConfigsRequest.


        :return: The scaling_configuration_name of this ListScalingConfigsRequest.
        :rtype: str
        """
        return self._scaling_configuration_name

    @scaling_configuration_name.setter
    def scaling_configuration_name(self, scaling_configuration_name):
        """Sets the scaling_configuration_name of this ListScalingConfigsRequest.


        :param scaling_configuration_name: The scaling_configuration_name of this ListScalingConfigsRequest.
        :type: str
        """
        self._scaling_configuration_name = scaling_configuration_name

    @property
    def image_id(self):
        """Gets the image_id of this ListScalingConfigsRequest.


        :return: The image_id of this ListScalingConfigsRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ListScalingConfigsRequest.


        :param image_id: The image_id of this ListScalingConfigsRequest.
        :type: str
        """
        self._image_id = image_id

    @property
    def start_number(self):
        """Gets the start_number of this ListScalingConfigsRequest.


        :return: The start_number of this ListScalingConfigsRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListScalingConfigsRequest.


        :param start_number: The start_number of this ListScalingConfigsRequest.
        :type: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListScalingConfigsRequest.


        :return: The limit of this ListScalingConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListScalingConfigsRequest.


        :param limit: The limit of this ListScalingConfigsRequest.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListScalingConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
