# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckJobNameIsExistsRequest:

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
        'job_name': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'job_name': 'job_name'
    }

    def __init__(self, project_id=None, job_name=None):
        r"""CheckJobNameIsExistsRequest

        The model defined in huaweicloud sdk

        :param project_id: CodeArts项目ID，32位数字、小写字母组合。
        :type project_id: str
        :param job_name: 任务名称
        :type job_name: str
        """
        
        

        self._project_id = None
        self._job_name = None
        self.discriminator = None

        self.project_id = project_id
        self.job_name = job_name

    @property
    def project_id(self):
        r"""Gets the project_id of this CheckJobNameIsExistsRequest.

        CodeArts项目ID，32位数字、小写字母组合。

        :return: The project_id of this CheckJobNameIsExistsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CheckJobNameIsExistsRequest.

        CodeArts项目ID，32位数字、小写字母组合。

        :param project_id: The project_id of this CheckJobNameIsExistsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def job_name(self):
        r"""Gets the job_name of this CheckJobNameIsExistsRequest.

        任务名称

        :return: The job_name of this CheckJobNameIsExistsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this CheckJobNameIsExistsRequest.

        任务名称

        :param job_name: The job_name of this CheckJobNameIsExistsRequest.
        :type job_name: str
        """
        self._job_name = job_name

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
        if not isinstance(other, CheckJobNameIsExistsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
