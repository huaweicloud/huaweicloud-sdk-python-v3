# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobProgressEntities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'current_task': 'str',
        'image_name': 'str',
        'process_percent': 'float',
        'sub_job_id': 'str',
        'sub_jobs_result': 'list[SubJobResult]',
        'sub_jobs_list': 'list[str]'
    }

    attribute_map = {
        'image_id': 'image_id',
        'current_task': 'current_task',
        'image_name': 'image_name',
        'process_percent': 'process_percent',
        'sub_job_id': 'subJobId',
        'sub_jobs_result': 'sub_jobs_result',
        'sub_jobs_list': 'sub_jobs_list'
    }

    def __init__(self, image_id=None, current_task=None, image_name=None, process_percent=None, sub_job_id=None, sub_jobs_result=None, sub_jobs_list=None):
        r"""JobProgressEntities

        The model defined in huaweicloud sdk

        :param image_id: 镜像ID
        :type image_id: str
        :param current_task: 当前任务名称
        :type current_task: str
        :param image_name: 镜像名称
        :type image_name: str
        :param process_percent: 任务执行进度
        :type process_percent: float
        :param sub_job_id: 子任务ID
        :type sub_job_id: str
        :param sub_jobs_result: 子任务结果列表
        :type sub_jobs_result: list[:class:`huaweicloudsdkims.v2.SubJobResult`]
        :param sub_jobs_list: 子任务ID列表
        :type sub_jobs_list: list[str]
        """
        
        

        self._image_id = None
        self._current_task = None
        self._image_name = None
        self._process_percent = None
        self._sub_job_id = None
        self._sub_jobs_result = None
        self._sub_jobs_list = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if current_task is not None:
            self.current_task = current_task
        if image_name is not None:
            self.image_name = image_name
        if process_percent is not None:
            self.process_percent = process_percent
        if sub_job_id is not None:
            self.sub_job_id = sub_job_id
        if sub_jobs_result is not None:
            self.sub_jobs_result = sub_jobs_result
        if sub_jobs_list is not None:
            self.sub_jobs_list = sub_jobs_list

    @property
    def image_id(self):
        r"""Gets the image_id of this JobProgressEntities.

        镜像ID

        :return: The image_id of this JobProgressEntities.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this JobProgressEntities.

        镜像ID

        :param image_id: The image_id of this JobProgressEntities.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def current_task(self):
        r"""Gets the current_task of this JobProgressEntities.

        当前任务名称

        :return: The current_task of this JobProgressEntities.
        :rtype: str
        """
        return self._current_task

    @current_task.setter
    def current_task(self, current_task):
        r"""Sets the current_task of this JobProgressEntities.

        当前任务名称

        :param current_task: The current_task of this JobProgressEntities.
        :type current_task: str
        """
        self._current_task = current_task

    @property
    def image_name(self):
        r"""Gets the image_name of this JobProgressEntities.

        镜像名称

        :return: The image_name of this JobProgressEntities.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this JobProgressEntities.

        镜像名称

        :param image_name: The image_name of this JobProgressEntities.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def process_percent(self):
        r"""Gets the process_percent of this JobProgressEntities.

        任务执行进度

        :return: The process_percent of this JobProgressEntities.
        :rtype: float
        """
        return self._process_percent

    @process_percent.setter
    def process_percent(self, process_percent):
        r"""Sets the process_percent of this JobProgressEntities.

        任务执行进度

        :param process_percent: The process_percent of this JobProgressEntities.
        :type process_percent: float
        """
        self._process_percent = process_percent

    @property
    def sub_job_id(self):
        r"""Gets the sub_job_id of this JobProgressEntities.

        子任务ID

        :return: The sub_job_id of this JobProgressEntities.
        :rtype: str
        """
        return self._sub_job_id

    @sub_job_id.setter
    def sub_job_id(self, sub_job_id):
        r"""Sets the sub_job_id of this JobProgressEntities.

        子任务ID

        :param sub_job_id: The sub_job_id of this JobProgressEntities.
        :type sub_job_id: str
        """
        self._sub_job_id = sub_job_id

    @property
    def sub_jobs_result(self):
        r"""Gets the sub_jobs_result of this JobProgressEntities.

        子任务结果列表

        :return: The sub_jobs_result of this JobProgressEntities.
        :rtype: list[:class:`huaweicloudsdkims.v2.SubJobResult`]
        """
        return self._sub_jobs_result

    @sub_jobs_result.setter
    def sub_jobs_result(self, sub_jobs_result):
        r"""Sets the sub_jobs_result of this JobProgressEntities.

        子任务结果列表

        :param sub_jobs_result: The sub_jobs_result of this JobProgressEntities.
        :type sub_jobs_result: list[:class:`huaweicloudsdkims.v2.SubJobResult`]
        """
        self._sub_jobs_result = sub_jobs_result

    @property
    def sub_jobs_list(self):
        r"""Gets the sub_jobs_list of this JobProgressEntities.

        子任务ID列表

        :return: The sub_jobs_list of this JobProgressEntities.
        :rtype: list[str]
        """
        return self._sub_jobs_list

    @sub_jobs_list.setter
    def sub_jobs_list(self, sub_jobs_list):
        r"""Sets the sub_jobs_list of this JobProgressEntities.

        子任务ID列表

        :param sub_jobs_list: The sub_jobs_list of this JobProgressEntities.
        :type sub_jobs_list: list[str]
        """
        self._sub_jobs_list = sub_jobs_list

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
        if not isinstance(other, JobProgressEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
