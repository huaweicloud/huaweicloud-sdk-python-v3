# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageBuildCommandRisksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'image_type': 'str',
        'image_id': 'str',
        'risk_name': 'str',
        'risk_level': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'image_type': 'image_type',
        'image_id': 'image_id',
        'risk_name': 'risk_name',
        'risk_level': 'risk_level'
    }

    def __init__(self, region=None, enterprise_project_id=None, limit=None, offset=None, image_type=None, image_id=None, risk_name=None, risk_level=None):
        r"""ListImageBuildCommandRisksRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param image_type: **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**:   - cicd：cicd镜像   - registry：仓库镜像 字符长度1-32  **默认取值**: 不涉及 
        :type image_type: str
        :param image_id: **参数解释**： 镜像id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 
        :type image_id: str
        :param risk_name: **参数解释**： 风险名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-512位 **默认取值**： 不涉及 
        :type risk_name: str
        :param risk_level: **参数解释**: 风险程度 **约束限制**: 不涉及 **取值范围**:   - critical ：严重   - high ：高危   - medium ：中危   - low ：低危 字符长度1-64  **默认取值**: 不涉及 
        :type risk_level: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._image_type = None
        self._image_id = None
        self._risk_name = None
        self._risk_level = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.image_type = image_type
        if image_id is not None:
            self.image_id = image_id
        if risk_name is not None:
            self.risk_name = risk_name
        if risk_level is not None:
            self.risk_level = risk_level

    @property
    def region(self):
        r"""Gets the region of this ListImageBuildCommandRisksRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListImageBuildCommandRisksRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListImageBuildCommandRisksRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListImageBuildCommandRisksRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImageBuildCommandRisksRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListImageBuildCommandRisksRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImageBuildCommandRisksRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListImageBuildCommandRisksRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListImageBuildCommandRisksRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListImageBuildCommandRisksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageBuildCommandRisksRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListImageBuildCommandRisksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListImageBuildCommandRisksRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListImageBuildCommandRisksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageBuildCommandRisksRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListImageBuildCommandRisksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def image_type(self):
        r"""Gets the image_type of this ListImageBuildCommandRisksRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**:   - cicd：cicd镜像   - registry：仓库镜像 字符长度1-32  **默认取值**: 不涉及 

        :return: The image_type of this ListImageBuildCommandRisksRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListImageBuildCommandRisksRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**:   - cicd：cicd镜像   - registry：仓库镜像 字符长度1-32  **默认取值**: 不涉及 

        :param image_type: The image_type of this ListImageBuildCommandRisksRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_id(self):
        r"""Gets the image_id of this ListImageBuildCommandRisksRequest.

        **参数解释**： 镜像id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 

        :return: The image_id of this ListImageBuildCommandRisksRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListImageBuildCommandRisksRequest.

        **参数解释**： 镜像id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 

        :param image_id: The image_id of this ListImageBuildCommandRisksRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def risk_name(self):
        r"""Gets the risk_name of this ListImageBuildCommandRisksRequest.

        **参数解释**： 风险名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-512位 **默认取值**： 不涉及 

        :return: The risk_name of this ListImageBuildCommandRisksRequest.
        :rtype: str
        """
        return self._risk_name

    @risk_name.setter
    def risk_name(self, risk_name):
        r"""Sets the risk_name of this ListImageBuildCommandRisksRequest.

        **参数解释**： 风险名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-512位 **默认取值**： 不涉及 

        :param risk_name: The risk_name of this ListImageBuildCommandRisksRequest.
        :type risk_name: str
        """
        self._risk_name = risk_name

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ListImageBuildCommandRisksRequest.

        **参数解释**: 风险程度 **约束限制**: 不涉及 **取值范围**:   - critical ：严重   - high ：高危   - medium ：中危   - low ：低危 字符长度1-64  **默认取值**: 不涉及 

        :return: The risk_level of this ListImageBuildCommandRisksRequest.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ListImageBuildCommandRisksRequest.

        **参数解释**: 风险程度 **约束限制**: 不涉及 **取值范围**:   - critical ：严重   - high ：高危   - medium ：中危   - low ：低危 字符长度1-64  **默认取值**: 不涉及 

        :param risk_level: The risk_level of this ListImageBuildCommandRisksRequest.
        :type risk_level: str
        """
        self._risk_level = risk_level

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
        if not isinstance(other, ListImageBuildCommandRisksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
