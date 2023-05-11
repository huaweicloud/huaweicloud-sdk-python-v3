# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServicePublicDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_services': 'list[EndpointService]',
        'total_count': 'int'
    }

    attribute_map = {
        'endpoint_services': 'endpoint_services',
        'total_count': 'total_count'
    }

    def __init__(self, endpoint_services=None, total_count=None):
        """ListServicePublicDetailsResponse

        The model defined in huaweicloud sdk

        :param endpoint_services: 终端节点服务列表。
        :type endpoint_services: list[:class:`huaweicloudsdkvpcep.v1.EndpointService`]
        :param total_count: 满足查询条件的公共终端节点服务总条数，不受分页（即limit、offset参数）影响。
        :type total_count: int
        """
        
        super(ListServicePublicDetailsResponse, self).__init__()

        self._endpoint_services = None
        self._total_count = None
        self.discriminator = None

        if endpoint_services is not None:
            self.endpoint_services = endpoint_services
        if total_count is not None:
            self.total_count = total_count

    @property
    def endpoint_services(self):
        """Gets the endpoint_services of this ListServicePublicDetailsResponse.

        终端节点服务列表。

        :return: The endpoint_services of this ListServicePublicDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.EndpointService`]
        """
        return self._endpoint_services

    @endpoint_services.setter
    def endpoint_services(self, endpoint_services):
        """Sets the endpoint_services of this ListServicePublicDetailsResponse.

        终端节点服务列表。

        :param endpoint_services: The endpoint_services of this ListServicePublicDetailsResponse.
        :type endpoint_services: list[:class:`huaweicloudsdkvpcep.v1.EndpointService`]
        """
        self._endpoint_services = endpoint_services

    @property
    def total_count(self):
        """Gets the total_count of this ListServicePublicDetailsResponse.

        满足查询条件的公共终端节点服务总条数，不受分页（即limit、offset参数）影响。

        :return: The total_count of this ListServicePublicDetailsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListServicePublicDetailsResponse.

        满足查询条件的公共终端节点服务总条数，不受分页（即limit、offset参数）影响。

        :param total_count: The total_count of this ListServicePublicDetailsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListServicePublicDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
