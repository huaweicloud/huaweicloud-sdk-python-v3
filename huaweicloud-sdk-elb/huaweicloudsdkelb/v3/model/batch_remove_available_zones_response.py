# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRemoveAvailableZonesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancer': 'LoadBalancer',
        'request_id': 'str'
    }

    attribute_map = {
        'loadbalancer': 'loadbalancer',
        'request_id': 'request_id'
    }

    def __init__(self, loadbalancer=None, request_id=None):
        r"""BatchRemoveAvailableZonesResponse

        The model defined in huaweicloud sdk

        :param loadbalancer: 
        :type loadbalancer: :class:`huaweicloudsdkelb.v3.LoadBalancer`
        :param request_id: 请求ID。  注：自动生成 。
        :type request_id: str
        """
        
        super(BatchRemoveAvailableZonesResponse, self).__init__()

        self._loadbalancer = None
        self._request_id = None
        self.discriminator = None

        if loadbalancer is not None:
            self.loadbalancer = loadbalancer
        if request_id is not None:
            self.request_id = request_id

    @property
    def loadbalancer(self):
        r"""Gets the loadbalancer of this BatchRemoveAvailableZonesResponse.

        :return: The loadbalancer of this BatchRemoveAvailableZonesResponse.
        :rtype: :class:`huaweicloudsdkelb.v3.LoadBalancer`
        """
        return self._loadbalancer

    @loadbalancer.setter
    def loadbalancer(self, loadbalancer):
        r"""Sets the loadbalancer of this BatchRemoveAvailableZonesResponse.

        :param loadbalancer: The loadbalancer of this BatchRemoveAvailableZonesResponse.
        :type loadbalancer: :class:`huaweicloudsdkelb.v3.LoadBalancer`
        """
        self._loadbalancer = loadbalancer

    @property
    def request_id(self):
        r"""Gets the request_id of this BatchRemoveAvailableZonesResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this BatchRemoveAvailableZonesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this BatchRemoveAvailableZonesResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this BatchRemoveAvailableZonesResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, BatchRemoveAvailableZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
