# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBinlogTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'binlog_type': 'str',
        'file_name': 'str',
        'backup_id': 'str'
    }

    attribute_map = {
        'binlog_type': 'binlog_type',
        'file_name': 'file_name',
        'backup_id': 'backup_id'
    }

    def __init__(self, binlog_type=None, file_name=None, backup_id=None):
        r"""CreateBinlogTaskRequestBody

        The model defined in huaweicloud sdk

        :param binlog_type: binlog类型。取值范围：latest（最近日志）、backup（归档日志）、fragment（碎片备份日志）
        :type binlog_type: str
        :param file_name: binlog文件名称
        :type file_name: str
        :param backup_id: 归档ID
        :type backup_id: str
        """
        
        

        self._binlog_type = None
        self._file_name = None
        self._backup_id = None
        self.discriminator = None

        self.binlog_type = binlog_type
        self.file_name = file_name
        if backup_id is not None:
            self.backup_id = backup_id

    @property
    def binlog_type(self):
        r"""Gets the binlog_type of this CreateBinlogTaskRequestBody.

        binlog类型。取值范围：latest（最近日志）、backup（归档日志）、fragment（碎片备份日志）

        :return: The binlog_type of this CreateBinlogTaskRequestBody.
        :rtype: str
        """
        return self._binlog_type

    @binlog_type.setter
    def binlog_type(self, binlog_type):
        r"""Sets the binlog_type of this CreateBinlogTaskRequestBody.

        binlog类型。取值范围：latest（最近日志）、backup（归档日志）、fragment（碎片备份日志）

        :param binlog_type: The binlog_type of this CreateBinlogTaskRequestBody.
        :type binlog_type: str
        """
        self._binlog_type = binlog_type

    @property
    def file_name(self):
        r"""Gets the file_name of this CreateBinlogTaskRequestBody.

        binlog文件名称

        :return: The file_name of this CreateBinlogTaskRequestBody.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this CreateBinlogTaskRequestBody.

        binlog文件名称

        :param file_name: The file_name of this CreateBinlogTaskRequestBody.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def backup_id(self):
        r"""Gets the backup_id of this CreateBinlogTaskRequestBody.

        归档ID

        :return: The backup_id of this CreateBinlogTaskRequestBody.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this CreateBinlogTaskRequestBody.

        归档ID

        :param backup_id: The backup_id of this CreateBinlogTaskRequestBody.
        :type backup_id: str
        """
        self._backup_id = backup_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateBinlogTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
