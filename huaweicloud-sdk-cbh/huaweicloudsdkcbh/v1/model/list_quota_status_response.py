# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQuotaStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_v6': 'str',
        'status': 'str',
        'eip_quota': 'int',
        'quota': 'int'
    }

    attribute_map = {
        'status_v6': 'status_v6',
        'status': 'status',
        'eip_quota': 'eip_quota',
        'quota': 'quota'
    }

    def __init__(self, status_v6=None, status=None, eip_quota=None, quota=None):
        """ListQuotaStatusResponse

        The model defined in huaweicloud sdk

        :param status_v6: 支持IPv6弹性云服务器资源状态。 - sellout 售罄 - normal  正常商用 - abandon 下线（即不显示）
        :type status_v6: str
        :param status: 弹性云服务器资源状态。 - sellout 售罄 - normal  正常商用 - abandon 下线（即不显示）
        :type status: str
        :param eip_quota: 弹性配额信息，返回默认值null。
        :type eip_quota: int
        :param quota: 剩余可创建云堡垒机配额信息，返回默认值null。
        :type quota: int
        """
        
        super(ListQuotaStatusResponse, self).__init__()

        self._status_v6 = None
        self._status = None
        self._eip_quota = None
        self._quota = None
        self.discriminator = None

        if status_v6 is not None:
            self.status_v6 = status_v6
        if status is not None:
            self.status = status
        if eip_quota is not None:
            self.eip_quota = eip_quota
        if quota is not None:
            self.quota = quota

    @property
    def status_v6(self):
        """Gets the status_v6 of this ListQuotaStatusResponse.

        支持IPv6弹性云服务器资源状态。 - sellout 售罄 - normal  正常商用 - abandon 下线（即不显示）

        :return: The status_v6 of this ListQuotaStatusResponse.
        :rtype: str
        """
        return self._status_v6

    @status_v6.setter
    def status_v6(self, status_v6):
        """Sets the status_v6 of this ListQuotaStatusResponse.

        支持IPv6弹性云服务器资源状态。 - sellout 售罄 - normal  正常商用 - abandon 下线（即不显示）

        :param status_v6: The status_v6 of this ListQuotaStatusResponse.
        :type status_v6: str
        """
        self._status_v6 = status_v6

    @property
    def status(self):
        """Gets the status of this ListQuotaStatusResponse.

        弹性云服务器资源状态。 - sellout 售罄 - normal  正常商用 - abandon 下线（即不显示）

        :return: The status of this ListQuotaStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListQuotaStatusResponse.

        弹性云服务器资源状态。 - sellout 售罄 - normal  正常商用 - abandon 下线（即不显示）

        :param status: The status of this ListQuotaStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def eip_quota(self):
        """Gets the eip_quota of this ListQuotaStatusResponse.

        弹性配额信息，返回默认值null。

        :return: The eip_quota of this ListQuotaStatusResponse.
        :rtype: int
        """
        return self._eip_quota

    @eip_quota.setter
    def eip_quota(self, eip_quota):
        """Sets the eip_quota of this ListQuotaStatusResponse.

        弹性配额信息，返回默认值null。

        :param eip_quota: The eip_quota of this ListQuotaStatusResponse.
        :type eip_quota: int
        """
        self._eip_quota = eip_quota

    @property
    def quota(self):
        """Gets the quota of this ListQuotaStatusResponse.

        剩余可创建云堡垒机配额信息，返回默认值null。

        :return: The quota of this ListQuotaStatusResponse.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ListQuotaStatusResponse.

        剩余可创建云堡垒机配额信息，返回默认值null。

        :param quota: The quota of this ListQuotaStatusResponse.
        :type quota: int
        """
        self._quota = quota

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
        if not isinstance(other, ListQuotaStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
