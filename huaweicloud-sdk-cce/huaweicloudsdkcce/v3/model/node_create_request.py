# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeCreateRequest:

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
        'metadata': 'NodeMetadata',
        'spec': 'NodeSpec'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, spec=None):
        r"""NodeCreateRequest

        The model defined in huaweicloud sdk

        :param kind: API类型，固定值“Node”，该值不可修改。  
        :type kind: str
        :param api_version: API版本，固定值“v3”，该值不可修改。  
        :type api_version: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.NodeMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.NodeSpec`
        """
        
        

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._spec = None
        self.discriminator = None

        self.kind = kind
        self.api_version = api_version
        if metadata is not None:
            self.metadata = metadata
        self.spec = spec

    @property
    def kind(self):
        r"""Gets the kind of this NodeCreateRequest.

        API类型，固定值“Node”，该值不可修改。  

        :return: The kind of this NodeCreateRequest.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this NodeCreateRequest.

        API类型，固定值“Node”，该值不可修改。  

        :param kind: The kind of this NodeCreateRequest.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this NodeCreateRequest.

        API版本，固定值“v3”，该值不可修改。  

        :return: The api_version of this NodeCreateRequest.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this NodeCreateRequest.

        API版本，固定值“v3”，该值不可修改。  

        :param api_version: The api_version of this NodeCreateRequest.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        r"""Gets the metadata of this NodeCreateRequest.

        :return: The metadata of this NodeCreateRequest.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this NodeCreateRequest.

        :param metadata: The metadata of this NodeCreateRequest.
        :type metadata: :class:`huaweicloudsdkcce.v3.NodeMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this NodeCreateRequest.

        :return: The spec of this NodeCreateRequest.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this NodeCreateRequest.

        :param spec: The spec of this NodeCreateRequest.
        :type spec: :class:`huaweicloudsdkcce.v3.NodeSpec`
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
        if not isinstance(other, NodeCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
