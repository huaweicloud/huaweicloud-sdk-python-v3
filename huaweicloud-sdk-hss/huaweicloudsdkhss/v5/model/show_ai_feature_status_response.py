# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAiFeatureStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ai_defender': 'str',
        'agentarts': 'str',
        'officeace': 'str',
        'openclaw': 'str'
    }

    attribute_map = {
        'ai_defender': 'ai_defender',
        'agentarts': 'agentarts',
        'officeace': 'officeace',
        'openclaw': 'openclaw'
    }

    def __init__(self, ai_defender=None, agentarts=None, officeace=None, openclaw=None):
        r"""ShowAiFeatureStatusResponse

        The model defined in huaweicloud sdk

        :param ai_defender: **参数解释**: AI Defender白名单开关状态 **取值范围**: - not_enabled：该Region已上线AI Defender，但该客户未开通，需显示引导页面 - enabled：该Region已上线AI Defender，并且该客户已开通 
        :type ai_defender: str
        :param agentarts: **参数解释**: AgentArts开关状态 **取值范围**: - not_available：该Region未上线AgentArts，不显示AgentArts任何内容 - not_enabled：该Region已上线AgentArts，但该客户未开通 - enabled：该Region已上线AgentArts，并且该客户已开通 
        :type agentarts: str
        :param officeace: **参数解释**: OfficeAce开关状态 **取值范围**: - not_available：该Region未上线OfficeAce，不显示OfficeAce任何内容 - not_enabled：该Region已上线OfficeAce，但该客户未开通 - enabled：该Region已上线OfficeAce，并且该客户已开通 
        :type officeace: str
        :param openclaw: **参数解释**: OpenClaw开关状态 **取值范围**: - not_available：该Region未上线OpenClaw - enabled：该Region已上线OpenClaw 
        :type openclaw: str
        """
        
        super().__init__()

        self._ai_defender = None
        self._agentarts = None
        self._officeace = None
        self._openclaw = None
        self.discriminator = None

        if ai_defender is not None:
            self.ai_defender = ai_defender
        if agentarts is not None:
            self.agentarts = agentarts
        if officeace is not None:
            self.officeace = officeace
        if openclaw is not None:
            self.openclaw = openclaw

    @property
    def ai_defender(self):
        r"""Gets the ai_defender of this ShowAiFeatureStatusResponse.

        **参数解释**: AI Defender白名单开关状态 **取值范围**: - not_enabled：该Region已上线AI Defender，但该客户未开通，需显示引导页面 - enabled：该Region已上线AI Defender，并且该客户已开通 

        :return: The ai_defender of this ShowAiFeatureStatusResponse.
        :rtype: str
        """
        return self._ai_defender

    @ai_defender.setter
    def ai_defender(self, ai_defender):
        r"""Sets the ai_defender of this ShowAiFeatureStatusResponse.

        **参数解释**: AI Defender白名单开关状态 **取值范围**: - not_enabled：该Region已上线AI Defender，但该客户未开通，需显示引导页面 - enabled：该Region已上线AI Defender，并且该客户已开通 

        :param ai_defender: The ai_defender of this ShowAiFeatureStatusResponse.
        :type ai_defender: str
        """
        self._ai_defender = ai_defender

    @property
    def agentarts(self):
        r"""Gets the agentarts of this ShowAiFeatureStatusResponse.

        **参数解释**: AgentArts开关状态 **取值范围**: - not_available：该Region未上线AgentArts，不显示AgentArts任何内容 - not_enabled：该Region已上线AgentArts，但该客户未开通 - enabled：该Region已上线AgentArts，并且该客户已开通 

        :return: The agentarts of this ShowAiFeatureStatusResponse.
        :rtype: str
        """
        return self._agentarts

    @agentarts.setter
    def agentarts(self, agentarts):
        r"""Sets the agentarts of this ShowAiFeatureStatusResponse.

        **参数解释**: AgentArts开关状态 **取值范围**: - not_available：该Region未上线AgentArts，不显示AgentArts任何内容 - not_enabled：该Region已上线AgentArts，但该客户未开通 - enabled：该Region已上线AgentArts，并且该客户已开通 

        :param agentarts: The agentarts of this ShowAiFeatureStatusResponse.
        :type agentarts: str
        """
        self._agentarts = agentarts

    @property
    def officeace(self):
        r"""Gets the officeace of this ShowAiFeatureStatusResponse.

        **参数解释**: OfficeAce开关状态 **取值范围**: - not_available：该Region未上线OfficeAce，不显示OfficeAce任何内容 - not_enabled：该Region已上线OfficeAce，但该客户未开通 - enabled：该Region已上线OfficeAce，并且该客户已开通 

        :return: The officeace of this ShowAiFeatureStatusResponse.
        :rtype: str
        """
        return self._officeace

    @officeace.setter
    def officeace(self, officeace):
        r"""Sets the officeace of this ShowAiFeatureStatusResponse.

        **参数解释**: OfficeAce开关状态 **取值范围**: - not_available：该Region未上线OfficeAce，不显示OfficeAce任何内容 - not_enabled：该Region已上线OfficeAce，但该客户未开通 - enabled：该Region已上线OfficeAce，并且该客户已开通 

        :param officeace: The officeace of this ShowAiFeatureStatusResponse.
        :type officeace: str
        """
        self._officeace = officeace

    @property
    def openclaw(self):
        r"""Gets the openclaw of this ShowAiFeatureStatusResponse.

        **参数解释**: OpenClaw开关状态 **取值范围**: - not_available：该Region未上线OpenClaw - enabled：该Region已上线OpenClaw 

        :return: The openclaw of this ShowAiFeatureStatusResponse.
        :rtype: str
        """
        return self._openclaw

    @openclaw.setter
    def openclaw(self, openclaw):
        r"""Sets the openclaw of this ShowAiFeatureStatusResponse.

        **参数解释**: OpenClaw开关状态 **取值范围**: - not_available：该Region未上线OpenClaw - enabled：该Region已上线OpenClaw 

        :param openclaw: The openclaw of this ShowAiFeatureStatusResponse.
        :type openclaw: str
        """
        self._openclaw = openclaw

    def to_dict(self):
        import warnings
        warnings.warn("ShowAiFeatureStatusResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowAiFeatureStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
