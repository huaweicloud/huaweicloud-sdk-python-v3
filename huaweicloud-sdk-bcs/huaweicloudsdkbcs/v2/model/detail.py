# coding: utf-8

import pprint
import re

import six





class Detail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'detail': 'detail'
    }

    def __init__(self, start_time=None, end_time=None, status=None, detail=None):
        """Detail - a model defined in huaweicloud sdk"""
        
        

        self._start_time = None
        self._end_time = None
        self._status = None
        self._detail = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail

    @property
    def start_time(self):
        """Gets the start_time of this Detail.

        开始时间

        :return: The start_time of this Detail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Detail.

        开始时间

        :param start_time: The start_time of this Detail.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Detail.

        结束时间

        :return: The end_time of this Detail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Detail.

        结束时间

        :param end_time: The end_time of this Detail.
        :type: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this Detail.

        状态

        :return: The status of this Detail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Detail.

        状态

        :param status: The status of this Detail.
        :type: str
        """
        self._status = status

    @property
    def detail(self):
        """Gets the detail of this Detail.

        细节描述

        :return: The detail of this Detail.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Detail.

        细节描述

        :param detail: The detail of this Detail.
        :type: str
        """
        self._detail = detail

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
        if not isinstance(other, Detail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
