# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClusterGroupAssociatedClustersRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_ids': 'list[str]'
    }

    attribute_map = {
        'cluster_ids': 'clusterIds'
    }

    def __init__(self, cluster_ids=None):
        r"""UpdateClusterGroupAssociatedClustersRequestBody

        The model defined in huaweicloud sdk

        :param cluster_ids: 更新容器舰队关联集群信息。
        :type cluster_ids: list[str]
        """
        
        

        self._cluster_ids = None
        self.discriminator = None

        if cluster_ids is not None:
            self.cluster_ids = cluster_ids

    @property
    def cluster_ids(self):
        r"""Gets the cluster_ids of this UpdateClusterGroupAssociatedClustersRequestBody.

        更新容器舰队关联集群信息。

        :return: The cluster_ids of this UpdateClusterGroupAssociatedClustersRequestBody.
        :rtype: list[str]
        """
        return self._cluster_ids

    @cluster_ids.setter
    def cluster_ids(self, cluster_ids):
        r"""Sets the cluster_ids of this UpdateClusterGroupAssociatedClustersRequestBody.

        更新容器舰队关联集群信息。

        :param cluster_ids: The cluster_ids of this UpdateClusterGroupAssociatedClustersRequestBody.
        :type cluster_ids: list[str]
        """
        self._cluster_ids = cluster_ids

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
        if not isinstance(other, UpdateClusterGroupAssociatedClustersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
