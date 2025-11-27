# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupDownloadLinkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'files': 'list[GetBackupDownloadLinkResponseBodyFiles]',
        'bucket': 'str',
        'group_id': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'files': 'files',
        'bucket': 'bucket',
        'group_id': 'group_id',
        'group_name': 'group_name'
    }

    def __init__(self, files=None, bucket=None, group_id=None, group_name=None):
        r"""ShowBackupDownloadLinkResponse

        The model defined in huaweicloud sdk

        :param files: 备份文件信息。
        :type files: list[:class:`huaweicloudsdkdds.v3.GetBackupDownloadLinkResponseBodyFiles`]
        :param bucket: OBS桶名。
        :type bucket: str
        :param group_id: 组ID。
        :type group_id: str
        :param group_name: 组名。
        :type group_name: str
        """
        
        super().__init__()

        self._files = None
        self._bucket = None
        self._group_id = None
        self._group_name = None
        self.discriminator = None

        if files is not None:
            self.files = files
        if bucket is not None:
            self.bucket = bucket
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name

    @property
    def files(self):
        r"""Gets the files of this ShowBackupDownloadLinkResponse.

        备份文件信息。

        :return: The files of this ShowBackupDownloadLinkResponse.
        :rtype: list[:class:`huaweicloudsdkdds.v3.GetBackupDownloadLinkResponseBodyFiles`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this ShowBackupDownloadLinkResponse.

        备份文件信息。

        :param files: The files of this ShowBackupDownloadLinkResponse.
        :type files: list[:class:`huaweicloudsdkdds.v3.GetBackupDownloadLinkResponseBodyFiles`]
        """
        self._files = files

    @property
    def bucket(self):
        r"""Gets the bucket of this ShowBackupDownloadLinkResponse.

        OBS桶名。

        :return: The bucket of this ShowBackupDownloadLinkResponse.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this ShowBackupDownloadLinkResponse.

        OBS桶名。

        :param bucket: The bucket of this ShowBackupDownloadLinkResponse.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowBackupDownloadLinkResponse.

        组ID。

        :return: The group_id of this ShowBackupDownloadLinkResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowBackupDownloadLinkResponse.

        组ID。

        :param group_id: The group_id of this ShowBackupDownloadLinkResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ShowBackupDownloadLinkResponse.

        组名。

        :return: The group_name of this ShowBackupDownloadLinkResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ShowBackupDownloadLinkResponse.

        组名。

        :param group_name: The group_name of this ShowBackupDownloadLinkResponse.
        :type group_name: str
        """
        self._group_name = group_name

    def to_dict(self):
        import warnings
        warnings.warn("ShowBackupDownloadLinkResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowBackupDownloadLinkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
