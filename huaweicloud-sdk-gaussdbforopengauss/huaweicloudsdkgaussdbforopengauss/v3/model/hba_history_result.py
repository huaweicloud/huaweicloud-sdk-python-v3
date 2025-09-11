# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HbaHistoryResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'time': 'datetime',
        'fail_reason': 'str',
        'before_confs': 'list[HbaConfResult]',
        'after_confs': 'list[HbaConfResult]'
    }

    attribute_map = {
        'status': 'status',
        'time': 'time',
        'fail_reason': 'fail_reason',
        'before_confs': 'before_confs',
        'after_confs': 'after_confs'
    }

    def __init__(self, status=None, time=None, fail_reason=None, before_confs=None, after_confs=None):
        r"""HbaHistoryResult

        The model defined in huaweicloud sdk

        :param status: **参数解释**: 修改结果。 **取值范围**:  - success：已生效。  - failed：未生效。  - etting：设置中。
        :type status: str
        :param time: **参数解释**: 修改时间。 **取值范围**: 不涉及。
        :type time: datetime
        :param fail_reason: **参数解释**: 修改失败原因。 **取值范围**: 不涉及。
        :type fail_reason: str
        :param before_confs: **参数解释**: 修改之前的值。
        :type before_confs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfResult`]
        :param after_confs: **参数解释**: 修改之后的值。
        :type after_confs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfResult`]
        """
        
        

        self._status = None
        self._time = None
        self._fail_reason = None
        self._before_confs = None
        self._after_confs = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if time is not None:
            self.time = time
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if before_confs is not None:
            self.before_confs = before_confs
        if after_confs is not None:
            self.after_confs = after_confs

    @property
    def status(self):
        r"""Gets the status of this HbaHistoryResult.

        **参数解释**: 修改结果。 **取值范围**:  - success：已生效。  - failed：未生效。  - etting：设置中。

        :return: The status of this HbaHistoryResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HbaHistoryResult.

        **参数解释**: 修改结果。 **取值范围**:  - success：已生效。  - failed：未生效。  - etting：设置中。

        :param status: The status of this HbaHistoryResult.
        :type status: str
        """
        self._status = status

    @property
    def time(self):
        r"""Gets the time of this HbaHistoryResult.

        **参数解释**: 修改时间。 **取值范围**: 不涉及。

        :return: The time of this HbaHistoryResult.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this HbaHistoryResult.

        **参数解释**: 修改时间。 **取值范围**: 不涉及。

        :param time: The time of this HbaHistoryResult.
        :type time: datetime
        """
        self._time = time

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this HbaHistoryResult.

        **参数解释**: 修改失败原因。 **取值范围**: 不涉及。

        :return: The fail_reason of this HbaHistoryResult.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this HbaHistoryResult.

        **参数解释**: 修改失败原因。 **取值范围**: 不涉及。

        :param fail_reason: The fail_reason of this HbaHistoryResult.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def before_confs(self):
        r"""Gets the before_confs of this HbaHistoryResult.

        **参数解释**: 修改之前的值。

        :return: The before_confs of this HbaHistoryResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfResult`]
        """
        return self._before_confs

    @before_confs.setter
    def before_confs(self, before_confs):
        r"""Sets the before_confs of this HbaHistoryResult.

        **参数解释**: 修改之前的值。

        :param before_confs: The before_confs of this HbaHistoryResult.
        :type before_confs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfResult`]
        """
        self._before_confs = before_confs

    @property
    def after_confs(self):
        r"""Gets the after_confs of this HbaHistoryResult.

        **参数解释**: 修改之后的值。

        :return: The after_confs of this HbaHistoryResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfResult`]
        """
        return self._after_confs

    @after_confs.setter
    def after_confs(self, after_confs):
        r"""Sets the after_confs of this HbaHistoryResult.

        **参数解释**: 修改之后的值。

        :param after_confs: The after_confs of this HbaHistoryResult.
        :type after_confs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfResult`]
        """
        self._after_confs = after_confs

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
        if not isinstance(other, HbaHistoryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
