# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowHealthMonitorResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'healthmonitor': 'HealthMonitor'
    }

    attribute_map = {
        'request_id': 'request_id',
        'healthmonitor': 'healthmonitor'
    }

    def __init__(self, request_id=None, healthmonitor=None):
        """ShowHealthMonitorResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._request_id = None
        self._healthmonitor = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if healthmonitor is not None:
            self.healthmonitor = healthmonitor

    @property
    def request_id(self):
        """Gets the request_id of this ShowHealthMonitorResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this ShowHealthMonitorResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowHealthMonitorResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this ShowHealthMonitorResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def healthmonitor(self):
        """Gets the healthmonitor of this ShowHealthMonitorResponse.


        :return: The healthmonitor of this ShowHealthMonitorResponse.
        :rtype: HealthMonitor
        """
        return self._healthmonitor

    @healthmonitor.setter
    def healthmonitor(self, healthmonitor):
        """Sets the healthmonitor of this ShowHealthMonitorResponse.


        :param healthmonitor: The healthmonitor of this ShowHealthMonitorResponse.
        :type: HealthMonitor
        """
        self._healthmonitor = healthmonitor

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
        if not isinstance(other, ShowHealthMonitorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
