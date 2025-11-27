# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConfigSetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'namespace': 'str',
        'helm_release_spec': 'object',
        'kustomization_spec': 'KustomizationSpec'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'helm_release_spec': 'helmReleaseSpec',
        'kustomization_spec': 'kustomizationSpec'
    }

    def __init__(self, name=None, namespace=None, helm_release_spec=None, kustomization_spec=None):
        r"""UpdateConfigSetRequestBody

        The model defined in huaweicloud sdk

        :param name: 配置集合的名称
        :type name: str
        :param namespace: 所在命名空间
        :type namespace: str
        :param helm_release_spec: 基于Helm Chart的部署配置（当前不支持HelmRelease类型）
        :type helm_release_spec: object
        :param kustomization_spec: 
        :type kustomization_spec: :class:`huaweicloudsdkucs.v1.KustomizationSpec`
        """
        
        

        self._name = None
        self._namespace = None
        self._helm_release_spec = None
        self._kustomization_spec = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if helm_release_spec is not None:
            self.helm_release_spec = helm_release_spec
        if kustomization_spec is not None:
            self.kustomization_spec = kustomization_spec

    @property
    def name(self):
        r"""Gets the name of this UpdateConfigSetRequestBody.

        配置集合的名称

        :return: The name of this UpdateConfigSetRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateConfigSetRequestBody.

        配置集合的名称

        :param name: The name of this UpdateConfigSetRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this UpdateConfigSetRequestBody.

        所在命名空间

        :return: The namespace of this UpdateConfigSetRequestBody.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this UpdateConfigSetRequestBody.

        所在命名空间

        :param namespace: The namespace of this UpdateConfigSetRequestBody.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def helm_release_spec(self):
        r"""Gets the helm_release_spec of this UpdateConfigSetRequestBody.

        基于Helm Chart的部署配置（当前不支持HelmRelease类型）

        :return: The helm_release_spec of this UpdateConfigSetRequestBody.
        :rtype: object
        """
        return self._helm_release_spec

    @helm_release_spec.setter
    def helm_release_spec(self, helm_release_spec):
        r"""Sets the helm_release_spec of this UpdateConfigSetRequestBody.

        基于Helm Chart的部署配置（当前不支持HelmRelease类型）

        :param helm_release_spec: The helm_release_spec of this UpdateConfigSetRequestBody.
        :type helm_release_spec: object
        """
        self._helm_release_spec = helm_release_spec

    @property
    def kustomization_spec(self):
        r"""Gets the kustomization_spec of this UpdateConfigSetRequestBody.

        :return: The kustomization_spec of this UpdateConfigSetRequestBody.
        :rtype: :class:`huaweicloudsdkucs.v1.KustomizationSpec`
        """
        return self._kustomization_spec

    @kustomization_spec.setter
    def kustomization_spec(self, kustomization_spec):
        r"""Sets the kustomization_spec of this UpdateConfigSetRequestBody.

        :param kustomization_spec: The kustomization_spec of this UpdateConfigSetRequestBody.
        :type kustomization_spec: :class:`huaweicloudsdkucs.v1.KustomizationSpec`
        """
        self._kustomization_spec = kustomization_spec

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
        if not isinstance(other, UpdateConfigSetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
