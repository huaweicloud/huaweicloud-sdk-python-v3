# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPipelineRunDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'pipeline_id': 'str',
        'manifest_version': 'str',
        'name': 'str',
        'description': 'str',
        'is_publish': 'bool',
        'executor_id': 'str',
        'executor_name': 'str',
        'status': 'str',
        'trigger_type': 'str',
        'run_number': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'stages': 'list[StageRun]',
        'domain_id': 'str',
        'project_id': 'str',
        'region': 'str',
        'component_id': 'str',
        'language': 'str',
        'sources': 'list[RunPipelineSource]',
        'artifacts': 'list[PackageInfo]',
        'subject_id': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'detail_url': 'str',
        'current_system_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'pipeline_id': 'pipeline_id',
        'manifest_version': 'manifest_version',
        'name': 'name',
        'description': 'description',
        'is_publish': 'is_publish',
        'executor_id': 'executor_id',
        'executor_name': 'executor_name',
        'status': 'status',
        'trigger_type': 'trigger_type',
        'run_number': 'run_number',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'stages': 'stages',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'region': 'region',
        'component_id': 'component_id',
        'language': 'language',
        'sources': 'sources',
        'artifacts': 'artifacts',
        'subject_id': 'subject_id',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'detail_url': 'detail_url',
        'current_system_time': 'current_system_time'
    }

    def __init__(self, id=None, pipeline_id=None, manifest_version=None, name=None, description=None, is_publish=None, executor_id=None, executor_name=None, status=None, trigger_type=None, run_number=None, start_time=None, end_time=None, stages=None, domain_id=None, project_id=None, region=None, component_id=None, language=None, sources=None, artifacts=None, subject_id=None, group_id=None, group_name=None, detail_url=None, current_system_time=None):
        """ShowPipelineRunDetailResponse

        The model defined in huaweicloud sdk

        :param id: 流水线运行实例ID
        :type id: str
        :param pipeline_id: 流水线ID
        :type pipeline_id: str
        :param manifest_version: 流水线版本
        :type manifest_version: str
        :param name: 流水线名称
        :type name: str
        :param description: 运行描述
        :type description: str
        :param is_publish: 是否为变更流水线
        :type is_publish: bool
        :param executor_id: 运行人ID
        :type executor_id: str
        :param executor_name: 运行人名称
        :type executor_name: str
        :param status: 状态
        :type status: str
        :param trigger_type: 触发类型
        :type trigger_type: str
        :param run_number: 运行序号
        :type run_number: int
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param stages: 阶段信息
        :type stages: list[:class:`huaweicloudsdkcodeartspipeline.v2.StageRun`]
        :param domain_id: 租户ID
        :type domain_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param region: 局点
        :type region: str
        :param component_id: 组件ID
        :type component_id: str
        :param language: 语言
        :type language: str
        :param sources: 运行源信息
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineSource`]
        :param artifacts: 流水线运行产物
        :type artifacts: list[:class:`huaweicloudsdkcodeartspipeline.v2.PackageInfo`]
        :param subject_id: 流水线运行实例ID
        :type subject_id: str
        :param group_id: 分组ID
        :type group_id: str
        :param group_name: 分组名称
        :type group_name: str
        :param detail_url: 详情页地址
        :type detail_url: str
        :param current_system_time: 当前系统时间
        :type current_system_time: str
        """
        
        super(ShowPipelineRunDetailResponse, self).__init__()

        self._id = None
        self._pipeline_id = None
        self._manifest_version = None
        self._name = None
        self._description = None
        self._is_publish = None
        self._executor_id = None
        self._executor_name = None
        self._status = None
        self._trigger_type = None
        self._run_number = None
        self._start_time = None
        self._end_time = None
        self._stages = None
        self._domain_id = None
        self._project_id = None
        self._region = None
        self._component_id = None
        self._language = None
        self._sources = None
        self._artifacts = None
        self._subject_id = None
        self._group_id = None
        self._group_name = None
        self._detail_url = None
        self._current_system_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if manifest_version is not None:
            self.manifest_version = manifest_version
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if is_publish is not None:
            self.is_publish = is_publish
        if executor_id is not None:
            self.executor_id = executor_id
        if executor_name is not None:
            self.executor_name = executor_name
        if status is not None:
            self.status = status
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if run_number is not None:
            self.run_number = run_number
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if stages is not None:
            self.stages = stages
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if region is not None:
            self.region = region
        if component_id is not None:
            self.component_id = component_id
        if language is not None:
            self.language = language
        if sources is not None:
            self.sources = sources
        if artifacts is not None:
            self.artifacts = artifacts
        if subject_id is not None:
            self.subject_id = subject_id
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if detail_url is not None:
            self.detail_url = detail_url
        if current_system_time is not None:
            self.current_system_time = current_system_time

    @property
    def id(self):
        """Gets the id of this ShowPipelineRunDetailResponse.

        流水线运行实例ID

        :return: The id of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowPipelineRunDetailResponse.

        流水线运行实例ID

        :param id: The id of this ShowPipelineRunDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this ShowPipelineRunDetailResponse.

        流水线ID

        :return: The pipeline_id of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this ShowPipelineRunDetailResponse.

        流水线ID

        :param pipeline_id: The pipeline_id of this ShowPipelineRunDetailResponse.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def manifest_version(self):
        """Gets the manifest_version of this ShowPipelineRunDetailResponse.

        流水线版本

        :return: The manifest_version of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        """Sets the manifest_version of this ShowPipelineRunDetailResponse.

        流水线版本

        :param manifest_version: The manifest_version of this ShowPipelineRunDetailResponse.
        :type manifest_version: str
        """
        self._manifest_version = manifest_version

    @property
    def name(self):
        """Gets the name of this ShowPipelineRunDetailResponse.

        流水线名称

        :return: The name of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowPipelineRunDetailResponse.

        流水线名称

        :param name: The name of this ShowPipelineRunDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowPipelineRunDetailResponse.

        运行描述

        :return: The description of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowPipelineRunDetailResponse.

        运行描述

        :param description: The description of this ShowPipelineRunDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def is_publish(self):
        """Gets the is_publish of this ShowPipelineRunDetailResponse.

        是否为变更流水线

        :return: The is_publish of this ShowPipelineRunDetailResponse.
        :rtype: bool
        """
        return self._is_publish

    @is_publish.setter
    def is_publish(self, is_publish):
        """Sets the is_publish of this ShowPipelineRunDetailResponse.

        是否为变更流水线

        :param is_publish: The is_publish of this ShowPipelineRunDetailResponse.
        :type is_publish: bool
        """
        self._is_publish = is_publish

    @property
    def executor_id(self):
        """Gets the executor_id of this ShowPipelineRunDetailResponse.

        运行人ID

        :return: The executor_id of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._executor_id

    @executor_id.setter
    def executor_id(self, executor_id):
        """Sets the executor_id of this ShowPipelineRunDetailResponse.

        运行人ID

        :param executor_id: The executor_id of this ShowPipelineRunDetailResponse.
        :type executor_id: str
        """
        self._executor_id = executor_id

    @property
    def executor_name(self):
        """Gets the executor_name of this ShowPipelineRunDetailResponse.

        运行人名称

        :return: The executor_name of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._executor_name

    @executor_name.setter
    def executor_name(self, executor_name):
        """Sets the executor_name of this ShowPipelineRunDetailResponse.

        运行人名称

        :param executor_name: The executor_name of this ShowPipelineRunDetailResponse.
        :type executor_name: str
        """
        self._executor_name = executor_name

    @property
    def status(self):
        """Gets the status of this ShowPipelineRunDetailResponse.

        状态

        :return: The status of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowPipelineRunDetailResponse.

        状态

        :param status: The status of this ShowPipelineRunDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def trigger_type(self):
        """Gets the trigger_type of this ShowPipelineRunDetailResponse.

        触发类型

        :return: The trigger_type of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this ShowPipelineRunDetailResponse.

        触发类型

        :param trigger_type: The trigger_type of this ShowPipelineRunDetailResponse.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def run_number(self):
        """Gets the run_number of this ShowPipelineRunDetailResponse.

        运行序号

        :return: The run_number of this ShowPipelineRunDetailResponse.
        :rtype: int
        """
        return self._run_number

    @run_number.setter
    def run_number(self, run_number):
        """Sets the run_number of this ShowPipelineRunDetailResponse.

        运行序号

        :param run_number: The run_number of this ShowPipelineRunDetailResponse.
        :type run_number: int
        """
        self._run_number = run_number

    @property
    def start_time(self):
        """Gets the start_time of this ShowPipelineRunDetailResponse.

        开始时间

        :return: The start_time of this ShowPipelineRunDetailResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowPipelineRunDetailResponse.

        开始时间

        :param start_time: The start_time of this ShowPipelineRunDetailResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowPipelineRunDetailResponse.

        结束时间

        :return: The end_time of this ShowPipelineRunDetailResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowPipelineRunDetailResponse.

        结束时间

        :param end_time: The end_time of this ShowPipelineRunDetailResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def stages(self):
        """Gets the stages of this ShowPipelineRunDetailResponse.

        阶段信息

        :return: The stages of this ShowPipelineRunDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.StageRun`]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this ShowPipelineRunDetailResponse.

        阶段信息

        :param stages: The stages of this ShowPipelineRunDetailResponse.
        :type stages: list[:class:`huaweicloudsdkcodeartspipeline.v2.StageRun`]
        """
        self._stages = stages

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowPipelineRunDetailResponse.

        租户ID

        :return: The domain_id of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowPipelineRunDetailResponse.

        租户ID

        :param domain_id: The domain_id of this ShowPipelineRunDetailResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this ShowPipelineRunDetailResponse.

        项目ID

        :return: The project_id of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowPipelineRunDetailResponse.

        项目ID

        :param project_id: The project_id of this ShowPipelineRunDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region(self):
        """Gets the region of this ShowPipelineRunDetailResponse.

        局点

        :return: The region of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowPipelineRunDetailResponse.

        局点

        :param region: The region of this ShowPipelineRunDetailResponse.
        :type region: str
        """
        self._region = region

    @property
    def component_id(self):
        """Gets the component_id of this ShowPipelineRunDetailResponse.

        组件ID

        :return: The component_id of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ShowPipelineRunDetailResponse.

        组件ID

        :param component_id: The component_id of this ShowPipelineRunDetailResponse.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def language(self):
        """Gets the language of this ShowPipelineRunDetailResponse.

        语言

        :return: The language of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ShowPipelineRunDetailResponse.

        语言

        :param language: The language of this ShowPipelineRunDetailResponse.
        :type language: str
        """
        self._language = language

    @property
    def sources(self):
        """Gets the sources of this ShowPipelineRunDetailResponse.

        运行源信息

        :return: The sources of this ShowPipelineRunDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineSource`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this ShowPipelineRunDetailResponse.

        运行源信息

        :param sources: The sources of this ShowPipelineRunDetailResponse.
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineSource`]
        """
        self._sources = sources

    @property
    def artifacts(self):
        """Gets the artifacts of this ShowPipelineRunDetailResponse.

        流水线运行产物

        :return: The artifacts of this ShowPipelineRunDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PackageInfo`]
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this ShowPipelineRunDetailResponse.

        流水线运行产物

        :param artifacts: The artifacts of this ShowPipelineRunDetailResponse.
        :type artifacts: list[:class:`huaweicloudsdkcodeartspipeline.v2.PackageInfo`]
        """
        self._artifacts = artifacts

    @property
    def subject_id(self):
        """Gets the subject_id of this ShowPipelineRunDetailResponse.

        流水线运行实例ID

        :return: The subject_id of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this ShowPipelineRunDetailResponse.

        流水线运行实例ID

        :param subject_id: The subject_id of this ShowPipelineRunDetailResponse.
        :type subject_id: str
        """
        self._subject_id = subject_id

    @property
    def group_id(self):
        """Gets the group_id of this ShowPipelineRunDetailResponse.

        分组ID

        :return: The group_id of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowPipelineRunDetailResponse.

        分组ID

        :param group_id: The group_id of this ShowPipelineRunDetailResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this ShowPipelineRunDetailResponse.

        分组名称

        :return: The group_name of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ShowPipelineRunDetailResponse.

        分组名称

        :param group_name: The group_name of this ShowPipelineRunDetailResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def detail_url(self):
        """Gets the detail_url of this ShowPipelineRunDetailResponse.

        详情页地址

        :return: The detail_url of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        """Sets the detail_url of this ShowPipelineRunDetailResponse.

        详情页地址

        :param detail_url: The detail_url of this ShowPipelineRunDetailResponse.
        :type detail_url: str
        """
        self._detail_url = detail_url

    @property
    def current_system_time(self):
        """Gets the current_system_time of this ShowPipelineRunDetailResponse.

        当前系统时间

        :return: The current_system_time of this ShowPipelineRunDetailResponse.
        :rtype: str
        """
        return self._current_system_time

    @current_system_time.setter
    def current_system_time(self, current_system_time):
        """Sets the current_system_time of this ShowPipelineRunDetailResponse.

        当前系统时间

        :param current_system_time: The current_system_time of this ShowPipelineRunDetailResponse.
        :type current_system_time: str
        """
        self._current_system_time = current_system_time

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
        if not isinstance(other, ShowPipelineRunDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
