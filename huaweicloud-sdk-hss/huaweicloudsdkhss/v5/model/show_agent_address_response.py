# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgentAddressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'anp_address': 'str',
        'region_id': 'str',
        'agent_address': 'str'
    }

    attribute_map = {
        'anp_address': 'anp_address',
        'region_id': 'region_id',
        'agent_address': 'agent_address'
    }

    def __init__(self, anp_address=None, region_id=None, agent_address=None):
        r"""ShowAgentAddressResponse

        The model defined in huaweicloud sdk

        :param anp_address: **参数解释**： pod_lb地址 **取值范围**： 字符长度1-256位 
        :type anp_address: str
        :param region_id: **参数解释**： region_id标识 **取值范围**： 字符长度1-128位 
        :type region_id: str
        :param agent_address: **参数解释**： 公网接入agent地址 **取值范围**： 字符长度1-256位 
        :type agent_address: str
        """
        
        super().__init__()

        self._anp_address = None
        self._region_id = None
        self._agent_address = None
        self.discriminator = None

        if anp_address is not None:
            self.anp_address = anp_address
        if region_id is not None:
            self.region_id = region_id
        if agent_address is not None:
            self.agent_address = agent_address

    @property
    def anp_address(self):
        r"""Gets the anp_address of this ShowAgentAddressResponse.

        **参数解释**： pod_lb地址 **取值范围**： 字符长度1-256位 

        :return: The anp_address of this ShowAgentAddressResponse.
        :rtype: str
        """
        return self._anp_address

    @anp_address.setter
    def anp_address(self, anp_address):
        r"""Sets the anp_address of this ShowAgentAddressResponse.

        **参数解释**： pod_lb地址 **取值范围**： 字符长度1-256位 

        :param anp_address: The anp_address of this ShowAgentAddressResponse.
        :type anp_address: str
        """
        self._anp_address = anp_address

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowAgentAddressResponse.

        **参数解释**： region_id标识 **取值范围**： 字符长度1-128位 

        :return: The region_id of this ShowAgentAddressResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowAgentAddressResponse.

        **参数解释**： region_id标识 **取值范围**： 字符长度1-128位 

        :param region_id: The region_id of this ShowAgentAddressResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def agent_address(self):
        r"""Gets the agent_address of this ShowAgentAddressResponse.

        **参数解释**： 公网接入agent地址 **取值范围**： 字符长度1-256位 

        :return: The agent_address of this ShowAgentAddressResponse.
        :rtype: str
        """
        return self._agent_address

    @agent_address.setter
    def agent_address(self, agent_address):
        r"""Sets the agent_address of this ShowAgentAddressResponse.

        **参数解释**： 公网接入agent地址 **取值范围**： 字符长度1-256位 

        :param agent_address: The agent_address of this ShowAgentAddressResponse.
        :type agent_address: str
        """
        self._agent_address = agent_address

    def to_dict(self):
        import warnings
        warnings.warn("ShowAgentAddressResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAgentAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
