# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class List2dModelTrainingJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'state': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'create_until': 'str',
        'create_since': 'str',
        'query_project_id': 'str',
        'update_since': 'str',
        'update_until': 'str',
        'batch_name': 'str',
        'tag': 'str',
        'job_id': 'str',
        'name': 'str',
        'model_resolution': 'str',
        'is_flexus': 'bool',
        'is_live_copy': 'bool',
        'train_location': 'str',
        'is_ondemand_resource': 'bool'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'state': 'state',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'create_until': 'create_until',
        'create_since': 'create_since',
        'query_project_id': 'query_project_id',
        'update_since': 'update_since',
        'update_until': 'update_until',
        'batch_name': 'batch_name',
        'tag': 'tag',
        'job_id': 'job_id',
        'name': 'name',
        'model_resolution': 'model_resolution',
        'is_flexus': 'is_flexus',
        'is_live_copy': 'is_live_copy',
        'train_location': 'train_location',
        'is_ondemand_resource': 'is_ondemand_resource'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, state=None, sort_key=None, sort_dir=None, create_until=None, create_since=None, query_project_id=None, update_since=None, update_until=None, batch_name=None, tag=None, job_id=None, name=None, model_resolution=None, is_flexus=None, is_live_copy=None, train_location=None, is_ondemand_resource=None):
        r"""List2dModelTrainingJobRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param state: 任务状态，默认所有状态。  可多个状态查询，使用英文逗号分隔。  如state&#x3D;CREATING,PUBLISHED
        :type state: str
        :param sort_key: 排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order
        :type sort_key: str
        :param sort_dir: 排序方式。 * asc：升序 * desc：降序  默认asc升序。
        :type sort_dir: str
        :param create_until: 过滤创建时间&lt;&#x3D;输入时间的记录。
        :type create_until: str
        :param create_since: 过滤创建时间&gt;&#x3D;输入时间的记录。
        :type create_since: str
        :param query_project_id: 查询租户id。
        :type query_project_id: str
        :param update_since: 过滤更新时间&gt;&#x3D;输入时间的记录。
        :type update_since: str
        :param update_until: 过滤更新时间&gt;&#x3D;输入时间的记录。
        :type update_until: str
        :param batch_name: 任务批次名称。
        :type batch_name: str
        :param tag: 任务标签。
        :type tag: str
        :param job_id: 任务ID。
        :type job_id: str
        :param name: 分身数字人模型名称
        :type name: str
        :param model_resolution: 模型分辨率
        :type model_resolution: str
        :param is_flexus: 是否是flexus任务
        :type is_flexus: bool
        :param is_live_copy: 是否是直播间复刻任务
        :type is_live_copy: bool
        :param train_location: 训练region
        :type train_location: str
        :param is_ondemand_resource: 是否测试版
        :type is_ondemand_resource: bool
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._state = None
        self._sort_key = None
        self._sort_dir = None
        self._create_until = None
        self._create_since = None
        self._query_project_id = None
        self._update_since = None
        self._update_until = None
        self._batch_name = None
        self._tag = None
        self._job_id = None
        self._name = None
        self._model_resolution = None
        self._is_flexus = None
        self._is_live_copy = None
        self._train_location = None
        self._is_ondemand_resource = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if state is not None:
            self.state = state
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if create_until is not None:
            self.create_until = create_until
        if create_since is not None:
            self.create_since = create_since
        if query_project_id is not None:
            self.query_project_id = query_project_id
        if update_since is not None:
            self.update_since = update_since
        if update_until is not None:
            self.update_until = update_until
        if batch_name is not None:
            self.batch_name = batch_name
        if tag is not None:
            self.tag = tag
        if job_id is not None:
            self.job_id = job_id
        if name is not None:
            self.name = name
        if model_resolution is not None:
            self.model_resolution = model_resolution
        if is_flexus is not None:
            self.is_flexus = is_flexus
        if is_live_copy is not None:
            self.is_live_copy = is_live_copy
        if train_location is not None:
            self.train_location = train_location
        if is_ondemand_resource is not None:
            self.is_ondemand_resource = is_ondemand_resource

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this List2dModelTrainingJobRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this List2dModelTrainingJobRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this List2dModelTrainingJobRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this List2dModelTrainingJobRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this List2dModelTrainingJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this List2dModelTrainingJobRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this List2dModelTrainingJobRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this List2dModelTrainingJobRequest.

        每页显示的条目数量。

        :return: The limit of this List2dModelTrainingJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this List2dModelTrainingJobRequest.

        每页显示的条目数量。

        :param limit: The limit of this List2dModelTrainingJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def state(self):
        r"""Gets the state of this List2dModelTrainingJobRequest.

        任务状态，默认所有状态。  可多个状态查询，使用英文逗号分隔。  如state=CREATING,PUBLISHED

        :return: The state of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this List2dModelTrainingJobRequest.

        任务状态，默认所有状态。  可多个状态查询，使用英文逗号分隔。  如state=CREATING,PUBLISHED

        :param state: The state of this List2dModelTrainingJobRequest.
        :type state: str
        """
        self._state = state

    @property
    def sort_key(self):
        r"""Gets the sort_key of this List2dModelTrainingJobRequest.

        排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order

        :return: The sort_key of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this List2dModelTrainingJobRequest.

        排序字段，支持的排序方式有： - 按创建时间排序：create_time - 按更新时间排序：update_time - 按资产排序：asset_order

        :param sort_key: The sort_key of this List2dModelTrainingJobRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this List2dModelTrainingJobRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :return: The sort_dir of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this List2dModelTrainingJobRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :param sort_dir: The sort_dir of this List2dModelTrainingJobRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def create_until(self):
        r"""Gets the create_until of this List2dModelTrainingJobRequest.

        过滤创建时间<=输入时间的记录。

        :return: The create_until of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._create_until

    @create_until.setter
    def create_until(self, create_until):
        r"""Sets the create_until of this List2dModelTrainingJobRequest.

        过滤创建时间<=输入时间的记录。

        :param create_until: The create_until of this List2dModelTrainingJobRequest.
        :type create_until: str
        """
        self._create_until = create_until

    @property
    def create_since(self):
        r"""Gets the create_since of this List2dModelTrainingJobRequest.

        过滤创建时间>=输入时间的记录。

        :return: The create_since of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._create_since

    @create_since.setter
    def create_since(self, create_since):
        r"""Sets the create_since of this List2dModelTrainingJobRequest.

        过滤创建时间>=输入时间的记录。

        :param create_since: The create_since of this List2dModelTrainingJobRequest.
        :type create_since: str
        """
        self._create_since = create_since

    @property
    def query_project_id(self):
        r"""Gets the query_project_id of this List2dModelTrainingJobRequest.

        查询租户id。

        :return: The query_project_id of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._query_project_id

    @query_project_id.setter
    def query_project_id(self, query_project_id):
        r"""Sets the query_project_id of this List2dModelTrainingJobRequest.

        查询租户id。

        :param query_project_id: The query_project_id of this List2dModelTrainingJobRequest.
        :type query_project_id: str
        """
        self._query_project_id = query_project_id

    @property
    def update_since(self):
        r"""Gets the update_since of this List2dModelTrainingJobRequest.

        过滤更新时间>=输入时间的记录。

        :return: The update_since of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._update_since

    @update_since.setter
    def update_since(self, update_since):
        r"""Sets the update_since of this List2dModelTrainingJobRequest.

        过滤更新时间>=输入时间的记录。

        :param update_since: The update_since of this List2dModelTrainingJobRequest.
        :type update_since: str
        """
        self._update_since = update_since

    @property
    def update_until(self):
        r"""Gets the update_until of this List2dModelTrainingJobRequest.

        过滤更新时间>=输入时间的记录。

        :return: The update_until of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._update_until

    @update_until.setter
    def update_until(self, update_until):
        r"""Sets the update_until of this List2dModelTrainingJobRequest.

        过滤更新时间>=输入时间的记录。

        :param update_until: The update_until of this List2dModelTrainingJobRequest.
        :type update_until: str
        """
        self._update_until = update_until

    @property
    def batch_name(self):
        r"""Gets the batch_name of this List2dModelTrainingJobRequest.

        任务批次名称。

        :return: The batch_name of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        r"""Sets the batch_name of this List2dModelTrainingJobRequest.

        任务批次名称。

        :param batch_name: The batch_name of this List2dModelTrainingJobRequest.
        :type batch_name: str
        """
        self._batch_name = batch_name

    @property
    def tag(self):
        r"""Gets the tag of this List2dModelTrainingJobRequest.

        任务标签。

        :return: The tag of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this List2dModelTrainingJobRequest.

        任务标签。

        :param tag: The tag of this List2dModelTrainingJobRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def job_id(self):
        r"""Gets the job_id of this List2dModelTrainingJobRequest.

        任务ID。

        :return: The job_id of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this List2dModelTrainingJobRequest.

        任务ID。

        :param job_id: The job_id of this List2dModelTrainingJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def name(self):
        r"""Gets the name of this List2dModelTrainingJobRequest.

        分身数字人模型名称

        :return: The name of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this List2dModelTrainingJobRequest.

        分身数字人模型名称

        :param name: The name of this List2dModelTrainingJobRequest.
        :type name: str
        """
        self._name = name

    @property
    def model_resolution(self):
        r"""Gets the model_resolution of this List2dModelTrainingJobRequest.

        模型分辨率

        :return: The model_resolution of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._model_resolution

    @model_resolution.setter
    def model_resolution(self, model_resolution):
        r"""Sets the model_resolution of this List2dModelTrainingJobRequest.

        模型分辨率

        :param model_resolution: The model_resolution of this List2dModelTrainingJobRequest.
        :type model_resolution: str
        """
        self._model_resolution = model_resolution

    @property
    def is_flexus(self):
        r"""Gets the is_flexus of this List2dModelTrainingJobRequest.

        是否是flexus任务

        :return: The is_flexus of this List2dModelTrainingJobRequest.
        :rtype: bool
        """
        return self._is_flexus

    @is_flexus.setter
    def is_flexus(self, is_flexus):
        r"""Sets the is_flexus of this List2dModelTrainingJobRequest.

        是否是flexus任务

        :param is_flexus: The is_flexus of this List2dModelTrainingJobRequest.
        :type is_flexus: bool
        """
        self._is_flexus = is_flexus

    @property
    def is_live_copy(self):
        r"""Gets the is_live_copy of this List2dModelTrainingJobRequest.

        是否是直播间复刻任务

        :return: The is_live_copy of this List2dModelTrainingJobRequest.
        :rtype: bool
        """
        return self._is_live_copy

    @is_live_copy.setter
    def is_live_copy(self, is_live_copy):
        r"""Sets the is_live_copy of this List2dModelTrainingJobRequest.

        是否是直播间复刻任务

        :param is_live_copy: The is_live_copy of this List2dModelTrainingJobRequest.
        :type is_live_copy: bool
        """
        self._is_live_copy = is_live_copy

    @property
    def train_location(self):
        r"""Gets the train_location of this List2dModelTrainingJobRequest.

        训练region

        :return: The train_location of this List2dModelTrainingJobRequest.
        :rtype: str
        """
        return self._train_location

    @train_location.setter
    def train_location(self, train_location):
        r"""Sets the train_location of this List2dModelTrainingJobRequest.

        训练region

        :param train_location: The train_location of this List2dModelTrainingJobRequest.
        :type train_location: str
        """
        self._train_location = train_location

    @property
    def is_ondemand_resource(self):
        r"""Gets the is_ondemand_resource of this List2dModelTrainingJobRequest.

        是否测试版

        :return: The is_ondemand_resource of this List2dModelTrainingJobRequest.
        :rtype: bool
        """
        return self._is_ondemand_resource

    @is_ondemand_resource.setter
    def is_ondemand_resource(self, is_ondemand_resource):
        r"""Sets the is_ondemand_resource of this List2dModelTrainingJobRequest.

        是否测试版

        :param is_ondemand_resource: The is_ondemand_resource of this List2dModelTrainingJobRequest.
        :type is_ondemand_resource: bool
        """
        self._is_ondemand_resource = is_ondemand_resource

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
        if not isinstance(other, List2dModelTrainingJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
