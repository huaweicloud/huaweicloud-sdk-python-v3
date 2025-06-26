# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimulationSrlz:

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
        'evaluation': 'SimulationEvaluationSrlz',
        'started_at': 'float',
        'ended_at': 'float',
        'batch_name': 'str',
        'algorithm_name': 'str',
        'algorithm_image_version': 'str',
        'record_mode': 'int',
        'datahub': 'bool',
        'custom_evaluation_image': 'str',
        'passing_score': 'int',
        'evaluation_result': 'SimulationEvaResultSrlz',
        'files_path_info': 'SimulationFilePathSrlz',
        'scenario_type': 'int',
        'scenario_id': 'int',
        'simulator_name': 'str',
        'labels': 'list[object]',
        'status': 'Status15eEnum',
        'batch': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'evaluation': 'evaluation',
        'started_at': 'started_at',
        'ended_at': 'ended_at',
        'batch_name': 'batch_name',
        'algorithm_name': 'algorithm_name',
        'algorithm_image_version': 'algorithm_image_version',
        'record_mode': 'record_mode',
        'datahub': 'datahub',
        'custom_evaluation_image': 'custom_evaluation_image',
        'passing_score': 'passing_score',
        'evaluation_result': 'evaluation_result',
        'files_path_info': 'files_path_info',
        'scenario_type': 'scenario_type',
        'scenario_id': 'scenario_id',
        'simulator_name': 'simulator_name',
        'labels': 'labels',
        'status': 'status',
        'batch': 'batch'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, evaluation=None, started_at=None, ended_at=None, batch_name=None, algorithm_name=None, algorithm_image_version=None, record_mode=None, datahub=None, custom_evaluation_image=None, passing_score=None, evaluation_result=None, files_path_info=None, scenario_type=None, scenario_id=None, simulator_name=None, labels=None, status=None, batch=None):
        r"""SimulationSrlz

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param id: 
        :type id: int
        :param created_at: 
        :type created_at: float
        :param updated_at: 
        :type updated_at: float
        :param evaluation: 反馈的子任务评测信息
        :type evaluation: :class:`huaweicloudsdkoctopus.v2.SimulationEvaluationSrlz`
        :param started_at: 子任务开始时间
        :type started_at: float
        :param ended_at: 子任务结束时间
        :type ended_at: float
        :param batch_name: 任务名称
        :type batch_name: str
        :param algorithm_name: 关联算法名称
        :type algorithm_name: str
        :param algorithm_image_version: 关联算法镜像版本
        :type algorithm_image_version: str
        :param record_mode: 录制模式
        :type record_mode: int
        :param datahub: 是否使用datahub
        :type datahub: bool
        :param custom_evaluation_image: 关联评测镜像
        :type custom_evaluation_image: str
        :param passing_score: 融合评测通过分数
        :type passing_score: int
        :param evaluation_result: 融合评测结果
        :type evaluation_result: :class:`huaweicloudsdkoctopus.v2.SimulationEvaResultSrlz`
        :param files_path_info: 仿真结果文件信息
        :type files_path_info: :class:`huaweicloudsdkoctopus.v2.SimulationFilePathSrlz`
        :param scenario_type: 场景类型
        :type scenario_type: int
        :param scenario_id: 场景id
        :type scenario_id: int
        :param simulator_name: 仿真器名称
        :type simulator_name: str
        :param labels: 场景资源标签
        :type labels: list[object]
        :param status: 子任务状态  * &#x60;0&#x60; - Success  成功 * &#x60;1&#x60; - Pending  等待中 * &#x60;2&#x60; - Scheduling  调度 * &#x60;3&#x60; - Running  运行 * &#x60;4&#x60; - Canceled  取消 * &#x60;10&#x60; - Prepare Fail  准备失败 * &#x60;11&#x60; - Controller Fail  控制失败 * &#x60;12&#x60; - License Fail  许可失败 * &#x60;13&#x60; - Simulator Fail  仿真器失败 * &#x60;14&#x60; - Algorithm Fail  算法失败 * &#x60;15&#x60; - Evaluation Fail  评测失败 * &#x60;16&#x60; - Evicted  丢失 * &#x60;31&#x60; - Timeout  超时 * &#x60;32&#x60; - Unknown  未知
        :type status: :class:`huaweicloudsdkoctopus.v2.Status15eEnum`
        :param batch: 关联batch
        :type batch: str
        """
        
        

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._evaluation = None
        self._started_at = None
        self._ended_at = None
        self._batch_name = None
        self._algorithm_name = None
        self._algorithm_image_version = None
        self._record_mode = None
        self._datahub = None
        self._custom_evaluation_image = None
        self._passing_score = None
        self._evaluation_result = None
        self._files_path_info = None
        self._scenario_type = None
        self._scenario_id = None
        self._simulator_name = None
        self._labels = None
        self._status = None
        self._batch = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if evaluation is not None:
            self.evaluation = evaluation
        if started_at is not None:
            self.started_at = started_at
        if ended_at is not None:
            self.ended_at = ended_at
        if batch_name is not None:
            self.batch_name = batch_name
        if algorithm_name is not None:
            self.algorithm_name = algorithm_name
        if algorithm_image_version is not None:
            self.algorithm_image_version = algorithm_image_version
        if record_mode is not None:
            self.record_mode = record_mode
        if datahub is not None:
            self.datahub = datahub
        if custom_evaluation_image is not None:
            self.custom_evaluation_image = custom_evaluation_image
        if passing_score is not None:
            self.passing_score = passing_score
        if evaluation_result is not None:
            self.evaluation_result = evaluation_result
        if files_path_info is not None:
            self.files_path_info = files_path_info
        if scenario_type is not None:
            self.scenario_type = scenario_type
        if scenario_id is not None:
            self.scenario_id = scenario_id
        if simulator_name is not None:
            self.simulator_name = simulator_name
        if labels is not None:
            self.labels = labels
        if status is not None:
            self.status = status
        if batch is not None:
            self.batch = batch

    @property
    def url(self):
        r"""Gets the url of this SimulationSrlz.

        :return: The url of this SimulationSrlz.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this SimulationSrlz.

        :param url: The url of this SimulationSrlz.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this SimulationSrlz.

        :return: The id of this SimulationSrlz.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SimulationSrlz.

        :param id: The id of this SimulationSrlz.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this SimulationSrlz.

        :return: The created_at of this SimulationSrlz.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SimulationSrlz.

        :param created_at: The created_at of this SimulationSrlz.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SimulationSrlz.

        :return: The updated_at of this SimulationSrlz.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SimulationSrlz.

        :param updated_at: The updated_at of this SimulationSrlz.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def evaluation(self):
        r"""Gets the evaluation of this SimulationSrlz.

        反馈的子任务评测信息

        :return: The evaluation of this SimulationSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.SimulationEvaluationSrlz`
        """
        return self._evaluation

    @evaluation.setter
    def evaluation(self, evaluation):
        r"""Sets the evaluation of this SimulationSrlz.

        反馈的子任务评测信息

        :param evaluation: The evaluation of this SimulationSrlz.
        :type evaluation: :class:`huaweicloudsdkoctopus.v2.SimulationEvaluationSrlz`
        """
        self._evaluation = evaluation

    @property
    def started_at(self):
        r"""Gets the started_at of this SimulationSrlz.

        子任务开始时间

        :return: The started_at of this SimulationSrlz.
        :rtype: float
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        r"""Sets the started_at of this SimulationSrlz.

        子任务开始时间

        :param started_at: The started_at of this SimulationSrlz.
        :type started_at: float
        """
        self._started_at = started_at

    @property
    def ended_at(self):
        r"""Gets the ended_at of this SimulationSrlz.

        子任务结束时间

        :return: The ended_at of this SimulationSrlz.
        :rtype: float
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        r"""Sets the ended_at of this SimulationSrlz.

        子任务结束时间

        :param ended_at: The ended_at of this SimulationSrlz.
        :type ended_at: float
        """
        self._ended_at = ended_at

    @property
    def batch_name(self):
        r"""Gets the batch_name of this SimulationSrlz.

        任务名称

        :return: The batch_name of this SimulationSrlz.
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        r"""Sets the batch_name of this SimulationSrlz.

        任务名称

        :param batch_name: The batch_name of this SimulationSrlz.
        :type batch_name: str
        """
        self._batch_name = batch_name

    @property
    def algorithm_name(self):
        r"""Gets the algorithm_name of this SimulationSrlz.

        关联算法名称

        :return: The algorithm_name of this SimulationSrlz.
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        r"""Sets the algorithm_name of this SimulationSrlz.

        关联算法名称

        :param algorithm_name: The algorithm_name of this SimulationSrlz.
        :type algorithm_name: str
        """
        self._algorithm_name = algorithm_name

    @property
    def algorithm_image_version(self):
        r"""Gets the algorithm_image_version of this SimulationSrlz.

        关联算法镜像版本

        :return: The algorithm_image_version of this SimulationSrlz.
        :rtype: str
        """
        return self._algorithm_image_version

    @algorithm_image_version.setter
    def algorithm_image_version(self, algorithm_image_version):
        r"""Sets the algorithm_image_version of this SimulationSrlz.

        关联算法镜像版本

        :param algorithm_image_version: The algorithm_image_version of this SimulationSrlz.
        :type algorithm_image_version: str
        """
        self._algorithm_image_version = algorithm_image_version

    @property
    def record_mode(self):
        r"""Gets the record_mode of this SimulationSrlz.

        录制模式

        :return: The record_mode of this SimulationSrlz.
        :rtype: int
        """
        return self._record_mode

    @record_mode.setter
    def record_mode(self, record_mode):
        r"""Sets the record_mode of this SimulationSrlz.

        录制模式

        :param record_mode: The record_mode of this SimulationSrlz.
        :type record_mode: int
        """
        self._record_mode = record_mode

    @property
    def datahub(self):
        r"""Gets the datahub of this SimulationSrlz.

        是否使用datahub

        :return: The datahub of this SimulationSrlz.
        :rtype: bool
        """
        return self._datahub

    @datahub.setter
    def datahub(self, datahub):
        r"""Sets the datahub of this SimulationSrlz.

        是否使用datahub

        :param datahub: The datahub of this SimulationSrlz.
        :type datahub: bool
        """
        self._datahub = datahub

    @property
    def custom_evaluation_image(self):
        r"""Gets the custom_evaluation_image of this SimulationSrlz.

        关联评测镜像

        :return: The custom_evaluation_image of this SimulationSrlz.
        :rtype: str
        """
        return self._custom_evaluation_image

    @custom_evaluation_image.setter
    def custom_evaluation_image(self, custom_evaluation_image):
        r"""Sets the custom_evaluation_image of this SimulationSrlz.

        关联评测镜像

        :param custom_evaluation_image: The custom_evaluation_image of this SimulationSrlz.
        :type custom_evaluation_image: str
        """
        self._custom_evaluation_image = custom_evaluation_image

    @property
    def passing_score(self):
        r"""Gets the passing_score of this SimulationSrlz.

        融合评测通过分数

        :return: The passing_score of this SimulationSrlz.
        :rtype: int
        """
        return self._passing_score

    @passing_score.setter
    def passing_score(self, passing_score):
        r"""Sets the passing_score of this SimulationSrlz.

        融合评测通过分数

        :param passing_score: The passing_score of this SimulationSrlz.
        :type passing_score: int
        """
        self._passing_score = passing_score

    @property
    def evaluation_result(self):
        r"""Gets the evaluation_result of this SimulationSrlz.

        融合评测结果

        :return: The evaluation_result of this SimulationSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.SimulationEvaResultSrlz`
        """
        return self._evaluation_result

    @evaluation_result.setter
    def evaluation_result(self, evaluation_result):
        r"""Sets the evaluation_result of this SimulationSrlz.

        融合评测结果

        :param evaluation_result: The evaluation_result of this SimulationSrlz.
        :type evaluation_result: :class:`huaweicloudsdkoctopus.v2.SimulationEvaResultSrlz`
        """
        self._evaluation_result = evaluation_result

    @property
    def files_path_info(self):
        r"""Gets the files_path_info of this SimulationSrlz.

        仿真结果文件信息

        :return: The files_path_info of this SimulationSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.SimulationFilePathSrlz`
        """
        return self._files_path_info

    @files_path_info.setter
    def files_path_info(self, files_path_info):
        r"""Sets the files_path_info of this SimulationSrlz.

        仿真结果文件信息

        :param files_path_info: The files_path_info of this SimulationSrlz.
        :type files_path_info: :class:`huaweicloudsdkoctopus.v2.SimulationFilePathSrlz`
        """
        self._files_path_info = files_path_info

    @property
    def scenario_type(self):
        r"""Gets the scenario_type of this SimulationSrlz.

        场景类型

        :return: The scenario_type of this SimulationSrlz.
        :rtype: int
        """
        return self._scenario_type

    @scenario_type.setter
    def scenario_type(self, scenario_type):
        r"""Sets the scenario_type of this SimulationSrlz.

        场景类型

        :param scenario_type: The scenario_type of this SimulationSrlz.
        :type scenario_type: int
        """
        self._scenario_type = scenario_type

    @property
    def scenario_id(self):
        r"""Gets the scenario_id of this SimulationSrlz.

        场景id

        :return: The scenario_id of this SimulationSrlz.
        :rtype: int
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        r"""Sets the scenario_id of this SimulationSrlz.

        场景id

        :param scenario_id: The scenario_id of this SimulationSrlz.
        :type scenario_id: int
        """
        self._scenario_id = scenario_id

    @property
    def simulator_name(self):
        r"""Gets the simulator_name of this SimulationSrlz.

        仿真器名称

        :return: The simulator_name of this SimulationSrlz.
        :rtype: str
        """
        return self._simulator_name

    @simulator_name.setter
    def simulator_name(self, simulator_name):
        r"""Sets the simulator_name of this SimulationSrlz.

        仿真器名称

        :param simulator_name: The simulator_name of this SimulationSrlz.
        :type simulator_name: str
        """
        self._simulator_name = simulator_name

    @property
    def labels(self):
        r"""Gets the labels of this SimulationSrlz.

        场景资源标签

        :return: The labels of this SimulationSrlz.
        :rtype: list[object]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this SimulationSrlz.

        场景资源标签

        :param labels: The labels of this SimulationSrlz.
        :type labels: list[object]
        """
        self._labels = labels

    @property
    def status(self):
        r"""Gets the status of this SimulationSrlz.

        子任务状态  * `0` - Success  成功 * `1` - Pending  等待中 * `2` - Scheduling  调度 * `3` - Running  运行 * `4` - Canceled  取消 * `10` - Prepare Fail  准备失败 * `11` - Controller Fail  控制失败 * `12` - License Fail  许可失败 * `13` - Simulator Fail  仿真器失败 * `14` - Algorithm Fail  算法失败 * `15` - Evaluation Fail  评测失败 * `16` - Evicted  丢失 * `31` - Timeout  超时 * `32` - Unknown  未知

        :return: The status of this SimulationSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.Status15eEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SimulationSrlz.

        子任务状态  * `0` - Success  成功 * `1` - Pending  等待中 * `2` - Scheduling  调度 * `3` - Running  运行 * `4` - Canceled  取消 * `10` - Prepare Fail  准备失败 * `11` - Controller Fail  控制失败 * `12` - License Fail  许可失败 * `13` - Simulator Fail  仿真器失败 * `14` - Algorithm Fail  算法失败 * `15` - Evaluation Fail  评测失败 * `16` - Evicted  丢失 * `31` - Timeout  超时 * `32` - Unknown  未知

        :param status: The status of this SimulationSrlz.
        :type status: :class:`huaweicloudsdkoctopus.v2.Status15eEnum`
        """
        self._status = status

    @property
    def batch(self):
        r"""Gets the batch of this SimulationSrlz.

        关联batch

        :return: The batch of this SimulationSrlz.
        :rtype: str
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        r"""Sets the batch of this SimulationSrlz.

        关联batch

        :param batch: The batch of this SimulationSrlz.
        :type batch: str
        """
        self._batch = batch

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
        if not isinstance(other, SimulationSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
