# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgencyPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_name': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'agency_name': 'agency_name',
        'x_language': 'X-Language'
    }

    def __init__(self, agency_name=None, x_language=None):
        r"""ShowAgencyPolicyRequest

        The model defined in huaweicloud sdk

        :param agency_name: 委托名称。目前仅支持RDSAccessProjectResource。
        :type agency_name: str
        :param x_language: 语言。默认en-us。
        :type x_language: str
        """
        
        

        self._agency_name = None
        self._x_language = None
        self.discriminator = None

        self.agency_name = agency_name
        if x_language is not None:
            self.x_language = x_language

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ShowAgencyPolicyRequest.

        委托名称。目前仅支持RDSAccessProjectResource。

        :return: The agency_name of this ShowAgencyPolicyRequest.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ShowAgencyPolicyRequest.

        委托名称。目前仅支持RDSAccessProjectResource。

        :param agency_name: The agency_name of this ShowAgencyPolicyRequest.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowAgencyPolicyRequest.

        语言。默认en-us。

        :return: The x_language of this ShowAgencyPolicyRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowAgencyPolicyRequest.

        语言。默认en-us。

        :param x_language: The x_language of this ShowAgencyPolicyRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowAgencyPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
