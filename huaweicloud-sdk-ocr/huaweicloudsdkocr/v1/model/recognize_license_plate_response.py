# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class RecognizeLicensePlateResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'result': 'LicensePlateResponseBodyItem'
    }

    attribute_map = {
        'result': 'result'
    }

    def __init__(self, result=None):
        """RecognizeLicensePlateResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._result = None
        self.discriminator = None

        if result is not None:
            self.result = result

    @property
    def result(self):
        """Gets the result of this RecognizeLicensePlateResponse.


        :return: The result of this RecognizeLicensePlateResponse.
        :rtype: LicensePlateResponseBodyItem
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RecognizeLicensePlateResponse.


        :param result: The result of this RecognizeLicensePlateResponse.
        :type: LicensePlateResponseBodyItem
        """
        self._result = result

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
        if not isinstance(other, RecognizeLicensePlateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
