# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateComponentRequestBody:

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
        'kind': 'ComponentKindObj',
        'metadata': 'UpdateComponentRequestMetadata',
        'spec': 'UpdateComponentRequestSpec'
    }

    attribute_map = {
        'api_version': 'api_version',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None):
        """UpdateComponentRequestBody

        The model defined in huaweicloud sdk

        :param api_version: 
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        :param kind: 
        :type kind: :class:`huaweicloudsdkcae.v1.ComponentKindObj`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcae.v1.UpdateComponentRequestMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcae.v1.UpdateComponentRequestSpec`
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
        """Gets the api_version of this UpdateComponentRequestBody.

        :return: The api_version of this UpdateComponentRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this UpdateComponentRequestBody.

        :param api_version: The api_version of this UpdateComponentRequestBody.
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this UpdateComponentRequestBody.

        :return: The kind of this UpdateComponentRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.ComponentKindObj`
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this UpdateComponentRequestBody.

        :param kind: The kind of this UpdateComponentRequestBody.
        :type kind: :class:`huaweicloudsdkcae.v1.ComponentKindObj`
        """
        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this UpdateComponentRequestBody.

        :return: The metadata of this UpdateComponentRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateComponentRequestMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UpdateComponentRequestBody.

        :param metadata: The metadata of this UpdateComponentRequestBody.
        :type metadata: :class:`huaweicloudsdkcae.v1.UpdateComponentRequestMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this UpdateComponentRequestBody.

        :return: The spec of this UpdateComponentRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.UpdateComponentRequestSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this UpdateComponentRequestBody.

        :param spec: The spec of this UpdateComponentRequestBody.
        :type spec: :class:`huaweicloudsdkcae.v1.UpdateComponentRequestSpec`
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
        if not isinstance(other, UpdateComponentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
