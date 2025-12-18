# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgencyInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'agency_name': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'agency_name': 'agency_name'
    }

    def __init__(self, x_language=None, agency_name=None):
        r"""ListAgencyInfosRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param agency_name: **参数解释**: 委托名称 **约束限制**: 不涉及。 **取值范围**: RDSAccessProjectResource **默认取值**: RDSAccessProjectResource
        :type agency_name: str
        """
        
        

        self._x_language = None
        self._agency_name = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.agency_name = agency_name

    @property
    def x_language(self):
        r"""Gets the x_language of this ListAgencyInfosRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ListAgencyInfosRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListAgencyInfosRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ListAgencyInfosRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ListAgencyInfosRequest.

        **参数解释**: 委托名称 **约束限制**: 不涉及。 **取值范围**: RDSAccessProjectResource **默认取值**: RDSAccessProjectResource

        :return: The agency_name of this ListAgencyInfosRequest.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ListAgencyInfosRequest.

        **参数解释**: 委托名称 **约束限制**: 不涉及。 **取值范围**: RDSAccessProjectResource **默认取值**: RDSAccessProjectResource

        :param agency_name: The agency_name of this ListAgencyInfosRequest.
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
        if not isinstance(other, ListAgencyInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
