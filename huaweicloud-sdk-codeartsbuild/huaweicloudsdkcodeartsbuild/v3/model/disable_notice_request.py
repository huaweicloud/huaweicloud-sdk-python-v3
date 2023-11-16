# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisableNoticeRequest:

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
        'notice_type': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'notice_type': 'notice_type'
    }

    def __init__(self, job_id=None, notice_type=None):
        """DisableNoticeRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param notice_type: 通知的类型,分为消息，邮件和钉钉
        :type notice_type: str
        """
        
        

        self._job_id = None
        self._notice_type = None
        self.discriminator = None

        self.job_id = job_id
        self.notice_type = notice_type

    @property
    def job_id(self):
        """Gets the job_id of this DisableNoticeRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this DisableNoticeRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DisableNoticeRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this DisableNoticeRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def notice_type(self):
        """Gets the notice_type of this DisableNoticeRequest.

        通知的类型,分为消息，邮件和钉钉

        :return: The notice_type of this DisableNoticeRequest.
        :rtype: str
        """
        return self._notice_type

    @notice_type.setter
    def notice_type(self, notice_type):
        """Sets the notice_type of this DisableNoticeRequest.

        通知的类型,分为消息，邮件和钉钉

        :param notice_type: The notice_type of this DisableNoticeRequest.
        :type notice_type: str
        """
        self._notice_type = notice_type

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
        if not isinstance(other, DisableNoticeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
