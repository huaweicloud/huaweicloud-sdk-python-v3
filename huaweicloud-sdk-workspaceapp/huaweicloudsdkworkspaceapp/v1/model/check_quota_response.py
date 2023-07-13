# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_enough': 'bool',
        'quota_remainder': 'list[QuotaRemainderData]'
    }

    attribute_map = {
        'is_enough': 'is_enough',
        'quota_remainder': 'quota_remainder'
    }

    def __init__(self, is_enough=None, quota_remainder=None):
        """CheckQuotaResponse

        The model defined in huaweicloud sdk

        :param is_enough: 配额是否足够true：足够 false：不足
        :type is_enough: bool
        :param quota_remainder: 配额剩余数量信息
        :type quota_remainder: list[:class:`huaweicloudsdkworkspaceapp.v1.QuotaRemainderData`]
        """
        
        super(CheckQuotaResponse, self).__init__()

        self._is_enough = None
        self._quota_remainder = None
        self.discriminator = None

        if is_enough is not None:
            self.is_enough = is_enough
        if quota_remainder is not None:
            self.quota_remainder = quota_remainder

    @property
    def is_enough(self):
        """Gets the is_enough of this CheckQuotaResponse.

        配额是否足够true：足够 false：不足

        :return: The is_enough of this CheckQuotaResponse.
        :rtype: bool
        """
        return self._is_enough

    @is_enough.setter
    def is_enough(self, is_enough):
        """Sets the is_enough of this CheckQuotaResponse.

        配额是否足够true：足够 false：不足

        :param is_enough: The is_enough of this CheckQuotaResponse.
        :type is_enough: bool
        """
        self._is_enough = is_enough

    @property
    def quota_remainder(self):
        """Gets the quota_remainder of this CheckQuotaResponse.

        配额剩余数量信息

        :return: The quota_remainder of this CheckQuotaResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.QuotaRemainderData`]
        """
        return self._quota_remainder

    @quota_remainder.setter
    def quota_remainder(self, quota_remainder):
        """Sets the quota_remainder of this CheckQuotaResponse.

        配额剩余数量信息

        :param quota_remainder: The quota_remainder of this CheckQuotaResponse.
        :type quota_remainder: list[:class:`huaweicloudsdkworkspaceapp.v1.QuotaRemainderData`]
        """
        self._quota_remainder = quota_remainder

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
        if not isinstance(other, CheckQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
