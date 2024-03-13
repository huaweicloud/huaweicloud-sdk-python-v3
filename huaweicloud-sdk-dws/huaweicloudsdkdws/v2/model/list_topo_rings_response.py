# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopoRingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_rings': 'list[TopoRingInfo]',
        'count': 'int'
    }

    attribute_map = {
        'cluster_rings': 'cluster_rings',
        'count': 'count'
    }

    def __init__(self, cluster_rings=None, count=None):
        """ListTopoRingsResponse

        The model defined in huaweicloud sdk

        :param cluster_rings: 集群拓扑环列表信息
        :type cluster_rings: list[:class:`huaweicloudsdkdws.v2.TopoRingInfo`]
        :param count: 集群环数量
        :type count: int
        """
        
        super(ListTopoRingsResponse, self).__init__()

        self._cluster_rings = None
        self._count = None
        self.discriminator = None

        if cluster_rings is not None:
            self.cluster_rings = cluster_rings
        if count is not None:
            self.count = count

    @property
    def cluster_rings(self):
        """Gets the cluster_rings of this ListTopoRingsResponse.

        集群拓扑环列表信息

        :return: The cluster_rings of this ListTopoRingsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TopoRingInfo`]
        """
        return self._cluster_rings

    @cluster_rings.setter
    def cluster_rings(self, cluster_rings):
        """Sets the cluster_rings of this ListTopoRingsResponse.

        集群拓扑环列表信息

        :param cluster_rings: The cluster_rings of this ListTopoRingsResponse.
        :type cluster_rings: list[:class:`huaweicloudsdkdws.v2.TopoRingInfo`]
        """
        self._cluster_rings = cluster_rings

    @property
    def count(self):
        """Gets the count of this ListTopoRingsResponse.

        集群环数量

        :return: The count of this ListTopoRingsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListTopoRingsResponse.

        集群环数量

        :param count: The count of this ListTopoRingsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListTopoRingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
