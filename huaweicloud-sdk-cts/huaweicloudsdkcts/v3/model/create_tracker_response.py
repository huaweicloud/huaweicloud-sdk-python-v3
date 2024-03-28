# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTrackerResponse(SdkResponse):

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
        'is_organization_tracker': 'bool',
        'management_event_selector': 'ManagementEventSelector',
        'lts': 'Lts',
        'tracker_type': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'tracker_name': 'str',
        'agency_name': 'str',
        'status': 'str',
        'detail': 'str',
        'is_support_trace_files_encryption': 'bool',
        'obs_info': 'ObsInfo',
        'data_bucket': 'DataBucketQuery'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'kms_id': 'kms_id',
        'is_support_validate': 'is_support_validate',
        'is_organization_tracker': 'is_organization_tracker',
        'management_event_selector': 'management_event_selector',
        'lts': 'lts',
        'tracker_type': 'tracker_type',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'tracker_name': 'tracker_name',
        'agency_name': 'agency_name',
        'status': 'status',
        'detail': 'detail',
        'is_support_trace_files_encryption': 'is_support_trace_files_encryption',
        'obs_info': 'obs_info',
        'data_bucket': 'data_bucket'
    }

    def __init__(self, id=None, create_time=None, kms_id=None, is_support_validate=None, is_organization_tracker=None, management_event_selector=None, lts=None, tracker_type=None, domain_id=None, project_id=None, tracker_name=None, agency_name=None, status=None, detail=None, is_support_trace_files_encryption=None, obs_info=None, data_bucket=None):
        """CreateTrackerResponse

        The model defined in huaweicloud sdk

        :param id: 追踪器唯一标识。
        :type id: str
        :param create_time: 追踪器创建时间戳。
        :type create_time: int
        :param kms_id: 事件文件转储加密所采用的秘钥id（从KMS获取）。 当\&quot;tracker_type\&quot;参数值为\&quot;system\&quot;和\&quot;is_support_trace_files_encryption\&quot;参数值为“是”时，此参数为必选项。
        :type kms_id: str
        :param is_support_validate: 是否打开事件文件校验。当前环境仅\&quot;tracker_type\&quot;参数值为\&quot;system\&quot;时支持该功能。
        :type is_support_validate: bool
        :param is_organization_tracker: 是否应用到我的组织。 只针对管理类追踪器。设置为true时，ORG组织下所有成员当前区域的审计日志会转储到该追踪器配置的OBS桶或者LTS日志流，但是事件列表界面不支持查看其它组织成员的审计日志。
        :type is_organization_tracker: bool
        :param management_event_selector: 
        :type management_event_selector: :class:`huaweicloudsdkcts.v3.ManagementEventSelector`
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
        :param agency_name: 云服务委托名称。
        :type agency_name: str
        :param status: 标识追踪器状态，包括正常（enabled），停止（disabled）和异常（error）三种状态，状态为异常时需通过明细（detail）字段说明错误来源。
        :type status: str
        :param detail: 该参数仅在追踪器状态异常时返回，用于标识追踪器异常的原因，包括桶策略异常（bucketPolicyError），桶不存在（noBucket）和欠费或冻结（arrears）三种原因。
        :type detail: str
        :param is_support_trace_files_encryption: 事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。 当前环境仅\&quot;tracker_type\&quot;参数值为\&quot;system\&quot;时支持该功能。
        :type is_support_trace_files_encryption: bool
        :param obs_info: 
        :type obs_info: :class:`huaweicloudsdkcts.v3.ObsInfo`
        :param data_bucket: 
        :type data_bucket: :class:`huaweicloudsdkcts.v3.DataBucketQuery`
        """
        
        super(CreateTrackerResponse, self).__init__()

        self._id = None
        self._create_time = None
        self._kms_id = None
        self._is_support_validate = None
        self._is_organization_tracker = None
        self._management_event_selector = None
        self._lts = None
        self._tracker_type = None
        self._domain_id = None
        self._project_id = None
        self._tracker_name = None
        self._agency_name = None
        self._status = None
        self._detail = None
        self._is_support_trace_files_encryption = None
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
        if is_organization_tracker is not None:
            self.is_organization_tracker = is_organization_tracker
        if management_event_selector is not None:
            self.management_event_selector = management_event_selector
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
        if agency_name is not None:
            self.agency_name = agency_name
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail
        if is_support_trace_files_encryption is not None:
            self.is_support_trace_files_encryption = is_support_trace_files_encryption
        if obs_info is not None:
            self.obs_info = obs_info
        if data_bucket is not None:
            self.data_bucket = data_bucket

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
        :type id: str
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
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def kms_id(self):
        """Gets the kms_id of this CreateTrackerResponse.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"tracker_type\"参数值为\"system\"和\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :return: The kms_id of this CreateTrackerResponse.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        """Sets the kms_id of this CreateTrackerResponse.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"tracker_type\"参数值为\"system\"和\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :param kms_id: The kms_id of this CreateTrackerResponse.
        :type kms_id: str
        """
        self._kms_id = kms_id

    @property
    def is_support_validate(self):
        """Gets the is_support_validate of this CreateTrackerResponse.

        是否打开事件文件校验。当前环境仅\"tracker_type\"参数值为\"system\"时支持该功能。

        :return: The is_support_validate of this CreateTrackerResponse.
        :rtype: bool
        """
        return self._is_support_validate

    @is_support_validate.setter
    def is_support_validate(self, is_support_validate):
        """Sets the is_support_validate of this CreateTrackerResponse.

        是否打开事件文件校验。当前环境仅\"tracker_type\"参数值为\"system\"时支持该功能。

        :param is_support_validate: The is_support_validate of this CreateTrackerResponse.
        :type is_support_validate: bool
        """
        self._is_support_validate = is_support_validate

    @property
    def is_organization_tracker(self):
        """Gets the is_organization_tracker of this CreateTrackerResponse.

        是否应用到我的组织。 只针对管理类追踪器。设置为true时，ORG组织下所有成员当前区域的审计日志会转储到该追踪器配置的OBS桶或者LTS日志流，但是事件列表界面不支持查看其它组织成员的审计日志。

        :return: The is_organization_tracker of this CreateTrackerResponse.
        :rtype: bool
        """
        return self._is_organization_tracker

    @is_organization_tracker.setter
    def is_organization_tracker(self, is_organization_tracker):
        """Sets the is_organization_tracker of this CreateTrackerResponse.

        是否应用到我的组织。 只针对管理类追踪器。设置为true时，ORG组织下所有成员当前区域的审计日志会转储到该追踪器配置的OBS桶或者LTS日志流，但是事件列表界面不支持查看其它组织成员的审计日志。

        :param is_organization_tracker: The is_organization_tracker of this CreateTrackerResponse.
        :type is_organization_tracker: bool
        """
        self._is_organization_tracker = is_organization_tracker

    @property
    def management_event_selector(self):
        """Gets the management_event_selector of this CreateTrackerResponse.

        :return: The management_event_selector of this CreateTrackerResponse.
        :rtype: :class:`huaweicloudsdkcts.v3.ManagementEventSelector`
        """
        return self._management_event_selector

    @management_event_selector.setter
    def management_event_selector(self, management_event_selector):
        """Sets the management_event_selector of this CreateTrackerResponse.

        :param management_event_selector: The management_event_selector of this CreateTrackerResponse.
        :type management_event_selector: :class:`huaweicloudsdkcts.v3.ManagementEventSelector`
        """
        self._management_event_selector = management_event_selector

    @property
    def lts(self):
        """Gets the lts of this CreateTrackerResponse.

        :return: The lts of this CreateTrackerResponse.
        :rtype: :class:`huaweicloudsdkcts.v3.Lts`
        """
        return self._lts

    @lts.setter
    def lts(self, lts):
        """Sets the lts of this CreateTrackerResponse.

        :param lts: The lts of this CreateTrackerResponse.
        :type lts: :class:`huaweicloudsdkcts.v3.Lts`
        """
        self._lts = lts

    @property
    def tracker_type(self):
        """Gets the tracker_type of this CreateTrackerResponse.

        标识追踪器类型。 目前支持系统追踪器类型有管理类追踪器（system）和数据类追踪器（data）。

        :return: The tracker_type of this CreateTrackerResponse.
        :rtype: str
        """
        return self._tracker_type

    @tracker_type.setter
    def tracker_type(self, tracker_type):
        """Sets the tracker_type of this CreateTrackerResponse.

        标识追踪器类型。 目前支持系统追踪器类型有管理类追踪器（system）和数据类追踪器（data）。

        :param tracker_type: The tracker_type of this CreateTrackerResponse.
        :type tracker_type: str
        """
        self._tracker_type = tracker_type

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
        :type domain_id: str
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
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tracker_name(self):
        """Gets the tracker_name of this CreateTrackerResponse.

        标识追踪器名称，当前版本默认为“system”。

        :return: The tracker_name of this CreateTrackerResponse.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        """Sets the tracker_name of this CreateTrackerResponse.

        标识追踪器名称，当前版本默认为“system”。

        :param tracker_name: The tracker_name of this CreateTrackerResponse.
        :type tracker_name: str
        """
        self._tracker_name = tracker_name

    @property
    def agency_name(self):
        """Gets the agency_name of this CreateTrackerResponse.

        云服务委托名称。

        :return: The agency_name of this CreateTrackerResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this CreateTrackerResponse.

        云服务委托名称。

        :param agency_name: The agency_name of this CreateTrackerResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def status(self):
        """Gets the status of this CreateTrackerResponse.

        标识追踪器状态，包括正常（enabled），停止（disabled）和异常（error）三种状态，状态为异常时需通过明细（detail）字段说明错误来源。

        :return: The status of this CreateTrackerResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateTrackerResponse.

        标识追踪器状态，包括正常（enabled），停止（disabled）和异常（error）三种状态，状态为异常时需通过明细（detail）字段说明错误来源。

        :param status: The status of this CreateTrackerResponse.
        :type status: str
        """
        self._status = status

    @property
    def detail(self):
        """Gets the detail of this CreateTrackerResponse.

        该参数仅在追踪器状态异常时返回，用于标识追踪器异常的原因，包括桶策略异常（bucketPolicyError），桶不存在（noBucket）和欠费或冻结（arrears）三种原因。

        :return: The detail of this CreateTrackerResponse.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this CreateTrackerResponse.

        该参数仅在追踪器状态异常时返回，用于标识追踪器异常的原因，包括桶策略异常（bucketPolicyError），桶不存在（noBucket）和欠费或冻结（arrears）三种原因。

        :param detail: The detail of this CreateTrackerResponse.
        :type detail: str
        """
        self._detail = detail

    @property
    def is_support_trace_files_encryption(self):
        """Gets the is_support_trace_files_encryption of this CreateTrackerResponse.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。 当前环境仅\"tracker_type\"参数值为\"system\"时支持该功能。

        :return: The is_support_trace_files_encryption of this CreateTrackerResponse.
        :rtype: bool
        """
        return self._is_support_trace_files_encryption

    @is_support_trace_files_encryption.setter
    def is_support_trace_files_encryption(self, is_support_trace_files_encryption):
        """Sets the is_support_trace_files_encryption of this CreateTrackerResponse.

        事件文件转储加密功能开关。 该参数必须与kms_id参数同时使用。 当前环境仅\"tracker_type\"参数值为\"system\"时支持该功能。

        :param is_support_trace_files_encryption: The is_support_trace_files_encryption of this CreateTrackerResponse.
        :type is_support_trace_files_encryption: bool
        """
        self._is_support_trace_files_encryption = is_support_trace_files_encryption

    @property
    def obs_info(self):
        """Gets the obs_info of this CreateTrackerResponse.

        :return: The obs_info of this CreateTrackerResponse.
        :rtype: :class:`huaweicloudsdkcts.v3.ObsInfo`
        """
        return self._obs_info

    @obs_info.setter
    def obs_info(self, obs_info):
        """Sets the obs_info of this CreateTrackerResponse.

        :param obs_info: The obs_info of this CreateTrackerResponse.
        :type obs_info: :class:`huaweicloudsdkcts.v3.ObsInfo`
        """
        self._obs_info = obs_info

    @property
    def data_bucket(self):
        """Gets the data_bucket of this CreateTrackerResponse.

        :return: The data_bucket of this CreateTrackerResponse.
        :rtype: :class:`huaweicloudsdkcts.v3.DataBucketQuery`
        """
        return self._data_bucket

    @data_bucket.setter
    def data_bucket(self, data_bucket):
        """Sets the data_bucket of this CreateTrackerResponse.

        :param data_bucket: The data_bucket of this CreateTrackerResponse.
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
        if not isinstance(other, CreateTrackerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
