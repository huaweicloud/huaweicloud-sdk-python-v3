# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferBackupResponseBodyResults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'status': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'status': 'status',
        'job_id': 'job_id'
    }

    def __init__(self, backup_id=None, status=None, job_id=None):
        r"""TransferBackupResponseBodyResults

        The model defined in huaweicloud sdk

        :param backup_id: 备份id
        :type backup_id: str
        :param status: 任务提交状态
        :type status: str
        :param job_id: 任务id
        :type job_id: str
        """
        
        

        self._backup_id = None
        self._status = None
        self._job_id = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if status is not None:
            self.status = status
        if job_id is not None:
            self.job_id = job_id

    @property
    def backup_id(self):
        r"""Gets the backup_id of this TransferBackupResponseBodyResults.

        备份id

        :return: The backup_id of this TransferBackupResponseBodyResults.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this TransferBackupResponseBodyResults.

        备份id

        :param backup_id: The backup_id of this TransferBackupResponseBodyResults.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def status(self):
        r"""Gets the status of this TransferBackupResponseBodyResults.

        任务提交状态

        :return: The status of this TransferBackupResponseBodyResults.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TransferBackupResponseBodyResults.

        任务提交状态

        :param status: The status of this TransferBackupResponseBodyResults.
        :type status: str
        """
        self._status = status

    @property
    def job_id(self):
        r"""Gets the job_id of this TransferBackupResponseBodyResults.

        任务id

        :return: The job_id of this TransferBackupResponseBodyResults.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this TransferBackupResponseBodyResults.

        任务id

        :param job_id: The job_id of this TransferBackupResponseBodyResults.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, TransferBackupResponseBodyResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
