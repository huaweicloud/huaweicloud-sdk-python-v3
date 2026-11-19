# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityScoreRequest:

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
        'need_cal_score': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'need_cal_score': 'need_cal_score'
    }

    def __init__(self, enterprise_project_id=None, need_cal_score=None):
        r"""ShowSecurityScoreRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param need_cal_score: **参数解释**: 是否计算分数 **约束限制**: 不涉及 **取值范围**: - 0：不计算 - 1：计算  **默认取值**: 0 
        :type need_cal_score: int
        """
        
        

        self._enterprise_project_id = None
        self._need_cal_score = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if need_cal_score is not None:
            self.need_cal_score = need_cal_score

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowSecurityScoreRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowSecurityScoreRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowSecurityScoreRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowSecurityScoreRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def need_cal_score(self):
        r"""Gets the need_cal_score of this ShowSecurityScoreRequest.

        **参数解释**: 是否计算分数 **约束限制**: 不涉及 **取值范围**: - 0：不计算 - 1：计算  **默认取值**: 0 

        :return: The need_cal_score of this ShowSecurityScoreRequest.
        :rtype: int
        """
        return self._need_cal_score

    @need_cal_score.setter
    def need_cal_score(self, need_cal_score):
        r"""Sets the need_cal_score of this ShowSecurityScoreRequest.

        **参数解释**: 是否计算分数 **约束限制**: 不涉及 **取值范围**: - 0：不计算 - 1：计算  **默认取值**: 0 

        :param need_cal_score: The need_cal_score of this ShowSecurityScoreRequest.
        :type need_cal_score: int
        """
        self._need_cal_score = need_cal_score

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
        if not isinstance(other, ShowSecurityScoreRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
