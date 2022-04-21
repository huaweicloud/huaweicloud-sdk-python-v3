# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevicesCalculation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'normal_devices': 'Calculation',
        'gateway_devices': 'Calculation',
        'subsets_devices': 'Calculation'
    }

    attribute_map = {
        'normal_devices': 'normal_devices',
        'gateway_devices': 'gateway_devices',
        'subsets_devices': 'subsets_devices'
    }

    def __init__(self, normal_devices=None, gateway_devices=None, subsets_devices=None):
        """DevicesCalculation

        The model defined in huaweicloud sdk

        :param normal_devices: 
        :type normal_devices: :class:`huaweicloudsdkroma.v2.Calculation`
        :param gateway_devices: 
        :type gateway_devices: :class:`huaweicloudsdkroma.v2.Calculation`
        :param subsets_devices: 
        :type subsets_devices: :class:`huaweicloudsdkroma.v2.Calculation`
        """
        
        

        self._normal_devices = None
        self._gateway_devices = None
        self._subsets_devices = None
        self.discriminator = None

        if normal_devices is not None:
            self.normal_devices = normal_devices
        if gateway_devices is not None:
            self.gateway_devices = gateway_devices
        if subsets_devices is not None:
            self.subsets_devices = subsets_devices

    @property
    def normal_devices(self):
        """Gets the normal_devices of this DevicesCalculation.


        :return: The normal_devices of this DevicesCalculation.
        :rtype: :class:`huaweicloudsdkroma.v2.Calculation`
        """
        return self._normal_devices

    @normal_devices.setter
    def normal_devices(self, normal_devices):
        """Sets the normal_devices of this DevicesCalculation.


        :param normal_devices: The normal_devices of this DevicesCalculation.
        :type normal_devices: :class:`huaweicloudsdkroma.v2.Calculation`
        """
        self._normal_devices = normal_devices

    @property
    def gateway_devices(self):
        """Gets the gateway_devices of this DevicesCalculation.


        :return: The gateway_devices of this DevicesCalculation.
        :rtype: :class:`huaweicloudsdkroma.v2.Calculation`
        """
        return self._gateway_devices

    @gateway_devices.setter
    def gateway_devices(self, gateway_devices):
        """Sets the gateway_devices of this DevicesCalculation.


        :param gateway_devices: The gateway_devices of this DevicesCalculation.
        :type gateway_devices: :class:`huaweicloudsdkroma.v2.Calculation`
        """
        self._gateway_devices = gateway_devices

    @property
    def subsets_devices(self):
        """Gets the subsets_devices of this DevicesCalculation.


        :return: The subsets_devices of this DevicesCalculation.
        :rtype: :class:`huaweicloudsdkroma.v2.Calculation`
        """
        return self._subsets_devices

    @subsets_devices.setter
    def subsets_devices(self, subsets_devices):
        """Sets the subsets_devices of this DevicesCalculation.


        :param subsets_devices: The subsets_devices of this DevicesCalculation.
        :type subsets_devices: :class:`huaweicloudsdkroma.v2.Calculation`
        """
        self._subsets_devices = subsets_devices

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
        if not isinstance(other, DevicesCalculation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
