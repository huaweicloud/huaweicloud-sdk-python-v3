# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAutopilotClusterMasterSnapshotResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uid': 'str',
        'metadata': 'SnapshotCluserResponseMetadata'
    }

    attribute_map = {
        'uid': 'uid',
        'metadata': 'metadata'
    }

    def __init__(self, uid=None, metadata=None):
        r"""CreateAutopilotClusterMasterSnapshotResponse

        The model defined in huaweicloud sdk

        :param uid: 任务ID
        :type uid: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.SnapshotCluserResponseMetadata`
        """
        
        super(CreateAutopilotClusterMasterSnapshotResponse, self).__init__()

        self._uid = None
        self._metadata = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if metadata is not None:
            self.metadata = metadata

    @property
    def uid(self):
        r"""Gets the uid of this CreateAutopilotClusterMasterSnapshotResponse.

        任务ID

        :return: The uid of this CreateAutopilotClusterMasterSnapshotResponse.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this CreateAutopilotClusterMasterSnapshotResponse.

        任务ID

        :param uid: The uid of this CreateAutopilotClusterMasterSnapshotResponse.
        :type uid: str
        """
        self._uid = uid

    @property
    def metadata(self):
        r"""Gets the metadata of this CreateAutopilotClusterMasterSnapshotResponse.

        :return: The metadata of this CreateAutopilotClusterMasterSnapshotResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.SnapshotCluserResponseMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this CreateAutopilotClusterMasterSnapshotResponse.

        :param metadata: The metadata of this CreateAutopilotClusterMasterSnapshotResponse.
        :type metadata: :class:`huaweicloudsdkcce.v3.SnapshotCluserResponseMetadata`
        """
        self._metadata = metadata

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
        if not isinstance(other, CreateAutopilotClusterMasterSnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
