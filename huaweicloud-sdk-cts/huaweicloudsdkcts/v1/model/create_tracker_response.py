# coding: utf-8

import pprint
import re

import six


class CreateTrackerResponse(object):


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
        'is_support_trace_files_encryption': 'bool',
        'kms_id': 'str',
        'obs_info': 'ObsInfo',
        'status': 'str',
        'tracker_name': 'str',
        'tracker_type': 'str',
        'lts': 'Lts',
        'log_file_validate': 'LogFileValidate'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'is_support_trace_files_encryption': 'is_support_trace_files_encryption',
        'kms_id': 'kms_id',
        'obs_info': 'obs_info',
        'status': 'status',
        'tracker_name': 'tracker_name',
        'tracker_type': 'tracker_type',
        'lts': 'lts',
        'log_file_validate': 'log_file_validate'
    }

    def __init__(self, id=None, create_time=None, domain_id=None, project_id=None, is_support_trace_files_encryption=None, kms_id=None, obs_info=None, status=None, tracker_name=None, tracker_type=None, lts=None, log_file_validate=None):  # noqa: E501
        """CreateTrackerResponse - a model defined in huaweicloud sdk"""

        self._id = None
        self._create_time = None
        self._domain_id = None
        self._project_id = None
        self._is_support_trace_files_encryption = None
        self._kms_id = None
        self._obs_info = None
        self._status = None
        self._tracker_name = None
        self._tracker_type = None
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
        if is_support_trace_files_encryption is not None:
            self.is_support_trace_files_encryption = is_support_trace_files_encryption
        if kms_id is not None:
            self.kms_id = kms_id
        if obs_info is not None:
            self.obs_info = obs_info
        if status is not None:
            self.status = status
        if tracker_name is not None:
            self.tracker_name = tracker_name
        if tracker_type is not None:
            self.tracker_type = tracker_type
        if lts is not None:
            self.lts = lts
        if log_file_validate is not None:
            self.log_file_validate = log_file_validate

    @property
    def id(self):
        """Gets the id of this CreateTrackerResponse.

        追踪器唯一标识。

        :return: The id of this CreateTrackerResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateTrackerResponse.

        追踪器唯一标识。

        :param id: The id of this CreateTrackerResponse.
        :type: str
        """
        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this CreateTrackerResponse.

        追踪器创建时间戳。

        :return: The create_time of this CreateTrackerResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateTrackerResponse.

        追踪器创建时间戳。

        :param create_time: The create_time of this CreateTrackerResponse.
        :type: int
        """
        self._create_time = create_time

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateTrackerResponse.

        账号ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。

        :return: The domain_id of this CreateTrackerResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateTrackerResponse.

        账号ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。

        :param domain_id: The domain_id of this CreateTrackerResponse.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateTrackerResponse.

        项目ID。

        :return: The project_id of this CreateTrackerResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateTrackerResponse.

        项目ID。

        :param project_id: The project_id of this CreateTrackerResponse.
        :type: str
        """
        self._project_id = project_id

    @property
    def is_support_trace_files_encryption(self):
        """Gets the is_support_trace_files_encryption of this CreateTrackerResponse.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。

        :return: The is_support_trace_files_encryption of this CreateTrackerResponse.
        :rtype: bool
        """
        return self._is_support_trace_files_encryption

    @is_support_trace_files_encryption.setter
    def is_support_trace_files_encryption(self, is_support_trace_files_encryption):
        """Sets the is_support_trace_files_encryption of this CreateTrackerResponse.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。

        :param is_support_trace_files_encryption: The is_support_trace_files_encryption of this CreateTrackerResponse.
        :type: bool
        """
        self._is_support_trace_files_encryption = is_support_trace_files_encryption

    @property
    def kms_id(self):
        """Gets the kms_id of this CreateTrackerResponse.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :return: The kms_id of this CreateTrackerResponse.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        """Sets the kms_id of this CreateTrackerResponse.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :param kms_id: The kms_id of this CreateTrackerResponse.
        :type: str
        """
        self._kms_id = kms_id

    @property
    def obs_info(self):
        """Gets the obs_info of this CreateTrackerResponse.


        :return: The obs_info of this CreateTrackerResponse.
        :rtype: ObsInfo
        """
        return self._obs_info

    @obs_info.setter
    def obs_info(self, obs_info):
        """Sets the obs_info of this CreateTrackerResponse.


        :param obs_info: The obs_info of this CreateTrackerResponse.
        :type: ObsInfo
        """
        self._obs_info = obs_info

    @property
    def status(self):
        """Gets the status of this CreateTrackerResponse.

        标识追踪器状态，该接口返回正常状态（enabled）。

        :return: The status of this CreateTrackerResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateTrackerResponse.

        标识追踪器状态，该接口返回正常状态（enabled）。

        :param status: The status of this CreateTrackerResponse.
        :type: str
        """
        self._status = status

    @property
    def tracker_name(self):
        """Gets the tracker_name of this CreateTrackerResponse.

        追踪器名称。

        :return: The tracker_name of this CreateTrackerResponse.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        """Sets the tracker_name of this CreateTrackerResponse.

        追踪器名称。

        :param tracker_name: The tracker_name of this CreateTrackerResponse.
        :type: str
        """
        self._tracker_name = tracker_name

    @property
    def tracker_type(self):
        """Gets the tracker_type of this CreateTrackerResponse.

        追踪器类型。

        :return: The tracker_type of this CreateTrackerResponse.
        :rtype: str
        """
        return self._tracker_type

    @tracker_type.setter
    def tracker_type(self, tracker_type):
        """Sets the tracker_type of this CreateTrackerResponse.

        追踪器类型。

        :param tracker_type: The tracker_type of this CreateTrackerResponse.
        :type: str
        """
        self._tracker_type = tracker_type

    @property
    def lts(self):
        """Gets the lts of this CreateTrackerResponse.


        :return: The lts of this CreateTrackerResponse.
        :rtype: Lts
        """
        return self._lts

    @lts.setter
    def lts(self, lts):
        """Sets the lts of this CreateTrackerResponse.


        :param lts: The lts of this CreateTrackerResponse.
        :type: Lts
        """
        self._lts = lts

    @property
    def log_file_validate(self):
        """Gets the log_file_validate of this CreateTrackerResponse.


        :return: The log_file_validate of this CreateTrackerResponse.
        :rtype: LogFileValidate
        """
        return self._log_file_validate

    @log_file_validate.setter
    def log_file_validate(self, log_file_validate):
        """Sets the log_file_validate of this CreateTrackerResponse.


        :param log_file_validate: The log_file_validate of this CreateTrackerResponse.
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
        if not isinstance(other, CreateTrackerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
