# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGeneralImageVulsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'type': 'str',
        'handle_status': 'str',
        'image_type': 'str',
        'severity_level': 'str',
        'vul_id': 'str',
        'vul_name': 'str',
        'cve_id': 'str',
        'label_list': 'list[str]',
        'status': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'handle_status': 'handle_status',
        'image_type': 'image_type',
        'severity_level': 'severity_level',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'cve_id': 'cve_id',
        'label_list': 'label_list',
        'status': 'status',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, type=None, handle_status=None, image_type=None, severity_level=None, vul_id=None, vul_name=None, cve_id=None, label_list=None, status=None, cluster_id=None):
        r"""ListGeneralImageVulsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param type: **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - app_vul：应用漏洞  **默认取值**: 不涉及
        :type type: str
        :param handle_status: **参数解释**: 漏洞的处理状态 **约束限制**: 不涉及 **取值范围**:： - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及
        :type handle_status: str
        :param image_type: **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像 - registry：仓库镜像 - cicd：CI/CD镜像 - cluster：集群镜像  **默认取值**: 不涉及
        :type image_type: str
        :param severity_level: **参数解释**: 漏洞的风险程度 **约束限制**: 不涉及 **取值范围**: - Critical：严重 - High：高危 - Medium：中危 - Low：低危  **默认取值**: 不涉及
        :type severity_level: str
        :param vul_id: **参数解释**: 漏洞id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type vul_id: str
        :param vul_name: **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type vul_name: str
        :param cve_id: **参数解释**: 漏洞编号 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type cve_id: str
        :param label_list: **参数解释**: 漏洞标签列表 **取值范围**: 最小值0，最大值10 
        :type label_list: list[str]
        :param status: **参数解释**: 漏洞当前状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 **默认取值**: 不涉及 
        :type status: str
        :param cluster_id: **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type cluster_id: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._type = None
        self._handle_status = None
        self._image_type = None
        self._severity_level = None
        self._vul_id = None
        self._vul_name = None
        self._cve_id = None
        self._label_list = None
        self._status = None
        self._cluster_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.type = type
        self.handle_status = handle_status
        self.image_type = image_type
        if severity_level is not None:
            self.severity_level = severity_level
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if cve_id is not None:
            self.cve_id = cve_id
        if label_list is not None:
            self.label_list = label_list
        if status is not None:
            self.status = status
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListGeneralImageVulsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListGeneralImageVulsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListGeneralImageVulsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListGeneralImageVulsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListGeneralImageVulsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListGeneralImageVulsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListGeneralImageVulsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListGeneralImageVulsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListGeneralImageVulsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListGeneralImageVulsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGeneralImageVulsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListGeneralImageVulsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        r"""Gets the type of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - app_vul：应用漏洞  **默认取值**: 不涉及

        :return: The type of this ListGeneralImageVulsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - app_vul：应用漏洞  **默认取值**: 不涉及

        :param type: The type of this ListGeneralImageVulsRequest.
        :type type: str
        """
        self._type = type

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞的处理状态 **约束限制**: 不涉及 **取值范围**:： - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及

        :return: The handle_status of this ListGeneralImageVulsRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞的处理状态 **约束限制**: 不涉及 **取值范围**:： - unhandled：未处理 - handled：已处理  **默认取值**: 不涉及

        :param handle_status: The handle_status of this ListGeneralImageVulsRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def image_type(self):
        r"""Gets the image_type of this ListGeneralImageVulsRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像 - registry：仓库镜像 - cicd：CI/CD镜像 - cluster：集群镜像  **默认取值**: 不涉及

        :return: The image_type of this ListGeneralImageVulsRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListGeneralImageVulsRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像 - registry：仓库镜像 - cicd：CI/CD镜像 - cluster：集群镜像  **默认取值**: 不涉及

        :param image_type: The image_type of this ListGeneralImageVulsRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞的风险程度 **约束限制**: 不涉及 **取值范围**: - Critical：严重 - High：高危 - Medium：中危 - Low：低危  **默认取值**: 不涉及

        :return: The severity_level of this ListGeneralImageVulsRequest.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞的风险程度 **约束限制**: 不涉及 **取值范围**: - Critical：严重 - High：高危 - Medium：中危 - Low：低危  **默认取值**: 不涉及

        :param severity_level: The severity_level of this ListGeneralImageVulsRequest.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The vul_id of this ListGeneralImageVulsRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param vul_id: The vul_id of this ListGeneralImageVulsRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The vul_name of this ListGeneralImageVulsRequest.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param vul_name: The vul_name of this ListGeneralImageVulsRequest.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def cve_id(self):
        r"""Gets the cve_id of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞编号 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The cve_id of this ListGeneralImageVulsRequest.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        r"""Sets the cve_id of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞编号 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param cve_id: The cve_id of this ListGeneralImageVulsRequest.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def label_list(self):
        r"""Gets the label_list of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞标签列表 **取值范围**: 最小值0，最大值10 

        :return: The label_list of this ListGeneralImageVulsRequest.
        :rtype: list[str]
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞标签列表 **取值范围**: 最小值0，最大值10 

        :param label_list: The label_list of this ListGeneralImageVulsRequest.
        :type label_list: list[str]
        """
        self._label_list = label_list

    @property
    def status(self):
        r"""Gets the status of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞当前状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 **默认取值**: 不涉及 

        :return: The status of this ListGeneralImageVulsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListGeneralImageVulsRequest.

        **参数解释**: 漏洞当前状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略 **默认取值**: 不涉及 

        :param status: The status of this ListGeneralImageVulsRequest.
        :type status: str
        """
        self._status = status

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListGeneralImageVulsRequest.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The cluster_id of this ListGeneralImageVulsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListGeneralImageVulsRequest.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param cluster_id: The cluster_id of this ListGeneralImageVulsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, ListGeneralImageVulsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
