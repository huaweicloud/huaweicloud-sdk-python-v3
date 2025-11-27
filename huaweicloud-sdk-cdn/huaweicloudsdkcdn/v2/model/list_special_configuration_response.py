# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpecialConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'special_configurations': 'list[SpeicialConfiguration]'
    }

    attribute_map = {
        'total': 'total',
        'special_configurations': 'specialConfigurations'
    }

    def __init__(self, total=None, special_configurations=None):
        r"""ListSpecialConfigurationResponse

        The model defined in huaweicloud sdk

        :param total: 总条数。
        :type total: int
        :param special_configurations: 域名特殊配置信息。
        :type special_configurations: list[:class:`huaweicloudsdkcdn.v2.SpeicialConfiguration`]
        """
        
        super().__init__()

        self._total = None
        self._special_configurations = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if special_configurations is not None:
            self.special_configurations = special_configurations

    @property
    def total(self):
        r"""Gets the total of this ListSpecialConfigurationResponse.

        总条数。

        :return: The total of this ListSpecialConfigurationResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSpecialConfigurationResponse.

        总条数。

        :param total: The total of this ListSpecialConfigurationResponse.
        :type total: int
        """
        self._total = total

    @property
    def special_configurations(self):
        r"""Gets the special_configurations of this ListSpecialConfigurationResponse.

        域名特殊配置信息。

        :return: The special_configurations of this ListSpecialConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.SpeicialConfiguration`]
        """
        return self._special_configurations

    @special_configurations.setter
    def special_configurations(self, special_configurations):
        r"""Sets the special_configurations of this ListSpecialConfigurationResponse.

        域名特殊配置信息。

        :param special_configurations: The special_configurations of this ListSpecialConfigurationResponse.
        :type special_configurations: list[:class:`huaweicloudsdkcdn.v2.SpeicialConfiguration`]
        """
        self._special_configurations = special_configurations

    def to_dict(self):
        import warnings
        warnings.warn("ListSpecialConfigurationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSpecialConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
