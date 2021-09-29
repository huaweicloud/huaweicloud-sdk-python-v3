# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Task:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bench_concurrent': 'int',
        'description': 'str',
        'id': 'int',
        'name': 'str',
        'operate_mode': 'int',
        'task_run_info': 'TaskRunInfo',
        'update_time': 'str'
    }

    attribute_map = {
        'bench_concurrent': 'bench_concurrent',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'operate_mode': 'operate_mode',
        'task_run_info': 'task_run_info',
        'update_time': 'update_time'
    }

    def __init__(self, bench_concurrent=None, description=None, id=None, name=None, operate_mode=None, task_run_info=None, update_time=None):
        """Task - a model defined in huaweicloud sdk"""
        
        

        self._bench_concurrent = None
        self._description = None
        self._id = None
        self._name = None
        self._operate_mode = None
        self._task_run_info = None
        self._update_time = None
        self.discriminator = None

        if bench_concurrent is not None:
            self.bench_concurrent = bench_concurrent
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if operate_mode is not None:
            self.operate_mode = operate_mode
        if task_run_info is not None:
            self.task_run_info = task_run_info
        if update_time is not None:
            self.update_time = update_time

    @property
    def bench_concurrent(self):
        """Gets the bench_concurrent of this Task.

        bench_concurrent

        :return: The bench_concurrent of this Task.
        :rtype: int
        """
        return self._bench_concurrent

    @bench_concurrent.setter
    def bench_concurrent(self, bench_concurrent):
        """Sets the bench_concurrent of this Task.

        bench_concurrent

        :param bench_concurrent: The bench_concurrent of this Task.
        :type: int
        """
        self._bench_concurrent = bench_concurrent

    @property
    def description(self):
        """Gets the description of this Task.

        description

        :return: The description of this Task.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Task.

        description

        :param description: The description of this Task.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this Task.

        id

        :return: The id of this Task.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Task.

        id

        :param id: The id of this Task.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Task.

        name

        :return: The name of this Task.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Task.

        name

        :param name: The name of this Task.
        :type: str
        """
        self._name = name

    @property
    def operate_mode(self):
        """Gets the operate_mode of this Task.

        operate_mode

        :return: The operate_mode of this Task.
        :rtype: int
        """
        return self._operate_mode

    @operate_mode.setter
    def operate_mode(self, operate_mode):
        """Sets the operate_mode of this Task.

        operate_mode

        :param operate_mode: The operate_mode of this Task.
        :type: int
        """
        self._operate_mode = operate_mode

    @property
    def task_run_info(self):
        """Gets the task_run_info of this Task.


        :return: The task_run_info of this Task.
        :rtype: TaskRunInfo
        """
        return self._task_run_info

    @task_run_info.setter
    def task_run_info(self, task_run_info):
        """Sets the task_run_info of this Task.


        :param task_run_info: The task_run_info of this Task.
        :type: TaskRunInfo
        """
        self._task_run_info = task_run_info

    @property
    def update_time(self):
        """Gets the update_time of this Task.

        update_time

        :return: The update_time of this Task.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Task.

        update_time

        :param update_time: The update_time of this Task.
        :type: str
        """
        self._update_time = update_time

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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
