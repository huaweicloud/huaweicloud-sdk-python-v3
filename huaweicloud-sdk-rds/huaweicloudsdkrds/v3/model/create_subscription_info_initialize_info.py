# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscriptionInfoInitializeInfo:

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
        'backup_id': 'str',
        'bucket_name': 'str',
        'file_path': 'str',
        'file_name': 'str',
        'overwrite_restore': 'bool'
    }

    attribute_map = {
        'file_source': 'file_source',
        'backup_id': 'backup_id',
        'bucket_name': 'bucket_name',
        'file_path': 'file_path',
        'file_name': 'file_name',
        'overwrite_restore': 'overwrite_restore'
    }

    def __init__(self, file_source=None, backup_id=None, bucket_name=None, file_path=None, file_name=None, overwrite_restore=None):
        r"""CreateSubscriptionInfoInitializeInfo

        The model defined in huaweicloud sdk

        :param file_source: 初始化使用的文件源，仅支持OBS或BACKUP。
        :type file_source: str
        :param backup_id: 使用备份文件初始化的备份文件ID。
        :type backup_id: str
        :param bucket_name: 使用OBS内备份文件恢复的bucket名称。
        :type bucket_name: str
        :param file_path: OBS桶内备份文件的路径。
        :type file_path: str
        :param file_name: OBS桶内备份文件的名称。
        :type file_name: str
        :param overwrite_restore: 是否使用备份文件对订阅库进行覆盖还原。
        :type overwrite_restore: bool
        """
        
        

        self._file_source = None
        self._backup_id = None
        self._bucket_name = None
        self._file_path = None
        self._file_name = None
        self._overwrite_restore = None
        self.discriminator = None

        if file_source is not None:
            self.file_source = file_source
        if backup_id is not None:
            self.backup_id = backup_id
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if file_path is not None:
            self.file_path = file_path
        if file_name is not None:
            self.file_name = file_name
        if overwrite_restore is not None:
            self.overwrite_restore = overwrite_restore

    @property
    def file_source(self):
        r"""Gets the file_source of this CreateSubscriptionInfoInitializeInfo.

        初始化使用的文件源，仅支持OBS或BACKUP。

        :return: The file_source of this CreateSubscriptionInfoInitializeInfo.
        :rtype: str
        """
        return self._file_source

    @file_source.setter
    def file_source(self, file_source):
        r"""Sets the file_source of this CreateSubscriptionInfoInitializeInfo.

        初始化使用的文件源，仅支持OBS或BACKUP。

        :param file_source: The file_source of this CreateSubscriptionInfoInitializeInfo.
        :type file_source: str
        """
        self._file_source = file_source

    @property
    def backup_id(self):
        r"""Gets the backup_id of this CreateSubscriptionInfoInitializeInfo.

        使用备份文件初始化的备份文件ID。

        :return: The backup_id of this CreateSubscriptionInfoInitializeInfo.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this CreateSubscriptionInfoInitializeInfo.

        使用备份文件初始化的备份文件ID。

        :param backup_id: The backup_id of this CreateSubscriptionInfoInitializeInfo.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this CreateSubscriptionInfoInitializeInfo.

        使用OBS内备份文件恢复的bucket名称。

        :return: The bucket_name of this CreateSubscriptionInfoInitializeInfo.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this CreateSubscriptionInfoInitializeInfo.

        使用OBS内备份文件恢复的bucket名称。

        :param bucket_name: The bucket_name of this CreateSubscriptionInfoInitializeInfo.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def file_path(self):
        r"""Gets the file_path of this CreateSubscriptionInfoInitializeInfo.

        OBS桶内备份文件的路径。

        :return: The file_path of this CreateSubscriptionInfoInitializeInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this CreateSubscriptionInfoInitializeInfo.

        OBS桶内备份文件的路径。

        :param file_path: The file_path of this CreateSubscriptionInfoInitializeInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_name(self):
        r"""Gets the file_name of this CreateSubscriptionInfoInitializeInfo.

        OBS桶内备份文件的名称。

        :return: The file_name of this CreateSubscriptionInfoInitializeInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this CreateSubscriptionInfoInitializeInfo.

        OBS桶内备份文件的名称。

        :param file_name: The file_name of this CreateSubscriptionInfoInitializeInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def overwrite_restore(self):
        r"""Gets the overwrite_restore of this CreateSubscriptionInfoInitializeInfo.

        是否使用备份文件对订阅库进行覆盖还原。

        :return: The overwrite_restore of this CreateSubscriptionInfoInitializeInfo.
        :rtype: bool
        """
        return self._overwrite_restore

    @overwrite_restore.setter
    def overwrite_restore(self, overwrite_restore):
        r"""Sets the overwrite_restore of this CreateSubscriptionInfoInitializeInfo.

        是否使用备份文件对订阅库进行覆盖还原。

        :param overwrite_restore: The overwrite_restore of this CreateSubscriptionInfoInitializeInfo.
        :type overwrite_restore: bool
        """
        self._overwrite_restore = overwrite_restore

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
        if not isinstance(other, CreateSubscriptionInfoInitializeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
