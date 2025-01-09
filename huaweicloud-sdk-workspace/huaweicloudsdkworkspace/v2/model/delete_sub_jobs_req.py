# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSubJobsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_ids': 'list[str]',
        'delete_by_status': 'str'
    }

    attribute_map = {
        'job_ids': 'job_ids',
        'delete_by_status': 'delete_by_status'
    }

    def __init__(self, job_ids=None, delete_by_status=None):
        """DeleteSubJobsReq

        The model defined in huaweicloud sdk

        :param job_ids: 任务ID列表，只能删除SUCCESS、FAILED两种状态。job_ids和delete_by_status必传一个。
        :type job_ids: list[str]
        :param delete_by_status: 通过任务状态删除，只能删除以下的两种状态 SUCCESS：成功。 FAILED：失败。job_ids和delete_by_status必传一个。
        :type delete_by_status: str
        """
        
        

        self._job_ids = None
        self._delete_by_status = None
        self.discriminator = None

        if job_ids is not None:
            self.job_ids = job_ids
        if delete_by_status is not None:
            self.delete_by_status = delete_by_status

    @property
    def job_ids(self):
        """Gets the job_ids of this DeleteSubJobsReq.

        任务ID列表，只能删除SUCCESS、FAILED两种状态。job_ids和delete_by_status必传一个。

        :return: The job_ids of this DeleteSubJobsReq.
        :rtype: list[str]
        """
        return self._job_ids

    @job_ids.setter
    def job_ids(self, job_ids):
        """Sets the job_ids of this DeleteSubJobsReq.

        任务ID列表，只能删除SUCCESS、FAILED两种状态。job_ids和delete_by_status必传一个。

        :param job_ids: The job_ids of this DeleteSubJobsReq.
        :type job_ids: list[str]
        """
        self._job_ids = job_ids

    @property
    def delete_by_status(self):
        """Gets the delete_by_status of this DeleteSubJobsReq.

        通过任务状态删除，只能删除以下的两种状态 SUCCESS：成功。 FAILED：失败。job_ids和delete_by_status必传一个。

        :return: The delete_by_status of this DeleteSubJobsReq.
        :rtype: str
        """
        return self._delete_by_status

    @delete_by_status.setter
    def delete_by_status(self, delete_by_status):
        """Sets the delete_by_status of this DeleteSubJobsReq.

        通过任务状态删除，只能删除以下的两种状态 SUCCESS：成功。 FAILED：失败。job_ids和delete_by_status必传一个。

        :param delete_by_status: The delete_by_status of this DeleteSubJobsReq.
        :type delete_by_status: str
        """
        self._delete_by_status = delete_by_status

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
        if not isinstance(other, DeleteSubJobsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
