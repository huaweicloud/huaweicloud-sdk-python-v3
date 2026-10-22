# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobUpdateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'spec': 'JobUpdateRequestBodySpec',
        'endpoints': 'JobEndpointsReq',
        'metadata': 'JobUpdateRequestBodyMetadata'
    }

    attribute_map = {
        'description': 'description',
        'spec': 'spec',
        'endpoints': 'endpoints',
        'metadata': 'metadata'
    }

    def __init__(self, description=None, spec=None, endpoints=None, metadata=None):
        r"""JobUpdateRequestBody

        The model defined in huaweicloud sdk

        :param description: 对训练作业的描述，默认为“NULL”，字符串的长度限制为[0, 256]。
        :type description: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkmodelarts.v1.JobUpdateRequestBodySpec`
        :param endpoints: 
        :type endpoints: :class:`huaweicloudsdkmodelarts.v1.JobEndpointsReq`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.JobUpdateRequestBodyMetadata`
        """
        
        

        self._description = None
        self._spec = None
        self._endpoints = None
        self._metadata = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if spec is not None:
            self.spec = spec
        if endpoints is not None:
            self.endpoints = endpoints
        if metadata is not None:
            self.metadata = metadata

    @property
    def description(self):
        r"""Gets the description of this JobUpdateRequestBody.

        对训练作业的描述，默认为“NULL”，字符串的长度限制为[0, 256]。

        :return: The description of this JobUpdateRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this JobUpdateRequestBody.

        对训练作业的描述，默认为“NULL”，字符串的长度限制为[0, 256]。

        :param description: The description of this JobUpdateRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def spec(self):
        r"""Gets the spec of this JobUpdateRequestBody.

        :return: The spec of this JobUpdateRequestBody.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobUpdateRequestBodySpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this JobUpdateRequestBody.

        :param spec: The spec of this JobUpdateRequestBody.
        :type spec: :class:`huaweicloudsdkmodelarts.v1.JobUpdateRequestBodySpec`
        """
        self._spec = spec

    @property
    def endpoints(self):
        r"""Gets the endpoints of this JobUpdateRequestBody.

        :return: The endpoints of this JobUpdateRequestBody.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobEndpointsReq`
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this JobUpdateRequestBody.

        :param endpoints: The endpoints of this JobUpdateRequestBody.
        :type endpoints: :class:`huaweicloudsdkmodelarts.v1.JobEndpointsReq`
        """
        self._endpoints = endpoints

    @property
    def metadata(self):
        r"""Gets the metadata of this JobUpdateRequestBody.

        :return: The metadata of this JobUpdateRequestBody.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobUpdateRequestBodyMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this JobUpdateRequestBody.

        :param metadata: The metadata of this JobUpdateRequestBody.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.JobUpdateRequestBodyMetadata`
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
        if not isinstance(other, JobUpdateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
