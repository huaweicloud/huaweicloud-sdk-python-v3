# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevicePropertiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'services': 'object'
    }

    attribute_map = {
        'services': 'services'
    }

    def __init__(self, services=None):
        """DevicePropertiesRequest

        The model defined in huaweicloud sdk

        :param services: **参数说明**：设备执行的属性，Json格式，里面是一个个健值对，如果serviceId不为空，每个健都是profile中属性的参数名（paraName）;如果serviceId为空则由用户自定义属性格式。设属性令示例：[{\&quot;service_id\&quot;: \&quot;Temperature\&quot;,\&quot;properties\&quot;: {\&quot;value\&quot;: 57}},{\&quot;service_id\&quot;: \&quot;Battery\&quot;,\&quot;properties\&quot;: {\&quot;level\&quot;: 80}}]，具体格式需要应用和设备约定。
        :type services: object
        """
        
        

        self._services = None
        self.discriminator = None

        if services is not None:
            self.services = services

    @property
    def services(self):
        """Gets the services of this DevicePropertiesRequest.

        **参数说明**：设备执行的属性，Json格式，里面是一个个健值对，如果serviceId不为空，每个健都是profile中属性的参数名（paraName）;如果serviceId为空则由用户自定义属性格式。设属性令示例：[{\"service_id\": \"Temperature\",\"properties\": {\"value\": 57}},{\"service_id\": \"Battery\",\"properties\": {\"level\": 80}}]，具体格式需要应用和设备约定。

        :return: The services of this DevicePropertiesRequest.
        :rtype: object
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this DevicePropertiesRequest.

        **参数说明**：设备执行的属性，Json格式，里面是一个个健值对，如果serviceId不为空，每个健都是profile中属性的参数名（paraName）;如果serviceId为空则由用户自定义属性格式。设属性令示例：[{\"service_id\": \"Temperature\",\"properties\": {\"value\": 57}},{\"service_id\": \"Battery\",\"properties\": {\"level\": 80}}]，具体格式需要应用和设备约定。

        :param services: The services of this DevicePropertiesRequest.
        :type services: object
        """
        self._services = services

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
        if not isinstance(other, DevicePropertiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
