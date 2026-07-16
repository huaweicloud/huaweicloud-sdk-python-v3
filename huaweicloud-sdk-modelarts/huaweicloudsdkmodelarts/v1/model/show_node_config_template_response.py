# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNodeConfigTemplateResponse(SdkResponse):

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
        'metadata': 'NodeConfigTemplateMeta',
        'spec': 'NodeConfigTemplateSpec'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None):
        r"""ShowNodeConfigTemplateResponse

        The model defined in huaweicloud sdk

        :param api_version: **参数解释**： API版本。 **取值范围**： 可选值如下： - v1
        :type api_version: str
        :param kind: **参数解释**： 资源类型。 **取值范围**： 可选值如下： - NodeConfigTemplate：节点配置模板
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.NodeConfigTemplateMeta`
        :param spec: 
        :type spec: :class:`huaweicloudsdkmodelarts.v1.NodeConfigTemplateSpec`
        """
        
        super().__init__()

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec

    @property
    def api_version(self):
        r"""Gets the api_version of this ShowNodeConfigTemplateResponse.

        **参数解释**： API版本。 **取值范围**： 可选值如下： - v1

        :return: The api_version of this ShowNodeConfigTemplateResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ShowNodeConfigTemplateResponse.

        **参数解释**： API版本。 **取值范围**： 可选值如下： - v1

        :param api_version: The api_version of this ShowNodeConfigTemplateResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this ShowNodeConfigTemplateResponse.

        **参数解释**： 资源类型。 **取值范围**： 可选值如下： - NodeConfigTemplate：节点配置模板

        :return: The kind of this ShowNodeConfigTemplateResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ShowNodeConfigTemplateResponse.

        **参数解释**： 资源类型。 **取值范围**： 可选值如下： - NodeConfigTemplate：节点配置模板

        :param kind: The kind of this ShowNodeConfigTemplateResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this ShowNodeConfigTemplateResponse.

        :return: The metadata of this ShowNodeConfigTemplateResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeConfigTemplateMeta`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ShowNodeConfigTemplateResponse.

        :param metadata: The metadata of this ShowNodeConfigTemplateResponse.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.NodeConfigTemplateMeta`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this ShowNodeConfigTemplateResponse.

        :return: The spec of this ShowNodeConfigTemplateResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeConfigTemplateSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ShowNodeConfigTemplateResponse.

        :param spec: The spec of this ShowNodeConfigTemplateResponse.
        :type spec: :class:`huaweicloudsdkmodelarts.v1.NodeConfigTemplateSpec`
        """
        self._spec = spec

    def to_dict(self):
        import warnings
        warnings.warn("ShowNodeConfigTemplateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowNodeConfigTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
