# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterMasterSnapshotTasksResponse(SdkResponse):

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
        'metadata': 'SnapshotTaskMetadata',
        'items': 'list[SnapshotTask]',
        'status': 'SnapshotTaskStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'items': 'items',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, items=None, status=None):
        r"""ListClusterMasterSnapshotTasksResponse

        The model defined in huaweicloud sdk

        :param api_version: api版本，默认为v3.1
        :type api_version: str
        :param kind: 任务类型
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.SnapshotTaskMetadata`
        :param items: 备份任务列表
        :type items: list[:class:`huaweicloudsdkcce.v3.SnapshotTask`]
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.SnapshotTaskStatus`
        """
        
        super(ListClusterMasterSnapshotTasksResponse, self).__init__()

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._items = None
        self._status = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if items is not None:
            self.items = items
        if status is not None:
            self.status = status

    @property
    def api_version(self):
        r"""Gets the api_version of this ListClusterMasterSnapshotTasksResponse.

        api版本，默认为v3.1

        :return: The api_version of this ListClusterMasterSnapshotTasksResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ListClusterMasterSnapshotTasksResponse.

        api版本，默认为v3.1

        :param api_version: The api_version of this ListClusterMasterSnapshotTasksResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this ListClusterMasterSnapshotTasksResponse.

        任务类型

        :return: The kind of this ListClusterMasterSnapshotTasksResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListClusterMasterSnapshotTasksResponse.

        任务类型

        :param kind: The kind of this ListClusterMasterSnapshotTasksResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this ListClusterMasterSnapshotTasksResponse.

        :return: The metadata of this ListClusterMasterSnapshotTasksResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.SnapshotTaskMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListClusterMasterSnapshotTasksResponse.

        :param metadata: The metadata of this ListClusterMasterSnapshotTasksResponse.
        :type metadata: :class:`huaweicloudsdkcce.v3.SnapshotTaskMetadata`
        """
        self._metadata = metadata

    @property
    def items(self):
        r"""Gets the items of this ListClusterMasterSnapshotTasksResponse.

        备份任务列表

        :return: The items of this ListClusterMasterSnapshotTasksResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.SnapshotTask`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListClusterMasterSnapshotTasksResponse.

        备份任务列表

        :param items: The items of this ListClusterMasterSnapshotTasksResponse.
        :type items: list[:class:`huaweicloudsdkcce.v3.SnapshotTask`]
        """
        self._items = items

    @property
    def status(self):
        r"""Gets the status of this ListClusterMasterSnapshotTasksResponse.

        :return: The status of this ListClusterMasterSnapshotTasksResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.SnapshotTaskStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListClusterMasterSnapshotTasksResponse.

        :param status: The status of this ListClusterMasterSnapshotTasksResponse.
        :type status: :class:`huaweicloudsdkcce.v3.SnapshotTaskStatus`
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
        if not isinstance(other, ListClusterMasterSnapshotTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
