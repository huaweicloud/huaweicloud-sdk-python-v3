# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterAssetStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_num': 'int',
        'work_load_num': 'int',
        'service_num': 'int',
        'pod_num': 'int'
    }

    attribute_map = {
        'cluster_num': 'cluster_num',
        'work_load_num': 'work_load_num',
        'service_num': 'service_num',
        'pod_num': 'pod_num'
    }

    def __init__(self, cluster_num=None, work_load_num=None, service_num=None, pod_num=None):
        r"""ShowClusterAssetStatisticsResponse

        The model defined in huaweicloud sdk

        :param cluster_num: 集群数量
        :type cluster_num: int
        :param work_load_num: 工作负载数量
        :type work_load_num: int
        :param service_num: 服务数量
        :type service_num: int
        :param pod_num: pod数量
        :type pod_num: int
        """
        
        super(ShowClusterAssetStatisticsResponse, self).__init__()

        self._cluster_num = None
        self._work_load_num = None
        self._service_num = None
        self._pod_num = None
        self.discriminator = None

        if cluster_num is not None:
            self.cluster_num = cluster_num
        if work_load_num is not None:
            self.work_load_num = work_load_num
        if service_num is not None:
            self.service_num = service_num
        if pod_num is not None:
            self.pod_num = pod_num

    @property
    def cluster_num(self):
        r"""Gets the cluster_num of this ShowClusterAssetStatisticsResponse.

        集群数量

        :return: The cluster_num of this ShowClusterAssetStatisticsResponse.
        :rtype: int
        """
        return self._cluster_num

    @cluster_num.setter
    def cluster_num(self, cluster_num):
        r"""Sets the cluster_num of this ShowClusterAssetStatisticsResponse.

        集群数量

        :param cluster_num: The cluster_num of this ShowClusterAssetStatisticsResponse.
        :type cluster_num: int
        """
        self._cluster_num = cluster_num

    @property
    def work_load_num(self):
        r"""Gets the work_load_num of this ShowClusterAssetStatisticsResponse.

        工作负载数量

        :return: The work_load_num of this ShowClusterAssetStatisticsResponse.
        :rtype: int
        """
        return self._work_load_num

    @work_load_num.setter
    def work_load_num(self, work_load_num):
        r"""Sets the work_load_num of this ShowClusterAssetStatisticsResponse.

        工作负载数量

        :param work_load_num: The work_load_num of this ShowClusterAssetStatisticsResponse.
        :type work_load_num: int
        """
        self._work_load_num = work_load_num

    @property
    def service_num(self):
        r"""Gets the service_num of this ShowClusterAssetStatisticsResponse.

        服务数量

        :return: The service_num of this ShowClusterAssetStatisticsResponse.
        :rtype: int
        """
        return self._service_num

    @service_num.setter
    def service_num(self, service_num):
        r"""Sets the service_num of this ShowClusterAssetStatisticsResponse.

        服务数量

        :param service_num: The service_num of this ShowClusterAssetStatisticsResponse.
        :type service_num: int
        """
        self._service_num = service_num

    @property
    def pod_num(self):
        r"""Gets the pod_num of this ShowClusterAssetStatisticsResponse.

        pod数量

        :return: The pod_num of this ShowClusterAssetStatisticsResponse.
        :rtype: int
        """
        return self._pod_num

    @pod_num.setter
    def pod_num(self, pod_num):
        r"""Sets the pod_num of this ShowClusterAssetStatisticsResponse.

        pod数量

        :param pod_num: The pod_num of this ShowClusterAssetStatisticsResponse.
        :type pod_num: int
        """
        self._pod_num = pod_num

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
        if not isinstance(other, ShowClusterAssetStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
