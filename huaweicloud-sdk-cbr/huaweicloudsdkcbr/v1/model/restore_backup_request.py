# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreBackupRequest:

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
        'body': 'BackupRestoreReq'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'body': 'body'
    }

    def __init__(self, backup_id=None, body=None):
        """RestoreBackupRequest

        The model defined in huaweicloud sdk

        :param backup_id: 备份id
        :type backup_id: str
        :param body: Body of the RestoreBackupRequest
        :type body: :class:`huaweicloudsdkcbr.v1.BackupRestoreReq`
        """
        
        

        self._backup_id = None
        self._body = None
        self.discriminator = None

        self.backup_id = backup_id
        if body is not None:
            self.body = body

    @property
    def backup_id(self):
        """Gets the backup_id of this RestoreBackupRequest.

        备份id

        :return: The backup_id of this RestoreBackupRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this RestoreBackupRequest.

        备份id

        :param backup_id: The backup_id of this RestoreBackupRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def body(self):
        """Gets the body of this RestoreBackupRequest.

        :return: The body of this RestoreBackupRequest.
        :rtype: :class:`huaweicloudsdkcbr.v1.BackupRestoreReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this RestoreBackupRequest.

        :param body: The body of this RestoreBackupRequest.
        :type body: :class:`huaweicloudsdkcbr.v1.BackupRestoreReq`
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
        if not isinstance(other, RestoreBackupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
