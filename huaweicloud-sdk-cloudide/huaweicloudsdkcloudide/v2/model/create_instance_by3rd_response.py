# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateInstanceBy3rdResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'result': 'InstancesResponseInstancesVOResult',
        'status': 'str'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status'
    }

    def __init__(self, result=None, status=None):
        """CreateInstanceBy3rdResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._result = None
        self._status = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if status is not None:
            self.status = status

    @property
    def result(self):
        """Gets the result of this CreateInstanceBy3rdResponse.


        :return: The result of this CreateInstanceBy3rdResponse.
        :rtype: InstancesResponseInstancesVOResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CreateInstanceBy3rdResponse.


        :param result: The result of this CreateInstanceBy3rdResponse.
        :type: InstancesResponseInstancesVOResult
        """
        self._result = result

    @property
    def status(self):
        """Gets the status of this CreateInstanceBy3rdResponse.

        状态

        :return: The status of this CreateInstanceBy3rdResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateInstanceBy3rdResponse.

        状态

        :param status: The status of this CreateInstanceBy3rdResponse.
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
        if not isinstance(other, CreateInstanceBy3rdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
