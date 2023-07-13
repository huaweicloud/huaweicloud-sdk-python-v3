# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPipelineLastStatusV2Response(SdkResponse):

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
        'name': 'str',
        'status': 'str',
        'result': 'str',
        'executor': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'detail_url': 'str',
        'modify_url': 'str',
        'build_id': 'str',
        'stages': 'list[PipelineStageResp]'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'name': 'name',
        'status': 'status',
        'result': 'result',
        'executor': 'executor',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'detail_url': 'detail_url',
        'modify_url': 'modify_url',
        'build_id': 'build_id',
        'stages': 'stages'
    }

    def __init__(self, pipeline_id=None, name=None, status=None, result=None, executor=None, start_time=None, finish_time=None, detail_url=None, modify_url=None, build_id=None, stages=None):
        """ShowPipelineLastStatusV2Response

        The model defined in huaweicloud sdk

        :param pipeline_id: 流水线id
        :type pipeline_id: str
        :param name: 流水线名称
        :type name: str
        :param status: 执行状态
        :type status: str
        :param result: 执行结果
        :type result: str
        :param executor: 执行人
        :type executor: str
        :param start_time: 启动时间
        :type start_time: str
        :param finish_time: 结束时间
        :type finish_time: str
        :param detail_url: 运行详情链接
        :type detail_url: str
        :param modify_url: 编辑链接
        :type modify_url: str
        :param build_id: 流水线执行序号
        :type build_id: str
        :param stages: 阶段信息
        :type stages: list[:class:`huaweicloudsdkdevstar.v1.PipelineStageResp`]
        """
        
        super(ShowPipelineLastStatusV2Response, self).__init__()

        self._pipeline_id = None
        self._name = None
        self._status = None
        self._result = None
        self._executor = None
        self._start_time = None
        self._finish_time = None
        self._detail_url = None
        self._modify_url = None
        self._build_id = None
        self._stages = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if result is not None:
            self.result = result
        if executor is not None:
            self.executor = executor
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if detail_url is not None:
            self.detail_url = detail_url
        if modify_url is not None:
            self.modify_url = modify_url
        if build_id is not None:
            self.build_id = build_id
        if stages is not None:
            self.stages = stages

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this ShowPipelineLastStatusV2Response.

        流水线id

        :return: The pipeline_id of this ShowPipelineLastStatusV2Response.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this ShowPipelineLastStatusV2Response.

        流水线id

        :param pipeline_id: The pipeline_id of this ShowPipelineLastStatusV2Response.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def name(self):
        """Gets the name of this ShowPipelineLastStatusV2Response.

        流水线名称

        :return: The name of this ShowPipelineLastStatusV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowPipelineLastStatusV2Response.

        流水线名称

        :param name: The name of this ShowPipelineLastStatusV2Response.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ShowPipelineLastStatusV2Response.

        执行状态

        :return: The status of this ShowPipelineLastStatusV2Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowPipelineLastStatusV2Response.

        执行状态

        :param status: The status of this ShowPipelineLastStatusV2Response.
        :type status: str
        """
        self._status = status

    @property
    def result(self):
        """Gets the result of this ShowPipelineLastStatusV2Response.

        执行结果

        :return: The result of this ShowPipelineLastStatusV2Response.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ShowPipelineLastStatusV2Response.

        执行结果

        :param result: The result of this ShowPipelineLastStatusV2Response.
        :type result: str
        """
        self._result = result

    @property
    def executor(self):
        """Gets the executor of this ShowPipelineLastStatusV2Response.

        执行人

        :return: The executor of this ShowPipelineLastStatusV2Response.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this ShowPipelineLastStatusV2Response.

        执行人

        :param executor: The executor of this ShowPipelineLastStatusV2Response.
        :type executor: str
        """
        self._executor = executor

    @property
    def start_time(self):
        """Gets the start_time of this ShowPipelineLastStatusV2Response.

        启动时间

        :return: The start_time of this ShowPipelineLastStatusV2Response.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowPipelineLastStatusV2Response.

        启动时间

        :param start_time: The start_time of this ShowPipelineLastStatusV2Response.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        """Gets the finish_time of this ShowPipelineLastStatusV2Response.

        结束时间

        :return: The finish_time of this ShowPipelineLastStatusV2Response.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this ShowPipelineLastStatusV2Response.

        结束时间

        :param finish_time: The finish_time of this ShowPipelineLastStatusV2Response.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def detail_url(self):
        """Gets the detail_url of this ShowPipelineLastStatusV2Response.

        运行详情链接

        :return: The detail_url of this ShowPipelineLastStatusV2Response.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        """Sets the detail_url of this ShowPipelineLastStatusV2Response.

        运行详情链接

        :param detail_url: The detail_url of this ShowPipelineLastStatusV2Response.
        :type detail_url: str
        """
        self._detail_url = detail_url

    @property
    def modify_url(self):
        """Gets the modify_url of this ShowPipelineLastStatusV2Response.

        编辑链接

        :return: The modify_url of this ShowPipelineLastStatusV2Response.
        :rtype: str
        """
        return self._modify_url

    @modify_url.setter
    def modify_url(self, modify_url):
        """Sets the modify_url of this ShowPipelineLastStatusV2Response.

        编辑链接

        :param modify_url: The modify_url of this ShowPipelineLastStatusV2Response.
        :type modify_url: str
        """
        self._modify_url = modify_url

    @property
    def build_id(self):
        """Gets the build_id of this ShowPipelineLastStatusV2Response.

        流水线执行序号

        :return: The build_id of this ShowPipelineLastStatusV2Response.
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this ShowPipelineLastStatusV2Response.

        流水线执行序号

        :param build_id: The build_id of this ShowPipelineLastStatusV2Response.
        :type build_id: str
        """
        self._build_id = build_id

    @property
    def stages(self):
        """Gets the stages of this ShowPipelineLastStatusV2Response.

        阶段信息

        :return: The stages of this ShowPipelineLastStatusV2Response.
        :rtype: list[:class:`huaweicloudsdkdevstar.v1.PipelineStageResp`]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this ShowPipelineLastStatusV2Response.

        阶段信息

        :param stages: The stages of this ShowPipelineLastStatusV2Response.
        :type stages: list[:class:`huaweicloudsdkdevstar.v1.PipelineStageResp`]
        """
        self._stages = stages

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
        if not isinstance(other, ShowPipelineLastStatusV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
