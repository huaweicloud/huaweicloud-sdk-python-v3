# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetryTaskRequestBodyClusterScanInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'range_type': 'str',
        'cluster_info_list': 'list[RetryTaskRequestBodyClusterScanInfoClusterInfoList]'
    }

    attribute_map = {
        'range_type': 'range_type',
        'cluster_info_list': 'cluster_info_list'
    }

    def __init__(self, range_type=None, cluster_info_list=None):
        r"""RetryTaskRequestBodyClusterScanInfo

        The model defined in huaweicloud sdk

        :param range_type: **参数解释**： 重新扫描的范围 **约束限制**: 必填 **取值范围**: - all_failed_cluster：任务下所有扫描失败的集群。 - specific_cluster：任务下指定扫描失败的集群。  **默认取值**: 不涉及 
        :type range_type: str
        :param cluster_info_list: **参数解释**： 扫描范围为specific_cluster时用于指定重新扫描的集群范围 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值200 
        :type cluster_info_list: list[:class:`huaweicloudsdkhss.v5.RetryTaskRequestBodyClusterScanInfoClusterInfoList`]
        """
        
        

        self._range_type = None
        self._cluster_info_list = None
        self.discriminator = None

        self.range_type = range_type
        if cluster_info_list is not None:
            self.cluster_info_list = cluster_info_list

    @property
    def range_type(self):
        r"""Gets the range_type of this RetryTaskRequestBodyClusterScanInfo.

        **参数解释**： 重新扫描的范围 **约束限制**: 必填 **取值范围**: - all_failed_cluster：任务下所有扫描失败的集群。 - specific_cluster：任务下指定扫描失败的集群。  **默认取值**: 不涉及 

        :return: The range_type of this RetryTaskRequestBodyClusterScanInfo.
        :rtype: str
        """
        return self._range_type

    @range_type.setter
    def range_type(self, range_type):
        r"""Sets the range_type of this RetryTaskRequestBodyClusterScanInfo.

        **参数解释**： 重新扫描的范围 **约束限制**: 必填 **取值范围**: - all_failed_cluster：任务下所有扫描失败的集群。 - specific_cluster：任务下指定扫描失败的集群。  **默认取值**: 不涉及 

        :param range_type: The range_type of this RetryTaskRequestBodyClusterScanInfo.
        :type range_type: str
        """
        self._range_type = range_type

    @property
    def cluster_info_list(self):
        r"""Gets the cluster_info_list of this RetryTaskRequestBodyClusterScanInfo.

        **参数解释**： 扫描范围为specific_cluster时用于指定重新扫描的集群范围 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值200 

        :return: The cluster_info_list of this RetryTaskRequestBodyClusterScanInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.RetryTaskRequestBodyClusterScanInfoClusterInfoList`]
        """
        return self._cluster_info_list

    @cluster_info_list.setter
    def cluster_info_list(self, cluster_info_list):
        r"""Sets the cluster_info_list of this RetryTaskRequestBodyClusterScanInfo.

        **参数解释**： 扫描范围为specific_cluster时用于指定重新扫描的集群范围 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值200 

        :param cluster_info_list: The cluster_info_list of this RetryTaskRequestBodyClusterScanInfo.
        :type cluster_info_list: list[:class:`huaweicloudsdkhss.v5.RetryTaskRequestBodyClusterScanInfoClusterInfoList`]
        """
        self._cluster_info_list = cluster_info_list

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
        if not isinstance(other, RetryTaskRequestBodyClusterScanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
