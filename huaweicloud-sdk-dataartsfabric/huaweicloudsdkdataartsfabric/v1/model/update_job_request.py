# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'workspace_id': 'str',
        'body': 'UpdateJobInput'
    }

    attribute_map = {
        'job_id': 'job_id',
        'workspace_id': 'workspace_id',
        'body': 'body'
    }

    def __init__(self, job_id=None, workspace_id=None, body=None):
        r"""UpdateJobRequest

        The model defined in huaweicloud sdk

        :param job_id: 作业 ID
        :type job_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param body: Body of the UpdateJobRequest
        :type body: :class:`huaweicloudsdkdataartsfabric.v1.UpdateJobInput`
        """
        
        

        self._job_id = None
        self._workspace_id = None
        self._body = None
        self.discriminator = None

        self.job_id = job_id
        self.workspace_id = workspace_id
        if body is not None:
            self.body = body

    @property
    def job_id(self):
        r"""Gets the job_id of this UpdateJobRequest.

        作业 ID

        :return: The job_id of this UpdateJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this UpdateJobRequest.

        作业 ID

        :param job_id: The job_id of this UpdateJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UpdateJobRequest.

        工作空间ID

        :return: The workspace_id of this UpdateJobRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UpdateJobRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this UpdateJobRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def body(self):
        r"""Gets the body of this UpdateJobRequest.

        :return: The body of this UpdateJobRequest.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.UpdateJobInput`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateJobRequest.

        :param body: The body of this UpdateJobRequest.
        :type body: :class:`huaweicloudsdkdataartsfabric.v1.UpdateJobInput`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
