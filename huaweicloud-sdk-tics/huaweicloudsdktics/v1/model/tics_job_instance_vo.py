# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsJobInstanceVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_time': 'datetime',
        'ext': 'str',
        'id': 'str',
        'is_single_predict': 'bool',
        'job_instance_type': 'str',
        'job_name': 'str',
        'job_partner': 'str',
        'result_ext': 'str',
        'round_id': 'int',
        'start_time': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'end_time': 'end_time',
        'ext': 'ext',
        'id': 'id',
        'is_single_predict': 'is_single_predict',
        'job_instance_type': 'job_instance_type',
        'job_name': 'job_name',
        'job_partner': 'job_partner',
        'result_ext': 'result_ext',
        'round_id': 'round_id',
        'start_time': 'start_time',
        'status': 'status'
    }

    def __init__(self, end_time=None, ext=None, id=None, is_single_predict=None, job_instance_type=None, job_name=None, job_partner=None, result_ext=None, round_id=None, start_time=None, status=None):
        """TicsJobInstanceVo

        The model defined in huaweicloud sdk

        :param end_time: 结束时间
        :type end_time: datetime
        :param ext: 参数等额外信息
        :type ext: str
        :param id: 实例id
        :type id: str
        :param is_single_predict: 单方还是双方预测
        :type is_single_predict: bool
        :param job_instance_type: 作业类型，HFL.横向联邦，SQL.联邦分析，VFL_EVALUATE.联邦评估，VFL_FEATURE_SELECTION.特征选择，VFL_ID_TRUNCATION.Id截断，VFL_PREDICT.联邦预测，VFL_SAMPLE_ALIGNMENT.样本对齐，VFL_TRAIN.联邦训练
        :type job_instance_type: str
        :param job_name: 作业名称
        :type job_name: str
        :param job_partner: 参与方信息
        :type job_partner: str
        :param result_ext: 参数等额外信息
        :type result_ext: str
        :param round_id: 作业执行总轮数
        :type round_id: int
        :param start_time: 开始时间
        :type start_time: datetime
        :param status: 作业、任务状态，作业任务状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中
        :type status: str
        """
        
        

        self._end_time = None
        self._ext = None
        self._id = None
        self._is_single_predict = None
        self._job_instance_type = None
        self._job_name = None
        self._job_partner = None
        self._result_ext = None
        self._round_id = None
        self._start_time = None
        self._status = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if ext is not None:
            self.ext = ext
        self.id = id
        if is_single_predict is not None:
            self.is_single_predict = is_single_predict
        self.job_instance_type = job_instance_type
        self.job_name = job_name
        if job_partner is not None:
            self.job_partner = job_partner
        if result_ext is not None:
            self.result_ext = result_ext
        if round_id is not None:
            self.round_id = round_id
        if start_time is not None:
            self.start_time = start_time
        self.status = status

    @property
    def end_time(self):
        """Gets the end_time of this TicsJobInstanceVo.

        结束时间

        :return: The end_time of this TicsJobInstanceVo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TicsJobInstanceVo.

        结束时间

        :param end_time: The end_time of this TicsJobInstanceVo.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def ext(self):
        """Gets the ext of this TicsJobInstanceVo.

        参数等额外信息

        :return: The ext of this TicsJobInstanceVo.
        :rtype: str
        """
        return self._ext

    @ext.setter
    def ext(self, ext):
        """Sets the ext of this TicsJobInstanceVo.

        参数等额外信息

        :param ext: The ext of this TicsJobInstanceVo.
        :type ext: str
        """
        self._ext = ext

    @property
    def id(self):
        """Gets the id of this TicsJobInstanceVo.

        实例id

        :return: The id of this TicsJobInstanceVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TicsJobInstanceVo.

        实例id

        :param id: The id of this TicsJobInstanceVo.
        :type id: str
        """
        self._id = id

    @property
    def is_single_predict(self):
        """Gets the is_single_predict of this TicsJobInstanceVo.

        单方还是双方预测

        :return: The is_single_predict of this TicsJobInstanceVo.
        :rtype: bool
        """
        return self._is_single_predict

    @is_single_predict.setter
    def is_single_predict(self, is_single_predict):
        """Sets the is_single_predict of this TicsJobInstanceVo.

        单方还是双方预测

        :param is_single_predict: The is_single_predict of this TicsJobInstanceVo.
        :type is_single_predict: bool
        """
        self._is_single_predict = is_single_predict

    @property
    def job_instance_type(self):
        """Gets the job_instance_type of this TicsJobInstanceVo.

        作业类型，HFL.横向联邦，SQL.联邦分析，VFL_EVALUATE.联邦评估，VFL_FEATURE_SELECTION.特征选择，VFL_ID_TRUNCATION.Id截断，VFL_PREDICT.联邦预测，VFL_SAMPLE_ALIGNMENT.样本对齐，VFL_TRAIN.联邦训练

        :return: The job_instance_type of this TicsJobInstanceVo.
        :rtype: str
        """
        return self._job_instance_type

    @job_instance_type.setter
    def job_instance_type(self, job_instance_type):
        """Sets the job_instance_type of this TicsJobInstanceVo.

        作业类型，HFL.横向联邦，SQL.联邦分析，VFL_EVALUATE.联邦评估，VFL_FEATURE_SELECTION.特征选择，VFL_ID_TRUNCATION.Id截断，VFL_PREDICT.联邦预测，VFL_SAMPLE_ALIGNMENT.样本对齐，VFL_TRAIN.联邦训练

        :param job_instance_type: The job_instance_type of this TicsJobInstanceVo.
        :type job_instance_type: str
        """
        self._job_instance_type = job_instance_type

    @property
    def job_name(self):
        """Gets the job_name of this TicsJobInstanceVo.

        作业名称

        :return: The job_name of this TicsJobInstanceVo.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this TicsJobInstanceVo.

        作业名称

        :param job_name: The job_name of this TicsJobInstanceVo.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_partner(self):
        """Gets the job_partner of this TicsJobInstanceVo.

        参与方信息

        :return: The job_partner of this TicsJobInstanceVo.
        :rtype: str
        """
        return self._job_partner

    @job_partner.setter
    def job_partner(self, job_partner):
        """Sets the job_partner of this TicsJobInstanceVo.

        参与方信息

        :param job_partner: The job_partner of this TicsJobInstanceVo.
        :type job_partner: str
        """
        self._job_partner = job_partner

    @property
    def result_ext(self):
        """Gets the result_ext of this TicsJobInstanceVo.

        参数等额外信息

        :return: The result_ext of this TicsJobInstanceVo.
        :rtype: str
        """
        return self._result_ext

    @result_ext.setter
    def result_ext(self, result_ext):
        """Sets the result_ext of this TicsJobInstanceVo.

        参数等额外信息

        :param result_ext: The result_ext of this TicsJobInstanceVo.
        :type result_ext: str
        """
        self._result_ext = result_ext

    @property
    def round_id(self):
        """Gets the round_id of this TicsJobInstanceVo.

        作业执行总轮数

        :return: The round_id of this TicsJobInstanceVo.
        :rtype: int
        """
        return self._round_id

    @round_id.setter
    def round_id(self, round_id):
        """Sets the round_id of this TicsJobInstanceVo.

        作业执行总轮数

        :param round_id: The round_id of this TicsJobInstanceVo.
        :type round_id: int
        """
        self._round_id = round_id

    @property
    def start_time(self):
        """Gets the start_time of this TicsJobInstanceVo.

        开始时间

        :return: The start_time of this TicsJobInstanceVo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TicsJobInstanceVo.

        开始时间

        :param start_time: The start_time of this TicsJobInstanceVo.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this TicsJobInstanceVo.

        作业、任务状态，作业任务状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中

        :return: The status of this TicsJobInstanceVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TicsJobInstanceVo.

        作业、任务状态，作业任务状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中

        :param status: The status of this TicsJobInstanceVo.
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
        if not isinstance(other, TicsJobInstanceVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
