# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVoiceTrainingJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'create_until': 'str',
        'create_since': 'str',
        'update_until': 'str',
        'update_since': 'str',
        'x_app_user_id': 'str',
        'state': 'str',
        'job_id': 'str',
        'voice_name': 'str',
        'tag': 'str',
        'job_type': 'str',
        'batch_name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'is_ondemand_resource': 'bool'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'create_until': 'create_until',
        'create_since': 'create_since',
        'update_until': 'update_until',
        'update_since': 'update_since',
        'x_app_user_id': 'X-App-UserId',
        'state': 'state',
        'job_id': 'job_id',
        'voice_name': 'voice_name',
        'tag': 'tag',
        'job_type': 'job_type',
        'batch_name': 'batch_name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'is_ondemand_resource': 'is_ondemand_resource'
    }

    def __init__(self, offset=None, limit=None, create_until=None, create_since=None, update_until=None, update_since=None, x_app_user_id=None, state=None, job_id=None, voice_name=None, tag=None, job_type=None, batch_name=None, sort_key=None, sort_dir=None, is_ondemand_resource=None):
        r"""ListVoiceTrainingJobRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param create_until: 过滤创建时间&lt;&#x3D;输入时间的记录。
        :type create_until: str
        :param create_since: 过滤创建时间&gt;&#x3D;输入时间的记录。
        :type create_since: str
        :param update_until: 过滤更新时间&lt;&#x3D;输入时间的记录。
        :type update_until: str
        :param update_since: 过滤更新时间&gt;&#x3D;输入时间的记录。
        :type update_since: str
        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param state: 任务状态，默认所有状态。 可多个状态查询，使用英文逗号分隔。 如state&#x3D;FAILED,WAITING
        :type state: str
        :param job_id: 任务id。
        :type job_id: str
        :param voice_name: 声音名称。
        :type voice_name: str
        :param tag: 任务标签。
        :type tag: str
        :param job_type: 训练类型。 * BASIC: 基础版(20句话) * MIDDLE: 进阶版(100句话) * ADVANCE: 高级版 * THIRD_PARTY: 第三方出门问问训练版 * THIRD_PARTY_LJZN: 第三方逻辑智能训练版 * FLEXUS: Flexus版---用的是大模型特征提取
        :type job_type: str
        :param batch_name: 批次名称。
        :type batch_name: str
        :param sort_key: 排序字段，当前支持：ceate_time/update_time
        :type sort_key: str
        :param sort_dir: 排序规则：desc(降序)/asc(升序)
        :type sort_dir: str
        :param is_ondemand_resource: 是否是按需任务
        :type is_ondemand_resource: bool
        """
        
        

        self._offset = None
        self._limit = None
        self._create_until = None
        self._create_since = None
        self._update_until = None
        self._update_since = None
        self._x_app_user_id = None
        self._state = None
        self._job_id = None
        self._voice_name = None
        self._tag = None
        self._job_type = None
        self._batch_name = None
        self._sort_key = None
        self._sort_dir = None
        self._is_ondemand_resource = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if create_until is not None:
            self.create_until = create_until
        if create_since is not None:
            self.create_since = create_since
        if update_until is not None:
            self.update_until = update_until
        if update_since is not None:
            self.update_since = update_since
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if state is not None:
            self.state = state
        if job_id is not None:
            self.job_id = job_id
        if voice_name is not None:
            self.voice_name = voice_name
        if tag is not None:
            self.tag = tag
        if job_type is not None:
            self.job_type = job_type
        if batch_name is not None:
            self.batch_name = batch_name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if is_ondemand_resource is not None:
            self.is_ondemand_resource = is_ondemand_resource

    @property
    def offset(self):
        r"""Gets the offset of this ListVoiceTrainingJobRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListVoiceTrainingJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVoiceTrainingJobRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListVoiceTrainingJobRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListVoiceTrainingJobRequest.

        每页显示的条目数量。

        :return: The limit of this ListVoiceTrainingJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVoiceTrainingJobRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListVoiceTrainingJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def create_until(self):
        r"""Gets the create_until of this ListVoiceTrainingJobRequest.

        过滤创建时间<=输入时间的记录。

        :return: The create_until of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._create_until

    @create_until.setter
    def create_until(self, create_until):
        r"""Sets the create_until of this ListVoiceTrainingJobRequest.

        过滤创建时间<=输入时间的记录。

        :param create_until: The create_until of this ListVoiceTrainingJobRequest.
        :type create_until: str
        """
        self._create_until = create_until

    @property
    def create_since(self):
        r"""Gets the create_since of this ListVoiceTrainingJobRequest.

        过滤创建时间>=输入时间的记录。

        :return: The create_since of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._create_since

    @create_since.setter
    def create_since(self, create_since):
        r"""Sets the create_since of this ListVoiceTrainingJobRequest.

        过滤创建时间>=输入时间的记录。

        :param create_since: The create_since of this ListVoiceTrainingJobRequest.
        :type create_since: str
        """
        self._create_since = create_since

    @property
    def update_until(self):
        r"""Gets the update_until of this ListVoiceTrainingJobRequest.

        过滤更新时间<=输入时间的记录。

        :return: The update_until of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._update_until

    @update_until.setter
    def update_until(self, update_until):
        r"""Sets the update_until of this ListVoiceTrainingJobRequest.

        过滤更新时间<=输入时间的记录。

        :param update_until: The update_until of this ListVoiceTrainingJobRequest.
        :type update_until: str
        """
        self._update_until = update_until

    @property
    def update_since(self):
        r"""Gets the update_since of this ListVoiceTrainingJobRequest.

        过滤更新时间>=输入时间的记录。

        :return: The update_since of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._update_since

    @update_since.setter
    def update_since(self, update_since):
        r"""Sets the update_since of this ListVoiceTrainingJobRequest.

        过滤更新时间>=输入时间的记录。

        :param update_since: The update_since of this ListVoiceTrainingJobRequest.
        :type update_since: str
        """
        self._update_since = update_since

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListVoiceTrainingJobRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListVoiceTrainingJobRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListVoiceTrainingJobRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def state(self):
        r"""Gets the state of this ListVoiceTrainingJobRequest.

        任务状态，默认所有状态。 可多个状态查询，使用英文逗号分隔。 如state=FAILED,WAITING

        :return: The state of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListVoiceTrainingJobRequest.

        任务状态，默认所有状态。 可多个状态查询，使用英文逗号分隔。 如state=FAILED,WAITING

        :param state: The state of this ListVoiceTrainingJobRequest.
        :type state: str
        """
        self._state = state

    @property
    def job_id(self):
        r"""Gets the job_id of this ListVoiceTrainingJobRequest.

        任务id。

        :return: The job_id of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListVoiceTrainingJobRequest.

        任务id。

        :param job_id: The job_id of this ListVoiceTrainingJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def voice_name(self):
        r"""Gets the voice_name of this ListVoiceTrainingJobRequest.

        声音名称。

        :return: The voice_name of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._voice_name

    @voice_name.setter
    def voice_name(self, voice_name):
        r"""Sets the voice_name of this ListVoiceTrainingJobRequest.

        声音名称。

        :param voice_name: The voice_name of this ListVoiceTrainingJobRequest.
        :type voice_name: str
        """
        self._voice_name = voice_name

    @property
    def tag(self):
        r"""Gets the tag of this ListVoiceTrainingJobRequest.

        任务标签。

        :return: The tag of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListVoiceTrainingJobRequest.

        任务标签。

        :param tag: The tag of this ListVoiceTrainingJobRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def job_type(self):
        r"""Gets the job_type of this ListVoiceTrainingJobRequest.

        训练类型。 * BASIC: 基础版(20句话) * MIDDLE: 进阶版(100句话) * ADVANCE: 高级版 * THIRD_PARTY: 第三方出门问问训练版 * THIRD_PARTY_LJZN: 第三方逻辑智能训练版 * FLEXUS: Flexus版---用的是大模型特征提取

        :return: The job_type of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListVoiceTrainingJobRequest.

        训练类型。 * BASIC: 基础版(20句话) * MIDDLE: 进阶版(100句话) * ADVANCE: 高级版 * THIRD_PARTY: 第三方出门问问训练版 * THIRD_PARTY_LJZN: 第三方逻辑智能训练版 * FLEXUS: Flexus版---用的是大模型特征提取

        :param job_type: The job_type of this ListVoiceTrainingJobRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def batch_name(self):
        r"""Gets the batch_name of this ListVoiceTrainingJobRequest.

        批次名称。

        :return: The batch_name of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        r"""Sets the batch_name of this ListVoiceTrainingJobRequest.

        批次名称。

        :param batch_name: The batch_name of this ListVoiceTrainingJobRequest.
        :type batch_name: str
        """
        self._batch_name = batch_name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListVoiceTrainingJobRequest.

        排序字段，当前支持：ceate_time/update_time

        :return: The sort_key of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListVoiceTrainingJobRequest.

        排序字段，当前支持：ceate_time/update_time

        :param sort_key: The sort_key of this ListVoiceTrainingJobRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListVoiceTrainingJobRequest.

        排序规则：desc(降序)/asc(升序)

        :return: The sort_dir of this ListVoiceTrainingJobRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListVoiceTrainingJobRequest.

        排序规则：desc(降序)/asc(升序)

        :param sort_dir: The sort_dir of this ListVoiceTrainingJobRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def is_ondemand_resource(self):
        r"""Gets the is_ondemand_resource of this ListVoiceTrainingJobRequest.

        是否是按需任务

        :return: The is_ondemand_resource of this ListVoiceTrainingJobRequest.
        :rtype: bool
        """
        return self._is_ondemand_resource

    @is_ondemand_resource.setter
    def is_ondemand_resource(self, is_ondemand_resource):
        r"""Sets the is_ondemand_resource of this ListVoiceTrainingJobRequest.

        是否是按需任务

        :param is_ondemand_resource: The is_ondemand_resource of this ListVoiceTrainingJobRequest.
        :type is_ondemand_resource: bool
        """
        self._is_ondemand_resource = is_ondemand_resource

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
        if not isinstance(other, ListVoiceTrainingJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
