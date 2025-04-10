# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTranscodingsTaskResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'status': 'str',
        'progress': 'int',
        'create_time': 'str',
        'end_time': 'str',
        'trans_template_id': 'list[int]',
        'input': 'ObsObjInfo',
        'output': 'ObsObjInfo',
        'output_file_name': 'list[str]',
        'user_data': 'str',
        'error_code': 'str',
        'description': 'str',
        'tips': 'str',
        'transcode_detail': 'TranscodeDetail',
        'thumbnail_output': 'ObsObjInfo',
        'thumbnail_outputname': 'str',
        'pic_info': 'list[PicInfo]',
        'av_parameters': 'list[AvParameters]',
        'additional_manifests': 'list[AdditionalManifests]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'progress': 'progress',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'trans_template_id': 'trans_template_id',
        'input': 'input',
        'output': 'output',
        'output_file_name': 'output_file_name',
        'user_data': 'user_data',
        'error_code': 'error_code',
        'description': 'description',
        'tips': 'tips',
        'transcode_detail': 'transcode_detail',
        'thumbnail_output': 'thumbnail_output',
        'thumbnail_outputname': 'thumbnail_outputname',
        'pic_info': 'pic_info',
        'av_parameters': 'av_parameters',
        'additional_manifests': 'additional_manifests'
    }

    def __init__(self, task_id=None, status=None, progress=None, create_time=None, end_time=None, trans_template_id=None, input=None, output=None, output_file_name=None, user_data=None, error_code=None, description=None, tips=None, transcode_detail=None, thumbnail_output=None, thumbnail_outputname=None, pic_info=None, av_parameters=None, additional_manifests=None):
        r"""QueryTranscodingsTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务ID。
        :type task_id: str
        :param status: 任务执行状态。 
        :type status: str
        :param progress: 任务执行进度百分比, 取值范围：[0, 100]。 
        :type progress: int
        :param create_time: 转码任务启动时间 
        :type create_time: str
        :param end_time: 转码任务结束时间 
        :type end_time: str
        :param trans_template_id: 转码任务对应的转码模板ID 
        :type trans_template_id: list[int]
        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output_file_name: 转码生成的文件名，数组类型，可能包含多个，包含截图文件名。 
        :type output_file_name: list[str]
        :param user_data: 用户自定义数据。 
        :type user_data: str
        :param error_code: 转码任务的返回码。 
        :type error_code: str
        :param description: 转码任务描述，当转码出现异常时，此字段为异常的原因。 
        :type description: str
        :param tips: 转码成功，但音频采样率过低时的提示。 
        :type tips: str
        :param transcode_detail: 
        :type transcode_detail: :class:`huaweicloudsdkmpc.v1.TranscodeDetail`
        :param thumbnail_output: 
        :type thumbnail_output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param thumbnail_outputname: 截图压缩包名。 
        :type thumbnail_outputname: str
        :param pic_info: 截图文件信息。 
        :type pic_info: list[:class:`huaweicloudsdkmpc.v1.PicInfo`]
        :param av_parameters: 转码参数。  若同时设置“trans_template_id”和此参数，则优先使用此参数进行转码。 
        :type av_parameters: list[:class:`huaweicloudsdkmpc.v1.AvParameters`]
        :param additional_manifests: 主索引定制参数。 
        :type additional_manifests: list[:class:`huaweicloudsdkmpc.v1.AdditionalManifests`]
        """
        
        

        self._task_id = None
        self._status = None
        self._progress = None
        self._create_time = None
        self._end_time = None
        self._trans_template_id = None
        self._input = None
        self._output = None
        self._output_file_name = None
        self._user_data = None
        self._error_code = None
        self._description = None
        self._tips = None
        self._transcode_detail = None
        self._thumbnail_output = None
        self._thumbnail_outputname = None
        self._pic_info = None
        self._av_parameters = None
        self._additional_manifests = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if trans_template_id is not None:
            self.trans_template_id = trans_template_id
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if output_file_name is not None:
            self.output_file_name = output_file_name
        if user_data is not None:
            self.user_data = user_data
        if error_code is not None:
            self.error_code = error_code
        if description is not None:
            self.description = description
        if tips is not None:
            self.tips = tips
        if transcode_detail is not None:
            self.transcode_detail = transcode_detail
        if thumbnail_output is not None:
            self.thumbnail_output = thumbnail_output
        if thumbnail_outputname is not None:
            self.thumbnail_outputname = thumbnail_outputname
        if pic_info is not None:
            self.pic_info = pic_info
        if av_parameters is not None:
            self.av_parameters = av_parameters
        if additional_manifests is not None:
            self.additional_manifests = additional_manifests

    @property
    def task_id(self):
        r"""Gets the task_id of this QueryTranscodingsTaskResponse.

        任务ID。

        :return: The task_id of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this QueryTranscodingsTaskResponse.

        任务ID。

        :param task_id: The task_id of this QueryTranscodingsTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this QueryTranscodingsTaskResponse.

        任务执行状态。 

        :return: The status of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryTranscodingsTaskResponse.

        任务执行状态。 

        :param status: The status of this QueryTranscodingsTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        r"""Gets the progress of this QueryTranscodingsTaskResponse.

        任务执行进度百分比, 取值范围：[0, 100]。 

        :return: The progress of this QueryTranscodingsTaskResponse.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this QueryTranscodingsTaskResponse.

        任务执行进度百分比, 取值范围：[0, 100]。 

        :param progress: The progress of this QueryTranscodingsTaskResponse.
        :type progress: int
        """
        self._progress = progress

    @property
    def create_time(self):
        r"""Gets the create_time of this QueryTranscodingsTaskResponse.

        转码任务启动时间 

        :return: The create_time of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this QueryTranscodingsTaskResponse.

        转码任务启动时间 

        :param create_time: The create_time of this QueryTranscodingsTaskResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this QueryTranscodingsTaskResponse.

        转码任务结束时间 

        :return: The end_time of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this QueryTranscodingsTaskResponse.

        转码任务结束时间 

        :param end_time: The end_time of this QueryTranscodingsTaskResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def trans_template_id(self):
        r"""Gets the trans_template_id of this QueryTranscodingsTaskResponse.

        转码任务对应的转码模板ID 

        :return: The trans_template_id of this QueryTranscodingsTaskResponse.
        :rtype: list[int]
        """
        return self._trans_template_id

    @trans_template_id.setter
    def trans_template_id(self, trans_template_id):
        r"""Sets the trans_template_id of this QueryTranscodingsTaskResponse.

        转码任务对应的转码模板ID 

        :param trans_template_id: The trans_template_id of this QueryTranscodingsTaskResponse.
        :type trans_template_id: list[int]
        """
        self._trans_template_id = trans_template_id

    @property
    def input(self):
        r"""Gets the input of this QueryTranscodingsTaskResponse.

        :return: The input of this QueryTranscodingsTaskResponse.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this QueryTranscodingsTaskResponse.

        :param input: The input of this QueryTranscodingsTaskResponse.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def output(self):
        r"""Gets the output of this QueryTranscodingsTaskResponse.

        :return: The output of this QueryTranscodingsTaskResponse.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this QueryTranscodingsTaskResponse.

        :param output: The output of this QueryTranscodingsTaskResponse.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def output_file_name(self):
        r"""Gets the output_file_name of this QueryTranscodingsTaskResponse.

        转码生成的文件名，数组类型，可能包含多个，包含截图文件名。 

        :return: The output_file_name of this QueryTranscodingsTaskResponse.
        :rtype: list[str]
        """
        return self._output_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        r"""Sets the output_file_name of this QueryTranscodingsTaskResponse.

        转码生成的文件名，数组类型，可能包含多个，包含截图文件名。 

        :param output_file_name: The output_file_name of this QueryTranscodingsTaskResponse.
        :type output_file_name: list[str]
        """
        self._output_file_name = output_file_name

    @property
    def user_data(self):
        r"""Gets the user_data of this QueryTranscodingsTaskResponse.

        用户自定义数据。 

        :return: The user_data of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this QueryTranscodingsTaskResponse.

        用户自定义数据。 

        :param user_data: The user_data of this QueryTranscodingsTaskResponse.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def error_code(self):
        r"""Gets the error_code of this QueryTranscodingsTaskResponse.

        转码任务的返回码。 

        :return: The error_code of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this QueryTranscodingsTaskResponse.

        转码任务的返回码。 

        :param error_code: The error_code of this QueryTranscodingsTaskResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def description(self):
        r"""Gets the description of this QueryTranscodingsTaskResponse.

        转码任务描述，当转码出现异常时，此字段为异常的原因。 

        :return: The description of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this QueryTranscodingsTaskResponse.

        转码任务描述，当转码出现异常时，此字段为异常的原因。 

        :param description: The description of this QueryTranscodingsTaskResponse.
        :type description: str
        """
        self._description = description

    @property
    def tips(self):
        r"""Gets the tips of this QueryTranscodingsTaskResponse.

        转码成功，但音频采样率过低时的提示。 

        :return: The tips of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._tips

    @tips.setter
    def tips(self, tips):
        r"""Sets the tips of this QueryTranscodingsTaskResponse.

        转码成功，但音频采样率过低时的提示。 

        :param tips: The tips of this QueryTranscodingsTaskResponse.
        :type tips: str
        """
        self._tips = tips

    @property
    def transcode_detail(self):
        r"""Gets the transcode_detail of this QueryTranscodingsTaskResponse.

        :return: The transcode_detail of this QueryTranscodingsTaskResponse.
        :rtype: :class:`huaweicloudsdkmpc.v1.TranscodeDetail`
        """
        return self._transcode_detail

    @transcode_detail.setter
    def transcode_detail(self, transcode_detail):
        r"""Sets the transcode_detail of this QueryTranscodingsTaskResponse.

        :param transcode_detail: The transcode_detail of this QueryTranscodingsTaskResponse.
        :type transcode_detail: :class:`huaweicloudsdkmpc.v1.TranscodeDetail`
        """
        self._transcode_detail = transcode_detail

    @property
    def thumbnail_output(self):
        r"""Gets the thumbnail_output of this QueryTranscodingsTaskResponse.

        :return: The thumbnail_output of this QueryTranscodingsTaskResponse.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._thumbnail_output

    @thumbnail_output.setter
    def thumbnail_output(self, thumbnail_output):
        r"""Sets the thumbnail_output of this QueryTranscodingsTaskResponse.

        :param thumbnail_output: The thumbnail_output of this QueryTranscodingsTaskResponse.
        :type thumbnail_output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._thumbnail_output = thumbnail_output

    @property
    def thumbnail_outputname(self):
        r"""Gets the thumbnail_outputname of this QueryTranscodingsTaskResponse.

        截图压缩包名。 

        :return: The thumbnail_outputname of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._thumbnail_outputname

    @thumbnail_outputname.setter
    def thumbnail_outputname(self, thumbnail_outputname):
        r"""Sets the thumbnail_outputname of this QueryTranscodingsTaskResponse.

        截图压缩包名。 

        :param thumbnail_outputname: The thumbnail_outputname of this QueryTranscodingsTaskResponse.
        :type thumbnail_outputname: str
        """
        self._thumbnail_outputname = thumbnail_outputname

    @property
    def pic_info(self):
        r"""Gets the pic_info of this QueryTranscodingsTaskResponse.

        截图文件信息。 

        :return: The pic_info of this QueryTranscodingsTaskResponse.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.PicInfo`]
        """
        return self._pic_info

    @pic_info.setter
    def pic_info(self, pic_info):
        r"""Sets the pic_info of this QueryTranscodingsTaskResponse.

        截图文件信息。 

        :param pic_info: The pic_info of this QueryTranscodingsTaskResponse.
        :type pic_info: list[:class:`huaweicloudsdkmpc.v1.PicInfo`]
        """
        self._pic_info = pic_info

    @property
    def av_parameters(self):
        r"""Gets the av_parameters of this QueryTranscodingsTaskResponse.

        转码参数。  若同时设置“trans_template_id”和此参数，则优先使用此参数进行转码。 

        :return: The av_parameters of this QueryTranscodingsTaskResponse.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.AvParameters`]
        """
        return self._av_parameters

    @av_parameters.setter
    def av_parameters(self, av_parameters):
        r"""Sets the av_parameters of this QueryTranscodingsTaskResponse.

        转码参数。  若同时设置“trans_template_id”和此参数，则优先使用此参数进行转码。 

        :param av_parameters: The av_parameters of this QueryTranscodingsTaskResponse.
        :type av_parameters: list[:class:`huaweicloudsdkmpc.v1.AvParameters`]
        """
        self._av_parameters = av_parameters

    @property
    def additional_manifests(self):
        r"""Gets the additional_manifests of this QueryTranscodingsTaskResponse.

        主索引定制参数。 

        :return: The additional_manifests of this QueryTranscodingsTaskResponse.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.AdditionalManifests`]
        """
        return self._additional_manifests

    @additional_manifests.setter
    def additional_manifests(self, additional_manifests):
        r"""Sets the additional_manifests of this QueryTranscodingsTaskResponse.

        主索引定制参数。 

        :param additional_manifests: The additional_manifests of this QueryTranscodingsTaskResponse.
        :type additional_manifests: list[:class:`huaweicloudsdkmpc.v1.AdditionalManifests`]
        """
        self._additional_manifests = additional_manifests

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
        if not isinstance(other, QueryTranscodingsTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
