# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateReplicationJobRequest:

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
        'x_language': 'str',
        'body': 'ModifyOfflineTaskReq'
    }

    attribute_map = {
        'job_id': 'job_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, job_id=None, x_language=None, body=None):
        r"""UpdateReplicationJobRequest

        The model defined in huaweicloud sdk

        :param job_id: 备份迁移任务ID。
        :type job_id: str
        :param x_language: 请求语言类型。 en-us：英文 zh-cn：中文
        :type x_language: str
        :param body: Body of the UpdateReplicationJobRequest
        :type body: :class:`huaweicloudsdkdrs.v5.ModifyOfflineTaskReq`
        """
        
        

        self._job_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.job_id = job_id
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def job_id(self):
        r"""Gets the job_id of this UpdateReplicationJobRequest.

        备份迁移任务ID。

        :return: The job_id of this UpdateReplicationJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this UpdateReplicationJobRequest.

        备份迁移任务ID。

        :param job_id: The job_id of this UpdateReplicationJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_language(self):
        r"""Gets the x_language of this UpdateReplicationJobRequest.

        请求语言类型。 en-us：英文 zh-cn：中文

        :return: The x_language of this UpdateReplicationJobRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this UpdateReplicationJobRequest.

        请求语言类型。 en-us：英文 zh-cn：中文

        :param x_language: The x_language of this UpdateReplicationJobRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this UpdateReplicationJobRequest.

        :return: The body of this UpdateReplicationJobRequest.
        :rtype: :class:`huaweicloudsdkdrs.v5.ModifyOfflineTaskReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateReplicationJobRequest.

        :param body: The body of this UpdateReplicationJobRequest.
        :type body: :class:`huaweicloudsdkdrs.v5.ModifyOfflineTaskReq`
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
        if not isinstance(other, UpdateReplicationJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
