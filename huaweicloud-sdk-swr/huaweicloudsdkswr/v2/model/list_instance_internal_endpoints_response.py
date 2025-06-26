# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceInternalEndpointsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'internal_endpoints': 'list[InternalEndpoint]',
        'total': 'int'
    }

    attribute_map = {
        'internal_endpoints': 'internal_endpoints',
        'total': 'total'
    }

    def __init__(self, internal_endpoints=None, total=None):
        r"""ListInstanceInternalEndpointsResponse

        The model defined in huaweicloud sdk

        :param internal_endpoints: 内网访问列表
        :type internal_endpoints: list[:class:`huaweicloudsdkswr.v2.InternalEndpoint`]
        :param total: 内网访问总数
        :type total: int
        """
        
        super(ListInstanceInternalEndpointsResponse, self).__init__()

        self._internal_endpoints = None
        self._total = None
        self.discriminator = None

        if internal_endpoints is not None:
            self.internal_endpoints = internal_endpoints
        if total is not None:
            self.total = total

    @property
    def internal_endpoints(self):
        r"""Gets the internal_endpoints of this ListInstanceInternalEndpointsResponse.

        内网访问列表

        :return: The internal_endpoints of this ListInstanceInternalEndpointsResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.InternalEndpoint`]
        """
        return self._internal_endpoints

    @internal_endpoints.setter
    def internal_endpoints(self, internal_endpoints):
        r"""Sets the internal_endpoints of this ListInstanceInternalEndpointsResponse.

        内网访问列表

        :param internal_endpoints: The internal_endpoints of this ListInstanceInternalEndpointsResponse.
        :type internal_endpoints: list[:class:`huaweicloudsdkswr.v2.InternalEndpoint`]
        """
        self._internal_endpoints = internal_endpoints

    @property
    def total(self):
        r"""Gets the total of this ListInstanceInternalEndpointsResponse.

        内网访问总数

        :return: The total of this ListInstanceInternalEndpointsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceInternalEndpointsResponse.

        内网访问总数

        :param total: The total of this ListInstanceInternalEndpointsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListInstanceInternalEndpointsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
