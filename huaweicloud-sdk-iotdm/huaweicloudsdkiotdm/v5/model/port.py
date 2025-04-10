# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Port:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_https_port': 'int',
        'app_amqps_port': 'int',
        'device_coap_port': 'int',
        'device_coaps_port': 'int',
        'device_mqtt_port': 'int',
        'device_mqtts_port': 'int',
        'device_https_port': 'int'
    }

    attribute_map = {
        'app_https_port': 'app_https_port',
        'app_amqps_port': 'app_amqps_port',
        'device_coap_port': 'device_coap_port',
        'device_coaps_port': 'device_coaps_port',
        'device_mqtt_port': 'device_mqtt_port',
        'device_mqtts_port': 'device_mqtts_port',
        'device_https_port': 'device_https_port'
    }

    def __init__(self, app_https_port=None, app_amqps_port=None, device_coap_port=None, device_coaps_port=None, device_mqtt_port=None, device_mqtts_port=None, device_https_port=None):
        r"""Port

        The model defined in huaweicloud sdk

        :param app_https_port: **参数说明**：应用接入HTTPS协议端口，默认值：443 
        :type app_https_port: int
        :param app_amqps_port: **参数说明**：应用接入AMQP协议端口, 默认值：5671 
        :type app_amqps_port: int
        :param device_coap_port: **参数说明**：设备接入COAP协议端口, 默认值：5683 
        :type device_coap_port: int
        :param device_coaps_port: **参数说明**：设备接入COAPS协议端口, 默认值：5684 
        :type device_coaps_port: int
        :param device_mqtt_port: **参数说明**：设备接入MQTT协议端口, 默认值：1883 
        :type device_mqtt_port: int
        :param device_mqtts_port: **参数说明**：设备接入MQTTS协议端口, 默认值：8883 
        :type device_mqtts_port: int
        :param device_https_port: **参数说明**：设备接入HTTPS协议端口, 默认值：443 
        :type device_https_port: int
        """
        
        

        self._app_https_port = None
        self._app_amqps_port = None
        self._device_coap_port = None
        self._device_coaps_port = None
        self._device_mqtt_port = None
        self._device_mqtts_port = None
        self._device_https_port = None
        self.discriminator = None

        if app_https_port is not None:
            self.app_https_port = app_https_port
        if app_amqps_port is not None:
            self.app_amqps_port = app_amqps_port
        if device_coap_port is not None:
            self.device_coap_port = device_coap_port
        if device_coaps_port is not None:
            self.device_coaps_port = device_coaps_port
        if device_mqtt_port is not None:
            self.device_mqtt_port = device_mqtt_port
        if device_mqtts_port is not None:
            self.device_mqtts_port = device_mqtts_port
        if device_https_port is not None:
            self.device_https_port = device_https_port

    @property
    def app_https_port(self):
        r"""Gets the app_https_port of this Port.

        **参数说明**：应用接入HTTPS协议端口，默认值：443 

        :return: The app_https_port of this Port.
        :rtype: int
        """
        return self._app_https_port

    @app_https_port.setter
    def app_https_port(self, app_https_port):
        r"""Sets the app_https_port of this Port.

        **参数说明**：应用接入HTTPS协议端口，默认值：443 

        :param app_https_port: The app_https_port of this Port.
        :type app_https_port: int
        """
        self._app_https_port = app_https_port

    @property
    def app_amqps_port(self):
        r"""Gets the app_amqps_port of this Port.

        **参数说明**：应用接入AMQP协议端口, 默认值：5671 

        :return: The app_amqps_port of this Port.
        :rtype: int
        """
        return self._app_amqps_port

    @app_amqps_port.setter
    def app_amqps_port(self, app_amqps_port):
        r"""Sets the app_amqps_port of this Port.

        **参数说明**：应用接入AMQP协议端口, 默认值：5671 

        :param app_amqps_port: The app_amqps_port of this Port.
        :type app_amqps_port: int
        """
        self._app_amqps_port = app_amqps_port

    @property
    def device_coap_port(self):
        r"""Gets the device_coap_port of this Port.

        **参数说明**：设备接入COAP协议端口, 默认值：5683 

        :return: The device_coap_port of this Port.
        :rtype: int
        """
        return self._device_coap_port

    @device_coap_port.setter
    def device_coap_port(self, device_coap_port):
        r"""Sets the device_coap_port of this Port.

        **参数说明**：设备接入COAP协议端口, 默认值：5683 

        :param device_coap_port: The device_coap_port of this Port.
        :type device_coap_port: int
        """
        self._device_coap_port = device_coap_port

    @property
    def device_coaps_port(self):
        r"""Gets the device_coaps_port of this Port.

        **参数说明**：设备接入COAPS协议端口, 默认值：5684 

        :return: The device_coaps_port of this Port.
        :rtype: int
        """
        return self._device_coaps_port

    @device_coaps_port.setter
    def device_coaps_port(self, device_coaps_port):
        r"""Sets the device_coaps_port of this Port.

        **参数说明**：设备接入COAPS协议端口, 默认值：5684 

        :param device_coaps_port: The device_coaps_port of this Port.
        :type device_coaps_port: int
        """
        self._device_coaps_port = device_coaps_port

    @property
    def device_mqtt_port(self):
        r"""Gets the device_mqtt_port of this Port.

        **参数说明**：设备接入MQTT协议端口, 默认值：1883 

        :return: The device_mqtt_port of this Port.
        :rtype: int
        """
        return self._device_mqtt_port

    @device_mqtt_port.setter
    def device_mqtt_port(self, device_mqtt_port):
        r"""Sets the device_mqtt_port of this Port.

        **参数说明**：设备接入MQTT协议端口, 默认值：1883 

        :param device_mqtt_port: The device_mqtt_port of this Port.
        :type device_mqtt_port: int
        """
        self._device_mqtt_port = device_mqtt_port

    @property
    def device_mqtts_port(self):
        r"""Gets the device_mqtts_port of this Port.

        **参数说明**：设备接入MQTTS协议端口, 默认值：8883 

        :return: The device_mqtts_port of this Port.
        :rtype: int
        """
        return self._device_mqtts_port

    @device_mqtts_port.setter
    def device_mqtts_port(self, device_mqtts_port):
        r"""Sets the device_mqtts_port of this Port.

        **参数说明**：设备接入MQTTS协议端口, 默认值：8883 

        :param device_mqtts_port: The device_mqtts_port of this Port.
        :type device_mqtts_port: int
        """
        self._device_mqtts_port = device_mqtts_port

    @property
    def device_https_port(self):
        r"""Gets the device_https_port of this Port.

        **参数说明**：设备接入HTTPS协议端口, 默认值：443 

        :return: The device_https_port of this Port.
        :rtype: int
        """
        return self._device_https_port

    @device_https_port.setter
    def device_https_port(self, device_https_port):
        r"""Sets the device_https_port of this Port.

        **参数说明**：设备接入HTTPS协议端口, 默认值：443 

        :param device_https_port: The device_https_port of this Port.
        :type device_https_port: int
        """
        self._device_https_port = device_https_port

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
        if not isinstance(other, Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
