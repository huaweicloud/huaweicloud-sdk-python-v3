# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterAffinity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_names': 'list[str]',
        'exclude': 'list[str]'
    }

    attribute_map = {
        'cluster_names': 'clusterNames',
        'exclude': 'exclude'
    }

    def __init__(self, cluster_names=None, exclude=None):
        r"""ClusterAffinity

        The model defined in huaweicloud sdk

        :param cluster_names: 指定要选择的集群名称列表
        :type cluster_names: list[str]
        :param exclude: 指定要排除的集群名称列表
        :type exclude: list[str]
        """
        
        

        self._cluster_names = None
        self._exclude = None
        self.discriminator = None

        if cluster_names is not None:
            self.cluster_names = cluster_names
        if exclude is not None:
            self.exclude = exclude

    @property
    def cluster_names(self):
        r"""Gets the cluster_names of this ClusterAffinity.

        指定要选择的集群名称列表

        :return: The cluster_names of this ClusterAffinity.
        :rtype: list[str]
        """
        return self._cluster_names

    @cluster_names.setter
    def cluster_names(self, cluster_names):
        r"""Sets the cluster_names of this ClusterAffinity.

        指定要选择的集群名称列表

        :param cluster_names: The cluster_names of this ClusterAffinity.
        :type cluster_names: list[str]
        """
        self._cluster_names = cluster_names

    @property
    def exclude(self):
        r"""Gets the exclude of this ClusterAffinity.

        指定要排除的集群名称列表

        :return: The exclude of this ClusterAffinity.
        :rtype: list[str]
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        r"""Sets the exclude of this ClusterAffinity.

        指定要排除的集群名称列表

        :param exclude: The exclude of this ClusterAffinity.
        :type exclude: list[str]
        """
        self._exclude = exclude

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClusterAffinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
