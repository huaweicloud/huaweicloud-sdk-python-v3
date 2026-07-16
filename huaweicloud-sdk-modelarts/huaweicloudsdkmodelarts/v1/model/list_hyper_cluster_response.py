# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHyperClusterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hyper_clusters': 'list[HyperCluster]'
    }

    attribute_map = {
        'hyper_clusters': 'hyper_clusters'
    }

    def __init__(self, hyper_clusters=None):
        r"""ListHyperClusterResponse

        The model defined in huaweicloud sdk

        :param hyper_clusters: **参数解释**：Hyper Cluster列表。
        :type hyper_clusters: list[:class:`huaweicloudsdkmodelarts.v1.HyperCluster`]
        """
        
        super().__init__()

        self._hyper_clusters = None
        self.discriminator = None

        if hyper_clusters is not None:
            self.hyper_clusters = hyper_clusters

    @property
    def hyper_clusters(self):
        r"""Gets the hyper_clusters of this ListHyperClusterResponse.

        **参数解释**：Hyper Cluster列表。

        :return: The hyper_clusters of this ListHyperClusterResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.HyperCluster`]
        """
        return self._hyper_clusters

    @hyper_clusters.setter
    def hyper_clusters(self, hyper_clusters):
        r"""Sets the hyper_clusters of this ListHyperClusterResponse.

        **参数解释**：Hyper Cluster列表。

        :param hyper_clusters: The hyper_clusters of this ListHyperClusterResponse.
        :type hyper_clusters: list[:class:`huaweicloudsdkmodelarts.v1.HyperCluster`]
        """
        self._hyper_clusters = hyper_clusters

    def to_dict(self):
        import warnings
        warnings.warn("ListHyperClusterResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListHyperClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
