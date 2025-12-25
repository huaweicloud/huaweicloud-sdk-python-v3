# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateShipperDelegateAuthRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_name': 'str'
    }

    attribute_map = {
        'agency_name': 'agency_name'
    }

    def __init__(self, agency_name=None):
        r"""CreateShipperDelegateAuthRequestBody

        The model defined in huaweicloud sdk

        :param agency_name: 委托的名称。
        :type agency_name: str
        """
        
        

        self._agency_name = None
        self.discriminator = None

        if agency_name is not None:
            self.agency_name = agency_name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateShipperDelegateAuthRequestBody.

        委托的名称。

        :return: The agency_name of this CreateShipperDelegateAuthRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateShipperDelegateAuthRequestBody.

        委托的名称。

        :param agency_name: The agency_name of this CreateShipperDelegateAuthRequestBody.
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
        if not isinstance(other, CreateShipperDelegateAuthRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
