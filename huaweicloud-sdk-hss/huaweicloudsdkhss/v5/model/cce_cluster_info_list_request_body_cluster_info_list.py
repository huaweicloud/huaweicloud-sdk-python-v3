# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CCEClusterInfoListRequestBodyClusterInfoList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'cluster_name': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name'
    }

    def __init__(self, cluster_id=None, cluster_name=None):
        r"""CCEClusterInfoListRequestBodyClusterInfoList

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CCEClusterInfoListRequestBodyClusterInfoList.

        集群id

        :return: The cluster_id of this CCEClusterInfoListRequestBodyClusterInfoList.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CCEClusterInfoListRequestBodyClusterInfoList.

        集群id

        :param cluster_id: The cluster_id of this CCEClusterInfoListRequestBodyClusterInfoList.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CCEClusterInfoListRequestBodyClusterInfoList.

        集群名称

        :return: The cluster_name of this CCEClusterInfoListRequestBodyClusterInfoList.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CCEClusterInfoListRequestBodyClusterInfoList.

        集群名称

        :param cluster_name: The cluster_name of this CCEClusterInfoListRequestBodyClusterInfoList.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

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
        if not isinstance(other, CCEClusterInfoListRequestBodyClusterInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
