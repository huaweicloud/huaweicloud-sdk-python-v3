# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatusClusterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'cluster_list': 'list[ShowStatusClusterItem]'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'cluster_list': 'cluster_list'
    }

    def __init__(self, metric_name=None, cluster_list=None):
        r"""ShowStatusClusterResponse

        The model defined in huaweicloud sdk

        :param metric_name: 资源名称
        :type metric_name: str
        :param cluster_list: 集群列表
        :type cluster_list: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusClusterItem`]
        """
        
        super().__init__()

        self._metric_name = None
        self._cluster_list = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if cluster_list is not None:
            self.cluster_list = cluster_list

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowStatusClusterResponse.

        资源名称

        :return: The metric_name of this ShowStatusClusterResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowStatusClusterResponse.

        资源名称

        :param metric_name: The metric_name of this ShowStatusClusterResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def cluster_list(self):
        r"""Gets the cluster_list of this ShowStatusClusterResponse.

        集群列表

        :return: The cluster_list of this ShowStatusClusterResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusClusterItem`]
        """
        return self._cluster_list

    @cluster_list.setter
    def cluster_list(self, cluster_list):
        r"""Sets the cluster_list of this ShowStatusClusterResponse.

        集群列表

        :param cluster_list: The cluster_list of this ShowStatusClusterResponse.
        :type cluster_list: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusClusterItem`]
        """
        self._cluster_list = cluster_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowStatusClusterResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowStatusClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
