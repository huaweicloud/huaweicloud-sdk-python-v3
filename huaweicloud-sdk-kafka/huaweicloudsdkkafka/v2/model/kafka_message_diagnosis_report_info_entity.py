# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaMessageDiagnosisReportInfoEntity:

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
        'group_name': 'str',
        'topic_name': 'str',
        'accumulated_partitions': 'int'
    }

    attribute_map = {
        'report_id': 'report_id',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'group_name': 'group_name',
        'topic_name': 'topic_name',
        'accumulated_partitions': 'accumulated_partitions'
    }

    def __init__(self, report_id=None, status=None, begin_time=None, end_time=None, group_name=None, topic_name=None, accumulated_partitions=None):
        r"""KafkaMessageDiagnosisReportInfoEntity

        The model defined in huaweicloud sdk

        :param report_id: 诊断报告ID
        :type report_id: str
        :param status: 消息积压诊断任务状态。 - diagnosing：诊断中 - failed：诊断失败 - deleted：手动删除 - finished：诊断完成 - normal：诊断结果正常 - abnormal：诊断结果异常
        :type status: str
        :param begin_time: 诊断任务开始时间
        :type begin_time: str
        :param end_time: 诊断任务结束时间
        :type end_time: str
        :param group_name: 该次诊断任务诊断的消费组名称
        :type group_name: str
        :param topic_name: 该次诊断任务诊断的Topic名称
        :type topic_name: str
        :param accumulated_partitions: 该次诊断任务发现的存在消息堆积的分区数
        :type accumulated_partitions: int
        """
        
        

        self._report_id = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._group_name = None
        self._topic_name = None
        self._accumulated_partitions = None
        self.discriminator = None

        self.report_id = report_id
        self.status = status
        self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        self.group_name = group_name
        self.topic_name = topic_name
        self.accumulated_partitions = accumulated_partitions

    @property
    def report_id(self):
        r"""Gets the report_id of this KafkaMessageDiagnosisReportInfoEntity.

        诊断报告ID

        :return: The report_id of this KafkaMessageDiagnosisReportInfoEntity.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this KafkaMessageDiagnosisReportInfoEntity.

        诊断报告ID

        :param report_id: The report_id of this KafkaMessageDiagnosisReportInfoEntity.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def status(self):
        r"""Gets the status of this KafkaMessageDiagnosisReportInfoEntity.

        消息积压诊断任务状态。 - diagnosing：诊断中 - failed：诊断失败 - deleted：手动删除 - finished：诊断完成 - normal：诊断结果正常 - abnormal：诊断结果异常

        :return: The status of this KafkaMessageDiagnosisReportInfoEntity.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this KafkaMessageDiagnosisReportInfoEntity.

        消息积压诊断任务状态。 - diagnosing：诊断中 - failed：诊断失败 - deleted：手动删除 - finished：诊断完成 - normal：诊断结果正常 - abnormal：诊断结果异常

        :param status: The status of this KafkaMessageDiagnosisReportInfoEntity.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this KafkaMessageDiagnosisReportInfoEntity.

        诊断任务开始时间

        :return: The begin_time of this KafkaMessageDiagnosisReportInfoEntity.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this KafkaMessageDiagnosisReportInfoEntity.

        诊断任务开始时间

        :param begin_time: The begin_time of this KafkaMessageDiagnosisReportInfoEntity.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this KafkaMessageDiagnosisReportInfoEntity.

        诊断任务结束时间

        :return: The end_time of this KafkaMessageDiagnosisReportInfoEntity.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this KafkaMessageDiagnosisReportInfoEntity.

        诊断任务结束时间

        :param end_time: The end_time of this KafkaMessageDiagnosisReportInfoEntity.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def group_name(self):
        r"""Gets the group_name of this KafkaMessageDiagnosisReportInfoEntity.

        该次诊断任务诊断的消费组名称

        :return: The group_name of this KafkaMessageDiagnosisReportInfoEntity.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this KafkaMessageDiagnosisReportInfoEntity.

        该次诊断任务诊断的消费组名称

        :param group_name: The group_name of this KafkaMessageDiagnosisReportInfoEntity.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def topic_name(self):
        r"""Gets the topic_name of this KafkaMessageDiagnosisReportInfoEntity.

        该次诊断任务诊断的Topic名称

        :return: The topic_name of this KafkaMessageDiagnosisReportInfoEntity.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        r"""Sets the topic_name of this KafkaMessageDiagnosisReportInfoEntity.

        该次诊断任务诊断的Topic名称

        :param topic_name: The topic_name of this KafkaMessageDiagnosisReportInfoEntity.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def accumulated_partitions(self):
        r"""Gets the accumulated_partitions of this KafkaMessageDiagnosisReportInfoEntity.

        该次诊断任务发现的存在消息堆积的分区数

        :return: The accumulated_partitions of this KafkaMessageDiagnosisReportInfoEntity.
        :rtype: int
        """
        return self._accumulated_partitions

    @accumulated_partitions.setter
    def accumulated_partitions(self, accumulated_partitions):
        r"""Sets the accumulated_partitions of this KafkaMessageDiagnosisReportInfoEntity.

        该次诊断任务发现的存在消息堆积的分区数

        :param accumulated_partitions: The accumulated_partitions of this KafkaMessageDiagnosisReportInfoEntity.
        :type accumulated_partitions: int
        """
        self._accumulated_partitions = accumulated_partitions

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
        if not isinstance(other, KafkaMessageDiagnosisReportInfoEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
