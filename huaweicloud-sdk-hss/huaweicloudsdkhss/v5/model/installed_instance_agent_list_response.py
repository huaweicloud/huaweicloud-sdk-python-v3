# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstalledInstanceAgentListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'access_error_num': 'int',
        'run_error_num': 'int',
        'upgrade_num': 'int',
        'upgrade_failed_num': 'int',
        'cluster_list': 'list[ClusterInfo]',
        'workload_list': 'list[WorkLoadInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'access_error_num': 'access_error_num',
        'run_error_num': 'run_error_num',
        'upgrade_num': 'upgrade_num',
        'upgrade_failed_num': 'upgrade_failed_num',
        'cluster_list': 'cluster_list',
        'workload_list': 'workload_list'
    }

    def __init__(self, total_num=None, access_error_num=None, run_error_num=None, upgrade_num=None, upgrade_failed_num=None, cluster_list=None, workload_list=None):
        r"""InstalledInstanceAgentListResponse

        The model defined in huaweicloud sdk

        :param total_num: **参数解释**: 安装列表总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_num: int
        :param access_error_num: **参数解释**: 安装列表接入异常工作负载/集群个数 **取值范围**: 最小值0，最大值2147483647 
        :type access_error_num: int
        :param run_error_num: **参数解释**: 安装列表运行异常工作负载/集群个数 **取值范围**: 最小值0，最大值2147483647 
        :type run_error_num: int
        :param upgrade_num: **参数解释**: 安装列表待升级Agent数 **取值范围**: 最小值0，最大值2147483647 
        :type upgrade_num: int
        :param upgrade_failed_num: **参数解释**: 安装列表升级失败实例数 **取值范围**: 最小值0，最大值2147483647 
        :type upgrade_failed_num: int
        :param cluster_list: **参数解释**: 集群安装agent列表 **取值范围**: 最小值0，最大值65535 
        :type cluster_list: list[:class:`huaweicloudsdkhss.v5.ClusterInfo`]
        :param workload_list: **参数解释**: 工作负载安装agent列表 **取值范围**: 最小值0，最大值65535 
        :type workload_list: list[:class:`huaweicloudsdkhss.v5.WorkLoadInfo`]
        """
        
        super().__init__()

        self._total_num = None
        self._access_error_num = None
        self._run_error_num = None
        self._upgrade_num = None
        self._upgrade_failed_num = None
        self._cluster_list = None
        self._workload_list = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if access_error_num is not None:
            self.access_error_num = access_error_num
        if run_error_num is not None:
            self.run_error_num = run_error_num
        if upgrade_num is not None:
            self.upgrade_num = upgrade_num
        if upgrade_failed_num is not None:
            self.upgrade_failed_num = upgrade_failed_num
        if cluster_list is not None:
            self.cluster_list = cluster_list
        if workload_list is not None:
            self.workload_list = workload_list

    @property
    def total_num(self):
        r"""Gets the total_num of this InstalledInstanceAgentListResponse.

        **参数解释**: 安装列表总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_num of this InstalledInstanceAgentListResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this InstalledInstanceAgentListResponse.

        **参数解释**: 安装列表总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_num: The total_num of this InstalledInstanceAgentListResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def access_error_num(self):
        r"""Gets the access_error_num of this InstalledInstanceAgentListResponse.

        **参数解释**: 安装列表接入异常工作负载/集群个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The access_error_num of this InstalledInstanceAgentListResponse.
        :rtype: int
        """
        return self._access_error_num

    @access_error_num.setter
    def access_error_num(self, access_error_num):
        r"""Sets the access_error_num of this InstalledInstanceAgentListResponse.

        **参数解释**: 安装列表接入异常工作负载/集群个数 **取值范围**: 最小值0，最大值2147483647 

        :param access_error_num: The access_error_num of this InstalledInstanceAgentListResponse.
        :type access_error_num: int
        """
        self._access_error_num = access_error_num

    @property
    def run_error_num(self):
        r"""Gets the run_error_num of this InstalledInstanceAgentListResponse.

        **参数解释**: 安装列表运行异常工作负载/集群个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The run_error_num of this InstalledInstanceAgentListResponse.
        :rtype: int
        """
        return self._run_error_num

    @run_error_num.setter
    def run_error_num(self, run_error_num):
        r"""Sets the run_error_num of this InstalledInstanceAgentListResponse.

        **参数解释**: 安装列表运行异常工作负载/集群个数 **取值范围**: 最小值0，最大值2147483647 

        :param run_error_num: The run_error_num of this InstalledInstanceAgentListResponse.
        :type run_error_num: int
        """
        self._run_error_num = run_error_num

    @property
    def upgrade_num(self):
        r"""Gets the upgrade_num of this InstalledInstanceAgentListResponse.

        **参数解释**: 安装列表待升级Agent数 **取值范围**: 最小值0，最大值2147483647 

        :return: The upgrade_num of this InstalledInstanceAgentListResponse.
        :rtype: int
        """
        return self._upgrade_num

    @upgrade_num.setter
    def upgrade_num(self, upgrade_num):
        r"""Sets the upgrade_num of this InstalledInstanceAgentListResponse.

        **参数解释**: 安装列表待升级Agent数 **取值范围**: 最小值0，最大值2147483647 

        :param upgrade_num: The upgrade_num of this InstalledInstanceAgentListResponse.
        :type upgrade_num: int
        """
        self._upgrade_num = upgrade_num

    @property
    def upgrade_failed_num(self):
        r"""Gets the upgrade_failed_num of this InstalledInstanceAgentListResponse.

        **参数解释**: 安装列表升级失败实例数 **取值范围**: 最小值0，最大值2147483647 

        :return: The upgrade_failed_num of this InstalledInstanceAgentListResponse.
        :rtype: int
        """
        return self._upgrade_failed_num

    @upgrade_failed_num.setter
    def upgrade_failed_num(self, upgrade_failed_num):
        r"""Sets the upgrade_failed_num of this InstalledInstanceAgentListResponse.

        **参数解释**: 安装列表升级失败实例数 **取值范围**: 最小值0，最大值2147483647 

        :param upgrade_failed_num: The upgrade_failed_num of this InstalledInstanceAgentListResponse.
        :type upgrade_failed_num: int
        """
        self._upgrade_failed_num = upgrade_failed_num

    @property
    def cluster_list(self):
        r"""Gets the cluster_list of this InstalledInstanceAgentListResponse.

        **参数解释**: 集群安装agent列表 **取值范围**: 最小值0，最大值65535 

        :return: The cluster_list of this InstalledInstanceAgentListResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterInfo`]
        """
        return self._cluster_list

    @cluster_list.setter
    def cluster_list(self, cluster_list):
        r"""Sets the cluster_list of this InstalledInstanceAgentListResponse.

        **参数解释**: 集群安装agent列表 **取值范围**: 最小值0，最大值65535 

        :param cluster_list: The cluster_list of this InstalledInstanceAgentListResponse.
        :type cluster_list: list[:class:`huaweicloudsdkhss.v5.ClusterInfo`]
        """
        self._cluster_list = cluster_list

    @property
    def workload_list(self):
        r"""Gets the workload_list of this InstalledInstanceAgentListResponse.

        **参数解释**: 工作负载安装agent列表 **取值范围**: 最小值0，最大值65535 

        :return: The workload_list of this InstalledInstanceAgentListResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.WorkLoadInfo`]
        """
        return self._workload_list

    @workload_list.setter
    def workload_list(self, workload_list):
        r"""Sets the workload_list of this InstalledInstanceAgentListResponse.

        **参数解释**: 工作负载安装agent列表 **取值范围**: 最小值0，最大值65535 

        :param workload_list: The workload_list of this InstalledInstanceAgentListResponse.
        :type workload_list: list[:class:`huaweicloudsdkhss.v5.WorkLoadInfo`]
        """
        self._workload_list = workload_list

    def to_dict(self):
        import warnings
        warnings.warn("InstalledInstanceAgentListResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, InstalledInstanceAgentListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
