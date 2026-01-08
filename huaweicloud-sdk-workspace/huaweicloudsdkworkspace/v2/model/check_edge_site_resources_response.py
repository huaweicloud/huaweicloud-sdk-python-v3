# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckEdgeSiteResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_enough': 'int',
        'resource_remainder': 'list[ResourceRemainderData]'
    }

    attribute_map = {
        'is_enough': 'is_enough',
        'resource_remainder': 'resource_remainder'
    }

    def __init__(self, is_enough=None, resource_remainder=None):
        r"""CheckEdgeSiteResourcesResponse

        The model defined in huaweicloud sdk

        :param is_enough: 配额是否足够1：足够 0 ：不足。
        :type is_enough: int
        :param resource_remainder: 资源剩余数量信息。
        :type resource_remainder: list[:class:`huaweicloudsdkworkspace.v2.ResourceRemainderData`]
        """
        
        super().__init__()

        self._is_enough = None
        self._resource_remainder = None
        self.discriminator = None

        if is_enough is not None:
            self.is_enough = is_enough
        if resource_remainder is not None:
            self.resource_remainder = resource_remainder

    @property
    def is_enough(self):
        r"""Gets the is_enough of this CheckEdgeSiteResourcesResponse.

        配额是否足够1：足够 0 ：不足。

        :return: The is_enough of this CheckEdgeSiteResourcesResponse.
        :rtype: int
        """
        return self._is_enough

    @is_enough.setter
    def is_enough(self, is_enough):
        r"""Sets the is_enough of this CheckEdgeSiteResourcesResponse.

        配额是否足够1：足够 0 ：不足。

        :param is_enough: The is_enough of this CheckEdgeSiteResourcesResponse.
        :type is_enough: int
        """
        self._is_enough = is_enough

    @property
    def resource_remainder(self):
        r"""Gets the resource_remainder of this CheckEdgeSiteResourcesResponse.

        资源剩余数量信息。

        :return: The resource_remainder of this CheckEdgeSiteResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ResourceRemainderData`]
        """
        return self._resource_remainder

    @resource_remainder.setter
    def resource_remainder(self, resource_remainder):
        r"""Sets the resource_remainder of this CheckEdgeSiteResourcesResponse.

        资源剩余数量信息。

        :param resource_remainder: The resource_remainder of this CheckEdgeSiteResourcesResponse.
        :type resource_remainder: list[:class:`huaweicloudsdkworkspace.v2.ResourceRemainderData`]
        """
        self._resource_remainder = resource_remainder

    def to_dict(self):
        import warnings
        warnings.warn("CheckEdgeSiteResourcesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CheckEdgeSiteResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
