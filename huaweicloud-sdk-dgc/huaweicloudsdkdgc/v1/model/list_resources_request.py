# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'resource_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'resource_name': 'resourceName'
    }

    def __init__(self, workspace=None, limit=None, offset=None, resource_name=None):
        """ListResourcesRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param limit: 分页参数:每页限定数量
        :type limit: int
        :param offset: 分页参数：页数
        :type offset: int
        :param resource_name: 资源名称
        :type resource_name: str
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._resource_name = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def workspace(self):
        """Gets the workspace of this ListResourcesRequest.

        工作空间id

        :return: The workspace of this ListResourcesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListResourcesRequest.

        工作空间id

        :param workspace: The workspace of this ListResourcesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        """Gets the limit of this ListResourcesRequest.

        分页参数:每页限定数量

        :return: The limit of this ListResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourcesRequest.

        分页参数:每页限定数量

        :param limit: The limit of this ListResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListResourcesRequest.

        分页参数：页数

        :return: The offset of this ListResourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListResourcesRequest.

        分页参数：页数

        :param offset: The offset of this ListResourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def resource_name(self):
        """Gets the resource_name of this ListResourcesRequest.

        资源名称

        :return: The resource_name of this ListResourcesRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListResourcesRequest.

        资源名称

        :param resource_name: The resource_name of this ListResourcesRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, ListResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
