# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeCloudResponse(SdkResponse):

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
        'edgeclouds': 'list[EdgeCloud]'
    }

    attribute_map = {
        'count': 'count',
        'edgeclouds': 'edgeclouds'
    }

    def __init__(self, count=None, edgeclouds=None):
        """ListEdgeCloudResponse

        The model defined in huaweicloud sdk

        :param count: 边缘业务数量。
        :type count: int
        :param edgeclouds: 边缘业务列表。
        :type edgeclouds: list[:class:`huaweicloudsdkiec.v1.EdgeCloud`]
        """
        
        super(ListEdgeCloudResponse, self).__init__()

        self._count = None
        self._edgeclouds = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if edgeclouds is not None:
            self.edgeclouds = edgeclouds

    @property
    def count(self):
        """Gets the count of this ListEdgeCloudResponse.

        边缘业务数量。

        :return: The count of this ListEdgeCloudResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListEdgeCloudResponse.

        边缘业务数量。

        :param count: The count of this ListEdgeCloudResponse.
        :type count: int
        """
        self._count = count

    @property
    def edgeclouds(self):
        """Gets the edgeclouds of this ListEdgeCloudResponse.

        边缘业务列表。

        :return: The edgeclouds of this ListEdgeCloudResponse.
        :rtype: list[:class:`huaweicloudsdkiec.v1.EdgeCloud`]
        """
        return self._edgeclouds

    @edgeclouds.setter
    def edgeclouds(self, edgeclouds):
        """Sets the edgeclouds of this ListEdgeCloudResponse.

        边缘业务列表。

        :param edgeclouds: The edgeclouds of this ListEdgeCloudResponse.
        :type edgeclouds: list[:class:`huaweicloudsdkiec.v1.EdgeCloud`]
        """
        self._edgeclouds = edgeclouds

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
        if not isinstance(other, ListEdgeCloudResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
