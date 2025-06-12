# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDefaultProjectPermissionRequest:

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
        'job_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'job_id': 'job_id'
    }

    def __init__(self, project_id=None, job_id=None):
        r"""ShowDefaultProjectPermissionRequest

        The model defined in huaweicloud sdk

        :param project_id: CodeArts项目ID，32位数字、小写字母组合。
        :type project_id: str
        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        """
        
        

        self._project_id = None
        self._job_id = None
        self.discriminator = None

        self.project_id = project_id
        self.job_id = job_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowDefaultProjectPermissionRequest.

        CodeArts项目ID，32位数字、小写字母组合。

        :return: The project_id of this ShowDefaultProjectPermissionRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowDefaultProjectPermissionRequest.

        CodeArts项目ID，32位数字、小写字母组合。

        :param project_id: The project_id of this ShowDefaultProjectPermissionRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowDefaultProjectPermissionRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this ShowDefaultProjectPermissionRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowDefaultProjectPermissionRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this ShowDefaultProjectPermissionRequest.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ShowDefaultProjectPermissionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
