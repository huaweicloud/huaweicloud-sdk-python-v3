# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupInfoResp:

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
        'file_info': 'list[BackupFileResp]'
    }

    attribute_map = {
        'file_source': 'file_source',
        'bucket_name': 'bucket_name',
        'file_info': 'file_info'
    }

    def __init__(self, file_source=None, bucket_name=None, file_info=None):
        r"""BackupInfoResp

        The model defined in huaweicloud sdk

        :param file_source: 备份文件来源，包括OBS和RDS两种。
        :type file_source: str
        :param bucket_name: OBS桶名称。
        :type bucket_name: str
        :param file_info: 备份文件列表。
        :type file_info: list[:class:`huaweicloudsdkdrs.v5.BackupFileResp`]
        """
        
        

        self._file_source = None
        self._bucket_name = None
        self._file_info = None
        self.discriminator = None

        if file_source is not None:
            self.file_source = file_source
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if file_info is not None:
            self.file_info = file_info

    @property
    def file_source(self):
        r"""Gets the file_source of this BackupInfoResp.

        备份文件来源，包括OBS和RDS两种。

        :return: The file_source of this BackupInfoResp.
        :rtype: str
        """
        return self._file_source

    @file_source.setter
    def file_source(self, file_source):
        r"""Sets the file_source of this BackupInfoResp.

        备份文件来源，包括OBS和RDS两种。

        :param file_source: The file_source of this BackupInfoResp.
        :type file_source: str
        """
        self._file_source = file_source

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this BackupInfoResp.

        OBS桶名称。

        :return: The bucket_name of this BackupInfoResp.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this BackupInfoResp.

        OBS桶名称。

        :param bucket_name: The bucket_name of this BackupInfoResp.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def file_info(self):
        r"""Gets the file_info of this BackupInfoResp.

        备份文件列表。

        :return: The file_info of this BackupInfoResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.BackupFileResp`]
        """
        return self._file_info

    @file_info.setter
    def file_info(self, file_info):
        r"""Sets the file_info of this BackupInfoResp.

        备份文件列表。

        :param file_info: The file_info of this BackupInfoResp.
        :type file_info: list[:class:`huaweicloudsdkdrs.v5.BackupFileResp`]
        """
        self._file_info = file_info

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
        if not isinstance(other, BackupInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
