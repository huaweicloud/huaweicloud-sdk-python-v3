# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResOnlineInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'job_id': 'str',
        'resource_id': 'str',
        'workspace_id': 'str',
        'body': 'UpdateResOnlineInstanceRequestBody'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'job_id': 'job_id',
        'resource_id': 'resource_id',
        'workspace_id': 'workspace_id',
        'body': 'body'
    }

    def __init__(self, content_type=None, job_id=None, resource_id=None, workspace_id=None, body=None):
        """UpdateResOnlineInstanceRequest

        The model defined in huaweicloud sdk

        :param content_type: 内容类型，取值为application/json。
        :type content_type: str
        :param job_id: 作业id。
        :type job_id: str
        :param resource_id: 资源id（数据源id或场景id）。
        :type resource_id: str
        :param workspace_id: 工作空间id。
        :type workspace_id: str
        :param body: Body of the UpdateResOnlineInstanceRequest
        :type body: :class:`huaweicloudsdkres.v1.UpdateResOnlineInstanceRequestBody`
        """
        
        

        self._content_type = None
        self._job_id = None
        self._resource_id = None
        self._workspace_id = None
        self._body = None
        self.discriminator = None

        self.content_type = content_type
        self.job_id = job_id
        self.resource_id = resource_id
        self.workspace_id = workspace_id
        if body is not None:
            self.body = body

    @property
    def content_type(self):
        """Gets the content_type of this UpdateResOnlineInstanceRequest.

        内容类型，取值为application/json。

        :return: The content_type of this UpdateResOnlineInstanceRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this UpdateResOnlineInstanceRequest.

        内容类型，取值为application/json。

        :param content_type: The content_type of this UpdateResOnlineInstanceRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def job_id(self):
        """Gets the job_id of this UpdateResOnlineInstanceRequest.

        作业id。

        :return: The job_id of this UpdateResOnlineInstanceRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateResOnlineInstanceRequest.

        作业id。

        :param job_id: The job_id of this UpdateResOnlineInstanceRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def resource_id(self):
        """Gets the resource_id of this UpdateResOnlineInstanceRequest.

        资源id（数据源id或场景id）。

        :return: The resource_id of this UpdateResOnlineInstanceRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this UpdateResOnlineInstanceRequest.

        资源id（数据源id或场景id）。

        :param resource_id: The resource_id of this UpdateResOnlineInstanceRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this UpdateResOnlineInstanceRequest.

        工作空间id。

        :return: The workspace_id of this UpdateResOnlineInstanceRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this UpdateResOnlineInstanceRequest.

        工作空间id。

        :param workspace_id: The workspace_id of this UpdateResOnlineInstanceRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def body(self):
        """Gets the body of this UpdateResOnlineInstanceRequest.

        :return: The body of this UpdateResOnlineInstanceRequest.
        :rtype: :class:`huaweicloudsdkres.v1.UpdateResOnlineInstanceRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateResOnlineInstanceRequest.

        :param body: The body of this UpdateResOnlineInstanceRequest.
        :type body: :class:`huaweicloudsdkres.v1.UpdateResOnlineInstanceRequestBody`
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
        if not isinstance(other, UpdateResOnlineInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
