# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteGaussMySqlBackupResponse(SdkResponse):

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
        'backup_name': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'backup_name': 'backup_name'
    }

    def __init__(self, backup_id=None, backup_name=None):
        r"""DeleteGaussMySqlBackupResponse

        The model defined in huaweicloud sdk

        :param backup_id: 备份ID。
        :type backup_id: str
        :param backup_name: 备份名称。
        :type backup_name: str
        """
        
        super(DeleteGaussMySqlBackupResponse, self).__init__()

        self._backup_id = None
        self._backup_name = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if backup_name is not None:
            self.backup_name = backup_name

    @property
    def backup_id(self):
        r"""Gets the backup_id of this DeleteGaussMySqlBackupResponse.

        备份ID。

        :return: The backup_id of this DeleteGaussMySqlBackupResponse.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this DeleteGaussMySqlBackupResponse.

        备份ID。

        :param backup_id: The backup_id of this DeleteGaussMySqlBackupResponse.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backup_name(self):
        r"""Gets the backup_name of this DeleteGaussMySqlBackupResponse.

        备份名称。

        :return: The backup_name of this DeleteGaussMySqlBackupResponse.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        r"""Sets the backup_name of this DeleteGaussMySqlBackupResponse.

        备份名称。

        :param backup_name: The backup_name of this DeleteGaussMySqlBackupResponse.
        :type backup_name: str
        """
        self._backup_name = backup_name

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
        if not isinstance(other, DeleteGaussMySqlBackupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
