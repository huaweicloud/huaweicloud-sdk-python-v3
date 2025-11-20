# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'support_tls': 'list[str]',
        'cipher': 'list[CipherInfo]'
    }

    attribute_map = {
        'support_tls': 'support_tls',
        'cipher': 'cipher'
    }

    def __init__(self, support_tls=None, cipher=None):
        r"""ListGlobalConfigResponse

        The model defined in huaweicloud sdk

        :param support_tls: 支持的tls版本列表
        :type support_tls: list[str]
        :param cipher: 加密套件列表
        :type cipher: list[:class:`huaweicloudsdkaad.v2.CipherInfo`]
        """
        
        super().__init__()

        self._support_tls = None
        self._cipher = None
        self.discriminator = None

        if support_tls is not None:
            self.support_tls = support_tls
        if cipher is not None:
            self.cipher = cipher

    @property
    def support_tls(self):
        r"""Gets the support_tls of this ListGlobalConfigResponse.

        支持的tls版本列表

        :return: The support_tls of this ListGlobalConfigResponse.
        :rtype: list[str]
        """
        return self._support_tls

    @support_tls.setter
    def support_tls(self, support_tls):
        r"""Sets the support_tls of this ListGlobalConfigResponse.

        支持的tls版本列表

        :param support_tls: The support_tls of this ListGlobalConfigResponse.
        :type support_tls: list[str]
        """
        self._support_tls = support_tls

    @property
    def cipher(self):
        r"""Gets the cipher of this ListGlobalConfigResponse.

        加密套件列表

        :return: The cipher of this ListGlobalConfigResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v2.CipherInfo`]
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        r"""Sets the cipher of this ListGlobalConfigResponse.

        加密套件列表

        :param cipher: The cipher of this ListGlobalConfigResponse.
        :type cipher: list[:class:`huaweicloudsdkaad.v2.CipherInfo`]
        """
        self._cipher = cipher

    def to_dict(self):
        import warnings
        warnings.warn("ListGlobalConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListGlobalConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
