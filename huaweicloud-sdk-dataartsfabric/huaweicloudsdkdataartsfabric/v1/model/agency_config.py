# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_agency': 'bool',
        'agency_name': 'str'
    }

    attribute_map = {
        'enable_agency': 'enable_agency',
        'agency_name': 'agency_name'
    }

    def __init__(self, enable_agency=None, agency_name=None):
        r"""AgencyConfig

        The model defined in huaweicloud sdk

        :param enable_agency: - **参数解释**：是否开启Ray Service委托授权功能。 - **约束限制**：不涉及。 - **取值范围**：开启true，关闭false。 - **默认取值**：false。 
        :type enable_agency: bool
        :param agency_name: - **参数解释**：授予Ray Service的委托名称。 - **约束限制**：不超过64位。 - **取值范围**：不涉及。 - **默认取值**：null。
        :type agency_name: str
        """
        
        

        self._enable_agency = None
        self._agency_name = None
        self.discriminator = None

        if enable_agency is not None:
            self.enable_agency = enable_agency
        if agency_name is not None:
            self.agency_name = agency_name

    @property
    def enable_agency(self):
        r"""Gets the enable_agency of this AgencyConfig.

        - **参数解释**：是否开启Ray Service委托授权功能。 - **约束限制**：不涉及。 - **取值范围**：开启true，关闭false。 - **默认取值**：false。 

        :return: The enable_agency of this AgencyConfig.
        :rtype: bool
        """
        return self._enable_agency

    @enable_agency.setter
    def enable_agency(self, enable_agency):
        r"""Sets the enable_agency of this AgencyConfig.

        - **参数解释**：是否开启Ray Service委托授权功能。 - **约束限制**：不涉及。 - **取值范围**：开启true，关闭false。 - **默认取值**：false。 

        :param enable_agency: The enable_agency of this AgencyConfig.
        :type enable_agency: bool
        """
        self._enable_agency = enable_agency

    @property
    def agency_name(self):
        r"""Gets the agency_name of this AgencyConfig.

        - **参数解释**：授予Ray Service的委托名称。 - **约束限制**：不超过64位。 - **取值范围**：不涉及。 - **默认取值**：null。

        :return: The agency_name of this AgencyConfig.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this AgencyConfig.

        - **参数解释**：授予Ray Service的委托名称。 - **约束限制**：不超过64位。 - **取值范围**：不涉及。 - **默认取值**：null。

        :param agency_name: The agency_name of this AgencyConfig.
        :type agency_name: str
        """
        self._agency_name = agency_name

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
        if not isinstance(other, AgencyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
