# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineExecuteStates:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'status': 'str',
        'stages': 'list[Stages]',
        'executor': 'str',
        'pipeline_name': 'str',
        'pipeline_id': 'str',
        'build_id': 'str',
        'detail_url': 'str',
        'modify_url': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status',
        'stages': 'stages',
        'executor': 'executor',
        'pipeline_name': 'pipeline_name',
        'pipeline_id': 'pipeline_id',
        'build_id': 'build_id',
        'detail_url': 'detail_url',
        'modify_url': 'modify_url',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, result=None, status=None, stages=None, executor=None, pipeline_name=None, pipeline_id=None, build_id=None, detail_url=None, modify_url=None, start_time=None, end_time=None):
        r"""PipelineExecuteStates

        The model defined in huaweicloud sdk

        :param result: 流水线执行结果。取值及含义：success：成功；error：失败；aborted：终止
        :type result: str
        :param status: 流水线执行状态.取值和含义:waiting:等待;running:执行中;verifying:待审核;suspending:挂起;completed:完成
        :type status: str
        :param stages: 阶段执行情况
        :type stages: list[:class:`huaweicloudsdkcodeartspipeline.v2.Stages`]
        :param executor: 执行人
        :type executor: str
        :param pipeline_name: 流水线名字
        :type pipeline_name: str
        :param pipeline_id: 流水线ID
        :type pipeline_id: str
        :param build_id: 流水线执行ID
        :type build_id: str
        :param detail_url: 流水线详情页URL
        :type detail_url: str
        :param modify_url: 流水线编辑页URL
        :type modify_url: str
        :param start_time: 开始执行时间
        :type start_time: str
        :param end_time: 结束执行时间
        :type end_time: str
        """
        
        

        self._result = None
        self._status = None
        self._stages = None
        self._executor = None
        self._pipeline_name = None
        self._pipeline_id = None
        self._build_id = None
        self._detail_url = None
        self._modify_url = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.result = result
        self.status = status
        self.stages = stages
        self.executor = executor
        self.pipeline_name = pipeline_name
        self.pipeline_id = pipeline_id
        self.build_id = build_id
        self.detail_url = detail_url
        self.modify_url = modify_url
        self.start_time = start_time
        self.end_time = end_time

    @property
    def result(self):
        r"""Gets the result of this PipelineExecuteStates.

        流水线执行结果。取值及含义：success：成功；error：失败；aborted：终止

        :return: The result of this PipelineExecuteStates.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this PipelineExecuteStates.

        流水线执行结果。取值及含义：success：成功；error：失败；aborted：终止

        :param result: The result of this PipelineExecuteStates.
        :type result: str
        """
        self._result = result

    @property
    def status(self):
        r"""Gets the status of this PipelineExecuteStates.

        流水线执行状态.取值和含义:waiting:等待;running:执行中;verifying:待审核;suspending:挂起;completed:完成

        :return: The status of this PipelineExecuteStates.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PipelineExecuteStates.

        流水线执行状态.取值和含义:waiting:等待;running:执行中;verifying:待审核;suspending:挂起;completed:完成

        :param status: The status of this PipelineExecuteStates.
        :type status: str
        """
        self._status = status

    @property
    def stages(self):
        r"""Gets the stages of this PipelineExecuteStates.

        阶段执行情况

        :return: The stages of this PipelineExecuteStates.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.Stages`]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        r"""Sets the stages of this PipelineExecuteStates.

        阶段执行情况

        :param stages: The stages of this PipelineExecuteStates.
        :type stages: list[:class:`huaweicloudsdkcodeartspipeline.v2.Stages`]
        """
        self._stages = stages

    @property
    def executor(self):
        r"""Gets the executor of this PipelineExecuteStates.

        执行人

        :return: The executor of this PipelineExecuteStates.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        r"""Sets the executor of this PipelineExecuteStates.

        执行人

        :param executor: The executor of this PipelineExecuteStates.
        :type executor: str
        """
        self._executor = executor

    @property
    def pipeline_name(self):
        r"""Gets the pipeline_name of this PipelineExecuteStates.

        流水线名字

        :return: The pipeline_name of this PipelineExecuteStates.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        r"""Sets the pipeline_name of this PipelineExecuteStates.

        流水线名字

        :param pipeline_name: The pipeline_name of this PipelineExecuteStates.
        :type pipeline_name: str
        """
        self._pipeline_name = pipeline_name

    @property
    def pipeline_id(self):
        r"""Gets the pipeline_id of this PipelineExecuteStates.

        流水线ID

        :return: The pipeline_id of this PipelineExecuteStates.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        r"""Sets the pipeline_id of this PipelineExecuteStates.

        流水线ID

        :param pipeline_id: The pipeline_id of this PipelineExecuteStates.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def build_id(self):
        r"""Gets the build_id of this PipelineExecuteStates.

        流水线执行ID

        :return: The build_id of this PipelineExecuteStates.
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        r"""Sets the build_id of this PipelineExecuteStates.

        流水线执行ID

        :param build_id: The build_id of this PipelineExecuteStates.
        :type build_id: str
        """
        self._build_id = build_id

    @property
    def detail_url(self):
        r"""Gets the detail_url of this PipelineExecuteStates.

        流水线详情页URL

        :return: The detail_url of this PipelineExecuteStates.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        r"""Sets the detail_url of this PipelineExecuteStates.

        流水线详情页URL

        :param detail_url: The detail_url of this PipelineExecuteStates.
        :type detail_url: str
        """
        self._detail_url = detail_url

    @property
    def modify_url(self):
        r"""Gets the modify_url of this PipelineExecuteStates.

        流水线编辑页URL

        :return: The modify_url of this PipelineExecuteStates.
        :rtype: str
        """
        return self._modify_url

    @modify_url.setter
    def modify_url(self, modify_url):
        r"""Sets the modify_url of this PipelineExecuteStates.

        流水线编辑页URL

        :param modify_url: The modify_url of this PipelineExecuteStates.
        :type modify_url: str
        """
        self._modify_url = modify_url

    @property
    def start_time(self):
        r"""Gets the start_time of this PipelineExecuteStates.

        开始执行时间

        :return: The start_time of this PipelineExecuteStates.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this PipelineExecuteStates.

        开始执行时间

        :param start_time: The start_time of this PipelineExecuteStates.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this PipelineExecuteStates.

        结束执行时间

        :return: The end_time of this PipelineExecuteStates.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this PipelineExecuteStates.

        结束执行时间

        :param end_time: The end_time of this PipelineExecuteStates.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, PipelineExecuteStates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
