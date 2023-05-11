# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunJobRequestBody:

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
        'parameter': 'list[ParameterItem]',
        'scm': 'Scm'
    }

    attribute_map = {
        'job_id': 'job_id',
        'parameter': 'parameter',
        'scm': 'scm'
    }

    def __init__(self, job_id=None, parameter=None, scm=None):
        """RunJobRequestBody

        The model defined in huaweicloud sdk

        :param job_id: 构建任务ID；编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串
        :type job_id: str
        :param parameter: 自定义参数
        :type parameter: list[:class:`huaweicloudsdkcodeartsbuild.v3.ParameterItem`]
        :param scm: 
        :type scm: :class:`huaweicloudsdkcodeartsbuild.v3.Scm`
        """
        
        

        self._job_id = None
        self._parameter = None
        self._scm = None
        self.discriminator = None

        self.job_id = job_id
        if parameter is not None:
            self.parameter = parameter
        if scm is not None:
            self.scm = scm

    @property
    def job_id(self):
        """Gets the job_id of this RunJobRequestBody.

        构建任务ID；编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串

        :return: The job_id of this RunJobRequestBody.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RunJobRequestBody.

        构建任务ID；编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串

        :param job_id: The job_id of this RunJobRequestBody.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def parameter(self):
        """Gets the parameter of this RunJobRequestBody.

        自定义参数

        :return: The parameter of this RunJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.ParameterItem`]
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this RunJobRequestBody.

        自定义参数

        :param parameter: The parameter of this RunJobRequestBody.
        :type parameter: list[:class:`huaweicloudsdkcodeartsbuild.v3.ParameterItem`]
        """
        self._parameter = parameter

    @property
    def scm(self):
        """Gets the scm of this RunJobRequestBody.

        :return: The scm of this RunJobRequestBody.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.Scm`
        """
        return self._scm

    @scm.setter
    def scm(self, scm):
        """Sets the scm of this RunJobRequestBody.

        :param scm: The scm of this RunJobRequestBody.
        :type scm: :class:`huaweicloudsdkcodeartsbuild.v3.Scm`
        """
        self._scm = scm

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
        if not isinstance(other, RunJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
