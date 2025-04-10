# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateThumbnailsTaskResponse(SdkResponse):

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
        'output': 'ObsObjInfo',
        'output_file_name': 'str',
        'thumbnail_time': 'str',
        'description': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'create_time': 'create_time',
        'output': 'output',
        'output_file_name': 'output_file_name',
        'thumbnail_time': 'thumbnail_time',
        'description': 'description'
    }

    def __init__(self, task_id=None, status=None, create_time=None, output=None, output_file_name=None, thumbnail_time=None, description=None):
        r"""CreateThumbnailsTaskResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务ID。
        :type task_id: str
        :param status: 任务状态
        :type status: str
        :param create_time: 任务创建时间
        :type create_time: str
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output_file_name: 截图文件名称
        :type output_file_name: str
        :param thumbnail_time: 指定的截图时间点
        :type thumbnail_time: str
        :param description: 截图任务描述，当截图出现异常时，此字段为异常的原因
        :type description: str
        """
        
        super(CreateThumbnailsTaskResponse, self).__init__()

        self._task_id = None
        self._status = None
        self._create_time = None
        self._output = None
        self._output_file_name = None
        self._thumbnail_time = None
        self._description = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if output is not None:
            self.output = output
        if output_file_name is not None:
            self.output_file_name = output_file_name
        if thumbnail_time is not None:
            self.thumbnail_time = thumbnail_time
        if description is not None:
            self.description = description

    @property
    def task_id(self):
        r"""Gets the task_id of this CreateThumbnailsTaskResponse.

        任务ID。

        :return: The task_id of this CreateThumbnailsTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CreateThumbnailsTaskResponse.

        任务ID。

        :param task_id: The task_id of this CreateThumbnailsTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this CreateThumbnailsTaskResponse.

        任务状态

        :return: The status of this CreateThumbnailsTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateThumbnailsTaskResponse.

        任务状态

        :param status: The status of this CreateThumbnailsTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateThumbnailsTaskResponse.

        任务创建时间

        :return: The create_time of this CreateThumbnailsTaskResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateThumbnailsTaskResponse.

        任务创建时间

        :param create_time: The create_time of this CreateThumbnailsTaskResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def output(self):
        r"""Gets the output of this CreateThumbnailsTaskResponse.

        :return: The output of this CreateThumbnailsTaskResponse.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this CreateThumbnailsTaskResponse.

        :param output: The output of this CreateThumbnailsTaskResponse.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def output_file_name(self):
        r"""Gets the output_file_name of this CreateThumbnailsTaskResponse.

        截图文件名称

        :return: The output_file_name of this CreateThumbnailsTaskResponse.
        :rtype: str
        """
        return self._output_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        r"""Sets the output_file_name of this CreateThumbnailsTaskResponse.

        截图文件名称

        :param output_file_name: The output_file_name of this CreateThumbnailsTaskResponse.
        :type output_file_name: str
        """
        self._output_file_name = output_file_name

    @property
    def thumbnail_time(self):
        r"""Gets the thumbnail_time of this CreateThumbnailsTaskResponse.

        指定的截图时间点

        :return: The thumbnail_time of this CreateThumbnailsTaskResponse.
        :rtype: str
        """
        return self._thumbnail_time

    @thumbnail_time.setter
    def thumbnail_time(self, thumbnail_time):
        r"""Sets the thumbnail_time of this CreateThumbnailsTaskResponse.

        指定的截图时间点

        :param thumbnail_time: The thumbnail_time of this CreateThumbnailsTaskResponse.
        :type thumbnail_time: str
        """
        self._thumbnail_time = thumbnail_time

    @property
    def description(self):
        r"""Gets the description of this CreateThumbnailsTaskResponse.

        截图任务描述，当截图出现异常时，此字段为异常的原因

        :return: The description of this CreateThumbnailsTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateThumbnailsTaskResponse.

        截图任务描述，当截图出现异常时，此字段为异常的原因

        :param description: The description of this CreateThumbnailsTaskResponse.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateThumbnailsTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
