# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowUpBandwidthResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'data_list': 'list[V2BandwidthData]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'data_list': 'data_list',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, data_list=None, x_request_id=None):
        """ShowUpBandwidthResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._data_list = None
        self._x_request_id = None
        self.discriminator = None

        if data_list is not None:
            self.data_list = data_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def data_list(self):
        """Gets the data_list of this ShowUpBandwidthResponse.

        采样数据列表

        :return: The data_list of this ShowUpBandwidthResponse.
        :rtype: list[V2BandwidthData]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        """Sets the data_list of this ShowUpBandwidthResponse.

        采样数据列表

        :param data_list: The data_list of this ShowUpBandwidthResponse.
        :type: list[V2BandwidthData]
        """
        self._data_list = data_list

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowUpBandwidthResponse.


        :return: The x_request_id of this ShowUpBandwidthResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowUpBandwidthResponse.


        :param x_request_id: The x_request_id of this ShowUpBandwidthResponse.
        :type: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowUpBandwidthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
