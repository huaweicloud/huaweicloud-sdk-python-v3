# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobPipelineInfoRequest:

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
        'all': 'str',
        'check_param_used': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'all': 'all',
        'check_param_used': 'check_param_used'
    }

    def __init__(self, job_id=None, all=None, check_param_used=None):
        r"""ShowJobPipelineInfoRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param all: 输入\&quot;true\&quot;或者\&quot;false\&quot;来控制返回参数是不是完整的
        :type all: str
        :param check_param_used: 移除未使用的参数
        :type check_param_used: str
        """
        
        

        self._job_id = None
        self._all = None
        self._check_param_used = None
        self.discriminator = None

        self.job_id = job_id
        if all is not None:
            self.all = all
        if check_param_used is not None:
            self.check_param_used = check_param_used

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowJobPipelineInfoRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this ShowJobPipelineInfoRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowJobPipelineInfoRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this ShowJobPipelineInfoRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def all(self):
        r"""Gets the all of this ShowJobPipelineInfoRequest.

        输入\"true\"或者\"false\"来控制返回参数是不是完整的

        :return: The all of this ShowJobPipelineInfoRequest.
        :rtype: str
        """
        return self._all

    @all.setter
    def all(self, all):
        r"""Sets the all of this ShowJobPipelineInfoRequest.

        输入\"true\"或者\"false\"来控制返回参数是不是完整的

        :param all: The all of this ShowJobPipelineInfoRequest.
        :type all: str
        """
        self._all = all

    @property
    def check_param_used(self):
        r"""Gets the check_param_used of this ShowJobPipelineInfoRequest.

        移除未使用的参数

        :return: The check_param_used of this ShowJobPipelineInfoRequest.
        :rtype: str
        """
        return self._check_param_used

    @check_param_used.setter
    def check_param_used(self, check_param_used):
        r"""Sets the check_param_used of this ShowJobPipelineInfoRequest.

        移除未使用的参数

        :param check_param_used: The check_param_used of this ShowJobPipelineInfoRequest.
        :type check_param_used: str
        """
        self._check_param_used = check_param_used

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
        if not isinstance(other, ShowJobPipelineInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
