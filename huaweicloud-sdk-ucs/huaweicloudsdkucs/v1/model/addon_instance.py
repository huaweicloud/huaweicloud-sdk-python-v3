# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddonInstance:

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
        'metadata': 'ObjectMeta',
        'spec': 'AddonInstanceSpec',
        'status': 'AddonInstanceStatus'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, spec=None, status=None):
        r"""AddonInstance

        The model defined in huaweicloud sdk

        :param kind: API类型，必须是\&quot;Addon\&quot;
        :type kind: str
        :param api_version: API版本，必须是\&quot;v3\&quot;
        :type api_version: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkucs.v1.ObjectMeta`
        :param spec: 
        :type spec: :class:`huaweicloudsdkucs.v1.AddonInstanceSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkucs.v1.AddonInstanceStatus`
        """
        
        

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        self.kind = kind
        self.api_version = api_version
        self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def kind(self):
        r"""Gets the kind of this AddonInstance.

        API类型，必须是\"Addon\"

        :return: The kind of this AddonInstance.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this AddonInstance.

        API类型，必须是\"Addon\"

        :param kind: The kind of this AddonInstance.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this AddonInstance.

        API版本，必须是\"v3\"

        :return: The api_version of this AddonInstance.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this AddonInstance.

        API版本，必须是\"v3\"

        :param api_version: The api_version of this AddonInstance.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        r"""Gets the metadata of this AddonInstance.

        :return: The metadata of this AddonInstance.
        :rtype: :class:`huaweicloudsdkucs.v1.ObjectMeta`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this AddonInstance.

        :param metadata: The metadata of this AddonInstance.
        :type metadata: :class:`huaweicloudsdkucs.v1.ObjectMeta`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this AddonInstance.

        :return: The spec of this AddonInstance.
        :rtype: :class:`huaweicloudsdkucs.v1.AddonInstanceSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this AddonInstance.

        :param spec: The spec of this AddonInstance.
        :type spec: :class:`huaweicloudsdkucs.v1.AddonInstanceSpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this AddonInstance.

        :return: The status of this AddonInstance.
        :rtype: :class:`huaweicloudsdkucs.v1.AddonInstanceStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AddonInstance.

        :param status: The status of this AddonInstance.
        :type status: :class:`huaweicloudsdkucs.v1.AddonInstanceStatus`
        """
        self._status = status

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
        if not isinstance(other, AddonInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
