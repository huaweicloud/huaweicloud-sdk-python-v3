# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageBuildCommandRisksImagesRequest:

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
        'image_type': 'str',
        'rule_id': 'str',
        'image_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'image_type': 'image_type',
        'rule_id': 'rule_id',
        'image_id': 'image_id'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, image_type=None, rule_id=None, image_id=None):
        r"""ListImageBuildCommandRisksImagesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param image_type: **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**:   - cicd：cicd镜像   - registry：仓库镜像 字符长度1-32 **默认取值**: 不涉及 
        :type image_type: str
        :param rule_id: **参数解释**: 风险检测规则ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64 **默认取值**: 不涉及 
        :type rule_id: str
        :param image_id: **参数解释**： 镜像id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 
        :type image_id: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._image_type = None
        self._rule_id = None
        self._image_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.image_type = image_type
        self.rule_id = rule_id
        if image_id is not None:
            self.image_id = image_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListImageBuildCommandRisksImagesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListImageBuildCommandRisksImagesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListImageBuildCommandRisksImagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListImageBuildCommandRisksImagesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListImageBuildCommandRisksImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListImageBuildCommandRisksImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def image_type(self):
        r"""Gets the image_type of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**:   - cicd：cicd镜像   - registry：仓库镜像 字符长度1-32 **默认取值**: 不涉及 

        :return: The image_type of this ListImageBuildCommandRisksImagesRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**:   - cicd：cicd镜像   - registry：仓库镜像 字符长度1-32 **默认取值**: 不涉及 

        :param image_type: The image_type of this ListImageBuildCommandRisksImagesRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def rule_id(self):
        r"""Gets the rule_id of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**: 风险检测规则ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64 **默认取值**: 不涉及 

        :return: The rule_id of this ListImageBuildCommandRisksImagesRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**: 风险检测规则ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64 **默认取值**: 不涉及 

        :param rule_id: The rule_id of this ListImageBuildCommandRisksImagesRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def image_id(self):
        r"""Gets the image_id of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**： 镜像id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 

        :return: The image_id of this ListImageBuildCommandRisksImagesRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListImageBuildCommandRisksImagesRequest.

        **参数解释**： 镜像id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 

        :param image_id: The image_id of this ListImageBuildCommandRisksImagesRequest.
        :type image_id: str
        """
        self._image_id = image_id

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
        if not isinstance(other, ListImageBuildCommandRisksImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
