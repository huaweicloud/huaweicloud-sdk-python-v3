# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEnvironmentResponse(SdkResponse):

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
        'metadata': 'EnvironmentMetadata'
    }

    attribute_map = {
        'api_version': 'api_version',
        'kind': 'kind',
        'metadata': 'metadata'
    }

    def __init__(self, api_version=None, kind=None, metadata=None):
        """CreateEnvironmentResponse

        The model defined in huaweicloud sdk

        :param api_version: API版本。
        :type api_version: str
        :param kind: 资源种类
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcae.v1.EnvironmentMetadata`
        """
        
        super(CreateEnvironmentResponse, self).__init__()

        self._api_version = None
        self._kind = None
        self._metadata = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata

    @property
    def api_version(self):
        """Gets the api_version of this CreateEnvironmentResponse.

        API版本。

        :return: The api_version of this CreateEnvironmentResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this CreateEnvironmentResponse.

        API版本。

        :param api_version: The api_version of this CreateEnvironmentResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this CreateEnvironmentResponse.

        资源种类

        :return: The kind of this CreateEnvironmentResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this CreateEnvironmentResponse.

        资源种类

        :param kind: The kind of this CreateEnvironmentResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this CreateEnvironmentResponse.


        :return: The metadata of this CreateEnvironmentResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.EnvironmentMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateEnvironmentResponse.


        :param metadata: The metadata of this CreateEnvironmentResponse.
        :type metadata: :class:`huaweicloudsdkcae.v1.EnvironmentMetadata`
        """
        self._metadata = metadata

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
        if not isinstance(other, CreateEnvironmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
