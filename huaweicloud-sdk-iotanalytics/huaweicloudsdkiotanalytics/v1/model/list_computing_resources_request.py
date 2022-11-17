# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListComputingResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'computing_resource_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'computing_resource_name': 'computing_resource_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, computing_resource_name=None, offset=None, limit=None):
        """ListComputingResourcesRequest

        The model defined in huaweicloud sdk

        :param computing_resource_name: 计算资源名称。
        :type computing_resource_name: str
        :param offset: 当前偏移量，默认为0。
        :type offset: int
        :param limit: 每页显示的最大作业个数，范围: [1, 100]。默认值：10。
        :type limit: int
        """
        
        

        self._computing_resource_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if computing_resource_name is not None:
            self.computing_resource_name = computing_resource_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def computing_resource_name(self):
        """Gets the computing_resource_name of this ListComputingResourcesRequest.

        计算资源名称。

        :return: The computing_resource_name of this ListComputingResourcesRequest.
        :rtype: str
        """
        return self._computing_resource_name

    @computing_resource_name.setter
    def computing_resource_name(self, computing_resource_name):
        """Sets the computing_resource_name of this ListComputingResourcesRequest.

        计算资源名称。

        :param computing_resource_name: The computing_resource_name of this ListComputingResourcesRequest.
        :type computing_resource_name: str
        """
        self._computing_resource_name = computing_resource_name

    @property
    def offset(self):
        """Gets the offset of this ListComputingResourcesRequest.

        当前偏移量，默认为0。

        :return: The offset of this ListComputingResourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListComputingResourcesRequest.

        当前偏移量，默认为0。

        :param offset: The offset of this ListComputingResourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListComputingResourcesRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：10。

        :return: The limit of this ListComputingResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListComputingResourcesRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：10。

        :param limit: The limit of this ListComputingResourcesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListComputingResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
