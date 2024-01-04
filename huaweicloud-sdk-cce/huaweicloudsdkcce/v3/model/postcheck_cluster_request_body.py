# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostcheckClusterRequestBody:

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
        'spec': 'PostcheckSpec'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'spec': 'spec'
    }

    def __init__(self, api_version=None, kind=None, spec=None):
        """PostcheckClusterRequestBody

        The model defined in huaweicloud sdk

        :param api_version: API版本，默认为v3
        :type api_version: str
        :param kind: 资源类型
        :type kind: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.PostcheckSpec`
        """
        
        

        self._api_version = None
        self._kind = None
        self._spec = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        self.spec = spec

    @property
    def api_version(self):
        """Gets the api_version of this PostcheckClusterRequestBody.

        API版本，默认为v3

        :return: The api_version of this PostcheckClusterRequestBody.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this PostcheckClusterRequestBody.

        API版本，默认为v3

        :param api_version: The api_version of this PostcheckClusterRequestBody.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this PostcheckClusterRequestBody.

        资源类型

        :return: The kind of this PostcheckClusterRequestBody.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PostcheckClusterRequestBody.

        资源类型

        :param kind: The kind of this PostcheckClusterRequestBody.
        :type kind: str
        """
        self._kind = kind

    @property
    def spec(self):
        """Gets the spec of this PostcheckClusterRequestBody.

        :return: The spec of this PostcheckClusterRequestBody.
        :rtype: :class:`huaweicloudsdkcce.v3.PostcheckSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this PostcheckClusterRequestBody.

        :param spec: The spec of this PostcheckClusterRequestBody.
        :type spec: :class:`huaweicloudsdkcce.v3.PostcheckSpec`
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
        if not isinstance(other, PostcheckClusterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
