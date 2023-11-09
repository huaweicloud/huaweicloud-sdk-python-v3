# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlJobListVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm_type': 'str',
        'approval_status': 'str',
        'create_time': 'datetime',
        'creator_name': 'str',
        'description': 'str',
        'ext': 'str',
        'hfl_platform_type': 'str',
        'hfl_type': 'str',
        'is_single_predict': 'bool',
        'job_id': 'str',
        'job_name': 'str',
        'job_type': 'str',
        'learning_task_type': 'str'
    }

    attribute_map = {
        'algorithm_type': 'algorithm_type',
        'approval_status': 'approval_status',
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'description': 'description',
        'ext': 'ext',
        'hfl_platform_type': 'hfl_platform_type',
        'hfl_type': 'hfl_type',
        'is_single_predict': 'is_single_predict',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'job_type': 'job_type',
        'learning_task_type': 'learning_task_type'
    }

    def __init__(self, algorithm_type=None, approval_status=None, create_time=None, creator_name=None, description=None, ext=None, hfl_platform_type=None, hfl_type=None, is_single_predict=None, job_id=None, job_name=None, job_type=None, learning_task_type=None):
        """FlJobListVo

        The model defined in huaweicloud sdk

        :param algorithm_type: 纵向联邦算法类型枚举，XG_BOOST.XGBoost,LIGHT_BGM.LightGBM,LOGISTIC_REGRESSION.逻辑回归,NEURAL_NETWORK.神经网络，FIBINET.FIBINET
        :type algorithm_type: str
        :param approval_status: fl作业审批状态，APPROVED.审批通过，APPROVING.审批中，NEW.新建，REJECTED.驳回，REVOKED.撤销
        :type approval_status: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param creator_name: 创建人名称
        :type creator_name: str
        :param description: 作业描述
        :type description: str
        :param ext: 参数等额外信息
        :type ext: str
        :param hfl_platform_type: 联邦学习运行平台枚举值，LOCAL.本地
        :type hfl_platform_type: str
        :param hfl_type: fl作业类型枚举,TRAIN.训练,EVALUATE.评估
        :type hfl_type: str
        :param is_single_predict: 单方还是双方预测
        :type is_single_predict: bool
        :param job_id: 作业id
        :type job_id: str
        :param job_name: 作业名称
        :type job_name: str
        :param job_type: 作业类型,SQL.联合SQL分析,HFL.横向联邦学习,VFL.纵向联邦学习,PREDICT.预测，DATA_EXCHANGE.数据交换
        :type job_type: str
        :param learning_task_type: 纵向联邦任务类型,CLASSIFICATION.分类，REGRESSION.拟合
        :type learning_task_type: str
        """
        
        

        self._algorithm_type = None
        self._approval_status = None
        self._create_time = None
        self._creator_name = None
        self._description = None
        self._ext = None
        self._hfl_platform_type = None
        self._hfl_type = None
        self._is_single_predict = None
        self._job_id = None
        self._job_name = None
        self._job_type = None
        self._learning_task_type = None
        self.discriminator = None

        if algorithm_type is not None:
            self.algorithm_type = algorithm_type
        if approval_status is not None:
            self.approval_status = approval_status
        self.create_time = create_time
        self.creator_name = creator_name
        if description is not None:
            self.description = description
        if ext is not None:
            self.ext = ext
        self.hfl_platform_type = hfl_platform_type
        self.hfl_type = hfl_type
        if is_single_predict is not None:
            self.is_single_predict = is_single_predict
        self.job_id = job_id
        self.job_name = job_name
        if job_type is not None:
            self.job_type = job_type
        if learning_task_type is not None:
            self.learning_task_type = learning_task_type

    @property
    def algorithm_type(self):
        """Gets the algorithm_type of this FlJobListVo.

        纵向联邦算法类型枚举，XG_BOOST.XGBoost,LIGHT_BGM.LightGBM,LOGISTIC_REGRESSION.逻辑回归,NEURAL_NETWORK.神经网络，FIBINET.FIBINET

        :return: The algorithm_type of this FlJobListVo.
        :rtype: str
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        """Sets the algorithm_type of this FlJobListVo.

        纵向联邦算法类型枚举，XG_BOOST.XGBoost,LIGHT_BGM.LightGBM,LOGISTIC_REGRESSION.逻辑回归,NEURAL_NETWORK.神经网络，FIBINET.FIBINET

        :param algorithm_type: The algorithm_type of this FlJobListVo.
        :type algorithm_type: str
        """
        self._algorithm_type = algorithm_type

    @property
    def approval_status(self):
        """Gets the approval_status of this FlJobListVo.

        fl作业审批状态，APPROVED.审批通过，APPROVING.审批中，NEW.新建，REJECTED.驳回，REVOKED.撤销

        :return: The approval_status of this FlJobListVo.
        :rtype: str
        """
        return self._approval_status

    @approval_status.setter
    def approval_status(self, approval_status):
        """Sets the approval_status of this FlJobListVo.

        fl作业审批状态，APPROVED.审批通过，APPROVING.审批中，NEW.新建，REJECTED.驳回，REVOKED.撤销

        :param approval_status: The approval_status of this FlJobListVo.
        :type approval_status: str
        """
        self._approval_status = approval_status

    @property
    def create_time(self):
        """Gets the create_time of this FlJobListVo.

        创建时间

        :return: The create_time of this FlJobListVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FlJobListVo.

        创建时间

        :param create_time: The create_time of this FlJobListVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        """Gets the creator_name of this FlJobListVo.

        创建人名称

        :return: The creator_name of this FlJobListVo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this FlJobListVo.

        创建人名称

        :param creator_name: The creator_name of this FlJobListVo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def description(self):
        """Gets the description of this FlJobListVo.

        作业描述

        :return: The description of this FlJobListVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FlJobListVo.

        作业描述

        :param description: The description of this FlJobListVo.
        :type description: str
        """
        self._description = description

    @property
    def ext(self):
        """Gets the ext of this FlJobListVo.

        参数等额外信息

        :return: The ext of this FlJobListVo.
        :rtype: str
        """
        return self._ext

    @ext.setter
    def ext(self, ext):
        """Sets the ext of this FlJobListVo.

        参数等额外信息

        :param ext: The ext of this FlJobListVo.
        :type ext: str
        """
        self._ext = ext

    @property
    def hfl_platform_type(self):
        """Gets the hfl_platform_type of this FlJobListVo.

        联邦学习运行平台枚举值，LOCAL.本地

        :return: The hfl_platform_type of this FlJobListVo.
        :rtype: str
        """
        return self._hfl_platform_type

    @hfl_platform_type.setter
    def hfl_platform_type(self, hfl_platform_type):
        """Sets the hfl_platform_type of this FlJobListVo.

        联邦学习运行平台枚举值，LOCAL.本地

        :param hfl_platform_type: The hfl_platform_type of this FlJobListVo.
        :type hfl_platform_type: str
        """
        self._hfl_platform_type = hfl_platform_type

    @property
    def hfl_type(self):
        """Gets the hfl_type of this FlJobListVo.

        fl作业类型枚举,TRAIN.训练,EVALUATE.评估

        :return: The hfl_type of this FlJobListVo.
        :rtype: str
        """
        return self._hfl_type

    @hfl_type.setter
    def hfl_type(self, hfl_type):
        """Sets the hfl_type of this FlJobListVo.

        fl作业类型枚举,TRAIN.训练,EVALUATE.评估

        :param hfl_type: The hfl_type of this FlJobListVo.
        :type hfl_type: str
        """
        self._hfl_type = hfl_type

    @property
    def is_single_predict(self):
        """Gets the is_single_predict of this FlJobListVo.

        单方还是双方预测

        :return: The is_single_predict of this FlJobListVo.
        :rtype: bool
        """
        return self._is_single_predict

    @is_single_predict.setter
    def is_single_predict(self, is_single_predict):
        """Sets the is_single_predict of this FlJobListVo.

        单方还是双方预测

        :param is_single_predict: The is_single_predict of this FlJobListVo.
        :type is_single_predict: bool
        """
        self._is_single_predict = is_single_predict

    @property
    def job_id(self):
        """Gets the job_id of this FlJobListVo.

        作业id

        :return: The job_id of this FlJobListVo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this FlJobListVo.

        作业id

        :param job_id: The job_id of this FlJobListVo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this FlJobListVo.

        作业名称

        :return: The job_name of this FlJobListVo.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this FlJobListVo.

        作业名称

        :param job_name: The job_name of this FlJobListVo.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        """Gets the job_type of this FlJobListVo.

        作业类型,SQL.联合SQL分析,HFL.横向联邦学习,VFL.纵向联邦学习,PREDICT.预测，DATA_EXCHANGE.数据交换

        :return: The job_type of this FlJobListVo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this FlJobListVo.

        作业类型,SQL.联合SQL分析,HFL.横向联邦学习,VFL.纵向联邦学习,PREDICT.预测，DATA_EXCHANGE.数据交换

        :param job_type: The job_type of this FlJobListVo.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def learning_task_type(self):
        """Gets the learning_task_type of this FlJobListVo.

        纵向联邦任务类型,CLASSIFICATION.分类，REGRESSION.拟合

        :return: The learning_task_type of this FlJobListVo.
        :rtype: str
        """
        return self._learning_task_type

    @learning_task_type.setter
    def learning_task_type(self, learning_task_type):
        """Sets the learning_task_type of this FlJobListVo.

        纵向联邦任务类型,CLASSIFICATION.分类，REGRESSION.拟合

        :param learning_task_type: The learning_task_type of this FlJobListVo.
        :type learning_task_type: str
        """
        self._learning_task_type = learning_task_type

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
        if not isinstance(other, FlJobListVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
