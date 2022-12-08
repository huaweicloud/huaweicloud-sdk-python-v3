# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateBandwidthPackageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_package': 'BandwidthPackage',
        'request_id': 'str'
    }

    attribute_map = {
        'bandwidth_package': 'bandwidth_package',
        'request_id': 'request_id'
    }

    def __init__(self, bandwidth_package=None, request_id=None):
        """DisassociateBandwidthPackageResponse

        The model defined in huaweicloud sdk

        :param bandwidth_package: 
        :type bandwidth_package: :class:`huaweicloudsdkcc.v3.BandwidthPackage`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(DisassociateBandwidthPackageResponse, self).__init__()

        self._bandwidth_package = None
        self._request_id = None
        self.discriminator = None

        if bandwidth_package is not None:
            self.bandwidth_package = bandwidth_package
        if request_id is not None:
            self.request_id = request_id

    @property
    def bandwidth_package(self):
        """Gets the bandwidth_package of this DisassociateBandwidthPackageResponse.

        :return: The bandwidth_package of this DisassociateBandwidthPackageResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.BandwidthPackage`
        """
        return self._bandwidth_package

    @bandwidth_package.setter
    def bandwidth_package(self, bandwidth_package):
        """Sets the bandwidth_package of this DisassociateBandwidthPackageResponse.

        :param bandwidth_package: The bandwidth_package of this DisassociateBandwidthPackageResponse.
        :type bandwidth_package: :class:`huaweicloudsdkcc.v3.BandwidthPackage`
        """
        self._bandwidth_package = bandwidth_package

    @property
    def request_id(self):
        """Gets the request_id of this DisassociateBandwidthPackageResponse.

        请求ID。

        :return: The request_id of this DisassociateBandwidthPackageResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DisassociateBandwidthPackageResponse.

        请求ID。

        :param request_id: The request_id of this DisassociateBandwidthPackageResponse.
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
        if not isinstance(other, DisassociateBandwidthPackageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
