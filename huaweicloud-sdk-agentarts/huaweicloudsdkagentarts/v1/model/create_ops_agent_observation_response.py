# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpsAgentObservationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'version': 'str',
        'source': 'str',
        'apm_app_id': 'str',
        'aom_prom_id': 'str',
        'apm_app_token': 'str',
        'aom_access_code': 'str',
        'lts_group_id': 'str',
        'lts_stream_id': 'str',
        'lts_label_name': 'str',
        'apm_exporter_endpoint': 'str',
        'aom_exporter_endpoint': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'version': 'version',
        'source': 'source',
        'apm_app_id': 'apm_app_id',
        'aom_prom_id': 'aom_prom_id',
        'apm_app_token': 'apm_app_token',
        'aom_access_code': 'aom_access_code',
        'lts_group_id': 'lts_group_id',
        'lts_stream_id': 'lts_stream_id',
        'lts_label_name': 'lts_label_name',
        'apm_exporter_endpoint': 'apm_exporter_endpoint',
        'aom_exporter_endpoint': 'aom_exporter_endpoint'
    }

    def __init__(self, resource_id=None, resource_name=None, resource_type=None, status=None, created_at=None, updated_at=None, version=None, source=None, apm_app_id=None, aom_prom_id=None, apm_app_token=None, aom_access_code=None, lts_group_id=None, lts_stream_id=None, lts_label_name=None, apm_exporter_endpoint=None, aom_exporter_endpoint=None):
        r"""CreateOpsAgentObservationResponse

        The model defined in huaweicloud sdk

        :param resource_id: 资源id
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_type: 资源类型 agent单智能体 workflow工作流 multiagents多智能体
        :type resource_type: str
        :param status: 状态 published发布态 draft草稿态
        :type status: str
        :param created_at: **参数解释：** 该合成条目生成的精确时间戳。 **约束限制：** 符合ISO8601标准。 **取值范围：** 日期时间字符串。 **默认取值：** 不涉及。 
        :type created_at: datetime
        :param updated_at: **参数解释：** 该合成条目生成的精确时间戳。 **约束限制：** 符合ISO8601标准。 **取值范围：** 日期时间字符串。 **默认取值：** 不涉及。 
        :type updated_at: datetime
        :param version: 版本
        :type version: str
        :param source: studio, agentrun, api 三种类型，默认为studio
        :type source: str
        :param apm_app_id: apm的app_id，非必填
        :type apm_app_id: str
        :param aom_prom_id: aom的app_id，非必填
        :type aom_prom_id: str
        :param apm_app_token: apm token，加密存储，非必填
        :type apm_app_token: str
        :param aom_access_code: aom access_code，加密存储，非必填
        :type aom_access_code: str
        :param lts_group_id: lts_group_id，非必填
        :type lts_group_id: str
        :param lts_stream_id: lts_stream_id，非必填
        :type lts_stream_id: str
        :param lts_label_name: 用于过滤lts日志标签的，key是 __labels__.task_name，对于需要查询日志上报的应用，必填，studio发布的应用必填，否则无法查询到应用日志
        :type lts_label_name: str
        :param apm_exporter_endpoint: apm上报地址
        :type apm_exporter_endpoint: str
        :param aom_exporter_endpoint: aom上报地址
        :type aom_exporter_endpoint: str
        """
        
        super().__init__()

        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._version = None
        self._source = None
        self._apm_app_id = None
        self._aom_prom_id = None
        self._apm_app_token = None
        self._aom_access_code = None
        self._lts_group_id = None
        self._lts_stream_id = None
        self._lts_label_name = None
        self._apm_exporter_endpoint = None
        self._aom_exporter_endpoint = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if version is not None:
            self.version = version
        if source is not None:
            self.source = source
        if apm_app_id is not None:
            self.apm_app_id = apm_app_id
        if aom_prom_id is not None:
            self.aom_prom_id = aom_prom_id
        if apm_app_token is not None:
            self.apm_app_token = apm_app_token
        if aom_access_code is not None:
            self.aom_access_code = aom_access_code
        if lts_group_id is not None:
            self.lts_group_id = lts_group_id
        if lts_stream_id is not None:
            self.lts_stream_id = lts_stream_id
        if lts_label_name is not None:
            self.lts_label_name = lts_label_name
        if apm_exporter_endpoint is not None:
            self.apm_exporter_endpoint = apm_exporter_endpoint
        if aom_exporter_endpoint is not None:
            self.aom_exporter_endpoint = aom_exporter_endpoint

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CreateOpsAgentObservationResponse.

        资源id

        :return: The resource_id of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CreateOpsAgentObservationResponse.

        资源id

        :param resource_id: The resource_id of this CreateOpsAgentObservationResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this CreateOpsAgentObservationResponse.

        资源名称

        :return: The resource_name of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this CreateOpsAgentObservationResponse.

        资源名称

        :param resource_name: The resource_name of this CreateOpsAgentObservationResponse.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CreateOpsAgentObservationResponse.

        资源类型 agent单智能体 workflow工作流 multiagents多智能体

        :return: The resource_type of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CreateOpsAgentObservationResponse.

        资源类型 agent单智能体 workflow工作流 multiagents多智能体

        :param resource_type: The resource_type of this CreateOpsAgentObservationResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def status(self):
        r"""Gets the status of this CreateOpsAgentObservationResponse.

        状态 published发布态 draft草稿态

        :return: The status of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateOpsAgentObservationResponse.

        状态 published发布态 draft草稿态

        :param status: The status of this CreateOpsAgentObservationResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateOpsAgentObservationResponse.

        **参数解释：** 该合成条目生成的精确时间戳。 **约束限制：** 符合ISO8601标准。 **取值范围：** 日期时间字符串。 **默认取值：** 不涉及。 

        :return: The created_at of this CreateOpsAgentObservationResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateOpsAgentObservationResponse.

        **参数解释：** 该合成条目生成的精确时间戳。 **约束限制：** 符合ISO8601标准。 **取值范围：** 日期时间字符串。 **默认取值：** 不涉及。 

        :param created_at: The created_at of this CreateOpsAgentObservationResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateOpsAgentObservationResponse.

        **参数解释：** 该合成条目生成的精确时间戳。 **约束限制：** 符合ISO8601标准。 **取值范围：** 日期时间字符串。 **默认取值：** 不涉及。 

        :return: The updated_at of this CreateOpsAgentObservationResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateOpsAgentObservationResponse.

        **参数解释：** 该合成条目生成的精确时间戳。 **约束限制：** 符合ISO8601标准。 **取值范围：** 日期时间字符串。 **默认取值：** 不涉及。 

        :param updated_at: The updated_at of this CreateOpsAgentObservationResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def version(self):
        r"""Gets the version of this CreateOpsAgentObservationResponse.

        版本

        :return: The version of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateOpsAgentObservationResponse.

        版本

        :param version: The version of this CreateOpsAgentObservationResponse.
        :type version: str
        """
        self._version = version

    @property
    def source(self):
        r"""Gets the source of this CreateOpsAgentObservationResponse.

        studio, agentrun, api 三种类型，默认为studio

        :return: The source of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateOpsAgentObservationResponse.

        studio, agentrun, api 三种类型，默认为studio

        :param source: The source of this CreateOpsAgentObservationResponse.
        :type source: str
        """
        self._source = source

    @property
    def apm_app_id(self):
        r"""Gets the apm_app_id of this CreateOpsAgentObservationResponse.

        apm的app_id，非必填

        :return: The apm_app_id of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._apm_app_id

    @apm_app_id.setter
    def apm_app_id(self, apm_app_id):
        r"""Sets the apm_app_id of this CreateOpsAgentObservationResponse.

        apm的app_id，非必填

        :param apm_app_id: The apm_app_id of this CreateOpsAgentObservationResponse.
        :type apm_app_id: str
        """
        self._apm_app_id = apm_app_id

    @property
    def aom_prom_id(self):
        r"""Gets the aom_prom_id of this CreateOpsAgentObservationResponse.

        aom的app_id，非必填

        :return: The aom_prom_id of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._aom_prom_id

    @aom_prom_id.setter
    def aom_prom_id(self, aom_prom_id):
        r"""Sets the aom_prom_id of this CreateOpsAgentObservationResponse.

        aom的app_id，非必填

        :param aom_prom_id: The aom_prom_id of this CreateOpsAgentObservationResponse.
        :type aom_prom_id: str
        """
        self._aom_prom_id = aom_prom_id

    @property
    def apm_app_token(self):
        r"""Gets the apm_app_token of this CreateOpsAgentObservationResponse.

        apm token，加密存储，非必填

        :return: The apm_app_token of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._apm_app_token

    @apm_app_token.setter
    def apm_app_token(self, apm_app_token):
        r"""Sets the apm_app_token of this CreateOpsAgentObservationResponse.

        apm token，加密存储，非必填

        :param apm_app_token: The apm_app_token of this CreateOpsAgentObservationResponse.
        :type apm_app_token: str
        """
        self._apm_app_token = apm_app_token

    @property
    def aom_access_code(self):
        r"""Gets the aom_access_code of this CreateOpsAgentObservationResponse.

        aom access_code，加密存储，非必填

        :return: The aom_access_code of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._aom_access_code

    @aom_access_code.setter
    def aom_access_code(self, aom_access_code):
        r"""Sets the aom_access_code of this CreateOpsAgentObservationResponse.

        aom access_code，加密存储，非必填

        :param aom_access_code: The aom_access_code of this CreateOpsAgentObservationResponse.
        :type aom_access_code: str
        """
        self._aom_access_code = aom_access_code

    @property
    def lts_group_id(self):
        r"""Gets the lts_group_id of this CreateOpsAgentObservationResponse.

        lts_group_id，非必填

        :return: The lts_group_id of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._lts_group_id

    @lts_group_id.setter
    def lts_group_id(self, lts_group_id):
        r"""Sets the lts_group_id of this CreateOpsAgentObservationResponse.

        lts_group_id，非必填

        :param lts_group_id: The lts_group_id of this CreateOpsAgentObservationResponse.
        :type lts_group_id: str
        """
        self._lts_group_id = lts_group_id

    @property
    def lts_stream_id(self):
        r"""Gets the lts_stream_id of this CreateOpsAgentObservationResponse.

        lts_stream_id，非必填

        :return: The lts_stream_id of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._lts_stream_id

    @lts_stream_id.setter
    def lts_stream_id(self, lts_stream_id):
        r"""Sets the lts_stream_id of this CreateOpsAgentObservationResponse.

        lts_stream_id，非必填

        :param lts_stream_id: The lts_stream_id of this CreateOpsAgentObservationResponse.
        :type lts_stream_id: str
        """
        self._lts_stream_id = lts_stream_id

    @property
    def lts_label_name(self):
        r"""Gets the lts_label_name of this CreateOpsAgentObservationResponse.

        用于过滤lts日志标签的，key是 __labels__.task_name，对于需要查询日志上报的应用，必填，studio发布的应用必填，否则无法查询到应用日志

        :return: The lts_label_name of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._lts_label_name

    @lts_label_name.setter
    def lts_label_name(self, lts_label_name):
        r"""Sets the lts_label_name of this CreateOpsAgentObservationResponse.

        用于过滤lts日志标签的，key是 __labels__.task_name，对于需要查询日志上报的应用，必填，studio发布的应用必填，否则无法查询到应用日志

        :param lts_label_name: The lts_label_name of this CreateOpsAgentObservationResponse.
        :type lts_label_name: str
        """
        self._lts_label_name = lts_label_name

    @property
    def apm_exporter_endpoint(self):
        r"""Gets the apm_exporter_endpoint of this CreateOpsAgentObservationResponse.

        apm上报地址

        :return: The apm_exporter_endpoint of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._apm_exporter_endpoint

    @apm_exporter_endpoint.setter
    def apm_exporter_endpoint(self, apm_exporter_endpoint):
        r"""Sets the apm_exporter_endpoint of this CreateOpsAgentObservationResponse.

        apm上报地址

        :param apm_exporter_endpoint: The apm_exporter_endpoint of this CreateOpsAgentObservationResponse.
        :type apm_exporter_endpoint: str
        """
        self._apm_exporter_endpoint = apm_exporter_endpoint

    @property
    def aom_exporter_endpoint(self):
        r"""Gets the aom_exporter_endpoint of this CreateOpsAgentObservationResponse.

        aom上报地址

        :return: The aom_exporter_endpoint of this CreateOpsAgentObservationResponse.
        :rtype: str
        """
        return self._aom_exporter_endpoint

    @aom_exporter_endpoint.setter
    def aom_exporter_endpoint(self, aom_exporter_endpoint):
        r"""Sets the aom_exporter_endpoint of this CreateOpsAgentObservationResponse.

        aom上报地址

        :param aom_exporter_endpoint: The aom_exporter_endpoint of this CreateOpsAgentObservationResponse.
        :type aom_exporter_endpoint: str
        """
        self._aom_exporter_endpoint = aom_exporter_endpoint

    def to_dict(self):
        import warnings
        warnings.warn("CreateOpsAgentObservationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateOpsAgentObservationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
