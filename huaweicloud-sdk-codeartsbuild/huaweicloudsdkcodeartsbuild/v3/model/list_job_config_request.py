# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobConfigRequest:

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
        'get_all_params': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'get_all_params': 'get_all_params'
    }

    def __init__(self, job_id=None, get_all_params=None):
        """ListJobConfigRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param get_all_params: 输入\&quot;true\&quot;或者\&quot;false\&quot;来控制返回参数是不是完整的
        :type get_all_params: str
        """
        
        

        self._job_id = None
        self._get_all_params = None
        self.discriminator = None

        self.job_id = job_id
        if get_all_params is not None:
            self.get_all_params = get_all_params

    @property
    def job_id(self):
        """Gets the job_id of this ListJobConfigRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this ListJobConfigRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListJobConfigRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this ListJobConfigRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def get_all_params(self):
        """Gets the get_all_params of this ListJobConfigRequest.

        输入\"true\"或者\"false\"来控制返回参数是不是完整的

        :return: The get_all_params of this ListJobConfigRequest.
        :rtype: str
        """
        return self._get_all_params

    @get_all_params.setter
    def get_all_params(self, get_all_params):
        """Sets the get_all_params of this ListJobConfigRequest.

        输入\"true\"或者\"false\"来控制返回参数是不是完整的

        :param get_all_params: The get_all_params of this ListJobConfigRequest.
        :type get_all_params: str
        """
        self._get_all_params = get_all_params

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
        if not isinstance(other, ListJobConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
