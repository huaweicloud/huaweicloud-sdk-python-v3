# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PatchNodePoolResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata': 'PatchNodePoolMetaVO',
        'spec': 'NodePoolSpec'
    }

    attribute_map = {
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, metadata=None, spec=None):
        r"""PatchNodePoolResponse

        The model defined in huaweicloud sdk

        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.PatchNodePoolMetaVO`
        :param spec: 
        :type spec: :class:`huaweicloudsdkmodelarts.v1.NodePoolSpec`
        """
        
        super().__init__()

        self._metadata = None
        self._spec = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec

    @property
    def metadata(self):
        r"""Gets the metadata of this PatchNodePoolResponse.

        :return: The metadata of this PatchNodePoolResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PatchNodePoolMetaVO`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this PatchNodePoolResponse.

        :param metadata: The metadata of this PatchNodePoolResponse.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.PatchNodePoolMetaVO`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this PatchNodePoolResponse.

        :return: The spec of this PatchNodePoolResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodePoolSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this PatchNodePoolResponse.

        :param spec: The spec of this PatchNodePoolResponse.
        :type spec: :class:`huaweicloudsdkmodelarts.v1.NodePoolSpec`
        """
        self._spec = spec

    def to_dict(self):
        import warnings
        warnings.warn("PatchNodePoolResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, PatchNodePoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
