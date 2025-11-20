# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainConfigRequest:

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
        'body': 'UpdateDomainConfigRequestBody'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'body': 'body'
    }

    def __init__(self, domain_id=None, body=None):
        r"""UpdateDomainConfigRequest

        The model defined in huaweicloud sdk

        :param domain_id: 域名id
        :type domain_id: str
        :param body: Body of the UpdateDomainConfigRequest
        :type body: :class:`huaweicloudsdkaad.v2.UpdateDomainConfigRequestBody`
        """
        
        

        self._domain_id = None
        self._body = None
        self.discriminator = None

        self.domain_id = domain_id
        if body is not None:
            self.body = body

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UpdateDomainConfigRequest.

        域名id

        :return: The domain_id of this UpdateDomainConfigRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UpdateDomainConfigRequest.

        域名id

        :param domain_id: The domain_id of this UpdateDomainConfigRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def body(self):
        r"""Gets the body of this UpdateDomainConfigRequest.

        :return: The body of this UpdateDomainConfigRequest.
        :rtype: :class:`huaweicloudsdkaad.v2.UpdateDomainConfigRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateDomainConfigRequest.

        :param body: The body of this UpdateDomainConfigRequest.
        :type body: :class:`huaweicloudsdkaad.v2.UpdateDomainConfigRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateDomainConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
