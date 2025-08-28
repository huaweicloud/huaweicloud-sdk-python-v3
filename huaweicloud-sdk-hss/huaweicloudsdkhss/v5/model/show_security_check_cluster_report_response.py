# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityCheckClusterReportResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_time': 'int',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'cluster_category': 'str',
        'local_image_vul_num': 'int',
        'risk_config_num': 'int',
        'privileged_container_num': 'int',
        'pod_num': 'int',
        'host_num': 'int',
        'container_num': 'int',
        'port_num': 'int',
        'process_num': 'int',
        'app_num': 'int',
        'local_image_vul_list': 'list[ClusterSecurityCheckLocalImageVulInfo]',
        'baseline_detection_list': 'list[ClusterSecurityCheckBaseLineDetectionInfo]',
        'privileged_container_list': 'list[ClusterSecurityCheckPrivilegedContainerInfo]',
        'port_list': 'list[ClusterSecurityCheckPortInfo]',
        'app_list': 'list[ClusterSecurityCheckAppInfo]',
        'process_list': 'list[ClusterSecurityCheckProcessInfo]'
    }

    attribute_map = {
        'scan_time': 'scan_time',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'cluster_category': 'cluster_category',
        'local_image_vul_num': 'local_image_vul_num',
        'risk_config_num': 'risk_config_num',
        'privileged_container_num': 'privileged_container_num',
        'pod_num': 'pod_num',
        'host_num': 'host_num',
        'container_num': 'container_num',
        'port_num': 'port_num',
        'process_num': 'process_num',
        'app_num': 'app_num',
        'local_image_vul_list': 'local_image_vul_list',
        'baseline_detection_list': 'baseline_detection_list',
        'privileged_container_list': 'privileged_container_list',
        'port_list': 'port_list',
        'app_list': 'app_list',
        'process_list': 'process_list'
    }

    def __init__(self, scan_time=None, cluster_id=None, cluster_name=None, cluster_category=None, local_image_vul_num=None, risk_config_num=None, privileged_container_num=None, pod_num=None, host_num=None, container_num=None, port_num=None, process_num=None, app_num=None, local_image_vul_list=None, baseline_detection_list=None, privileged_container_list=None, port_list=None, app_list=None, process_list=None):
        r"""ShowSecurityCheckClusterReportResponse

        The model defined in huaweicloud sdk

        :param scan_time: **参数解释**： 体检时间 **取值范围**： 不涉及 
        :type scan_time: int
        :param cluster_id: **参数解释**： 集群ID **取值范围**： 不涉及 
        :type cluster_id: str
        :param cluster_name: **参数解释**： 集群名称 **取值范围**： 不涉及 
        :type cluster_name: str
        :param cluster_category: **参数解释**： 集群类型 **取值范围**： - CCE：CCE Standard集群 - Turbo：CCE Turbo集群 
        :type cluster_category: str
        :param local_image_vul_num: **参数解释**： 本地镜像漏洞风险数量 **取值范围**： 不涉及 
        :type local_image_vul_num: int
        :param risk_config_num: **参数解释**： 基线风险数量 **取值范围**： 不涉及 
        :type risk_config_num: int
        :param privileged_container_num: **参数解释**： 特权容器数量 **取值范围**： 不涉及 
        :type privileged_container_num: int
        :param pod_num: **参数解释**： pod数量 **取值范围**： 不涉及 
        :type pod_num: int
        :param host_num: **参数解释**： 节点数量 **取值范围**： 不涉及 
        :type host_num: int
        :param container_num: **参数解释**： 容器数量 **取值范围**： 不涉及 
        :type container_num: int
        :param port_num: **参数解释**： 端口数量 **取值范围**： 不涉及 
        :type port_num: int
        :param process_num: **参数解释**： 进程数量 **取值范围**： 不涉及 
        :type process_num: int
        :param app_num: **参数解释**： 软件数量 **取值范围**： 不涉及 
        :type app_num: int
        :param local_image_vul_list: **参数解释**： 本地镜像漏洞列表 **取值范围**： 不涉及 
        :type local_image_vul_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckLocalImageVulInfo`]
        :param baseline_detection_list: **参数解释**： 基线检测列表 **取值范围**： 不涉及 
        :type baseline_detection_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckBaseLineDetectionInfo`]
        :param privileged_container_list: **参数解释**： 特权容器列表 **取值范围**： 不涉及 
        :type privileged_container_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckPrivilegedContainerInfo`]
        :param port_list: **参数解释**： 端口列表 **取值范围**： 不涉及 
        :type port_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckPortInfo`]
        :param app_list: **参数解释**： 软件列表 **取值范围**： 不涉及 
        :type app_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckAppInfo`]
        :param process_list: **参数解释**： 进程列表 **取值范围**： 不涉及 
        :type process_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckProcessInfo`]
        """
        
        super(ShowSecurityCheckClusterReportResponse, self).__init__()

        self._scan_time = None
        self._cluster_id = None
        self._cluster_name = None
        self._cluster_category = None
        self._local_image_vul_num = None
        self._risk_config_num = None
        self._privileged_container_num = None
        self._pod_num = None
        self._host_num = None
        self._container_num = None
        self._port_num = None
        self._process_num = None
        self._app_num = None
        self._local_image_vul_list = None
        self._baseline_detection_list = None
        self._privileged_container_list = None
        self._port_list = None
        self._app_list = None
        self._process_list = None
        self.discriminator = None

        if scan_time is not None:
            self.scan_time = scan_time
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_category is not None:
            self.cluster_category = cluster_category
        if local_image_vul_num is not None:
            self.local_image_vul_num = local_image_vul_num
        if risk_config_num is not None:
            self.risk_config_num = risk_config_num
        if privileged_container_num is not None:
            self.privileged_container_num = privileged_container_num
        if pod_num is not None:
            self.pod_num = pod_num
        if host_num is not None:
            self.host_num = host_num
        if container_num is not None:
            self.container_num = container_num
        if port_num is not None:
            self.port_num = port_num
        if process_num is not None:
            self.process_num = process_num
        if app_num is not None:
            self.app_num = app_num
        if local_image_vul_list is not None:
            self.local_image_vul_list = local_image_vul_list
        if baseline_detection_list is not None:
            self.baseline_detection_list = baseline_detection_list
        if privileged_container_list is not None:
            self.privileged_container_list = privileged_container_list
        if port_list is not None:
            self.port_list = port_list
        if app_list is not None:
            self.app_list = app_list
        if process_list is not None:
            self.process_list = process_list

    @property
    def scan_time(self):
        r"""Gets the scan_time of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 体检时间 **取值范围**： 不涉及 

        :return: The scan_time of this ShowSecurityCheckClusterReportResponse.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 体检时间 **取值范围**： 不涉及 

        :param scan_time: The scan_time of this ShowSecurityCheckClusterReportResponse.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 集群ID **取值范围**： 不涉及 

        :return: The cluster_id of this ShowSecurityCheckClusterReportResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 集群ID **取值范围**： 不涉及 

        :param cluster_id: The cluster_id of this ShowSecurityCheckClusterReportResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 集群名称 **取值范围**： 不涉及 

        :return: The cluster_name of this ShowSecurityCheckClusterReportResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 集群名称 **取值范围**： 不涉及 

        :param cluster_name: The cluster_name of this ShowSecurityCheckClusterReportResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_category(self):
        r"""Gets the cluster_category of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 集群类型 **取值范围**： - CCE：CCE Standard集群 - Turbo：CCE Turbo集群 

        :return: The cluster_category of this ShowSecurityCheckClusterReportResponse.
        :rtype: str
        """
        return self._cluster_category

    @cluster_category.setter
    def cluster_category(self, cluster_category):
        r"""Sets the cluster_category of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 集群类型 **取值范围**： - CCE：CCE Standard集群 - Turbo：CCE Turbo集群 

        :param cluster_category: The cluster_category of this ShowSecurityCheckClusterReportResponse.
        :type cluster_category: str
        """
        self._cluster_category = cluster_category

    @property
    def local_image_vul_num(self):
        r"""Gets the local_image_vul_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 本地镜像漏洞风险数量 **取值范围**： 不涉及 

        :return: The local_image_vul_num of this ShowSecurityCheckClusterReportResponse.
        :rtype: int
        """
        return self._local_image_vul_num

    @local_image_vul_num.setter
    def local_image_vul_num(self, local_image_vul_num):
        r"""Sets the local_image_vul_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 本地镜像漏洞风险数量 **取值范围**： 不涉及 

        :param local_image_vul_num: The local_image_vul_num of this ShowSecurityCheckClusterReportResponse.
        :type local_image_vul_num: int
        """
        self._local_image_vul_num = local_image_vul_num

    @property
    def risk_config_num(self):
        r"""Gets the risk_config_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 基线风险数量 **取值范围**： 不涉及 

        :return: The risk_config_num of this ShowSecurityCheckClusterReportResponse.
        :rtype: int
        """
        return self._risk_config_num

    @risk_config_num.setter
    def risk_config_num(self, risk_config_num):
        r"""Sets the risk_config_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 基线风险数量 **取值范围**： 不涉及 

        :param risk_config_num: The risk_config_num of this ShowSecurityCheckClusterReportResponse.
        :type risk_config_num: int
        """
        self._risk_config_num = risk_config_num

    @property
    def privileged_container_num(self):
        r"""Gets the privileged_container_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 特权容器数量 **取值范围**： 不涉及 

        :return: The privileged_container_num of this ShowSecurityCheckClusterReportResponse.
        :rtype: int
        """
        return self._privileged_container_num

    @privileged_container_num.setter
    def privileged_container_num(self, privileged_container_num):
        r"""Sets the privileged_container_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 特权容器数量 **取值范围**： 不涉及 

        :param privileged_container_num: The privileged_container_num of this ShowSecurityCheckClusterReportResponse.
        :type privileged_container_num: int
        """
        self._privileged_container_num = privileged_container_num

    @property
    def pod_num(self):
        r"""Gets the pod_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： pod数量 **取值范围**： 不涉及 

        :return: The pod_num of this ShowSecurityCheckClusterReportResponse.
        :rtype: int
        """
        return self._pod_num

    @pod_num.setter
    def pod_num(self, pod_num):
        r"""Sets the pod_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： pod数量 **取值范围**： 不涉及 

        :param pod_num: The pod_num of this ShowSecurityCheckClusterReportResponse.
        :type pod_num: int
        """
        self._pod_num = pod_num

    @property
    def host_num(self):
        r"""Gets the host_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 节点数量 **取值范围**： 不涉及 

        :return: The host_num of this ShowSecurityCheckClusterReportResponse.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 节点数量 **取值范围**： 不涉及 

        :param host_num: The host_num of this ShowSecurityCheckClusterReportResponse.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def container_num(self):
        r"""Gets the container_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 容器数量 **取值范围**： 不涉及 

        :return: The container_num of this ShowSecurityCheckClusterReportResponse.
        :rtype: int
        """
        return self._container_num

    @container_num.setter
    def container_num(self, container_num):
        r"""Sets the container_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 容器数量 **取值范围**： 不涉及 

        :param container_num: The container_num of this ShowSecurityCheckClusterReportResponse.
        :type container_num: int
        """
        self._container_num = container_num

    @property
    def port_num(self):
        r"""Gets the port_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 端口数量 **取值范围**： 不涉及 

        :return: The port_num of this ShowSecurityCheckClusterReportResponse.
        :rtype: int
        """
        return self._port_num

    @port_num.setter
    def port_num(self, port_num):
        r"""Sets the port_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 端口数量 **取值范围**： 不涉及 

        :param port_num: The port_num of this ShowSecurityCheckClusterReportResponse.
        :type port_num: int
        """
        self._port_num = port_num

    @property
    def process_num(self):
        r"""Gets the process_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 进程数量 **取值范围**： 不涉及 

        :return: The process_num of this ShowSecurityCheckClusterReportResponse.
        :rtype: int
        """
        return self._process_num

    @process_num.setter
    def process_num(self, process_num):
        r"""Sets the process_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 进程数量 **取值范围**： 不涉及 

        :param process_num: The process_num of this ShowSecurityCheckClusterReportResponse.
        :type process_num: int
        """
        self._process_num = process_num

    @property
    def app_num(self):
        r"""Gets the app_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 软件数量 **取值范围**： 不涉及 

        :return: The app_num of this ShowSecurityCheckClusterReportResponse.
        :rtype: int
        """
        return self._app_num

    @app_num.setter
    def app_num(self, app_num):
        r"""Sets the app_num of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 软件数量 **取值范围**： 不涉及 

        :param app_num: The app_num of this ShowSecurityCheckClusterReportResponse.
        :type app_num: int
        """
        self._app_num = app_num

    @property
    def local_image_vul_list(self):
        r"""Gets the local_image_vul_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 本地镜像漏洞列表 **取值范围**： 不涉及 

        :return: The local_image_vul_list of this ShowSecurityCheckClusterReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckLocalImageVulInfo`]
        """
        return self._local_image_vul_list

    @local_image_vul_list.setter
    def local_image_vul_list(self, local_image_vul_list):
        r"""Sets the local_image_vul_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 本地镜像漏洞列表 **取值范围**： 不涉及 

        :param local_image_vul_list: The local_image_vul_list of this ShowSecurityCheckClusterReportResponse.
        :type local_image_vul_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckLocalImageVulInfo`]
        """
        self._local_image_vul_list = local_image_vul_list

    @property
    def baseline_detection_list(self):
        r"""Gets the baseline_detection_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 基线检测列表 **取值范围**： 不涉及 

        :return: The baseline_detection_list of this ShowSecurityCheckClusterReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckBaseLineDetectionInfo`]
        """
        return self._baseline_detection_list

    @baseline_detection_list.setter
    def baseline_detection_list(self, baseline_detection_list):
        r"""Sets the baseline_detection_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 基线检测列表 **取值范围**： 不涉及 

        :param baseline_detection_list: The baseline_detection_list of this ShowSecurityCheckClusterReportResponse.
        :type baseline_detection_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckBaseLineDetectionInfo`]
        """
        self._baseline_detection_list = baseline_detection_list

    @property
    def privileged_container_list(self):
        r"""Gets the privileged_container_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 特权容器列表 **取值范围**： 不涉及 

        :return: The privileged_container_list of this ShowSecurityCheckClusterReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckPrivilegedContainerInfo`]
        """
        return self._privileged_container_list

    @privileged_container_list.setter
    def privileged_container_list(self, privileged_container_list):
        r"""Sets the privileged_container_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 特权容器列表 **取值范围**： 不涉及 

        :param privileged_container_list: The privileged_container_list of this ShowSecurityCheckClusterReportResponse.
        :type privileged_container_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckPrivilegedContainerInfo`]
        """
        self._privileged_container_list = privileged_container_list

    @property
    def port_list(self):
        r"""Gets the port_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 端口列表 **取值范围**： 不涉及 

        :return: The port_list of this ShowSecurityCheckClusterReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckPortInfo`]
        """
        return self._port_list

    @port_list.setter
    def port_list(self, port_list):
        r"""Sets the port_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 端口列表 **取值范围**： 不涉及 

        :param port_list: The port_list of this ShowSecurityCheckClusterReportResponse.
        :type port_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckPortInfo`]
        """
        self._port_list = port_list

    @property
    def app_list(self):
        r"""Gets the app_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 软件列表 **取值范围**： 不涉及 

        :return: The app_list of this ShowSecurityCheckClusterReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckAppInfo`]
        """
        return self._app_list

    @app_list.setter
    def app_list(self, app_list):
        r"""Sets the app_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 软件列表 **取值范围**： 不涉及 

        :param app_list: The app_list of this ShowSecurityCheckClusterReportResponse.
        :type app_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckAppInfo`]
        """
        self._app_list = app_list

    @property
    def process_list(self):
        r"""Gets the process_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 进程列表 **取值范围**： 不涉及 

        :return: The process_list of this ShowSecurityCheckClusterReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckProcessInfo`]
        """
        return self._process_list

    @process_list.setter
    def process_list(self, process_list):
        r"""Sets the process_list of this ShowSecurityCheckClusterReportResponse.

        **参数解释**： 进程列表 **取值范围**： 不涉及 

        :param process_list: The process_list of this ShowSecurityCheckClusterReportResponse.
        :type process_list: list[:class:`huaweicloudsdkhss.v5.ClusterSecurityCheckProcessInfo`]
        """
        self._process_list = process_list

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
        if not isinstance(other, ShowSecurityCheckClusterReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
