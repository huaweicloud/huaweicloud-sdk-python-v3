# coding: utf-8

import pprint
import re

import six





class Schedule:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sche_type': 'str',
        'cron': 'Cron',
        'event': 'Event'
    }

    attribute_map = {
        'sche_type': 'scheType',
        'cron': 'cron',
        'event': 'event'
    }

    def __init__(self, sche_type=None, cron=None, event=None):
        """Schedule - a model defined in huaweicloud sdk"""
        
        

        self._sche_type = None
        self._cron = None
        self._event = None
        self.discriminator = None

        if sche_type is not None:
            self.sche_type = sche_type
        if cron is not None:
            self.cron = cron
        if event is not None:
            self.event = event

    @property
    def sche_type(self):
        """Gets the sche_type of this Schedule.


        :return: The sche_type of this Schedule.
        :rtype: str
        """
        return self._sche_type

    @sche_type.setter
    def sche_type(self, sche_type):
        """Sets the sche_type of this Schedule.


        :param sche_type: The sche_type of this Schedule.
        :type: str
        """
        self._sche_type = sche_type

    @property
    def cron(self):
        """Gets the cron of this Schedule.


        :return: The cron of this Schedule.
        :rtype: Cron
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this Schedule.


        :param cron: The cron of this Schedule.
        :type: Cron
        """
        self._cron = cron

    @property
    def event(self):
        """Gets the event of this Schedule.


        :return: The event of this Schedule.
        :rtype: Event
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this Schedule.


        :param event: The event of this Schedule.
        :type: Event
        """
        self._event = event

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
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
