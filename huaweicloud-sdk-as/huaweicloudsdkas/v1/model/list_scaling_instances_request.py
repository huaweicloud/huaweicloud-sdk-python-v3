# coding: utf-8

import pprint
import re

import six





class ListScalingInstancesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_group_id': 'str',
        'life_cycle_state': 'str',
        'health_status': 'str',
        'protect_from_scaling_down': 'str',
        'start_number': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'life_cycle_state': 'life_cycle_state',
        'health_status': 'health_status',
        'protect_from_scaling_down': 'protect_from_scaling_down',
        'start_number': 'start_number',
        'limit': 'limit'
    }

    def __init__(self, scaling_group_id=None, life_cycle_state=None, health_status=None, protect_from_scaling_down=None, start_number=None, limit=None):
        """ListScalingInstancesRequest - a model defined in huaweicloud sdk"""
        
        

        self._scaling_group_id = None
        self._life_cycle_state = None
        self._health_status = None
        self._protect_from_scaling_down = None
        self._start_number = None
        self._limit = None
        self.discriminator = None

        self.scaling_group_id = scaling_group_id
        if life_cycle_state is not None:
            self.life_cycle_state = life_cycle_state
        if health_status is not None:
            self.health_status = health_status
        if protect_from_scaling_down is not None:
            self.protect_from_scaling_down = protect_from_scaling_down
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ListScalingInstancesRequest.


        :return: The scaling_group_id of this ListScalingInstancesRequest.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ListScalingInstancesRequest.


        :param scaling_group_id: The scaling_group_id of this ListScalingInstancesRequest.
        :type: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def life_cycle_state(self):
        """Gets the life_cycle_state of this ListScalingInstancesRequest.


        :return: The life_cycle_state of this ListScalingInstancesRequest.
        :rtype: str
        """
        return self._life_cycle_state

    @life_cycle_state.setter
    def life_cycle_state(self, life_cycle_state):
        """Sets the life_cycle_state of this ListScalingInstancesRequest.


        :param life_cycle_state: The life_cycle_state of this ListScalingInstancesRequest.
        :type: str
        """
        self._life_cycle_state = life_cycle_state

    @property
    def health_status(self):
        """Gets the health_status of this ListScalingInstancesRequest.


        :return: The health_status of this ListScalingInstancesRequest.
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        """Sets the health_status of this ListScalingInstancesRequest.


        :param health_status: The health_status of this ListScalingInstancesRequest.
        :type: str
        """
        self._health_status = health_status

    @property
    def protect_from_scaling_down(self):
        """Gets the protect_from_scaling_down of this ListScalingInstancesRequest.


        :return: The protect_from_scaling_down of this ListScalingInstancesRequest.
        :rtype: str
        """
        return self._protect_from_scaling_down

    @protect_from_scaling_down.setter
    def protect_from_scaling_down(self, protect_from_scaling_down):
        """Sets the protect_from_scaling_down of this ListScalingInstancesRequest.


        :param protect_from_scaling_down: The protect_from_scaling_down of this ListScalingInstancesRequest.
        :type: str
        """
        self._protect_from_scaling_down = protect_from_scaling_down

    @property
    def start_number(self):
        """Gets the start_number of this ListScalingInstancesRequest.


        :return: The start_number of this ListScalingInstancesRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListScalingInstancesRequest.


        :param start_number: The start_number of this ListScalingInstancesRequest.
        :type: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListScalingInstancesRequest.


        :return: The limit of this ListScalingInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListScalingInstancesRequest.


        :param limit: The limit of this ListScalingInstancesRequest.
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
        if not isinstance(other, ListScalingInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
