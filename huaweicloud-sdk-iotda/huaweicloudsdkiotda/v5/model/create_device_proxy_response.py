# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDeviceProxyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy_id': 'str',
        'proxy_name': 'str',
        'proxy_devices': 'list[str]',
        'effective_time_range': 'EffectiveTimeRangeResponseDTO',
        'app_id': 'str'
    }

    attribute_map = {
        'proxy_id': 'proxy_id',
        'proxy_name': 'proxy_name',
        'proxy_devices': 'proxy_devices',
        'effective_time_range': 'effective_time_range',
        'app_id': 'app_id'
    }

    def __init__(self, proxy_id=None, proxy_name=None, proxy_devices=None, effective_time_range=None, app_id=None):
        r"""CreateDeviceProxyResponse

        The model defined in huaweicloud sdk

        :param proxy_id: **参数说明**：代理ID。用来唯一标识一个代理规则
        :type proxy_id: str
        :param proxy_name: **参数说明**：设备代理名称
        :type proxy_name: str
        :param proxy_devices: **参数说明**：代理设备组，组内所有设备共享网关权限，即组内任意一个网关下的子设备可以通过组里任意一个网关上线然后进行数据上报。
        :type proxy_devices: list[str]
        :param effective_time_range: 
        :type effective_time_range: :class:`huaweicloudsdkiotda.v5.EffectiveTimeRangeResponseDTO`
        :param app_id: **参数说明**：资源空间ID。
        :type app_id: str
        """
        
        super(CreateDeviceProxyResponse, self).__init__()

        self._proxy_id = None
        self._proxy_name = None
        self._proxy_devices = None
        self._effective_time_range = None
        self._app_id = None
        self.discriminator = None

        if proxy_id is not None:
            self.proxy_id = proxy_id
        if proxy_name is not None:
            self.proxy_name = proxy_name
        if proxy_devices is not None:
            self.proxy_devices = proxy_devices
        if effective_time_range is not None:
            self.effective_time_range = effective_time_range
        if app_id is not None:
            self.app_id = app_id

    @property
    def proxy_id(self):
        r"""Gets the proxy_id of this CreateDeviceProxyResponse.

        **参数说明**：代理ID。用来唯一标识一个代理规则

        :return: The proxy_id of this CreateDeviceProxyResponse.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        r"""Sets the proxy_id of this CreateDeviceProxyResponse.

        **参数说明**：代理ID。用来唯一标识一个代理规则

        :param proxy_id: The proxy_id of this CreateDeviceProxyResponse.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

    @property
    def proxy_name(self):
        r"""Gets the proxy_name of this CreateDeviceProxyResponse.

        **参数说明**：设备代理名称

        :return: The proxy_name of this CreateDeviceProxyResponse.
        :rtype: str
        """
        return self._proxy_name

    @proxy_name.setter
    def proxy_name(self, proxy_name):
        r"""Sets the proxy_name of this CreateDeviceProxyResponse.

        **参数说明**：设备代理名称

        :param proxy_name: The proxy_name of this CreateDeviceProxyResponse.
        :type proxy_name: str
        """
        self._proxy_name = proxy_name

    @property
    def proxy_devices(self):
        r"""Gets the proxy_devices of this CreateDeviceProxyResponse.

        **参数说明**：代理设备组，组内所有设备共享网关权限，即组内任意一个网关下的子设备可以通过组里任意一个网关上线然后进行数据上报。

        :return: The proxy_devices of this CreateDeviceProxyResponse.
        :rtype: list[str]
        """
        return self._proxy_devices

    @proxy_devices.setter
    def proxy_devices(self, proxy_devices):
        r"""Sets the proxy_devices of this CreateDeviceProxyResponse.

        **参数说明**：代理设备组，组内所有设备共享网关权限，即组内任意一个网关下的子设备可以通过组里任意一个网关上线然后进行数据上报。

        :param proxy_devices: The proxy_devices of this CreateDeviceProxyResponse.
        :type proxy_devices: list[str]
        """
        self._proxy_devices = proxy_devices

    @property
    def effective_time_range(self):
        r"""Gets the effective_time_range of this CreateDeviceProxyResponse.

        :return: The effective_time_range of this CreateDeviceProxyResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.EffectiveTimeRangeResponseDTO`
        """
        return self._effective_time_range

    @effective_time_range.setter
    def effective_time_range(self, effective_time_range):
        r"""Sets the effective_time_range of this CreateDeviceProxyResponse.

        :param effective_time_range: The effective_time_range of this CreateDeviceProxyResponse.
        :type effective_time_range: :class:`huaweicloudsdkiotda.v5.EffectiveTimeRangeResponseDTO`
        """
        self._effective_time_range = effective_time_range

    @property
    def app_id(self):
        r"""Gets the app_id of this CreateDeviceProxyResponse.

        **参数说明**：资源空间ID。

        :return: The app_id of this CreateDeviceProxyResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CreateDeviceProxyResponse.

        **参数说明**：资源空间ID。

        :param app_id: The app_id of this CreateDeviceProxyResponse.
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
        if not isinstance(other, CreateDeviceProxyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
