# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteActionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'ApiVersionObj',
        'kind': 'ActionKindObj',
        'metadata': 'ExecuteActionRequestBodyMetadata',
        'spec': 'ActionOnComponentSpec'
    }

    attribute_map = {
        'api_version': 'api_version',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None):
        """ExecuteActionRequestBody

        The model defined in huaweicloud sdk

        :param api_version: 
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        :param kind: 
        :type kind: :class:`huaweicloudsdkcae.v1.ActionKindObj`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcae.v1.ExecuteActionRequestBodyMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcae.v1.ActionOnComponentSpec`
        """
        
        

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec

    @property
    def api_version(self):
        """Gets the api_version of this ExecuteActionRequestBody.

        :return: The api_version of this ExecuteActionRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ExecuteActionRequestBody.

        :param api_version: The api_version of this ExecuteActionRequestBody.
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this ExecuteActionRequestBody.

        :return: The kind of this ExecuteActionRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.ActionKindObj`
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ExecuteActionRequestBody.

        :param kind: The kind of this ExecuteActionRequestBody.
        :type kind: :class:`huaweicloudsdkcae.v1.ActionKindObj`
        """
        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this ExecuteActionRequestBody.

        :return: The metadata of this ExecuteActionRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.ExecuteActionRequestBodyMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ExecuteActionRequestBody.

        :param metadata: The metadata of this ExecuteActionRequestBody.
        :type metadata: :class:`huaweicloudsdkcae.v1.ExecuteActionRequestBodyMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this ExecuteActionRequestBody.

        :return: The spec of this ExecuteActionRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.ActionOnComponentSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ExecuteActionRequestBody.

        :param spec: The spec of this ExecuteActionRequestBody.
        :type spec: :class:`huaweicloudsdkcae.v1.ActionOnComponentSpec`
        """
        self._spec = spec

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExecuteActionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
