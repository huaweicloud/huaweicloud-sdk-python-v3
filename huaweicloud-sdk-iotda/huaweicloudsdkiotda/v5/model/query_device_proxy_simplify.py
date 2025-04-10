# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDeviceProxySimplify:

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
        'effective_time_range': 'EffectiveTimeRangeResponseDTO',
        'app_id': 'str'
    }

    attribute_map = {
        'proxy_id': 'proxy_id',
        'proxy_name': 'proxy_name',
        'effective_time_range': 'effective_time_range',
        'app_id': 'app_id'
    }

    def __init__(self, proxy_id=None, proxy_name=None, effective_time_range=None, app_id=None):
        r"""QueryDeviceProxySimplify

        The model defined in huaweicloud sdk

        :param proxy_id: **参数说明**：代理ID。用来唯一标识一个代理规则
        :type proxy_id: str
        :param proxy_name: **参数说明**：设备代理名称
        :type proxy_name: str
        :param effective_time_range: 
        :type effective_time_range: :class:`huaweicloudsdkiotda.v5.EffectiveTimeRangeResponseDTO`
        :param app_id: **参数说明**：资源空间ID。
        :type app_id: str
        """
        
        

        self._proxy_id = None
        self._proxy_name = None
        self._effective_time_range = None
        self._app_id = None
        self.discriminator = None

        if proxy_id is not None:
            self.proxy_id = proxy_id
        if proxy_name is not None:
            self.proxy_name = proxy_name
        if effective_time_range is not None:
            self.effective_time_range = effective_time_range
        if app_id is not None:
            self.app_id = app_id

    @property
    def proxy_id(self):
        r"""Gets the proxy_id of this QueryDeviceProxySimplify.

        **参数说明**：代理ID。用来唯一标识一个代理规则

        :return: The proxy_id of this QueryDeviceProxySimplify.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        r"""Sets the proxy_id of this QueryDeviceProxySimplify.

        **参数说明**：代理ID。用来唯一标识一个代理规则

        :param proxy_id: The proxy_id of this QueryDeviceProxySimplify.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

    @property
    def proxy_name(self):
        r"""Gets the proxy_name of this QueryDeviceProxySimplify.

        **参数说明**：设备代理名称

        :return: The proxy_name of this QueryDeviceProxySimplify.
        :rtype: str
        """
        return self._proxy_name

    @proxy_name.setter
    def proxy_name(self, proxy_name):
        r"""Sets the proxy_name of this QueryDeviceProxySimplify.

        **参数说明**：设备代理名称

        :param proxy_name: The proxy_name of this QueryDeviceProxySimplify.
        :type proxy_name: str
        """
        self._proxy_name = proxy_name

    @property
    def effective_time_range(self):
        r"""Gets the effective_time_range of this QueryDeviceProxySimplify.

        :return: The effective_time_range of this QueryDeviceProxySimplify.
        :rtype: :class:`huaweicloudsdkiotda.v5.EffectiveTimeRangeResponseDTO`
        """
        return self._effective_time_range

    @effective_time_range.setter
    def effective_time_range(self, effective_time_range):
        r"""Sets the effective_time_range of this QueryDeviceProxySimplify.

        :param effective_time_range: The effective_time_range of this QueryDeviceProxySimplify.
        :type effective_time_range: :class:`huaweicloudsdkiotda.v5.EffectiveTimeRangeResponseDTO`
        """
        self._effective_time_range = effective_time_range

    @property
    def app_id(self):
        r"""Gets the app_id of this QueryDeviceProxySimplify.

        **参数说明**：资源空间ID。

        :return: The app_id of this QueryDeviceProxySimplify.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this QueryDeviceProxySimplify.

        **参数说明**：资源空间ID。

        :param app_id: The app_id of this QueryDeviceProxySimplify.
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
        if not isinstance(other, QueryDeviceProxySimplify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
