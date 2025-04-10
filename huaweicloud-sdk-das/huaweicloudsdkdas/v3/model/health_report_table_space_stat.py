# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportTableSpaceStat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size_top': 'list[HealthReportTableSpaceInfo]',
        'rows_top': 'list[HealthReportTableSpaceInfo]',
        'size_incr_top': 'list[HealthReportTableSpaceIncrInfo]',
        'rows_incr_top': 'list[HealthReportTableSpaceIncrInfo]',
        'analyze_success': 'bool',
        'error_message': 'str'
    }

    attribute_map = {
        'size_top': 'size_top',
        'rows_top': 'rows_top',
        'size_incr_top': 'size_incr_top',
        'rows_incr_top': 'rows_incr_top',
        'analyze_success': 'analyze_success',
        'error_message': 'error_message'
    }

    def __init__(self, size_top=None, rows_top=None, size_incr_top=None, rows_incr_top=None, analyze_success=None, error_message=None):
        r"""HealthReportTableSpaceStat

        The model defined in huaweicloud sdk

        :param size_top: 表大小Top列表。
        :type size_top: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceInfo`]
        :param rows_top: 表行数量Top列表。
        :type rows_top: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceInfo`]
        :param size_incr_top: 表大小增长Top列表。
        :type size_incr_top: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceIncrInfo`]
        :param rows_incr_top: 表行数量增长Top列表。
        :type rows_incr_top: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceIncrInfo`]
        :param analyze_success: 统计分析是否成功。
        :type analyze_success: bool
        :param error_message: 错误信息。
        :type error_message: str
        """
        
        

        self._size_top = None
        self._rows_top = None
        self._size_incr_top = None
        self._rows_incr_top = None
        self._analyze_success = None
        self._error_message = None
        self.discriminator = None

        self.size_top = size_top
        self.rows_top = rows_top
        self.size_incr_top = size_incr_top
        self.rows_incr_top = rows_incr_top
        self.analyze_success = analyze_success
        self.error_message = error_message

    @property
    def size_top(self):
        r"""Gets the size_top of this HealthReportTableSpaceStat.

        表大小Top列表。

        :return: The size_top of this HealthReportTableSpaceStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceInfo`]
        """
        return self._size_top

    @size_top.setter
    def size_top(self, size_top):
        r"""Sets the size_top of this HealthReportTableSpaceStat.

        表大小Top列表。

        :param size_top: The size_top of this HealthReportTableSpaceStat.
        :type size_top: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceInfo`]
        """
        self._size_top = size_top

    @property
    def rows_top(self):
        r"""Gets the rows_top of this HealthReportTableSpaceStat.

        表行数量Top列表。

        :return: The rows_top of this HealthReportTableSpaceStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceInfo`]
        """
        return self._rows_top

    @rows_top.setter
    def rows_top(self, rows_top):
        r"""Sets the rows_top of this HealthReportTableSpaceStat.

        表行数量Top列表。

        :param rows_top: The rows_top of this HealthReportTableSpaceStat.
        :type rows_top: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceInfo`]
        """
        self._rows_top = rows_top

    @property
    def size_incr_top(self):
        r"""Gets the size_incr_top of this HealthReportTableSpaceStat.

        表大小增长Top列表。

        :return: The size_incr_top of this HealthReportTableSpaceStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceIncrInfo`]
        """
        return self._size_incr_top

    @size_incr_top.setter
    def size_incr_top(self, size_incr_top):
        r"""Sets the size_incr_top of this HealthReportTableSpaceStat.

        表大小增长Top列表。

        :param size_incr_top: The size_incr_top of this HealthReportTableSpaceStat.
        :type size_incr_top: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceIncrInfo`]
        """
        self._size_incr_top = size_incr_top

    @property
    def rows_incr_top(self):
        r"""Gets the rows_incr_top of this HealthReportTableSpaceStat.

        表行数量增长Top列表。

        :return: The rows_incr_top of this HealthReportTableSpaceStat.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceIncrInfo`]
        """
        return self._rows_incr_top

    @rows_incr_top.setter
    def rows_incr_top(self, rows_incr_top):
        r"""Sets the rows_incr_top of this HealthReportTableSpaceStat.

        表行数量增长Top列表。

        :param rows_incr_top: The rows_incr_top of this HealthReportTableSpaceStat.
        :type rows_incr_top: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceIncrInfo`]
        """
        self._rows_incr_top = rows_incr_top

    @property
    def analyze_success(self):
        r"""Gets the analyze_success of this HealthReportTableSpaceStat.

        统计分析是否成功。

        :return: The analyze_success of this HealthReportTableSpaceStat.
        :rtype: bool
        """
        return self._analyze_success

    @analyze_success.setter
    def analyze_success(self, analyze_success):
        r"""Sets the analyze_success of this HealthReportTableSpaceStat.

        统计分析是否成功。

        :param analyze_success: The analyze_success of this HealthReportTableSpaceStat.
        :type analyze_success: bool
        """
        self._analyze_success = analyze_success

    @property
    def error_message(self):
        r"""Gets the error_message of this HealthReportTableSpaceStat.

        错误信息。

        :return: The error_message of this HealthReportTableSpaceStat.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this HealthReportTableSpaceStat.

        错误信息。

        :param error_message: The error_message of this HealthReportTableSpaceStat.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, HealthReportTableSpaceStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
