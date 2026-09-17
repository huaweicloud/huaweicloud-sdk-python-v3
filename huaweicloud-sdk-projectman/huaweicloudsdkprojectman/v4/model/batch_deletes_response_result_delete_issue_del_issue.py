# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeletesResponseResultDeleteIssueDelIssue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'tracker_id': 'int',
        'subject': 'str',
        'status_id': 'int',
        'done_ratio': 'int',
        'expected_work_hours': 'int',
        'actual_work_hours': 'int',
        'deleted': 'bool',
        'is_archived': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'tracker_id': 'tracker_id',
        'subject': 'subject',
        'status_id': 'status_id',
        'done_ratio': 'done_ratio',
        'expected_work_hours': 'expected_work_hours',
        'actual_work_hours': 'actual_work_hours',
        'deleted': 'deleted',
        'is_archived': 'is_archived'
    }

    def __init__(self, id=None, tracker_id=None, subject=None, status_id=None, done_ratio=None, expected_work_hours=None, actual_work_hours=None, deleted=None, is_archived=None):
        r"""BatchDeletesResponseResultDeleteIssueDelIssue

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 工作项id。 **取值范围：** 不涉及。
        :type id: int
        :param tracker_id: **参数解释：** 工作项类型。 **取值范围：** 2（任务/Task） 3（缺陷/Bug） 5（Epic） 6（Feature） 7（Story）
        :type tracker_id: int
        :param subject: **参数解释：** 工作项名称 。 **取值范围：** 不涉及。
        :type subject: str
        :param status_id: **参数解释：** 工作项状态id 。 **取值范围：** 不涉及。
        :type status_id: int
        :param done_ratio: **参数解释：** 工作项完成度。 **取值范围：** 不涉及。
        :type done_ratio: int
        :param expected_work_hours: **参数解释：** 预计工时(单位：人时)。 **取值范围：** 不涉及。
        :type expected_work_hours: int
        :param actual_work_hours: **参数解释：** 实际工时(单位：人时)。 **取值范围：** 不涉及。
        :type actual_work_hours: int
        :param deleted: **参数解释：** 是否完成删除。 **取值范围：** 0（未删除） 1（已删除）
        :type deleted: bool
        :param is_archived: **参数解释：** 是否归档。 **取值范围：** 0（未归档） 1（已归档）
        :type is_archived: bool
        """
        
        

        self._id = None
        self._tracker_id = None
        self._subject = None
        self._status_id = None
        self._done_ratio = None
        self._expected_work_hours = None
        self._actual_work_hours = None
        self._deleted = None
        self._is_archived = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tracker_id is not None:
            self.tracker_id = tracker_id
        if subject is not None:
            self.subject = subject
        if status_id is not None:
            self.status_id = status_id
        if done_ratio is not None:
            self.done_ratio = done_ratio
        if expected_work_hours is not None:
            self.expected_work_hours = expected_work_hours
        if actual_work_hours is not None:
            self.actual_work_hours = actual_work_hours
        if deleted is not None:
            self.deleted = deleted
        if is_archived is not None:
            self.is_archived = is_archived

    @property
    def id(self):
        r"""Gets the id of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 工作项id。 **取值范围：** 不涉及。

        :return: The id of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 工作项id。 **取值范围：** 不涉及。

        :param id: The id of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :type id: int
        """
        self._id = id

    @property
    def tracker_id(self):
        r"""Gets the tracker_id of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 工作项类型。 **取值范围：** 2（任务/Task） 3（缺陷/Bug） 5（Epic） 6（Feature） 7（Story）

        :return: The tracker_id of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :rtype: int
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        r"""Sets the tracker_id of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 工作项类型。 **取值范围：** 2（任务/Task） 3（缺陷/Bug） 5（Epic） 6（Feature） 7（Story）

        :param tracker_id: The tracker_id of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :type tracker_id: int
        """
        self._tracker_id = tracker_id

    @property
    def subject(self):
        r"""Gets the subject of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 工作项名称 。 **取值范围：** 不涉及。

        :return: The subject of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 工作项名称 。 **取值范围：** 不涉及。

        :param subject: The subject of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :type subject: str
        """
        self._subject = subject

    @property
    def status_id(self):
        r"""Gets the status_id of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 工作项状态id 。 **取值范围：** 不涉及。

        :return: The status_id of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        r"""Sets the status_id of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 工作项状态id 。 **取值范围：** 不涉及。

        :param status_id: The status_id of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :type status_id: int
        """
        self._status_id = status_id

    @property
    def done_ratio(self):
        r"""Gets the done_ratio of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 工作项完成度。 **取值范围：** 不涉及。

        :return: The done_ratio of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :rtype: int
        """
        return self._done_ratio

    @done_ratio.setter
    def done_ratio(self, done_ratio):
        r"""Sets the done_ratio of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 工作项完成度。 **取值范围：** 不涉及。

        :param done_ratio: The done_ratio of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :type done_ratio: int
        """
        self._done_ratio = done_ratio

    @property
    def expected_work_hours(self):
        r"""Gets the expected_work_hours of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 预计工时(单位：人时)。 **取值范围：** 不涉及。

        :return: The expected_work_hours of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :rtype: int
        """
        return self._expected_work_hours

    @expected_work_hours.setter
    def expected_work_hours(self, expected_work_hours):
        r"""Sets the expected_work_hours of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 预计工时(单位：人时)。 **取值范围：** 不涉及。

        :param expected_work_hours: The expected_work_hours of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :type expected_work_hours: int
        """
        self._expected_work_hours = expected_work_hours

    @property
    def actual_work_hours(self):
        r"""Gets the actual_work_hours of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 实际工时(单位：人时)。 **取值范围：** 不涉及。

        :return: The actual_work_hours of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :rtype: int
        """
        return self._actual_work_hours

    @actual_work_hours.setter
    def actual_work_hours(self, actual_work_hours):
        r"""Sets the actual_work_hours of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 实际工时(单位：人时)。 **取值范围：** 不涉及。

        :param actual_work_hours: The actual_work_hours of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :type actual_work_hours: int
        """
        self._actual_work_hours = actual_work_hours

    @property
    def deleted(self):
        r"""Gets the deleted of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 是否完成删除。 **取值范围：** 0（未删除） 1（已删除）

        :return: The deleted of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 是否完成删除。 **取值范围：** 0（未删除） 1（已删除）

        :param deleted: The deleted of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :type deleted: bool
        """
        self._deleted = deleted

    @property
    def is_archived(self):
        r"""Gets the is_archived of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 是否归档。 **取值范围：** 0（未归档） 1（已归档）

        :return: The is_archived of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        r"""Sets the is_archived of this BatchDeletesResponseResultDeleteIssueDelIssue.

        **参数解释：** 是否归档。 **取值范围：** 0（未归档） 1（已归档）

        :param is_archived: The is_archived of this BatchDeletesResponseResultDeleteIssueDelIssue.
        :type is_archived: bool
        """
        self._is_archived = is_archived

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
        if not isinstance(other, BatchDeletesResponseResultDeleteIssueDelIssue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
