# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationRecordResp:

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
        'operator': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'operator': 'operator',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, id=None, operator=None, start_time=None, end_time=None, status=None, failed_reason=None):
        r"""ConfigurationRecordResp

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 记录ID。 **取值范围**： 不涉及。
        :type id: str
        :param operator: **参数解释**： 操作名称。 **取值范围**： 不涉及。
        :type operator: str
        :param start_time: **参数解释**： 开始时间。 **取值范围**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 结束时间。 **取值范围**： 不涉及。
        :type end_time: str
        :param status: **参数解释**： 状态。 **取值范围**： 不涉及。
        :type status: str
        :param failed_reason: **参数解释**： 失败原因。 **取值范围**： 不涉及。
        :type failed_reason: str
        """
        
        

        self._id = None
        self._operator = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._failed_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if operator is not None:
            self.operator = operator
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def id(self):
        r"""Gets the id of this ConfigurationRecordResp.

        **参数解释**： 记录ID。 **取值范围**： 不涉及。

        :return: The id of this ConfigurationRecordResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConfigurationRecordResp.

        **参数解释**： 记录ID。 **取值范围**： 不涉及。

        :param id: The id of this ConfigurationRecordResp.
        :type id: str
        """
        self._id = id

    @property
    def operator(self):
        r"""Gets the operator of this ConfigurationRecordResp.

        **参数解释**： 操作名称。 **取值范围**： 不涉及。

        :return: The operator of this ConfigurationRecordResp.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ConfigurationRecordResp.

        **参数解释**： 操作名称。 **取值范围**： 不涉及。

        :param operator: The operator of this ConfigurationRecordResp.
        :type operator: str
        """
        self._operator = operator

    @property
    def start_time(self):
        r"""Gets the start_time of this ConfigurationRecordResp.

        **参数解释**： 开始时间。 **取值范围**： 不涉及。

        :return: The start_time of this ConfigurationRecordResp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ConfigurationRecordResp.

        **参数解释**： 开始时间。 **取值范围**： 不涉及。

        :param start_time: The start_time of this ConfigurationRecordResp.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ConfigurationRecordResp.

        **参数解释**： 结束时间。 **取值范围**： 不涉及。

        :return: The end_time of this ConfigurationRecordResp.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ConfigurationRecordResp.

        **参数解释**： 结束时间。 **取值范围**： 不涉及。

        :param end_time: The end_time of this ConfigurationRecordResp.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this ConfigurationRecordResp.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :return: The status of this ConfigurationRecordResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ConfigurationRecordResp.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :param status: The status of this ConfigurationRecordResp.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ConfigurationRecordResp.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。

        :return: The failed_reason of this ConfigurationRecordResp.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ConfigurationRecordResp.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。

        :param failed_reason: The failed_reason of this ConfigurationRecordResp.
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
        if not isinstance(other, ConfigurationRecordResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
