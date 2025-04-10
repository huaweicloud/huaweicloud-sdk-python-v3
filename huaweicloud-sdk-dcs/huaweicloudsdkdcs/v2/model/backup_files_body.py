# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupFilesBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_source': 'str',
        'bucket_name': 'str',
        'files': 'list[Files]',
        'backup_id': 'str'
    }

    attribute_map = {
        'file_source': 'file_source',
        'bucket_name': 'bucket_name',
        'files': 'files',
        'backup_id': 'backup_id'
    }

    def __init__(self, file_source=None, bucket_name=None, files=None, backup_id=None):
        r"""BackupFilesBody

        The model defined in huaweicloud sdk

        :param file_source: 数据来源，当前仅支持OBS桶方式，取值为：self_build_obs。
        :type file_source: str
        :param bucket_name: OBS桶名。
        :type bucket_name: str
        :param files: 导入的备份文件文件列表。
        :type files: list[:class:`huaweicloudsdkdcs.v2.Files`]
        :param backup_id: 备份记录ID，数据来源为备份记录时必须填写
        :type backup_id: str
        """
        
        

        self._file_source = None
        self._bucket_name = None
        self._files = None
        self._backup_id = None
        self.discriminator = None

        if file_source is not None:
            self.file_source = file_source
        if bucket_name is not None:
            self.bucket_name = bucket_name
        self.files = files
        if backup_id is not None:
            self.backup_id = backup_id

    @property
    def file_source(self):
        r"""Gets the file_source of this BackupFilesBody.

        数据来源，当前仅支持OBS桶方式，取值为：self_build_obs。

        :return: The file_source of this BackupFilesBody.
        :rtype: str
        """
        return self._file_source

    @file_source.setter
    def file_source(self, file_source):
        r"""Sets the file_source of this BackupFilesBody.

        数据来源，当前仅支持OBS桶方式，取值为：self_build_obs。

        :param file_source: The file_source of this BackupFilesBody.
        :type file_source: str
        """
        self._file_source = file_source

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this BackupFilesBody.

        OBS桶名。

        :return: The bucket_name of this BackupFilesBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this BackupFilesBody.

        OBS桶名。

        :param bucket_name: The bucket_name of this BackupFilesBody.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def files(self):
        r"""Gets the files of this BackupFilesBody.

        导入的备份文件文件列表。

        :return: The files of this BackupFilesBody.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.Files`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this BackupFilesBody.

        导入的备份文件文件列表。

        :param files: The files of this BackupFilesBody.
        :type files: list[:class:`huaweicloudsdkdcs.v2.Files`]
        """
        self._files = files

    @property
    def backup_id(self):
        r"""Gets the backup_id of this BackupFilesBody.

        备份记录ID，数据来源为备份记录时必须填写

        :return: The backup_id of this BackupFilesBody.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this BackupFilesBody.

        备份记录ID，数据来源为备份记录时必须填写

        :param backup_id: The backup_id of this BackupFilesBody.
        :type backup_id: str
        """
        self._backup_id = backup_id

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
        if not isinstance(other, BackupFilesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
