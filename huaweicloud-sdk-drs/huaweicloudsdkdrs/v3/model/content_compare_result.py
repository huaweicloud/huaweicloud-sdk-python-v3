# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentCompareResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'compare_task_id': 'str',
        'content_compare_overview': 'list[ContentCompareResultOverview]',
        'content_compare_overview_count': 'int',
        'content_compare_details': 'list[ContentCompareResultDetails]',
        'content_compare_diffs': 'list[ContentCompareResultDiffs]',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'compare_task_id': 'compare_task_id',
        'content_compare_overview': 'content_compare_overview',
        'content_compare_overview_count': 'content_compare_overview_count',
        'content_compare_details': 'content_compare_details',
        'content_compare_diffs': 'content_compare_diffs',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, compare_task_id=None, content_compare_overview=None, content_compare_overview_count=None, content_compare_details=None, content_compare_diffs=None, error_code=None, error_msg=None):
        """ContentCompareResult

        The model defined in huaweicloud sdk

        :param compare_task_id: 内容对比的任务id。
        :type compare_task_id: str
        :param content_compare_overview: 内容对比结果概览。
        :type content_compare_overview: list[:class:`huaweicloudsdkdrs.v3.ContentCompareResultOverview`]
        :param content_compare_overview_count: 内容对比结果概览总数。
        :type content_compare_overview_count: int
        :param content_compare_details: 内容对比结果详情。
        :type content_compare_details: list[:class:`huaweicloudsdkdrs.v3.ContentCompareResultDetails`]
        :param content_compare_diffs: 内容对比结果差异。
        :type content_compare_diffs: list[:class:`huaweicloudsdkdrs.v3.ContentCompareResultDiffs`]
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误信息。
        :type error_msg: str
        """
        
        

        self._compare_task_id = None
        self._content_compare_overview = None
        self._content_compare_overview_count = None
        self._content_compare_details = None
        self._content_compare_diffs = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        self.compare_task_id = compare_task_id
        if content_compare_overview is not None:
            self.content_compare_overview = content_compare_overview
        if content_compare_overview_count is not None:
            self.content_compare_overview_count = content_compare_overview_count
        if content_compare_details is not None:
            self.content_compare_details = content_compare_details
        if content_compare_diffs is not None:
            self.content_compare_diffs = content_compare_diffs
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def compare_task_id(self):
        """Gets the compare_task_id of this ContentCompareResult.

        内容对比的任务id。

        :return: The compare_task_id of this ContentCompareResult.
        :rtype: str
        """
        return self._compare_task_id

    @compare_task_id.setter
    def compare_task_id(self, compare_task_id):
        """Sets the compare_task_id of this ContentCompareResult.

        内容对比的任务id。

        :param compare_task_id: The compare_task_id of this ContentCompareResult.
        :type compare_task_id: str
        """
        self._compare_task_id = compare_task_id

    @property
    def content_compare_overview(self):
        """Gets the content_compare_overview of this ContentCompareResult.

        内容对比结果概览。

        :return: The content_compare_overview of this ContentCompareResult.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ContentCompareResultOverview`]
        """
        return self._content_compare_overview

    @content_compare_overview.setter
    def content_compare_overview(self, content_compare_overview):
        """Sets the content_compare_overview of this ContentCompareResult.

        内容对比结果概览。

        :param content_compare_overview: The content_compare_overview of this ContentCompareResult.
        :type content_compare_overview: list[:class:`huaweicloudsdkdrs.v3.ContentCompareResultOverview`]
        """
        self._content_compare_overview = content_compare_overview

    @property
    def content_compare_overview_count(self):
        """Gets the content_compare_overview_count of this ContentCompareResult.

        内容对比结果概览总数。

        :return: The content_compare_overview_count of this ContentCompareResult.
        :rtype: int
        """
        return self._content_compare_overview_count

    @content_compare_overview_count.setter
    def content_compare_overview_count(self, content_compare_overview_count):
        """Sets the content_compare_overview_count of this ContentCompareResult.

        内容对比结果概览总数。

        :param content_compare_overview_count: The content_compare_overview_count of this ContentCompareResult.
        :type content_compare_overview_count: int
        """
        self._content_compare_overview_count = content_compare_overview_count

    @property
    def content_compare_details(self):
        """Gets the content_compare_details of this ContentCompareResult.

        内容对比结果详情。

        :return: The content_compare_details of this ContentCompareResult.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ContentCompareResultDetails`]
        """
        return self._content_compare_details

    @content_compare_details.setter
    def content_compare_details(self, content_compare_details):
        """Sets the content_compare_details of this ContentCompareResult.

        内容对比结果详情。

        :param content_compare_details: The content_compare_details of this ContentCompareResult.
        :type content_compare_details: list[:class:`huaweicloudsdkdrs.v3.ContentCompareResultDetails`]
        """
        self._content_compare_details = content_compare_details

    @property
    def content_compare_diffs(self):
        """Gets the content_compare_diffs of this ContentCompareResult.

        内容对比结果差异。

        :return: The content_compare_diffs of this ContentCompareResult.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ContentCompareResultDiffs`]
        """
        return self._content_compare_diffs

    @content_compare_diffs.setter
    def content_compare_diffs(self, content_compare_diffs):
        """Sets the content_compare_diffs of this ContentCompareResult.

        内容对比结果差异。

        :param content_compare_diffs: The content_compare_diffs of this ContentCompareResult.
        :type content_compare_diffs: list[:class:`huaweicloudsdkdrs.v3.ContentCompareResultDiffs`]
        """
        self._content_compare_diffs = content_compare_diffs

    @property
    def error_code(self):
        """Gets the error_code of this ContentCompareResult.

        错误码。

        :return: The error_code of this ContentCompareResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ContentCompareResult.

        错误码。

        :param error_code: The error_code of this ContentCompareResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ContentCompareResult.

        错误信息。

        :return: The error_msg of this ContentCompareResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ContentCompareResult.

        错误信息。

        :param error_msg: The error_msg of this ContentCompareResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ContentCompareResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
