# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiComponentStatisticsRequest:

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
        'category': 'str',
        'catalogue': 'str',
        'limit': 'int',
        'offset': 'int',
        'ai_component_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'category': 'category',
        'catalogue': 'catalogue',
        'limit': 'limit',
        'offset': 'offset',
        'ai_component_name': 'ai_component_name'
    }

    def __init__(self, enterprise_project_id=None, category=None, catalogue=None, limit=None, offset=None, ai_component_name=None):
        r"""ListAiComponentStatisticsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param category: **参数解释**: 资产类别 **约束限制**: 不涉及 **取值范围**: - host：主机资产 - container：容器资产  **默认取值**: host 
        :type category: str
        :param catalogue: **参数解释**: AI组件类别 **约束限制**: 不涉及 **取值范围**: - app：应用 - tool：工具  **默认取值**: 不涉及
        :type catalogue: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param ai_component_name: **参数解释**： AI组件对应类型的名称 **取值范围**： 字符长度1-256位 **约束限制**: 不涉及 **默认取值**: 不涉及 
        :type ai_component_name: str
        """
        
        

        self._enterprise_project_id = None
        self._category = None
        self._catalogue = None
        self._limit = None
        self._offset = None
        self._ai_component_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.category = category
        self.catalogue = catalogue
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if ai_component_name is not None:
            self.ai_component_name = ai_component_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAiComponentStatisticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListAiComponentStatisticsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAiComponentStatisticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListAiComponentStatisticsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def category(self):
        r"""Gets the category of this ListAiComponentStatisticsRequest.

        **参数解释**: 资产类别 **约束限制**: 不涉及 **取值范围**: - host：主机资产 - container：容器资产  **默认取值**: host 

        :return: The category of this ListAiComponentStatisticsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListAiComponentStatisticsRequest.

        **参数解释**: 资产类别 **约束限制**: 不涉及 **取值范围**: - host：主机资产 - container：容器资产  **默认取值**: host 

        :param category: The category of this ListAiComponentStatisticsRequest.
        :type category: str
        """
        self._category = category

    @property
    def catalogue(self):
        r"""Gets the catalogue of this ListAiComponentStatisticsRequest.

        **参数解释**: AI组件类别 **约束限制**: 不涉及 **取值范围**: - app：应用 - tool：工具  **默认取值**: 不涉及

        :return: The catalogue of this ListAiComponentStatisticsRequest.
        :rtype: str
        """
        return self._catalogue

    @catalogue.setter
    def catalogue(self, catalogue):
        r"""Sets the catalogue of this ListAiComponentStatisticsRequest.

        **参数解释**: AI组件类别 **约束限制**: 不涉及 **取值范围**: - app：应用 - tool：工具  **默认取值**: 不涉及

        :param catalogue: The catalogue of this ListAiComponentStatisticsRequest.
        :type catalogue: str
        """
        self._catalogue = catalogue

    @property
    def limit(self):
        r"""Gets the limit of this ListAiComponentStatisticsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListAiComponentStatisticsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAiComponentStatisticsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListAiComponentStatisticsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAiComponentStatisticsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListAiComponentStatisticsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAiComponentStatisticsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListAiComponentStatisticsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def ai_component_name(self):
        r"""Gets the ai_component_name of this ListAiComponentStatisticsRequest.

        **参数解释**： AI组件对应类型的名称 **取值范围**： 字符长度1-256位 **约束限制**: 不涉及 **默认取值**: 不涉及 

        :return: The ai_component_name of this ListAiComponentStatisticsRequest.
        :rtype: str
        """
        return self._ai_component_name

    @ai_component_name.setter
    def ai_component_name(self, ai_component_name):
        r"""Sets the ai_component_name of this ListAiComponentStatisticsRequest.

        **参数解释**： AI组件对应类型的名称 **取值范围**： 字符长度1-256位 **约束限制**: 不涉及 **默认取值**: 不涉及 

        :param ai_component_name: The ai_component_name of this ListAiComponentStatisticsRequest.
        :type ai_component_name: str
        """
        self._ai_component_name = ai_component_name

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
        if not isinstance(other, ListAiComponentStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
