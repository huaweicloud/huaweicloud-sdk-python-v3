# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskResourcesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_type': 'str',
        'cluster_scan_info': 'ListTaskResourcesRequestBodyClusterScanInfo',
        'iac_scan_info': 'ListTaskResourcesRequestBodyIacScanInfo'
    }

    attribute_map = {
        'task_type': 'task_type',
        'cluster_scan_info': 'cluster_scan_info',
        'iac_scan_info': 'iac_scan_info'
    }

    def __init__(self, task_type=None, cluster_scan_info=None, iac_scan_info=None):
        r"""ListTaskResourcesRequestBody

        The model defined in huaweicloud sdk

        :param task_type: 任务类型，包含如下   - cluster_scan：集群扫描   - iac_scan：iac扫描
        :type task_type: str
        :param cluster_scan_info: 
        :type cluster_scan_info: :class:`huaweicloudsdkhss.v5.ListTaskResourcesRequestBodyClusterScanInfo`
        :param iac_scan_info: 
        :type iac_scan_info: :class:`huaweicloudsdkhss.v5.ListTaskResourcesRequestBodyIacScanInfo`
        """
        
        

        self._task_type = None
        self._cluster_scan_info = None
        self._iac_scan_info = None
        self.discriminator = None

        self.task_type = task_type
        if cluster_scan_info is not None:
            self.cluster_scan_info = cluster_scan_info
        if iac_scan_info is not None:
            self.iac_scan_info = iac_scan_info

    @property
    def task_type(self):
        r"""Gets the task_type of this ListTaskResourcesRequestBody.

        任务类型，包含如下   - cluster_scan：集群扫描   - iac_scan：iac扫描

        :return: The task_type of this ListTaskResourcesRequestBody.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListTaskResourcesRequestBody.

        任务类型，包含如下   - cluster_scan：集群扫描   - iac_scan：iac扫描

        :param task_type: The task_type of this ListTaskResourcesRequestBody.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def cluster_scan_info(self):
        r"""Gets the cluster_scan_info of this ListTaskResourcesRequestBody.

        :return: The cluster_scan_info of this ListTaskResourcesRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.ListTaskResourcesRequestBodyClusterScanInfo`
        """
        return self._cluster_scan_info

    @cluster_scan_info.setter
    def cluster_scan_info(self, cluster_scan_info):
        r"""Sets the cluster_scan_info of this ListTaskResourcesRequestBody.

        :param cluster_scan_info: The cluster_scan_info of this ListTaskResourcesRequestBody.
        :type cluster_scan_info: :class:`huaweicloudsdkhss.v5.ListTaskResourcesRequestBodyClusterScanInfo`
        """
        self._cluster_scan_info = cluster_scan_info

    @property
    def iac_scan_info(self):
        r"""Gets the iac_scan_info of this ListTaskResourcesRequestBody.

        :return: The iac_scan_info of this ListTaskResourcesRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.ListTaskResourcesRequestBodyIacScanInfo`
        """
        return self._iac_scan_info

    @iac_scan_info.setter
    def iac_scan_info(self, iac_scan_info):
        r"""Sets the iac_scan_info of this ListTaskResourcesRequestBody.

        :param iac_scan_info: The iac_scan_info of this ListTaskResourcesRequestBody.
        :type iac_scan_info: :class:`huaweicloudsdkhss.v5.ListTaskResourcesRequestBodyIacScanInfo`
        """
        self._iac_scan_info = iac_scan_info

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
        if not isinstance(other, ListTaskResourcesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
