# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'task_id': 'str',
        'body': 'MetadataCollectionTask'
    }

    attribute_map = {
        'workspace': 'workspace',
        'task_id': 'task_id',
        'body': 'body'
    }

    def __init__(self, workspace=None, task_id=None, body=None):
        r"""UpdateTaskInfoRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param task_id: 任务id
        :type task_id: str
        :param body: Body of the UpdateTaskInfoRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.MetadataCollectionTask`
        """
        
        

        self._workspace = None
        self._task_id = None
        self._body = None
        self.discriminator = None

        self.workspace = workspace
        self.task_id = task_id
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        r"""Gets the workspace of this UpdateTaskInfoRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this UpdateTaskInfoRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this UpdateTaskInfoRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this UpdateTaskInfoRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def task_id(self):
        r"""Gets the task_id of this UpdateTaskInfoRequest.

        任务id

        :return: The task_id of this UpdateTaskInfoRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this UpdateTaskInfoRequest.

        任务id

        :param task_id: The task_id of this UpdateTaskInfoRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def body(self):
        r"""Gets the body of this UpdateTaskInfoRequest.

        :return: The body of this UpdateTaskInfoRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.MetadataCollectionTask`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateTaskInfoRequest.

        :param body: The body of this UpdateTaskInfoRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.MetadataCollectionTask`
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
        if not isinstance(other, UpdateTaskInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
