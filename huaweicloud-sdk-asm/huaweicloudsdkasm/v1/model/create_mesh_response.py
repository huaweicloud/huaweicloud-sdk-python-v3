# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMeshResponse(SdkResponse):

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
        'metadata': 'MeshMetadata',
        'spec': 'MeshSpec',
        'status': 'MeshStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None):
        r"""CreateMeshResponse

        The model defined in huaweicloud sdk

        :param api_version: API版本，固定值“v1”，该值不可修改
        :type api_version: str
        :param kind: API类型，固定值“Mesh”或“mesh”，该值不可修改
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkasm.v1.MeshMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkasm.v1.MeshSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkasm.v1.MeshStatus`
        """
        
        super(CreateMeshResponse, self).__init__()

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def api_version(self):
        r"""Gets the api_version of this CreateMeshResponse.

        API版本，固定值“v1”，该值不可修改

        :return: The api_version of this CreateMeshResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this CreateMeshResponse.

        API版本，固定值“v1”，该值不可修改

        :param api_version: The api_version of this CreateMeshResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this CreateMeshResponse.

        API类型，固定值“Mesh”或“mesh”，该值不可修改

        :return: The kind of this CreateMeshResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this CreateMeshResponse.

        API类型，固定值“Mesh”或“mesh”，该值不可修改

        :param kind: The kind of this CreateMeshResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this CreateMeshResponse.

        :return: The metadata of this CreateMeshResponse.
        :rtype: :class:`huaweicloudsdkasm.v1.MeshMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this CreateMeshResponse.

        :param metadata: The metadata of this CreateMeshResponse.
        :type metadata: :class:`huaweicloudsdkasm.v1.MeshMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this CreateMeshResponse.

        :return: The spec of this CreateMeshResponse.
        :rtype: :class:`huaweicloudsdkasm.v1.MeshSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this CreateMeshResponse.

        :param spec: The spec of this CreateMeshResponse.
        :type spec: :class:`huaweicloudsdkasm.v1.MeshSpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this CreateMeshResponse.

        :return: The status of this CreateMeshResponse.
        :rtype: :class:`huaweicloudsdkasm.v1.MeshStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateMeshResponse.

        :param status: The status of this CreateMeshResponse.
        :type status: :class:`huaweicloudsdkasm.v1.MeshStatus`
        """
        self._status = status

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
        if not isinstance(other, CreateMeshResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
