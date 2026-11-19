# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceProtectionsResponse(SdkResponse):

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
        'cluster_list': 'list[ClusterInfo]',
        'workload_list': 'list[WorkLoadInfo]',
        'instance_list': 'list[ServerlessInstanceInfo]',
        'risk_num': 'int',
        'abnormal_num': 'int',
        'unprotect_num': 'int',
        'instance_num': 'int'
    }

    attribute_map = {
        'total_num': 'total_num',
        'cluster_list': 'cluster_list',
        'workload_list': 'workload_list',
        'instance_list': 'instance_list',
        'risk_num': 'risk_num',
        'abnormal_num': 'abnormal_num',
        'unprotect_num': 'unprotect_num',
        'instance_num': 'instance_num'
    }

    def __init__(self, total_num=None, cluster_list=None, workload_list=None, instance_list=None, risk_num=None, abnormal_num=None, unprotect_num=None, instance_num=None):
        r"""ListInstanceProtectionsResponse

        The model defined in huaweicloud sdk

        :param total_num: **参数解释**: 防护列表总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_num: int
        :param cluster_list: **参数解释**: 集群防护列表 **取值范围**: 最小值0，最大值65535 
        :type cluster_list: list[:class:`huaweicloudsdkhss.v5.ClusterInfo`]
        :param workload_list: **参数解释**: 工作负载防护列表 **取值范围**: 最小值0，最大值65535 
        :type workload_list: list[:class:`huaweicloudsdkhss.v5.WorkLoadInfo`]
        :param instance_list: **参数解释**: 实例防护列表 **取值范围**: 最小值0，最大值65535 
        :type instance_list: list[:class:`huaweicloudsdkhss.v5.ServerlessInstanceInfo`]
        :param risk_num: **参数解释**: 有风险实例数 **取值范围**: 最小值0，最大值2147483647 
        :type risk_num: int
        :param abnormal_num: **参数解释**: 防护异常数 **取值范围**: 最小值0，最大值2147483647 
        :type abnormal_num: int
        :param unprotect_num: **参数解释**: 未防护实例数 **取值范围**: 最小值0，最大值2147483647 
        :type unprotect_num: int
        :param instance_num: **参数解释**: 全部实例数 **取值范围**: 最小值0，最大值2147483647 
        :type instance_num: int
        """
        
        super().__init__()

        self._total_num = None
        self._cluster_list = None
        self._workload_list = None
        self._instance_list = None
        self._risk_num = None
        self._abnormal_num = None
        self._unprotect_num = None
        self._instance_num = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if cluster_list is not None:
            self.cluster_list = cluster_list
        if workload_list is not None:
            self.workload_list = workload_list
        if instance_list is not None:
            self.instance_list = instance_list
        if risk_num is not None:
            self.risk_num = risk_num
        if abnormal_num is not None:
            self.abnormal_num = abnormal_num
        if unprotect_num is not None:
            self.unprotect_num = unprotect_num
        if instance_num is not None:
            self.instance_num = instance_num

    @property
    def total_num(self):
        r"""Gets the total_num of this ListInstanceProtectionsResponse.

        **参数解释**: 防护列表总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_num of this ListInstanceProtectionsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListInstanceProtectionsResponse.

        **参数解释**: 防护列表总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_num: The total_num of this ListInstanceProtectionsResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def cluster_list(self):
        r"""Gets the cluster_list of this ListInstanceProtectionsResponse.

        **参数解释**: 集群防护列表 **取值范围**: 最小值0，最大值65535 

        :return: The cluster_list of this ListInstanceProtectionsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterInfo`]
        """
        return self._cluster_list

    @cluster_list.setter
    def cluster_list(self, cluster_list):
        r"""Sets the cluster_list of this ListInstanceProtectionsResponse.

        **参数解释**: 集群防护列表 **取值范围**: 最小值0，最大值65535 

        :param cluster_list: The cluster_list of this ListInstanceProtectionsResponse.
        :type cluster_list: list[:class:`huaweicloudsdkhss.v5.ClusterInfo`]
        """
        self._cluster_list = cluster_list

    @property
    def workload_list(self):
        r"""Gets the workload_list of this ListInstanceProtectionsResponse.

        **参数解释**: 工作负载防护列表 **取值范围**: 最小值0，最大值65535 

        :return: The workload_list of this ListInstanceProtectionsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.WorkLoadInfo`]
        """
        return self._workload_list

    @workload_list.setter
    def workload_list(self, workload_list):
        r"""Sets the workload_list of this ListInstanceProtectionsResponse.

        **参数解释**: 工作负载防护列表 **取值范围**: 最小值0，最大值65535 

        :param workload_list: The workload_list of this ListInstanceProtectionsResponse.
        :type workload_list: list[:class:`huaweicloudsdkhss.v5.WorkLoadInfo`]
        """
        self._workload_list = workload_list

    @property
    def instance_list(self):
        r"""Gets the instance_list of this ListInstanceProtectionsResponse.

        **参数解释**: 实例防护列表 **取值范围**: 最小值0，最大值65535 

        :return: The instance_list of this ListInstanceProtectionsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ServerlessInstanceInfo`]
        """
        return self._instance_list

    @instance_list.setter
    def instance_list(self, instance_list):
        r"""Sets the instance_list of this ListInstanceProtectionsResponse.

        **参数解释**: 实例防护列表 **取值范围**: 最小值0，最大值65535 

        :param instance_list: The instance_list of this ListInstanceProtectionsResponse.
        :type instance_list: list[:class:`huaweicloudsdkhss.v5.ServerlessInstanceInfo`]
        """
        self._instance_list = instance_list

    @property
    def risk_num(self):
        r"""Gets the risk_num of this ListInstanceProtectionsResponse.

        **参数解释**: 有风险实例数 **取值范围**: 最小值0，最大值2147483647 

        :return: The risk_num of this ListInstanceProtectionsResponse.
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        r"""Sets the risk_num of this ListInstanceProtectionsResponse.

        **参数解释**: 有风险实例数 **取值范围**: 最小值0，最大值2147483647 

        :param risk_num: The risk_num of this ListInstanceProtectionsResponse.
        :type risk_num: int
        """
        self._risk_num = risk_num

    @property
    def abnormal_num(self):
        r"""Gets the abnormal_num of this ListInstanceProtectionsResponse.

        **参数解释**: 防护异常数 **取值范围**: 最小值0，最大值2147483647 

        :return: The abnormal_num of this ListInstanceProtectionsResponse.
        :rtype: int
        """
        return self._abnormal_num

    @abnormal_num.setter
    def abnormal_num(self, abnormal_num):
        r"""Sets the abnormal_num of this ListInstanceProtectionsResponse.

        **参数解释**: 防护异常数 **取值范围**: 最小值0，最大值2147483647 

        :param abnormal_num: The abnormal_num of this ListInstanceProtectionsResponse.
        :type abnormal_num: int
        """
        self._abnormal_num = abnormal_num

    @property
    def unprotect_num(self):
        r"""Gets the unprotect_num of this ListInstanceProtectionsResponse.

        **参数解释**: 未防护实例数 **取值范围**: 最小值0，最大值2147483647 

        :return: The unprotect_num of this ListInstanceProtectionsResponse.
        :rtype: int
        """
        return self._unprotect_num

    @unprotect_num.setter
    def unprotect_num(self, unprotect_num):
        r"""Sets the unprotect_num of this ListInstanceProtectionsResponse.

        **参数解释**: 未防护实例数 **取值范围**: 最小值0，最大值2147483647 

        :param unprotect_num: The unprotect_num of this ListInstanceProtectionsResponse.
        :type unprotect_num: int
        """
        self._unprotect_num = unprotect_num

    @property
    def instance_num(self):
        r"""Gets the instance_num of this ListInstanceProtectionsResponse.

        **参数解释**: 全部实例数 **取值范围**: 最小值0，最大值2147483647 

        :return: The instance_num of this ListInstanceProtectionsResponse.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        r"""Sets the instance_num of this ListInstanceProtectionsResponse.

        **参数解释**: 全部实例数 **取值范围**: 最小值0，最大值2147483647 

        :param instance_num: The instance_num of this ListInstanceProtectionsResponse.
        :type instance_num: int
        """
        self._instance_num = instance_num

    def to_dict(self):
        import warnings
        warnings.warn("ListInstanceProtectionsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListInstanceProtectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
