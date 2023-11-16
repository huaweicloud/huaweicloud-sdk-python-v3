# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUnblockQuotaStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'total_unblocking_quota': 'int',
        'remaining_unblocking_quota': 'int',
        'unblocking_quota_today': 'int',
        'remaining_unblocking_quota_today': 'int'
    }

    attribute_map = {
        'type': 'type',
        'total_unblocking_quota': 'total_unblocking_quota',
        'remaining_unblocking_quota': 'remaining_unblocking_quota',
        'unblocking_quota_today': 'unblocking_quota_today',
        'remaining_unblocking_quota_today': 'remaining_unblocking_quota_today'
    }

    def __init__(self, type=None, total_unblocking_quota=None, remaining_unblocking_quota=None, unblocking_quota_today=None, remaining_unblocking_quota_today=None):
        """ListUnblockQuotaStatisticsResponse

        The model defined in huaweicloud sdk

        :param type: 用户类型：common_user , native_protection_user
        :type type: str
        :param total_unblocking_quota: 解封总配额
        :type total_unblocking_quota: int
        :param remaining_unblocking_quota: 剩余解封配额
        :type remaining_unblocking_quota: int
        :param unblocking_quota_today: 今日解封配额
        :type unblocking_quota_today: int
        :param remaining_unblocking_quota_today: 今日剩余解封配额
        :type remaining_unblocking_quota_today: int
        """
        
        super(ListUnblockQuotaStatisticsResponse, self).__init__()

        self._type = None
        self._total_unblocking_quota = None
        self._remaining_unblocking_quota = None
        self._unblocking_quota_today = None
        self._remaining_unblocking_quota_today = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if total_unblocking_quota is not None:
            self.total_unblocking_quota = total_unblocking_quota
        if remaining_unblocking_quota is not None:
            self.remaining_unblocking_quota = remaining_unblocking_quota
        if unblocking_quota_today is not None:
            self.unblocking_quota_today = unblocking_quota_today
        if remaining_unblocking_quota_today is not None:
            self.remaining_unblocking_quota_today = remaining_unblocking_quota_today

    @property
    def type(self):
        """Gets the type of this ListUnblockQuotaStatisticsResponse.

        用户类型：common_user , native_protection_user

        :return: The type of this ListUnblockQuotaStatisticsResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListUnblockQuotaStatisticsResponse.

        用户类型：common_user , native_protection_user

        :param type: The type of this ListUnblockQuotaStatisticsResponse.
        :type type: str
        """
        self._type = type

    @property
    def total_unblocking_quota(self):
        """Gets the total_unblocking_quota of this ListUnblockQuotaStatisticsResponse.

        解封总配额

        :return: The total_unblocking_quota of this ListUnblockQuotaStatisticsResponse.
        :rtype: int
        """
        return self._total_unblocking_quota

    @total_unblocking_quota.setter
    def total_unblocking_quota(self, total_unblocking_quota):
        """Sets the total_unblocking_quota of this ListUnblockQuotaStatisticsResponse.

        解封总配额

        :param total_unblocking_quota: The total_unblocking_quota of this ListUnblockQuotaStatisticsResponse.
        :type total_unblocking_quota: int
        """
        self._total_unblocking_quota = total_unblocking_quota

    @property
    def remaining_unblocking_quota(self):
        """Gets the remaining_unblocking_quota of this ListUnblockQuotaStatisticsResponse.

        剩余解封配额

        :return: The remaining_unblocking_quota of this ListUnblockQuotaStatisticsResponse.
        :rtype: int
        """
        return self._remaining_unblocking_quota

    @remaining_unblocking_quota.setter
    def remaining_unblocking_quota(self, remaining_unblocking_quota):
        """Sets the remaining_unblocking_quota of this ListUnblockQuotaStatisticsResponse.

        剩余解封配额

        :param remaining_unblocking_quota: The remaining_unblocking_quota of this ListUnblockQuotaStatisticsResponse.
        :type remaining_unblocking_quota: int
        """
        self._remaining_unblocking_quota = remaining_unblocking_quota

    @property
    def unblocking_quota_today(self):
        """Gets the unblocking_quota_today of this ListUnblockQuotaStatisticsResponse.

        今日解封配额

        :return: The unblocking_quota_today of this ListUnblockQuotaStatisticsResponse.
        :rtype: int
        """
        return self._unblocking_quota_today

    @unblocking_quota_today.setter
    def unblocking_quota_today(self, unblocking_quota_today):
        """Sets the unblocking_quota_today of this ListUnblockQuotaStatisticsResponse.

        今日解封配额

        :param unblocking_quota_today: The unblocking_quota_today of this ListUnblockQuotaStatisticsResponse.
        :type unblocking_quota_today: int
        """
        self._unblocking_quota_today = unblocking_quota_today

    @property
    def remaining_unblocking_quota_today(self):
        """Gets the remaining_unblocking_quota_today of this ListUnblockQuotaStatisticsResponse.

        今日剩余解封配额

        :return: The remaining_unblocking_quota_today of this ListUnblockQuotaStatisticsResponse.
        :rtype: int
        """
        return self._remaining_unblocking_quota_today

    @remaining_unblocking_quota_today.setter
    def remaining_unblocking_quota_today(self, remaining_unblocking_quota_today):
        """Sets the remaining_unblocking_quota_today of this ListUnblockQuotaStatisticsResponse.

        今日剩余解封配额

        :param remaining_unblocking_quota_today: The remaining_unblocking_quota_today of this ListUnblockQuotaStatisticsResponse.
        :type remaining_unblocking_quota_today: int
        """
        self._remaining_unblocking_quota_today = remaining_unblocking_quota_today

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
        if not isinstance(other, ListUnblockQuotaStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
