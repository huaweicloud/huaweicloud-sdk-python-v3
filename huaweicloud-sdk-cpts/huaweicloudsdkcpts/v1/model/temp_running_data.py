# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TempRunningData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_method_url': 'list[str]',
        'crawler_status': 'int',
        'related_temp_running_id': 'int',
        'task_run_info_id': 'int',
        'temp_id': 'int',
        'temp_name': 'str',
        'temp_running_status': 'int'
    }

    attribute_map = {
        'content_method_url': 'content_method_url',
        'crawler_status': 'crawler_status',
        'related_temp_running_id': 'related_temp_running_id',
        'task_run_info_id': 'task_run_info_id',
        'temp_id': 'temp_id',
        'temp_name': 'temp_name',
        'temp_running_status': 'temp_running_status'
    }

    def __init__(self, content_method_url=None, crawler_status=None, related_temp_running_id=None, task_run_info_id=None, temp_id=None, temp_name=None, temp_running_status=None):
        """TempRunningData

        The model defined in huaweicloud sdk

        :param content_method_url: content_method_url
        :type content_method_url: list[str]
        :param crawler_status: crawler_status
        :type crawler_status: int
        :param related_temp_running_id: related_temp_running_id
        :type related_temp_running_id: int
        :param task_run_info_id: task_run_info_id
        :type task_run_info_id: int
        :param temp_id: temp_id
        :type temp_id: int
        :param temp_name: temp_name
        :type temp_name: str
        :param temp_running_status: temp_running_status
        :type temp_running_status: int
        """
        
        

        self._content_method_url = None
        self._crawler_status = None
        self._related_temp_running_id = None
        self._task_run_info_id = None
        self._temp_id = None
        self._temp_name = None
        self._temp_running_status = None
        self.discriminator = None

        if content_method_url is not None:
            self.content_method_url = content_method_url
        if crawler_status is not None:
            self.crawler_status = crawler_status
        if related_temp_running_id is not None:
            self.related_temp_running_id = related_temp_running_id
        if task_run_info_id is not None:
            self.task_run_info_id = task_run_info_id
        if temp_id is not None:
            self.temp_id = temp_id
        if temp_name is not None:
            self.temp_name = temp_name
        if temp_running_status is not None:
            self.temp_running_status = temp_running_status

    @property
    def content_method_url(self):
        """Gets the content_method_url of this TempRunningData.

        content_method_url

        :return: The content_method_url of this TempRunningData.
        :rtype: list[str]
        """
        return self._content_method_url

    @content_method_url.setter
    def content_method_url(self, content_method_url):
        """Sets the content_method_url of this TempRunningData.

        content_method_url

        :param content_method_url: The content_method_url of this TempRunningData.
        :type content_method_url: list[str]
        """
        self._content_method_url = content_method_url

    @property
    def crawler_status(self):
        """Gets the crawler_status of this TempRunningData.

        crawler_status

        :return: The crawler_status of this TempRunningData.
        :rtype: int
        """
        return self._crawler_status

    @crawler_status.setter
    def crawler_status(self, crawler_status):
        """Sets the crawler_status of this TempRunningData.

        crawler_status

        :param crawler_status: The crawler_status of this TempRunningData.
        :type crawler_status: int
        """
        self._crawler_status = crawler_status

    @property
    def related_temp_running_id(self):
        """Gets the related_temp_running_id of this TempRunningData.

        related_temp_running_id

        :return: The related_temp_running_id of this TempRunningData.
        :rtype: int
        """
        return self._related_temp_running_id

    @related_temp_running_id.setter
    def related_temp_running_id(self, related_temp_running_id):
        """Sets the related_temp_running_id of this TempRunningData.

        related_temp_running_id

        :param related_temp_running_id: The related_temp_running_id of this TempRunningData.
        :type related_temp_running_id: int
        """
        self._related_temp_running_id = related_temp_running_id

    @property
    def task_run_info_id(self):
        """Gets the task_run_info_id of this TempRunningData.

        task_run_info_id

        :return: The task_run_info_id of this TempRunningData.
        :rtype: int
        """
        return self._task_run_info_id

    @task_run_info_id.setter
    def task_run_info_id(self, task_run_info_id):
        """Sets the task_run_info_id of this TempRunningData.

        task_run_info_id

        :param task_run_info_id: The task_run_info_id of this TempRunningData.
        :type task_run_info_id: int
        """
        self._task_run_info_id = task_run_info_id

    @property
    def temp_id(self):
        """Gets the temp_id of this TempRunningData.

        temp_id

        :return: The temp_id of this TempRunningData.
        :rtype: int
        """
        return self._temp_id

    @temp_id.setter
    def temp_id(self, temp_id):
        """Sets the temp_id of this TempRunningData.

        temp_id

        :param temp_id: The temp_id of this TempRunningData.
        :type temp_id: int
        """
        self._temp_id = temp_id

    @property
    def temp_name(self):
        """Gets the temp_name of this TempRunningData.

        temp_name

        :return: The temp_name of this TempRunningData.
        :rtype: str
        """
        return self._temp_name

    @temp_name.setter
    def temp_name(self, temp_name):
        """Sets the temp_name of this TempRunningData.

        temp_name

        :param temp_name: The temp_name of this TempRunningData.
        :type temp_name: str
        """
        self._temp_name = temp_name

    @property
    def temp_running_status(self):
        """Gets the temp_running_status of this TempRunningData.

        temp_running_status

        :return: The temp_running_status of this TempRunningData.
        :rtype: int
        """
        return self._temp_running_status

    @temp_running_status.setter
    def temp_running_status(self, temp_running_status):
        """Sets the temp_running_status of this TempRunningData.

        temp_running_status

        :param temp_running_status: The temp_running_status of this TempRunningData.
        :type temp_running_status: int
        """
        self._temp_running_status = temp_running_status

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
        if not isinstance(other, TempRunningData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
