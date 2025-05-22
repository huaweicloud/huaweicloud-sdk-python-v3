# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdentitySourceSyncRecordVo:

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
        'identity_source_id': 'str',
        'identity_source_type': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'add_count': 'int',
        'update_count': 'int',
        'delete_count': 'int',
        'failed_count': 'int',
        'status': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'identity_source_id': 'identity_source_id',
        'identity_source_type': 'identity_source_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'add_count': 'add_count',
        'update_count': 'update_count',
        'delete_count': 'delete_count',
        'failed_count': 'failed_count',
        'status': 'status',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, id=None, identity_source_id=None, identity_source_type=None, start_time=None, end_time=None, add_count=None, update_count=None, delete_count=None, failed_count=None, status=None, fail_reason=None):
        r"""IdentitySourceSyncRecordVo

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 记录ID。 **取值范围**： 不涉及。
        :type id: str
        :param identity_source_id: **参数解释**： 身份源ID。 **取值范围**： 不涉及。
        :type identity_source_id: str
        :param identity_source_type: **参数解释**： 身份源类型。 **取值范围**： 不涉及。
        :type identity_source_type: str
        :param start_time: **参数解释**： 任务开始时间。 **取值范围**： 不涉及。
        :type start_time: int
        :param end_time: **参数解释**： 任务结束时间。 **取值范围**： 不涉及。
        :type end_time: int
        :param add_count: **参数解释**： 添加记录数。 **取值范围**： 大于等于0。
        :type add_count: int
        :param update_count: **参数解释**： 更新记录数。 **取值范围**： 大于等于0。
        :type update_count: int
        :param delete_count: **参数解释**： 删除记录数。 **取值范围**： 大于等于0。
        :type delete_count: int
        :param failed_count: **参数解释**： 失败记录数。 **取值范围**： 大于等于0。
        :type failed_count: int
        :param status: **参数解释**： 状态。 **取值范围**： 不涉及。
        :type status: str
        :param fail_reason: **参数解释**： 失败原因。 **取值范围**： 不涉及。
        :type fail_reason: str
        """
        
        

        self._id = None
        self._identity_source_id = None
        self._identity_source_type = None
        self._start_time = None
        self._end_time = None
        self._add_count = None
        self._update_count = None
        self._delete_count = None
        self._failed_count = None
        self._status = None
        self._fail_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if identity_source_id is not None:
            self.identity_source_id = identity_source_id
        if identity_source_type is not None:
            self.identity_source_type = identity_source_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if add_count is not None:
            self.add_count = add_count
        if update_count is not None:
            self.update_count = update_count
        if delete_count is not None:
            self.delete_count = delete_count
        if failed_count is not None:
            self.failed_count = failed_count
        if status is not None:
            self.status = status
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def id(self):
        r"""Gets the id of this IdentitySourceSyncRecordVo.

        **参数解释**： 记录ID。 **取值范围**： 不涉及。

        :return: The id of this IdentitySourceSyncRecordVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IdentitySourceSyncRecordVo.

        **参数解释**： 记录ID。 **取值范围**： 不涉及。

        :param id: The id of this IdentitySourceSyncRecordVo.
        :type id: str
        """
        self._id = id

    @property
    def identity_source_id(self):
        r"""Gets the identity_source_id of this IdentitySourceSyncRecordVo.

        **参数解释**： 身份源ID。 **取值范围**： 不涉及。

        :return: The identity_source_id of this IdentitySourceSyncRecordVo.
        :rtype: str
        """
        return self._identity_source_id

    @identity_source_id.setter
    def identity_source_id(self, identity_source_id):
        r"""Sets the identity_source_id of this IdentitySourceSyncRecordVo.

        **参数解释**： 身份源ID。 **取值范围**： 不涉及。

        :param identity_source_id: The identity_source_id of this IdentitySourceSyncRecordVo.
        :type identity_source_id: str
        """
        self._identity_source_id = identity_source_id

    @property
    def identity_source_type(self):
        r"""Gets the identity_source_type of this IdentitySourceSyncRecordVo.

        **参数解释**： 身份源类型。 **取值范围**： 不涉及。

        :return: The identity_source_type of this IdentitySourceSyncRecordVo.
        :rtype: str
        """
        return self._identity_source_type

    @identity_source_type.setter
    def identity_source_type(self, identity_source_type):
        r"""Sets the identity_source_type of this IdentitySourceSyncRecordVo.

        **参数解释**： 身份源类型。 **取值范围**： 不涉及。

        :param identity_source_type: The identity_source_type of this IdentitySourceSyncRecordVo.
        :type identity_source_type: str
        """
        self._identity_source_type = identity_source_type

    @property
    def start_time(self):
        r"""Gets the start_time of this IdentitySourceSyncRecordVo.

        **参数解释**： 任务开始时间。 **取值范围**： 不涉及。

        :return: The start_time of this IdentitySourceSyncRecordVo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this IdentitySourceSyncRecordVo.

        **参数解释**： 任务开始时间。 **取值范围**： 不涉及。

        :param start_time: The start_time of this IdentitySourceSyncRecordVo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this IdentitySourceSyncRecordVo.

        **参数解释**： 任务结束时间。 **取值范围**： 不涉及。

        :return: The end_time of this IdentitySourceSyncRecordVo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this IdentitySourceSyncRecordVo.

        **参数解释**： 任务结束时间。 **取值范围**： 不涉及。

        :param end_time: The end_time of this IdentitySourceSyncRecordVo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def add_count(self):
        r"""Gets the add_count of this IdentitySourceSyncRecordVo.

        **参数解释**： 添加记录数。 **取值范围**： 大于等于0。

        :return: The add_count of this IdentitySourceSyncRecordVo.
        :rtype: int
        """
        return self._add_count

    @add_count.setter
    def add_count(self, add_count):
        r"""Sets the add_count of this IdentitySourceSyncRecordVo.

        **参数解释**： 添加记录数。 **取值范围**： 大于等于0。

        :param add_count: The add_count of this IdentitySourceSyncRecordVo.
        :type add_count: int
        """
        self._add_count = add_count

    @property
    def update_count(self):
        r"""Gets the update_count of this IdentitySourceSyncRecordVo.

        **参数解释**： 更新记录数。 **取值范围**： 大于等于0。

        :return: The update_count of this IdentitySourceSyncRecordVo.
        :rtype: int
        """
        return self._update_count

    @update_count.setter
    def update_count(self, update_count):
        r"""Sets the update_count of this IdentitySourceSyncRecordVo.

        **参数解释**： 更新记录数。 **取值范围**： 大于等于0。

        :param update_count: The update_count of this IdentitySourceSyncRecordVo.
        :type update_count: int
        """
        self._update_count = update_count

    @property
    def delete_count(self):
        r"""Gets the delete_count of this IdentitySourceSyncRecordVo.

        **参数解释**： 删除记录数。 **取值范围**： 大于等于0。

        :return: The delete_count of this IdentitySourceSyncRecordVo.
        :rtype: int
        """
        return self._delete_count

    @delete_count.setter
    def delete_count(self, delete_count):
        r"""Sets the delete_count of this IdentitySourceSyncRecordVo.

        **参数解释**： 删除记录数。 **取值范围**： 大于等于0。

        :param delete_count: The delete_count of this IdentitySourceSyncRecordVo.
        :type delete_count: int
        """
        self._delete_count = delete_count

    @property
    def failed_count(self):
        r"""Gets the failed_count of this IdentitySourceSyncRecordVo.

        **参数解释**： 失败记录数。 **取值范围**： 大于等于0。

        :return: The failed_count of this IdentitySourceSyncRecordVo.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        r"""Sets the failed_count of this IdentitySourceSyncRecordVo.

        **参数解释**： 失败记录数。 **取值范围**： 大于等于0。

        :param failed_count: The failed_count of this IdentitySourceSyncRecordVo.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def status(self):
        r"""Gets the status of this IdentitySourceSyncRecordVo.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :return: The status of this IdentitySourceSyncRecordVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IdentitySourceSyncRecordVo.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :param status: The status of this IdentitySourceSyncRecordVo.
        :type status: str
        """
        self._status = status

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this IdentitySourceSyncRecordVo.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。

        :return: The fail_reason of this IdentitySourceSyncRecordVo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this IdentitySourceSyncRecordVo.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。

        :param fail_reason: The fail_reason of this IdentitySourceSyncRecordVo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, IdentitySourceSyncRecordVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
