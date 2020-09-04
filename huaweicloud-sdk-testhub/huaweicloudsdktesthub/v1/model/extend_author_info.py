# coding: utf-8

import pprint
import re

import six





class ExtendAuthorInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'time': 'time'
    }

    def __init__(self, id=None, name=None, time=None):
        """ExtendAuthorInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if time is not None:
            self.time = time

    @property
    def id(self):
        """Gets the id of this ExtendAuthorInfo.

        id信息

        :return: The id of this ExtendAuthorInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExtendAuthorInfo.

        id信息

        :param id: The id of this ExtendAuthorInfo.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ExtendAuthorInfo.

        名称信息

        :return: The name of this ExtendAuthorInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExtendAuthorInfo.

        名称信息

        :param name: The name of this ExtendAuthorInfo.
        :type: str
        """
        self._name = name

    @property
    def time(self):
        """Gets the time of this ExtendAuthorInfo.

        时间信息

        :return: The time of this ExtendAuthorInfo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ExtendAuthorInfo.

        时间信息

        :param time: The time of this ExtendAuthorInfo.
        :type: str
        """
        self._time = time

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
        if not isinstance(other, ExtendAuthorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
