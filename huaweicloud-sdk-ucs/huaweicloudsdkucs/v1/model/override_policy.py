# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OverridePolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'spec': 'OverrideSpec'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'spec': 'spec'
    }

    def __init__(self, kind=None, api_version=None, spec=None):
        r"""OverridePolicy

        The model defined in huaweicloud sdk

        :param kind: API类型，固定值“OverridePolicy”
        :type kind: str
        :param api_version: API版本
        :type api_version: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkucs.v1.OverrideSpec`
        """
        
        

        self._kind = None
        self._api_version = None
        self._spec = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if spec is not None:
            self.spec = spec

    @property
    def kind(self):
        r"""Gets the kind of this OverridePolicy.

        API类型，固定值“OverridePolicy”

        :return: The kind of this OverridePolicy.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this OverridePolicy.

        API类型，固定值“OverridePolicy”

        :param kind: The kind of this OverridePolicy.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this OverridePolicy.

        API版本

        :return: The api_version of this OverridePolicy.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this OverridePolicy.

        API版本

        :param api_version: The api_version of this OverridePolicy.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def spec(self):
        r"""Gets the spec of this OverridePolicy.

        :return: The spec of this OverridePolicy.
        :rtype: :class:`huaweicloudsdkucs.v1.OverrideSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this OverridePolicy.

        :param spec: The spec of this OverridePolicy.
        :type spec: :class:`huaweicloudsdkucs.v1.OverrideSpec`
        """
        self._spec = spec

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
        if not isinstance(other, OverridePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
