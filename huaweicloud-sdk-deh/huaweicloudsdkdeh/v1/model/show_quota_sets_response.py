# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotaSetsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_set': 'list[RespQuotaSet]'
    }

    attribute_map = {
        'quota_set': 'quota_set'
    }

    def __init__(self, quota_set=None):
        """ShowQuotaSetsResponse

        The model defined in huaweicloud sdk

        :param quota_set: 专属主机的配额。
        :type quota_set: list[:class:`huaweicloudsdkdeh.v1.RespQuotaSet`]
        """
        
        super(ShowQuotaSetsResponse, self).__init__()

        self._quota_set = None
        self.discriminator = None

        if quota_set is not None:
            self.quota_set = quota_set

    @property
    def quota_set(self):
        """Gets the quota_set of this ShowQuotaSetsResponse.

        专属主机的配额。

        :return: The quota_set of this ShowQuotaSetsResponse.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.RespQuotaSet`]
        """
        return self._quota_set

    @quota_set.setter
    def quota_set(self, quota_set):
        """Sets the quota_set of this ShowQuotaSetsResponse.

        专属主机的配额。

        :param quota_set: The quota_set of this ShowQuotaSetsResponse.
        :type quota_set: list[:class:`huaweicloudsdkdeh.v1.RespQuotaSet`]
        """
        self._quota_set = quota_set

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
        if not isinstance(other, ShowQuotaSetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
