# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchQuotaResponse(SdkResponse):

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
        'eip_quota': 'int',
        'status': 'str',
        'status_v6': 'str'
    }

    attribute_map = {
        'quota': 'quota',
        'eip_quota': 'eip_quota',
        'status': 'status',
        'status_v6': 'status_v6'
    }

    def __init__(self, quota=None, eip_quota=None, status=None, status_v6=None):
        """SearchQuotaResponse

        The model defined in huaweicloud sdk

        :param quota: 配额
        :type quota: int
        :param eip_quota: EIP配额
        :type eip_quota: int
        :param status: 状态
        :type status: str
        :param status_v6: v6状态
        :type status_v6: str
        """
        
        super(SearchQuotaResponse, self).__init__()

        self._quota = None
        self._eip_quota = None
        self._status = None
        self._status_v6 = None
        self.discriminator = None

        if quota is not None:
            self.quota = quota
        if eip_quota is not None:
            self.eip_quota = eip_quota
        if status is not None:
            self.status = status
        if status_v6 is not None:
            self.status_v6 = status_v6

    @property
    def quota(self):
        """Gets the quota of this SearchQuotaResponse.

        配额

        :return: The quota of this SearchQuotaResponse.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this SearchQuotaResponse.

        配额

        :param quota: The quota of this SearchQuotaResponse.
        :type quota: int
        """
        self._quota = quota

    @property
    def eip_quota(self):
        """Gets the eip_quota of this SearchQuotaResponse.

        EIP配额

        :return: The eip_quota of this SearchQuotaResponse.
        :rtype: int
        """
        return self._eip_quota

    @eip_quota.setter
    def eip_quota(self, eip_quota):
        """Sets the eip_quota of this SearchQuotaResponse.

        EIP配额

        :param eip_quota: The eip_quota of this SearchQuotaResponse.
        :type eip_quota: int
        """
        self._eip_quota = eip_quota

    @property
    def status(self):
        """Gets the status of this SearchQuotaResponse.

        状态

        :return: The status of this SearchQuotaResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchQuotaResponse.

        状态

        :param status: The status of this SearchQuotaResponse.
        :type status: str
        """
        self._status = status

    @property
    def status_v6(self):
        """Gets the status_v6 of this SearchQuotaResponse.

        v6状态

        :return: The status_v6 of this SearchQuotaResponse.
        :rtype: str
        """
        return self._status_v6

    @status_v6.setter
    def status_v6(self, status_v6):
        """Sets the status_v6 of this SearchQuotaResponse.

        v6状态

        :param status_v6: The status_v6 of this SearchQuotaResponse.
        :type status_v6: str
        """
        self._status_v6 = status_v6

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
        if not isinstance(other, SearchQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
