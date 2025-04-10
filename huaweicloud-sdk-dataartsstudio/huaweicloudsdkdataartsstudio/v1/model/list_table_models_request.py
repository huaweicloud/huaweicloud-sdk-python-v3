# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableModelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'x_project_id': 'str',
        'name': 'str',
        'create_by': 'str',
        'approver': 'str',
        'status': 'str',
        'sync_status': 'str',
        'sync_key': 'list[str]',
        'begin_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'model_id': 'str',
        'biz_catalog_id': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'name': 'name',
        'create_by': 'create_by',
        'approver': 'approver',
        'status': 'status',
        'sync_status': 'sync_status',
        'sync_key': 'sync_key',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'model_id': 'model_id',
        'biz_catalog_id': 'biz_catalog_id'
    }

    def __init__(self, workspace=None, x_project_id=None, name=None, create_by=None, approver=None, status=None, sync_status=None, sync_key=None, begin_time=None, end_time=None, limit=None, offset=None, model_id=None, biz_catalog_id=None):
        r"""ListTableModelsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param name: 按名称或编码模糊查询。
        :type name: str
        :param create_by: 按创建者查询。
        :type create_by: str
        :param approver: 按审核人查询。
        :type approver: str
        :param status: 业务状态。 枚举值：   - DRAFT: 草稿   - PUBLISH_DEVELOPING: 发布待审批   - PUBLISHED: 已发布   - OFFLINE_DEVELOPING: 下线待审批   - OFFLINE: 已下线   - REJECT: 已驳回 
        :type status: str
        :param sync_status: 同步状态枚举。 枚举值：   - RUNNING: 同步中   - NO_NEED: 未同步   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败 
        :type sync_status: str
        :param sync_key: 同步任务类型枚举。 枚举值：   - BUSINESS_ASSET: 同步业务资产   - DATA_QUALITY: 创建质量作业   - TECHNICAL_ASSET: 同步技术资产   - META_DATA_LINK: 资产关联   - PHYSICAL_TABLE: 创建表（生产环境）   - DEV_PHYSICAL_TABLE: 创建表（开发环境）   - DLF_TASK: 创建数据开发作业   - MATERIALIZATION: 数值落库（码表）   - PUBLISH_TO_DLM: 发布数据服务API   - SUMMARY_STATUS: 整体状态 
        :type sync_key: list[str]
        :param begin_time: 时间过滤左边界，与end_time一起使用，只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type begin_time: str
        :param end_time: 时间过滤右边界，与begin_time一起使用只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type end_time: str
        :param limit: 每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。
        :type limit: int
        :param offset: 查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。
        :type offset: int
        :param model_id: 所属关系建模的模型ID。
        :type model_id: str
        :param biz_catalog_id: 所属的业务分层的ID。
        :type biz_catalog_id: str
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._name = None
        self._create_by = None
        self._approver = None
        self._status = None
        self._sync_status = None
        self._sync_key = None
        self._begin_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._model_id = None
        self._biz_catalog_id = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if name is not None:
            self.name = name
        if create_by is not None:
            self.create_by = create_by
        if approver is not None:
            self.approver = approver
        if status is not None:
            self.status = status
        if sync_status is not None:
            self.sync_status = sync_status
        if sync_key is not None:
            self.sync_key = sync_key
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.model_id = model_id
        if biz_catalog_id is not None:
            self.biz_catalog_id = biz_catalog_id

    @property
    def workspace(self):
        r"""Gets the workspace of this ListTableModelsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListTableModelsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListTableModelsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListTableModelsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListTableModelsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ListTableModelsRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListTableModelsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ListTableModelsRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def name(self):
        r"""Gets the name of this ListTableModelsRequest.

        按名称或编码模糊查询。

        :return: The name of this ListTableModelsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListTableModelsRequest.

        按名称或编码模糊查询。

        :param name: The name of this ListTableModelsRequest.
        :type name: str
        """
        self._name = name

    @property
    def create_by(self):
        r"""Gets the create_by of this ListTableModelsRequest.

        按创建者查询。

        :return: The create_by of this ListTableModelsRequest.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this ListTableModelsRequest.

        按创建者查询。

        :param create_by: The create_by of this ListTableModelsRequest.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def approver(self):
        r"""Gets the approver of this ListTableModelsRequest.

        按审核人查询。

        :return: The approver of this ListTableModelsRequest.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        r"""Sets the approver of this ListTableModelsRequest.

        按审核人查询。

        :param approver: The approver of this ListTableModelsRequest.
        :type approver: str
        """
        self._approver = approver

    @property
    def status(self):
        r"""Gets the status of this ListTableModelsRequest.

        业务状态。 枚举值：   - DRAFT: 草稿   - PUBLISH_DEVELOPING: 发布待审批   - PUBLISHED: 已发布   - OFFLINE_DEVELOPING: 下线待审批   - OFFLINE: 已下线   - REJECT: 已驳回 

        :return: The status of this ListTableModelsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListTableModelsRequest.

        业务状态。 枚举值：   - DRAFT: 草稿   - PUBLISH_DEVELOPING: 发布待审批   - PUBLISHED: 已发布   - OFFLINE_DEVELOPING: 下线待审批   - OFFLINE: 已下线   - REJECT: 已驳回 

        :param status: The status of this ListTableModelsRequest.
        :type status: str
        """
        self._status = status

    @property
    def sync_status(self):
        r"""Gets the sync_status of this ListTableModelsRequest.

        同步状态枚举。 枚举值：   - RUNNING: 同步中   - NO_NEED: 未同步   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败 

        :return: The sync_status of this ListTableModelsRequest.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        r"""Sets the sync_status of this ListTableModelsRequest.

        同步状态枚举。 枚举值：   - RUNNING: 同步中   - NO_NEED: 未同步   - SUMMARY_SUCCESS: 整体成功   - SUMMARY_FAILED: 整体失败 

        :param sync_status: The sync_status of this ListTableModelsRequest.
        :type sync_status: str
        """
        self._sync_status = sync_status

    @property
    def sync_key(self):
        r"""Gets the sync_key of this ListTableModelsRequest.

        同步任务类型枚举。 枚举值：   - BUSINESS_ASSET: 同步业务资产   - DATA_QUALITY: 创建质量作业   - TECHNICAL_ASSET: 同步技术资产   - META_DATA_LINK: 资产关联   - PHYSICAL_TABLE: 创建表（生产环境）   - DEV_PHYSICAL_TABLE: 创建表（开发环境）   - DLF_TASK: 创建数据开发作业   - MATERIALIZATION: 数值落库（码表）   - PUBLISH_TO_DLM: 发布数据服务API   - SUMMARY_STATUS: 整体状态 

        :return: The sync_key of this ListTableModelsRequest.
        :rtype: list[str]
        """
        return self._sync_key

    @sync_key.setter
    def sync_key(self, sync_key):
        r"""Sets the sync_key of this ListTableModelsRequest.

        同步任务类型枚举。 枚举值：   - BUSINESS_ASSET: 同步业务资产   - DATA_QUALITY: 创建质量作业   - TECHNICAL_ASSET: 同步技术资产   - META_DATA_LINK: 资产关联   - PHYSICAL_TABLE: 创建表（生产环境）   - DEV_PHYSICAL_TABLE: 创建表（开发环境）   - DLF_TASK: 创建数据开发作业   - MATERIALIZATION: 数值落库（码表）   - PUBLISH_TO_DLM: 发布数据服务API   - SUMMARY_STATUS: 整体状态 

        :param sync_key: The sync_key of this ListTableModelsRequest.
        :type sync_key: list[str]
        """
        self._sync_key = sync_key

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListTableModelsRequest.

        时间过滤左边界，与end_time一起使用，只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The begin_time of this ListTableModelsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListTableModelsRequest.

        时间过滤左边界，与end_time一起使用，只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param begin_time: The begin_time of this ListTableModelsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTableModelsRequest.

        时间过滤右边界，与begin_time一起使用只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The end_time of this ListTableModelsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTableModelsRequest.

        时间过滤右边界，与begin_time一起使用只支持时间范围过滤，单边过滤无效。格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param end_time: The end_time of this ListTableModelsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListTableModelsRequest.

        每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。

        :return: The limit of this ListTableModelsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTableModelsRequest.

        每页查询条数，即查询Y条数据。默认值50，取值范围[1,100]。

        :param limit: The limit of this ListTableModelsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTableModelsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。

        :return: The offset of this ListTableModelsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTableModelsRequest.

        查询起始坐标，即跳过X条数据，仅支持0或limit的整数倍，不满足则向下取整，默认值0。

        :param offset: The offset of this ListTableModelsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def model_id(self):
        r"""Gets the model_id of this ListTableModelsRequest.

        所属关系建模的模型ID。

        :return: The model_id of this ListTableModelsRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this ListTableModelsRequest.

        所属关系建模的模型ID。

        :param model_id: The model_id of this ListTableModelsRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def biz_catalog_id(self):
        r"""Gets the biz_catalog_id of this ListTableModelsRequest.

        所属的业务分层的ID。

        :return: The biz_catalog_id of this ListTableModelsRequest.
        :rtype: str
        """
        return self._biz_catalog_id

    @biz_catalog_id.setter
    def biz_catalog_id(self, biz_catalog_id):
        r"""Sets the biz_catalog_id of this ListTableModelsRequest.

        所属的业务分层的ID。

        :param biz_catalog_id: The biz_catalog_id of this ListTableModelsRequest.
        :type biz_catalog_id: str
        """
        self._biz_catalog_id = biz_catalog_id

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
        if not isinstance(other, ListTableModelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
