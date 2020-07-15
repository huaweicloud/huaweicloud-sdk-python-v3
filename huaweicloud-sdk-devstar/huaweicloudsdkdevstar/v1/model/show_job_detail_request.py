# coding: utf-8

import pprint
import re

import six





class ShowJobDetailRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_id': 'job_id'
    }

    def __init__(self, x_language='zh-cn', job_id=None):
        """ShowJobDetailRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._job_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_id = job_id

    @property
    def x_language(self):
        """Gets the x_language of this ShowJobDetailRequest.


        :return: The x_language of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowJobDetailRequest.


        :param x_language: The x_language of this ShowJobDetailRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobDetailRequest.


        :return: The job_id of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobDetailRequest.


        :param job_id: The job_id of this ShowJobDetailRequest.
        :type: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ShowJobDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
