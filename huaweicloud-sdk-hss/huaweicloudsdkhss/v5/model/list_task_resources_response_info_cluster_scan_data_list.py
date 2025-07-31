# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskResourcesResponseInfoClusterScanDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'cluster_id': 'str',
        'cluster_type': 'str',
        'cluster_version': 'str',
        'scan_status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'scan_detail_list': 'list[ListTaskResourcesResponseInfoScanDetailList]'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'cluster_version': 'cluster_version',
        'scan_status': 'scan_status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'scan_detail_list': 'scan_detail_list'
    }

    def __init__(self, cluster_name=None, cluster_id=None, cluster_type=None, cluster_version=None, scan_status=None, start_time=None, end_time=None, scan_detail_list=None):
        r"""ListTaskResourcesResponseInfoClusterScanDataList

        The model defined in huaweicloud sdk

        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_type: 集群类型，包含如下： - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群
        :type cluster_type: str
        :param cluster_version: 集群版本
        :type cluster_version: str
        :param scan_status: 集群的扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败
        :type scan_status: str
        :param start_time: 该集群扫描开始的时间
        :type start_time: int
        :param end_time: 该集群扫描结束的时间
        :type end_time: int
        :param scan_detail_list: 当前集群的扫描详情信息
        :type scan_detail_list: list[:class:`huaweicloudsdkhss.v5.ListTaskResourcesResponseInfoScanDetailList`]
        """
        
        

        self._cluster_name = None
        self._cluster_id = None
        self._cluster_type = None
        self._cluster_version = None
        self._scan_status = None
        self._start_time = None
        self._end_time = None
        self._scan_detail_list = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_version is not None:
            self.cluster_version = cluster_version
        if scan_status is not None:
            self.scan_status = scan_status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if scan_detail_list is not None:
            self.scan_detail_list = scan_detail_list

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListTaskResourcesResponseInfoClusterScanDataList.

        集群名称

        :return: The cluster_name of this ListTaskResourcesResponseInfoClusterScanDataList.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListTaskResourcesResponseInfoClusterScanDataList.

        集群名称

        :param cluster_name: The cluster_name of this ListTaskResourcesResponseInfoClusterScanDataList.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListTaskResourcesResponseInfoClusterScanDataList.

        集群id

        :return: The cluster_id of this ListTaskResourcesResponseInfoClusterScanDataList.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListTaskResourcesResponseInfoClusterScanDataList.

        集群id

        :param cluster_id: The cluster_id of this ListTaskResourcesResponseInfoClusterScanDataList.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ListTaskResourcesResponseInfoClusterScanDataList.

        集群类型，包含如下： - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :return: The cluster_type of this ListTaskResourcesResponseInfoClusterScanDataList.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ListTaskResourcesResponseInfoClusterScanDataList.

        集群类型，包含如下： - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :param cluster_type: The cluster_type of this ListTaskResourcesResponseInfoClusterScanDataList.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_version(self):
        r"""Gets the cluster_version of this ListTaskResourcesResponseInfoClusterScanDataList.

        集群版本

        :return: The cluster_version of this ListTaskResourcesResponseInfoClusterScanDataList.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        r"""Sets the cluster_version of this ListTaskResourcesResponseInfoClusterScanDataList.

        集群版本

        :param cluster_version: The cluster_version of this ListTaskResourcesResponseInfoClusterScanDataList.
        :type cluster_version: str
        """
        self._cluster_version = cluster_version

    @property
    def scan_status(self):
        r"""Gets the scan_status of this ListTaskResourcesResponseInfoClusterScanDataList.

        集群的扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败

        :return: The scan_status of this ListTaskResourcesResponseInfoClusterScanDataList.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this ListTaskResourcesResponseInfoClusterScanDataList.

        集群的扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败

        :param scan_status: The scan_status of this ListTaskResourcesResponseInfoClusterScanDataList.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTaskResourcesResponseInfoClusterScanDataList.

        该集群扫描开始的时间

        :return: The start_time of this ListTaskResourcesResponseInfoClusterScanDataList.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTaskResourcesResponseInfoClusterScanDataList.

        该集群扫描开始的时间

        :param start_time: The start_time of this ListTaskResourcesResponseInfoClusterScanDataList.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTaskResourcesResponseInfoClusterScanDataList.

        该集群扫描结束的时间

        :return: The end_time of this ListTaskResourcesResponseInfoClusterScanDataList.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTaskResourcesResponseInfoClusterScanDataList.

        该集群扫描结束的时间

        :param end_time: The end_time of this ListTaskResourcesResponseInfoClusterScanDataList.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def scan_detail_list(self):
        r"""Gets the scan_detail_list of this ListTaskResourcesResponseInfoClusterScanDataList.

        当前集群的扫描详情信息

        :return: The scan_detail_list of this ListTaskResourcesResponseInfoClusterScanDataList.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ListTaskResourcesResponseInfoScanDetailList`]
        """
        return self._scan_detail_list

    @scan_detail_list.setter
    def scan_detail_list(self, scan_detail_list):
        r"""Sets the scan_detail_list of this ListTaskResourcesResponseInfoClusterScanDataList.

        当前集群的扫描详情信息

        :param scan_detail_list: The scan_detail_list of this ListTaskResourcesResponseInfoClusterScanDataList.
        :type scan_detail_list: list[:class:`huaweicloudsdkhss.v5.ListTaskResourcesResponseInfoScanDetailList`]
        """
        self._scan_detail_list = scan_detail_list

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
        if not isinstance(other, ListTaskResourcesResponseInfoClusterScanDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
