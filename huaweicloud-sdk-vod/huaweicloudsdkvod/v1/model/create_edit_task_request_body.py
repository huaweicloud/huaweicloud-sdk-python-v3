# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEditTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inputs': 'list[EditMediaTaskInput]',
        'file_name': 'str',
        'editing_settings': 'EditingSetting',
        'callback_url': 'str',
        'session_context': 'str',
        'output': 'ObsInfo',
        'media_process_task': 'AdditionalObjectProcessReq'
    }

    attribute_map = {
        'inputs': 'inputs',
        'file_name': 'file_name',
        'editing_settings': 'editing_settings',
        'callback_url': 'callback_url',
        'session_context': 'session_context',
        'output': 'output',
        'media_process_task': 'media_process_task'
    }

    def __init__(self, inputs=None, file_name=None, editing_settings=None, callback_url=None, session_context=None, output=None, media_process_task=None):
        r"""CreateEditTaskRequestBody

        The model defined in huaweicloud sdk

        :param inputs: 编辑任务输入
        :type inputs: list[:class:`huaweicloudsdkvod.v1.EditMediaTaskInput`]
        :param file_name: 输出文件名
        :type file_name: str
        :param editing_settings: 
        :type editing_settings: :class:`huaweicloudsdkvod.v1.EditingSetting`
        :param callback_url: 回调地址
        :type callback_url: str
        :param session_context: 自定义上下文
        :type session_context: str
        :param output: 
        :type output: :class:`huaweicloudsdkvod.v1.ObsInfo`
        :param media_process_task: 
        :type media_process_task: :class:`huaweicloudsdkvod.v1.AdditionalObjectProcessReq`
        """
        
        

        self._inputs = None
        self._file_name = None
        self._editing_settings = None
        self._callback_url = None
        self._session_context = None
        self._output = None
        self._media_process_task = None
        self.discriminator = None

        self.inputs = inputs
        if file_name is not None:
            self.file_name = file_name
        if editing_settings is not None:
            self.editing_settings = editing_settings
        if callback_url is not None:
            self.callback_url = callback_url
        if session_context is not None:
            self.session_context = session_context
        self.output = output
        if media_process_task is not None:
            self.media_process_task = media_process_task

    @property
    def inputs(self):
        r"""Gets the inputs of this CreateEditTaskRequestBody.

        编辑任务输入

        :return: The inputs of this CreateEditTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkvod.v1.EditMediaTaskInput`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this CreateEditTaskRequestBody.

        编辑任务输入

        :param inputs: The inputs of this CreateEditTaskRequestBody.
        :type inputs: list[:class:`huaweicloudsdkvod.v1.EditMediaTaskInput`]
        """
        self._inputs = inputs

    @property
    def file_name(self):
        r"""Gets the file_name of this CreateEditTaskRequestBody.

        输出文件名

        :return: The file_name of this CreateEditTaskRequestBody.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this CreateEditTaskRequestBody.

        输出文件名

        :param file_name: The file_name of this CreateEditTaskRequestBody.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def editing_settings(self):
        r"""Gets the editing_settings of this CreateEditTaskRequestBody.

        :return: The editing_settings of this CreateEditTaskRequestBody.
        :rtype: :class:`huaweicloudsdkvod.v1.EditingSetting`
        """
        return self._editing_settings

    @editing_settings.setter
    def editing_settings(self, editing_settings):
        r"""Sets the editing_settings of this CreateEditTaskRequestBody.

        :param editing_settings: The editing_settings of this CreateEditTaskRequestBody.
        :type editing_settings: :class:`huaweicloudsdkvod.v1.EditingSetting`
        """
        self._editing_settings = editing_settings

    @property
    def callback_url(self):
        r"""Gets the callback_url of this CreateEditTaskRequestBody.

        回调地址

        :return: The callback_url of this CreateEditTaskRequestBody.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this CreateEditTaskRequestBody.

        回调地址

        :param callback_url: The callback_url of this CreateEditTaskRequestBody.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def session_context(self):
        r"""Gets the session_context of this CreateEditTaskRequestBody.

        自定义上下文

        :return: The session_context of this CreateEditTaskRequestBody.
        :rtype: str
        """
        return self._session_context

    @session_context.setter
    def session_context(self, session_context):
        r"""Sets the session_context of this CreateEditTaskRequestBody.

        自定义上下文

        :param session_context: The session_context of this CreateEditTaskRequestBody.
        :type session_context: str
        """
        self._session_context = session_context

    @property
    def output(self):
        r"""Gets the output of this CreateEditTaskRequestBody.

        :return: The output of this CreateEditTaskRequestBody.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this CreateEditTaskRequestBody.

        :param output: The output of this CreateEditTaskRequestBody.
        :type output: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._output = output

    @property
    def media_process_task(self):
        r"""Gets the media_process_task of this CreateEditTaskRequestBody.

        :return: The media_process_task of this CreateEditTaskRequestBody.
        :rtype: :class:`huaweicloudsdkvod.v1.AdditionalObjectProcessReq`
        """
        return self._media_process_task

    @media_process_task.setter
    def media_process_task(self, media_process_task):
        r"""Sets the media_process_task of this CreateEditTaskRequestBody.

        :param media_process_task: The media_process_task of this CreateEditTaskRequestBody.
        :type media_process_task: :class:`huaweicloudsdkvod.v1.AdditionalObjectProcessReq`
        """
        self._media_process_task = media_process_task

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
        if not isinstance(other, CreateEditTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
