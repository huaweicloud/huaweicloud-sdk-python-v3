# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageBuildCommandRiskResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'latest_scan_time': 'int',
        'image_num': 'int',
        'risk_id': 'str',
        'rule_id': 'str',
        'risk_name': 'str',
        'risk_level': 'str',
        'description': 'str',
        'image_type': 'str'
    }

    attribute_map = {
        'latest_scan_time': 'latest_scan_time',
        'image_num': 'image_num',
        'risk_id': 'risk_id',
        'rule_id': 'rule_id',
        'risk_name': 'risk_name',
        'risk_level': 'risk_level',
        'description': 'description',
        'image_type': 'image_type'
    }

    def __init__(self, latest_scan_time=None, image_num=None, risk_id=None, rule_id=None, risk_name=None, risk_level=None, description=None, image_type=None):
        r"""ImageBuildCommandRiskResponseInfo

        The model defined in huaweicloud sdk

        :param latest_scan_time: **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 大小0-9223372036854775807 
        :type latest_scan_time: int
        :param image_num: **参数解释**: 受影响的镜像的数量，进行了当前构建指令的镜像数量 **取值范围**: 大小0-2097152 
        :type image_num: int
        :param risk_id: **参数解释** 风险id **取值范围** 字符长度1-64位
        :type risk_id: str
        :param rule_id: **参数解释** 风险检测规则id **取值范围** 字符长度1-64位
        :type rule_id: str
        :param risk_name: **参数解释** 风险名称 **取值范围** 字符长度1-512位
        :type risk_name: str
        :param risk_level: **参数解释** 风险程度 **取值范围** - critical：严重。 - high：高危。 - medium：中危。 - low：低危。
        :type risk_level: str
        :param description: **参数解释** 风险描述 **取值范围** 字符长度0-65534位
        :type description: str
        :param image_type: **参数解释** 镜像类型 **取值范围** 字符长度1-32位
        :type image_type: str
        """
        
        

        self._latest_scan_time = None
        self._image_num = None
        self._risk_id = None
        self._rule_id = None
        self._risk_name = None
        self._risk_level = None
        self._description = None
        self._image_type = None
        self.discriminator = None

        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if image_num is not None:
            self.image_num = image_num
        if risk_id is not None:
            self.risk_id = risk_id
        if rule_id is not None:
            self.rule_id = rule_id
        if risk_name is not None:
            self.risk_name = risk_name
        if risk_level is not None:
            self.risk_level = risk_level
        if description is not None:
            self.description = description
        if image_type is not None:
            self.image_type = image_type

    @property
    def latest_scan_time(self):
        r"""Gets the latest_scan_time of this ImageBuildCommandRiskResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 大小0-9223372036854775807 

        :return: The latest_scan_time of this ImageBuildCommandRiskResponseInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        r"""Sets the latest_scan_time of this ImageBuildCommandRiskResponseInfo.

        **参数解释**: 最后一次检测时间，时间单位 毫秒（ms） **取值范围**: 大小0-9223372036854775807 

        :param latest_scan_time: The latest_scan_time of this ImageBuildCommandRiskResponseInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def image_num(self):
        r"""Gets the image_num of this ImageBuildCommandRiskResponseInfo.

        **参数解释**: 受影响的镜像的数量，进行了当前构建指令的镜像数量 **取值范围**: 大小0-2097152 

        :return: The image_num of this ImageBuildCommandRiskResponseInfo.
        :rtype: int
        """
        return self._image_num

    @image_num.setter
    def image_num(self, image_num):
        r"""Sets the image_num of this ImageBuildCommandRiskResponseInfo.

        **参数解释**: 受影响的镜像的数量，进行了当前构建指令的镜像数量 **取值范围**: 大小0-2097152 

        :param image_num: The image_num of this ImageBuildCommandRiskResponseInfo.
        :type image_num: int
        """
        self._image_num = image_num

    @property
    def risk_id(self):
        r"""Gets the risk_id of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 风险id **取值范围** 字符长度1-64位

        :return: The risk_id of this ImageBuildCommandRiskResponseInfo.
        :rtype: str
        """
        return self._risk_id

    @risk_id.setter
    def risk_id(self, risk_id):
        r"""Sets the risk_id of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 风险id **取值范围** 字符长度1-64位

        :param risk_id: The risk_id of this ImageBuildCommandRiskResponseInfo.
        :type risk_id: str
        """
        self._risk_id = risk_id

    @property
    def rule_id(self):
        r"""Gets the rule_id of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 风险检测规则id **取值范围** 字符长度1-64位

        :return: The rule_id of this ImageBuildCommandRiskResponseInfo.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 风险检测规则id **取值范围** 字符长度1-64位

        :param rule_id: The rule_id of this ImageBuildCommandRiskResponseInfo.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def risk_name(self):
        r"""Gets the risk_name of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 风险名称 **取值范围** 字符长度1-512位

        :return: The risk_name of this ImageBuildCommandRiskResponseInfo.
        :rtype: str
        """
        return self._risk_name

    @risk_name.setter
    def risk_name(self, risk_name):
        r"""Sets the risk_name of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 风险名称 **取值范围** 字符长度1-512位

        :param risk_name: The risk_name of this ImageBuildCommandRiskResponseInfo.
        :type risk_name: str
        """
        self._risk_name = risk_name

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 风险程度 **取值范围** - critical：严重。 - high：高危。 - medium：中危。 - low：低危。

        :return: The risk_level of this ImageBuildCommandRiskResponseInfo.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 风险程度 **取值范围** - critical：严重。 - high：高危。 - medium：中危。 - low：低危。

        :param risk_level: The risk_level of this ImageBuildCommandRiskResponseInfo.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def description(self):
        r"""Gets the description of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 风险描述 **取值范围** 字符长度0-65534位

        :return: The description of this ImageBuildCommandRiskResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 风险描述 **取值范围** 字符长度0-65534位

        :param description: The description of this ImageBuildCommandRiskResponseInfo.
        :type description: str
        """
        self._description = description

    @property
    def image_type(self):
        r"""Gets the image_type of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 镜像类型 **取值范围** 字符长度1-32位

        :return: The image_type of this ImageBuildCommandRiskResponseInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ImageBuildCommandRiskResponseInfo.

        **参数解释** 镜像类型 **取值范围** 字符长度1-32位

        :param image_type: The image_type of this ImageBuildCommandRiskResponseInfo.
        :type image_type: str
        """
        self._image_type = image_type

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
        if not isinstance(other, ImageBuildCommandRiskResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
