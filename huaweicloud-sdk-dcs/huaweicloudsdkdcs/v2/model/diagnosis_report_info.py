# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosisReportInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id': 'str',
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'created_at': 'str',
        'node_num': 'int',
        'abnormal_item_sum': 'int',
        'failed_item_sum': 'int'
    }

    attribute_map = {
        'report_id': 'report_id',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'created_at': 'created_at',
        'node_num': 'node_num',
        'abnormal_item_sum': 'abnormal_item_sum',
        'failed_item_sum': 'failed_item_sum'
    }

    def __init__(self, report_id=None, status=None, begin_time=None, end_time=None, created_at=None, node_num=None, abnormal_item_sum=None, failed_item_sum=None):
        """DiagnosisReportInfo

        The model defined in huaweicloud sdk

        :param report_id: 诊断报告ID
        :type report_id: str
        :param status: 诊断任务状态
        :type status: str
        :param begin_time: 诊断时间段的开始时间。格式为：2017-03-31T12:24:46.297Z
        :type begin_time: str
        :param end_time: 诊断时间段的结束时间。格式为：2017-03-31T12:24:46.297Z
        :type end_time: str
        :param created_at: 诊断报告创建时间
        :type created_at: str
        :param node_num: 参与诊断的节点个数
        :type node_num: int
        :param abnormal_item_sum: 诊断结果为异常的诊断项总数
        :type abnormal_item_sum: int
        :param failed_item_sum: 诊断失败的诊断项总数
        :type failed_item_sum: int
        """
        
        

        self._report_id = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._created_at = None
        self._node_num = None
        self._abnormal_item_sum = None
        self._failed_item_sum = None
        self.discriminator = None

        self.report_id = report_id
        self.status = status
        self.begin_time = begin_time
        self.end_time = end_time
        self.created_at = created_at
        self.node_num = node_num
        self.abnormal_item_sum = abnormal_item_sum
        self.failed_item_sum = failed_item_sum

    @property
    def report_id(self):
        """Gets the report_id of this DiagnosisReportInfo.

        诊断报告ID

        :return: The report_id of this DiagnosisReportInfo.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this DiagnosisReportInfo.

        诊断报告ID

        :param report_id: The report_id of this DiagnosisReportInfo.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def status(self):
        """Gets the status of this DiagnosisReportInfo.

        诊断任务状态

        :return: The status of this DiagnosisReportInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DiagnosisReportInfo.

        诊断任务状态

        :param status: The status of this DiagnosisReportInfo.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        """Gets the begin_time of this DiagnosisReportInfo.

        诊断时间段的开始时间。格式为：2017-03-31T12:24:46.297Z

        :return: The begin_time of this DiagnosisReportInfo.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this DiagnosisReportInfo.

        诊断时间段的开始时间。格式为：2017-03-31T12:24:46.297Z

        :param begin_time: The begin_time of this DiagnosisReportInfo.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this DiagnosisReportInfo.

        诊断时间段的结束时间。格式为：2017-03-31T12:24:46.297Z

        :return: The end_time of this DiagnosisReportInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DiagnosisReportInfo.

        诊断时间段的结束时间。格式为：2017-03-31T12:24:46.297Z

        :param end_time: The end_time of this DiagnosisReportInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def created_at(self):
        """Gets the created_at of this DiagnosisReportInfo.

        诊断报告创建时间

        :return: The created_at of this DiagnosisReportInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DiagnosisReportInfo.

        诊断报告创建时间

        :param created_at: The created_at of this DiagnosisReportInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def node_num(self):
        """Gets the node_num of this DiagnosisReportInfo.

        参与诊断的节点个数

        :return: The node_num of this DiagnosisReportInfo.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this DiagnosisReportInfo.

        参与诊断的节点个数

        :param node_num: The node_num of this DiagnosisReportInfo.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def abnormal_item_sum(self):
        """Gets the abnormal_item_sum of this DiagnosisReportInfo.

        诊断结果为异常的诊断项总数

        :return: The abnormal_item_sum of this DiagnosisReportInfo.
        :rtype: int
        """
        return self._abnormal_item_sum

    @abnormal_item_sum.setter
    def abnormal_item_sum(self, abnormal_item_sum):
        """Sets the abnormal_item_sum of this DiagnosisReportInfo.

        诊断结果为异常的诊断项总数

        :param abnormal_item_sum: The abnormal_item_sum of this DiagnosisReportInfo.
        :type abnormal_item_sum: int
        """
        self._abnormal_item_sum = abnormal_item_sum

    @property
    def failed_item_sum(self):
        """Gets the failed_item_sum of this DiagnosisReportInfo.

        诊断失败的诊断项总数

        :return: The failed_item_sum of this DiagnosisReportInfo.
        :rtype: int
        """
        return self._failed_item_sum

    @failed_item_sum.setter
    def failed_item_sum(self, failed_item_sum):
        """Sets the failed_item_sum of this DiagnosisReportInfo.

        诊断失败的诊断项总数

        :param failed_item_sum: The failed_item_sum of this DiagnosisReportInfo.
        :type failed_item_sum: int
        """
        self._failed_item_sum = failed_item_sum

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
        if not isinstance(other, DiagnosisReportInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
