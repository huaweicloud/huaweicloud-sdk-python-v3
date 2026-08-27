# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtocolConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol_configs': 'list[ProtocolConfigBase]',
        'page': 'Page'
    }

    attribute_map = {
        'protocol_configs': 'protocol_configs',
        'page': 'page'
    }

    def __init__(self, protocol_configs=None, page=None):
        r"""ListProtocolConfigsResponse

        The model defined in huaweicloud sdk

        :param protocol_configs: 泛协议配置列表
        :type protocol_configs: list[:class:`huaweicloudsdkiotda.v5.ProtocolConfigBase`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super().__init__()

        self._protocol_configs = None
        self._page = None
        self.discriminator = None

        if protocol_configs is not None:
            self.protocol_configs = protocol_configs
        if page is not None:
            self.page = page

    @property
    def protocol_configs(self):
        r"""Gets the protocol_configs of this ListProtocolConfigsResponse.

        泛协议配置列表

        :return: The protocol_configs of this ListProtocolConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ProtocolConfigBase`]
        """
        return self._protocol_configs

    @protocol_configs.setter
    def protocol_configs(self, protocol_configs):
        r"""Sets the protocol_configs of this ListProtocolConfigsResponse.

        泛协议配置列表

        :param protocol_configs: The protocol_configs of this ListProtocolConfigsResponse.
        :type protocol_configs: list[:class:`huaweicloudsdkiotda.v5.ProtocolConfigBase`]
        """
        self._protocol_configs = protocol_configs

    @property
    def page(self):
        r"""Gets the page of this ListProtocolConfigsResponse.

        :return: The page of this ListProtocolConfigsResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListProtocolConfigsResponse.

        :param page: The page of this ListProtocolConfigsResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        self._page = page

    def to_dict(self):
        import warnings
        warnings.warn("ListProtocolConfigsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListProtocolConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
