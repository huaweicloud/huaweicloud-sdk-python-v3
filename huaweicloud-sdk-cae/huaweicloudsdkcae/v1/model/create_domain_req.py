# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDomainReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'kind': 'str',
        'metadata': 'CreateMetaDomain'
    }

    attribute_map = {
        'api_version': 'api_version',
        'kind': 'kind',
        'metadata': 'metadata'
    }

    def __init__(self, api_version=None, kind=None, metadata=None):
        r"""CreateDomainReq

        The model defined in huaweicloud sdk

        :param api_version: API版本，固定值“v1”，该值不可修改。
        :type api_version: str
        :param kind: API类型，固定值“Domain”，该值不可修改。
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcae.v1.CreateMetaDomain`
        """
        
        

        self._api_version = None
        self._kind = None
        self._metadata = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        self.metadata = metadata

    @property
    def api_version(self):
        r"""Gets the api_version of this CreateDomainReq.

        API版本，固定值“v1”，该值不可修改。

        :return: The api_version of this CreateDomainReq.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this CreateDomainReq.

        API版本，固定值“v1”，该值不可修改。

        :param api_version: The api_version of this CreateDomainReq.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this CreateDomainReq.

        API类型，固定值“Domain”，该值不可修改。

        :return: The kind of this CreateDomainReq.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this CreateDomainReq.

        API类型，固定值“Domain”，该值不可修改。

        :param kind: The kind of this CreateDomainReq.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this CreateDomainReq.

        :return: The metadata of this CreateDomainReq.
        :rtype: :class:`huaweicloudsdkcae.v1.CreateMetaDomain`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this CreateDomainReq.

        :param metadata: The metadata of this CreateDomainReq.
        :type metadata: :class:`huaweicloudsdkcae.v1.CreateMetaDomain`
        """
        self._metadata = metadata

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
        if not isinstance(other, CreateDomainReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
