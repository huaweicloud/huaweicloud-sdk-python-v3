# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetryFactoryJobInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'workspace': 'str',
        'x_project_id': 'str',
        'body': 'RetryFactoryJobInstanceBody'
    }

    attribute_map = {
        'job_name': 'job_name',
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'body': 'body'
    }

    def __init__(self, job_name=None, workspace=None, x_project_id=None, body=None):
        r"""RetryFactoryJobInstanceRequest

        The model defined in huaweicloud sdk

        :param job_name: 当前作业名称
        :type job_name: str
        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param body: Body of the RetryFactoryJobInstanceRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.RetryFactoryJobInstanceBody`
        """
        
        

        self._job_name = None
        self._workspace = None
        self._x_project_id = None
        self._body = None
        self.discriminator = None

        self.job_name = job_name
        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if body is not None:
            self.body = body

    @property
    def job_name(self):
        r"""Gets the job_name of this RetryFactoryJobInstanceRequest.

        当前作业名称

        :return: The job_name of this RetryFactoryJobInstanceRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this RetryFactoryJobInstanceRequest.

        当前作业名称

        :param job_name: The job_name of this RetryFactoryJobInstanceRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def workspace(self):
        r"""Gets the workspace of this RetryFactoryJobInstanceRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this RetryFactoryJobInstanceRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this RetryFactoryJobInstanceRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this RetryFactoryJobInstanceRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this RetryFactoryJobInstanceRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this RetryFactoryJobInstanceRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this RetryFactoryJobInstanceRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this RetryFactoryJobInstanceRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def body(self):
        r"""Gets the body of this RetryFactoryJobInstanceRequest.

        :return: The body of this RetryFactoryJobInstanceRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.RetryFactoryJobInstanceBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this RetryFactoryJobInstanceRequest.

        :param body: The body of this RetryFactoryJobInstanceRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.RetryFactoryJobInstanceBody`
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
        if not isinstance(other, RetryFactoryJobInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
