# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskResourcesRequestBodyClusterScanInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_status': 'str',
        'cluster_name': 'str',
        'cluster_id': 'str',
        'cluster_type': 'str'
    }

    attribute_map = {
        'scan_status': 'scan_status',
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type'
    }

    def __init__(self, scan_status=None, cluster_name=None, cluster_id=None, cluster_type=None):
        r"""ListTaskResourcesRequestBodyClusterScanInfo

        The model defined in huaweicloud sdk

        :param scan_status: 集群的扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败
        :type scan_status: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_type: 集群类型，包含如下： - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群
        :type cluster_type: str
        """
        
        

        self._scan_status = None
        self._cluster_name = None
        self._cluster_id = None
        self._cluster_type = None
        self.discriminator = None

        if scan_status is not None:
            self.scan_status = scan_status
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type

    @property
    def scan_status(self):
        r"""Gets the scan_status of this ListTaskResourcesRequestBodyClusterScanInfo.

        集群的扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败

        :return: The scan_status of this ListTaskResourcesRequestBodyClusterScanInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this ListTaskResourcesRequestBodyClusterScanInfo.

        集群的扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败

        :param scan_status: The scan_status of this ListTaskResourcesRequestBodyClusterScanInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListTaskResourcesRequestBodyClusterScanInfo.

        集群名称

        :return: The cluster_name of this ListTaskResourcesRequestBodyClusterScanInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListTaskResourcesRequestBodyClusterScanInfo.

        集群名称

        :param cluster_name: The cluster_name of this ListTaskResourcesRequestBodyClusterScanInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListTaskResourcesRequestBodyClusterScanInfo.

        集群id

        :return: The cluster_id of this ListTaskResourcesRequestBodyClusterScanInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListTaskResourcesRequestBodyClusterScanInfo.

        集群id

        :param cluster_id: The cluster_id of this ListTaskResourcesRequestBodyClusterScanInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ListTaskResourcesRequestBodyClusterScanInfo.

        集群类型，包含如下： - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :return: The cluster_type of this ListTaskResourcesRequestBodyClusterScanInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ListTaskResourcesRequestBodyClusterScanInfo.

        集群类型，包含如下： - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :param cluster_type: The cluster_type of this ListTaskResourcesRequestBodyClusterScanInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

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
        if not isinstance(other, ListTaskResourcesRequestBodyClusterScanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
