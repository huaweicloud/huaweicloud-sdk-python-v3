# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceAllProxyVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy_engine_version_infos': 'list[ProxyEngineVersionInfo]'
    }

    attribute_map = {
        'proxy_engine_version_infos': 'proxy_engine_version_infos'
    }

    def __init__(self, proxy_engine_version_infos=None):
        r"""ListInstanceAllProxyVersionResponse

        The model defined in huaweicloud sdk

        :param proxy_engine_version_infos: **参数解释**：  数据库代理节点引擎版本信息列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type proxy_engine_version_infos: list[:class:`huaweicloudsdkrds.v3.ProxyEngineVersionInfo`]
        """
        
        super().__init__()

        self._proxy_engine_version_infos = None
        self.discriminator = None

        if proxy_engine_version_infos is not None:
            self.proxy_engine_version_infos = proxy_engine_version_infos

    @property
    def proxy_engine_version_infos(self):
        r"""Gets the proxy_engine_version_infos of this ListInstanceAllProxyVersionResponse.

        **参数解释**：  数据库代理节点引擎版本信息列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The proxy_engine_version_infos of this ListInstanceAllProxyVersionResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ProxyEngineVersionInfo`]
        """
        return self._proxy_engine_version_infos

    @proxy_engine_version_infos.setter
    def proxy_engine_version_infos(self, proxy_engine_version_infos):
        r"""Sets the proxy_engine_version_infos of this ListInstanceAllProxyVersionResponse.

        **参数解释**：  数据库代理节点引擎版本信息列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param proxy_engine_version_infos: The proxy_engine_version_infos of this ListInstanceAllProxyVersionResponse.
        :type proxy_engine_version_infos: list[:class:`huaweicloudsdkrds.v3.ProxyEngineVersionInfo`]
        """
        self._proxy_engine_version_infos = proxy_engine_version_infos

    def to_dict(self):
        import warnings
        warnings.warn("ListInstanceAllProxyVersionResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListInstanceAllProxyVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
