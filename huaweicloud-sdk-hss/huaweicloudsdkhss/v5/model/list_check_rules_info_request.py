# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCheckRulesInfoRequest:

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
        'image_type': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'instance_id': 'str',
        'image_id': 'str',
        'scan_result': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'image_type': 'image_type',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'instance_id': 'instance_id',
        'image_id': 'image_id',
        'scan_result': 'scan_result'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, type=None, image_type=None, namespace=None, image_name=None, image_version=None, instance_id=None, image_id=None, scan_result=None):
        r"""ListCheckRulesInfoRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param type: **参数解释**: 类型 **约束限制**: 不涉及 **取值范围**: - image : 镜像  **默认取值**: 不涉及 
        :type type: str
        :param image_type: **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - cicd：cicd镜像 - registry：仓库镜像  **默认取值**: 不涉及 
        :type image_type: str
        :param namespace: **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符串大小0-65535 **默认取值**: 不涉及 
        :type namespace: str
        :param image_name: **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符串大小0-65535 **默认取值**: 不涉及 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本名称 **约束限制**: 不涉及 **取值范围**: 字符串大小0-65535 **默认取值**: 不涉及 
        :type image_version: str
        :param instance_id: **参数解释**: 企业仓库实例ID，swr共享版无需使用该参数 **约束限制**: 不涉及 **取值范围**: 字符串大小0-128 **默认取值**: 不涉及 
        :type instance_id: str
        :param image_id: **参数解释**: 镜像id **约束限制**： 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type image_id: str
        :param scan_result: **参数解释**: 检测结果 **约束限制**: 不涉及 **取值范围**:   - pass：通过   - failed：未通过 **默认取值**: 不涉及
        :type scan_result: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._type = None
        self._image_type = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._instance_id = None
        self._image_id = None
        self._scan_result = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.type = type
        self.image_type = image_type
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if instance_id is not None:
            self.instance_id = instance_id
        if image_id is not None:
            self.image_id = image_id
        if scan_result is not None:
            self.scan_result = scan_result

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListCheckRulesInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListCheckRulesInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListCheckRulesInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListCheckRulesInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListCheckRulesInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListCheckRulesInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCheckRulesInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListCheckRulesInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCheckRulesInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListCheckRulesInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCheckRulesInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListCheckRulesInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        r"""Gets the type of this ListCheckRulesInfoRequest.

        **参数解释**: 类型 **约束限制**: 不涉及 **取值范围**: - image : 镜像  **默认取值**: 不涉及 

        :return: The type of this ListCheckRulesInfoRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListCheckRulesInfoRequest.

        **参数解释**: 类型 **约束限制**: 不涉及 **取值范围**: - image : 镜像  **默认取值**: 不涉及 

        :param type: The type of this ListCheckRulesInfoRequest.
        :type type: str
        """
        self._type = type

    @property
    def image_type(self):
        r"""Gets the image_type of this ListCheckRulesInfoRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - cicd：cicd镜像 - registry：仓库镜像  **默认取值**: 不涉及 

        :return: The image_type of this ListCheckRulesInfoRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListCheckRulesInfoRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - cicd：cicd镜像 - registry：仓库镜像  **默认取值**: 不涉及 

        :param image_type: The image_type of this ListCheckRulesInfoRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def namespace(self):
        r"""Gets the namespace of this ListCheckRulesInfoRequest.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符串大小0-65535 **默认取值**: 不涉及 

        :return: The namespace of this ListCheckRulesInfoRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListCheckRulesInfoRequest.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符串大小0-65535 **默认取值**: 不涉及 

        :param namespace: The namespace of this ListCheckRulesInfoRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ListCheckRulesInfoRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符串大小0-65535 **默认取值**: 不涉及 

        :return: The image_name of this ListCheckRulesInfoRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListCheckRulesInfoRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符串大小0-65535 **默认取值**: 不涉及 

        :param image_name: The image_name of this ListCheckRulesInfoRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ListCheckRulesInfoRequest.

        **参数解释**: 镜像版本名称 **约束限制**: 不涉及 **取值范围**: 字符串大小0-65535 **默认取值**: 不涉及 

        :return: The image_version of this ListCheckRulesInfoRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListCheckRulesInfoRequest.

        **参数解释**: 镜像版本名称 **约束限制**: 不涉及 **取值范围**: 字符串大小0-65535 **默认取值**: 不涉及 

        :param image_version: The image_version of this ListCheckRulesInfoRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListCheckRulesInfoRequest.

        **参数解释**: 企业仓库实例ID，swr共享版无需使用该参数 **约束限制**: 不涉及 **取值范围**: 字符串大小0-128 **默认取值**: 不涉及 

        :return: The instance_id of this ListCheckRulesInfoRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListCheckRulesInfoRequest.

        **参数解释**: 企业仓库实例ID，swr共享版无需使用该参数 **约束限制**: 不涉及 **取值范围**: 字符串大小0-128 **默认取值**: 不涉及 

        :param instance_id: The instance_id of this ListCheckRulesInfoRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def image_id(self):
        r"""Gets the image_id of this ListCheckRulesInfoRequest.

        **参数解释**: 镜像id **约束限制**： 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The image_id of this ListCheckRulesInfoRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListCheckRulesInfoRequest.

        **参数解释**: 镜像id **约束限制**： 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param image_id: The image_id of this ListCheckRulesInfoRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def scan_result(self):
        r"""Gets the scan_result of this ListCheckRulesInfoRequest.

        **参数解释**: 检测结果 **约束限制**: 不涉及 **取值范围**:   - pass：通过   - failed：未通过 **默认取值**: 不涉及

        :return: The scan_result of this ListCheckRulesInfoRequest.
        :rtype: str
        """
        return self._scan_result

    @scan_result.setter
    def scan_result(self, scan_result):
        r"""Sets the scan_result of this ListCheckRulesInfoRequest.

        **参数解释**: 检测结果 **约束限制**: 不涉及 **取值范围**:   - pass：通过   - failed：未通过 **默认取值**: 不涉及

        :param scan_result: The scan_result of this ListCheckRulesInfoRequest.
        :type scan_result: str
        """
        self._scan_result = scan_result

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
        if not isinstance(other, ListCheckRulesInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
