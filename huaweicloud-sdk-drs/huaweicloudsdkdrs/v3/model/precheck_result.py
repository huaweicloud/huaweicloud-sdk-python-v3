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
        'failed_sub_jobs': 'list[PrecheckFailSubJobVO]'
    }

    attribute_map = {
        'item': 'item',
        'result': 'result',
        'failed_reason': 'failed_reason',
        'data': 'data',
        'raw_error_msg': 'raw_error_msg',
        'group': 'group',
        'failed_sub_jobs': 'failed_sub_jobs'
    }

    def __init__(self, item=None, result=None, failed_reason=None, data=None, raw_error_msg=None, group=None, failed_sub_jobs=None):
        """PrecheckResult

        The model defined in huaweicloud sdk

        :param item: 检查项。
        :type item: str
        :param result: 检查结果
        :type result: str
        :param failed_reason: 失败原因。
        :type failed_reason: str
        :param data: 加密的数据。
        :type data: str
        :param raw_error_msg: 行错误信息。
        :type raw_error_msg: str
        :param group: 检查项分组
        :type group: str
        :param failed_sub_jobs: 失败的子任务信息。
        :type failed_sub_jobs: list[:class:`huaweicloudsdkdrs.v3.PrecheckFailSubJobVO`]
        """
        
        

        self._item = None
        self._result = None
        self._failed_reason = None
        self._data = None
        self._raw_error_msg = None
        self._group = None
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
        if failed_sub_jobs is not None:
            self.failed_sub_jobs = failed_sub_jobs

    @property
    def item(self):
        """Gets the item of this PrecheckResult.

        检查项。

        :return: The item of this PrecheckResult.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this PrecheckResult.

        检查项。

        :param item: The item of this PrecheckResult.
        :type item: str
        """
        self._item = item

    @property
    def result(self):
        """Gets the result of this PrecheckResult.

        检查结果

        :return: The result of this PrecheckResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PrecheckResult.

        检查结果

        :param result: The result of this PrecheckResult.
        :type result: str
        """
        self._result = result

    @property
    def failed_reason(self):
        """Gets the failed_reason of this PrecheckResult.

        失败原因。

        :return: The failed_reason of this PrecheckResult.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this PrecheckResult.

        失败原因。

        :param failed_reason: The failed_reason of this PrecheckResult.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def data(self):
        """Gets the data of this PrecheckResult.

        加密的数据。

        :return: The data of this PrecheckResult.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PrecheckResult.

        加密的数据。

        :param data: The data of this PrecheckResult.
        :type data: str
        """
        self._data = data

    @property
    def raw_error_msg(self):
        """Gets the raw_error_msg of this PrecheckResult.

        行错误信息。

        :return: The raw_error_msg of this PrecheckResult.
        :rtype: str
        """
        return self._raw_error_msg

    @raw_error_msg.setter
    def raw_error_msg(self, raw_error_msg):
        """Sets the raw_error_msg of this PrecheckResult.

        行错误信息。

        :param raw_error_msg: The raw_error_msg of this PrecheckResult.
        :type raw_error_msg: str
        """
        self._raw_error_msg = raw_error_msg

    @property
    def group(self):
        """Gets the group of this PrecheckResult.

        检查项分组

        :return: The group of this PrecheckResult.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this PrecheckResult.

        检查项分组

        :param group: The group of this PrecheckResult.
        :type group: str
        """
        self._group = group

    @property
    def failed_sub_jobs(self):
        """Gets the failed_sub_jobs of this PrecheckResult.

        失败的子任务信息。

        :return: The failed_sub_jobs of this PrecheckResult.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.PrecheckFailSubJobVO`]
        """
        return self._failed_sub_jobs

    @failed_sub_jobs.setter
    def failed_sub_jobs(self, failed_sub_jobs):
        """Sets the failed_sub_jobs of this PrecheckResult.

        失败的子任务信息。

        :param failed_sub_jobs: The failed_sub_jobs of this PrecheckResult.
        :type failed_sub_jobs: list[:class:`huaweicloudsdkdrs.v3.PrecheckFailSubJobVO`]
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
