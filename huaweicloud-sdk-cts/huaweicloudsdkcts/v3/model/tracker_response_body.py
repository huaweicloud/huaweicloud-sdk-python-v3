# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrackerResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'create_time': 'int',
        'kms_id': 'str',
        'is_support_validate': 'bool',
        'lts': 'Lts',
        'tracker_type': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'tracker_name': 'str',
        'status': 'str',
        'detail': 'str',
        'is_support_trace_files_encryption': 'bool',
        'group_id': 'str',
        'stream_id': 'str',
        'obs_info': 'ObsInfo',
        'data_bucket': 'DataBucketQuery'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'kms_id': 'kms_id',
        'is_support_validate': 'is_support_validate',
        'lts': 'lts',
        'tracker_type': 'tracker_type',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'tracker_name': 'tracker_name',
        'status': 'status',
        'detail': 'detail',
        'is_support_trace_files_encryption': 'is_support_trace_files_encryption',
        'group_id': 'group_id',
        'stream_id': 'stream_id',
        'obs_info': 'obs_info',
        'data_bucket': 'data_bucket'
    }

    def __init__(self, id=None, create_time=None, kms_id=None, is_support_validate=None, lts=None, tracker_type=None, domain_id=None, project_id=None, tracker_name=None, status=None, detail=None, is_support_trace_files_encryption=None, group_id=None, stream_id=None, obs_info=None, data_bucket=None):
        """TrackerResponseBody

        The model defined in huaweicloud sdk

        :param id: 追踪器唯一标识。
        :type id: str
        :param create_time: 追踪器创建时间戳。
        :type create_time: int
        :param kms_id: 事件文件转储加密所采用的秘钥id（从KMS获取）。 当\&quot;tracker_type\&quot;参数值为\&quot;system\&quot;和\&quot;is_support_trace_files_encryption\&quot;参数值为“是”时，此参数为必选项。
        :type kms_id: str
        :param is_support_validate: 是否打开事件文件校验。
        :type is_support_validate: bool
        :param lts: 
        :type lts: :class:`huaweicloudsdkcts.v3.Lts`
        :param tracker_type: 标识追踪器类型。 目前支持系统追踪器类型有管理类追踪器（system）和数据类追踪器（data）。
        :type tracker_type: str
        :param domain_id: 账号ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。
        :type domain_id: str
        :param project_id: 项目ID。
        :type project_id: str
        :param tracker_name: 标识追踪器名称，当前版本默认为“system”。
        :type tracker_name: str
        :param status: 标识追踪器状态，包括正常（enabled），停止（disabled）和异常（error）三种状态，状态为异常时需通过明细（detail）字段说明错误来源。
        :type status: str
        :param detail: 该参数仅在追踪器状态异常时返回，用于标识追踪器异常的原因，包括桶策略异常（bucketPolicyError），桶不存在（noBucket）和欠费或冻结（arrears）三种原因。
        :type detail: str
        :param is_support_trace_files_encryption: 事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。 当前环境仅\&quot;tracker_type\&quot;参数值为\&quot;system\&quot;时支持该功能。
        :type is_support_trace_files_encryption: bool
        :param group_id: LTS服务日志组的ID。
        :type group_id: str
        :param stream_id: LTS服务日志流的ID。
        :type stream_id: str
        :param obs_info: 
        :type obs_info: :class:`huaweicloudsdkcts.v3.ObsInfo`
        :param data_bucket: 
        :type data_bucket: :class:`huaweicloudsdkcts.v3.DataBucketQuery`
        """
        
        

        self._id = None
        self._create_time = None
        self._kms_id = None
        self._is_support_validate = None
        self._lts = None
        self._tracker_type = None
        self._domain_id = None
        self._project_id = None
        self._tracker_name = None
        self._status = None
        self._detail = None
        self._is_support_trace_files_encryption = None
        self._group_id = None
        self._stream_id = None
        self._obs_info = None
        self._data_bucket = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if kms_id is not None:
            self.kms_id = kms_id
        if is_support_validate is not None:
            self.is_support_validate = is_support_validate
        if lts is not None:
            self.lts = lts
        if tracker_type is not None:
            self.tracker_type = tracker_type
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if tracker_name is not None:
            self.tracker_name = tracker_name
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail
        if is_support_trace_files_encryption is not None:
            self.is_support_trace_files_encryption = is_support_trace_files_encryption
        if group_id is not None:
            self.group_id = group_id
        if stream_id is not None:
            self.stream_id = stream_id
        if obs_info is not None:
            self.obs_info = obs_info
        if data_bucket is not None:
            self.data_bucket = data_bucket

    @property
    def id(self):
        """Gets the id of this TrackerResponseBody.

        追踪器唯一标识。

        :return: The id of this TrackerResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrackerResponseBody.

        追踪器唯一标识。

        :param id: The id of this TrackerResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this TrackerResponseBody.

        追踪器创建时间戳。

        :return: The create_time of this TrackerResponseBody.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TrackerResponseBody.

        追踪器创建时间戳。

        :param create_time: The create_time of this TrackerResponseBody.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def kms_id(self):
        """Gets the kms_id of this TrackerResponseBody.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"tracker_type\"参数值为\"system\"和\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :return: The kms_id of this TrackerResponseBody.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        """Sets the kms_id of this TrackerResponseBody.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"tracker_type\"参数值为\"system\"和\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :param kms_id: The kms_id of this TrackerResponseBody.
        :type kms_id: str
        """
        self._kms_id = kms_id

    @property
    def is_support_validate(self):
        """Gets the is_support_validate of this TrackerResponseBody.

        是否打开事件文件校验。

        :return: The is_support_validate of this TrackerResponseBody.
        :rtype: bool
        """
        return self._is_support_validate

    @is_support_validate.setter
    def is_support_validate(self, is_support_validate):
        """Sets the is_support_validate of this TrackerResponseBody.

        是否打开事件文件校验。

        :param is_support_validate: The is_support_validate of this TrackerResponseBody.
        :type is_support_validate: bool
        """
        self._is_support_validate = is_support_validate

    @property
    def lts(self):
        """Gets the lts of this TrackerResponseBody.


        :return: The lts of this TrackerResponseBody.
        :rtype: :class:`huaweicloudsdkcts.v3.Lts`
        """
        return self._lts

    @lts.setter
    def lts(self, lts):
        """Sets the lts of this TrackerResponseBody.


        :param lts: The lts of this TrackerResponseBody.
        :type lts: :class:`huaweicloudsdkcts.v3.Lts`
        """
        self._lts = lts

    @property
    def tracker_type(self):
        """Gets the tracker_type of this TrackerResponseBody.

        标识追踪器类型。 目前支持系统追踪器类型有管理类追踪器（system）和数据类追踪器（data）。

        :return: The tracker_type of this TrackerResponseBody.
        :rtype: str
        """
        return self._tracker_type

    @tracker_type.setter
    def tracker_type(self, tracker_type):
        """Sets the tracker_type of this TrackerResponseBody.

        标识追踪器类型。 目前支持系统追踪器类型有管理类追踪器（system）和数据类追踪器（data）。

        :param tracker_type: The tracker_type of this TrackerResponseBody.
        :type tracker_type: str
        """
        self._tracker_type = tracker_type

    @property
    def domain_id(self):
        """Gets the domain_id of this TrackerResponseBody.

        账号ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。

        :return: The domain_id of this TrackerResponseBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this TrackerResponseBody.

        账号ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。

        :param domain_id: The domain_id of this TrackerResponseBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this TrackerResponseBody.

        项目ID。

        :return: The project_id of this TrackerResponseBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TrackerResponseBody.

        项目ID。

        :param project_id: The project_id of this TrackerResponseBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tracker_name(self):
        """Gets the tracker_name of this TrackerResponseBody.

        标识追踪器名称，当前版本默认为“system”。

        :return: The tracker_name of this TrackerResponseBody.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        """Sets the tracker_name of this TrackerResponseBody.

        标识追踪器名称，当前版本默认为“system”。

        :param tracker_name: The tracker_name of this TrackerResponseBody.
        :type tracker_name: str
        """
        self._tracker_name = tracker_name

    @property
    def status(self):
        """Gets the status of this TrackerResponseBody.

        标识追踪器状态，包括正常（enabled），停止（disabled）和异常（error）三种状态，状态为异常时需通过明细（detail）字段说明错误来源。

        :return: The status of this TrackerResponseBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TrackerResponseBody.

        标识追踪器状态，包括正常（enabled），停止（disabled）和异常（error）三种状态，状态为异常时需通过明细（detail）字段说明错误来源。

        :param status: The status of this TrackerResponseBody.
        :type status: str
        """
        self._status = status

    @property
    def detail(self):
        """Gets the detail of this TrackerResponseBody.

        该参数仅在追踪器状态异常时返回，用于标识追踪器异常的原因，包括桶策略异常（bucketPolicyError），桶不存在（noBucket）和欠费或冻结（arrears）三种原因。

        :return: The detail of this TrackerResponseBody.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this TrackerResponseBody.

        该参数仅在追踪器状态异常时返回，用于标识追踪器异常的原因，包括桶策略异常（bucketPolicyError），桶不存在（noBucket）和欠费或冻结（arrears）三种原因。

        :param detail: The detail of this TrackerResponseBody.
        :type detail: str
        """
        self._detail = detail

    @property
    def is_support_trace_files_encryption(self):
        """Gets the is_support_trace_files_encryption of this TrackerResponseBody.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。 当前环境仅\"tracker_type\"参数值为\"system\"时支持该功能。

        :return: The is_support_trace_files_encryption of this TrackerResponseBody.
        :rtype: bool
        """
        return self._is_support_trace_files_encryption

    @is_support_trace_files_encryption.setter
    def is_support_trace_files_encryption(self, is_support_trace_files_encryption):
        """Sets the is_support_trace_files_encryption of this TrackerResponseBody.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。 当前环境仅\"tracker_type\"参数值为\"system\"时支持该功能。

        :param is_support_trace_files_encryption: The is_support_trace_files_encryption of this TrackerResponseBody.
        :type is_support_trace_files_encryption: bool
        """
        self._is_support_trace_files_encryption = is_support_trace_files_encryption

    @property
    def group_id(self):
        """Gets the group_id of this TrackerResponseBody.

        LTS服务日志组的ID。

        :return: The group_id of this TrackerResponseBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this TrackerResponseBody.

        LTS服务日志组的ID。

        :param group_id: The group_id of this TrackerResponseBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def stream_id(self):
        """Gets the stream_id of this TrackerResponseBody.

        LTS服务日志流的ID。

        :return: The stream_id of this TrackerResponseBody.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this TrackerResponseBody.

        LTS服务日志流的ID。

        :param stream_id: The stream_id of this TrackerResponseBody.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def obs_info(self):
        """Gets the obs_info of this TrackerResponseBody.


        :return: The obs_info of this TrackerResponseBody.
        :rtype: :class:`huaweicloudsdkcts.v3.ObsInfo`
        """
        return self._obs_info

    @obs_info.setter
    def obs_info(self, obs_info):
        """Sets the obs_info of this TrackerResponseBody.


        :param obs_info: The obs_info of this TrackerResponseBody.
        :type obs_info: :class:`huaweicloudsdkcts.v3.ObsInfo`
        """
        self._obs_info = obs_info

    @property
    def data_bucket(self):
        """Gets the data_bucket of this TrackerResponseBody.


        :return: The data_bucket of this TrackerResponseBody.
        :rtype: :class:`huaweicloudsdkcts.v3.DataBucketQuery`
        """
        return self._data_bucket

    @data_bucket.setter
    def data_bucket(self, data_bucket):
        """Sets the data_bucket of this TrackerResponseBody.


        :param data_bucket: The data_bucket of this TrackerResponseBody.
        :type data_bucket: :class:`huaweicloudsdkcts.v3.DataBucketQuery`
        """
        self._data_bucket = data_bucket

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
        if not isinstance(other, TrackerResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
