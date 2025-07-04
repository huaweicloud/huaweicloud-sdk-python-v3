# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetTaskResultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'task_uri': 'str',
        'body': 'ExecuteTaskInfo'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'task_uri': 'task_uri',
        'body': 'body'
    }

    def __init__(self, project_uuid=None, task_uri=None, body=None):
        r"""SetTaskResultRequest

        The model defined in huaweicloud sdk

        :param project_uuid: 项目id
        :type project_uuid: str
        :param task_uri: 任务uri
        :type task_uri: str
        :param body: Body of the SetTaskResultRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.ExecuteTaskInfo`
        """
        
        

        self._project_uuid = None
        self._task_uri = None
        self._body = None
        self.discriminator = None

        self.project_uuid = project_uuid
        self.task_uri = task_uri
        if body is not None:
            self.body = body

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this SetTaskResultRequest.

        项目id

        :return: The project_uuid of this SetTaskResultRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this SetTaskResultRequest.

        项目id

        :param project_uuid: The project_uuid of this SetTaskResultRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def task_uri(self):
        r"""Gets the task_uri of this SetTaskResultRequest.

        任务uri

        :return: The task_uri of this SetTaskResultRequest.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this SetTaskResultRequest.

        任务uri

        :param task_uri: The task_uri of this SetTaskResultRequest.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def body(self):
        r"""Gets the body of this SetTaskResultRequest.

        :return: The body of this SetTaskResultRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ExecuteTaskInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SetTaskResultRequest.

        :param body: The body of this SetTaskResultRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.ExecuteTaskInfo`
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
        if not isinstance(other, SetTaskResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
