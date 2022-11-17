# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster': 'Cluster'
    }

    attribute_map = {
        'cluster': 'cluster'
    }

    def __init__(self, cluster=None):
        """CreateClusterResponse

        The model defined in huaweicloud sdk

        :param cluster: 
        :type cluster: :class:`huaweicloudsdkdws.v2.Cluster`
        """
        
        super(CreateClusterResponse, self).__init__()

        self._cluster = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster

    @property
    def cluster(self):
        """Gets the cluster of this CreateClusterResponse.

        :return: The cluster of this CreateClusterResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.Cluster`
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this CreateClusterResponse.

        :param cluster: The cluster of this CreateClusterResponse.
        :type cluster: :class:`huaweicloudsdkdws.v2.Cluster`
        """
        self._cluster = cluster

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
        if not isinstance(other, CreateClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
