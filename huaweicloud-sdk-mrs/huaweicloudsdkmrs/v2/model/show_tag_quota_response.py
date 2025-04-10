# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTagQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_quota': 'int',
        'available_quota': 'int'
    }

    attribute_map = {
        'total_quota': 'total_quota',
        'available_quota': 'available_quota'
    }

    def __init__(self, total_quota=None, available_quota=None):
        r"""ShowTagQuotaResponse

        The model defined in huaweicloud sdk

        :param total_quota: 总配额大小
        :type total_quota: int
        :param available_quota: 可使用配额大小
        :type available_quota: int
        """
        
        super(ShowTagQuotaResponse, self).__init__()

        self._total_quota = None
        self._available_quota = None
        self.discriminator = None

        if total_quota is not None:
            self.total_quota = total_quota
        if available_quota is not None:
            self.available_quota = available_quota

    @property
    def total_quota(self):
        r"""Gets the total_quota of this ShowTagQuotaResponse.

        总配额大小

        :return: The total_quota of this ShowTagQuotaResponse.
        :rtype: int
        """
        return self._total_quota

    @total_quota.setter
    def total_quota(self, total_quota):
        r"""Sets the total_quota of this ShowTagQuotaResponse.

        总配额大小

        :param total_quota: The total_quota of this ShowTagQuotaResponse.
        :type total_quota: int
        """
        self._total_quota = total_quota

    @property
    def available_quota(self):
        r"""Gets the available_quota of this ShowTagQuotaResponse.

        可使用配额大小

        :return: The available_quota of this ShowTagQuotaResponse.
        :rtype: int
        """
        return self._available_quota

    @available_quota.setter
    def available_quota(self, available_quota):
        r"""Sets the available_quota of this ShowTagQuotaResponse.

        可使用配额大小

        :param available_quota: The available_quota of this ShowTagQuotaResponse.
        :type available_quota: int
        """
        self._available_quota = available_quota

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
        if not isinstance(other, ShowTagQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
