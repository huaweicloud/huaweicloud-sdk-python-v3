# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseResourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'resources': 'list[DatabaseResourceRsp]',
        'x_resource_mappings': 'str'
    }

    attribute_map = {
        'count': 'count',
        'resources': 'resources',
        'x_resource_mappings': 'X-Resource-Mappings'
    }

    def __init__(self, count=None, resources=None, x_resource_mappings=None):
        """ListDatabaseResourceResponse

        The model defined in huaweicloud sdk

        :param count: 总数
        :type count: int
        :param resources: 数据库资源列表
        :type resources: list[:class:`huaweicloudsdkeihealth.v1.DatabaseResourceRsp`]
        :param x_resource_mappings: 
        :type x_resource_mappings: str
        """
        
        super(ListDatabaseResourceResponse, self).__init__()

        self._count = None
        self._resources = None
        self._x_resource_mappings = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if resources is not None:
            self.resources = resources
        if x_resource_mappings is not None:
            self.x_resource_mappings = x_resource_mappings

    @property
    def count(self):
        """Gets the count of this ListDatabaseResourceResponse.

        总数

        :return: The count of this ListDatabaseResourceResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDatabaseResourceResponse.

        总数

        :param count: The count of this ListDatabaseResourceResponse.
        :type count: int
        """
        self._count = count

    @property
    def resources(self):
        """Gets the resources of this ListDatabaseResourceResponse.

        数据库资源列表

        :return: The resources of this ListDatabaseResourceResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DatabaseResourceRsp`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListDatabaseResourceResponse.

        数据库资源列表

        :param resources: The resources of this ListDatabaseResourceResponse.
        :type resources: list[:class:`huaweicloudsdkeihealth.v1.DatabaseResourceRsp`]
        """
        self._resources = resources

    @property
    def x_resource_mappings(self):
        """Gets the x_resource_mappings of this ListDatabaseResourceResponse.

        :return: The x_resource_mappings of this ListDatabaseResourceResponse.
        :rtype: str
        """
        return self._x_resource_mappings

    @x_resource_mappings.setter
    def x_resource_mappings(self, x_resource_mappings):
        """Sets the x_resource_mappings of this ListDatabaseResourceResponse.

        :param x_resource_mappings: The x_resource_mappings of this ListDatabaseResourceResponse.
        :type x_resource_mappings: str
        """
        self._x_resource_mappings = x_resource_mappings

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
        if not isinstance(other, ListDatabaseResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
