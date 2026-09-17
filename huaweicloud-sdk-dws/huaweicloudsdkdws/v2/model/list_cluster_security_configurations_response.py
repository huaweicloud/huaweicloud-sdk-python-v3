# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterSecurityConfigurationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configurations': 'list[SecurityConfigurationParameter]',
        'count': 'int'
    }

    attribute_map = {
        'configurations': 'configurations',
        'count': 'count'
    }

    def __init__(self, configurations=None, count=None):
        r"""ListClusterSecurityConfigurationsResponse

        The model defined in huaweicloud sdk

        :param configurations: **参数解释**： 参数列表。 **取值范围**： 不涉及。
        :type configurations: list[:class:`huaweicloudsdkdws.v2.SecurityConfigurationParameter`]
        :param count: **参数解释**： 总条数。 **取值范围**： 不涉及。
        :type count: int
        """
        
        super().__init__()

        self._configurations = None
        self._count = None
        self.discriminator = None

        if configurations is not None:
            self.configurations = configurations
        if count is not None:
            self.count = count

    @property
    def configurations(self):
        r"""Gets the configurations of this ListClusterSecurityConfigurationsResponse.

        **参数解释**： 参数列表。 **取值范围**： 不涉及。

        :return: The configurations of this ListClusterSecurityConfigurationsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.SecurityConfigurationParameter`]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        r"""Sets the configurations of this ListClusterSecurityConfigurationsResponse.

        **参数解释**： 参数列表。 **取值范围**： 不涉及。

        :param configurations: The configurations of this ListClusterSecurityConfigurationsResponse.
        :type configurations: list[:class:`huaweicloudsdkdws.v2.SecurityConfigurationParameter`]
        """
        self._configurations = configurations

    @property
    def count(self):
        r"""Gets the count of this ListClusterSecurityConfigurationsResponse.

        **参数解释**： 总条数。 **取值范围**： 不涉及。

        :return: The count of this ListClusterSecurityConfigurationsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListClusterSecurityConfigurationsResponse.

        **参数解释**： 总条数。 **取值范围**： 不涉及。

        :param count: The count of this ListClusterSecurityConfigurationsResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ListClusterSecurityConfigurationsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListClusterSecurityConfigurationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
