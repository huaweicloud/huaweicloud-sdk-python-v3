# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterCluster:

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
        'metadata': 'RegisterClusterMetadata',
        'spec': 'RegisterClusterSpec'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, spec=None):
        r"""RegisterCluster

        The model defined in huaweicloud sdk

        :param kind: 资源类型。注册集群必须填写为Cluster。
        :type kind: str
        :param api_version: API版本信息。现版本仅为v1。
        :type api_version: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkucs.v1.RegisterClusterMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkucs.v1.RegisterClusterSpec`
        """
        
        

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._spec = None
        self.discriminator = None

        self.kind = kind
        self.api_version = api_version
        self.metadata = metadata
        self.spec = spec

    @property
    def kind(self):
        r"""Gets the kind of this RegisterCluster.

        资源类型。注册集群必须填写为Cluster。

        :return: The kind of this RegisterCluster.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this RegisterCluster.

        资源类型。注册集群必须填写为Cluster。

        :param kind: The kind of this RegisterCluster.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this RegisterCluster.

        API版本信息。现版本仅为v1。

        :return: The api_version of this RegisterCluster.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this RegisterCluster.

        API版本信息。现版本仅为v1。

        :param api_version: The api_version of this RegisterCluster.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        r"""Gets the metadata of this RegisterCluster.

        :return: The metadata of this RegisterCluster.
        :rtype: :class:`huaweicloudsdkucs.v1.RegisterClusterMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this RegisterCluster.

        :param metadata: The metadata of this RegisterCluster.
        :type metadata: :class:`huaweicloudsdkucs.v1.RegisterClusterMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this RegisterCluster.

        :return: The spec of this RegisterCluster.
        :rtype: :class:`huaweicloudsdkucs.v1.RegisterClusterSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this RegisterCluster.

        :param spec: The spec of this RegisterCluster.
        :type spec: :class:`huaweicloudsdkucs.v1.RegisterClusterSpec`
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
        if not isinstance(other, RegisterCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
