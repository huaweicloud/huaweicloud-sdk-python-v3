# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkJobResponse(SdkResponse):

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
        'feature': 'str',
        'spark_version': 'str'
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
        'feature': 'feature',
        'spark_version': 'spark_version'
    }

    def __init__(self, id=None, state=None, app_id=None, log=None, sc_type=None, cluster_name=None, create_time=None, name=None, owner=None, proxy_user=None, kind=None, queue=None, image=None, req_body=None, update_time=None, feature=None, spark_version=None):
        r"""ShowSparkJobResponse

        The model defined in huaweicloud sdk

        :param id: 参数解释:  Batch作业的id 示例: 80ceaaff-3cfc-4162-a56f-70031ea4fa91 约束限制:  无 取值范围: 无 默认取值: 无
        :type id: str
        :param state: 参数解释:  Batch作业的状态 示例: starting 约束限制:  无 取值范围: starting：正在启动 running：正在执行任务 dead：session已退出 success：session停止成功 recovering：正在恢复 默认取值: 无
        :type state: str
        :param app_id: 参数解释:  批处理作业的后台app id 示例: batch-session-83ce2d53-8ae4-4afa-a0e2-e71a7aaa015c:30663 约束限制:  无 取值范围: 无 默认取值: 无
        :type app_id: str
        :param log: 参数解释:  显示当前Batch作业的最后10条记录 约束限制:  无 取值范围: 无 默认取值: 无
        :type log: list[str]
        :param sc_type: 参数解释:   计算资源类型。用户自定义时返回CUSTOMIZED 示例: CUSTOMIZED 约束限制:  无 取值范围: 无 默认取值: 无
        :type sc_type: str
        :param cluster_name: 参数解释:   批处理作业所在队列 示例: test 约束限制:  无 取值范围: 无 默认取值: 无
        :type cluster_name: str
        :param create_time: 参数解释:   Batch的创建时间。是单位为“毫秒”的时间戳 示例: 1747169026784 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type create_time: int
        :param name: 参数解释:   创建时用户指定的批处理名称，不能超过128个字符 示例: testsparksdhd_smn 约束限制:  不超过128个字符的字符串 取值范围: 无 默认取值: 无
        :type name: str
        :param owner: 参数解释:   批处理作业所属用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无
        :type owner: str
        :param proxy_user: 参数解释:   批处理作业所属代理用户（资源租户） 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无
        :type proxy_user: str
        :param kind: 参数解释:   批处理作业类型，只支持spark类型参数 示例: spark 约束限制:  无 取值范围: spark 默认取值: 无
        :type kind: str
        :param queue: 参数解释:   用于指定队列，填写已创建DLI的队列名 示例: genzy_520 约束限制:  无 取值范围: 无 默认取值: 无
        :type queue: str
        :param image: 参数解释:   自定义镜像。格式为：组织名/镜像名:镜像版本 示例: dli/spark:2.4.8 约束限制:  格式为：组织名/镜像名:镜像版本的字符串 取值范围: 无 默认取值: 无
        :type image: str
        :param req_body: 参数解释:   请求参数详情 示例: {\\\&quot;jars\\\&quot;:[],\\\&quot;pyFiles\\\&quot;:[],\\\&quot;files\\\&quot;:[],\\\&quot;modelFiles\\\&quot;:[],\\\&quot;resources\\\&quot;:[],\\\&quot;modules\\\&quot;:[],\\\&quot;groups\\\&quot;:[],\\\&quot;archives\\\&quot;:[],\\\&quot;queue\\\&quot;:\\\&quot;general_0509\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;testsparkjar43535\\\&quot;,\\\&quot;conf\\\&quot;:{},\\\&quot;execution_agency_urn\\\&quot;:\\\&quot;agency\\\&quot;,\\\&quot;file\\\&quot;:\\\&quot;obs://qinzhuo/spark-examples_2.11-2.1.0.luxor.jar\\\&quot;,\\\&quot;args\\\&quot;:[],\\\&quot;className\\\&quot;:\\\&quot;org.apache.spark.examples.SparkPi\\\&quot;,\\\&quot;autoRecovery\\\&quot;:false,\\\&quot;minRecoveryDelayTime\\\&quot;:10000,\\\&quot;maxRetryTimes\\\&quot;:20,\\\&quot;obs_bucket\\\&quot;:\\\&quot;rain3\\\&quot;,\\\&quot;feature\\\&quot;:\\\&quot;basic\\\&quot;,\\\&quot;spark_version\\\&quot;:\\\&quot;3.3.1\\\&quot;} 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无
        :type req_body: str
        :param update_time: 参数解释:   更新时间 示例: 1747362066342 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type update_time: int
        :param feature: 参数解释:  作业特性。表示用户作业使用的Spark镜像类型。 示例: basic 约束限制:  无 取值范围: basic：表示使用DLI提供的基础Spark镜像 custom：表示使用用户自定义的Spark镜像 ai：表示使用DLI提供的AI镜像 默认取值: 无
        :type feature: str
        :param spark_version: 参数解释:  作业使用spark组件的版本号，在“feature”为“basic”或“ai”时填写，若不填写，则使用默认的spark组件版本号2.3.2 示例: 2.3.2 约束限制:  无 取值范围: 无 默认取值: 2.3.2
        :type spark_version: str
        """
        
        super(ShowSparkJobResponse, self).__init__()

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
        self._feature = None
        self._spark_version = None
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
        if feature is not None:
            self.feature = feature
        if spark_version is not None:
            self.spark_version = spark_version

    @property
    def id(self):
        r"""Gets the id of this ShowSparkJobResponse.

        参数解释:  Batch作业的id 示例: 80ceaaff-3cfc-4162-a56f-70031ea4fa91 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The id of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSparkJobResponse.

        参数解释:  Batch作业的id 示例: 80ceaaff-3cfc-4162-a56f-70031ea4fa91 约束限制:  无 取值范围: 无 默认取值: 无

        :param id: The id of this ShowSparkJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        r"""Gets the state of this ShowSparkJobResponse.

        参数解释:  Batch作业的状态 示例: starting 约束限制:  无 取值范围: starting：正在启动 running：正在执行任务 dead：session已退出 success：session停止成功 recovering：正在恢复 默认取值: 无

        :return: The state of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowSparkJobResponse.

        参数解释:  Batch作业的状态 示例: starting 约束限制:  无 取值范围: starting：正在启动 running：正在执行任务 dead：session已退出 success：session停止成功 recovering：正在恢复 默认取值: 无

        :param state: The state of this ShowSparkJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowSparkJobResponse.

        参数解释:  批处理作业的后台app id 示例: batch-session-83ce2d53-8ae4-4afa-a0e2-e71a7aaa015c:30663 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The app_id of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowSparkJobResponse.

        参数解释:  批处理作业的后台app id 示例: batch-session-83ce2d53-8ae4-4afa-a0e2-e71a7aaa015c:30663 约束限制:  无 取值范围: 无 默认取值: 无

        :param app_id: The app_id of this ShowSparkJobResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def log(self):
        r"""Gets the log of this ShowSparkJobResponse.

        参数解释:  显示当前Batch作业的最后10条记录 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The log of this ShowSparkJobResponse.
        :rtype: list[str]
        """
        return self._log

    @log.setter
    def log(self, log):
        r"""Sets the log of this ShowSparkJobResponse.

        参数解释:  显示当前Batch作业的最后10条记录 约束限制:  无 取值范围: 无 默认取值: 无

        :param log: The log of this ShowSparkJobResponse.
        :type log: list[str]
        """
        self._log = log

    @property
    def sc_type(self):
        r"""Gets the sc_type of this ShowSparkJobResponse.

        参数解释:   计算资源类型。用户自定义时返回CUSTOMIZED 示例: CUSTOMIZED 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The sc_type of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._sc_type

    @sc_type.setter
    def sc_type(self, sc_type):
        r"""Sets the sc_type of this ShowSparkJobResponse.

        参数解释:   计算资源类型。用户自定义时返回CUSTOMIZED 示例: CUSTOMIZED 约束限制:  无 取值范围: 无 默认取值: 无

        :param sc_type: The sc_type of this ShowSparkJobResponse.
        :type sc_type: str
        """
        self._sc_type = sc_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ShowSparkJobResponse.

        参数解释:   批处理作业所在队列 示例: test 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The cluster_name of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ShowSparkJobResponse.

        参数解释:   批处理作业所在队列 示例: test 约束限制:  无 取值范围: 无 默认取值: 无

        :param cluster_name: The cluster_name of this ShowSparkJobResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowSparkJobResponse.

        参数解释:   Batch的创建时间。是单位为“毫秒”的时间戳 示例: 1747169026784 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The create_time of this ShowSparkJobResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowSparkJobResponse.

        参数解释:   Batch的创建时间。是单位为“毫秒”的时间戳 示例: 1747169026784 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param create_time: The create_time of this ShowSparkJobResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this ShowSparkJobResponse.

        参数解释:   创建时用户指定的批处理名称，不能超过128个字符 示例: testsparksdhd_smn 约束限制:  不超过128个字符的字符串 取值范围: 无 默认取值: 无

        :return: The name of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowSparkJobResponse.

        参数解释:   创建时用户指定的批处理名称，不能超过128个字符 示例: testsparksdhd_smn 约束限制:  不超过128个字符的字符串 取值范围: 无 默认取值: 无

        :param name: The name of this ShowSparkJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        r"""Gets the owner of this ShowSparkJobResponse.

        参数解释:   批处理作业所属用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The owner of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ShowSparkJobResponse.

        参数解释:   批处理作业所属用户 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

        :param owner: The owner of this ShowSparkJobResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def proxy_user(self):
        r"""Gets the proxy_user of this ShowSparkJobResponse.

        参数解释:   批处理作业所属代理用户（资源租户） 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The proxy_user of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._proxy_user

    @proxy_user.setter
    def proxy_user(self, proxy_user):
        r"""Sets the proxy_user of this ShowSparkJobResponse.

        参数解释:   批处理作业所属代理用户（资源租户） 示例: tenant1 约束限制:  无 取值范围: 无 默认取值: 无

        :param proxy_user: The proxy_user of this ShowSparkJobResponse.
        :type proxy_user: str
        """
        self._proxy_user = proxy_user

    @property
    def kind(self):
        r"""Gets the kind of this ShowSparkJobResponse.

        参数解释:   批处理作业类型，只支持spark类型参数 示例: spark 约束限制:  无 取值范围: spark 默认取值: 无

        :return: The kind of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ShowSparkJobResponse.

        参数解释:   批处理作业类型，只支持spark类型参数 示例: spark 约束限制:  无 取值范围: spark 默认取值: 无

        :param kind: The kind of this ShowSparkJobResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def queue(self):
        r"""Gets the queue of this ShowSparkJobResponse.

        参数解释:   用于指定队列，填写已创建DLI的队列名 示例: genzy_520 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The queue of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this ShowSparkJobResponse.

        参数解释:   用于指定队列，填写已创建DLI的队列名 示例: genzy_520 约束限制:  无 取值范围: 无 默认取值: 无

        :param queue: The queue of this ShowSparkJobResponse.
        :type queue: str
        """
        self._queue = queue

    @property
    def image(self):
        r"""Gets the image of this ShowSparkJobResponse.

        参数解释:   自定义镜像。格式为：组织名/镜像名:镜像版本 示例: dli/spark:2.4.8 约束限制:  格式为：组织名/镜像名:镜像版本的字符串 取值范围: 无 默认取值: 无

        :return: The image of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this ShowSparkJobResponse.

        参数解释:   自定义镜像。格式为：组织名/镜像名:镜像版本 示例: dli/spark:2.4.8 约束限制:  格式为：组织名/镜像名:镜像版本的字符串 取值范围: 无 默认取值: 无

        :param image: The image of this ShowSparkJobResponse.
        :type image: str
        """
        self._image = image

    @property
    def req_body(self):
        r"""Gets the req_body of this ShowSparkJobResponse.

        参数解释:   请求参数详情 示例: {\\\"jars\\\":[],\\\"pyFiles\\\":[],\\\"files\\\":[],\\\"modelFiles\\\":[],\\\"resources\\\":[],\\\"modules\\\":[],\\\"groups\\\":[],\\\"archives\\\":[],\\\"queue\\\":\\\"general_0509\\\",\\\"name\\\":\\\"testsparkjar43535\\\",\\\"conf\\\":{},\\\"execution_agency_urn\\\":\\\"agency\\\",\\\"file\\\":\\\"obs://qinzhuo/spark-examples_2.11-2.1.0.luxor.jar\\\",\\\"args\\\":[],\\\"className\\\":\\\"org.apache.spark.examples.SparkPi\\\",\\\"autoRecovery\\\":false,\\\"minRecoveryDelayTime\\\":10000,\\\"maxRetryTimes\\\":20,\\\"obs_bucket\\\":\\\"rain3\\\",\\\"feature\\\":\\\"basic\\\",\\\"spark_version\\\":\\\"3.3.1\\\"} 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无

        :return: The req_body of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._req_body

    @req_body.setter
    def req_body(self, req_body):
        r"""Sets the req_body of this ShowSparkJobResponse.

        参数解释:   请求参数详情 示例: {\\\"jars\\\":[],\\\"pyFiles\\\":[],\\\"files\\\":[],\\\"modelFiles\\\":[],\\\"resources\\\":[],\\\"modules\\\":[],\\\"groups\\\":[],\\\"archives\\\":[],\\\"queue\\\":\\\"general_0509\\\",\\\"name\\\":\\\"testsparkjar43535\\\",\\\"conf\\\":{},\\\"execution_agency_urn\\\":\\\"agency\\\",\\\"file\\\":\\\"obs://qinzhuo/spark-examples_2.11-2.1.0.luxor.jar\\\",\\\"args\\\":[],\\\"className\\\":\\\"org.apache.spark.examples.SparkPi\\\",\\\"autoRecovery\\\":false,\\\"minRecoveryDelayTime\\\":10000,\\\"maxRetryTimes\\\":20,\\\"obs_bucket\\\":\\\"rain3\\\",\\\"feature\\\":\\\"basic\\\",\\\"spark_version\\\":\\\"3.3.1\\\"} 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无

        :param req_body: The req_body of this ShowSparkJobResponse.
        :type req_body: str
        """
        self._req_body = req_body

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowSparkJobResponse.

        参数解释:   更新时间 示例: 1747362066342 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The update_time of this ShowSparkJobResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowSparkJobResponse.

        参数解释:   更新时间 示例: 1747362066342 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param update_time: The update_time of this ShowSparkJobResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def feature(self):
        r"""Gets the feature of this ShowSparkJobResponse.

        参数解释:  作业特性。表示用户作业使用的Spark镜像类型。 示例: basic 约束限制:  无 取值范围: basic：表示使用DLI提供的基础Spark镜像 custom：表示使用用户自定义的Spark镜像 ai：表示使用DLI提供的AI镜像 默认取值: 无

        :return: The feature of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this ShowSparkJobResponse.

        参数解释:  作业特性。表示用户作业使用的Spark镜像类型。 示例: basic 约束限制:  无 取值范围: basic：表示使用DLI提供的基础Spark镜像 custom：表示使用用户自定义的Spark镜像 ai：表示使用DLI提供的AI镜像 默认取值: 无

        :param feature: The feature of this ShowSparkJobResponse.
        :type feature: str
        """
        self._feature = feature

    @property
    def spark_version(self):
        r"""Gets the spark_version of this ShowSparkJobResponse.

        参数解释:  作业使用spark组件的版本号，在“feature”为“basic”或“ai”时填写，若不填写，则使用默认的spark组件版本号2.3.2 示例: 2.3.2 约束限制:  无 取值范围: 无 默认取值: 2.3.2

        :return: The spark_version of this ShowSparkJobResponse.
        :rtype: str
        """
        return self._spark_version

    @spark_version.setter
    def spark_version(self, spark_version):
        r"""Sets the spark_version of this ShowSparkJobResponse.

        参数解释:  作业使用spark组件的版本号，在“feature”为“basic”或“ai”时填写，若不填写，则使用默认的spark组件版本号2.3.2 示例: 2.3.2 约束限制:  无 取值范围: 无 默认取值: 2.3.2

        :param spark_version: The spark_version of this ShowSparkJobResponse.
        :type spark_version: str
        """
        self._spark_version = spark_version

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
        if not isinstance(other, ShowSparkJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
