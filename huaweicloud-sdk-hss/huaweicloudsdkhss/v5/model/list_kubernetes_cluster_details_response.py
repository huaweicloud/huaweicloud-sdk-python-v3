# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKubernetesClusterDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_update_time': 'int',
        'total_num': 'int',
        'cluster_info_list': 'list[KubernetesClusterInfo]'
    }

    attribute_map = {
        'last_update_time': 'last_update_time',
        'total_num': 'total_num',
        'cluster_info_list': 'cluster_info_list'
    }

    def __init__(self, last_update_time=None, total_num=None, cluster_info_list=None):
        r"""ListKubernetesClusterDetailsResponse

        The model defined in huaweicloud sdk

        :param last_update_time: 最近更新时间
        :type last_update_time: int
        :param total_num: 集群总数
        :type total_num: int
        :param cluster_info_list: 集群列表
        :type cluster_info_list: list[:class:`huaweicloudsdkhss.v5.KubernetesClusterInfo`]
        """
        
        super(ListKubernetesClusterDetailsResponse, self).__init__()

        self._last_update_time = None
        self._total_num = None
        self._cluster_info_list = None
        self.discriminator = None

        if last_update_time is not None:
            self.last_update_time = last_update_time
        if total_num is not None:
            self.total_num = total_num
        if cluster_info_list is not None:
            self.cluster_info_list = cluster_info_list

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this ListKubernetesClusterDetailsResponse.

        最近更新时间

        :return: The last_update_time of this ListKubernetesClusterDetailsResponse.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this ListKubernetesClusterDetailsResponse.

        最近更新时间

        :param last_update_time: The last_update_time of this ListKubernetesClusterDetailsResponse.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def total_num(self):
        r"""Gets the total_num of this ListKubernetesClusterDetailsResponse.

        集群总数

        :return: The total_num of this ListKubernetesClusterDetailsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListKubernetesClusterDetailsResponse.

        集群总数

        :param total_num: The total_num of this ListKubernetesClusterDetailsResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def cluster_info_list(self):
        r"""Gets the cluster_info_list of this ListKubernetesClusterDetailsResponse.

        集群列表

        :return: The cluster_info_list of this ListKubernetesClusterDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.KubernetesClusterInfo`]
        """
        return self._cluster_info_list

    @cluster_info_list.setter
    def cluster_info_list(self, cluster_info_list):
        r"""Sets the cluster_info_list of this ListKubernetesClusterDetailsResponse.

        集群列表

        :param cluster_info_list: The cluster_info_list of this ListKubernetesClusterDetailsResponse.
        :type cluster_info_list: list[:class:`huaweicloudsdkhss.v5.KubernetesClusterInfo`]
        """
        self._cluster_info_list = cluster_info_list

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
        if not isinstance(other, ListKubernetesClusterDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
