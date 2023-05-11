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
        'request_id': 'str',
        'quota': 'Quota'
    }

    attribute_map = {
        'request_id': 'request_id',
        'quota': 'quota'
    }

    def __init__(self, request_id=None, quota=None):
        """ShowQuotaResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。  注：自动生成 。
        :type request_id: str
        :param quota: 
        :type quota: :class:`huaweicloudsdkelb.v3.Quota`
        """
        
        super(ShowQuotaResponse, self).__init__()

        self._request_id = None
        self._quota = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if quota is not None:
            self.quota = quota

    @property
    def request_id(self):
        """Gets the request_id of this ShowQuotaResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this ShowQuotaResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowQuotaResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this ShowQuotaResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def quota(self):
        """Gets the quota of this ShowQuotaResponse.

        :return: The quota of this ShowQuotaResponse.
        :rtype: :class:`huaweicloudsdkelb.v3.Quota`
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ShowQuotaResponse.

        :param quota: The quota of this ShowQuotaResponse.
        :type quota: :class:`huaweicloudsdkelb.v3.Quota`
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
        if not isinstance(other, ShowQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
