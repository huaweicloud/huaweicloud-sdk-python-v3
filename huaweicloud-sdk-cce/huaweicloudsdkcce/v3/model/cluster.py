# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Cluster:

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
        'metadata': 'ClusterMetadata',
        'spec': 'ClusterSpec',
        'status': 'ClusterStatus'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, spec=None, status=None):
        r"""Cluster

        The model defined in huaweicloud sdk

        :param kind: API类型，固定值“Cluster”或“cluster”，该值不可修改。  
        :type kind: str
        :param api_version: API版本，固定值“v3”，该值不可修改。  
        :type api_version: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.ClusterMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.ClusterSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.ClusterStatus`
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
        self.spec = spec
        if status is not None:
            self.status = status

    @property
    def kind(self):
        r"""Gets the kind of this Cluster.

        API类型，固定值“Cluster”或“cluster”，该值不可修改。  

        :return: The kind of this Cluster.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this Cluster.

        API类型，固定值“Cluster”或“cluster”，该值不可修改。  

        :param kind: The kind of this Cluster.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this Cluster.

        API版本，固定值“v3”，该值不可修改。  

        :return: The api_version of this Cluster.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this Cluster.

        API版本，固定值“v3”，该值不可修改。  

        :param api_version: The api_version of this Cluster.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        r"""Gets the metadata of this Cluster.

        :return: The metadata of this Cluster.
        :rtype: :class:`huaweicloudsdkcce.v3.ClusterMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this Cluster.

        :param metadata: The metadata of this Cluster.
        :type metadata: :class:`huaweicloudsdkcce.v3.ClusterMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this Cluster.

        :return: The spec of this Cluster.
        :rtype: :class:`huaweicloudsdkcce.v3.ClusterSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this Cluster.

        :param spec: The spec of this Cluster.
        :type spec: :class:`huaweicloudsdkcce.v3.ClusterSpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this Cluster.

        :return: The status of this Cluster.
        :rtype: :class:`huaweicloudsdkcce.v3.ClusterStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Cluster.

        :param status: The status of this Cluster.
        :type status: :class:`huaweicloudsdkcce.v3.ClusterStatus`
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
        if not isinstance(other, Cluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
