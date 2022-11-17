# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunJobInBatch:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resume_savepoint': 'bool',
        'job_ids': 'list[int]'
    }

    attribute_map = {
        'resume_savepoint': 'resume_savepoint',
        'job_ids': 'job_ids'
    }

    def __init__(self, resume_savepoint=None, job_ids=None):
        """RunJobInBatch

        The model defined in huaweicloud sdk

        :param resume_savepoint: 是否将作业从最近创建的保存点恢复。类型为boolean。  当resume_savepoint为true时，表示作业从最近创建的保存点恢复。 当resume_savepoint为false时，表示不恢复正常启动。默认为false。
        :type resume_savepoint: bool
        :param job_ids: 
        :type job_ids: list[int]
        """
        
        

        self._resume_savepoint = None
        self._job_ids = None
        self.discriminator = None

        if resume_savepoint is not None:
            self.resume_savepoint = resume_savepoint
        self.job_ids = job_ids

    @property
    def resume_savepoint(self):
        """Gets the resume_savepoint of this RunJobInBatch.

        是否将作业从最近创建的保存点恢复。类型为boolean。  当resume_savepoint为true时，表示作业从最近创建的保存点恢复。 当resume_savepoint为false时，表示不恢复正常启动。默认为false。

        :return: The resume_savepoint of this RunJobInBatch.
        :rtype: bool
        """
        return self._resume_savepoint

    @resume_savepoint.setter
    def resume_savepoint(self, resume_savepoint):
        """Sets the resume_savepoint of this RunJobInBatch.

        是否将作业从最近创建的保存点恢复。类型为boolean。  当resume_savepoint为true时，表示作业从最近创建的保存点恢复。 当resume_savepoint为false时，表示不恢复正常启动。默认为false。

        :param resume_savepoint: The resume_savepoint of this RunJobInBatch.
        :type resume_savepoint: bool
        """
        self._resume_savepoint = resume_savepoint

    @property
    def job_ids(self):
        """Gets the job_ids of this RunJobInBatch.

        

        :return: The job_ids of this RunJobInBatch.
        :rtype: list[int]
        """
        return self._job_ids

    @job_ids.setter
    def job_ids(self, job_ids):
        """Sets the job_ids of this RunJobInBatch.

        

        :param job_ids: The job_ids of this RunJobInBatch.
        :type job_ids: list[int]
        """
        self._job_ids = job_ids

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
        if not isinstance(other, RunJobInBatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
