# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloseDomainNewReq:

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
        'auth_type': 'DomainType'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'auth_type': 'auth_type'
    }

    def __init__(self, domain_id=None, auth_type=None):
        r"""CloseDomainNewReq

        The model defined in huaweicloud sdk

        :param domain_id: 域id。
        :type domain_id: str
        :param auth_type: 
        :type auth_type: :class:`huaweicloudsdkworkspace.v2.DomainType`
        """
        
        

        self._domain_id = None
        self._auth_type = None
        self.discriminator = None

        self.domain_id = domain_id
        self.auth_type = auth_type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CloseDomainNewReq.

        域id。

        :return: The domain_id of this CloseDomainNewReq.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CloseDomainNewReq.

        域id。

        :param domain_id: The domain_id of this CloseDomainNewReq.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def auth_type(self):
        r"""Gets the auth_type of this CloseDomainNewReq.

        :return: The auth_type of this CloseDomainNewReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DomainType`
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this CloseDomainNewReq.

        :param auth_type: The auth_type of this CloseDomainNewReq.
        :type auth_type: :class:`huaweicloudsdkworkspace.v2.DomainType`
        """
        self._auth_type = auth_type

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
        if not isinstance(other, CloseDomainNewReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
