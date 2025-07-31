# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperProtectHostDirRequestInfo:

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
        'local_backup_dir': 'str'
    }

    attribute_map = {
        'protect_dir': 'protect_dir',
        'exclude_child_dir': 'exclude_child_dir',
        'exclude_file_path': 'exclude_file_path',
        'local_backup_dir': 'local_backup_dir'
    }

    def __init__(self, protect_dir=None, exclude_child_dir=None, exclude_file_path=None, local_backup_dir=None):
        r"""WebTamperProtectHostDirRequestInfo

        The model defined in huaweicloud sdk

        :param protect_dir: 防护目录
        :type protect_dir: str
        :param exclude_child_dir: 排除子目录
        :type exclude_child_dir: str
        :param exclude_file_path: 排除文件路径
        :type exclude_file_path: str
        :param local_backup_dir: 本地备份路径
        :type local_backup_dir: str
        """
        
        

        self._protect_dir = None
        self._exclude_child_dir = None
        self._exclude_file_path = None
        self._local_backup_dir = None
        self.discriminator = None

        if protect_dir is not None:
            self.protect_dir = protect_dir
        if exclude_child_dir is not None:
            self.exclude_child_dir = exclude_child_dir
        if exclude_file_path is not None:
            self.exclude_file_path = exclude_file_path
        if local_backup_dir is not None:
            self.local_backup_dir = local_backup_dir

    @property
    def protect_dir(self):
        r"""Gets the protect_dir of this WebTamperProtectHostDirRequestInfo.

        防护目录

        :return: The protect_dir of this WebTamperProtectHostDirRequestInfo.
        :rtype: str
        """
        return self._protect_dir

    @protect_dir.setter
    def protect_dir(self, protect_dir):
        r"""Sets the protect_dir of this WebTamperProtectHostDirRequestInfo.

        防护目录

        :param protect_dir: The protect_dir of this WebTamperProtectHostDirRequestInfo.
        :type protect_dir: str
        """
        self._protect_dir = protect_dir

    @property
    def exclude_child_dir(self):
        r"""Gets the exclude_child_dir of this WebTamperProtectHostDirRequestInfo.

        排除子目录

        :return: The exclude_child_dir of this WebTamperProtectHostDirRequestInfo.
        :rtype: str
        """
        return self._exclude_child_dir

    @exclude_child_dir.setter
    def exclude_child_dir(self, exclude_child_dir):
        r"""Sets the exclude_child_dir of this WebTamperProtectHostDirRequestInfo.

        排除子目录

        :param exclude_child_dir: The exclude_child_dir of this WebTamperProtectHostDirRequestInfo.
        :type exclude_child_dir: str
        """
        self._exclude_child_dir = exclude_child_dir

    @property
    def exclude_file_path(self):
        r"""Gets the exclude_file_path of this WebTamperProtectHostDirRequestInfo.

        排除文件路径

        :return: The exclude_file_path of this WebTamperProtectHostDirRequestInfo.
        :rtype: str
        """
        return self._exclude_file_path

    @exclude_file_path.setter
    def exclude_file_path(self, exclude_file_path):
        r"""Sets the exclude_file_path of this WebTamperProtectHostDirRequestInfo.

        排除文件路径

        :param exclude_file_path: The exclude_file_path of this WebTamperProtectHostDirRequestInfo.
        :type exclude_file_path: str
        """
        self._exclude_file_path = exclude_file_path

    @property
    def local_backup_dir(self):
        r"""Gets the local_backup_dir of this WebTamperProtectHostDirRequestInfo.

        本地备份路径

        :return: The local_backup_dir of this WebTamperProtectHostDirRequestInfo.
        :rtype: str
        """
        return self._local_backup_dir

    @local_backup_dir.setter
    def local_backup_dir(self, local_backup_dir):
        r"""Sets the local_backup_dir of this WebTamperProtectHostDirRequestInfo.

        本地备份路径

        :param local_backup_dir: The local_backup_dir of this WebTamperProtectHostDirRequestInfo.
        :type local_backup_dir: str
        """
        self._local_backup_dir = local_backup_dir

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
        if not isinstance(other, WebTamperProtectHostDirRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
