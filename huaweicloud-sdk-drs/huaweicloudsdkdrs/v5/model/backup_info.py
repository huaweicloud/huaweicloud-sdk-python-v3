# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupInfo:

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
        'files': 'list[BackupFileInfo]'
    }

    attribute_map = {
        'file_source': 'file_source',
        'bucket_name': 'bucket_name',
        'files': 'files'
    }

    def __init__(self, file_source=None, bucket_name=None, files=None):
        r"""BackupInfo

        The model defined in huaweicloud sdk

        :param file_source: 备份文件来源：（全部大写） - OBS：存放在OBS中的备份文件。 - RDS：RDS实例的备份文件。
        :type file_source: str
        :param bucket_name: OBS桶名称，使用OBS桶备份文件恢复时必填。 约束：长度范围为3～63个字符，仅支持小写字母、数字、中划线（-）、点（.），且只能以字母或数字开头和结尾，禁止使用IP地址。 如果选择从OBS桶获取备份文件必填，参考登录[客户端登录](https://support.huaweicloud.com/clientogw-obs/zh-cn_topic_0045829058.html)OBS Browser客户端，首页为OBS桶列表，可以获取到备份文件所在桶的名称。
        :type bucket_name: str
        :param files: 备份文件信息列表。
        :type files: list[:class:`huaweicloudsdkdrs.v5.BackupFileInfo`]
        """
        
        

        self._file_source = None
        self._bucket_name = None
        self._files = None
        self.discriminator = None

        self.file_source = file_source
        if bucket_name is not None:
            self.bucket_name = bucket_name
        self.files = files

    @property
    def file_source(self):
        r"""Gets the file_source of this BackupInfo.

        备份文件来源：（全部大写） - OBS：存放在OBS中的备份文件。 - RDS：RDS实例的备份文件。

        :return: The file_source of this BackupInfo.
        :rtype: str
        """
        return self._file_source

    @file_source.setter
    def file_source(self, file_source):
        r"""Sets the file_source of this BackupInfo.

        备份文件来源：（全部大写） - OBS：存放在OBS中的备份文件。 - RDS：RDS实例的备份文件。

        :param file_source: The file_source of this BackupInfo.
        :type file_source: str
        """
        self._file_source = file_source

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this BackupInfo.

        OBS桶名称，使用OBS桶备份文件恢复时必填。 约束：长度范围为3～63个字符，仅支持小写字母、数字、中划线（-）、点（.），且只能以字母或数字开头和结尾，禁止使用IP地址。 如果选择从OBS桶获取备份文件必填，参考登录[客户端登录](https://support.huaweicloud.com/clientogw-obs/zh-cn_topic_0045829058.html)OBS Browser客户端，首页为OBS桶列表，可以获取到备份文件所在桶的名称。

        :return: The bucket_name of this BackupInfo.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this BackupInfo.

        OBS桶名称，使用OBS桶备份文件恢复时必填。 约束：长度范围为3～63个字符，仅支持小写字母、数字、中划线（-）、点（.），且只能以字母或数字开头和结尾，禁止使用IP地址。 如果选择从OBS桶获取备份文件必填，参考登录[客户端登录](https://support.huaweicloud.com/clientogw-obs/zh-cn_topic_0045829058.html)OBS Browser客户端，首页为OBS桶列表，可以获取到备份文件所在桶的名称。

        :param bucket_name: The bucket_name of this BackupInfo.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def files(self):
        r"""Gets the files of this BackupInfo.

        备份文件信息列表。

        :return: The files of this BackupInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.BackupFileInfo`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this BackupInfo.

        备份文件信息列表。

        :param files: The files of this BackupInfo.
        :type files: list[:class:`huaweicloudsdkdrs.v5.BackupFileInfo`]
        """
        self._files = files

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
        if not isinstance(other, BackupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
