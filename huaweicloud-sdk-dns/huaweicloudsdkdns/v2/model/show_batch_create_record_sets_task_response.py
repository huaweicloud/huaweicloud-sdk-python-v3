# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBatchCreateRecordSetsTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'total_count': 'int',
        'success_count': 'int',
        'error_count': 'int',
        'error_items': 'list[ShowBatchCreateRecordSetsTaskErrorItem]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'total_count': 'total_count',
        'success_count': 'success_count',
        'error_count': 'error_count',
        'error_items': 'error_items'
    }

    def __init__(self, task_id=None, status=None, created_at=None, updated_at=None, total_count=None, success_count=None, error_count=None, error_items=None):
        r"""ShowBatchCreateRecordSetsTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 批量创建记录集任务的ID。 **取值范围：** 不涉及。
        :type task_id: str
        :param status: **参数解释：** 任务状态。 **取值范围：** - PENDING：处理中 - DONE：已完成
        :type status: str
        :param created_at: **参数解释：** 任务的创建时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。 **取值范围：** 不涉及。
        :type created_at: str
        :param updated_at: **参数解释：** 任务的更新时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。 **取值范围：** 不涉及。
        :type updated_at: str
        :param total_count: **参数解释：** 批量创建记录集的总数。 **取值范围：** 不涉及。
        :type total_count: int
        :param success_count: **参数解释：** 记录集创建成功的数量。 **取值范围：** 不涉及。
        :type success_count: int
        :param error_count: **参数解释：** 记录集创建失败的数量。 **取值范围：** 不涉及。
        :type error_count: int
        :param error_items: **参数解释：** 记录集创建失败的条目。 **取值范围：** 不涉及。
        :type error_items: list[:class:`huaweicloudsdkdns.v2.ShowBatchCreateRecordSetsTaskErrorItem`]
        """
        
        super().__init__()

        self._task_id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._total_count = None
        self._success_count = None
        self._error_count = None
        self._error_items = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if total_count is not None:
            self.total_count = total_count
        if success_count is not None:
            self.success_count = success_count
        if error_count is not None:
            self.error_count = error_count
        if error_items is not None:
            self.error_items = error_items

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 批量创建记录集任务的ID。 **取值范围：** 不涉及。

        :return: The task_id of this ShowBatchCreateRecordSetsTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 批量创建记录集任务的ID。 **取值范围：** 不涉及。

        :param task_id: The task_id of this ShowBatchCreateRecordSetsTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 任务状态。 **取值范围：** - PENDING：处理中 - DONE：已完成

        :return: The status of this ShowBatchCreateRecordSetsTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 任务状态。 **取值范围：** - PENDING：处理中 - DONE：已完成

        :param status: The status of this ShowBatchCreateRecordSetsTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 任务的创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :return: The created_at of this ShowBatchCreateRecordSetsTaskResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 任务的创建时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :param created_at: The created_at of this ShowBatchCreateRecordSetsTaskResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 任务的更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :return: The updated_at of this ShowBatchCreateRecordSetsTaskResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 任务的更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。 **取值范围：** 不涉及。

        :param updated_at: The updated_at of this ShowBatchCreateRecordSetsTaskResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 批量创建记录集的总数。 **取值范围：** 不涉及。

        :return: The total_count of this ShowBatchCreateRecordSetsTaskResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 批量创建记录集的总数。 **取值范围：** 不涉及。

        :param total_count: The total_count of this ShowBatchCreateRecordSetsTaskResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def success_count(self):
        r"""Gets the success_count of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 记录集创建成功的数量。 **取值范围：** 不涉及。

        :return: The success_count of this ShowBatchCreateRecordSetsTaskResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 记录集创建成功的数量。 **取值范围：** 不涉及。

        :param success_count: The success_count of this ShowBatchCreateRecordSetsTaskResponse.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def error_count(self):
        r"""Gets the error_count of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 记录集创建失败的数量。 **取值范围：** 不涉及。

        :return: The error_count of this ShowBatchCreateRecordSetsTaskResponse.
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        r"""Sets the error_count of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 记录集创建失败的数量。 **取值范围：** 不涉及。

        :param error_count: The error_count of this ShowBatchCreateRecordSetsTaskResponse.
        :type error_count: int
        """
        self._error_count = error_count

    @property
    def error_items(self):
        r"""Gets the error_items of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 记录集创建失败的条目。 **取值范围：** 不涉及。

        :return: The error_items of this ShowBatchCreateRecordSetsTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.ShowBatchCreateRecordSetsTaskErrorItem`]
        """
        return self._error_items

    @error_items.setter
    def error_items(self, error_items):
        r"""Sets the error_items of this ShowBatchCreateRecordSetsTaskResponse.

        **参数解释：** 记录集创建失败的条目。 **取值范围：** 不涉及。

        :param error_items: The error_items of this ShowBatchCreateRecordSetsTaskResponse.
        :type error_items: list[:class:`huaweicloudsdkdns.v2.ShowBatchCreateRecordSetsTaskErrorItem`]
        """
        self._error_items = error_items

    def to_dict(self):
        import warnings
        warnings.warn("ShowBatchCreateRecordSetsTaskResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowBatchCreateRecordSetsTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
