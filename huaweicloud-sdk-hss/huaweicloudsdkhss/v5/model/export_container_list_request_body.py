# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportContainerListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_container': 'bool',
        'cluster_type': 'str',
        'cluster_name': 'str',
        'container_name': 'str',
        'pod_name': 'str',
        'image_name': 'str',
        'status': 'str',
        'risky': 'bool',
        'create_time': 'ExportContainerListRequestBodyCreateTime',
        'cpu_limit': 'str',
        'memory_limit': 'str',
        'export_headers': 'list[list[str]]'
    }

    attribute_map = {
        'cluster_container': 'cluster_container',
        'cluster_type': 'cluster_type',
        'cluster_name': 'cluster_name',
        'container_name': 'container_name',
        'pod_name': 'pod_name',
        'image_name': 'image_name',
        'status': 'status',
        'risky': 'risky',
        'create_time': 'create_time',
        'cpu_limit': 'cpu_limit',
        'memory_limit': 'memory_limit',
        'export_headers': 'export_headers'
    }

    def __init__(self, cluster_container=None, cluster_type=None, cluster_name=None, container_name=None, pod_name=None, image_name=None, status=None, risky=None, create_time=None, cpu_limit=None, memory_limit=None, export_headers=None):
        r"""ExportContainerListRequestBody

        The model defined in huaweicloud sdk

        :param cluster_container: **参数解释**: 是否是集群内的容器。只导出集群内容器时，设置此参数值为true。只导出非集群容器时，设置此参数为false。 **约束限制**: 不涉及 **取值范围**: true或者false。 **默认取值**: 不涉及 
        :type cluster_container: bool
        :param cluster_type: **参数解释**: 集群类型。 **约束限制**: 不涉及 **取值范围**:   - cce：CCE集群   - ali：阿里云集群   - tencent：腾讯云集群   - azure：微软云集群   - aws：亚马逊集群   - self_built_hw：华为云自建集群   - self_built_idc：IDC自建集群  **默认取值**: 不涉及 
        :type cluster_type: str
        :param cluster_name: **参数解释**: 所属集群名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-255。 **默认取值**: 不涉及 
        :type cluster_name: str
        :param container_name: **参数解释**: 容器名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-255。 **默认取值**: 不涉及 
        :type container_name: str
        :param pod_name: **参数解释**: 所属Pod名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-512。 **默认取值**: 不涉及 
        :type pod_name: str
        :param image_name: **参数解释**: 镜像名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-255。 **默认取值**: 不涉及 
        :type image_name: str
        :param status: **参数解释**: 容器状态。 **约束限制**: 不涉及 **取值范围**:   - Running : 运行中   - Waiting : 等待   - Terminated : 终止   - Isolated : 已隔离   - Paused : 已暂停  **默认取值**: 不涉及 
        :type status: str
        :param risky: **参数解释**: 是否有安全风险。只导出有安全风险容器时，设置此参数值为true。只导出无安全风险容器时，设置此参数为false。 **约束限制**: 不涉及 **取值范围**: true或者false。 **默认取值**: 不涉及 
        :type risky: bool
        :param create_time: 
        :type create_time: :class:`huaweicloudsdkhss.v5.ExportContainerListRequestBodyCreateTime`
        :param cpu_limit: **参数解释**: cpu限制。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64。以m为单位，例如100m。 **默认取值**: 不涉及 
        :type cpu_limit: str
        :param memory_limit: **参数解释**: 内存限制。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64。以Mi、Gi为单位，例如300Mi。 **默认取值**: 不涉及 
        :type memory_limit: str
        :param export_headers: **参数解释**: 导出容器列表的表头信息。 **约束限制**: 不涉及 **取值范围**: 合法的key值及其对应的表头名称（表头名称可自定义）   - container_id：容器id   - container_name：容器名称   - image_name：镜像名称   - pod_name：所属POD   - cluster_name：所属集群   - cluster_type：集群类型   - status：状态   - risky：是否有安全风险   - low_risk：低危风险   - medium_risk：中危风险   - high_risk：高危风险   - fatal_risk：致命风险   - create_time：创建时间   - restart_count：重启次数   - cpu_limit：CPU限制   - memory_limit：内存限制  **默认取值**: 不涉及 
        :type export_headers: list[list[str]]
        """
        
        

        self._cluster_container = None
        self._cluster_type = None
        self._cluster_name = None
        self._container_name = None
        self._pod_name = None
        self._image_name = None
        self._status = None
        self._risky = None
        self._create_time = None
        self._cpu_limit = None
        self._memory_limit = None
        self._export_headers = None
        self.discriminator = None

        if cluster_container is not None:
            self.cluster_container = cluster_container
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if container_name is not None:
            self.container_name = container_name
        if pod_name is not None:
            self.pod_name = pod_name
        if image_name is not None:
            self.image_name = image_name
        if status is not None:
            self.status = status
        if risky is not None:
            self.risky = risky
        if create_time is not None:
            self.create_time = create_time
        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if memory_limit is not None:
            self.memory_limit = memory_limit
        self.export_headers = export_headers

    @property
    def cluster_container(self):
        r"""Gets the cluster_container of this ExportContainerListRequestBody.

        **参数解释**: 是否是集群内的容器。只导出集群内容器时，设置此参数值为true。只导出非集群容器时，设置此参数为false。 **约束限制**: 不涉及 **取值范围**: true或者false。 **默认取值**: 不涉及 

        :return: The cluster_container of this ExportContainerListRequestBody.
        :rtype: bool
        """
        return self._cluster_container

    @cluster_container.setter
    def cluster_container(self, cluster_container):
        r"""Sets the cluster_container of this ExportContainerListRequestBody.

        **参数解释**: 是否是集群内的容器。只导出集群内容器时，设置此参数值为true。只导出非集群容器时，设置此参数为false。 **约束限制**: 不涉及 **取值范围**: true或者false。 **默认取值**: 不涉及 

        :param cluster_container: The cluster_container of this ExportContainerListRequestBody.
        :type cluster_container: bool
        """
        self._cluster_container = cluster_container

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ExportContainerListRequestBody.

        **参数解释**: 集群类型。 **约束限制**: 不涉及 **取值范围**:   - cce：CCE集群   - ali：阿里云集群   - tencent：腾讯云集群   - azure：微软云集群   - aws：亚马逊集群   - self_built_hw：华为云自建集群   - self_built_idc：IDC自建集群  **默认取值**: 不涉及 

        :return: The cluster_type of this ExportContainerListRequestBody.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ExportContainerListRequestBody.

        **参数解释**: 集群类型。 **约束限制**: 不涉及 **取值范围**:   - cce：CCE集群   - ali：阿里云集群   - tencent：腾讯云集群   - azure：微软云集群   - aws：亚马逊集群   - self_built_hw：华为云自建集群   - self_built_idc：IDC自建集群  **默认取值**: 不涉及 

        :param cluster_type: The cluster_type of this ExportContainerListRequestBody.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ExportContainerListRequestBody.

        **参数解释**: 所属集群名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-255。 **默认取值**: 不涉及 

        :return: The cluster_name of this ExportContainerListRequestBody.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ExportContainerListRequestBody.

        **参数解释**: 所属集群名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-255。 **默认取值**: 不涉及 

        :param cluster_name: The cluster_name of this ExportContainerListRequestBody.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def container_name(self):
        r"""Gets the container_name of this ExportContainerListRequestBody.

        **参数解释**: 容器名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-255。 **默认取值**: 不涉及 

        :return: The container_name of this ExportContainerListRequestBody.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ExportContainerListRequestBody.

        **参数解释**: 容器名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-255。 **默认取值**: 不涉及 

        :param container_name: The container_name of this ExportContainerListRequestBody.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ExportContainerListRequestBody.

        **参数解释**: 所属Pod名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-512。 **默认取值**: 不涉及 

        :return: The pod_name of this ExportContainerListRequestBody.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ExportContainerListRequestBody.

        **参数解释**: 所属Pod名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-512。 **默认取值**: 不涉及 

        :param pod_name: The pod_name of this ExportContainerListRequestBody.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def image_name(self):
        r"""Gets the image_name of this ExportContainerListRequestBody.

        **参数解释**: 镜像名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-255。 **默认取值**: 不涉及 

        :return: The image_name of this ExportContainerListRequestBody.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ExportContainerListRequestBody.

        **参数解释**: 镜像名称。 **约束限制**: 不涉及 **取值范围**: 字符长度1-255。 **默认取值**: 不涉及 

        :param image_name: The image_name of this ExportContainerListRequestBody.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def status(self):
        r"""Gets the status of this ExportContainerListRequestBody.

        **参数解释**: 容器状态。 **约束限制**: 不涉及 **取值范围**:   - Running : 运行中   - Waiting : 等待   - Terminated : 终止   - Isolated : 已隔离   - Paused : 已暂停  **默认取值**: 不涉及 

        :return: The status of this ExportContainerListRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportContainerListRequestBody.

        **参数解释**: 容器状态。 **约束限制**: 不涉及 **取值范围**:   - Running : 运行中   - Waiting : 等待   - Terminated : 终止   - Isolated : 已隔离   - Paused : 已暂停  **默认取值**: 不涉及 

        :param status: The status of this ExportContainerListRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def risky(self):
        r"""Gets the risky of this ExportContainerListRequestBody.

        **参数解释**: 是否有安全风险。只导出有安全风险容器时，设置此参数值为true。只导出无安全风险容器时，设置此参数为false。 **约束限制**: 不涉及 **取值范围**: true或者false。 **默认取值**: 不涉及 

        :return: The risky of this ExportContainerListRequestBody.
        :rtype: bool
        """
        return self._risky

    @risky.setter
    def risky(self, risky):
        r"""Sets the risky of this ExportContainerListRequestBody.

        **参数解释**: 是否有安全风险。只导出有安全风险容器时，设置此参数值为true。只导出无安全风险容器时，设置此参数为false。 **约束限制**: 不涉及 **取值范围**: true或者false。 **默认取值**: 不涉及 

        :param risky: The risky of this ExportContainerListRequestBody.
        :type risky: bool
        """
        self._risky = risky

    @property
    def create_time(self):
        r"""Gets the create_time of this ExportContainerListRequestBody.

        :return: The create_time of this ExportContainerListRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.ExportContainerListRequestBodyCreateTime`
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ExportContainerListRequestBody.

        :param create_time: The create_time of this ExportContainerListRequestBody.
        :type create_time: :class:`huaweicloudsdkhss.v5.ExportContainerListRequestBodyCreateTime`
        """
        self._create_time = create_time

    @property
    def cpu_limit(self):
        r"""Gets the cpu_limit of this ExportContainerListRequestBody.

        **参数解释**: cpu限制。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64。以m为单位，例如100m。 **默认取值**: 不涉及 

        :return: The cpu_limit of this ExportContainerListRequestBody.
        :rtype: str
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        r"""Sets the cpu_limit of this ExportContainerListRequestBody.

        **参数解释**: cpu限制。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64。以m为单位，例如100m。 **默认取值**: 不涉及 

        :param cpu_limit: The cpu_limit of this ExportContainerListRequestBody.
        :type cpu_limit: str
        """
        self._cpu_limit = cpu_limit

    @property
    def memory_limit(self):
        r"""Gets the memory_limit of this ExportContainerListRequestBody.

        **参数解释**: 内存限制。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64。以Mi、Gi为单位，例如300Mi。 **默认取值**: 不涉及 

        :return: The memory_limit of this ExportContainerListRequestBody.
        :rtype: str
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        r"""Sets the memory_limit of this ExportContainerListRequestBody.

        **参数解释**: 内存限制。 **约束限制**: 不涉及 **取值范围**: 字符长度0-64。以Mi、Gi为单位，例如300Mi。 **默认取值**: 不涉及 

        :param memory_limit: The memory_limit of this ExportContainerListRequestBody.
        :type memory_limit: str
        """
        self._memory_limit = memory_limit

    @property
    def export_headers(self):
        r"""Gets the export_headers of this ExportContainerListRequestBody.

        **参数解释**: 导出容器列表的表头信息。 **约束限制**: 不涉及 **取值范围**: 合法的key值及其对应的表头名称（表头名称可自定义）   - container_id：容器id   - container_name：容器名称   - image_name：镜像名称   - pod_name：所属POD   - cluster_name：所属集群   - cluster_type：集群类型   - status：状态   - risky：是否有安全风险   - low_risk：低危风险   - medium_risk：中危风险   - high_risk：高危风险   - fatal_risk：致命风险   - create_time：创建时间   - restart_count：重启次数   - cpu_limit：CPU限制   - memory_limit：内存限制  **默认取值**: 不涉及 

        :return: The export_headers of this ExportContainerListRequestBody.
        :rtype: list[list[str]]
        """
        return self._export_headers

    @export_headers.setter
    def export_headers(self, export_headers):
        r"""Sets the export_headers of this ExportContainerListRequestBody.

        **参数解释**: 导出容器列表的表头信息。 **约束限制**: 不涉及 **取值范围**: 合法的key值及其对应的表头名称（表头名称可自定义）   - container_id：容器id   - container_name：容器名称   - image_name：镜像名称   - pod_name：所属POD   - cluster_name：所属集群   - cluster_type：集群类型   - status：状态   - risky：是否有安全风险   - low_risk：低危风险   - medium_risk：中危风险   - high_risk：高危风险   - fatal_risk：致命风险   - create_time：创建时间   - restart_count：重启次数   - cpu_limit：CPU限制   - memory_limit：内存限制  **默认取值**: 不涉及 

        :param export_headers: The export_headers of this ExportContainerListRequestBody.
        :type export_headers: list[list[str]]
        """
        self._export_headers = export_headers

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
        if not isinstance(other, ExportContainerListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
