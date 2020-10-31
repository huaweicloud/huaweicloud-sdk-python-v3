# coding: utf-8

import pprint
import re

import six





class CreateIterationRequestV4:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'begin_time': 'str',
        'description': 'str',
        'end_time': 'str',
        'name': 'str'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'description': 'description',
        'end_time': 'end_time',
        'name': 'name'
    }

    def __init__(self, begin_time=None, description=None, end_time=None, name=None):
        """CreateIterationRequestV4 - a model defined in huaweicloud sdk"""
        
        

        self._begin_time = None
        self._description = None
        self._end_time = None
        self._name = None
        self.discriminator = None

        self.begin_time = begin_time
        if description is not None:
            self.description = description
        self.end_time = end_time
        self.name = name

    @property
    def begin_time(self):
        """Gets the begin_time of this CreateIterationRequestV4.

        开始时间，年-月-日

        :return: The begin_time of this CreateIterationRequestV4.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this CreateIterationRequestV4.

        开始时间，年-月-日

        :param begin_time: The begin_time of this CreateIterationRequestV4.
        :type: str
        """
        self._begin_time = begin_time

    @property
    def description(self):
        """Gets the description of this CreateIterationRequestV4.

        描述

        :return: The description of this CreateIterationRequestV4.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateIterationRequestV4.

        描述

        :param description: The description of this CreateIterationRequestV4.
        :type: str
        """
        self._description = description

    @property
    def end_time(self):
        """Gets the end_time of this CreateIterationRequestV4.

        结束时间，年-月-日

        :return: The end_time of this CreateIterationRequestV4.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CreateIterationRequestV4.

        结束时间，年-月-日

        :param end_time: The end_time of this CreateIterationRequestV4.
        :type: str
        """
        self._end_time = end_time

    @property
    def name(self):
        """Gets the name of this CreateIterationRequestV4.

        标题

        :return: The name of this CreateIterationRequestV4.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateIterationRequestV4.

        标题

        :param name: The name of this CreateIterationRequestV4.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, CreateIterationRequestV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
