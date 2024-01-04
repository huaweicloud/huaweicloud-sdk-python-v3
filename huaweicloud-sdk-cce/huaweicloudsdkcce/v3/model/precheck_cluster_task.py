# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrecheckClusterTask:

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
        'metadata': 'PrecheckTaskMetadata',
        'spec': 'PrecheckSpec',
        'status': 'PrecheckStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None):
        """PrecheckClusterTask

        The model defined in huaweicloud sdk

        :param api_version: api版本，默认为v3
        :type api_version: str
        :param kind: 资源类型，默认为PreCheckTask
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.PrecheckTaskMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.PrecheckSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.PrecheckStatus`
        """
        
        

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
        """Gets the api_version of this PrecheckClusterTask.

        api版本，默认为v3

        :return: The api_version of this PrecheckClusterTask.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this PrecheckClusterTask.

        api版本，默认为v3

        :param api_version: The api_version of this PrecheckClusterTask.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this PrecheckClusterTask.

        资源类型，默认为PreCheckTask

        :return: The kind of this PrecheckClusterTask.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PrecheckClusterTask.

        资源类型，默认为PreCheckTask

        :param kind: The kind of this PrecheckClusterTask.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this PrecheckClusterTask.

        :return: The metadata of this PrecheckClusterTask.
        :rtype: :class:`huaweicloudsdkcce.v3.PrecheckTaskMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PrecheckClusterTask.

        :param metadata: The metadata of this PrecheckClusterTask.
        :type metadata: :class:`huaweicloudsdkcce.v3.PrecheckTaskMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this PrecheckClusterTask.

        :return: The spec of this PrecheckClusterTask.
        :rtype: :class:`huaweicloudsdkcce.v3.PrecheckSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this PrecheckClusterTask.

        :param spec: The spec of this PrecheckClusterTask.
        :type spec: :class:`huaweicloudsdkcce.v3.PrecheckSpec`
        """
        self._spec = spec

    @property
    def status(self):
        """Gets the status of this PrecheckClusterTask.

        :return: The status of this PrecheckClusterTask.
        :rtype: :class:`huaweicloudsdkcce.v3.PrecheckStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PrecheckClusterTask.

        :param status: The status of this PrecheckClusterTask.
        :type status: :class:`huaweicloudsdkcce.v3.PrecheckStatus`
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
        if not isinstance(other, PrecheckClusterTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
