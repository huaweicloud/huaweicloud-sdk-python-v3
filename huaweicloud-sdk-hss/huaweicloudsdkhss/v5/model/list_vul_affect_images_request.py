# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulAffectImagesRequest:

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
        'is_handled': 'bool',
        'vul_id': 'str',
        'type': 'str',
        'image_type': 'str',
        'repair_necessity': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'registry_name': 'str',
        'registry_type': 'str',
        'status': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'is_handled': 'is_handled',
        'vul_id': 'vul_id',
        'type': 'type',
        'image_type': 'image_type',
        'repair_necessity': 'repair_necessity',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'registry_name': 'registry_name',
        'registry_type': 'registry_type',
        'status': 'status',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, is_handled=None, vul_id=None, type=None, image_type=None, repair_necessity=None, image_id=None, image_name=None, registry_name=None, registry_type=None, status=None, cluster_id=None):
        r"""ListVulAffectImagesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param is_handled: **参数解释**: 查询已处理/未处理的镜像 **约束限制**: 不涉及 **取值范围**: - true：查询已处理的镜像 - false：查询未处理的镜像  **默认取值**: 不涉及 
        :type is_handled: bool
        :param vul_id: **参数解释**: 漏洞id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type vul_id: str
        :param type: **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - app_vul：应用漏洞 - linux_vul：系统漏洞  **默认取值**: 不涉及 
        :type type: str
        :param image_type: **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像 - registry：仓库镜像 - cicd：CI/CD镜像 - cluster：集群镜像  **默认取值**: 不涉及 
        :type image_type: str
        :param repair_necessity: **参数解释**: 危险程度 **约束限制**: 不涉及 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：严重  **默认取值**: 不涉及 
        :type repair_necessity: str
        :param image_id: **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type image_id: str
        :param image_name: **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type image_name: str
        :param registry_name: **参数解释**: 镜像仓名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type registry_name: str
        :param registry_type: **参数解释**: 镜像仓类型 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type registry_type: str
        :param status: **参数解释**: 漏洞对应镜像的处理状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略  **默认取值**: 不涉及 
        :type status: str
        :param cluster_id: **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type cluster_id: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._is_handled = None
        self._vul_id = None
        self._type = None
        self._image_type = None
        self._repair_necessity = None
        self._image_id = None
        self._image_name = None
        self._registry_name = None
        self._registry_type = None
        self._status = None
        self._cluster_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.is_handled = is_handled
        self.vul_id = vul_id
        self.type = type
        self.image_type = image_type
        if repair_necessity is not None:
            self.repair_necessity = repair_necessity
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if registry_name is not None:
            self.registry_name = registry_name
        if registry_type is not None:
            self.registry_type = registry_type
        if status is not None:
            self.status = status
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVulAffectImagesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListVulAffectImagesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVulAffectImagesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListVulAffectImagesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListVulAffectImagesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListVulAffectImagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVulAffectImagesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListVulAffectImagesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListVulAffectImagesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListVulAffectImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVulAffectImagesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListVulAffectImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def is_handled(self):
        r"""Gets the is_handled of this ListVulAffectImagesRequest.

        **参数解释**: 查询已处理/未处理的镜像 **约束限制**: 不涉及 **取值范围**: - true：查询已处理的镜像 - false：查询未处理的镜像  **默认取值**: 不涉及 

        :return: The is_handled of this ListVulAffectImagesRequest.
        :rtype: bool
        """
        return self._is_handled

    @is_handled.setter
    def is_handled(self, is_handled):
        r"""Sets the is_handled of this ListVulAffectImagesRequest.

        **参数解释**: 查询已处理/未处理的镜像 **约束限制**: 不涉及 **取值范围**: - true：查询已处理的镜像 - false：查询未处理的镜像  **默认取值**: 不涉及 

        :param is_handled: The is_handled of this ListVulAffectImagesRequest.
        :type is_handled: bool
        """
        self._is_handled = is_handled

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ListVulAffectImagesRequest.

        **参数解释**: 漏洞id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The vul_id of this ListVulAffectImagesRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ListVulAffectImagesRequest.

        **参数解释**: 漏洞id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param vul_id: The vul_id of this ListVulAffectImagesRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def type(self):
        r"""Gets the type of this ListVulAffectImagesRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - app_vul：应用漏洞 - linux_vul：系统漏洞  **默认取值**: 不涉及 

        :return: The type of this ListVulAffectImagesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListVulAffectImagesRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - app_vul：应用漏洞 - linux_vul：系统漏洞  **默认取值**: 不涉及 

        :param type: The type of this ListVulAffectImagesRequest.
        :type type: str
        """
        self._type = type

    @property
    def image_type(self):
        r"""Gets the image_type of this ListVulAffectImagesRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像 - registry：仓库镜像 - cicd：CI/CD镜像 - cluster：集群镜像  **默认取值**: 不涉及 

        :return: The image_type of this ListVulAffectImagesRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListVulAffectImagesRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像 - registry：仓库镜像 - cicd：CI/CD镜像 - cluster：集群镜像  **默认取值**: 不涉及 

        :param image_type: The image_type of this ListVulAffectImagesRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def repair_necessity(self):
        r"""Gets the repair_necessity of this ListVulAffectImagesRequest.

        **参数解释**: 危险程度 **约束限制**: 不涉及 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：严重  **默认取值**: 不涉及 

        :return: The repair_necessity of this ListVulAffectImagesRequest.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        r"""Sets the repair_necessity of this ListVulAffectImagesRequest.

        **参数解释**: 危险程度 **约束限制**: 不涉及 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：严重  **默认取值**: 不涉及 

        :param repair_necessity: The repair_necessity of this ListVulAffectImagesRequest.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def image_id(self):
        r"""Gets the image_id of this ListVulAffectImagesRequest.

        **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The image_id of this ListVulAffectImagesRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListVulAffectImagesRequest.

        **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param image_id: The image_id of this ListVulAffectImagesRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this ListVulAffectImagesRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The image_name of this ListVulAffectImagesRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListVulAffectImagesRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param image_name: The image_name of this ListVulAffectImagesRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def registry_name(self):
        r"""Gets the registry_name of this ListVulAffectImagesRequest.

        **参数解释**: 镜像仓名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The registry_name of this ListVulAffectImagesRequest.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this ListVulAffectImagesRequest.

        **参数解释**: 镜像仓名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param registry_name: The registry_name of this ListVulAffectImagesRequest.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def registry_type(self):
        r"""Gets the registry_type of this ListVulAffectImagesRequest.

        **参数解释**: 镜像仓类型 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The registry_type of this ListVulAffectImagesRequest.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this ListVulAffectImagesRequest.

        **参数解释**: 镜像仓类型 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param registry_type: The registry_type of this ListVulAffectImagesRequest.
        :type registry_type: str
        """
        self._registry_type = registry_type

    @property
    def status(self):
        r"""Gets the status of this ListVulAffectImagesRequest.

        **参数解释**: 漏洞对应镜像的处理状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略  **默认取值**: 不涉及 

        :return: The status of this ListVulAffectImagesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVulAffectImagesRequest.

        **参数解释**: 漏洞对应镜像的处理状态 **约束限制**: 不涉及 **取值范围**: - vul_status_unfix：未处理 - vul_status_ignored：已忽略  **默认取值**: 不涉及 

        :param status: The status of this ListVulAffectImagesRequest.
        :type status: str
        """
        self._status = status

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListVulAffectImagesRequest.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The cluster_id of this ListVulAffectImagesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListVulAffectImagesRequest.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param cluster_id: The cluster_id of this ListVulAffectImagesRequest.
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
        if not isinstance(other, ListVulAffectImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
