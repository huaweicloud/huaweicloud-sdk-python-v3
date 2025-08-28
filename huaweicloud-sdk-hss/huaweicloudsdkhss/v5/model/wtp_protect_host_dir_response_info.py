# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WtpProtectHostDirResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_dir': 'str',
        'exclude_child_dir': 'str',
        'exclude_file_path': 'str',
        'exclue_file_path': 'str',
        'local_backup_dir': 'str',
        'protect_status': 'str',
        'error': 'str'
    }

    attribute_map = {
        'protect_dir': 'protect_dir',
        'exclude_child_dir': 'exclude_child_dir',
        'exclude_file_path': 'exclude_file_path',
        'exclue_file_path': 'exclue_file_path',
        'local_backup_dir': 'local_backup_dir',
        'protect_status': 'protect_status',
        'error': 'error'
    }

    def __init__(self, protect_dir=None, exclude_child_dir=None, exclude_file_path=None, exclue_file_path=None, local_backup_dir=None, protect_status=None, error=None):
        r"""WtpProtectHostDirResponseInfo

        The model defined in huaweicloud sdk

        :param protect_dir: **参数解释**: 防护目录 **取值范围**: 字符长度0-512位 
        :type protect_dir: str
        :param exclude_child_dir: **参数解释**: 排除子目录 **取值范围**: 字符长度0-512位 
        :type exclude_child_dir: str
        :param exclude_file_path: **参数解释**: 排除文件路径 **取值范围**: 字符长度0-512位 
        :type exclude_file_path: str
        :param exclue_file_path: 排除文件路径
        :type exclue_file_path: str
        :param local_backup_dir: **参数解释**: 本地备份路径 **取值范围**: 字符长度0-512位 
        :type local_backup_dir: str
        :param protect_status: **参数解释**: 防护状态 **取值范围**: - closed ：未开启。 - opened ：防护中。 - opening ：开启中。 - closing ：关闭中。 - open_failed ：防护失败。 
        :type protect_status: str
        :param error: **参数解释**: 失败原因，当防护状态为open_failed时存在失败原因 **取值范围**: 字符长度0-512位 
        :type error: str
        """
        
        

        self._protect_dir = None
        self._exclude_child_dir = None
        self._exclude_file_path = None
        self._exclue_file_path = None
        self._local_backup_dir = None
        self._protect_status = None
        self._error = None
        self.discriminator = None

        if protect_dir is not None:
            self.protect_dir = protect_dir
        if exclude_child_dir is not None:
            self.exclude_child_dir = exclude_child_dir
        if exclude_file_path is not None:
            self.exclude_file_path = exclude_file_path
        if exclue_file_path is not None:
            self.exclue_file_path = exclue_file_path
        if local_backup_dir is not None:
            self.local_backup_dir = local_backup_dir
        if protect_status is not None:
            self.protect_status = protect_status
        if error is not None:
            self.error = error

    @property
    def protect_dir(self):
        r"""Gets the protect_dir of this WtpProtectHostDirResponseInfo.

        **参数解释**: 防护目录 **取值范围**: 字符长度0-512位 

        :return: The protect_dir of this WtpProtectHostDirResponseInfo.
        :rtype: str
        """
        return self._protect_dir

    @protect_dir.setter
    def protect_dir(self, protect_dir):
        r"""Sets the protect_dir of this WtpProtectHostDirResponseInfo.

        **参数解释**: 防护目录 **取值范围**: 字符长度0-512位 

        :param protect_dir: The protect_dir of this WtpProtectHostDirResponseInfo.
        :type protect_dir: str
        """
        self._protect_dir = protect_dir

    @property
    def exclude_child_dir(self):
        r"""Gets the exclude_child_dir of this WtpProtectHostDirResponseInfo.

        **参数解释**: 排除子目录 **取值范围**: 字符长度0-512位 

        :return: The exclude_child_dir of this WtpProtectHostDirResponseInfo.
        :rtype: str
        """
        return self._exclude_child_dir

    @exclude_child_dir.setter
    def exclude_child_dir(self, exclude_child_dir):
        r"""Sets the exclude_child_dir of this WtpProtectHostDirResponseInfo.

        **参数解释**: 排除子目录 **取值范围**: 字符长度0-512位 

        :param exclude_child_dir: The exclude_child_dir of this WtpProtectHostDirResponseInfo.
        :type exclude_child_dir: str
        """
        self._exclude_child_dir = exclude_child_dir

    @property
    def exclude_file_path(self):
        r"""Gets the exclude_file_path of this WtpProtectHostDirResponseInfo.

        **参数解释**: 排除文件路径 **取值范围**: 字符长度0-512位 

        :return: The exclude_file_path of this WtpProtectHostDirResponseInfo.
        :rtype: str
        """
        return self._exclude_file_path

    @exclude_file_path.setter
    def exclude_file_path(self, exclude_file_path):
        r"""Sets the exclude_file_path of this WtpProtectHostDirResponseInfo.

        **参数解释**: 排除文件路径 **取值范围**: 字符长度0-512位 

        :param exclude_file_path: The exclude_file_path of this WtpProtectHostDirResponseInfo.
        :type exclude_file_path: str
        """
        self._exclude_file_path = exclude_file_path

    @property
    def exclue_file_path(self):
        r"""Gets the exclue_file_path of this WtpProtectHostDirResponseInfo.

        排除文件路径

        :return: The exclue_file_path of this WtpProtectHostDirResponseInfo.
        :rtype: str
        """
        return self._exclue_file_path

    @exclue_file_path.setter
    def exclue_file_path(self, exclue_file_path):
        r"""Sets the exclue_file_path of this WtpProtectHostDirResponseInfo.

        排除文件路径

        :param exclue_file_path: The exclue_file_path of this WtpProtectHostDirResponseInfo.
        :type exclue_file_path: str
        """
        self._exclue_file_path = exclue_file_path

    @property
    def local_backup_dir(self):
        r"""Gets the local_backup_dir of this WtpProtectHostDirResponseInfo.

        **参数解释**: 本地备份路径 **取值范围**: 字符长度0-512位 

        :return: The local_backup_dir of this WtpProtectHostDirResponseInfo.
        :rtype: str
        """
        return self._local_backup_dir

    @local_backup_dir.setter
    def local_backup_dir(self, local_backup_dir):
        r"""Sets the local_backup_dir of this WtpProtectHostDirResponseInfo.

        **参数解释**: 本地备份路径 **取值范围**: 字符长度0-512位 

        :param local_backup_dir: The local_backup_dir of this WtpProtectHostDirResponseInfo.
        :type local_backup_dir: str
        """
        self._local_backup_dir = local_backup_dir

    @property
    def protect_status(self):
        r"""Gets the protect_status of this WtpProtectHostDirResponseInfo.

        **参数解释**: 防护状态 **取值范围**: - closed ：未开启。 - opened ：防护中。 - opening ：开启中。 - closing ：关闭中。 - open_failed ：防护失败。 

        :return: The protect_status of this WtpProtectHostDirResponseInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this WtpProtectHostDirResponseInfo.

        **参数解释**: 防护状态 **取值范围**: - closed ：未开启。 - opened ：防护中。 - opening ：开启中。 - closing ：关闭中。 - open_failed ：防护失败。 

        :param protect_status: The protect_status of this WtpProtectHostDirResponseInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def error(self):
        r"""Gets the error of this WtpProtectHostDirResponseInfo.

        **参数解释**: 失败原因，当防护状态为open_failed时存在失败原因 **取值范围**: 字符长度0-512位 

        :return: The error of this WtpProtectHostDirResponseInfo.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this WtpProtectHostDirResponseInfo.

        **参数解释**: 失败原因，当防护状态为open_failed时存在失败原因 **取值范围**: 字符长度0-512位 

        :param error: The error of this WtpProtectHostDirResponseInfo.
        :type error: str
        """
        self._error = error

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
        if not isinstance(other, WtpProtectHostDirResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
