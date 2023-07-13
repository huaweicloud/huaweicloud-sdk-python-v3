# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGaussMySqlBackupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup': 'Backup',
        'job_id': 'str'
    }

    attribute_map = {
        'backup': 'backup',
        'job_id': 'job_id'
    }

    def __init__(self, backup=None, job_id=None):
        """CreateGaussMySqlBackupResponse

        The model defined in huaweicloud sdk

        :param backup: 
        :type backup: :class:`huaweicloudsdkgaussdb.v3.Backup`
        :param job_id: 任务ID。
        :type job_id: str
        """
        
        super(CreateGaussMySqlBackupResponse, self).__init__()

        self._backup = None
        self._job_id = None
        self.discriminator = None

        if backup is not None:
            self.backup = backup
        if job_id is not None:
            self.job_id = job_id

    @property
    def backup(self):
        """Gets the backup of this CreateGaussMySqlBackupResponse.

        :return: The backup of this CreateGaussMySqlBackupResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.Backup`
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        """Sets the backup of this CreateGaussMySqlBackupResponse.

        :param backup: The backup of this CreateGaussMySqlBackupResponse.
        :type backup: :class:`huaweicloudsdkgaussdb.v3.Backup`
        """
        self._backup = backup

    @property
    def job_id(self):
        """Gets the job_id of this CreateGaussMySqlBackupResponse.

        任务ID。

        :return: The job_id of this CreateGaussMySqlBackupResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateGaussMySqlBackupResponse.

        任务ID。

        :param job_id: The job_id of this CreateGaussMySqlBackupResponse.
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
        if not isinstance(other, CreateGaussMySqlBackupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
