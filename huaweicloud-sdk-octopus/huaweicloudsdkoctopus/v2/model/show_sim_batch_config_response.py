# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSimBatchConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'id': 'int',
        'created_at': 'float',
        'updated_at': 'float',
        'scenarios': 'BatchConfigScenarioSrlz',
        'msg_notify_method': 'BatchConfigMsgNotifySrlz',
        'algorithm': 'str',
        'algorithm_name': 'str',
        'builtins_evaluation': 'bool',
        'custom_evaluation_image': 'str',
        'custom_simulator_image_id': 'int',
        'evaluation_info': 'BatchConfigEvaluationInfoSrlz',
        'batch_size': 'int',
        'duration': 'str',
        'repeat_times': 'int',
        'name': 'str',
        'description': 'str',
        'simulator_name': 'str',
        'record_mode': 'RecordModeEnum',
        'priority': 'PriorityEnum',
        'datahub': 'bool',
        'passing_score': 'int',
        'scenario_type': 'int',
        'scenario_set_id': 'int',
        'triggerable': 'bool',
        'evaluations': 'list[str]'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'scenarios': 'scenarios',
        'msg_notify_method': 'msg_notify_method',
        'algorithm': 'algorithm',
        'algorithm_name': 'algorithm_name',
        'builtins_evaluation': 'builtins_evaluation',
        'custom_evaluation_image': 'custom_evaluation_image',
        'custom_simulator_image_id': 'custom_simulator_image_id',
        'evaluation_info': 'evaluation_info',
        'batch_size': 'batch_size',
        'duration': 'duration',
        'repeat_times': 'repeat_times',
        'name': 'name',
        'description': 'description',
        'simulator_name': 'simulator_name',
        'record_mode': 'record_mode',
        'priority': 'priority',
        'datahub': 'datahub',
        'passing_score': 'passing_score',
        'scenario_type': 'scenario_type',
        'scenario_set_id': 'scenario_set_id',
        'triggerable': 'triggerable',
        'evaluations': 'evaluations'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, scenarios=None, msg_notify_method=None, algorithm=None, algorithm_name=None, builtins_evaluation=None, custom_evaluation_image=None, custom_simulator_image_id=None, evaluation_info=None, batch_size=None, duration=None, repeat_times=None, name=None, description=None, simulator_name=None, record_mode=None, priority=None, datahub=None, passing_score=None, scenario_type=None, scenario_set_id=None, triggerable=None, evaluations=None):
        r"""ShowSimBatchConfigResponse

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param id: 
        :type id: int
        :param created_at: 
        :type created_at: float
        :param updated_at: 
        :type updated_at: float
        :param scenarios: 场景信息
        :type scenarios: :class:`huaweicloudsdkoctopus.v2.BatchConfigScenarioSrlz`
        :param msg_notify_method: 消息通知
        :type msg_notify_method: :class:`huaweicloudsdkoctopus.v2.BatchConfigMsgNotifySrlz`
        :param algorithm: 关联算法项目
        :type algorithm: str
        :param algorithm_name: 算法名称
        :type algorithm_name: str
        :param builtins_evaluation: 是否使用内置评测
        :type builtins_evaluation: bool
        :param custom_evaluation_image: 关联评测镜像
        :type custom_evaluation_image: str
        :param custom_simulator_image_id: 镜像管理中的仿真器镜像的版本id
        :type custom_simulator_image_id: int
        :param evaluation_info: 评测配置信息
        :type evaluation_info: :class:`huaweicloudsdkoctopus.v2.BatchConfigEvaluationInfoSrlz`
        :param batch_size: 任务数量
        :type batch_size: int
        :param duration: 子任务最大运行时长
        :type duration: str
        :param repeat_times: 重复运行次数
        :type repeat_times: int
        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param simulator_name: 仿真器名称,取值范围:A,B,C,D,E
        :type simulator_name: str
        :param record_mode: 录制模式  * &#x60;0&#x60; - 不录制 * &#x60;1&#x60; - 录制
        :type record_mode: :class:`huaweicloudsdkoctopus.v2.RecordModeEnum`
        :param priority: 优先级,取值越大，优先级越高。  * &#x60;120&#x60; - S * &#x60;100&#x60; - A * &#x60;80&#x60; - B * &#x60;60&#x60; - C * &#x60;40&#x60; - D
        :type priority: :class:`huaweicloudsdkoctopus.v2.PriorityEnum`
        :param datahub: 是否使用datahub
        :type datahub: bool
        :param passing_score: 融合评测通过分数
        :type passing_score: int
        :param scenario_type: 场景资源类型
        :type scenario_type: int
        :param scenario_set_id: 景资源组ID
        :type scenario_set_id: int
        :param triggerable: 是否可通过流水线功能触发
        :type triggerable: bool
        :param evaluations: 关联评测管理项目
        :type evaluations: list[str]
        """
        
        super(ShowSimBatchConfigResponse, self).__init__()

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._scenarios = None
        self._msg_notify_method = None
        self._algorithm = None
        self._algorithm_name = None
        self._builtins_evaluation = None
        self._custom_evaluation_image = None
        self._custom_simulator_image_id = None
        self._evaluation_info = None
        self._batch_size = None
        self._duration = None
        self._repeat_times = None
        self._name = None
        self._description = None
        self._simulator_name = None
        self._record_mode = None
        self._priority = None
        self._datahub = None
        self._passing_score = None
        self._scenario_type = None
        self._scenario_set_id = None
        self._triggerable = None
        self._evaluations = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if scenarios is not None:
            self.scenarios = scenarios
        self.msg_notify_method = msg_notify_method
        self.algorithm = algorithm
        if algorithm_name is not None:
            self.algorithm_name = algorithm_name
        if builtins_evaluation is not None:
            self.builtins_evaluation = builtins_evaluation
        self.custom_evaluation_image = custom_evaluation_image
        self.custom_simulator_image_id = custom_simulator_image_id
        if evaluation_info is not None:
            self.evaluation_info = evaluation_info
        if batch_size is not None:
            self.batch_size = batch_size
        if duration is not None:
            self.duration = duration
        if repeat_times is not None:
            self.repeat_times = repeat_times
        if name is not None:
            self.name = name
        self.description = description
        if simulator_name is not None:
            self.simulator_name = simulator_name
        if record_mode is not None:
            self.record_mode = record_mode
        if priority is not None:
            self.priority = priority
        self.datahub = datahub
        if passing_score is not None:
            self.passing_score = passing_score
        if scenario_type is not None:
            self.scenario_type = scenario_type
        if scenario_set_id is not None:
            self.scenario_set_id = scenario_set_id
        if triggerable is not None:
            self.triggerable = triggerable
        if evaluations is not None:
            self.evaluations = evaluations

    @property
    def url(self):
        r"""Gets the url of this ShowSimBatchConfigResponse.

        :return: The url of this ShowSimBatchConfigResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowSimBatchConfigResponse.

        :param url: The url of this ShowSimBatchConfigResponse.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this ShowSimBatchConfigResponse.

        :return: The id of this ShowSimBatchConfigResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSimBatchConfigResponse.

        :param id: The id of this ShowSimBatchConfigResponse.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowSimBatchConfigResponse.

        :return: The created_at of this ShowSimBatchConfigResponse.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowSimBatchConfigResponse.

        :param created_at: The created_at of this ShowSimBatchConfigResponse.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowSimBatchConfigResponse.

        :return: The updated_at of this ShowSimBatchConfigResponse.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowSimBatchConfigResponse.

        :param updated_at: The updated_at of this ShowSimBatchConfigResponse.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def scenarios(self):
        r"""Gets the scenarios of this ShowSimBatchConfigResponse.

        场景信息

        :return: The scenarios of this ShowSimBatchConfigResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.BatchConfigScenarioSrlz`
        """
        return self._scenarios

    @scenarios.setter
    def scenarios(self, scenarios):
        r"""Sets the scenarios of this ShowSimBatchConfigResponse.

        场景信息

        :param scenarios: The scenarios of this ShowSimBatchConfigResponse.
        :type scenarios: :class:`huaweicloudsdkoctopus.v2.BatchConfigScenarioSrlz`
        """
        self._scenarios = scenarios

    @property
    def msg_notify_method(self):
        r"""Gets the msg_notify_method of this ShowSimBatchConfigResponse.

        消息通知

        :return: The msg_notify_method of this ShowSimBatchConfigResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.BatchConfigMsgNotifySrlz`
        """
        return self._msg_notify_method

    @msg_notify_method.setter
    def msg_notify_method(self, msg_notify_method):
        r"""Sets the msg_notify_method of this ShowSimBatchConfigResponse.

        消息通知

        :param msg_notify_method: The msg_notify_method of this ShowSimBatchConfigResponse.
        :type msg_notify_method: :class:`huaweicloudsdkoctopus.v2.BatchConfigMsgNotifySrlz`
        """
        self._msg_notify_method = msg_notify_method

    @property
    def algorithm(self):
        r"""Gets the algorithm of this ShowSimBatchConfigResponse.

        关联算法项目

        :return: The algorithm of this ShowSimBatchConfigResponse.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this ShowSimBatchConfigResponse.

        关联算法项目

        :param algorithm: The algorithm of this ShowSimBatchConfigResponse.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def algorithm_name(self):
        r"""Gets the algorithm_name of this ShowSimBatchConfigResponse.

        算法名称

        :return: The algorithm_name of this ShowSimBatchConfigResponse.
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        r"""Sets the algorithm_name of this ShowSimBatchConfigResponse.

        算法名称

        :param algorithm_name: The algorithm_name of this ShowSimBatchConfigResponse.
        :type algorithm_name: str
        """
        self._algorithm_name = algorithm_name

    @property
    def builtins_evaluation(self):
        r"""Gets the builtins_evaluation of this ShowSimBatchConfigResponse.

        是否使用内置评测

        :return: The builtins_evaluation of this ShowSimBatchConfigResponse.
        :rtype: bool
        """
        return self._builtins_evaluation

    @builtins_evaluation.setter
    def builtins_evaluation(self, builtins_evaluation):
        r"""Sets the builtins_evaluation of this ShowSimBatchConfigResponse.

        是否使用内置评测

        :param builtins_evaluation: The builtins_evaluation of this ShowSimBatchConfigResponse.
        :type builtins_evaluation: bool
        """
        self._builtins_evaluation = builtins_evaluation

    @property
    def custom_evaluation_image(self):
        r"""Gets the custom_evaluation_image of this ShowSimBatchConfigResponse.

        关联评测镜像

        :return: The custom_evaluation_image of this ShowSimBatchConfigResponse.
        :rtype: str
        """
        return self._custom_evaluation_image

    @custom_evaluation_image.setter
    def custom_evaluation_image(self, custom_evaluation_image):
        r"""Sets the custom_evaluation_image of this ShowSimBatchConfigResponse.

        关联评测镜像

        :param custom_evaluation_image: The custom_evaluation_image of this ShowSimBatchConfigResponse.
        :type custom_evaluation_image: str
        """
        self._custom_evaluation_image = custom_evaluation_image

    @property
    def custom_simulator_image_id(self):
        r"""Gets the custom_simulator_image_id of this ShowSimBatchConfigResponse.

        镜像管理中的仿真器镜像的版本id

        :return: The custom_simulator_image_id of this ShowSimBatchConfigResponse.
        :rtype: int
        """
        return self._custom_simulator_image_id

    @custom_simulator_image_id.setter
    def custom_simulator_image_id(self, custom_simulator_image_id):
        r"""Sets the custom_simulator_image_id of this ShowSimBatchConfigResponse.

        镜像管理中的仿真器镜像的版本id

        :param custom_simulator_image_id: The custom_simulator_image_id of this ShowSimBatchConfigResponse.
        :type custom_simulator_image_id: int
        """
        self._custom_simulator_image_id = custom_simulator_image_id

    @property
    def evaluation_info(self):
        r"""Gets the evaluation_info of this ShowSimBatchConfigResponse.

        评测配置信息

        :return: The evaluation_info of this ShowSimBatchConfigResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.BatchConfigEvaluationInfoSrlz`
        """
        return self._evaluation_info

    @evaluation_info.setter
    def evaluation_info(self, evaluation_info):
        r"""Sets the evaluation_info of this ShowSimBatchConfigResponse.

        评测配置信息

        :param evaluation_info: The evaluation_info of this ShowSimBatchConfigResponse.
        :type evaluation_info: :class:`huaweicloudsdkoctopus.v2.BatchConfigEvaluationInfoSrlz`
        """
        self._evaluation_info = evaluation_info

    @property
    def batch_size(self):
        r"""Gets the batch_size of this ShowSimBatchConfigResponse.

        任务数量

        :return: The batch_size of this ShowSimBatchConfigResponse.
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        r"""Sets the batch_size of this ShowSimBatchConfigResponse.

        任务数量

        :param batch_size: The batch_size of this ShowSimBatchConfigResponse.
        :type batch_size: int
        """
        self._batch_size = batch_size

    @property
    def duration(self):
        r"""Gets the duration of this ShowSimBatchConfigResponse.

        子任务最大运行时长

        :return: The duration of this ShowSimBatchConfigResponse.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ShowSimBatchConfigResponse.

        子任务最大运行时长

        :param duration: The duration of this ShowSimBatchConfigResponse.
        :type duration: str
        """
        self._duration = duration

    @property
    def repeat_times(self):
        r"""Gets the repeat_times of this ShowSimBatchConfigResponse.

        重复运行次数

        :return: The repeat_times of this ShowSimBatchConfigResponse.
        :rtype: int
        """
        return self._repeat_times

    @repeat_times.setter
    def repeat_times(self, repeat_times):
        r"""Sets the repeat_times of this ShowSimBatchConfigResponse.

        重复运行次数

        :param repeat_times: The repeat_times of this ShowSimBatchConfigResponse.
        :type repeat_times: int
        """
        self._repeat_times = repeat_times

    @property
    def name(self):
        r"""Gets the name of this ShowSimBatchConfigResponse.

        名称

        :return: The name of this ShowSimBatchConfigResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowSimBatchConfigResponse.

        名称

        :param name: The name of this ShowSimBatchConfigResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowSimBatchConfigResponse.

        描述

        :return: The description of this ShowSimBatchConfigResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowSimBatchConfigResponse.

        描述

        :param description: The description of this ShowSimBatchConfigResponse.
        :type description: str
        """
        self._description = description

    @property
    def simulator_name(self):
        r"""Gets the simulator_name of this ShowSimBatchConfigResponse.

        仿真器名称,取值范围:A,B,C,D,E

        :return: The simulator_name of this ShowSimBatchConfigResponse.
        :rtype: str
        """
        return self._simulator_name

    @simulator_name.setter
    def simulator_name(self, simulator_name):
        r"""Sets the simulator_name of this ShowSimBatchConfigResponse.

        仿真器名称,取值范围:A,B,C,D,E

        :param simulator_name: The simulator_name of this ShowSimBatchConfigResponse.
        :type simulator_name: str
        """
        self._simulator_name = simulator_name

    @property
    def record_mode(self):
        r"""Gets the record_mode of this ShowSimBatchConfigResponse.

        录制模式  * `0` - 不录制 * `1` - 录制

        :return: The record_mode of this ShowSimBatchConfigResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.RecordModeEnum`
        """
        return self._record_mode

    @record_mode.setter
    def record_mode(self, record_mode):
        r"""Sets the record_mode of this ShowSimBatchConfigResponse.

        录制模式  * `0` - 不录制 * `1` - 录制

        :param record_mode: The record_mode of this ShowSimBatchConfigResponse.
        :type record_mode: :class:`huaweicloudsdkoctopus.v2.RecordModeEnum`
        """
        self._record_mode = record_mode

    @property
    def priority(self):
        r"""Gets the priority of this ShowSimBatchConfigResponse.

        优先级,取值越大，优先级越高。  * `120` - S * `100` - A * `80` - B * `60` - C * `40` - D

        :return: The priority of this ShowSimBatchConfigResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.PriorityEnum`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ShowSimBatchConfigResponse.

        优先级,取值越大，优先级越高。  * `120` - S * `100` - A * `80` - B * `60` - C * `40` - D

        :param priority: The priority of this ShowSimBatchConfigResponse.
        :type priority: :class:`huaweicloudsdkoctopus.v2.PriorityEnum`
        """
        self._priority = priority

    @property
    def datahub(self):
        r"""Gets the datahub of this ShowSimBatchConfigResponse.

        是否使用datahub

        :return: The datahub of this ShowSimBatchConfigResponse.
        :rtype: bool
        """
        return self._datahub

    @datahub.setter
    def datahub(self, datahub):
        r"""Sets the datahub of this ShowSimBatchConfigResponse.

        是否使用datahub

        :param datahub: The datahub of this ShowSimBatchConfigResponse.
        :type datahub: bool
        """
        self._datahub = datahub

    @property
    def passing_score(self):
        r"""Gets the passing_score of this ShowSimBatchConfigResponse.

        融合评测通过分数

        :return: The passing_score of this ShowSimBatchConfigResponse.
        :rtype: int
        """
        return self._passing_score

    @passing_score.setter
    def passing_score(self, passing_score):
        r"""Sets the passing_score of this ShowSimBatchConfigResponse.

        融合评测通过分数

        :param passing_score: The passing_score of this ShowSimBatchConfigResponse.
        :type passing_score: int
        """
        self._passing_score = passing_score

    @property
    def scenario_type(self):
        r"""Gets the scenario_type of this ShowSimBatchConfigResponse.

        场景资源类型

        :return: The scenario_type of this ShowSimBatchConfigResponse.
        :rtype: int
        """
        return self._scenario_type

    @scenario_type.setter
    def scenario_type(self, scenario_type):
        r"""Sets the scenario_type of this ShowSimBatchConfigResponse.

        场景资源类型

        :param scenario_type: The scenario_type of this ShowSimBatchConfigResponse.
        :type scenario_type: int
        """
        self._scenario_type = scenario_type

    @property
    def scenario_set_id(self):
        r"""Gets the scenario_set_id of this ShowSimBatchConfigResponse.

        景资源组ID

        :return: The scenario_set_id of this ShowSimBatchConfigResponse.
        :rtype: int
        """
        return self._scenario_set_id

    @scenario_set_id.setter
    def scenario_set_id(self, scenario_set_id):
        r"""Sets the scenario_set_id of this ShowSimBatchConfigResponse.

        景资源组ID

        :param scenario_set_id: The scenario_set_id of this ShowSimBatchConfigResponse.
        :type scenario_set_id: int
        """
        self._scenario_set_id = scenario_set_id

    @property
    def triggerable(self):
        r"""Gets the triggerable of this ShowSimBatchConfigResponse.

        是否可通过流水线功能触发

        :return: The triggerable of this ShowSimBatchConfigResponse.
        :rtype: bool
        """
        return self._triggerable

    @triggerable.setter
    def triggerable(self, triggerable):
        r"""Sets the triggerable of this ShowSimBatchConfigResponse.

        是否可通过流水线功能触发

        :param triggerable: The triggerable of this ShowSimBatchConfigResponse.
        :type triggerable: bool
        """
        self._triggerable = triggerable

    @property
    def evaluations(self):
        r"""Gets the evaluations of this ShowSimBatchConfigResponse.

        关联评测管理项目

        :return: The evaluations of this ShowSimBatchConfigResponse.
        :rtype: list[str]
        """
        return self._evaluations

    @evaluations.setter
    def evaluations(self, evaluations):
        r"""Sets the evaluations of this ShowSimBatchConfigResponse.

        关联评测管理项目

        :param evaluations: The evaluations of this ShowSimBatchConfigResponse.
        :type evaluations: list[str]
        """
        self._evaluations = evaluations

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
        if not isinstance(other, ShowSimBatchConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
