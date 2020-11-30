# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowTrafficResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'traffic_info': 'list[TrafficInfo]'
    }

    attribute_map = {
        'total': 'total',
        'traffic_info': 'traffic_info'
    }

    def __init__(self, total=None, traffic_info=None):
        """ShowTrafficResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total = None
        self._traffic_info = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if traffic_info is not None:
            self.traffic_info = traffic_info

    @property
    def total(self):
        """Gets the total of this ShowTrafficResponse.

        查询结果的总元素数量

        :return: The total of this ShowTrafficResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowTrafficResponse.

        查询结果的总元素数量

        :param total: The total of this ShowTrafficResponse.
        :type: int
        """
        self._total = total

    @property
    def traffic_info(self):
        """Gets the traffic_info of this ShowTrafficResponse.

        流量信息

        :return: The traffic_info of this ShowTrafficResponse.
        :rtype: list[TrafficInfo]
        """
        return self._traffic_info

    @traffic_info.setter
    def traffic_info(self, traffic_info):
        """Sets the traffic_info of this ShowTrafficResponse.

        流量信息

        :param traffic_info: The traffic_info of this ShowTrafficResponse.
        :type: list[TrafficInfo]
        """
        self._traffic_info = traffic_info

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
        if not isinstance(other, ShowTrafficResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
