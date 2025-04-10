# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportBackupReq:

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
        'export_path': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'export_path': 'export_path'
    }

    def __init__(self, backup_id=None, export_path=None):
        r"""ExportBackupReq

        The model defined in huaweicloud sdk

        :param backup_id: 备份ID
        :type backup_id: str
        :param export_path: 导出路径
        :type export_path: str
        """
        
        

        self._backup_id = None
        self._export_path = None
        self.discriminator = None

        self.backup_id = backup_id
        self.export_path = export_path

    @property
    def backup_id(self):
        r"""Gets the backup_id of this ExportBackupReq.

        备份ID

        :return: The backup_id of this ExportBackupReq.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this ExportBackupReq.

        备份ID

        :param backup_id: The backup_id of this ExportBackupReq.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def export_path(self):
        r"""Gets the export_path of this ExportBackupReq.

        导出路径

        :return: The export_path of this ExportBackupReq.
        :rtype: str
        """
        return self._export_path

    @export_path.setter
    def export_path(self, export_path):
        r"""Sets the export_path of this ExportBackupReq.

        导出路径

        :param export_path: The export_path of this ExportBackupReq.
        :type export_path: str
        """
        self._export_path = export_path

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
        if not isinstance(other, ExportBackupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
