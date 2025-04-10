# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAccessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_type': 'str',
        'domain_name': 'str',
        'public_addresses_enable': 'bool',
        'ip_whitelist': 'IPWhiteList'
    }

    attribute_map = {
        'access_type': 'access_type',
        'domain_name': 'domain_name',
        'public_addresses_enable': 'public_addresses_enable',
        'ip_whitelist': 'ip_whitelist'
    }

    def __init__(self, access_type=None, domain_name=None, public_addresses_enable=None, ip_whitelist=None):
        r"""UpdateAccessInfo

        The model defined in huaweicloud sdk

        :param access_type: **参数说明**：接入地址的类型，如应用接入的HTTPS协议的取值为：APP_HTTPS，设备接入的MQTT协议的取值为：DEVICE_MQTT **取值范围**： - APP_HTTPS：应用接入HTTPS协议 - APP_AMQP：应用接入AMQP协议 - APP_MQTT：应用接入MQTT协议 - DEVICE_COAP：设备接入COAP协议 - DEVICE_MQTT：设备接入MQTT协议 - DEVICE_HTTPS：设备接入HTTPS协议 
        :type access_type: str
        :param domain_name: **参数说明**：接入域名，如果需要更新域名，则携带该字段。 
        :type domain_name: str
        :param public_addresses_enable: **参数说明**：是否配置公网接入地址，true，false **取值范围**： - true：配置公网接入地址，平台将自动分配公网接入地址。约束：分配地址后将不能修改或删除。 
        :type public_addresses_enable: bool
        :param ip_whitelist: 
        :type ip_whitelist: :class:`huaweicloudsdkiotdm.v5.IPWhiteList`
        """
        
        

        self._access_type = None
        self._domain_name = None
        self._public_addresses_enable = None
        self._ip_whitelist = None
        self.discriminator = None

        self.access_type = access_type
        if domain_name is not None:
            self.domain_name = domain_name
        if public_addresses_enable is not None:
            self.public_addresses_enable = public_addresses_enable
        if ip_whitelist is not None:
            self.ip_whitelist = ip_whitelist

    @property
    def access_type(self):
        r"""Gets the access_type of this UpdateAccessInfo.

        **参数说明**：接入地址的类型，如应用接入的HTTPS协议的取值为：APP_HTTPS，设备接入的MQTT协议的取值为：DEVICE_MQTT **取值范围**： - APP_HTTPS：应用接入HTTPS协议 - APP_AMQP：应用接入AMQP协议 - APP_MQTT：应用接入MQTT协议 - DEVICE_COAP：设备接入COAP协议 - DEVICE_MQTT：设备接入MQTT协议 - DEVICE_HTTPS：设备接入HTTPS协议 

        :return: The access_type of this UpdateAccessInfo.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        r"""Sets the access_type of this UpdateAccessInfo.

        **参数说明**：接入地址的类型，如应用接入的HTTPS协议的取值为：APP_HTTPS，设备接入的MQTT协议的取值为：DEVICE_MQTT **取值范围**： - APP_HTTPS：应用接入HTTPS协议 - APP_AMQP：应用接入AMQP协议 - APP_MQTT：应用接入MQTT协议 - DEVICE_COAP：设备接入COAP协议 - DEVICE_MQTT：设备接入MQTT协议 - DEVICE_HTTPS：设备接入HTTPS协议 

        :param access_type: The access_type of this UpdateAccessInfo.
        :type access_type: str
        """
        self._access_type = access_type

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UpdateAccessInfo.

        **参数说明**：接入域名，如果需要更新域名，则携带该字段。 

        :return: The domain_name of this UpdateAccessInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UpdateAccessInfo.

        **参数说明**：接入域名，如果需要更新域名，则携带该字段。 

        :param domain_name: The domain_name of this UpdateAccessInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def public_addresses_enable(self):
        r"""Gets the public_addresses_enable of this UpdateAccessInfo.

        **参数说明**：是否配置公网接入地址，true，false **取值范围**： - true：配置公网接入地址，平台将自动分配公网接入地址。约束：分配地址后将不能修改或删除。 

        :return: The public_addresses_enable of this UpdateAccessInfo.
        :rtype: bool
        """
        return self._public_addresses_enable

    @public_addresses_enable.setter
    def public_addresses_enable(self, public_addresses_enable):
        r"""Sets the public_addresses_enable of this UpdateAccessInfo.

        **参数说明**：是否配置公网接入地址，true，false **取值范围**： - true：配置公网接入地址，平台将自动分配公网接入地址。约束：分配地址后将不能修改或删除。 

        :param public_addresses_enable: The public_addresses_enable of this UpdateAccessInfo.
        :type public_addresses_enable: bool
        """
        self._public_addresses_enable = public_addresses_enable

    @property
    def ip_whitelist(self):
        r"""Gets the ip_whitelist of this UpdateAccessInfo.

        :return: The ip_whitelist of this UpdateAccessInfo.
        :rtype: :class:`huaweicloudsdkiotdm.v5.IPWhiteList`
        """
        return self._ip_whitelist

    @ip_whitelist.setter
    def ip_whitelist(self, ip_whitelist):
        r"""Sets the ip_whitelist of this UpdateAccessInfo.

        :param ip_whitelist: The ip_whitelist of this UpdateAccessInfo.
        :type ip_whitelist: :class:`huaweicloudsdkiotdm.v5.IPWhiteList`
        """
        self._ip_whitelist = ip_whitelist

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
        if not isinstance(other, UpdateAccessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
