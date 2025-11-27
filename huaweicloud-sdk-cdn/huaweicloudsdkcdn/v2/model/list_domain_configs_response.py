# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cname_status': 'list[CnameStatus]'
    }

    attribute_map = {
        'cname_status': 'cname_status'
    }

    def __init__(self, cname_status=None):
        r"""ListDomainConfigsResponse

        The model defined in huaweicloud sdk

        :param cname_status: 域名cname状态。
        :type cname_status: list[:class:`huaweicloudsdkcdn.v2.CnameStatus`]
        """
        
        super().__init__()

        self._cname_status = None
        self.discriminator = None

        if cname_status is not None:
            self.cname_status = cname_status

    @property
    def cname_status(self):
        r"""Gets the cname_status of this ListDomainConfigsResponse.

        域名cname状态。

        :return: The cname_status of this ListDomainConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.CnameStatus`]
        """
        return self._cname_status

    @cname_status.setter
    def cname_status(self, cname_status):
        r"""Sets the cname_status of this ListDomainConfigsResponse.

        域名cname状态。

        :param cname_status: The cname_status of this ListDomainConfigsResponse.
        :type cname_status: list[:class:`huaweicloudsdkcdn.v2.CnameStatus`]
        """
        self._cname_status = cname_status

    def to_dict(self):
        import warnings
        warnings.warn("ListDomainConfigsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListDomainConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
