# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetClusterFlavorSpecsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_flavor_specs': 'ClusterFlavorSpecification'
    }

    attribute_map = {
        'cluster_flavor_specs': 'clusterFlavorSpecs'
    }

    def __init__(self, cluster_flavor_specs=None):
        r"""GetClusterFlavorSpecsResponse

        The model defined in huaweicloud sdk

        :param cluster_flavor_specs: 
        :type cluster_flavor_specs: :class:`huaweicloudsdkcce.v3.ClusterFlavorSpecification`
        """
        
        super().__init__()

        self._cluster_flavor_specs = None
        self.discriminator = None

        if cluster_flavor_specs is not None:
            self.cluster_flavor_specs = cluster_flavor_specs

    @property
    def cluster_flavor_specs(self):
        r"""Gets the cluster_flavor_specs of this GetClusterFlavorSpecsResponse.

        :return: The cluster_flavor_specs of this GetClusterFlavorSpecsResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.ClusterFlavorSpecification`
        """
        return self._cluster_flavor_specs

    @cluster_flavor_specs.setter
    def cluster_flavor_specs(self, cluster_flavor_specs):
        r"""Sets the cluster_flavor_specs of this GetClusterFlavorSpecsResponse.

        :param cluster_flavor_specs: The cluster_flavor_specs of this GetClusterFlavorSpecsResponse.
        :type cluster_flavor_specs: :class:`huaweicloudsdkcce.v3.ClusterFlavorSpecification`
        """
        self._cluster_flavor_specs = cluster_flavor_specs

    def to_dict(self):
        import warnings
        warnings.warn("GetClusterFlavorSpecsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GetClusterFlavorSpecsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
