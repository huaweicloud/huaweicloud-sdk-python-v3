# coding: utf-8

import pprint
import re

import six





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
        'output_url': 'str',
        'transcode_detail': 'TranscodeDetail',
        'thumbnail_output': 'ObsObjInfo',
        'thumbnail_outputname': 'str',
        'pic_info': 'list[PicInfo]',
        'audit_report': 'AuditReport'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
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
        'output_url': 'output_url',
        'transcode_detail': 'transcode_detail',
        'thumbnail_output': 'thumbnail_output',
        'thumbnail_outputname': 'thumbnail_outputname',
        'pic_info': 'pic_info',
        'audit_report': 'audit_report'
    }

    def __init__(self, task_id=None, status=None, create_time=None, end_time=None, trans_template_id=None, input=None, output=None, output_file_name=None, user_data=None, error_code=None, description=None, tips=None, output_url=None, transcode_detail=None, thumbnail_output=None, thumbnail_outputname=None, pic_info=None, audit_report=None):
        """QueryTranscodingsTaskResponse - a model defined in huaweicloud sdk"""
        
        

        self._task_id = None
        self._status = None
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
        self._output_url = None
        self._transcode_detail = None
        self._thumbnail_output = None
        self._thumbnail_outputname = None
        self._pic_info = None
        self._audit_report = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
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
        if output_url is not None:
            self.output_url = output_url
        if transcode_detail is not None:
            self.transcode_detail = transcode_detail
        if thumbnail_output is not None:
            self.thumbnail_output = thumbnail_output
        if thumbnail_outputname is not None:
            self.thumbnail_outputname = thumbnail_outputname
        if pic_info is not None:
            self.pic_info = pic_info
        if audit_report is not None:
            self.audit_report = audit_report

    @property
    def task_id(self):
        """Gets the task_id of this QueryTranscodingsTaskResponse.

        任务ID。

        :return: The task_id of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this QueryTranscodingsTaskResponse.

        任务ID。

        :param task_id: The task_id of this QueryTranscodingsTaskResponse.
        :type: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this QueryTranscodingsTaskResponse.

        任务执行状态。 

        :return: The status of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryTranscodingsTaskResponse.

        任务执行状态。 

        :param status: The status of this QueryTranscodingsTaskResponse.
        :type: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this QueryTranscodingsTaskResponse.

        转码任务启动时间 

        :return: The create_time of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryTranscodingsTaskResponse.

        转码任务启动时间 

        :param create_time: The create_time of this QueryTranscodingsTaskResponse.
        :type: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        """Gets the end_time of this QueryTranscodingsTaskResponse.

        转码任务结束时间 

        :return: The end_time of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QueryTranscodingsTaskResponse.

        转码任务结束时间 

        :param end_time: The end_time of this QueryTranscodingsTaskResponse.
        :type: str
        """
        self._end_time = end_time

    @property
    def trans_template_id(self):
        """Gets the trans_template_id of this QueryTranscodingsTaskResponse.

        转码任务对应的转码模板ID 

        :return: The trans_template_id of this QueryTranscodingsTaskResponse.
        :rtype: list[int]
        """
        return self._trans_template_id

    @trans_template_id.setter
    def trans_template_id(self, trans_template_id):
        """Sets the trans_template_id of this QueryTranscodingsTaskResponse.

        转码任务对应的转码模板ID 

        :param trans_template_id: The trans_template_id of this QueryTranscodingsTaskResponse.
        :type: list[int]
        """
        self._trans_template_id = trans_template_id

    @property
    def input(self):
        """Gets the input of this QueryTranscodingsTaskResponse.


        :return: The input of this QueryTranscodingsTaskResponse.
        :rtype: ObsObjInfo
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this QueryTranscodingsTaskResponse.


        :param input: The input of this QueryTranscodingsTaskResponse.
        :type: ObsObjInfo
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this QueryTranscodingsTaskResponse.


        :return: The output of this QueryTranscodingsTaskResponse.
        :rtype: ObsObjInfo
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this QueryTranscodingsTaskResponse.


        :param output: The output of this QueryTranscodingsTaskResponse.
        :type: ObsObjInfo
        """
        self._output = output

    @property
    def output_file_name(self):
        """Gets the output_file_name of this QueryTranscodingsTaskResponse.

        转码生成的文件名，数组类型，可能包含多个，包含截图文件名。 

        :return: The output_file_name of this QueryTranscodingsTaskResponse.
        :rtype: list[str]
        """
        return self._output_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        """Sets the output_file_name of this QueryTranscodingsTaskResponse.

        转码生成的文件名，数组类型，可能包含多个，包含截图文件名。 

        :param output_file_name: The output_file_name of this QueryTranscodingsTaskResponse.
        :type: list[str]
        """
        self._output_file_name = output_file_name

    @property
    def user_data(self):
        """Gets the user_data of this QueryTranscodingsTaskResponse.

        用户自定义数据。 

        :return: The user_data of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this QueryTranscodingsTaskResponse.

        用户自定义数据。 

        :param user_data: The user_data of this QueryTranscodingsTaskResponse.
        :type: str
        """
        self._user_data = user_data

    @property
    def error_code(self):
        """Gets the error_code of this QueryTranscodingsTaskResponse.

        转码任务的返回码。 

        :return: The error_code of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this QueryTranscodingsTaskResponse.

        转码任务的返回码。 

        :param error_code: The error_code of this QueryTranscodingsTaskResponse.
        :type: str
        """
        self._error_code = error_code

    @property
    def description(self):
        """Gets the description of this QueryTranscodingsTaskResponse.

        转码任务描述，当转码出现异常时，此字段为异常的原因。 

        :return: The description of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryTranscodingsTaskResponse.

        转码任务描述，当转码出现异常时，此字段为异常的原因。 

        :param description: The description of this QueryTranscodingsTaskResponse.
        :type: str
        """
        self._description = description

    @property
    def tips(self):
        """Gets the tips of this QueryTranscodingsTaskResponse.

        转码成功，但音频采样率过低时的提示。 

        :return: The tips of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._tips

    @tips.setter
    def tips(self, tips):
        """Sets the tips of this QueryTranscodingsTaskResponse.

        转码成功，但音频采样率过低时的提示。 

        :param tips: The tips of this QueryTranscodingsTaskResponse.
        :type: str
        """
        self._tips = tips

    @property
    def output_url(self):
        """Gets the output_url of this QueryTranscodingsTaskResponse.

        质检文件输出路径 

        :return: The output_url of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._output_url

    @output_url.setter
    def output_url(self, output_url):
        """Sets the output_url of this QueryTranscodingsTaskResponse.

        质检文件输出路径 

        :param output_url: The output_url of this QueryTranscodingsTaskResponse.
        :type: str
        """
        self._output_url = output_url

    @property
    def transcode_detail(self):
        """Gets the transcode_detail of this QueryTranscodingsTaskResponse.


        :return: The transcode_detail of this QueryTranscodingsTaskResponse.
        :rtype: TranscodeDetail
        """
        return self._transcode_detail

    @transcode_detail.setter
    def transcode_detail(self, transcode_detail):
        """Sets the transcode_detail of this QueryTranscodingsTaskResponse.


        :param transcode_detail: The transcode_detail of this QueryTranscodingsTaskResponse.
        :type: TranscodeDetail
        """
        self._transcode_detail = transcode_detail

    @property
    def thumbnail_output(self):
        """Gets the thumbnail_output of this QueryTranscodingsTaskResponse.


        :return: The thumbnail_output of this QueryTranscodingsTaskResponse.
        :rtype: ObsObjInfo
        """
        return self._thumbnail_output

    @thumbnail_output.setter
    def thumbnail_output(self, thumbnail_output):
        """Sets the thumbnail_output of this QueryTranscodingsTaskResponse.


        :param thumbnail_output: The thumbnail_output of this QueryTranscodingsTaskResponse.
        :type: ObsObjInfo
        """
        self._thumbnail_output = thumbnail_output

    @property
    def thumbnail_outputname(self):
        """Gets the thumbnail_outputname of this QueryTranscodingsTaskResponse.

        截图压缩包名。 

        :return: The thumbnail_outputname of this QueryTranscodingsTaskResponse.
        :rtype: str
        """
        return self._thumbnail_outputname

    @thumbnail_outputname.setter
    def thumbnail_outputname(self, thumbnail_outputname):
        """Sets the thumbnail_outputname of this QueryTranscodingsTaskResponse.

        截图压缩包名。 

        :param thumbnail_outputname: The thumbnail_outputname of this QueryTranscodingsTaskResponse.
        :type: str
        """
        self._thumbnail_outputname = thumbnail_outputname

    @property
    def pic_info(self):
        """Gets the pic_info of this QueryTranscodingsTaskResponse.

        截图文件信息。 

        :return: The pic_info of this QueryTranscodingsTaskResponse.
        :rtype: list[PicInfo]
        """
        return self._pic_info

    @pic_info.setter
    def pic_info(self, pic_info):
        """Sets the pic_info of this QueryTranscodingsTaskResponse.

        截图文件信息。 

        :param pic_info: The pic_info of this QueryTranscodingsTaskResponse.
        :type: list[PicInfo]
        """
        self._pic_info = pic_info

    @property
    def audit_report(self):
        """Gets the audit_report of this QueryTranscodingsTaskResponse.


        :return: The audit_report of this QueryTranscodingsTaskResponse.
        :rtype: AuditReport
        """
        return self._audit_report

    @audit_report.setter
    def audit_report(self, audit_report):
        """Sets the audit_report of this QueryTranscodingsTaskResponse.


        :param audit_report: The audit_report of this QueryTranscodingsTaskResponse.
        :type: AuditReport
        """
        self._audit_report = audit_report

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryTranscodingsTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
