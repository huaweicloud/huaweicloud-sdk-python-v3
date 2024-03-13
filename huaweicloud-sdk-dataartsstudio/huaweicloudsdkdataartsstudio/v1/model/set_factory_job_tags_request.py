# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetFactoryJobTagsRequest:

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
        'job_name': 'str',
        'authorization': 'str',
        'host': 'str',
        'body': 'SetJobTagsRequestBody'
    }

    attribute_map = {
        'workspace': 'workspace',
        'job_name': 'job_name',
        'authorization': 'Authorization',
        'host': 'Host',
        'body': 'body'
    }

    def __init__(self, workspace=None, job_name=None, authorization=None, host=None, body=None):
        """SetFactoryJobTagsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param job_name: 作业名称.
        :type job_name: str
        :param authorization: 使用AK/SK进行认证时该字段必选
        :type authorization: str
        :param host: 使用AK/SK进行认证时该字段必选
        :type host: str
        :param body: Body of the SetFactoryJobTagsRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.SetJobTagsRequestBody`
        """
        
        

        self._workspace = None
        self._job_name = None
        self._authorization = None
        self._host = None
        self._body = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        self.job_name = job_name
        if authorization is not None:
            self.authorization = authorization
        if host is not None:
            self.host = host
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        """Gets the workspace of this SetFactoryJobTagsRequest.

        工作空间id

        :return: The workspace of this SetFactoryJobTagsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this SetFactoryJobTagsRequest.

        工作空间id

        :param workspace: The workspace of this SetFactoryJobTagsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def job_name(self):
        """Gets the job_name of this SetFactoryJobTagsRequest.

        作业名称.

        :return: The job_name of this SetFactoryJobTagsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this SetFactoryJobTagsRequest.

        作业名称.

        :param job_name: The job_name of this SetFactoryJobTagsRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def authorization(self):
        """Gets the authorization of this SetFactoryJobTagsRequest.

        使用AK/SK进行认证时该字段必选

        :return: The authorization of this SetFactoryJobTagsRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this SetFactoryJobTagsRequest.

        使用AK/SK进行认证时该字段必选

        :param authorization: The authorization of this SetFactoryJobTagsRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def host(self):
        """Gets the host of this SetFactoryJobTagsRequest.

        使用AK/SK进行认证时该字段必选

        :return: The host of this SetFactoryJobTagsRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SetFactoryJobTagsRequest.

        使用AK/SK进行认证时该字段必选

        :param host: The host of this SetFactoryJobTagsRequest.
        :type host: str
        """
        self._host = host

    @property
    def body(self):
        """Gets the body of this SetFactoryJobTagsRequest.

        :return: The body of this SetFactoryJobTagsRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.SetJobTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SetFactoryJobTagsRequest.

        :param body: The body of this SetFactoryJobTagsRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.SetJobTagsRequestBody`
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
        if not isinstance(other, SetFactoryJobTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
