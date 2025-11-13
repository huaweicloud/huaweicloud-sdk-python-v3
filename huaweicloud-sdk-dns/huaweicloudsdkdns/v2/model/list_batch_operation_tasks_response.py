# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBatchOperationTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks': 'list[ListBatchOperationTasksItem]',
        'metadata': 'Metadata'
    }

    attribute_map = {
        'tasks': 'tasks',
        'metadata': 'metadata'
    }

    def __init__(self, tasks=None, metadata=None):
        r"""ListBatchOperationTasksResponse

        The model defined in huaweicloud sdk

        :param tasks: 批量操作任务列表。
        :type tasks: list[:class:`huaweicloudsdkdns.v2.ListBatchOperationTasksItem`]
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        
        super().__init__()

        self._tasks = None
        self._metadata = None
        self.discriminator = None

        if tasks is not None:
            self.tasks = tasks
        if metadata is not None:
            self.metadata = metadata

    @property
    def tasks(self):
        r"""Gets the tasks of this ListBatchOperationTasksResponse.

        批量操作任务列表。

        :return: The tasks of this ListBatchOperationTasksResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.ListBatchOperationTasksItem`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListBatchOperationTasksResponse.

        批量操作任务列表。

        :param tasks: The tasks of this ListBatchOperationTasksResponse.
        :type tasks: list[:class:`huaweicloudsdkdns.v2.ListBatchOperationTasksItem`]
        """
        self._tasks = tasks

    @property
    def metadata(self):
        r"""Gets the metadata of this ListBatchOperationTasksResponse.

        :return: The metadata of this ListBatchOperationTasksResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListBatchOperationTasksResponse.

        :param metadata: The metadata of this ListBatchOperationTasksResponse.
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        self._metadata = metadata

    def to_dict(self):
        import warnings
        warnings.warn("ListBatchOperationTasksResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListBatchOperationTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
