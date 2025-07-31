# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTaskRequestBodyClusterScanInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_type_list': 'list[str]',
        'range_type': 'str',
        'cluster_id_list': 'list[str]'
    }

    attribute_map = {
        'scan_type_list': 'scan_type_list',
        'range_type': 'range_type',
        'cluster_id_list': 'cluster_id_list'
    }

    def __init__(self, scan_type_list=None, range_type=None, cluster_id_list=None):
        r"""CreateTaskRequestBodyClusterScanInfo

        The model defined in huaweicloud sdk

        :param scan_type_list: 扫描项类型
        :type scan_type_list: list[str]
        :param range_type: 扫描范围类型，包含如下   - all_cluster：扫描所有符合扫描条件的集群   - specific_cluster: 扫描指定集群
        :type range_type: str
        :param cluster_id_list: 需要扫描的集群id列表，扫描范围类型为“specific_cluster”时必传
        :type cluster_id_list: list[str]
        """
        
        

        self._scan_type_list = None
        self._range_type = None
        self._cluster_id_list = None
        self.discriminator = None

        self.scan_type_list = scan_type_list
        self.range_type = range_type
        if cluster_id_list is not None:
            self.cluster_id_list = cluster_id_list

    @property
    def scan_type_list(self):
        r"""Gets the scan_type_list of this CreateTaskRequestBodyClusterScanInfo.

        扫描项类型

        :return: The scan_type_list of this CreateTaskRequestBodyClusterScanInfo.
        :rtype: list[str]
        """
        return self._scan_type_list

    @scan_type_list.setter
    def scan_type_list(self, scan_type_list):
        r"""Sets the scan_type_list of this CreateTaskRequestBodyClusterScanInfo.

        扫描项类型

        :param scan_type_list: The scan_type_list of this CreateTaskRequestBodyClusterScanInfo.
        :type scan_type_list: list[str]
        """
        self._scan_type_list = scan_type_list

    @property
    def range_type(self):
        r"""Gets the range_type of this CreateTaskRequestBodyClusterScanInfo.

        扫描范围类型，包含如下   - all_cluster：扫描所有符合扫描条件的集群   - specific_cluster: 扫描指定集群

        :return: The range_type of this CreateTaskRequestBodyClusterScanInfo.
        :rtype: str
        """
        return self._range_type

    @range_type.setter
    def range_type(self, range_type):
        r"""Sets the range_type of this CreateTaskRequestBodyClusterScanInfo.

        扫描范围类型，包含如下   - all_cluster：扫描所有符合扫描条件的集群   - specific_cluster: 扫描指定集群

        :param range_type: The range_type of this CreateTaskRequestBodyClusterScanInfo.
        :type range_type: str
        """
        self._range_type = range_type

    @property
    def cluster_id_list(self):
        r"""Gets the cluster_id_list of this CreateTaskRequestBodyClusterScanInfo.

        需要扫描的集群id列表，扫描范围类型为“specific_cluster”时必传

        :return: The cluster_id_list of this CreateTaskRequestBodyClusterScanInfo.
        :rtype: list[str]
        """
        return self._cluster_id_list

    @cluster_id_list.setter
    def cluster_id_list(self, cluster_id_list):
        r"""Sets the cluster_id_list of this CreateTaskRequestBodyClusterScanInfo.

        需要扫描的集群id列表，扫描范围类型为“specific_cluster”时必传

        :param cluster_id_list: The cluster_id_list of this CreateTaskRequestBodyClusterScanInfo.
        :type cluster_id_list: list[str]
        """
        self._cluster_id_list = cluster_id_list

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
        if not isinstance(other, CreateTaskRequestBodyClusterScanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
