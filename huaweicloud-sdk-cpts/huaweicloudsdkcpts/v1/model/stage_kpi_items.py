# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StageKpiItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'average_response_time': 'StageKpiItem',
        'success_rate': 'StageKpiItem'
    }

    attribute_map = {
        'average_response_time': 'average_response_time',
        'success_rate': 'success_rate'
    }

    def __init__(self, average_response_time=None, success_rate=None):
        """StageKpiItems

        The model defined in huaweicloud sdk

        :param average_response_time: 
        :type average_response_time: :class:`huaweicloudsdkcpts.v1.StageKpiItem`
        :param success_rate: 
        :type success_rate: :class:`huaweicloudsdkcpts.v1.StageKpiItem`
        """
        
        

        self._average_response_time = None
        self._success_rate = None
        self.discriminator = None

        if average_response_time is not None:
            self.average_response_time = average_response_time
        if success_rate is not None:
            self.success_rate = success_rate

    @property
    def average_response_time(self):
        """Gets the average_response_time of this StageKpiItems.


        :return: The average_response_time of this StageKpiItems.
        :rtype: :class:`huaweicloudsdkcpts.v1.StageKpiItem`
        """
        return self._average_response_time

    @average_response_time.setter
    def average_response_time(self, average_response_time):
        """Sets the average_response_time of this StageKpiItems.


        :param average_response_time: The average_response_time of this StageKpiItems.
        :type average_response_time: :class:`huaweicloudsdkcpts.v1.StageKpiItem`
        """
        self._average_response_time = average_response_time

    @property
    def success_rate(self):
        """Gets the success_rate of this StageKpiItems.


        :return: The success_rate of this StageKpiItems.
        :rtype: :class:`huaweicloudsdkcpts.v1.StageKpiItem`
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this StageKpiItems.


        :param success_rate: The success_rate of this StageKpiItems.
        :type success_rate: :class:`huaweicloudsdkcpts.v1.StageKpiItem`
        """
        self._success_rate = success_rate

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StageKpiItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
