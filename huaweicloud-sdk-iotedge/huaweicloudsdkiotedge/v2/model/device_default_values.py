# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceDefaultValues:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'service_id': 'str',
        'properties': 'object'
    }

    attribute_map = {
        'device_id': 'device_id',
        'service_id': 'service_id',
        'properties': 'properties'
    }

    def __init__(self, device_id=None, service_id=None, properties=None):
        r"""DeviceDefaultValues

        The model defined in huaweicloud sdk

        :param device_id: 设备ID
        :type device_id: str
        :param service_id: 服务id，可选
        :type service_id: str
        :param properties: 属性key和value的map，用于设置属性的值
        :type properties: object
        """
        
        

        self._device_id = None
        self._service_id = None
        self._properties = None
        self.discriminator = None

        self.device_id = device_id
        if service_id is not None:
            self.service_id = service_id
        self.properties = properties

    @property
    def device_id(self):
        r"""Gets the device_id of this DeviceDefaultValues.

        设备ID

        :return: The device_id of this DeviceDefaultValues.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this DeviceDefaultValues.

        设备ID

        :param device_id: The device_id of this DeviceDefaultValues.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def service_id(self):
        r"""Gets the service_id of this DeviceDefaultValues.

        服务id，可选

        :return: The service_id of this DeviceDefaultValues.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this DeviceDefaultValues.

        服务id，可选

        :param service_id: The service_id of this DeviceDefaultValues.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def properties(self):
        r"""Gets the properties of this DeviceDefaultValues.

        属性key和value的map，用于设置属性的值

        :return: The properties of this DeviceDefaultValues.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this DeviceDefaultValues.

        属性key和value的map，用于设置属性的值

        :param properties: The properties of this DeviceDefaultValues.
        :type properties: object
        """
        self._properties = properties

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
        if not isinstance(other, DeviceDefaultValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
