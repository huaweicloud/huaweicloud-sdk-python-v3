# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckCidrResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manage_cidrs': 'list[str]',
        'conflict_cidrs': 'list[str]'
    }

    attribute_map = {
        'manage_cidrs': 'manage_cidrs',
        'conflict_cidrs': 'conflict_cidrs'
    }

    def __init__(self, manage_cidrs=None, conflict_cidrs=None):
        r"""CheckCidrResponse

        The model defined in huaweicloud sdk

        :param manage_cidrs: 规划的冲突网段
        :type manage_cidrs: list[str]
        :param conflict_cidrs: 租户网段与冲突网段的重叠部分
        :type conflict_cidrs: list[str]
        """
        
        super().__init__()

        self._manage_cidrs = None
        self._conflict_cidrs = None
        self.discriminator = None

        if manage_cidrs is not None:
            self.manage_cidrs = manage_cidrs
        if conflict_cidrs is not None:
            self.conflict_cidrs = conflict_cidrs

    @property
    def manage_cidrs(self):
        r"""Gets the manage_cidrs of this CheckCidrResponse.

        规划的冲突网段

        :return: The manage_cidrs of this CheckCidrResponse.
        :rtype: list[str]
        """
        return self._manage_cidrs

    @manage_cidrs.setter
    def manage_cidrs(self, manage_cidrs):
        r"""Sets the manage_cidrs of this CheckCidrResponse.

        规划的冲突网段

        :param manage_cidrs: The manage_cidrs of this CheckCidrResponse.
        :type manage_cidrs: list[str]
        """
        self._manage_cidrs = manage_cidrs

    @property
    def conflict_cidrs(self):
        r"""Gets the conflict_cidrs of this CheckCidrResponse.

        租户网段与冲突网段的重叠部分

        :return: The conflict_cidrs of this CheckCidrResponse.
        :rtype: list[str]
        """
        return self._conflict_cidrs

    @conflict_cidrs.setter
    def conflict_cidrs(self, conflict_cidrs):
        r"""Sets the conflict_cidrs of this CheckCidrResponse.

        租户网段与冲突网段的重叠部分

        :param conflict_cidrs: The conflict_cidrs of this CheckCidrResponse.
        :type conflict_cidrs: list[str]
        """
        self._conflict_cidrs = conflict_cidrs

    def to_dict(self):
        import warnings
        warnings.warn("CheckCidrResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CheckCidrResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
