# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistentVolumeClaim:

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
        'metadata': 'PersistentVolumeClaimMetadata',
        'spec': 'PersistentVolumeClaimSpec',
        'status': 'PersistentVolumeClaimStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None):
        """PersistentVolumeClaim

        The model defined in huaweicloud sdk

        :param api_version: API版本，固定值**v1**
        :type api_version: str
        :param kind: API类型，固定值**PersistentVolumeClaim**
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.PersistentVolumeClaimMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.PersistentVolumeClaimSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.PersistentVolumeClaimStatus`
        """
        
        

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        self.metadata = metadata
        self.spec = spec
        if status is not None:
            self.status = status

    @property
    def api_version(self):
        """Gets the api_version of this PersistentVolumeClaim.

        API版本，固定值**v1**

        :return: The api_version of this PersistentVolumeClaim.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this PersistentVolumeClaim.

        API版本，固定值**v1**

        :param api_version: The api_version of this PersistentVolumeClaim.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this PersistentVolumeClaim.

        API类型，固定值**PersistentVolumeClaim**

        :return: The kind of this PersistentVolumeClaim.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PersistentVolumeClaim.

        API类型，固定值**PersistentVolumeClaim**

        :param kind: The kind of this PersistentVolumeClaim.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this PersistentVolumeClaim.

        :return: The metadata of this PersistentVolumeClaim.
        :rtype: :class:`huaweicloudsdkcce.v3.PersistentVolumeClaimMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PersistentVolumeClaim.

        :param metadata: The metadata of this PersistentVolumeClaim.
        :type metadata: :class:`huaweicloudsdkcce.v3.PersistentVolumeClaimMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this PersistentVolumeClaim.

        :return: The spec of this PersistentVolumeClaim.
        :rtype: :class:`huaweicloudsdkcce.v3.PersistentVolumeClaimSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this PersistentVolumeClaim.

        :param spec: The spec of this PersistentVolumeClaim.
        :type spec: :class:`huaweicloudsdkcce.v3.PersistentVolumeClaimSpec`
        """
        self._spec = spec

    @property
    def status(self):
        """Gets the status of this PersistentVolumeClaim.

        :return: The status of this PersistentVolumeClaim.
        :rtype: :class:`huaweicloudsdkcce.v3.PersistentVolumeClaimStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PersistentVolumeClaim.

        :param status: The status of this PersistentVolumeClaim.
        :type status: :class:`huaweicloudsdkcce.v3.PersistentVolumeClaimStatus`
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
        if not isinstance(other, PersistentVolumeClaim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
