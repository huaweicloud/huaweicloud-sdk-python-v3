# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddonCheckTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata': 'CheckTaskMetadata',
        'spec': 'CheckTaskSpec',
        'status': 'CheckTaskStatus'
    }

    attribute_map = {
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, metadata=None, spec=None, status=None):
        r"""AddonCheckTask

        The model defined in huaweicloud sdk

        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.CheckTaskMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.CheckTaskSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.CheckTaskStatus`
        """
        
        

        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        self.metadata = metadata
        if spec is not None:
            self.spec = spec
        self.status = status

    @property
    def metadata(self):
        r"""Gets the metadata of this AddonCheckTask.

        :return: The metadata of this AddonCheckTask.
        :rtype: :class:`huaweicloudsdkcce.v3.CheckTaskMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this AddonCheckTask.

        :param metadata: The metadata of this AddonCheckTask.
        :type metadata: :class:`huaweicloudsdkcce.v3.CheckTaskMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this AddonCheckTask.

        :return: The spec of this AddonCheckTask.
        :rtype: :class:`huaweicloudsdkcce.v3.CheckTaskSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this AddonCheckTask.

        :param spec: The spec of this AddonCheckTask.
        :type spec: :class:`huaweicloudsdkcce.v3.CheckTaskSpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this AddonCheckTask.

        :return: The status of this AddonCheckTask.
        :rtype: :class:`huaweicloudsdkcce.v3.CheckTaskStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AddonCheckTask.

        :param status: The status of this AddonCheckTask.
        :type status: :class:`huaweicloudsdkcce.v3.CheckTaskStatus`
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
        if not isinstance(other, AddonCheckTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
