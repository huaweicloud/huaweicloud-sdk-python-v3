# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTenantResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources': 'list[ResourceItemInfo]',
        'count': 'float',
        'x_request_id': 'str'
    }

    attribute_map = {
        'resources': 'resources',
        'count': 'count',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, resources=None, count=None, x_request_id=None):
        r"""ListTenantResourcesResponse

        The model defined in huaweicloud sdk

        :param resources: 资源用量列表
        :type resources: list[:class:`huaweicloudsdkmetastudio.v1.ResourceItemInfo`]
        :param count: 资源总数。
        :type count: float
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListTenantResourcesResponse, self).__init__()

        self._resources = None
        self._count = None
        self._x_request_id = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if count is not None:
            self.count = count
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def resources(self):
        r"""Gets the resources of this ListTenantResourcesResponse.

        资源用量列表

        :return: The resources of this ListTenantResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ResourceItemInfo`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListTenantResourcesResponse.

        资源用量列表

        :param resources: The resources of this ListTenantResourcesResponse.
        :type resources: list[:class:`huaweicloudsdkmetastudio.v1.ResourceItemInfo`]
        """
        self._resources = resources

    @property
    def count(self):
        r"""Gets the count of this ListTenantResourcesResponse.

        资源总数。

        :return: The count of this ListTenantResourcesResponse.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListTenantResourcesResponse.

        资源总数。

        :param count: The count of this ListTenantResourcesResponse.
        :type count: float
        """
        self._count = count

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListTenantResourcesResponse.

        :return: The x_request_id of this ListTenantResourcesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListTenantResourcesResponse.

        :param x_request_id: The x_request_id of this ListTenantResourcesResponse.
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
        if not isinstance(other, ListTenantResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
