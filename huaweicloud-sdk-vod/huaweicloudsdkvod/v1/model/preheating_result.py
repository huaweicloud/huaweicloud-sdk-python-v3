# coding: utf-8

import pprint
import re

import six





class PreheatingResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'status': 'str'
    }

    attribute_map = {
        'url': 'url',
        'status': 'status'
    }

    def __init__(self, url=None, status=None):
        """PreheatingResult - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._status = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if status is not None:
            self.status = status

    @property
    def url(self):
        """Gets the url of this PreheatingResult.

        预热任务数组。<br/> 

        :return: The url of this PreheatingResult.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PreheatingResult.

        预热任务数组。<br/> 

        :param url: The url of this PreheatingResult.
        :type: str
        """
        self._url = url

    @property
    def status(self):
        """Gets the status of this PreheatingResult.

        预热任务状态，取值processing， succeed， failed，分别表示处理中，完成，失败。<br/> 

        :return: The status of this PreheatingResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PreheatingResult.

        预热任务状态，取值processing， succeed， failed，分别表示处理中，完成，失败。<br/> 

        :param status: The status of this PreheatingResult.
        :type: str
        """
        self._status = status

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
        if not isinstance(other, PreheatingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
