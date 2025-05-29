# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobConfigDiffRequest:

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
        'revisedl_no': 'str',
        'original_no': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'revisedl_no': 'revisedl_no',
        'original_no': 'original_no'
    }

    def __init__(self, job_id=None, revisedl_no=None, original_no=None):
        r"""ShowJobConfigDiffRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param revisedl_no: 新记录的序号
        :type revisedl_no: str
        :param original_no: 原记录的序号
        :type original_no: str
        """
        
        

        self._job_id = None
        self._revisedl_no = None
        self._original_no = None
        self.discriminator = None

        self.job_id = job_id
        self.revisedl_no = revisedl_no
        self.original_no = original_no

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowJobConfigDiffRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this ShowJobConfigDiffRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowJobConfigDiffRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this ShowJobConfigDiffRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def revisedl_no(self):
        r"""Gets the revisedl_no of this ShowJobConfigDiffRequest.

        新记录的序号

        :return: The revisedl_no of this ShowJobConfigDiffRequest.
        :rtype: str
        """
        return self._revisedl_no

    @revisedl_no.setter
    def revisedl_no(self, revisedl_no):
        r"""Sets the revisedl_no of this ShowJobConfigDiffRequest.

        新记录的序号

        :param revisedl_no: The revisedl_no of this ShowJobConfigDiffRequest.
        :type revisedl_no: str
        """
        self._revisedl_no = revisedl_no

    @property
    def original_no(self):
        r"""Gets the original_no of this ShowJobConfigDiffRequest.

        原记录的序号

        :return: The original_no of this ShowJobConfigDiffRequest.
        :rtype: str
        """
        return self._original_no

    @original_no.setter
    def original_no(self, original_no):
        r"""Sets the original_no of this ShowJobConfigDiffRequest.

        原记录的序号

        :param original_no: The original_no of this ShowJobConfigDiffRequest.
        :type original_no: str
        """
        self._original_no = original_no

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
        if not isinstance(other, ShowJobConfigDiffRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
