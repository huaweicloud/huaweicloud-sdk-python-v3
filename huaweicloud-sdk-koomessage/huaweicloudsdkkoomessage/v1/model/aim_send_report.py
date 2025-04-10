# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AimSendReport:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_time': 'str',
        'tpl_id': 'str',
        'tpl_name': 'str',
        'submission_count': 'int',
        'support_resolve_count': 'int',
        'send_count': 'int',
        'send_success_count': 'int',
        'resolve_success_count': 'int'
    }

    attribute_map = {
        'report_time': 'report_time',
        'tpl_id': 'tpl_id',
        'tpl_name': 'tpl_name',
        'submission_count': 'submission_count',
        'support_resolve_count': 'support_resolve_count',
        'send_count': 'send_count',
        'send_success_count': 'send_success_count',
        'resolve_success_count': 'resolve_success_count'
    }

    def __init__(self, report_time=None, tpl_id=None, tpl_name=None, submission_count=None, support_resolve_count=None, send_count=None, send_success_count=None, resolve_success_count=None):
        r"""AimSendReport

        The model defined in huaweicloud sdk

        :param report_time: 报表日期时间。
        :type report_time: str
        :param tpl_id: 智能信息模板ID。
        :type tpl_id: str
        :param tpl_name: 智能信息模板名称。
        :type tpl_name: str
        :param submission_count: 提交号码总数量。
        :type submission_count: int
        :param support_resolve_count: 支持解析数量。  &gt; 此数据不包括通过API发送的智能信息任务。 
        :type support_resolve_count: int
        :param send_count: 发送数量。
        :type send_count: int
        :param send_success_count: 成功发送数量。
        :type send_success_count: int
        :param resolve_success_count: 成功解析数量。
        :type resolve_success_count: int
        """
        
        

        self._report_time = None
        self._tpl_id = None
        self._tpl_name = None
        self._submission_count = None
        self._support_resolve_count = None
        self._send_count = None
        self._send_success_count = None
        self._resolve_success_count = None
        self.discriminator = None

        if report_time is not None:
            self.report_time = report_time
        if tpl_id is not None:
            self.tpl_id = tpl_id
        if tpl_name is not None:
            self.tpl_name = tpl_name
        if submission_count is not None:
            self.submission_count = submission_count
        if support_resolve_count is not None:
            self.support_resolve_count = support_resolve_count
        if send_count is not None:
            self.send_count = send_count
        if send_success_count is not None:
            self.send_success_count = send_success_count
        if resolve_success_count is not None:
            self.resolve_success_count = resolve_success_count

    @property
    def report_time(self):
        r"""Gets the report_time of this AimSendReport.

        报表日期时间。

        :return: The report_time of this AimSendReport.
        :rtype: str
        """
        return self._report_time

    @report_time.setter
    def report_time(self, report_time):
        r"""Sets the report_time of this AimSendReport.

        报表日期时间。

        :param report_time: The report_time of this AimSendReport.
        :type report_time: str
        """
        self._report_time = report_time

    @property
    def tpl_id(self):
        r"""Gets the tpl_id of this AimSendReport.

        智能信息模板ID。

        :return: The tpl_id of this AimSendReport.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        r"""Sets the tpl_id of this AimSendReport.

        智能信息模板ID。

        :param tpl_id: The tpl_id of this AimSendReport.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def tpl_name(self):
        r"""Gets the tpl_name of this AimSendReport.

        智能信息模板名称。

        :return: The tpl_name of this AimSendReport.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        r"""Sets the tpl_name of this AimSendReport.

        智能信息模板名称。

        :param tpl_name: The tpl_name of this AimSendReport.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def submission_count(self):
        r"""Gets the submission_count of this AimSendReport.

        提交号码总数量。

        :return: The submission_count of this AimSendReport.
        :rtype: int
        """
        return self._submission_count

    @submission_count.setter
    def submission_count(self, submission_count):
        r"""Sets the submission_count of this AimSendReport.

        提交号码总数量。

        :param submission_count: The submission_count of this AimSendReport.
        :type submission_count: int
        """
        self._submission_count = submission_count

    @property
    def support_resolve_count(self):
        r"""Gets the support_resolve_count of this AimSendReport.

        支持解析数量。  > 此数据不包括通过API发送的智能信息任务。 

        :return: The support_resolve_count of this AimSendReport.
        :rtype: int
        """
        return self._support_resolve_count

    @support_resolve_count.setter
    def support_resolve_count(self, support_resolve_count):
        r"""Sets the support_resolve_count of this AimSendReport.

        支持解析数量。  > 此数据不包括通过API发送的智能信息任务。 

        :param support_resolve_count: The support_resolve_count of this AimSendReport.
        :type support_resolve_count: int
        """
        self._support_resolve_count = support_resolve_count

    @property
    def send_count(self):
        r"""Gets the send_count of this AimSendReport.

        发送数量。

        :return: The send_count of this AimSendReport.
        :rtype: int
        """
        return self._send_count

    @send_count.setter
    def send_count(self, send_count):
        r"""Sets the send_count of this AimSendReport.

        发送数量。

        :param send_count: The send_count of this AimSendReport.
        :type send_count: int
        """
        self._send_count = send_count

    @property
    def send_success_count(self):
        r"""Gets the send_success_count of this AimSendReport.

        成功发送数量。

        :return: The send_success_count of this AimSendReport.
        :rtype: int
        """
        return self._send_success_count

    @send_success_count.setter
    def send_success_count(self, send_success_count):
        r"""Sets the send_success_count of this AimSendReport.

        成功发送数量。

        :param send_success_count: The send_success_count of this AimSendReport.
        :type send_success_count: int
        """
        self._send_success_count = send_success_count

    @property
    def resolve_success_count(self):
        r"""Gets the resolve_success_count of this AimSendReport.

        成功解析数量。

        :return: The resolve_success_count of this AimSendReport.
        :rtype: int
        """
        return self._resolve_success_count

    @resolve_success_count.setter
    def resolve_success_count(self, resolve_success_count):
        r"""Sets the resolve_success_count of this AimSendReport.

        成功解析数量。

        :param resolve_success_count: The resolve_success_count of this AimSendReport.
        :type resolve_success_count: int
        """
        self._resolve_success_count = resolve_success_count

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
        if not isinstance(other, AimSendReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
