# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisableTheJobRequest:

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
        'body': 'DisableTheJobRequestBody'
    }

    attribute_map = {
        'job_id': 'job_id',
        'body': 'body'
    }

    def __init__(self, job_id=None, body=None):
        r"""DisableTheJobRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param body: Body of the DisableTheJobRequest
        :type body: :class:`huaweicloudsdkcodeartsbuild.v3.DisableTheJobRequestBody`
        """
        
        

        self._job_id = None
        self._body = None
        self.discriminator = None

        self.job_id = job_id
        if body is not None:
            self.body = body

    @property
    def job_id(self):
        r"""Gets the job_id of this DisableTheJobRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this DisableTheJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DisableTheJobRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this DisableTheJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def body(self):
        r"""Gets the body of this DisableTheJobRequest.

        :return: The body of this DisableTheJobRequest.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.DisableTheJobRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DisableTheJobRequest.

        :param body: The body of this DisableTheJobRequest.
        :type body: :class:`huaweicloudsdkcodeartsbuild.v3.DisableTheJobRequestBody`
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
        if not isinstance(other, DisableTheJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
