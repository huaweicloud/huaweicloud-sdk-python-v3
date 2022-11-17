# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInfos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'url': 'str',
        'task_type': 'str'
    }

    attribute_map = {
        'task_name': 'task_name',
        'url': 'url',
        'task_type': 'task_type'
    }

    def __init__(self, task_name=None, url=None, task_type=None):
        """TaskInfos

        The model defined in huaweicloud sdk

        :param task_name: 任务名称
        :type task_name: str
        :param url: 待扫描的目标网址
        :type url: str
        :param task_type: 扫描任务类型:   * normal - 普通任务   * monitor - 监测任务 
        :type task_type: str
        """
        
        

        self._task_name = None
        self._url = None
        self._task_type = None
        self.discriminator = None

        self.task_name = task_name
        self.url = url
        if task_type is not None:
            self.task_type = task_type

    @property
    def task_name(self):
        """Gets the task_name of this TaskInfos.

        任务名称

        :return: The task_name of this TaskInfos.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskInfos.

        任务名称

        :param task_name: The task_name of this TaskInfos.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def url(self):
        """Gets the url of this TaskInfos.

        待扫描的目标网址

        :return: The url of this TaskInfos.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TaskInfos.

        待扫描的目标网址

        :param url: The url of this TaskInfos.
        :type url: str
        """
        self._url = url

    @property
    def task_type(self):
        """Gets the task_type of this TaskInfos.

        扫描任务类型:   * normal - 普通任务   * monitor - 监测任务 

        :return: The task_type of this TaskInfos.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this TaskInfos.

        扫描任务类型:   * normal - 普通任务   * monitor - 监测任务 

        :param task_type: The task_type of this TaskInfos.
        :type task_type: str
        """
        self._task_type = task_type

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
        if not isinstance(other, TaskInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
