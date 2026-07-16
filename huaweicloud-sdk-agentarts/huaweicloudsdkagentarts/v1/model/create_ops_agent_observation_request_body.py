# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpsAgentObservationRequestBody:

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
        'create_by': 'str',
        'create_time': 'int',
        'update_by': 'str',
        'updated_time': 'int',
        'version': 'str',
        'source': 'str',
        'apm_app_id': 'str',
        'aom_prom_id': 'str',
        'apm_app_token': 'str',
        'aom_access_code': 'str',
        'lts_group_id': 'str',
        'lts_stream_id': 'str',
        'lts_label_name': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'status': 'status',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'update_by': 'update_by',
        'updated_time': 'updated_time',
        'version': 'version',
        'source': 'source',
        'apm_app_id': 'apm_app_id',
        'aom_prom_id': 'aom_prom_id',
        'apm_app_token': 'apm_app_token',
        'aom_access_code': 'aom_access_code',
        'lts_group_id': 'lts_group_id',
        'lts_stream_id': 'lts_stream_id',
        'lts_label_name': 'lts_label_name'
    }

    def __init__(self, resource_id=None, resource_name=None, resource_type=None, status=None, create_by=None, create_time=None, update_by=None, updated_time=None, version=None, source=None, apm_app_id=None, aom_prom_id=None, apm_app_token=None, aom_access_code=None, lts_group_id=None, lts_stream_id=None, lts_label_name=None):
        r"""CreateOpsAgentObservationRequestBody

        The model defined in huaweicloud sdk

        :param resource_id: 资源id
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_type: 智能体类型,agent单智能体,multiagent,workflow工作流
        :type resource_type: str
        :param status: 状态,published发布,draft草稿
        :type status: str
        :param create_by: 创建人
        :type create_by: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_by: 更新人
        :type update_by: str
        :param updated_time: 更新时间
        :type updated_time: int
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
        """
        
        

        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._status = None
        self._create_by = None
        self._create_time = None
        self._update_by = None
        self._updated_time = None
        self._version = None
        self._source = None
        self._apm_app_id = None
        self._aom_prom_id = None
        self._apm_app_token = None
        self._aom_access_code = None
        self._lts_group_id = None
        self._lts_stream_id = None
        self._lts_label_name = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if status is not None:
            self.status = status
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if update_by is not None:
            self.update_by = update_by
        if updated_time is not None:
            self.updated_time = updated_time
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

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CreateOpsAgentObservationRequestBody.

        资源id

        :return: The resource_id of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CreateOpsAgentObservationRequestBody.

        资源id

        :param resource_id: The resource_id of this CreateOpsAgentObservationRequestBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this CreateOpsAgentObservationRequestBody.

        资源名称

        :return: The resource_name of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this CreateOpsAgentObservationRequestBody.

        资源名称

        :param resource_name: The resource_name of this CreateOpsAgentObservationRequestBody.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CreateOpsAgentObservationRequestBody.

        智能体类型,agent单智能体,multiagent,workflow工作流

        :return: The resource_type of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CreateOpsAgentObservationRequestBody.

        智能体类型,agent单智能体,multiagent,workflow工作流

        :param resource_type: The resource_type of this CreateOpsAgentObservationRequestBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def status(self):
        r"""Gets the status of this CreateOpsAgentObservationRequestBody.

        状态,published发布,draft草稿

        :return: The status of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateOpsAgentObservationRequestBody.

        状态,published发布,draft草稿

        :param status: The status of this CreateOpsAgentObservationRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def create_by(self):
        r"""Gets the create_by of this CreateOpsAgentObservationRequestBody.

        创建人

        :return: The create_by of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this CreateOpsAgentObservationRequestBody.

        创建人

        :param create_by: The create_by of this CreateOpsAgentObservationRequestBody.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateOpsAgentObservationRequestBody.

        创建时间

        :return: The create_time of this CreateOpsAgentObservationRequestBody.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateOpsAgentObservationRequestBody.

        创建时间

        :param create_time: The create_time of this CreateOpsAgentObservationRequestBody.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_by(self):
        r"""Gets the update_by of this CreateOpsAgentObservationRequestBody.

        更新人

        :return: The update_by of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this CreateOpsAgentObservationRequestBody.

        更新人

        :param update_by: The update_by of this CreateOpsAgentObservationRequestBody.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def updated_time(self):
        r"""Gets the updated_time of this CreateOpsAgentObservationRequestBody.

        更新时间

        :return: The updated_time of this CreateOpsAgentObservationRequestBody.
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this CreateOpsAgentObservationRequestBody.

        更新时间

        :param updated_time: The updated_time of this CreateOpsAgentObservationRequestBody.
        :type updated_time: int
        """
        self._updated_time = updated_time

    @property
    def version(self):
        r"""Gets the version of this CreateOpsAgentObservationRequestBody.

        版本

        :return: The version of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateOpsAgentObservationRequestBody.

        版本

        :param version: The version of this CreateOpsAgentObservationRequestBody.
        :type version: str
        """
        self._version = version

    @property
    def source(self):
        r"""Gets the source of this CreateOpsAgentObservationRequestBody.

        studio, agentrun, api 三种类型，默认为studio

        :return: The source of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateOpsAgentObservationRequestBody.

        studio, agentrun, api 三种类型，默认为studio

        :param source: The source of this CreateOpsAgentObservationRequestBody.
        :type source: str
        """
        self._source = source

    @property
    def apm_app_id(self):
        r"""Gets the apm_app_id of this CreateOpsAgentObservationRequestBody.

        apm的app_id，非必填

        :return: The apm_app_id of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._apm_app_id

    @apm_app_id.setter
    def apm_app_id(self, apm_app_id):
        r"""Sets the apm_app_id of this CreateOpsAgentObservationRequestBody.

        apm的app_id，非必填

        :param apm_app_id: The apm_app_id of this CreateOpsAgentObservationRequestBody.
        :type apm_app_id: str
        """
        self._apm_app_id = apm_app_id

    @property
    def aom_prom_id(self):
        r"""Gets the aom_prom_id of this CreateOpsAgentObservationRequestBody.

        aom的app_id，非必填

        :return: The aom_prom_id of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._aom_prom_id

    @aom_prom_id.setter
    def aom_prom_id(self, aom_prom_id):
        r"""Sets the aom_prom_id of this CreateOpsAgentObservationRequestBody.

        aom的app_id，非必填

        :param aom_prom_id: The aom_prom_id of this CreateOpsAgentObservationRequestBody.
        :type aom_prom_id: str
        """
        self._aom_prom_id = aom_prom_id

    @property
    def apm_app_token(self):
        r"""Gets the apm_app_token of this CreateOpsAgentObservationRequestBody.

        apm token，加密存储，非必填

        :return: The apm_app_token of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._apm_app_token

    @apm_app_token.setter
    def apm_app_token(self, apm_app_token):
        r"""Sets the apm_app_token of this CreateOpsAgentObservationRequestBody.

        apm token，加密存储，非必填

        :param apm_app_token: The apm_app_token of this CreateOpsAgentObservationRequestBody.
        :type apm_app_token: str
        """
        self._apm_app_token = apm_app_token

    @property
    def aom_access_code(self):
        r"""Gets the aom_access_code of this CreateOpsAgentObservationRequestBody.

        aom access_code，加密存储，非必填

        :return: The aom_access_code of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._aom_access_code

    @aom_access_code.setter
    def aom_access_code(self, aom_access_code):
        r"""Sets the aom_access_code of this CreateOpsAgentObservationRequestBody.

        aom access_code，加密存储，非必填

        :param aom_access_code: The aom_access_code of this CreateOpsAgentObservationRequestBody.
        :type aom_access_code: str
        """
        self._aom_access_code = aom_access_code

    @property
    def lts_group_id(self):
        r"""Gets the lts_group_id of this CreateOpsAgentObservationRequestBody.

        lts_group_id，非必填

        :return: The lts_group_id of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._lts_group_id

    @lts_group_id.setter
    def lts_group_id(self, lts_group_id):
        r"""Sets the lts_group_id of this CreateOpsAgentObservationRequestBody.

        lts_group_id，非必填

        :param lts_group_id: The lts_group_id of this CreateOpsAgentObservationRequestBody.
        :type lts_group_id: str
        """
        self._lts_group_id = lts_group_id

    @property
    def lts_stream_id(self):
        r"""Gets the lts_stream_id of this CreateOpsAgentObservationRequestBody.

        lts_stream_id，非必填

        :return: The lts_stream_id of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._lts_stream_id

    @lts_stream_id.setter
    def lts_stream_id(self, lts_stream_id):
        r"""Sets the lts_stream_id of this CreateOpsAgentObservationRequestBody.

        lts_stream_id，非必填

        :param lts_stream_id: The lts_stream_id of this CreateOpsAgentObservationRequestBody.
        :type lts_stream_id: str
        """
        self._lts_stream_id = lts_stream_id

    @property
    def lts_label_name(self):
        r"""Gets the lts_label_name of this CreateOpsAgentObservationRequestBody.

        用于过滤lts日志标签的，key是 __labels__.task_name，对于需要查询日志上报的应用，必填，studio发布的应用必填，否则无法查询到应用日志

        :return: The lts_label_name of this CreateOpsAgentObservationRequestBody.
        :rtype: str
        """
        return self._lts_label_name

    @lts_label_name.setter
    def lts_label_name(self, lts_label_name):
        r"""Sets the lts_label_name of this CreateOpsAgentObservationRequestBody.

        用于过滤lts日志标签的，key是 __labels__.task_name，对于需要查询日志上报的应用，必填，studio发布的应用必填，否则无法查询到应用日志

        :param lts_label_name: The lts_label_name of this CreateOpsAgentObservationRequestBody.
        :type lts_label_name: str
        """
        self._lts_label_name = lts_label_name

    def to_dict(self):
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
        if not isinstance(other, CreateOpsAgentObservationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
