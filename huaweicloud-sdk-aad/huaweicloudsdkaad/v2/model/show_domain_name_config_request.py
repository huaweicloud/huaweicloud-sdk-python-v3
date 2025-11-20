# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainNameConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'type': 'type'
    }

    def __init__(self, domain_id=None, type=None):
        r"""ShowDomainNameConfigRequest

        The model defined in huaweicloud sdk

        :param domain_id: 域名id
        :type domain_id: str
        :param type: 请求类型 domain、waf
        :type type: str
        """
        
        

        self._domain_id = None
        self._type = None
        self.discriminator = None

        self.domain_id = domain_id
        self.type = type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowDomainNameConfigRequest.

        域名id

        :return: The domain_id of this ShowDomainNameConfigRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowDomainNameConfigRequest.

        域名id

        :param domain_id: The domain_id of this ShowDomainNameConfigRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def type(self):
        r"""Gets the type of this ShowDomainNameConfigRequest.

        请求类型 domain、waf

        :return: The type of this ShowDomainNameConfigRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowDomainNameConfigRequest.

        请求类型 domain、waf

        :param type: The type of this ShowDomainNameConfigRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowDomainNameConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
