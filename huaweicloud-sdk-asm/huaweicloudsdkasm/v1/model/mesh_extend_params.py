# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MeshExtendParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clusters': 'list[MeshCluster]'
    }

    attribute_map = {
        'clusters': 'clusters'
    }

    def __init__(self, clusters=None):
        r"""MeshExtendParams

        The model defined in huaweicloud sdk

        :param clusters: 网格内集群信息
        :type clusters: list[:class:`huaweicloudsdkasm.v1.MeshCluster`]
        """
        
        

        self._clusters = None
        self.discriminator = None

        if clusters is not None:
            self.clusters = clusters

    @property
    def clusters(self):
        r"""Gets the clusters of this MeshExtendParams.

        网格内集群信息

        :return: The clusters of this MeshExtendParams.
        :rtype: list[:class:`huaweicloudsdkasm.v1.MeshCluster`]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this MeshExtendParams.

        网格内集群信息

        :param clusters: The clusters of this MeshExtendParams.
        :type clusters: list[:class:`huaweicloudsdkasm.v1.MeshCluster`]
        """
        self._clusters = clusters

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
        if not isinstance(other, MeshExtendParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
