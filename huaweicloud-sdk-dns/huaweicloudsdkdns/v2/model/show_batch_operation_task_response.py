# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBatchOperationTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'status': 'str',
        'created_at': 'str',
        'success_count': 'int',
        'error_count': 'int',
        'error_items': 'list[ShowBatchOperationTaskErrorItem]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'created_at': 'created_at',
        'success_count': 'success_count',
        'error_count': 'error_count',
        'error_items': 'error_items'
    }

    def __init__(self, id=None, type=None, status=None, created_at=None, success_count=None, error_count=None, error_items=None):
        r"""ShowBatchOperationTaskResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 批量操作任务的ID。 **取值范围：** 不涉及。
        :type id: str
        :param type: **参数解释：** 任务类型。 **取值范围：** - batch_create_zone：批量添加域名 - create：批量添加记录集 - import_recordset：批量导入记录集 - delete：批量删除记录集 - batch_update_rs：批量修改记录集 - transfer：批量转移域名
        :type type: str
        :param status: **参数解释：** 任务状态。 **取值范围：** - PENDING：执行中 - DONE：已完成
        :type status: str
        :param created_at: **参数解释：** 任务的创建时间。 格式：yyyy-MM-dd HH:mm:ss。 **取值范围：** 不涉及。
        :type created_at: str
        :param success_count: **参数解释：** 批量操作成功的数量。 **取值范围：** 不涉及。
        :type success_count: int
        :param error_count: **参数解释：** 批量操作失败的数量。 **取值范围：** 不涉及。
        :type error_count: int
        :param error_items: 批量操作任务列表。
        :type error_items: list[:class:`huaweicloudsdkdns.v2.ShowBatchOperationTaskErrorItem`]
        """
        
        super().__init__()

        self._id = None
        self._type = None
        self._status = None
        self._created_at = None
        self._success_count = None
        self._error_count = None
        self._error_items = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if success_count is not None:
            self.success_count = success_count
        if error_count is not None:
            self.error_count = error_count
        if error_items is not None:
            self.error_items = error_items

    @property
    def id(self):
        r"""Gets the id of this ShowBatchOperationTaskResponse.

        **参数解释：** 批量操作任务的ID。 **取值范围：** 不涉及。

        :return: The id of this ShowBatchOperationTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowBatchOperationTaskResponse.

        **参数解释：** 批量操作任务的ID。 **取值范围：** 不涉及。

        :param id: The id of this ShowBatchOperationTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ShowBatchOperationTaskResponse.

        **参数解释：** 任务类型。 **取值范围：** - batch_create_zone：批量添加域名 - create：批量添加记录集 - import_recordset：批量导入记录集 - delete：批量删除记录集 - batch_update_rs：批量修改记录集 - transfer：批量转移域名

        :return: The type of this ShowBatchOperationTaskResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowBatchOperationTaskResponse.

        **参数解释：** 任务类型。 **取值范围：** - batch_create_zone：批量添加域名 - create：批量添加记录集 - import_recordset：批量导入记录集 - delete：批量删除记录集 - batch_update_rs：批量修改记录集 - transfer：批量转移域名

        :param type: The type of this ShowBatchOperationTaskResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ShowBatchOperationTaskResponse.

        **参数解释：** 任务状态。 **取值范围：** - PENDING：执行中 - DONE：已完成

        :return: The status of this ShowBatchOperationTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowBatchOperationTaskResponse.

        **参数解释：** 任务状态。 **取值范围：** - PENDING：执行中 - DONE：已完成

        :param status: The status of this ShowBatchOperationTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowBatchOperationTaskResponse.

        **参数解释：** 任务的创建时间。 格式：yyyy-MM-dd HH:mm:ss。 **取值范围：** 不涉及。

        :return: The created_at of this ShowBatchOperationTaskResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowBatchOperationTaskResponse.

        **参数解释：** 任务的创建时间。 格式：yyyy-MM-dd HH:mm:ss。 **取值范围：** 不涉及。

        :param created_at: The created_at of this ShowBatchOperationTaskResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def success_count(self):
        r"""Gets the success_count of this ShowBatchOperationTaskResponse.

        **参数解释：** 批量操作成功的数量。 **取值范围：** 不涉及。

        :return: The success_count of this ShowBatchOperationTaskResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this ShowBatchOperationTaskResponse.

        **参数解释：** 批量操作成功的数量。 **取值范围：** 不涉及。

        :param success_count: The success_count of this ShowBatchOperationTaskResponse.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def error_count(self):
        r"""Gets the error_count of this ShowBatchOperationTaskResponse.

        **参数解释：** 批量操作失败的数量。 **取值范围：** 不涉及。

        :return: The error_count of this ShowBatchOperationTaskResponse.
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        r"""Sets the error_count of this ShowBatchOperationTaskResponse.

        **参数解释：** 批量操作失败的数量。 **取值范围：** 不涉及。

        :param error_count: The error_count of this ShowBatchOperationTaskResponse.
        :type error_count: int
        """
        self._error_count = error_count

    @property
    def error_items(self):
        r"""Gets the error_items of this ShowBatchOperationTaskResponse.

        批量操作任务列表。

        :return: The error_items of this ShowBatchOperationTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.ShowBatchOperationTaskErrorItem`]
        """
        return self._error_items

    @error_items.setter
    def error_items(self, error_items):
        r"""Sets the error_items of this ShowBatchOperationTaskResponse.

        批量操作任务列表。

        :param error_items: The error_items of this ShowBatchOperationTaskResponse.
        :type error_items: list[:class:`huaweicloudsdkdns.v2.ShowBatchOperationTaskErrorItem`]
        """
        self._error_items = error_items

    def to_dict(self):
        import warnings
        warnings.warn("ShowBatchOperationTaskResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowBatchOperationTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
