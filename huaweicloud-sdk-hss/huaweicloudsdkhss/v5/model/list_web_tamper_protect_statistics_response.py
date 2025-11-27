# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWebTamperProtectStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_failed_nums': 'int',
        'redundant_nums': 'int',
        'unprotect_nums': 'int',
        'protected_nums': 'int',
        'protect_total_nums': 'int',
        'protected_event_nums': 'int'
    }

    attribute_map = {
        'protect_failed_nums': 'protect_failed_nums',
        'redundant_nums': 'redundant_nums',
        'unprotect_nums': 'unprotect_nums',
        'protected_nums': 'protected_nums',
        'protect_total_nums': 'protect_total_nums',
        'protected_event_nums': 'protected_event_nums'
    }

    def __init__(self, protect_failed_nums=None, redundant_nums=None, unprotect_nums=None, protected_nums=None, protect_total_nums=None, protected_event_nums=None):
        r"""ListWebTamperProtectStatisticsResponse

        The model defined in huaweicloud sdk

        :param protect_failed_nums: 防护失败的数量
        :type protect_failed_nums: int
        :param redundant_nums: 防护冗余数量
        :type redundant_nums: int
        :param unprotect_nums: 未防护数量
        :type unprotect_nums: int
        :param protected_nums: 已防护数量
        :type protected_nums: int
        :param protect_total_nums: 防护资产总数
        :type protect_total_nums: int
        :param protected_event_nums: 防护事件数量
        :type protected_event_nums: int
        """
        
        super().__init__()

        self._protect_failed_nums = None
        self._redundant_nums = None
        self._unprotect_nums = None
        self._protected_nums = None
        self._protect_total_nums = None
        self._protected_event_nums = None
        self.discriminator = None

        if protect_failed_nums is not None:
            self.protect_failed_nums = protect_failed_nums
        if redundant_nums is not None:
            self.redundant_nums = redundant_nums
        if unprotect_nums is not None:
            self.unprotect_nums = unprotect_nums
        if protected_nums is not None:
            self.protected_nums = protected_nums
        if protect_total_nums is not None:
            self.protect_total_nums = protect_total_nums
        if protected_event_nums is not None:
            self.protected_event_nums = protected_event_nums

    @property
    def protect_failed_nums(self):
        r"""Gets the protect_failed_nums of this ListWebTamperProtectStatisticsResponse.

        防护失败的数量

        :return: The protect_failed_nums of this ListWebTamperProtectStatisticsResponse.
        :rtype: int
        """
        return self._protect_failed_nums

    @protect_failed_nums.setter
    def protect_failed_nums(self, protect_failed_nums):
        r"""Sets the protect_failed_nums of this ListWebTamperProtectStatisticsResponse.

        防护失败的数量

        :param protect_failed_nums: The protect_failed_nums of this ListWebTamperProtectStatisticsResponse.
        :type protect_failed_nums: int
        """
        self._protect_failed_nums = protect_failed_nums

    @property
    def redundant_nums(self):
        r"""Gets the redundant_nums of this ListWebTamperProtectStatisticsResponse.

        防护冗余数量

        :return: The redundant_nums of this ListWebTamperProtectStatisticsResponse.
        :rtype: int
        """
        return self._redundant_nums

    @redundant_nums.setter
    def redundant_nums(self, redundant_nums):
        r"""Sets the redundant_nums of this ListWebTamperProtectStatisticsResponse.

        防护冗余数量

        :param redundant_nums: The redundant_nums of this ListWebTamperProtectStatisticsResponse.
        :type redundant_nums: int
        """
        self._redundant_nums = redundant_nums

    @property
    def unprotect_nums(self):
        r"""Gets the unprotect_nums of this ListWebTamperProtectStatisticsResponse.

        未防护数量

        :return: The unprotect_nums of this ListWebTamperProtectStatisticsResponse.
        :rtype: int
        """
        return self._unprotect_nums

    @unprotect_nums.setter
    def unprotect_nums(self, unprotect_nums):
        r"""Sets the unprotect_nums of this ListWebTamperProtectStatisticsResponse.

        未防护数量

        :param unprotect_nums: The unprotect_nums of this ListWebTamperProtectStatisticsResponse.
        :type unprotect_nums: int
        """
        self._unprotect_nums = unprotect_nums

    @property
    def protected_nums(self):
        r"""Gets the protected_nums of this ListWebTamperProtectStatisticsResponse.

        已防护数量

        :return: The protected_nums of this ListWebTamperProtectStatisticsResponse.
        :rtype: int
        """
        return self._protected_nums

    @protected_nums.setter
    def protected_nums(self, protected_nums):
        r"""Sets the protected_nums of this ListWebTamperProtectStatisticsResponse.

        已防护数量

        :param protected_nums: The protected_nums of this ListWebTamperProtectStatisticsResponse.
        :type protected_nums: int
        """
        self._protected_nums = protected_nums

    @property
    def protect_total_nums(self):
        r"""Gets the protect_total_nums of this ListWebTamperProtectStatisticsResponse.

        防护资产总数

        :return: The protect_total_nums of this ListWebTamperProtectStatisticsResponse.
        :rtype: int
        """
        return self._protect_total_nums

    @protect_total_nums.setter
    def protect_total_nums(self, protect_total_nums):
        r"""Sets the protect_total_nums of this ListWebTamperProtectStatisticsResponse.

        防护资产总数

        :param protect_total_nums: The protect_total_nums of this ListWebTamperProtectStatisticsResponse.
        :type protect_total_nums: int
        """
        self._protect_total_nums = protect_total_nums

    @property
    def protected_event_nums(self):
        r"""Gets the protected_event_nums of this ListWebTamperProtectStatisticsResponse.

        防护事件数量

        :return: The protected_event_nums of this ListWebTamperProtectStatisticsResponse.
        :rtype: int
        """
        return self._protected_event_nums

    @protected_event_nums.setter
    def protected_event_nums(self, protected_event_nums):
        r"""Sets the protected_event_nums of this ListWebTamperProtectStatisticsResponse.

        防护事件数量

        :param protected_event_nums: The protected_event_nums of this ListWebTamperProtectStatisticsResponse.
        :type protected_event_nums: int
        """
        self._protected_event_nums = protected_event_nums

    def to_dict(self):
        import warnings
        warnings.warn("ListWebTamperProtectStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListWebTamperProtectStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
