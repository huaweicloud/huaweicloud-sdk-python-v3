# coding: utf-8

import pprint
import re

import six


class ListTrackerResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'id': 'str',
        'create_time': 'int',
        'domain_id': 'str',
        'project_id': 'str',
        'tracker_name': 'str',
        'bucket_name': 'str',
        'file_prefix_name': 'str',
        'status': 'str',
        'detail': 'str',
        'is_obs_created': 'bool',
        'is_support_trace_files_encryption': 'bool',
        'kms_id': 'str',
        'lts': 'Lts',
        'log_file_validate': 'LogFileValidate'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'tracker_name': 'tracker_name',
        'bucket_name': 'bucket_name',
        'file_prefix_name': 'file_prefix_name',
        'status': 'status',
        'detail': 'detail',
        'is_obs_created': 'is_obs_created',
        'is_support_trace_files_encryption': 'is_support_trace_files_encryption',
        'kms_id': 'kms_id',
        'lts': 'lts',
        'log_file_validate': 'log_file_validate'
    }

    def __init__(self, id=None, create_time=None, domain_id=None, project_id=None, tracker_name=None, bucket_name=None, file_prefix_name=None, status=None, detail=None, is_obs_created=None, is_support_trace_files_encryption=None, kms_id=None, lts=None, log_file_validate=None):  # noqa: E501
        """ListTrackerResponse - a model defined in huaweicloud sdk"""

        self._id = None
        self._create_time = None
        self._domain_id = None
        self._project_id = None
        self._tracker_name = None
        self._bucket_name = None
        self._file_prefix_name = None
        self._status = None
        self._detail = None
        self._is_obs_created = None
        self._is_support_trace_files_encryption = None
        self._kms_id = None
        self._lts = None
        self._log_file_validate = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if tracker_name is not None:
            self.tracker_name = tracker_name
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if file_prefix_name is not None:
            self.file_prefix_name = file_prefix_name
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail
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
    def id(self):
        """Gets the id of this ListTrackerResponse.

        追踪器唯一标识。

        :return: The id of this ListTrackerResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListTrackerResponse.

        追踪器唯一标识。

        :param id: The id of this ListTrackerResponse.
        :type: str
        """
        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this ListTrackerResponse.

        追踪器创建时间戳。

        :return: The create_time of this ListTrackerResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListTrackerResponse.

        追踪器创建时间戳。

        :param create_time: The create_time of this ListTrackerResponse.
        :type: int
        """
        self._create_time = create_time

    @property
    def domain_id(self):
        """Gets the domain_id of this ListTrackerResponse.

        账号ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。

        :return: The domain_id of this ListTrackerResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListTrackerResponse.

        账号ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。

        :param domain_id: The domain_id of this ListTrackerResponse.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this ListTrackerResponse.

        项目ID。

        :return: The project_id of this ListTrackerResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListTrackerResponse.

        项目ID。

        :param project_id: The project_id of this ListTrackerResponse.
        :type: str
        """
        self._project_id = project_id

    @property
    def tracker_name(self):
        """Gets the tracker_name of this ListTrackerResponse.

        标识追踪器名称，当前版本默认为“system”。

        :return: The tracker_name of this ListTrackerResponse.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        """Sets the tracker_name of this ListTrackerResponse.

        标识追踪器名称，当前版本默认为“system”。

        :param tracker_name: The tracker_name of this ListTrackerResponse.
        :type: str
        """
        self._tracker_name = tracker_name

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ListTrackerResponse.

        标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。

        :return: The bucket_name of this ListTrackerResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ListTrackerResponse.

        标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。

        :param bucket_name: The bucket_name of this ListTrackerResponse.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def file_prefix_name(self):
        """Gets the file_prefix_name of this ListTrackerResponse.

        标识需要存储于OBS的日志文件前缀。

        :return: The file_prefix_name of this ListTrackerResponse.
        :rtype: str
        """
        return self._file_prefix_name

    @file_prefix_name.setter
    def file_prefix_name(self, file_prefix_name):
        """Sets the file_prefix_name of this ListTrackerResponse.

        标识需要存储于OBS的日志文件前缀。

        :param file_prefix_name: The file_prefix_name of this ListTrackerResponse.
        :type: str
        """
        self._file_prefix_name = file_prefix_name

    @property
    def status(self):
        """Gets the status of this ListTrackerResponse.

        标识追踪器状态，包括正常（enabled），停止（disabled）和异常（error）三种状态，状态为异常时需通过明细（detail）字段说明错误来源。

        :return: The status of this ListTrackerResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListTrackerResponse.

        标识追踪器状态，包括正常（enabled），停止（disabled）和异常（error）三种状态，状态为异常时需通过明细（detail）字段说明错误来源。

        :param status: The status of this ListTrackerResponse.
        :type: str
        """
        self._status = status

    @property
    def detail(self):
        """Gets the detail of this ListTrackerResponse.

        该参数仅在追踪器状态异常时返回，用于标识追踪器异常的原因，包括桶策略异常（bucketPolicyError），桶不存在（noBucket）和欠费或冻结（arrears）三种原因。

        :return: The detail of this ListTrackerResponse.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ListTrackerResponse.

        该参数仅在追踪器状态异常时返回，用于标识追踪器异常的原因，包括桶策略异常（bucketPolicyError），桶不存在（noBucket）和欠费或冻结（arrears）三种原因。

        :param detail: The detail of this ListTrackerResponse.
        :type: str
        """
        self._detail = detail

    @property
    def is_obs_created(self):
        """Gets the is_obs_created of this ListTrackerResponse.

        是否支持新建OBS桶。   值为“true”时，表示新创建OBS桶存储事件文件；   值为“false”时，选择已存在的OBS桶存储事件文件。 桶名称包含数字、字母、'-'和'.'（非数字、字母类字符最多存在1个），长度为3～64字符。

        :return: The is_obs_created of this ListTrackerResponse.
        :rtype: bool
        """
        return self._is_obs_created

    @is_obs_created.setter
    def is_obs_created(self, is_obs_created):
        """Sets the is_obs_created of this ListTrackerResponse.

        是否支持新建OBS桶。   值为“true”时，表示新创建OBS桶存储事件文件；   值为“false”时，选择已存在的OBS桶存储事件文件。 桶名称包含数字、字母、'-'和'.'（非数字、字母类字符最多存在1个），长度为3～64字符。

        :param is_obs_created: The is_obs_created of this ListTrackerResponse.
        :type: bool
        """
        self._is_obs_created = is_obs_created

    @property
    def is_support_trace_files_encryption(self):
        """Gets the is_support_trace_files_encryption of this ListTrackerResponse.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。

        :return: The is_support_trace_files_encryption of this ListTrackerResponse.
        :rtype: bool
        """
        return self._is_support_trace_files_encryption

    @is_support_trace_files_encryption.setter
    def is_support_trace_files_encryption(self, is_support_trace_files_encryption):
        """Sets the is_support_trace_files_encryption of this ListTrackerResponse.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。

        :param is_support_trace_files_encryption: The is_support_trace_files_encryption of this ListTrackerResponse.
        :type: bool
        """
        self._is_support_trace_files_encryption = is_support_trace_files_encryption

    @property
    def kms_id(self):
        """Gets the kms_id of this ListTrackerResponse.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :return: The kms_id of this ListTrackerResponse.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        """Sets the kms_id of this ListTrackerResponse.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :param kms_id: The kms_id of this ListTrackerResponse.
        :type: str
        """
        self._kms_id = kms_id

    @property
    def lts(self):
        """Gets the lts of this ListTrackerResponse.


        :return: The lts of this ListTrackerResponse.
        :rtype: Lts
        """
        return self._lts

    @lts.setter
    def lts(self, lts):
        """Sets the lts of this ListTrackerResponse.


        :param lts: The lts of this ListTrackerResponse.
        :type: Lts
        """
        self._lts = lts

    @property
    def log_file_validate(self):
        """Gets the log_file_validate of this ListTrackerResponse.


        :return: The log_file_validate of this ListTrackerResponse.
        :rtype: LogFileValidate
        """
        return self._log_file_validate

    @log_file_validate.setter
    def log_file_validate(self, log_file_validate):
        """Sets the log_file_validate of this ListTrackerResponse.


        :param log_file_validate: The log_file_validate of this ListTrackerResponse.
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
        if not isinstance(other, ListTrackerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
