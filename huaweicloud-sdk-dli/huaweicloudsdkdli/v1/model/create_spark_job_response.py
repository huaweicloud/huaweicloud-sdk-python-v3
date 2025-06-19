# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSparkJobResponse(SdkResponse):

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
        'state': 'str',
        'app_id': 'str',
        'log': 'list[str]',
        'sc_type': 'str',
        'cluster_name': 'str',
        'create_time': 'int',
        'name': 'str',
        'owner': 'str',
        'proxy_user': 'str',
        'kind': 'str',
        'queue': 'str',
        'image': 'str',
        'update_time': 'int',
        'duration': 'int'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'app_id': 'appId',
        'log': 'log',
        'sc_type': 'sc_type',
        'cluster_name': 'cluster_name',
        'create_time': 'create_time',
        'name': 'name',
        'owner': 'owner',
        'proxy_user': 'proxyUser',
        'kind': 'kind',
        'queue': 'queue',
        'image': 'image',
        'update_time': 'update_time',
        'duration': 'duration'
    }

    def __init__(self, id=None, state=None, app_id=None, log=None, sc_type=None, cluster_name=None, create_time=None, name=None, owner=None, proxy_user=None, kind=None, queue=None, image=None, update_time=None, duration=None):
        r"""CreateSparkJobResponse

        The model defined in huaweicloud sdk

        :param id: 参数解释:   Batch作业的id 示例: 80ceaaff-3cfc-4162-a56f-70031ea4fa91 约束限制:  无 取值范围: 无 默认取值: 无
        :type id: str
        :param state: 参数解释:   Batch作业的状态 示例: starting 约束限制:  无 取值范围: starting：正在启动 running：正在执行任务 dead：session已退出 success：session停止成功 recovering：正在恢复 默认取值: 无
        :type state: str
        :param app_id: 参数解释:   批处理作业的后台app id 示例: batch-session-ca2a4042-0db9-45ab-bc7f-ae6a56846348:30671 约束限制:  无 取值范围: 无 默认取值: 无
        :type app_id: str
        :param log: 参数解释:   显示当前Batch作业的最后10条记录 约束限制:  无 取值范围: 无 默认取值: 无
        :type log: list[str]
        :param sc_type: 参数解释: 计算资源类型，目前可接受参数A, B, C。如果不指定，则按最小类型创建。 示例: A 约束限制: 无 取值范围: A：物理资源：8核32G内存，driverCores：2；executorCores：1；driverMemory：7G；executorMemory：4G；numExecutor：6 B：16核64G内存,2,2,7G,8G,7 C：32核128G内存,4,2,15G,8G,14 默认取值: 无
        :type sc_type: str
        :param cluster_name: 参数解释:   会话所在队列 约束限制:  无 取值范围: 无 默认取值: 无
        :type cluster_name: str
        :param create_time: 参数解释:   Batch的创建时间。是单位为“毫秒”的时间戳 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type create_time: int
        :param name: 参数解释:   创建时用户指定的批处理名称，不能超过128个字符 示例: test_spark 约束限制:  不超过128个字符的字符串 取值范围: 无 默认取值: 无
        :type name: str
        :param owner: 参数解释:   批处理作业所属用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无
        :type owner: str
        :param proxy_user: 参数解释:  批处理作业所属代理用户（资源租户） 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无
        :type proxy_user: str
        :param kind: 参数解释:  批处理作业类型，只支持spark类型参数 示例: spark 约束限制:  无 取值范围: spark 默认取值: 无
        :type kind: str
        :param queue: 参数解释:  用于指定队列，填写已创建DLI的队列名 示例: gen0218 约束限制:  无 取值范围: 无 默认取值: 无
        :type queue: str
        :param image: 参数解释:  自定义镜像。格式为：组织名/镜像名:镜像版本 示例: ceshi/spark_general-x86_64:3.3.1-2.3.7.1720240718867424736954752.tensorflow 约束限制:  无 取值范围: 无 默认取值: 无
        :type image: str
        :param update_time: 参数解释:  批处理作业的更新时间。是单位为“毫秒”的时间戳 示例: 1739867779341 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type update_time: int
        :param duration: 参数解释:  作业运行时长，单位毫秒 示例: 213038 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type duration: int
        """
        
        super(CreateSparkJobResponse, self).__init__()

        self._id = None
        self._state = None
        self._app_id = None
        self._log = None
        self._sc_type = None
        self._cluster_name = None
        self._create_time = None
        self._name = None
        self._owner = None
        self._proxy_user = None
        self._kind = None
        self._queue = None
        self._image = None
        self._update_time = None
        self._duration = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if app_id is not None:
            self.app_id = app_id
        if log is not None:
            self.log = log
        if sc_type is not None:
            self.sc_type = sc_type
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if create_time is not None:
            self.create_time = create_time
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if proxy_user is not None:
            self.proxy_user = proxy_user
        if kind is not None:
            self.kind = kind
        if queue is not None:
            self.queue = queue
        if image is not None:
            self.image = image
        if update_time is not None:
            self.update_time = update_time
        if duration is not None:
            self.duration = duration

    @property
    def id(self):
        r"""Gets the id of this CreateSparkJobResponse.

        参数解释:   Batch作业的id 示例: 80ceaaff-3cfc-4162-a56f-70031ea4fa91 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The id of this CreateSparkJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateSparkJobResponse.

        参数解释:   Batch作业的id 示例: 80ceaaff-3cfc-4162-a56f-70031ea4fa91 约束限制:  无 取值范围: 无 默认取值: 无

        :param id: The id of this CreateSparkJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        r"""Gets the state of this CreateSparkJobResponse.

        参数解释:   Batch作业的状态 示例: starting 约束限制:  无 取值范围: starting：正在启动 running：正在执行任务 dead：session已退出 success：session停止成功 recovering：正在恢复 默认取值: 无

        :return: The state of this CreateSparkJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CreateSparkJobResponse.

        参数解释:   Batch作业的状态 示例: starting 约束限制:  无 取值范围: starting：正在启动 running：正在执行任务 dead：session已退出 success：session停止成功 recovering：正在恢复 默认取值: 无

        :param state: The state of this CreateSparkJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def app_id(self):
        r"""Gets the app_id of this CreateSparkJobResponse.

        参数解释:   批处理作业的后台app id 示例: batch-session-ca2a4042-0db9-45ab-bc7f-ae6a56846348:30671 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The app_id of this CreateSparkJobResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CreateSparkJobResponse.

        参数解释:   批处理作业的后台app id 示例: batch-session-ca2a4042-0db9-45ab-bc7f-ae6a56846348:30671 约束限制:  无 取值范围: 无 默认取值: 无

        :param app_id: The app_id of this CreateSparkJobResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def log(self):
        r"""Gets the log of this CreateSparkJobResponse.

        参数解释:   显示当前Batch作业的最后10条记录 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The log of this CreateSparkJobResponse.
        :rtype: list[str]
        """
        return self._log

    @log.setter
    def log(self, log):
        r"""Sets the log of this CreateSparkJobResponse.

        参数解释:   显示当前Batch作业的最后10条记录 约束限制:  无 取值范围: 无 默认取值: 无

        :param log: The log of this CreateSparkJobResponse.
        :type log: list[str]
        """
        self._log = log

    @property
    def sc_type(self):
        r"""Gets the sc_type of this CreateSparkJobResponse.

        参数解释: 计算资源类型，目前可接受参数A, B, C。如果不指定，则按最小类型创建。 示例: A 约束限制: 无 取值范围: A：物理资源：8核32G内存，driverCores：2；executorCores：1；driverMemory：7G；executorMemory：4G；numExecutor：6 B：16核64G内存,2,2,7G,8G,7 C：32核128G内存,4,2,15G,8G,14 默认取值: 无

        :return: The sc_type of this CreateSparkJobResponse.
        :rtype: str
        """
        return self._sc_type

    @sc_type.setter
    def sc_type(self, sc_type):
        r"""Sets the sc_type of this CreateSparkJobResponse.

        参数解释: 计算资源类型，目前可接受参数A, B, C。如果不指定，则按最小类型创建。 示例: A 约束限制: 无 取值范围: A：物理资源：8核32G内存，driverCores：2；executorCores：1；driverMemory：7G；executorMemory：4G；numExecutor：6 B：16核64G内存,2,2,7G,8G,7 C：32核128G内存,4,2,15G,8G,14 默认取值: 无

        :param sc_type: The sc_type of this CreateSparkJobResponse.
        :type sc_type: str
        """
        self._sc_type = sc_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CreateSparkJobResponse.

        参数解释:   会话所在队列 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The cluster_name of this CreateSparkJobResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CreateSparkJobResponse.

        参数解释:   会话所在队列 约束限制:  无 取值范围: 无 默认取值: 无

        :param cluster_name: The cluster_name of this CreateSparkJobResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateSparkJobResponse.

        参数解释:   Batch的创建时间。是单位为“毫秒”的时间戳 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The create_time of this CreateSparkJobResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateSparkJobResponse.

        参数解释:   Batch的创建时间。是单位为“毫秒”的时间戳 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param create_time: The create_time of this CreateSparkJobResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this CreateSparkJobResponse.

        参数解释:   创建时用户指定的批处理名称，不能超过128个字符 示例: test_spark 约束限制:  不超过128个字符的字符串 取值范围: 无 默认取值: 无

        :return: The name of this CreateSparkJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSparkJobResponse.

        参数解释:   创建时用户指定的批处理名称，不能超过128个字符 示例: test_spark 约束限制:  不超过128个字符的字符串 取值范围: 无 默认取值: 无

        :param name: The name of this CreateSparkJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        r"""Gets the owner of this CreateSparkJobResponse.

        参数解释:   批处理作业所属用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The owner of this CreateSparkJobResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this CreateSparkJobResponse.

        参数解释:   批处理作业所属用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

        :param owner: The owner of this CreateSparkJobResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def proxy_user(self):
        r"""Gets the proxy_user of this CreateSparkJobResponse.

        参数解释:  批处理作业所属代理用户（资源租户） 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The proxy_user of this CreateSparkJobResponse.
        :rtype: str
        """
        return self._proxy_user

    @proxy_user.setter
    def proxy_user(self, proxy_user):
        r"""Sets the proxy_user of this CreateSparkJobResponse.

        参数解释:  批处理作业所属代理用户（资源租户） 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无

        :param proxy_user: The proxy_user of this CreateSparkJobResponse.
        :type proxy_user: str
        """
        self._proxy_user = proxy_user

    @property
    def kind(self):
        r"""Gets the kind of this CreateSparkJobResponse.

        参数解释:  批处理作业类型，只支持spark类型参数 示例: spark 约束限制:  无 取值范围: spark 默认取值: 无

        :return: The kind of this CreateSparkJobResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this CreateSparkJobResponse.

        参数解释:  批处理作业类型，只支持spark类型参数 示例: spark 约束限制:  无 取值范围: spark 默认取值: 无

        :param kind: The kind of this CreateSparkJobResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def queue(self):
        r"""Gets the queue of this CreateSparkJobResponse.

        参数解释:  用于指定队列，填写已创建DLI的队列名 示例: gen0218 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The queue of this CreateSparkJobResponse.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this CreateSparkJobResponse.

        参数解释:  用于指定队列，填写已创建DLI的队列名 示例: gen0218 约束限制:  无 取值范围: 无 默认取值: 无

        :param queue: The queue of this CreateSparkJobResponse.
        :type queue: str
        """
        self._queue = queue

    @property
    def image(self):
        r"""Gets the image of this CreateSparkJobResponse.

        参数解释:  自定义镜像。格式为：组织名/镜像名:镜像版本 示例: ceshi/spark_general-x86_64:3.3.1-2.3.7.1720240718867424736954752.tensorflow 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The image of this CreateSparkJobResponse.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this CreateSparkJobResponse.

        参数解释:  自定义镜像。格式为：组织名/镜像名:镜像版本 示例: ceshi/spark_general-x86_64:3.3.1-2.3.7.1720240718867424736954752.tensorflow 约束限制:  无 取值范围: 无 默认取值: 无

        :param image: The image of this CreateSparkJobResponse.
        :type image: str
        """
        self._image = image

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateSparkJobResponse.

        参数解释:  批处理作业的更新时间。是单位为“毫秒”的时间戳 示例: 1739867779341 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The update_time of this CreateSparkJobResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateSparkJobResponse.

        参数解释:  批处理作业的更新时间。是单位为“毫秒”的时间戳 示例: 1739867779341 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param update_time: The update_time of this CreateSparkJobResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def duration(self):
        r"""Gets the duration of this CreateSparkJobResponse.

        参数解释:  作业运行时长，单位毫秒 示例: 213038 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The duration of this CreateSparkJobResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this CreateSparkJobResponse.

        参数解释:  作业运行时长，单位毫秒 示例: 213038 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param duration: The duration of this CreateSparkJobResponse.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, CreateSparkJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
