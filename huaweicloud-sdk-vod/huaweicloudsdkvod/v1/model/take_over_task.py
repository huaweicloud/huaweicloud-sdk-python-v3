# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TakeOverTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'object': 'str',
        'host_type': 'int',
        'output_bucket': 'str',
        'output_path': 'str',
        'task_id': 'str',
        'suffix': 'list[str]',
        'template_group_name': 'str',
        'create_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'exec_desc': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'object': 'object',
        'host_type': 'host_type',
        'output_bucket': 'output_bucket',
        'output_path': 'output_path',
        'task_id': 'task_id',
        'suffix': 'suffix',
        'template_group_name': 'template_group_name',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'status': 'status',
        'exec_desc': 'exec_desc'
    }

    def __init__(self, bucket=None, object=None, host_type=None, output_bucket=None, output_path=None, task_id=None, suffix=None, template_group_name=None, create_time=None, end_time=None, status=None, exec_desc=None):
        """TakeOverTask

        The model defined in huaweicloud sdk

        :param bucket: 桶名。
        :type bucket: str
        :param object: 目录/文件名。
        :type object: str
        :param host_type: 托管类型。  取值如下： - 0：表示存储到点播桶 - 1：表示存储在租户桶 - 2：表示存储到租户OBS桶中，且输出目录与源文件的存储目录相同。
        :type host_type: int
        :param output_bucket: 输出桶 。
        :type output_bucket: str
        :param output_path: 输出路径 。
        :type output_path: str
        :param task_id: 任务ID。
        :type task_id: str
        :param suffix: 托管文件类型。
        :type suffix: list[str]
        :param template_group_name: 转码模板组 。
        :type template_group_name: str
        :param create_time: 创建时间。
        :type create_time: str
        :param end_time: 结束时间。
        :type end_time: str
        :param status: 任务状态。
        :type status: str
        :param exec_desc: 媒资的任务执行描述汇总。
        :type exec_desc: str
        """
        
        

        self._bucket = None
        self._object = None
        self._host_type = None
        self._output_bucket = None
        self._output_path = None
        self._task_id = None
        self._suffix = None
        self._template_group_name = None
        self._create_time = None
        self._end_time = None
        self._status = None
        self._exec_desc = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if object is not None:
            self.object = object
        if host_type is not None:
            self.host_type = host_type
        if output_bucket is not None:
            self.output_bucket = output_bucket
        if output_path is not None:
            self.output_path = output_path
        if task_id is not None:
            self.task_id = task_id
        if suffix is not None:
            self.suffix = suffix
        if template_group_name is not None:
            self.template_group_name = template_group_name
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if exec_desc is not None:
            self.exec_desc = exec_desc

    @property
    def bucket(self):
        """Gets the bucket of this TakeOverTask.

        桶名。

        :return: The bucket of this TakeOverTask.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this TakeOverTask.

        桶名。

        :param bucket: The bucket of this TakeOverTask.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def object(self):
        """Gets the object of this TakeOverTask.

        目录/文件名。

        :return: The object of this TakeOverTask.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this TakeOverTask.

        目录/文件名。

        :param object: The object of this TakeOverTask.
        :type object: str
        """
        self._object = object

    @property
    def host_type(self):
        """Gets the host_type of this TakeOverTask.

        托管类型。  取值如下： - 0：表示存储到点播桶 - 1：表示存储在租户桶 - 2：表示存储到租户OBS桶中，且输出目录与源文件的存储目录相同。

        :return: The host_type of this TakeOverTask.
        :rtype: int
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this TakeOverTask.

        托管类型。  取值如下： - 0：表示存储到点播桶 - 1：表示存储在租户桶 - 2：表示存储到租户OBS桶中，且输出目录与源文件的存储目录相同。

        :param host_type: The host_type of this TakeOverTask.
        :type host_type: int
        """
        self._host_type = host_type

    @property
    def output_bucket(self):
        """Gets the output_bucket of this TakeOverTask.

        输出桶 。

        :return: The output_bucket of this TakeOverTask.
        :rtype: str
        """
        return self._output_bucket

    @output_bucket.setter
    def output_bucket(self, output_bucket):
        """Sets the output_bucket of this TakeOverTask.

        输出桶 。

        :param output_bucket: The output_bucket of this TakeOverTask.
        :type output_bucket: str
        """
        self._output_bucket = output_bucket

    @property
    def output_path(self):
        """Gets the output_path of this TakeOverTask.

        输出路径 。

        :return: The output_path of this TakeOverTask.
        :rtype: str
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        """Sets the output_path of this TakeOverTask.

        输出路径 。

        :param output_path: The output_path of this TakeOverTask.
        :type output_path: str
        """
        self._output_path = output_path

    @property
    def task_id(self):
        """Gets the task_id of this TakeOverTask.

        任务ID。

        :return: The task_id of this TakeOverTask.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TakeOverTask.

        任务ID。

        :param task_id: The task_id of this TakeOverTask.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def suffix(self):
        """Gets the suffix of this TakeOverTask.

        托管文件类型。

        :return: The suffix of this TakeOverTask.
        :rtype: list[str]
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this TakeOverTask.

        托管文件类型。

        :param suffix: The suffix of this TakeOverTask.
        :type suffix: list[str]
        """
        self._suffix = suffix

    @property
    def template_group_name(self):
        """Gets the template_group_name of this TakeOverTask.

        转码模板组 。

        :return: The template_group_name of this TakeOverTask.
        :rtype: str
        """
        return self._template_group_name

    @template_group_name.setter
    def template_group_name(self, template_group_name):
        """Sets the template_group_name of this TakeOverTask.

        转码模板组 。

        :param template_group_name: The template_group_name of this TakeOverTask.
        :type template_group_name: str
        """
        self._template_group_name = template_group_name

    @property
    def create_time(self):
        """Gets the create_time of this TakeOverTask.

        创建时间。

        :return: The create_time of this TakeOverTask.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TakeOverTask.

        创建时间。

        :param create_time: The create_time of this TakeOverTask.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        """Gets the end_time of this TakeOverTask.

        结束时间。

        :return: The end_time of this TakeOverTask.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TakeOverTask.

        结束时间。

        :param end_time: The end_time of this TakeOverTask.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this TakeOverTask.

        任务状态。

        :return: The status of this TakeOverTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TakeOverTask.

        任务状态。

        :param status: The status of this TakeOverTask.
        :type status: str
        """
        self._status = status

    @property
    def exec_desc(self):
        """Gets the exec_desc of this TakeOverTask.

        媒资的任务执行描述汇总。

        :return: The exec_desc of this TakeOverTask.
        :rtype: str
        """
        return self._exec_desc

    @exec_desc.setter
    def exec_desc(self, exec_desc):
        """Sets the exec_desc of this TakeOverTask.

        媒资的任务执行描述汇总。

        :param exec_desc: The exec_desc of this TakeOverTask.
        :type exec_desc: str
        """
        self._exec_desc = exec_desc

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
        if not isinstance(other, TakeOverTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
