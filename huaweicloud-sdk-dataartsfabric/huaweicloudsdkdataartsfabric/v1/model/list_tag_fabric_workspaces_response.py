# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagFabricWorkspacesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources': 'list[TagFabricWorkspace]',
        'total_count': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'resources': 'resources',
        'total_count': 'total_count',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, resources=None, total_count=None, x_request_id=None):
        """ListTagFabricWorkspacesResponse

        The model defined in huaweicloud sdk

        :param resources: 资源列表。
        :type resources: list[:class:`huaweicloudsdkdataartsfabric.v1.TagFabricWorkspace`]
        :param total_count: 资源总数
        :type total_count: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListTagFabricWorkspacesResponse, self).__init__()

        self._resources = None
        self._total_count = None
        self._x_request_id = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if total_count is not None:
            self.total_count = total_count
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def resources(self):
        """Gets the resources of this ListTagFabricWorkspacesResponse.

        资源列表。

        :return: The resources of this ListTagFabricWorkspacesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.TagFabricWorkspace`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListTagFabricWorkspacesResponse.

        资源列表。

        :param resources: The resources of this ListTagFabricWorkspacesResponse.
        :type resources: list[:class:`huaweicloudsdkdataartsfabric.v1.TagFabricWorkspace`]
        """
        self._resources = resources

    @property
    def total_count(self):
        """Gets the total_count of this ListTagFabricWorkspacesResponse.

        资源总数

        :return: The total_count of this ListTagFabricWorkspacesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListTagFabricWorkspacesResponse.

        资源总数

        :param total_count: The total_count of this ListTagFabricWorkspacesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListTagFabricWorkspacesResponse.

        :return: The x_request_id of this ListTagFabricWorkspacesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListTagFabricWorkspacesResponse.

        :param x_request_id: The x_request_id of this ListTagFabricWorkspacesResponse.
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
        if not isinstance(other, ListTagFabricWorkspacesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
