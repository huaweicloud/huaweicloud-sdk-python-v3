# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone_id': 'str',
        'include_files': 'list[str]',
        'exclude_files': 'list[str]',
        'bucket_name': 'str',
        'object_path': 'str'
    }

    attribute_map = {
        'phone_id': 'phone_id',
        'include_files': 'include_files',
        'exclude_files': 'exclude_files',
        'bucket_name': 'bucket_name',
        'object_path': 'object_path'
    }

    def __init__(self, phone_id=None, include_files=None, exclude_files=None, bucket_name=None, object_path=None):
        r"""StorageInfo

        The model defined in huaweicloud sdk

        :param phone_id: 云手机ID。
        :type phone_id: str
        :param include_files: 需要导出数据的存储路径，绝对路径，最大长度4096字节。仅支持导出/data和、cache目录下的数据。目前只支持大小写字母、数字、小数点（.）、斜线（/）、中划线（-）、下划线（_）、加号（+）、井号（#）、星号（*）、等号这些字符。[文件导出打包时仅保留路径最后一级的文件权限、属主、标签等元数据，如对文件的上层目录权限有要求，建议参考[云手机数据备份与恢复](https://support.huaweicloud.com/api-cph/cph_api_0801.html)](tag:hws)。
        :type include_files: list[str]
        :param exclude_files: 不能导出数据的存储路径。exclude_files优先级比include_files高，如果冲突，exclude_files生效。 路径要求同include_files。
        :type exclude_files: list[str]
        :param bucket_name: 导出数据存储的OBS桶名。 合法的OBS桶名，3-63个字符，只能由小写字母、数字、中划线（-）和小数点（.）组成。
        :type bucket_name: str
        :param object_path: 导出数据存储的OBS路径名。 符合OBS的路径名规范，最大长度1024字符。目前只支持大小写字母、数字、小数点（.）、斜线（/）、中划线（-）、下划线（_）、加号（+）、井号（#）、等号这些字符。
        :type object_path: str
        """
        
        

        self._phone_id = None
        self._include_files = None
        self._exclude_files = None
        self._bucket_name = None
        self._object_path = None
        self.discriminator = None

        self.phone_id = phone_id
        self.include_files = include_files
        if exclude_files is not None:
            self.exclude_files = exclude_files
        self.bucket_name = bucket_name
        self.object_path = object_path

    @property
    def phone_id(self):
        r"""Gets the phone_id of this StorageInfo.

        云手机ID。

        :return: The phone_id of this StorageInfo.
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        r"""Sets the phone_id of this StorageInfo.

        云手机ID。

        :param phone_id: The phone_id of this StorageInfo.
        :type phone_id: str
        """
        self._phone_id = phone_id

    @property
    def include_files(self):
        r"""Gets the include_files of this StorageInfo.

        需要导出数据的存储路径，绝对路径，最大长度4096字节。仅支持导出/data和、cache目录下的数据。目前只支持大小写字母、数字、小数点（.）、斜线（/）、中划线（-）、下划线（_）、加号（+）、井号（#）、星号（*）、等号这些字符。[文件导出打包时仅保留路径最后一级的文件权限、属主、标签等元数据，如对文件的上层目录权限有要求，建议参考[云手机数据备份与恢复](https://support.huaweicloud.com/api-cph/cph_api_0801.html)](tag:hws)。

        :return: The include_files of this StorageInfo.
        :rtype: list[str]
        """
        return self._include_files

    @include_files.setter
    def include_files(self, include_files):
        r"""Sets the include_files of this StorageInfo.

        需要导出数据的存储路径，绝对路径，最大长度4096字节。仅支持导出/data和、cache目录下的数据。目前只支持大小写字母、数字、小数点（.）、斜线（/）、中划线（-）、下划线（_）、加号（+）、井号（#）、星号（*）、等号这些字符。[文件导出打包时仅保留路径最后一级的文件权限、属主、标签等元数据，如对文件的上层目录权限有要求，建议参考[云手机数据备份与恢复](https://support.huaweicloud.com/api-cph/cph_api_0801.html)](tag:hws)。

        :param include_files: The include_files of this StorageInfo.
        :type include_files: list[str]
        """
        self._include_files = include_files

    @property
    def exclude_files(self):
        r"""Gets the exclude_files of this StorageInfo.

        不能导出数据的存储路径。exclude_files优先级比include_files高，如果冲突，exclude_files生效。 路径要求同include_files。

        :return: The exclude_files of this StorageInfo.
        :rtype: list[str]
        """
        return self._exclude_files

    @exclude_files.setter
    def exclude_files(self, exclude_files):
        r"""Sets the exclude_files of this StorageInfo.

        不能导出数据的存储路径。exclude_files优先级比include_files高，如果冲突，exclude_files生效。 路径要求同include_files。

        :param exclude_files: The exclude_files of this StorageInfo.
        :type exclude_files: list[str]
        """
        self._exclude_files = exclude_files

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this StorageInfo.

        导出数据存储的OBS桶名。 合法的OBS桶名，3-63个字符，只能由小写字母、数字、中划线（-）和小数点（.）组成。

        :return: The bucket_name of this StorageInfo.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this StorageInfo.

        导出数据存储的OBS桶名。 合法的OBS桶名，3-63个字符，只能由小写字母、数字、中划线（-）和小数点（.）组成。

        :param bucket_name: The bucket_name of this StorageInfo.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_path(self):
        r"""Gets the object_path of this StorageInfo.

        导出数据存储的OBS路径名。 符合OBS的路径名规范，最大长度1024字符。目前只支持大小写字母、数字、小数点（.）、斜线（/）、中划线（-）、下划线（_）、加号（+）、井号（#）、等号这些字符。

        :return: The object_path of this StorageInfo.
        :rtype: str
        """
        return self._object_path

    @object_path.setter
    def object_path(self, object_path):
        r"""Sets the object_path of this StorageInfo.

        导出数据存储的OBS路径名。 符合OBS的路径名规范，最大长度1024字符。目前只支持大小写字母、数字、小数点（.）、斜线（/）、中划线（-）、下划线（_）、加号（+）、井号（#）、等号这些字符。

        :param object_path: The object_path of this StorageInfo.
        :type object_path: str
        """
        self._object_path = object_path

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
        if not isinstance(other, StorageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
