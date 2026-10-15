# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportFileObsUrisRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'report_type': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'report_type': 'report_type',
        'x_language': 'X-Language'
    }

    def __init__(self, job_id=None, report_type=None, x_language=None):
        r"""ShowReportFileObsUrisRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param report_type: 导出的sql文件类型。取值范围：  abnormal_sql ：异常sql列表 abnormal_sql_detail ：异常sql详情 slow_sql ：慢sql列表 slow_sql_detail ： 慢sql详情
        :type report_type: str
        :param x_language: 请求语言类型。
        :type x_language: str
        """
        
        

        self._job_id = None
        self._report_type = None
        self._x_language = None
        self.discriminator = None

        self.job_id = job_id
        self.report_type = report_type
        if x_language is not None:
            self.x_language = x_language

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowReportFileObsUrisRequest.

        任务ID。

        :return: The job_id of this ShowReportFileObsUrisRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowReportFileObsUrisRequest.

        任务ID。

        :param job_id: The job_id of this ShowReportFileObsUrisRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def report_type(self):
        r"""Gets the report_type of this ShowReportFileObsUrisRequest.

        导出的sql文件类型。取值范围：  abnormal_sql ：异常sql列表 abnormal_sql_detail ：异常sql详情 slow_sql ：慢sql列表 slow_sql_detail ： 慢sql详情

        :return: The report_type of this ShowReportFileObsUrisRequest.
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        r"""Sets the report_type of this ShowReportFileObsUrisRequest.

        导出的sql文件类型。取值范围：  abnormal_sql ：异常sql列表 abnormal_sql_detail ：异常sql详情 slow_sql ：慢sql列表 slow_sql_detail ： 慢sql详情

        :param report_type: The report_type of this ShowReportFileObsUrisRequest.
        :type report_type: str
        """
        self._report_type = report_type

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowReportFileObsUrisRequest.

        请求语言类型。

        :return: The x_language of this ShowReportFileObsUrisRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowReportFileObsUrisRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowReportFileObsUrisRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowReportFileObsUrisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
