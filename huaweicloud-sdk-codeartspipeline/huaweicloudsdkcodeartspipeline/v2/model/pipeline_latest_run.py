# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineLatestRun:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_id': 'str',
        'pipeline_run_id': 'str',
        'executor_id': 'str',
        'executor_name': 'str',
        'stage_status_list': 'list[PipelineLatestRunStageStatusList]',
        'status': 'str',
        'run_number': 'int',
        'trigger_type': 'str',
        'build_params': 'PipelineLatestRunBuildParams',
        'artifact_params': 'PipelineLatestRunArtifactParams',
        'start_time': 'int',
        'end_time': 'int',
        'modify_url': 'str',
        'detail_url': 'str'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'pipeline_run_id': 'pipeline_run_id',
        'executor_id': 'executor_id',
        'executor_name': 'executor_name',
        'stage_status_list': 'stage_status_list',
        'status': 'status',
        'run_number': 'run_number',
        'trigger_type': 'trigger_type',
        'build_params': 'build_params',
        'artifact_params': 'artifact_params',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'modify_url': 'modify_url',
        'detail_url': 'detail_url'
    }

    def __init__(self, pipeline_id=None, pipeline_run_id=None, executor_id=None, executor_name=None, stage_status_list=None, status=None, run_number=None, trigger_type=None, build_params=None, artifact_params=None, start_time=None, end_time=None, modify_url=None, detail_url=None):
        """PipelineLatestRun

        The model defined in huaweicloud sdk

        :param pipeline_id: 流水线ID
        :type pipeline_id: str
        :param pipeline_run_id: 流水线运行实例ID
        :type pipeline_run_id: str
        :param executor_id: 执行人ID
        :type executor_id: str
        :param executor_name: 执行人名称
        :type executor_name: str
        :param stage_status_list: 阶段状态信息
        :type stage_status_list: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineLatestRunStageStatusList`]
        :param status: 流水线状态
        :type status: str
        :param run_number: 运行序号
        :type run_number: int
        :param trigger_type: 触发类型
        :type trigger_type: str
        :param build_params: 
        :type build_params: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineLatestRunBuildParams`
        :param artifact_params: 
        :type artifact_params: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineLatestRunArtifactParams`
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param modify_url: 修改页地址
        :type modify_url: str
        :param detail_url: 详情页地址
        :type detail_url: str
        """
        
        

        self._pipeline_id = None
        self._pipeline_run_id = None
        self._executor_id = None
        self._executor_name = None
        self._stage_status_list = None
        self._status = None
        self._run_number = None
        self._trigger_type = None
        self._build_params = None
        self._artifact_params = None
        self._start_time = None
        self._end_time = None
        self._modify_url = None
        self._detail_url = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if pipeline_run_id is not None:
            self.pipeline_run_id = pipeline_run_id
        if executor_id is not None:
            self.executor_id = executor_id
        if executor_name is not None:
            self.executor_name = executor_name
        if stage_status_list is not None:
            self.stage_status_list = stage_status_list
        if status is not None:
            self.status = status
        if run_number is not None:
            self.run_number = run_number
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if build_params is not None:
            self.build_params = build_params
        if artifact_params is not None:
            self.artifact_params = artifact_params
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if modify_url is not None:
            self.modify_url = modify_url
        if detail_url is not None:
            self.detail_url = detail_url

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this PipelineLatestRun.

        流水线ID

        :return: The pipeline_id of this PipelineLatestRun.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this PipelineLatestRun.

        流水线ID

        :param pipeline_id: The pipeline_id of this PipelineLatestRun.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def pipeline_run_id(self):
        """Gets the pipeline_run_id of this PipelineLatestRun.

        流水线运行实例ID

        :return: The pipeline_run_id of this PipelineLatestRun.
        :rtype: str
        """
        return self._pipeline_run_id

    @pipeline_run_id.setter
    def pipeline_run_id(self, pipeline_run_id):
        """Sets the pipeline_run_id of this PipelineLatestRun.

        流水线运行实例ID

        :param pipeline_run_id: The pipeline_run_id of this PipelineLatestRun.
        :type pipeline_run_id: str
        """
        self._pipeline_run_id = pipeline_run_id

    @property
    def executor_id(self):
        """Gets the executor_id of this PipelineLatestRun.

        执行人ID

        :return: The executor_id of this PipelineLatestRun.
        :rtype: str
        """
        return self._executor_id

    @executor_id.setter
    def executor_id(self, executor_id):
        """Sets the executor_id of this PipelineLatestRun.

        执行人ID

        :param executor_id: The executor_id of this PipelineLatestRun.
        :type executor_id: str
        """
        self._executor_id = executor_id

    @property
    def executor_name(self):
        """Gets the executor_name of this PipelineLatestRun.

        执行人名称

        :return: The executor_name of this PipelineLatestRun.
        :rtype: str
        """
        return self._executor_name

    @executor_name.setter
    def executor_name(self, executor_name):
        """Sets the executor_name of this PipelineLatestRun.

        执行人名称

        :param executor_name: The executor_name of this PipelineLatestRun.
        :type executor_name: str
        """
        self._executor_name = executor_name

    @property
    def stage_status_list(self):
        """Gets the stage_status_list of this PipelineLatestRun.

        阶段状态信息

        :return: The stage_status_list of this PipelineLatestRun.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineLatestRunStageStatusList`]
        """
        return self._stage_status_list

    @stage_status_list.setter
    def stage_status_list(self, stage_status_list):
        """Sets the stage_status_list of this PipelineLatestRun.

        阶段状态信息

        :param stage_status_list: The stage_status_list of this PipelineLatestRun.
        :type stage_status_list: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineLatestRunStageStatusList`]
        """
        self._stage_status_list = stage_status_list

    @property
    def status(self):
        """Gets the status of this PipelineLatestRun.

        流水线状态

        :return: The status of this PipelineLatestRun.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PipelineLatestRun.

        流水线状态

        :param status: The status of this PipelineLatestRun.
        :type status: str
        """
        self._status = status

    @property
    def run_number(self):
        """Gets the run_number of this PipelineLatestRun.

        运行序号

        :return: The run_number of this PipelineLatestRun.
        :rtype: int
        """
        return self._run_number

    @run_number.setter
    def run_number(self, run_number):
        """Sets the run_number of this PipelineLatestRun.

        运行序号

        :param run_number: The run_number of this PipelineLatestRun.
        :type run_number: int
        """
        self._run_number = run_number

    @property
    def trigger_type(self):
        """Gets the trigger_type of this PipelineLatestRun.

        触发类型

        :return: The trigger_type of this PipelineLatestRun.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this PipelineLatestRun.

        触发类型

        :param trigger_type: The trigger_type of this PipelineLatestRun.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def build_params(self):
        """Gets the build_params of this PipelineLatestRun.

        :return: The build_params of this PipelineLatestRun.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineLatestRunBuildParams`
        """
        return self._build_params

    @build_params.setter
    def build_params(self, build_params):
        """Sets the build_params of this PipelineLatestRun.

        :param build_params: The build_params of this PipelineLatestRun.
        :type build_params: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineLatestRunBuildParams`
        """
        self._build_params = build_params

    @property
    def artifact_params(self):
        """Gets the artifact_params of this PipelineLatestRun.

        :return: The artifact_params of this PipelineLatestRun.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineLatestRunArtifactParams`
        """
        return self._artifact_params

    @artifact_params.setter
    def artifact_params(self, artifact_params):
        """Sets the artifact_params of this PipelineLatestRun.

        :param artifact_params: The artifact_params of this PipelineLatestRun.
        :type artifact_params: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineLatestRunArtifactParams`
        """
        self._artifact_params = artifact_params

    @property
    def start_time(self):
        """Gets the start_time of this PipelineLatestRun.

        开始时间

        :return: The start_time of this PipelineLatestRun.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PipelineLatestRun.

        开始时间

        :param start_time: The start_time of this PipelineLatestRun.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this PipelineLatestRun.

        结束时间

        :return: The end_time of this PipelineLatestRun.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PipelineLatestRun.

        结束时间

        :param end_time: The end_time of this PipelineLatestRun.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def modify_url(self):
        """Gets the modify_url of this PipelineLatestRun.

        修改页地址

        :return: The modify_url of this PipelineLatestRun.
        :rtype: str
        """
        return self._modify_url

    @modify_url.setter
    def modify_url(self, modify_url):
        """Sets the modify_url of this PipelineLatestRun.

        修改页地址

        :param modify_url: The modify_url of this PipelineLatestRun.
        :type modify_url: str
        """
        self._modify_url = modify_url

    @property
    def detail_url(self):
        """Gets the detail_url of this PipelineLatestRun.

        详情页地址

        :return: The detail_url of this PipelineLatestRun.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        """Sets the detail_url of this PipelineLatestRun.

        详情页地址

        :param detail_url: The detail_url of this PipelineLatestRun.
        :type detail_url: str
        """
        self._detail_url = detail_url

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
        if not isinstance(other, PipelineLatestRun):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
