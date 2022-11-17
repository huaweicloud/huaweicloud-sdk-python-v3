# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeNodeCertsResponse(SdkResponse):

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
        'node_certs': 'list[NodeCert]'
    }

    attribute_map = {
        'count': 'count',
        'node_certs': 'node_certs'
    }

    def __init__(self, count=None, node_certs=None):
        """ListEdgeNodeCertsResponse

        The model defined in huaweicloud sdk

        :param count: 节点上已关联的应用证书和设备证书的数目
        :type count: int
        :param node_certs: 节点上的证书列表
        :type node_certs: list[:class:`huaweicloudsdkief.v1.NodeCert`]
        """
        
        super(ListEdgeNodeCertsResponse, self).__init__()

        self._count = None
        self._node_certs = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if node_certs is not None:
            self.node_certs = node_certs

    @property
    def count(self):
        """Gets the count of this ListEdgeNodeCertsResponse.

        节点上已关联的应用证书和设备证书的数目

        :return: The count of this ListEdgeNodeCertsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListEdgeNodeCertsResponse.

        节点上已关联的应用证书和设备证书的数目

        :param count: The count of this ListEdgeNodeCertsResponse.
        :type count: int
        """
        self._count = count

    @property
    def node_certs(self):
        """Gets the node_certs of this ListEdgeNodeCertsResponse.

        节点上的证书列表

        :return: The node_certs of this ListEdgeNodeCertsResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.NodeCert`]
        """
        return self._node_certs

    @node_certs.setter
    def node_certs(self, node_certs):
        """Sets the node_certs of this ListEdgeNodeCertsResponse.

        节点上的证书列表

        :param node_certs: The node_certs of this ListEdgeNodeCertsResponse.
        :type node_certs: list[:class:`huaweicloudsdkief.v1.NodeCert`]
        """
        self._node_certs = node_certs

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
        if not isinstance(other, ListEdgeNodeCertsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
