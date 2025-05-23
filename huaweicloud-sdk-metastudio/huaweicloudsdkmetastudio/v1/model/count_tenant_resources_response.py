# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountTenantResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources_count': 'list[ResourcesCount]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'resources_count': 'resources_count',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, resources_count=None, x_request_id=None):
        r"""CountTenantResourcesResponse

        The model defined in huaweicloud sdk

        :param resources_count: 资源总数列表
        :type resources_count: list[:class:`huaweicloudsdkmetastudio.v1.ResourcesCount`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CountTenantResourcesResponse, self).__init__()

        self._resources_count = None
        self._x_request_id = None
        self.discriminator = None

        if resources_count is not None:
            self.resources_count = resources_count
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def resources_count(self):
        r"""Gets the resources_count of this CountTenantResourcesResponse.

        资源总数列表

        :return: The resources_count of this CountTenantResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ResourcesCount`]
        """
        return self._resources_count

    @resources_count.setter
    def resources_count(self, resources_count):
        r"""Sets the resources_count of this CountTenantResourcesResponse.

        资源总数列表

        :param resources_count: The resources_count of this CountTenantResourcesResponse.
        :type resources_count: list[:class:`huaweicloudsdkmetastudio.v1.ResourcesCount`]
        """
        self._resources_count = resources_count

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CountTenantResourcesResponse.

        :return: The x_request_id of this CountTenantResourcesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CountTenantResourcesResponse.

        :param x_request_id: The x_request_id of this CountTenantResourcesResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CountTenantResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
