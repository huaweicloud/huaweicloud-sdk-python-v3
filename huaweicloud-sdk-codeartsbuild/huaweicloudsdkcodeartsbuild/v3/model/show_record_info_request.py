# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRecordInfoRequest:

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
        'build_no': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'build_no': 'build_no'
    }

    def __init__(self, job_id=None, build_no=None):
        r"""ShowRecordInfoRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param build_no: 构建任务的构建编号，从1开始，每次构建递增1
        :type build_no: int
        """
        
        

        self._job_id = None
        self._build_no = None
        self.discriminator = None

        self.job_id = job_id
        self.build_no = build_no

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowRecordInfoRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this ShowRecordInfoRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowRecordInfoRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this ShowRecordInfoRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def build_no(self):
        r"""Gets the build_no of this ShowRecordInfoRequest.

        构建任务的构建编号，从1开始，每次构建递增1

        :return: The build_no of this ShowRecordInfoRequest.
        :rtype: int
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        r"""Sets the build_no of this ShowRecordInfoRequest.

        构建任务的构建编号，从1开始，每次构建递增1

        :param build_no: The build_no of this ShowRecordInfoRequest.
        :type build_no: int
        """
        self._build_no = build_no

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
        if not isinstance(other, ShowRecordInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
