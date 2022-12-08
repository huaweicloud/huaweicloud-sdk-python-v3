# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQuotaStateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota': 'str',
        'status_v6': 'str',
        'status': 'str',
        'eip_quota': 'str'
    }

    attribute_map = {
        'quota': 'quota',
        'status_v6': 'status_v6',
        'status': 'status',
        'eip_quota': 'eip_quota'
    }

    def __init__(self, quota=None, status_v6=None, status=None, eip_quota=None):
        """ListQuotaStateResponse

        The model defined in huaweicloud sdk

        :param quota: 配额
        :type quota: str
        :param status_v6: 支持IPv6 ECS资源信息
        :type status_v6: str
        :param status: ECS资源状态
        :type status: str
        :param eip_quota: EIP配额信息
        :type eip_quota: str
        """
        
        super(ListQuotaStateResponse, self).__init__()

        self._quota = None
        self._status_v6 = None
        self._status = None
        self._eip_quota = None
        self.discriminator = None

        if quota is not None:
            self.quota = quota
        if status_v6 is not None:
            self.status_v6 = status_v6
        if status is not None:
            self.status = status
        if eip_quota is not None:
            self.eip_quota = eip_quota

    @property
    def quota(self):
        """Gets the quota of this ListQuotaStateResponse.

        配额

        :return: The quota of this ListQuotaStateResponse.
        :rtype: str
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ListQuotaStateResponse.

        配额

        :param quota: The quota of this ListQuotaStateResponse.
        :type quota: str
        """
        self._quota = quota

    @property
    def status_v6(self):
        """Gets the status_v6 of this ListQuotaStateResponse.

        支持IPv6 ECS资源信息

        :return: The status_v6 of this ListQuotaStateResponse.
        :rtype: str
        """
        return self._status_v6

    @status_v6.setter
    def status_v6(self, status_v6):
        """Sets the status_v6 of this ListQuotaStateResponse.

        支持IPv6 ECS资源信息

        :param status_v6: The status_v6 of this ListQuotaStateResponse.
        :type status_v6: str
        """
        self._status_v6 = status_v6

    @property
    def status(self):
        """Gets the status of this ListQuotaStateResponse.

        ECS资源状态

        :return: The status of this ListQuotaStateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListQuotaStateResponse.

        ECS资源状态

        :param status: The status of this ListQuotaStateResponse.
        :type status: str
        """
        self._status = status

    @property
    def eip_quota(self):
        """Gets the eip_quota of this ListQuotaStateResponse.

        EIP配额信息

        :return: The eip_quota of this ListQuotaStateResponse.
        :rtype: str
        """
        return self._eip_quota

    @eip_quota.setter
    def eip_quota(self, eip_quota):
        """Sets the eip_quota of this ListQuotaStateResponse.

        EIP配额信息

        :param eip_quota: The eip_quota of this ListQuotaStateResponse.
        :type eip_quota: str
        """
        self._eip_quota = eip_quota

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
        if not isinstance(other, ListQuotaStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
