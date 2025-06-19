# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkJob:

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
        'req_body': 'str',
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
        'req_body': 'req_body',
        'update_time': 'update_time',
        'duration': 'duration'
    }

    def __init__(self, id=None, state=None, app_id=None, log=None, sc_type=None, cluster_name=None, create_time=None, name=None, owner=None, proxy_user=None, kind=None, queue=None, image=None, req_body=None, update_time=None, duration=None):
        r"""SparkJob

        The model defined in huaweicloud sdk

        :param id: 参数解释:  Batch作业的id。 示例: 80ceaaff-3cfc-4162-a56f-70031ea4fa91 约束限制:  无 取值范围: 无 默认取值: 无
        :type id: str
        :param state: 参数解释:  Batch作业的状态 示例: starting 约束限制:  无 取值范围: starting：正在启动；running：正在执行任务；dead：session已退出；success：session停止成功；recovering：正在恢复 默认取值: 无
        :type state: str
        :param app_id: 参数解释:  批处理作业的后台app id 示例: batch-session-1f49b734-757a-419c-9519-7754520cb03c:31309 约束限制:  无 取值范围: 无 默认取值: 无
        :type app_id: str
        :param log: 参数解释:  显示当前Batch作业的最后10条记录 约束限制:  无 取值范围: 无 默认取值: 无
        :type log: list[str]
        :param sc_type: 参数解释:   计算资源类型，目前可接受参数A, B, C。如果不指定，则按最小类型创建。 示例: A 约束限制:  无 取值范围: A：物理资源：8核32G内存，driverCores：2；executorCores：1；driverMemory：7G；executorMemory：4G；numExecutor：6。 B：16核64G内存,2,2,7G,8G,7。 C：32核128G内存,4,2,15G,8G,14。 默认取值: 无
        :type sc_type: str
        :param cluster_name: 参数解释:  会话所在队列 示例: test 约束限制:  无 取值范围: 无 默认取值: 无
        :type cluster_name: str
        :param create_time: 参数解释:  Batch的创建时间。是单位为“毫秒”的时间戳 示例: 1747169165821 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type create_time: int
        :param name: 参数解释:  创建时用户指定的批处理名称，不能超过128个字符 示例: test_pyFiles 约束限制:  无 取值范围: 无 默认取值: 无
        :type name: str
        :param owner: 参数解释:  批处理作业所属用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无
        :type owner: str
        :param proxy_user: 参数解释:  批处理作业所属代理用户（资源租户） 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无
        :type proxy_user: str
        :param kind: 参数解释:   批处理作业类型，只支持spark类型参数 示例: spark 约束限制:  无 取值范围: spark 默认取值: 无
        :type kind: str
        :param queue: 参数解释:   用于指定队列，填写已创建DLI的队列名 示例: gen_native 约束限制:  无 取值范围: 无 默认取值: 无
        :type queue: str
        :param image: 参数解释:   自定义镜像。格式为：组织名/镜像名:镜像版本 示例: ceshi/spark_general-x86_64:3.3.1-2.3.8.1020240906885119450448000 约束限制:  格式为: 组织名/镜像名:镜像版本的字符串 取值范围: 无 默认取值: 无
        :type image: str
        :param req_body: 参数解释:   请求参数详情 示例: {\\\&quot;jars\\\&quot;:[\\\&quot;spark-examples_2.11-2.4.5-h0.cbu.dli.300.20240725.r1.jar\\\&quot;],\\\&quot;pyFiles\\\&quot;:[],\\\&quot;files\\\&quot;:[],\\\&quot;modelFiles\\\&quot;:[],\\\&quot;resources\\\&quot;:[],\\\&quot;modules\\\&quot;:[],\\\&quot;groups\\\&quot;:[],\\\&quot;archives\\\&quot;:[],\\\&quot;queue\\\&quot;:\\\&quot;gen0218\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;conf\\\&quot;:{},\\\&quot;execution_agency_urn\\\&quot;:\\\&quot;agency\\\&quot;,\\\&quot;file\\\&quot;:\\\&quot;obs://dli-wzy/package/job/spark/longrunning.py\\\&quot;,\\\&quot;args\\\&quot;:[],\\\&quot;className\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;autoRecovery\\\&quot;:false,\\\&quot;minRecoveryDelayTime\\\&quot;:10000,\\\&quot;maxRetryTimes\\\&quot;:20,\\\&quot;obs_bucket\\\&quot;:\\\&quot;rain3\\\&quot;,\\\&quot;image\\\&quot;:\\\&quot;ceshi/spark_general-x86_64:3.3.1-2.3.8.1020240906885119450448000\\\&quot;,\\\&quot;feature\\\&quot;:\\\&quot;custom\\\&quot;,\\\&quot;spark_version\\\&quot;:\\\&quot;3.3.1\\\&quot;} 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无
        :type req_body: str
        :param update_time: 参数解释:   更新时间 示例: 1739867996988 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type update_time: int
        :param duration: 参数解释:   作业运行时长，单位毫秒 示例: 141079 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type duration: int
        """
        
        

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
        self._req_body = None
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
        if req_body is not None:
            self.req_body = req_body
        if update_time is not None:
            self.update_time = update_time
        if duration is not None:
            self.duration = duration

    @property
    def id(self):
        r"""Gets the id of this SparkJob.

        参数解释:  Batch作业的id。 示例: 80ceaaff-3cfc-4162-a56f-70031ea4fa91 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The id of this SparkJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SparkJob.

        参数解释:  Batch作业的id。 示例: 80ceaaff-3cfc-4162-a56f-70031ea4fa91 约束限制:  无 取值范围: 无 默认取值: 无

        :param id: The id of this SparkJob.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        r"""Gets the state of this SparkJob.

        参数解释:  Batch作业的状态 示例: starting 约束限制:  无 取值范围: starting：正在启动；running：正在执行任务；dead：session已退出；success：session停止成功；recovering：正在恢复 默认取值: 无

        :return: The state of this SparkJob.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this SparkJob.

        参数解释:  Batch作业的状态 示例: starting 约束限制:  无 取值范围: starting：正在启动；running：正在执行任务；dead：session已退出；success：session停止成功；recovering：正在恢复 默认取值: 无

        :param state: The state of this SparkJob.
        :type state: str
        """
        self._state = state

    @property
    def app_id(self):
        r"""Gets the app_id of this SparkJob.

        参数解释:  批处理作业的后台app id 示例: batch-session-1f49b734-757a-419c-9519-7754520cb03c:31309 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The app_id of this SparkJob.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this SparkJob.

        参数解释:  批处理作业的后台app id 示例: batch-session-1f49b734-757a-419c-9519-7754520cb03c:31309 约束限制:  无 取值范围: 无 默认取值: 无

        :param app_id: The app_id of this SparkJob.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def log(self):
        r"""Gets the log of this SparkJob.

        参数解释:  显示当前Batch作业的最后10条记录 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The log of this SparkJob.
        :rtype: list[str]
        """
        return self._log

    @log.setter
    def log(self, log):
        r"""Sets the log of this SparkJob.

        参数解释:  显示当前Batch作业的最后10条记录 约束限制:  无 取值范围: 无 默认取值: 无

        :param log: The log of this SparkJob.
        :type log: list[str]
        """
        self._log = log

    @property
    def sc_type(self):
        r"""Gets the sc_type of this SparkJob.

        参数解释:   计算资源类型，目前可接受参数A, B, C。如果不指定，则按最小类型创建。 示例: A 约束限制:  无 取值范围: A：物理资源：8核32G内存，driverCores：2；executorCores：1；driverMemory：7G；executorMemory：4G；numExecutor：6。 B：16核64G内存,2,2,7G,8G,7。 C：32核128G内存,4,2,15G,8G,14。 默认取值: 无

        :return: The sc_type of this SparkJob.
        :rtype: str
        """
        return self._sc_type

    @sc_type.setter
    def sc_type(self, sc_type):
        r"""Sets the sc_type of this SparkJob.

        参数解释:   计算资源类型，目前可接受参数A, B, C。如果不指定，则按最小类型创建。 示例: A 约束限制:  无 取值范围: A：物理资源：8核32G内存，driverCores：2；executorCores：1；driverMemory：7G；executorMemory：4G；numExecutor：6。 B：16核64G内存,2,2,7G,8G,7。 C：32核128G内存,4,2,15G,8G,14。 默认取值: 无

        :param sc_type: The sc_type of this SparkJob.
        :type sc_type: str
        """
        self._sc_type = sc_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this SparkJob.

        参数解释:  会话所在队列 示例: test 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The cluster_name of this SparkJob.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this SparkJob.

        参数解释:  会话所在队列 示例: test 约束限制:  无 取值范围: 无 默认取值: 无

        :param cluster_name: The cluster_name of this SparkJob.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def create_time(self):
        r"""Gets the create_time of this SparkJob.

        参数解释:  Batch的创建时间。是单位为“毫秒”的时间戳 示例: 1747169165821 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The create_time of this SparkJob.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SparkJob.

        参数解释:  Batch的创建时间。是单位为“毫秒”的时间戳 示例: 1747169165821 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param create_time: The create_time of this SparkJob.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this SparkJob.

        参数解释:  创建时用户指定的批处理名称，不能超过128个字符 示例: test_pyFiles 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The name of this SparkJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SparkJob.

        参数解释:  创建时用户指定的批处理名称，不能超过128个字符 示例: test_pyFiles 约束限制:  无 取值范围: 无 默认取值: 无

        :param name: The name of this SparkJob.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        r"""Gets the owner of this SparkJob.

        参数解释:  批处理作业所属用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The owner of this SparkJob.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this SparkJob.

        参数解释:  批处理作业所属用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

        :param owner: The owner of this SparkJob.
        :type owner: str
        """
        self._owner = owner

    @property
    def proxy_user(self):
        r"""Gets the proxy_user of this SparkJob.

        参数解释:  批处理作业所属代理用户（资源租户） 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The proxy_user of this SparkJob.
        :rtype: str
        """
        return self._proxy_user

    @proxy_user.setter
    def proxy_user(self, proxy_user):
        r"""Sets the proxy_user of this SparkJob.

        参数解释:  批处理作业所属代理用户（资源租户） 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无

        :param proxy_user: The proxy_user of this SparkJob.
        :type proxy_user: str
        """
        self._proxy_user = proxy_user

    @property
    def kind(self):
        r"""Gets the kind of this SparkJob.

        参数解释:   批处理作业类型，只支持spark类型参数 示例: spark 约束限制:  无 取值范围: spark 默认取值: 无

        :return: The kind of this SparkJob.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this SparkJob.

        参数解释:   批处理作业类型，只支持spark类型参数 示例: spark 约束限制:  无 取值范围: spark 默认取值: 无

        :param kind: The kind of this SparkJob.
        :type kind: str
        """
        self._kind = kind

    @property
    def queue(self):
        r"""Gets the queue of this SparkJob.

        参数解释:   用于指定队列，填写已创建DLI的队列名 示例: gen_native 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The queue of this SparkJob.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this SparkJob.

        参数解释:   用于指定队列，填写已创建DLI的队列名 示例: gen_native 约束限制:  无 取值范围: 无 默认取值: 无

        :param queue: The queue of this SparkJob.
        :type queue: str
        """
        self._queue = queue

    @property
    def image(self):
        r"""Gets the image of this SparkJob.

        参数解释:   自定义镜像。格式为：组织名/镜像名:镜像版本 示例: ceshi/spark_general-x86_64:3.3.1-2.3.8.1020240906885119450448000 约束限制:  格式为: 组织名/镜像名:镜像版本的字符串 取值范围: 无 默认取值: 无

        :return: The image of this SparkJob.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this SparkJob.

        参数解释:   自定义镜像。格式为：组织名/镜像名:镜像版本 示例: ceshi/spark_general-x86_64:3.3.1-2.3.8.1020240906885119450448000 约束限制:  格式为: 组织名/镜像名:镜像版本的字符串 取值范围: 无 默认取值: 无

        :param image: The image of this SparkJob.
        :type image: str
        """
        self._image = image

    @property
    def req_body(self):
        r"""Gets the req_body of this SparkJob.

        参数解释:   请求参数详情 示例: {\\\"jars\\\":[\\\"spark-examples_2.11-2.4.5-h0.cbu.dli.300.20240725.r1.jar\\\"],\\\"pyFiles\\\":[],\\\"files\\\":[],\\\"modelFiles\\\":[],\\\"resources\\\":[],\\\"modules\\\":[],\\\"groups\\\":[],\\\"archives\\\":[],\\\"queue\\\":\\\"gen0218\\\",\\\"name\\\":\\\"\\\",\\\"conf\\\":{},\\\"execution_agency_urn\\\":\\\"agency\\\",\\\"file\\\":\\\"obs://dli-wzy/package/job/spark/longrunning.py\\\",\\\"args\\\":[],\\\"className\\\":\\\"\\\",\\\"autoRecovery\\\":false,\\\"minRecoveryDelayTime\\\":10000,\\\"maxRetryTimes\\\":20,\\\"obs_bucket\\\":\\\"rain3\\\",\\\"image\\\":\\\"ceshi/spark_general-x86_64:3.3.1-2.3.8.1020240906885119450448000\\\",\\\"feature\\\":\\\"custom\\\",\\\"spark_version\\\":\\\"3.3.1\\\"} 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无

        :return: The req_body of this SparkJob.
        :rtype: str
        """
        return self._req_body

    @req_body.setter
    def req_body(self, req_body):
        r"""Sets the req_body of this SparkJob.

        参数解释:   请求参数详情 示例: {\\\"jars\\\":[\\\"spark-examples_2.11-2.4.5-h0.cbu.dli.300.20240725.r1.jar\\\"],\\\"pyFiles\\\":[],\\\"files\\\":[],\\\"modelFiles\\\":[],\\\"resources\\\":[],\\\"modules\\\":[],\\\"groups\\\":[],\\\"archives\\\":[],\\\"queue\\\":\\\"gen0218\\\",\\\"name\\\":\\\"\\\",\\\"conf\\\":{},\\\"execution_agency_urn\\\":\\\"agency\\\",\\\"file\\\":\\\"obs://dli-wzy/package/job/spark/longrunning.py\\\",\\\"args\\\":[],\\\"className\\\":\\\"\\\",\\\"autoRecovery\\\":false,\\\"minRecoveryDelayTime\\\":10000,\\\"maxRetryTimes\\\":20,\\\"obs_bucket\\\":\\\"rain3\\\",\\\"image\\\":\\\"ceshi/spark_general-x86_64:3.3.1-2.3.8.1020240906885119450448000\\\",\\\"feature\\\":\\\"custom\\\",\\\"spark_version\\\":\\\"3.3.1\\\"} 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无

        :param req_body: The req_body of this SparkJob.
        :type req_body: str
        """
        self._req_body = req_body

    @property
    def update_time(self):
        r"""Gets the update_time of this SparkJob.

        参数解释:   更新时间 示例: 1739867996988 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The update_time of this SparkJob.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this SparkJob.

        参数解释:   更新时间 示例: 1739867996988 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param update_time: The update_time of this SparkJob.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def duration(self):
        r"""Gets the duration of this SparkJob.

        参数解释:   作业运行时长，单位毫秒 示例: 141079 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The duration of this SparkJob.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this SparkJob.

        参数解释:   作业运行时长，单位毫秒 示例: 141079 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param duration: The duration of this SparkJob.
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
        if not isinstance(other, SparkJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
