# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetryInfo:

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
        'is_sync_re_edit': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'is_sync_re_edit': 'is_sync_re_edit'
    }

    def __init__(self, job_id=None, is_sync_re_edit=None):
        r"""RetryInfo

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param is_sync_re_edit: 再编辑之后启动，必填为true。
        :type is_sync_re_edit: bool
        """
        
        

        self._job_id = None
        self._is_sync_re_edit = None
        self.discriminator = None

        self.job_id = job_id
        if is_sync_re_edit is not None:
            self.is_sync_re_edit = is_sync_re_edit

    @property
    def job_id(self):
        r"""Gets the job_id of this RetryInfo.

        任务ID

        :return: The job_id of this RetryInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this RetryInfo.

        任务ID

        :param job_id: The job_id of this RetryInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def is_sync_re_edit(self):
        r"""Gets the is_sync_re_edit of this RetryInfo.

        再编辑之后启动，必填为true。

        :return: The is_sync_re_edit of this RetryInfo.
        :rtype: bool
        """
        return self._is_sync_re_edit

    @is_sync_re_edit.setter
    def is_sync_re_edit(self, is_sync_re_edit):
        r"""Sets the is_sync_re_edit of this RetryInfo.

        再编辑之后启动，必填为true。

        :param is_sync_re_edit: The is_sync_re_edit of this RetryInfo.
        :type is_sync_re_edit: bool
        """
        self._is_sync_re_edit = is_sync_re_edit

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
        if not isinstance(other, RetryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
