# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchGetSecretValueResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'versions': 'list[Version]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'versions': 'versions'
    }

    def __init__(self, total_count=None, versions=None):
        r"""BatchGetSecretValueResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释：**  返回的凭据版本总数 **取值范围：** 不涉及
        :type total_count: int
        :param versions: **参数解释：**  凭据版本值 **取值范围：** 不涉及
        :type versions: list[:class:`huaweicloudsdkcsms.v1.Version`]
        """
        
        super().__init__()

        self._total_count = None
        self._versions = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if versions is not None:
            self.versions = versions

    @property
    def total_count(self):
        r"""Gets the total_count of this BatchGetSecretValueResponse.

        **参数解释：**  返回的凭据版本总数 **取值范围：** 不涉及

        :return: The total_count of this BatchGetSecretValueResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this BatchGetSecretValueResponse.

        **参数解释：**  返回的凭据版本总数 **取值范围：** 不涉及

        :param total_count: The total_count of this BatchGetSecretValueResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def versions(self):
        r"""Gets the versions of this BatchGetSecretValueResponse.

        **参数解释：**  凭据版本值 **取值范围：** 不涉及

        :return: The versions of this BatchGetSecretValueResponse.
        :rtype: list[:class:`huaweicloudsdkcsms.v1.Version`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this BatchGetSecretValueResponse.

        **参数解释：**  凭据版本值 **取值范围：** 不涉及

        :param versions: The versions of this BatchGetSecretValueResponse.
        :type versions: list[:class:`huaweicloudsdkcsms.v1.Version`]
        """
        self._versions = versions

    def to_dict(self):
        import warnings
        warnings.warn("BatchGetSecretValueResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchGetSecretValueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
