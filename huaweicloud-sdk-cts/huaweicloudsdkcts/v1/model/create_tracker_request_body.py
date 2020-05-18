# coding: utf-8

import pprint
import re

import six


class CreateTrackerRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'bucket_name': 'str',
        'file_prefix_name': 'str',
        'is_obs_created': 'bool',
        'is_support_trace_files_encryption': 'bool',
        'kms_id': 'str',
        'lts': 'Lts',
        'log_file_validate': 'LogFileValidate'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'file_prefix_name': 'file_prefix_name',
        'is_obs_created': 'is_obs_created',
        'is_support_trace_files_encryption': 'is_support_trace_files_encryption',
        'kms_id': 'kms_id',
        'lts': 'lts',
        'log_file_validate': 'log_file_validate'
    }

    def __init__(self, bucket_name=None, file_prefix_name=None, is_obs_created=None, is_support_trace_files_encryption=None, kms_id=None, lts=None, log_file_validate=None):  # noqa: E501
        """CreateTrackerRequestBody - a model defined in huaweicloud sdk"""

        self._bucket_name = None
        self._file_prefix_name = None
        self._is_obs_created = None
        self._is_support_trace_files_encryption = None
        self._kms_id = None
        self._lts = None
        self._log_file_validate = None
        self.discriminator = None

        self.bucket_name = bucket_name
        if file_prefix_name is not None:
            self.file_prefix_name = file_prefix_name
        if is_obs_created is not None:
            self.is_obs_created = is_obs_created
        if is_support_trace_files_encryption is not None:
            self.is_support_trace_files_encryption = is_support_trace_files_encryption
        if kms_id is not None:
            self.kms_id = kms_id
        if lts is not None:
            self.lts = lts
        if log_file_validate is not None:
            self.log_file_validate = log_file_validate

    @property
    def bucket_name(self):
        """Gets the bucket_name of this CreateTrackerRequestBody.

        标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。

        :return: The bucket_name of this CreateTrackerRequestBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this CreateTrackerRequestBody.

        标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。

        :param bucket_name: The bucket_name of this CreateTrackerRequestBody.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def file_prefix_name(self):
        """Gets the file_prefix_name of this CreateTrackerRequestBody.

        标识需要存储于OBS的日志文件前缀，0-9，a-z，A-Z，'-'，'.'，'_'长度为0～64字符。

        :return: The file_prefix_name of this CreateTrackerRequestBody.
        :rtype: str
        """
        return self._file_prefix_name

    @file_prefix_name.setter
    def file_prefix_name(self, file_prefix_name):
        """Sets the file_prefix_name of this CreateTrackerRequestBody.

        标识需要存储于OBS的日志文件前缀，0-9，a-z，A-Z，'-'，'.'，'_'长度为0～64字符。

        :param file_prefix_name: The file_prefix_name of this CreateTrackerRequestBody.
        :type: str
        """
        self._file_prefix_name = file_prefix_name

    @property
    def is_obs_created(self):
        """Gets the is_obs_created of this CreateTrackerRequestBody.

        是否支持新建OBS桶,默认为“false”。   值为“true”时，表示新创建OBS桶存储事件文件；   值为“false”时，选择已存在的OBS桶存储事件文件。 桶名称包含数字、字母、'-'和'.'（非数字、字母类字符最多存在1个），长度为3～64字符。

        :return: The is_obs_created of this CreateTrackerRequestBody.
        :rtype: bool
        """
        return self._is_obs_created

    @is_obs_created.setter
    def is_obs_created(self, is_obs_created):
        """Sets the is_obs_created of this CreateTrackerRequestBody.

        是否支持新建OBS桶,默认为“false”。   值为“true”时，表示新创建OBS桶存储事件文件；   值为“false”时，选择已存在的OBS桶存储事件文件。 桶名称包含数字、字母、'-'和'.'（非数字、字母类字符最多存在1个），长度为3～64字符。

        :param is_obs_created: The is_obs_created of this CreateTrackerRequestBody.
        :type: bool
        """
        self._is_obs_created = is_obs_created

    @property
    def is_support_trace_files_encryption(self):
        """Gets the is_support_trace_files_encryption of this CreateTrackerRequestBody.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。

        :return: The is_support_trace_files_encryption of this CreateTrackerRequestBody.
        :rtype: bool
        """
        return self._is_support_trace_files_encryption

    @is_support_trace_files_encryption.setter
    def is_support_trace_files_encryption(self, is_support_trace_files_encryption):
        """Sets the is_support_trace_files_encryption of this CreateTrackerRequestBody.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。

        :param is_support_trace_files_encryption: The is_support_trace_files_encryption of this CreateTrackerRequestBody.
        :type: bool
        """
        self._is_support_trace_files_encryption = is_support_trace_files_encryption

    @property
    def kms_id(self):
        """Gets the kms_id of this CreateTrackerRequestBody.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :return: The kms_id of this CreateTrackerRequestBody.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        """Sets the kms_id of this CreateTrackerRequestBody.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :param kms_id: The kms_id of this CreateTrackerRequestBody.
        :type: str
        """
        self._kms_id = kms_id

    @property
    def lts(self):
        """Gets the lts of this CreateTrackerRequestBody.


        :return: The lts of this CreateTrackerRequestBody.
        :rtype: Lts
        """
        return self._lts

    @lts.setter
    def lts(self, lts):
        """Sets the lts of this CreateTrackerRequestBody.


        :param lts: The lts of this CreateTrackerRequestBody.
        :type: Lts
        """
        self._lts = lts

    @property
    def log_file_validate(self):
        """Gets the log_file_validate of this CreateTrackerRequestBody.


        :return: The log_file_validate of this CreateTrackerRequestBody.
        :rtype: LogFileValidate
        """
        return self._log_file_validate

    @log_file_validate.setter
    def log_file_validate(self, log_file_validate):
        """Sets the log_file_validate of this CreateTrackerRequestBody.


        :param log_file_validate: The log_file_validate of this CreateTrackerRequestBody.
        :type: LogFileValidate
        """
        self._log_file_validate = log_file_validate

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateTrackerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
