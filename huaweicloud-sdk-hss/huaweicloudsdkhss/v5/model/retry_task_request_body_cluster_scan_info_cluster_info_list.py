# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetryTaskRequestBodyClusterScanInfoClusterInfoList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'scan_type_list': 'list[str]'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'scan_type_list': 'scan_type_list'
    }

    def __init__(self, cluster_id=None, scan_type_list=None):
        r"""RetryTaskRequestBodyClusterScanInfoClusterInfoList

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type cluster_id: str
        :param scan_type_list: **参数解释**： 该集群重新扫描的扫描项列表，若不指定则重新扫描集群下所有扫描失败的扫描项 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值3 
        :type scan_type_list: list[str]
        """
        
        

        self._cluster_id = None
        self._scan_type_list = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if scan_type_list is not None:
            self.scan_type_list = scan_type_list

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this RetryTaskRequestBodyClusterScanInfoClusterInfoList.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The cluster_id of this RetryTaskRequestBodyClusterScanInfoClusterInfoList.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this RetryTaskRequestBodyClusterScanInfoClusterInfoList.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param cluster_id: The cluster_id of this RetryTaskRequestBodyClusterScanInfoClusterInfoList.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def scan_type_list(self):
        r"""Gets the scan_type_list of this RetryTaskRequestBodyClusterScanInfoClusterInfoList.

        **参数解释**： 该集群重新扫描的扫描项列表，若不指定则重新扫描集群下所有扫描失败的扫描项 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值3 

        :return: The scan_type_list of this RetryTaskRequestBodyClusterScanInfoClusterInfoList.
        :rtype: list[str]
        """
        return self._scan_type_list

    @scan_type_list.setter
    def scan_type_list(self, scan_type_list):
        r"""Sets the scan_type_list of this RetryTaskRequestBodyClusterScanInfoClusterInfoList.

        **参数解释**： 该集群重新扫描的扫描项列表，若不指定则重新扫描集群下所有扫描失败的扫描项 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值3 

        :param scan_type_list: The scan_type_list of this RetryTaskRequestBodyClusterScanInfoClusterInfoList.
        :type scan_type_list: list[str]
        """
        self._scan_type_list = scan_type_list

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
        if not isinstance(other, RetryTaskRequestBodyClusterScanInfoClusterInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
