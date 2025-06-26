# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterUpdateRecordResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_id': 'str',
        'status': 'str',
        'record_type': 'str',
        'from_version': 'str',
        'to_version': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'job_id': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'item_id': 'item_id',
        'status': 'status',
        'record_type': 'record_type',
        'from_version': 'from_version',
        'to_version': 'to_version',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'job_id': 'job_id',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, item_id=None, status=None, record_type=None, from_version=None, to_version=None, start_time=None, end_time=None, job_id=None, failed_reason=None):
        r"""ClusterUpdateRecordResp

        The model defined in huaweicloud sdk

        :param item_id: **参数解释**： 升级项目ID。 **取值范围**： 不涉及。
        :type item_id: str
        :param status: **参数解释**： 升级状态。 **取值范围**： 不涉及。
        :type status: str
        :param record_type: **参数解释**： 升级类型。 **取值范围**： 不涉及。
        :type record_type: str
        :param from_version: **参数解释**： 升级前版本。 **取值范围**： 不涉及。
        :type from_version: str
        :param to_version: **参数解释**： 目标版本。 **取值范围**： 不涉及。
        :type to_version: str
        :param start_time: **参数解释**： 开始时间。 **取值范围**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 结束时间。 **取值范围**： 不涉及。
        :type end_time: str
        :param job_id: **参数解释**： 升级任务ID。 **取值范围**： 不涉及。
        :type job_id: str
        :param failed_reason: **参数解释**： 失败原因。 **取值范围**： 不涉及。
        :type failed_reason: str
        """
        
        

        self._item_id = None
        self._status = None
        self._record_type = None
        self._from_version = None
        self._to_version = None
        self._start_time = None
        self._end_time = None
        self._job_id = None
        self._failed_reason = None
        self.discriminator = None

        if item_id is not None:
            self.item_id = item_id
        if status is not None:
            self.status = status
        if record_type is not None:
            self.record_type = record_type
        if from_version is not None:
            self.from_version = from_version
        if to_version is not None:
            self.to_version = to_version
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if job_id is not None:
            self.job_id = job_id
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def item_id(self):
        r"""Gets the item_id of this ClusterUpdateRecordResp.

        **参数解释**： 升级项目ID。 **取值范围**： 不涉及。

        :return: The item_id of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this ClusterUpdateRecordResp.

        **参数解释**： 升级项目ID。 **取值范围**： 不涉及。

        :param item_id: The item_id of this ClusterUpdateRecordResp.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def status(self):
        r"""Gets the status of this ClusterUpdateRecordResp.

        **参数解释**： 升级状态。 **取值范围**： 不涉及。

        :return: The status of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ClusterUpdateRecordResp.

        **参数解释**： 升级状态。 **取值范围**： 不涉及。

        :param status: The status of this ClusterUpdateRecordResp.
        :type status: str
        """
        self._status = status

    @property
    def record_type(self):
        r"""Gets the record_type of this ClusterUpdateRecordResp.

        **参数解释**： 升级类型。 **取值范围**： 不涉及。

        :return: The record_type of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        r"""Sets the record_type of this ClusterUpdateRecordResp.

        **参数解释**： 升级类型。 **取值范围**： 不涉及。

        :param record_type: The record_type of this ClusterUpdateRecordResp.
        :type record_type: str
        """
        self._record_type = record_type

    @property
    def from_version(self):
        r"""Gets the from_version of this ClusterUpdateRecordResp.

        **参数解释**： 升级前版本。 **取值范围**： 不涉及。

        :return: The from_version of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._from_version

    @from_version.setter
    def from_version(self, from_version):
        r"""Sets the from_version of this ClusterUpdateRecordResp.

        **参数解释**： 升级前版本。 **取值范围**： 不涉及。

        :param from_version: The from_version of this ClusterUpdateRecordResp.
        :type from_version: str
        """
        self._from_version = from_version

    @property
    def to_version(self):
        r"""Gets the to_version of this ClusterUpdateRecordResp.

        **参数解释**： 目标版本。 **取值范围**： 不涉及。

        :return: The to_version of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._to_version

    @to_version.setter
    def to_version(self, to_version):
        r"""Sets the to_version of this ClusterUpdateRecordResp.

        **参数解释**： 目标版本。 **取值范围**： 不涉及。

        :param to_version: The to_version of this ClusterUpdateRecordResp.
        :type to_version: str
        """
        self._to_version = to_version

    @property
    def start_time(self):
        r"""Gets the start_time of this ClusterUpdateRecordResp.

        **参数解释**： 开始时间。 **取值范围**： 不涉及。

        :return: The start_time of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ClusterUpdateRecordResp.

        **参数解释**： 开始时间。 **取值范围**： 不涉及。

        :param start_time: The start_time of this ClusterUpdateRecordResp.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ClusterUpdateRecordResp.

        **参数解释**： 结束时间。 **取值范围**： 不涉及。

        :return: The end_time of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ClusterUpdateRecordResp.

        **参数解释**： 结束时间。 **取值范围**： 不涉及。

        :param end_time: The end_time of this ClusterUpdateRecordResp.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def job_id(self):
        r"""Gets the job_id of this ClusterUpdateRecordResp.

        **参数解释**： 升级任务ID。 **取值范围**： 不涉及。

        :return: The job_id of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ClusterUpdateRecordResp.

        **参数解释**： 升级任务ID。 **取值范围**： 不涉及。

        :param job_id: The job_id of this ClusterUpdateRecordResp.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ClusterUpdateRecordResp.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。

        :return: The failed_reason of this ClusterUpdateRecordResp.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ClusterUpdateRecordResp.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。

        :param failed_reason: The failed_reason of this ClusterUpdateRecordResp.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

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
        if not isinstance(other, ClusterUpdateRecordResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
