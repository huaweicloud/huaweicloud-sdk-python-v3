# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrecheckResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item': 'str',
        'result': 'str',
        'failed_reason': 'str',
        'data': 'str',
        'raw_error_msg': 'str',
        'group': 'str',
        'is_support_skip': 'bool',
        'is_skipped': 'bool',
        'failed_sub_jobs': 'list[PrecheckFailSubJobResult]'
    }

    attribute_map = {
        'item': 'item',
        'result': 'result',
        'failed_reason': 'failed_reason',
        'data': 'data',
        'raw_error_msg': 'raw_error_msg',
        'group': 'group',
        'is_support_skip': 'is_support_skip',
        'is_skipped': 'is_skipped',
        'failed_sub_jobs': 'failed_sub_jobs'
    }

    def __init__(self, item=None, result=None, failed_reason=None, data=None, raw_error_msg=None, group=None, is_support_skip=None, is_skipped=None, failed_sub_jobs=None):
        r"""PrecheckResult

        The model defined in huaweicloud sdk

        :param item: 检查项。
        :type item: str
        :param result: 检查结果。取值： - PASSED：检查通过。 - ALARM：检查告警项。 - FAILED：检查失败。
        :type result: str
        :param failed_reason: 失败原因。
        :type failed_reason: str
        :param data: 失败数据。
        :type data: str
        :param raw_error_msg: 失败详情。
        :type raw_error_msg: str
        :param group: 检查项分组。
        :type group: str
        :param is_support_skip: 是否支持跳过。
        :type is_support_skip: bool
        :param is_skipped: 是否已跳过。
        :type is_skipped: bool
        :param failed_sub_jobs: 失败子任务详情。
        :type failed_sub_jobs: list[:class:`huaweicloudsdkdrs.v5.PrecheckFailSubJobResult`]
        """
        
        

        self._item = None
        self._result = None
        self._failed_reason = None
        self._data = None
        self._raw_error_msg = None
        self._group = None
        self._is_support_skip = None
        self._is_skipped = None
        self._failed_sub_jobs = None
        self.discriminator = None

        if item is not None:
            self.item = item
        if result is not None:
            self.result = result
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if data is not None:
            self.data = data
        if raw_error_msg is not None:
            self.raw_error_msg = raw_error_msg
        if group is not None:
            self.group = group
        if is_support_skip is not None:
            self.is_support_skip = is_support_skip
        if is_skipped is not None:
            self.is_skipped = is_skipped
        if failed_sub_jobs is not None:
            self.failed_sub_jobs = failed_sub_jobs

    @property
    def item(self):
        r"""Gets the item of this PrecheckResult.

        检查项。

        :return: The item of this PrecheckResult.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this PrecheckResult.

        检查项。

        :param item: The item of this PrecheckResult.
        :type item: str
        """
        self._item = item

    @property
    def result(self):
        r"""Gets the result of this PrecheckResult.

        检查结果。取值： - PASSED：检查通过。 - ALARM：检查告警项。 - FAILED：检查失败。

        :return: The result of this PrecheckResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this PrecheckResult.

        检查结果。取值： - PASSED：检查通过。 - ALARM：检查告警项。 - FAILED：检查失败。

        :param result: The result of this PrecheckResult.
        :type result: str
        """
        self._result = result

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this PrecheckResult.

        失败原因。

        :return: The failed_reason of this PrecheckResult.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this PrecheckResult.

        失败原因。

        :param failed_reason: The failed_reason of this PrecheckResult.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def data(self):
        r"""Gets the data of this PrecheckResult.

        失败数据。

        :return: The data of this PrecheckResult.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this PrecheckResult.

        失败数据。

        :param data: The data of this PrecheckResult.
        :type data: str
        """
        self._data = data

    @property
    def raw_error_msg(self):
        r"""Gets the raw_error_msg of this PrecheckResult.

        失败详情。

        :return: The raw_error_msg of this PrecheckResult.
        :rtype: str
        """
        return self._raw_error_msg

    @raw_error_msg.setter
    def raw_error_msg(self, raw_error_msg):
        r"""Sets the raw_error_msg of this PrecheckResult.

        失败详情。

        :param raw_error_msg: The raw_error_msg of this PrecheckResult.
        :type raw_error_msg: str
        """
        self._raw_error_msg = raw_error_msg

    @property
    def group(self):
        r"""Gets the group of this PrecheckResult.

        检查项分组。

        :return: The group of this PrecheckResult.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this PrecheckResult.

        检查项分组。

        :param group: The group of this PrecheckResult.
        :type group: str
        """
        self._group = group

    @property
    def is_support_skip(self):
        r"""Gets the is_support_skip of this PrecheckResult.

        是否支持跳过。

        :return: The is_support_skip of this PrecheckResult.
        :rtype: bool
        """
        return self._is_support_skip

    @is_support_skip.setter
    def is_support_skip(self, is_support_skip):
        r"""Sets the is_support_skip of this PrecheckResult.

        是否支持跳过。

        :param is_support_skip: The is_support_skip of this PrecheckResult.
        :type is_support_skip: bool
        """
        self._is_support_skip = is_support_skip

    @property
    def is_skipped(self):
        r"""Gets the is_skipped of this PrecheckResult.

        是否已跳过。

        :return: The is_skipped of this PrecheckResult.
        :rtype: bool
        """
        return self._is_skipped

    @is_skipped.setter
    def is_skipped(self, is_skipped):
        r"""Sets the is_skipped of this PrecheckResult.

        是否已跳过。

        :param is_skipped: The is_skipped of this PrecheckResult.
        :type is_skipped: bool
        """
        self._is_skipped = is_skipped

    @property
    def failed_sub_jobs(self):
        r"""Gets the failed_sub_jobs of this PrecheckResult.

        失败子任务详情。

        :return: The failed_sub_jobs of this PrecheckResult.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.PrecheckFailSubJobResult`]
        """
        return self._failed_sub_jobs

    @failed_sub_jobs.setter
    def failed_sub_jobs(self, failed_sub_jobs):
        r"""Sets the failed_sub_jobs of this PrecheckResult.

        失败子任务详情。

        :param failed_sub_jobs: The failed_sub_jobs of this PrecheckResult.
        :type failed_sub_jobs: list[:class:`huaweicloudsdkdrs.v5.PrecheckFailSubJobResult`]
        """
        self._failed_sub_jobs = failed_sub_jobs

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
        if not isinstance(other, PrecheckResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
