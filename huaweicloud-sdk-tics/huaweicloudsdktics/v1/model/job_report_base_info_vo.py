# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobReportBaseInfoVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exe_time': 'datetime',
        'executor': 'str',
        'hfl_type': 'str',
        'job_name': 'str',
        'job_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'exe_time': 'exe_time',
        'executor': 'executor',
        'hfl_type': 'hfl_type',
        'job_name': 'job_name',
        'job_type': 'job_type',
        'status': 'status'
    }

    def __init__(self, exe_time=None, executor=None, hfl_type=None, job_name=None, job_type=None, status=None):
        """JobReportBaseInfoVo

        The model defined in huaweicloud sdk

        :param exe_time: 执行时间
        :type exe_time: datetime
        :param executor: 执行人
        :type executor: str
        :param hfl_type: hfl作业类型枚举，TRAIN.训练,EVALUATE.评估
        :type hfl_type: str
        :param job_name: 作业名称
        :type job_name: str
        :param job_type: 作业类型，HFL.横向联邦，SQL.联邦分析，VFL_EVALUATE.联邦评估，VFL_FEATURE_SELECTION.特征选择，VFL_ID_TRUNCATION.Id截断，VFL_PREDICT.联邦预测，VFL_SAMPLE_ALIGNMENT.样本对齐，VFL_TRAIN.联邦训练
        :type job_type: str
        :param status: 作业任务状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中
        :type status: str
        """
        
        

        self._exe_time = None
        self._executor = None
        self._hfl_type = None
        self._job_name = None
        self._job_type = None
        self._status = None
        self.discriminator = None

        if exe_time is not None:
            self.exe_time = exe_time
        if executor is not None:
            self.executor = executor
        self.hfl_type = hfl_type
        self.job_name = job_name
        self.job_type = job_type
        self.status = status

    @property
    def exe_time(self):
        """Gets the exe_time of this JobReportBaseInfoVo.

        执行时间

        :return: The exe_time of this JobReportBaseInfoVo.
        :rtype: datetime
        """
        return self._exe_time

    @exe_time.setter
    def exe_time(self, exe_time):
        """Sets the exe_time of this JobReportBaseInfoVo.

        执行时间

        :param exe_time: The exe_time of this JobReportBaseInfoVo.
        :type exe_time: datetime
        """
        self._exe_time = exe_time

    @property
    def executor(self):
        """Gets the executor of this JobReportBaseInfoVo.

        执行人

        :return: The executor of this JobReportBaseInfoVo.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this JobReportBaseInfoVo.

        执行人

        :param executor: The executor of this JobReportBaseInfoVo.
        :type executor: str
        """
        self._executor = executor

    @property
    def hfl_type(self):
        """Gets the hfl_type of this JobReportBaseInfoVo.

        hfl作业类型枚举，TRAIN.训练,EVALUATE.评估

        :return: The hfl_type of this JobReportBaseInfoVo.
        :rtype: str
        """
        return self._hfl_type

    @hfl_type.setter
    def hfl_type(self, hfl_type):
        """Sets the hfl_type of this JobReportBaseInfoVo.

        hfl作业类型枚举，TRAIN.训练,EVALUATE.评估

        :param hfl_type: The hfl_type of this JobReportBaseInfoVo.
        :type hfl_type: str
        """
        self._hfl_type = hfl_type

    @property
    def job_name(self):
        """Gets the job_name of this JobReportBaseInfoVo.

        作业名称

        :return: The job_name of this JobReportBaseInfoVo.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobReportBaseInfoVo.

        作业名称

        :param job_name: The job_name of this JobReportBaseInfoVo.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        """Gets the job_type of this JobReportBaseInfoVo.

        作业类型，HFL.横向联邦，SQL.联邦分析，VFL_EVALUATE.联邦评估，VFL_FEATURE_SELECTION.特征选择，VFL_ID_TRUNCATION.Id截断，VFL_PREDICT.联邦预测，VFL_SAMPLE_ALIGNMENT.样本对齐，VFL_TRAIN.联邦训练

        :return: The job_type of this JobReportBaseInfoVo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobReportBaseInfoVo.

        作业类型，HFL.横向联邦，SQL.联邦分析，VFL_EVALUATE.联邦评估，VFL_FEATURE_SELECTION.特征选择，VFL_ID_TRUNCATION.Id截断，VFL_PREDICT.联邦预测，VFL_SAMPLE_ALIGNMENT.样本对齐，VFL_TRAIN.联邦训练

        :param job_type: The job_type of this JobReportBaseInfoVo.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        """Gets the status of this JobReportBaseInfoVo.

        作业任务状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中

        :return: The status of this JobReportBaseInfoVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobReportBaseInfoVo.

        作业任务状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中

        :param status: The status of this JobReportBaseInfoVo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, JobReportBaseInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
