# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RejectManualReviewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_run_id': 'str',
        'step_run_id': 'str',
        'project_id': 'str',
        'pipeline_id': 'str',
        'pipeline_run_id': 'str'
    }

    attribute_map = {
        'job_run_id': 'job_run_id',
        'step_run_id': 'step_run_id',
        'project_id': 'project_id',
        'pipeline_id': 'pipeline_id',
        'pipeline_run_id': 'pipeline_run_id'
    }

    def __init__(self, job_run_id=None, step_run_id=None, project_id=None, pipeline_id=None, pipeline_run_id=None):
        r"""RejectManualReviewRequest

        The model defined in huaweicloud sdk

        :param job_run_id: 流水线任务ID
        :type job_run_id: str
        :param step_run_id: 流水线步骤ID
        :type step_run_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param pipeline_id: 流水线ID
        :type pipeline_id: str
        :param pipeline_run_id: 流水线运行实例ID
        :type pipeline_run_id: str
        """
        
        

        self._job_run_id = None
        self._step_run_id = None
        self._project_id = None
        self._pipeline_id = None
        self._pipeline_run_id = None
        self.discriminator = None

        self.job_run_id = job_run_id
        self.step_run_id = step_run_id
        self.project_id = project_id
        self.pipeline_id = pipeline_id
        self.pipeline_run_id = pipeline_run_id

    @property
    def job_run_id(self):
        r"""Gets the job_run_id of this RejectManualReviewRequest.

        流水线任务ID

        :return: The job_run_id of this RejectManualReviewRequest.
        :rtype: str
        """
        return self._job_run_id

    @job_run_id.setter
    def job_run_id(self, job_run_id):
        r"""Sets the job_run_id of this RejectManualReviewRequest.

        流水线任务ID

        :param job_run_id: The job_run_id of this RejectManualReviewRequest.
        :type job_run_id: str
        """
        self._job_run_id = job_run_id

    @property
    def step_run_id(self):
        r"""Gets the step_run_id of this RejectManualReviewRequest.

        流水线步骤ID

        :return: The step_run_id of this RejectManualReviewRequest.
        :rtype: str
        """
        return self._step_run_id

    @step_run_id.setter
    def step_run_id(self, step_run_id):
        r"""Sets the step_run_id of this RejectManualReviewRequest.

        流水线步骤ID

        :param step_run_id: The step_run_id of this RejectManualReviewRequest.
        :type step_run_id: str
        """
        self._step_run_id = step_run_id

    @property
    def project_id(self):
        r"""Gets the project_id of this RejectManualReviewRequest.

        项目ID

        :return: The project_id of this RejectManualReviewRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RejectManualReviewRequest.

        项目ID

        :param project_id: The project_id of this RejectManualReviewRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def pipeline_id(self):
        r"""Gets the pipeline_id of this RejectManualReviewRequest.

        流水线ID

        :return: The pipeline_id of this RejectManualReviewRequest.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        r"""Sets the pipeline_id of this RejectManualReviewRequest.

        流水线ID

        :param pipeline_id: The pipeline_id of this RejectManualReviewRequest.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def pipeline_run_id(self):
        r"""Gets the pipeline_run_id of this RejectManualReviewRequest.

        流水线运行实例ID

        :return: The pipeline_run_id of this RejectManualReviewRequest.
        :rtype: str
        """
        return self._pipeline_run_id

    @pipeline_run_id.setter
    def pipeline_run_id(self, pipeline_run_id):
        r"""Sets the pipeline_run_id of this RejectManualReviewRequest.

        流水线运行实例ID

        :param pipeline_run_id: The pipeline_run_id of this RejectManualReviewRequest.
        :type pipeline_run_id: str
        """
        self._pipeline_run_id = pipeline_run_id

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
        if not isinstance(other, RejectManualReviewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
