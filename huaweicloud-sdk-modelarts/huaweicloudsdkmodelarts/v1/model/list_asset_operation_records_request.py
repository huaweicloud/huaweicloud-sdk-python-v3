# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetOperationRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort_dir': 'str',
        'sort_key': 'str',
        'record_id': 'str',
        'job_type': 'str',
        'job_id': 'str',
        'job_name': 'str',
        'job_status': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'asset_id': 'str',
        'asset_code': 'str',
        'is_deleted': 'bool'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'limit': 'limit',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'record_id': 'record_id',
        'job_type': 'job_type',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'job_status': 'job_status',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'asset_id': 'asset_id',
        'asset_code': 'asset_code',
        'is_deleted': 'is_deleted'
    }

    def __init__(self, workspace_id=None, limit=None, offset=None, sort_dir=None, sort_key=None, record_id=None, job_type=None, job_id=None, job_name=None, job_status=None, user_id=None, user_name=None, asset_id=None, asset_code=None, is_deleted=None):
        r"""ListAssetOperationRecordsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。
        :type workspace_id: str
        :param limit: **参数解释**：限制量，单次查询总量，必须由数字组成。 **约束限制**：不涉及。 **取值范围**：1-1000。 **默认取值**：100。
        :type limit: int
        :param offset: **参数解释**：偏移量，查询起始偏移，必须由数字组成。 **约束限制**：不涉及。 **取值范围**0-100000000。 **默认取值**：0。
        :type offset: int
        :param sort_dir: **参数解释**：排序方向。 **约束限制**：不涉及。 **取值范围**： 枚举值： - ASC: 升序 - DESC: 降序。 **默认取值**：DESC。
        :type sort_dir: str
        :param sort_key: **参数解释**：排序字段。 **约束限制**：不涉及。 **取值范围**：枚举值： - created_at: 创建时间 - updated_at: 更新时间。 **默认取值**：created_at。
        :type sort_key: str
        :param record_id: **参数解释**：操作记录ID。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type record_id: str
        :param job_type: **参数解释**：作业类型。 **约束限制**：1-40位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type job_type: str
        :param job_id: **参数解释**：关联任务ID。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type job_id: str
        :param job_name: **参数解释**：关联任务名称。 **约束限制**：1-128位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type job_name: str
        :param job_status: **参数解释**：关联任务状态。 **约束限制**：1-40位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type job_status: str
        :param user_id: **参数解释**：操作用户ID。 **约束限制**：1-36位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type user_id: str
        :param user_name: **参数解释**：操作用户的用户名。 **约束限制**：1-128位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type user_name: str
        :param asset_id: **参数解释**：资产ID。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_id: str
        :param asset_code: **参数解释**：资产code。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type asset_code: str
        :param is_deleted: **参数解释**：任务是否删除。 **约束限制**：不涉及。 **取值范围**：true,false。 **默认取值**：不涉及。
        :type is_deleted: bool
        """
        
        

        self._workspace_id = None
        self._limit = None
        self._offset = None
        self._sort_dir = None
        self._sort_key = None
        self._record_id = None
        self._job_type = None
        self._job_id = None
        self._job_name = None
        self._job_status = None
        self._user_id = None
        self._user_name = None
        self._asset_id = None
        self._asset_code = None
        self._is_deleted = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if record_id is not None:
            self.record_id = record_id
        if job_type is not None:
            self.job_type = job_type
        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if job_status is not None:
            self.job_status = job_status
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if asset_id is not None:
            self.asset_id = asset_id
        if asset_code is not None:
            self.asset_code = asset_code
        if is_deleted is not None:
            self.is_deleted = is_deleted

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAssetOperationRecordsRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :return: The workspace_id of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAssetOperationRecordsRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :param workspace_id: The workspace_id of this ListAssetOperationRecordsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAssetOperationRecordsRequest.

        **参数解释**：限制量，单次查询总量，必须由数字组成。 **约束限制**：不涉及。 **取值范围**：1-1000。 **默认取值**：100。

        :return: The limit of this ListAssetOperationRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAssetOperationRecordsRequest.

        **参数解释**：限制量，单次查询总量，必须由数字组成。 **约束限制**：不涉及。 **取值范围**：1-1000。 **默认取值**：100。

        :param limit: The limit of this ListAssetOperationRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAssetOperationRecordsRequest.

        **参数解释**：偏移量，查询起始偏移，必须由数字组成。 **约束限制**：不涉及。 **取值范围**0-100000000。 **默认取值**：0。

        :return: The offset of this ListAssetOperationRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAssetOperationRecordsRequest.

        **参数解释**：偏移量，查询起始偏移，必须由数字组成。 **约束限制**：不涉及。 **取值范围**0-100000000。 **默认取值**：0。

        :param offset: The offset of this ListAssetOperationRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListAssetOperationRecordsRequest.

        **参数解释**：排序方向。 **约束限制**：不涉及。 **取值范围**： 枚举值： - ASC: 升序 - DESC: 降序。 **默认取值**：DESC。

        :return: The sort_dir of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListAssetOperationRecordsRequest.

        **参数解释**：排序方向。 **约束限制**：不涉及。 **取值范围**： 枚举值： - ASC: 升序 - DESC: 降序。 **默认取值**：DESC。

        :param sort_dir: The sort_dir of this ListAssetOperationRecordsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListAssetOperationRecordsRequest.

        **参数解释**：排序字段。 **约束限制**：不涉及。 **取值范围**：枚举值： - created_at: 创建时间 - updated_at: 更新时间。 **默认取值**：created_at。

        :return: The sort_key of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListAssetOperationRecordsRequest.

        **参数解释**：排序字段。 **约束限制**：不涉及。 **取值范围**：枚举值： - created_at: 创建时间 - updated_at: 更新时间。 **默认取值**：created_at。

        :param sort_key: The sort_key of this ListAssetOperationRecordsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def record_id(self):
        r"""Gets the record_id of this ListAssetOperationRecordsRequest.

        **参数解释**：操作记录ID。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The record_id of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        r"""Sets the record_id of this ListAssetOperationRecordsRequest.

        **参数解释**：操作记录ID。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param record_id: The record_id of this ListAssetOperationRecordsRequest.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def job_type(self):
        r"""Gets the job_type of this ListAssetOperationRecordsRequest.

        **参数解释**：作业类型。 **约束限制**：1-40位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The job_type of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListAssetOperationRecordsRequest.

        **参数解释**：作业类型。 **约束限制**：1-40位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param job_type: The job_type of this ListAssetOperationRecordsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_id(self):
        r"""Gets the job_id of this ListAssetOperationRecordsRequest.

        **参数解释**：关联任务ID。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The job_id of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListAssetOperationRecordsRequest.

        **参数解释**：关联任务ID。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param job_id: The job_id of this ListAssetOperationRecordsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ListAssetOperationRecordsRequest.

        **参数解释**：关联任务名称。 **约束限制**：1-128位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The job_name of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListAssetOperationRecordsRequest.

        **参数解释**：关联任务名称。 **约束限制**：1-128位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param job_name: The job_name of this ListAssetOperationRecordsRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_status(self):
        r"""Gets the job_status of this ListAssetOperationRecordsRequest.

        **参数解释**：关联任务状态。 **约束限制**：1-40位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The job_status of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        r"""Sets the job_status of this ListAssetOperationRecordsRequest.

        **参数解释**：关联任务状态。 **约束限制**：1-40位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param job_status: The job_status of this ListAssetOperationRecordsRequest.
        :type job_status: str
        """
        self._job_status = job_status

    @property
    def user_id(self):
        r"""Gets the user_id of this ListAssetOperationRecordsRequest.

        **参数解释**：操作用户ID。 **约束限制**：1-36位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The user_id of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ListAssetOperationRecordsRequest.

        **参数解释**：操作用户ID。 **约束限制**：1-36位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param user_id: The user_id of this ListAssetOperationRecordsRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ListAssetOperationRecordsRequest.

        **参数解释**：操作用户的用户名。 **约束限制**：1-128位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The user_name of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListAssetOperationRecordsRequest.

        **参数解释**：操作用户的用户名。 **约束限制**：1-128位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param user_name: The user_name of this ListAssetOperationRecordsRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ListAssetOperationRecordsRequest.

        **参数解释**：资产ID。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_id of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ListAssetOperationRecordsRequest.

        **参数解释**：资产ID。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_id: The asset_id of this ListAssetOperationRecordsRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_code(self):
        r"""Gets the asset_code of this ListAssetOperationRecordsRequest.

        **参数解释**：资产code。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The asset_code of this ListAssetOperationRecordsRequest.
        :rtype: str
        """
        return self._asset_code

    @asset_code.setter
    def asset_code(self, asset_code):
        r"""Sets the asset_code of this ListAssetOperationRecordsRequest.

        **参数解释**：资产code。 **约束限制**：1-64位字符串。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param asset_code: The asset_code of this ListAssetOperationRecordsRequest.
        :type asset_code: str
        """
        self._asset_code = asset_code

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this ListAssetOperationRecordsRequest.

        **参数解释**：任务是否删除。 **约束限制**：不涉及。 **取值范围**：true,false。 **默认取值**：不涉及。

        :return: The is_deleted of this ListAssetOperationRecordsRequest.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this ListAssetOperationRecordsRequest.

        **参数解释**：任务是否删除。 **约束限制**：不涉及。 **取值范围**：true,false。 **默认取值**：不涉及。

        :param is_deleted: The is_deleted of this ListAssetOperationRecordsRequest.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

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
        if not isinstance(other, ListAssetOperationRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
