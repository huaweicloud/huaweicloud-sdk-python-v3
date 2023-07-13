# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIgnorePathRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'task_id': 'str',
        'body': 'UpdateIgnorePathRequestBody'
    }

    attribute_map = {
        'project_id': 'project_id',
        'task_id': 'task_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, task_id=None, body=None):
        """UpdateIgnorePathRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param task_id: 任务ID
        :type task_id: str
        :param body: Body of the UpdateIgnorePathRequest
        :type body: :class:`huaweicloudsdkcodeartscheck.v2.UpdateIgnorePathRequestBody`
        """
        
        

        self._project_id = None
        self._task_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.task_id = task_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        """Gets the project_id of this UpdateIgnorePathRequest.

        项目ID

        :return: The project_id of this UpdateIgnorePathRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateIgnorePathRequest.

        项目ID

        :param project_id: The project_id of this UpdateIgnorePathRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def task_id(self):
        """Gets the task_id of this UpdateIgnorePathRequest.

        任务ID

        :return: The task_id of this UpdateIgnorePathRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this UpdateIgnorePathRequest.

        任务ID

        :param task_id: The task_id of this UpdateIgnorePathRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def body(self):
        """Gets the body of this UpdateIgnorePathRequest.

        :return: The body of this UpdateIgnorePathRequest.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.UpdateIgnorePathRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateIgnorePathRequest.

        :param body: The body of this UpdateIgnorePathRequest.
        :type body: :class:`huaweicloudsdkcodeartscheck.v2.UpdateIgnorePathRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateIgnorePathRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
