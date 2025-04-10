# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDeviceProxy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy_name': 'str',
        'proxy_devices': 'list[str]',
        'effective_time_range': 'EffectiveTimeRange',
        'app_id': 'str'
    }

    attribute_map = {
        'proxy_name': 'proxy_name',
        'proxy_devices': 'proxy_devices',
        'effective_time_range': 'effective_time_range',
        'app_id': 'app_id'
    }

    def __init__(self, proxy_name=None, proxy_devices=None, effective_time_range=None, app_id=None):
        r"""AddDeviceProxy

        The model defined in huaweicloud sdk

        :param proxy_name: **参数说明**：设备代理名称
        :type proxy_name: str
        :param proxy_devices: **参数说明**：代理设备列表，列表内所有设备共享网关权限，即列表内任意一个网关下的子设备可以通过组里任意一个网关上线然后进行数据上报。 **取值范围**：列表内填写设备id，列表内最少有2个设备id，最多有10个设备id，设备id取值范围：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合，建议不少于4个字符。
        :type proxy_devices: list[str]
        :param effective_time_range: 
        :type effective_time_range: :class:`huaweicloudsdkiotda.v5.EffectiveTimeRange`
        :param app_id: **参数说明**：资源空间ID。携带该参数指定创建的设备归属到哪个资源空间下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        """
        
        

        self._proxy_name = None
        self._proxy_devices = None
        self._effective_time_range = None
        self._app_id = None
        self.discriminator = None

        self.proxy_name = proxy_name
        self.proxy_devices = proxy_devices
        self.effective_time_range = effective_time_range
        self.app_id = app_id

    @property
    def proxy_name(self):
        r"""Gets the proxy_name of this AddDeviceProxy.

        **参数说明**：设备代理名称

        :return: The proxy_name of this AddDeviceProxy.
        :rtype: str
        """
        return self._proxy_name

    @proxy_name.setter
    def proxy_name(self, proxy_name):
        r"""Sets the proxy_name of this AddDeviceProxy.

        **参数说明**：设备代理名称

        :param proxy_name: The proxy_name of this AddDeviceProxy.
        :type proxy_name: str
        """
        self._proxy_name = proxy_name

    @property
    def proxy_devices(self):
        r"""Gets the proxy_devices of this AddDeviceProxy.

        **参数说明**：代理设备列表，列表内所有设备共享网关权限，即列表内任意一个网关下的子设备可以通过组里任意一个网关上线然后进行数据上报。 **取值范围**：列表内填写设备id，列表内最少有2个设备id，最多有10个设备id，设备id取值范围：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合，建议不少于4个字符。

        :return: The proxy_devices of this AddDeviceProxy.
        :rtype: list[str]
        """
        return self._proxy_devices

    @proxy_devices.setter
    def proxy_devices(self, proxy_devices):
        r"""Sets the proxy_devices of this AddDeviceProxy.

        **参数说明**：代理设备列表，列表内所有设备共享网关权限，即列表内任意一个网关下的子设备可以通过组里任意一个网关上线然后进行数据上报。 **取值范围**：列表内填写设备id，列表内最少有2个设备id，最多有10个设备id，设备id取值范围：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合，建议不少于4个字符。

        :param proxy_devices: The proxy_devices of this AddDeviceProxy.
        :type proxy_devices: list[str]
        """
        self._proxy_devices = proxy_devices

    @property
    def effective_time_range(self):
        r"""Gets the effective_time_range of this AddDeviceProxy.

        :return: The effective_time_range of this AddDeviceProxy.
        :rtype: :class:`huaweicloudsdkiotda.v5.EffectiveTimeRange`
        """
        return self._effective_time_range

    @effective_time_range.setter
    def effective_time_range(self, effective_time_range):
        r"""Sets the effective_time_range of this AddDeviceProxy.

        :param effective_time_range: The effective_time_range of this AddDeviceProxy.
        :type effective_time_range: :class:`huaweicloudsdkiotda.v5.EffectiveTimeRange`
        """
        self._effective_time_range = effective_time_range

    @property
    def app_id(self):
        r"""Gets the app_id of this AddDeviceProxy.

        **参数说明**：资源空间ID。携带该参数指定创建的设备归属到哪个资源空间下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this AddDeviceProxy.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this AddDeviceProxy.

        **参数说明**：资源空间ID。携带该参数指定创建的设备归属到哪个资源空间下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this AddDeviceProxy.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, AddDeviceProxy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
