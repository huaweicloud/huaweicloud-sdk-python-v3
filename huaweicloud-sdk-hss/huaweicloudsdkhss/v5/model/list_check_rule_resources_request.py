# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCheckRuleResourcesRequest:

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
        'check_rule_id': 'str',
        'check_name': 'str',
        'standard': 'str',
        'scan_result': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'image_type': 'image_type',
        'check_rule_id': 'check_rule_id',
        'check_name': 'check_name',
        'standard': 'standard',
        'scan_result': 'scan_result'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, type=None, image_type=None, check_rule_id=None, check_name=None, standard=None, scan_result=None):
        r"""ListCheckRuleResourcesRequest

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
        :param check_rule_id: **参数解释**: 检查项ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 
        :type check_rule_id: str
        :param check_name: **参数解释**: 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 
        :type check_name: str
        :param standard: **参数解释**: 标准类型 **约束限制**: 不涉及 **取值范围**: - cn_standard：等保合规标准 - hw_standard：云安全实践标准 **默认取值**: 不涉及
        :type standard: str
        :param scan_result: **参数解释**: 检测结果 **约束限制**: 不涉及 **取值范围**: - pass：通过 - failed：未通过  **默认取值**: 不涉及
        :type scan_result: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._type = None
        self._image_type = None
        self._check_rule_id = None
        self._check_name = None
        self._standard = None
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
        self.check_rule_id = check_rule_id
        self.check_name = check_name
        self.standard = standard
        if scan_result is not None:
            self.scan_result = scan_result

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListCheckRuleResourcesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListCheckRuleResourcesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListCheckRuleResourcesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListCheckRuleResourcesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListCheckRuleResourcesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListCheckRuleResourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCheckRuleResourcesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListCheckRuleResourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCheckRuleResourcesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListCheckRuleResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCheckRuleResourcesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListCheckRuleResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        r"""Gets the type of this ListCheckRuleResourcesRequest.

        **参数解释**: 类型 **约束限制**: 不涉及 **取值范围**: - image : 镜像  **默认取值**: 不涉及 

        :return: The type of this ListCheckRuleResourcesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListCheckRuleResourcesRequest.

        **参数解释**: 类型 **约束限制**: 不涉及 **取值范围**: - image : 镜像  **默认取值**: 不涉及 

        :param type: The type of this ListCheckRuleResourcesRequest.
        :type type: str
        """
        self._type = type

    @property
    def image_type(self):
        r"""Gets the image_type of this ListCheckRuleResourcesRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - cicd：cicd镜像 - registry：仓库镜像  **默认取值**: 不涉及 

        :return: The image_type of this ListCheckRuleResourcesRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListCheckRuleResourcesRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - cicd：cicd镜像 - registry：仓库镜像  **默认取值**: 不涉及 

        :param image_type: The image_type of this ListCheckRuleResourcesRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def check_rule_id(self):
        r"""Gets the check_rule_id of this ListCheckRuleResourcesRequest.

        **参数解释**: 检查项ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 

        :return: The check_rule_id of this ListCheckRuleResourcesRequest.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        r"""Sets the check_rule_id of this ListCheckRuleResourcesRequest.

        **参数解释**: 检查项ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 

        :param check_rule_id: The check_rule_id of this ListCheckRuleResourcesRequest.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def check_name(self):
        r"""Gets the check_name of this ListCheckRuleResourcesRequest.

        **参数解释**: 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 

        :return: The check_name of this ListCheckRuleResourcesRequest.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ListCheckRuleResourcesRequest.

        **参数解释**: 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 

        :param check_name: The check_name of this ListCheckRuleResourcesRequest.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def standard(self):
        r"""Gets the standard of this ListCheckRuleResourcesRequest.

        **参数解释**: 标准类型 **约束限制**: 不涉及 **取值范围**: - cn_standard：等保合规标准 - hw_standard：云安全实践标准 **默认取值**: 不涉及

        :return: The standard of this ListCheckRuleResourcesRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ListCheckRuleResourcesRequest.

        **参数解释**: 标准类型 **约束限制**: 不涉及 **取值范围**: - cn_standard：等保合规标准 - hw_standard：云安全实践标准 **默认取值**: 不涉及

        :param standard: The standard of this ListCheckRuleResourcesRequest.
        :type standard: str
        """
        self._standard = standard

    @property
    def scan_result(self):
        r"""Gets the scan_result of this ListCheckRuleResourcesRequest.

        **参数解释**: 检测结果 **约束限制**: 不涉及 **取值范围**: - pass：通过 - failed：未通过  **默认取值**: 不涉及

        :return: The scan_result of this ListCheckRuleResourcesRequest.
        :rtype: str
        """
        return self._scan_result

    @scan_result.setter
    def scan_result(self, scan_result):
        r"""Sets the scan_result of this ListCheckRuleResourcesRequest.

        **参数解释**: 检测结果 **约束限制**: 不涉及 **取值范围**: - pass：通过 - failed：未通过  **默认取值**: 不涉及

        :param scan_result: The scan_result of this ListCheckRuleResourcesRequest.
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
        if not isinstance(other, ListCheckRuleResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
