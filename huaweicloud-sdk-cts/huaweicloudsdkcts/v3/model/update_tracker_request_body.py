# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTrackerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tracker_type': 'str',
        'tracker_name': 'str',
        'agency_name': 'str',
        'status': 'str',
        'is_organization_tracker': 'bool',
        'management_event_selector': 'ManagementEventSelector',
        'is_lts_enabled': 'bool',
        'obs_info': 'TrackerObsInfo',
        'is_support_trace_files_encryption': 'bool',
        'kms_id': 'str',
        'is_support_validate': 'bool',
        'data_bucket': 'DataBucket'
    }

    attribute_map = {
        'tracker_type': 'tracker_type',
        'tracker_name': 'tracker_name',
        'agency_name': 'agency_name',
        'status': 'status',
        'is_organization_tracker': 'is_organization_tracker',
        'management_event_selector': 'management_event_selector',
        'is_lts_enabled': 'is_lts_enabled',
        'obs_info': 'obs_info',
        'is_support_trace_files_encryption': 'is_support_trace_files_encryption',
        'kms_id': 'kms_id',
        'is_support_validate': 'is_support_validate',
        'data_bucket': 'data_bucket'
    }

    def __init__(self, tracker_type=None, tracker_name=None, agency_name=None, status=None, is_organization_tracker=None, management_event_selector=None, is_lts_enabled=None, obs_info=None, is_support_trace_files_encryption=None, kms_id=None, is_support_validate=None, data_bucket=None):
        r"""UpdateTrackerRequestBody

        The model defined in huaweicloud sdk

        :param tracker_type: 标识追踪器类型。 目前支持系统追踪器类型有管理类追踪器(system)和数据类追踪器(data)。 数据类追踪器和管理类追踪器共同参数有：is_lts_enabled, obs_info; 管理类追踪器参数：is_support_trace_files_encryption, kms_id, is_support_validate, is_support_validate; 数据类追踪器参数：tracker_name, data_bucket。
        :type tracker_type: str
        :param tracker_name: 标识追踪器名称。 当\&quot;tracker_type\&quot;参数值为\&quot;system\&quot;时该参数为默认值\&quot;system\&quot;。 当\&quot;tracker_type\&quot;参数值为\&quot;data\&quot;时该参数需要指定追踪器名称\&quot;。
        :type tracker_name: str
        :param agency_name: 云服务委托名称。 参数值为\&quot;cts_admin_trust\&quot;时，更新追踪器会自动创建一个云服务委托：cts_admin_trust。
        :type agency_name: str
        :param status: 标识追踪器状态，该接口中可修改的状态包括正常（enabled）和停止（disabled）。如果选择修改状态为停止，则修改成功后追踪器停止记录事件。
        :type status: str
        :param is_organization_tracker: 是否应用到我的组织。 只针对管理类追踪器。设置为true时，ORG组织下所有成员当前区域的审计日志会转储到该追踪器配置的OBS桶或者LTS日志流，但是事件列表界面不支持查看其它组织成员的审计日志。
        :type is_organization_tracker: bool
        :param management_event_selector: 
        :type management_event_selector: :class:`huaweicloudsdkcts.v3.ManagementEventSelector`
        :param is_lts_enabled: 是否打开事件分析。
        :type is_lts_enabled: bool
        :param obs_info: 
        :type obs_info: :class:`huaweicloudsdkcts.v3.TrackerObsInfo`
        :param is_support_trace_files_encryption: 事件文件转储加密功能开关。 当\&quot;tracker_type\&quot;参数值为\&quot;system\&quot;时该参数值有效。 该参数必须与kms_id参数同时使用。
        :type is_support_trace_files_encryption: bool
        :param kms_id: 事件文件转储加密所采用的秘钥id（从KMS获取）。 当\&quot;tracker_type\&quot;参数值为\&quot;system\&quot;时该参数值有效。 当\&quot;is_support_trace_files_encryption\&quot;参数值为“是”时，此参数为必选项。
        :type kms_id: str
        :param is_support_validate: 事件文件转储时是否打开事件文件校验。 当\&quot;tracker_type\&quot;参数值为\&quot;system\&quot;时该参数值有效。
        :type is_support_validate: bool
        :param data_bucket: 
        :type data_bucket: :class:`huaweicloudsdkcts.v3.DataBucket`
        """
        
        

        self._tracker_type = None
        self._tracker_name = None
        self._agency_name = None
        self._status = None
        self._is_organization_tracker = None
        self._management_event_selector = None
        self._is_lts_enabled = None
        self._obs_info = None
        self._is_support_trace_files_encryption = None
        self._kms_id = None
        self._is_support_validate = None
        self._data_bucket = None
        self.discriminator = None

        self.tracker_type = tracker_type
        self.tracker_name = tracker_name
        if agency_name is not None:
            self.agency_name = agency_name
        if status is not None:
            self.status = status
        if is_organization_tracker is not None:
            self.is_organization_tracker = is_organization_tracker
        if management_event_selector is not None:
            self.management_event_selector = management_event_selector
        if is_lts_enabled is not None:
            self.is_lts_enabled = is_lts_enabled
        if obs_info is not None:
            self.obs_info = obs_info
        if is_support_trace_files_encryption is not None:
            self.is_support_trace_files_encryption = is_support_trace_files_encryption
        if kms_id is not None:
            self.kms_id = kms_id
        if is_support_validate is not None:
            self.is_support_validate = is_support_validate
        if data_bucket is not None:
            self.data_bucket = data_bucket

    @property
    def tracker_type(self):
        r"""Gets the tracker_type of this UpdateTrackerRequestBody.

        标识追踪器类型。 目前支持系统追踪器类型有管理类追踪器(system)和数据类追踪器(data)。 数据类追踪器和管理类追踪器共同参数有：is_lts_enabled, obs_info; 管理类追踪器参数：is_support_trace_files_encryption, kms_id, is_support_validate, is_support_validate; 数据类追踪器参数：tracker_name, data_bucket。

        :return: The tracker_type of this UpdateTrackerRequestBody.
        :rtype: str
        """
        return self._tracker_type

    @tracker_type.setter
    def tracker_type(self, tracker_type):
        r"""Sets the tracker_type of this UpdateTrackerRequestBody.

        标识追踪器类型。 目前支持系统追踪器类型有管理类追踪器(system)和数据类追踪器(data)。 数据类追踪器和管理类追踪器共同参数有：is_lts_enabled, obs_info; 管理类追踪器参数：is_support_trace_files_encryption, kms_id, is_support_validate, is_support_validate; 数据类追踪器参数：tracker_name, data_bucket。

        :param tracker_type: The tracker_type of this UpdateTrackerRequestBody.
        :type tracker_type: str
        """
        self._tracker_type = tracker_type

    @property
    def tracker_name(self):
        r"""Gets the tracker_name of this UpdateTrackerRequestBody.

        标识追踪器名称。 当\"tracker_type\"参数值为\"system\"时该参数为默认值\"system\"。 当\"tracker_type\"参数值为\"data\"时该参数需要指定追踪器名称\"。

        :return: The tracker_name of this UpdateTrackerRequestBody.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        r"""Sets the tracker_name of this UpdateTrackerRequestBody.

        标识追踪器名称。 当\"tracker_type\"参数值为\"system\"时该参数为默认值\"system\"。 当\"tracker_type\"参数值为\"data\"时该参数需要指定追踪器名称\"。

        :param tracker_name: The tracker_name of this UpdateTrackerRequestBody.
        :type tracker_name: str
        """
        self._tracker_name = tracker_name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this UpdateTrackerRequestBody.

        云服务委托名称。 参数值为\"cts_admin_trust\"时，更新追踪器会自动创建一个云服务委托：cts_admin_trust。

        :return: The agency_name of this UpdateTrackerRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this UpdateTrackerRequestBody.

        云服务委托名称。 参数值为\"cts_admin_trust\"时，更新追踪器会自动创建一个云服务委托：cts_admin_trust。

        :param agency_name: The agency_name of this UpdateTrackerRequestBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def status(self):
        r"""Gets the status of this UpdateTrackerRequestBody.

        标识追踪器状态，该接口中可修改的状态包括正常（enabled）和停止（disabled）。如果选择修改状态为停止，则修改成功后追踪器停止记录事件。

        :return: The status of this UpdateTrackerRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateTrackerRequestBody.

        标识追踪器状态，该接口中可修改的状态包括正常（enabled）和停止（disabled）。如果选择修改状态为停止，则修改成功后追踪器停止记录事件。

        :param status: The status of this UpdateTrackerRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def is_organization_tracker(self):
        r"""Gets the is_organization_tracker of this UpdateTrackerRequestBody.

        是否应用到我的组织。 只针对管理类追踪器。设置为true时，ORG组织下所有成员当前区域的审计日志会转储到该追踪器配置的OBS桶或者LTS日志流，但是事件列表界面不支持查看其它组织成员的审计日志。

        :return: The is_organization_tracker of this UpdateTrackerRequestBody.
        :rtype: bool
        """
        return self._is_organization_tracker

    @is_organization_tracker.setter
    def is_organization_tracker(self, is_organization_tracker):
        r"""Sets the is_organization_tracker of this UpdateTrackerRequestBody.

        是否应用到我的组织。 只针对管理类追踪器。设置为true时，ORG组织下所有成员当前区域的审计日志会转储到该追踪器配置的OBS桶或者LTS日志流，但是事件列表界面不支持查看其它组织成员的审计日志。

        :param is_organization_tracker: The is_organization_tracker of this UpdateTrackerRequestBody.
        :type is_organization_tracker: bool
        """
        self._is_organization_tracker = is_organization_tracker

    @property
    def management_event_selector(self):
        r"""Gets the management_event_selector of this UpdateTrackerRequestBody.

        :return: The management_event_selector of this UpdateTrackerRequestBody.
        :rtype: :class:`huaweicloudsdkcts.v3.ManagementEventSelector`
        """
        return self._management_event_selector

    @management_event_selector.setter
    def management_event_selector(self, management_event_selector):
        r"""Sets the management_event_selector of this UpdateTrackerRequestBody.

        :param management_event_selector: The management_event_selector of this UpdateTrackerRequestBody.
        :type management_event_selector: :class:`huaweicloudsdkcts.v3.ManagementEventSelector`
        """
        self._management_event_selector = management_event_selector

    @property
    def is_lts_enabled(self):
        r"""Gets the is_lts_enabled of this UpdateTrackerRequestBody.

        是否打开事件分析。

        :return: The is_lts_enabled of this UpdateTrackerRequestBody.
        :rtype: bool
        """
        return self._is_lts_enabled

    @is_lts_enabled.setter
    def is_lts_enabled(self, is_lts_enabled):
        r"""Sets the is_lts_enabled of this UpdateTrackerRequestBody.

        是否打开事件分析。

        :param is_lts_enabled: The is_lts_enabled of this UpdateTrackerRequestBody.
        :type is_lts_enabled: bool
        """
        self._is_lts_enabled = is_lts_enabled

    @property
    def obs_info(self):
        r"""Gets the obs_info of this UpdateTrackerRequestBody.

        :return: The obs_info of this UpdateTrackerRequestBody.
        :rtype: :class:`huaweicloudsdkcts.v3.TrackerObsInfo`
        """
        return self._obs_info

    @obs_info.setter
    def obs_info(self, obs_info):
        r"""Sets the obs_info of this UpdateTrackerRequestBody.

        :param obs_info: The obs_info of this UpdateTrackerRequestBody.
        :type obs_info: :class:`huaweicloudsdkcts.v3.TrackerObsInfo`
        """
        self._obs_info = obs_info

    @property
    def is_support_trace_files_encryption(self):
        r"""Gets the is_support_trace_files_encryption of this UpdateTrackerRequestBody.

        事件文件转储加密功能开关。 当\"tracker_type\"参数值为\"system\"时该参数值有效。 该参数必须与kms_id参数同时使用。

        :return: The is_support_trace_files_encryption of this UpdateTrackerRequestBody.
        :rtype: bool
        """
        return self._is_support_trace_files_encryption

    @is_support_trace_files_encryption.setter
    def is_support_trace_files_encryption(self, is_support_trace_files_encryption):
        r"""Sets the is_support_trace_files_encryption of this UpdateTrackerRequestBody.

        事件文件转储加密功能开关。 当\"tracker_type\"参数值为\"system\"时该参数值有效。 该参数必须与kms_id参数同时使用。

        :param is_support_trace_files_encryption: The is_support_trace_files_encryption of this UpdateTrackerRequestBody.
        :type is_support_trace_files_encryption: bool
        """
        self._is_support_trace_files_encryption = is_support_trace_files_encryption

    @property
    def kms_id(self):
        r"""Gets the kms_id of this UpdateTrackerRequestBody.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"tracker_type\"参数值为\"system\"时该参数值有效。 当\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :return: The kms_id of this UpdateTrackerRequestBody.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        r"""Sets the kms_id of this UpdateTrackerRequestBody.

        事件文件转储加密所采用的秘钥id（从KMS获取）。 当\"tracker_type\"参数值为\"system\"时该参数值有效。 当\"is_support_trace_files_encryption\"参数值为“是”时，此参数为必选项。

        :param kms_id: The kms_id of this UpdateTrackerRequestBody.
        :type kms_id: str
        """
        self._kms_id = kms_id

    @property
    def is_support_validate(self):
        r"""Gets the is_support_validate of this UpdateTrackerRequestBody.

        事件文件转储时是否打开事件文件校验。 当\"tracker_type\"参数值为\"system\"时该参数值有效。

        :return: The is_support_validate of this UpdateTrackerRequestBody.
        :rtype: bool
        """
        return self._is_support_validate

    @is_support_validate.setter
    def is_support_validate(self, is_support_validate):
        r"""Sets the is_support_validate of this UpdateTrackerRequestBody.

        事件文件转储时是否打开事件文件校验。 当\"tracker_type\"参数值为\"system\"时该参数值有效。

        :param is_support_validate: The is_support_validate of this UpdateTrackerRequestBody.
        :type is_support_validate: bool
        """
        self._is_support_validate = is_support_validate

    @property
    def data_bucket(self):
        r"""Gets the data_bucket of this UpdateTrackerRequestBody.

        :return: The data_bucket of this UpdateTrackerRequestBody.
        :rtype: :class:`huaweicloudsdkcts.v3.DataBucket`
        """
        return self._data_bucket

    @data_bucket.setter
    def data_bucket(self, data_bucket):
        r"""Sets the data_bucket of this UpdateTrackerRequestBody.

        :param data_bucket: The data_bucket of this UpdateTrackerRequestBody.
        :type data_bucket: :class:`huaweicloudsdkcts.v3.DataBucket`
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
        if not isinstance(other, UpdateTrackerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
