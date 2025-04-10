# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobBatchDelete:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id_list': 'list[str]'
    }

    attribute_map = {
        'job_id_list': 'job_id_list'
    }

    def __init__(self, job_id_list=None):
        r"""JobBatchDelete

        The model defined in huaweicloud sdk

        :param job_id_list: 作业ID列表。获取方法，请参见[获取作业ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。
        :type job_id_list: list[str]
        """
        
        

        self._job_id_list = None
        self.discriminator = None

        if job_id_list is not None:
            self.job_id_list = job_id_list

    @property
    def job_id_list(self):
        r"""Gets the job_id_list of this JobBatchDelete.

        作业ID列表。获取方法，请参见[获取作业ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。

        :return: The job_id_list of this JobBatchDelete.
        :rtype: list[str]
        """
        return self._job_id_list

    @job_id_list.setter
    def job_id_list(self, job_id_list):
        r"""Sets the job_id_list of this JobBatchDelete.

        作业ID列表。获取方法，请参见[获取作业ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。

        :param job_id_list: The job_id_list of this JobBatchDelete.
        :type job_id_list: list[str]
        """
        self._job_id_list = job_id_list

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
        if not isinstance(other, JobBatchDelete):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
