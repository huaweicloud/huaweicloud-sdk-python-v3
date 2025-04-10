# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default_certs': 'list[DefaultCertsResource]',
        'custom_certs': 'list[CustomCertsResource]'
    }

    attribute_map = {
        'default_certs': 'defaultCerts',
        'custom_certs': 'customCerts'
    }

    def __init__(self, default_certs=None, custom_certs=None):
        r"""ListCertsResponse

        The model defined in huaweicloud sdk

        :param default_certs: 默认证书列表。
        :type default_certs: list[:class:`huaweicloudsdkcss.v1.DefaultCertsResource`]
        :param custom_certs: 自定义证书列表。
        :type custom_certs: list[:class:`huaweicloudsdkcss.v1.CustomCertsResource`]
        """
        
        super(ListCertsResponse, self).__init__()

        self._default_certs = None
        self._custom_certs = None
        self.discriminator = None

        if default_certs is not None:
            self.default_certs = default_certs
        if custom_certs is not None:
            self.custom_certs = custom_certs

    @property
    def default_certs(self):
        r"""Gets the default_certs of this ListCertsResponse.

        默认证书列表。

        :return: The default_certs of this ListCertsResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.DefaultCertsResource`]
        """
        return self._default_certs

    @default_certs.setter
    def default_certs(self, default_certs):
        r"""Sets the default_certs of this ListCertsResponse.

        默认证书列表。

        :param default_certs: The default_certs of this ListCertsResponse.
        :type default_certs: list[:class:`huaweicloudsdkcss.v1.DefaultCertsResource`]
        """
        self._default_certs = default_certs

    @property
    def custom_certs(self):
        r"""Gets the custom_certs of this ListCertsResponse.

        自定义证书列表。

        :return: The custom_certs of this ListCertsResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.CustomCertsResource`]
        """
        return self._custom_certs

    @custom_certs.setter
    def custom_certs(self, custom_certs):
        r"""Sets the custom_certs of this ListCertsResponse.

        自定义证书列表。

        :param custom_certs: The custom_certs of this ListCertsResponse.
        :type custom_certs: list[:class:`huaweicloudsdkcss.v1.CustomCertsResource`]
        """
        self._custom_certs = custom_certs

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
        if not isinstance(other, ListCertsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
