# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota': 'int',
        'quota_used': 'int'
    }

    attribute_map = {
        'quota': 'quota',
        'quota_used': 'quota_used'
    }

    def __init__(self, quota=None, quota_used=None):
        r"""ShowQuotaResponse

        The model defined in huaweicloud sdk

        :param quota: 云堡垒机实例最大创建数量。
        :type quota: int
        :param quota_used: 当前云堡垒机实例创建个数。
        :type quota_used: int
        """
        
        super(ShowQuotaResponse, self).__init__()

        self._quota = None
        self._quota_used = None
        self.discriminator = None

        if quota is not None:
            self.quota = quota
        if quota_used is not None:
            self.quota_used = quota_used

    @property
    def quota(self):
        r"""Gets the quota of this ShowQuotaResponse.

        云堡垒机实例最大创建数量。

        :return: The quota of this ShowQuotaResponse.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ShowQuotaResponse.

        云堡垒机实例最大创建数量。

        :param quota: The quota of this ShowQuotaResponse.
        :type quota: int
        """
        self._quota = quota

    @property
    def quota_used(self):
        r"""Gets the quota_used of this ShowQuotaResponse.

        当前云堡垒机实例创建个数。

        :return: The quota_used of this ShowQuotaResponse.
        :rtype: int
        """
        return self._quota_used

    @quota_used.setter
    def quota_used(self, quota_used):
        r"""Sets the quota_used of this ShowQuotaResponse.

        当前云堡垒机实例创建个数。

        :param quota_used: The quota_used of this ShowQuotaResponse.
        :type quota_used: int
        """
        self._quota_used = quota_used

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
        if not isinstance(other, ShowQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
