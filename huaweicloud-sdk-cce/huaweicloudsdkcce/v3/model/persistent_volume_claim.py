# coding: utf-8

import pprint
import re

import six





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

    def __init__(self, api_version='v1', kind='PersistentVolumeClaim', metadata=None, spec=None, status=None):
        """PersistentVolumeClaim - a model defined in huaweicloud sdk"""
        
        

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
        :type: str
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
        :type: str
        """
        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this PersistentVolumeClaim.


        :return: The metadata of this PersistentVolumeClaim.
        :rtype: PersistentVolumeClaimMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PersistentVolumeClaim.


        :param metadata: The metadata of this PersistentVolumeClaim.
        :type: PersistentVolumeClaimMetadata
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this PersistentVolumeClaim.


        :return: The spec of this PersistentVolumeClaim.
        :rtype: PersistentVolumeClaimSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this PersistentVolumeClaim.


        :param spec: The spec of this PersistentVolumeClaim.
        :type: PersistentVolumeClaimSpec
        """
        self._spec = spec

    @property
    def status(self):
        """Gets the status of this PersistentVolumeClaim.


        :return: The status of this PersistentVolumeClaim.
        :rtype: PersistentVolumeClaimStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PersistentVolumeClaim.


        :param status: The status of this PersistentVolumeClaim.
        :type: PersistentVolumeClaimStatus
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PersistentVolumeClaim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
