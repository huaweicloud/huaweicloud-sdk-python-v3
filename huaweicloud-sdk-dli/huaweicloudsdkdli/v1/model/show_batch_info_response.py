# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBatchInfoResponse(SdkResponse):

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
        'app_id': 'list[str]',
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
        'update_time': 'update_time',
        'feature': 'feature',
        'spark_version': 'spark_version'
    }

    def __init__(self, id=None, state=None, app_id=None, log=None, sc_type=None, cluster_name=None, create_time=None, name=None, owner=None, proxy_user=None, kind=None, queue=None, image=None, update_time=None, feature=None, spark_version=None):
        """ShowBatchInfoResponse

        The model defined in huaweicloud sdk

        :param id: Batch作业的id。
        :type id: str
        :param state: Batch作业的状态。包括： starting：正在启动；running：正在执行任务；dead：session已退出；success：session停止成功；recovering：正在恢复。
        :type state: str
        :param app_id: Batch作业的后台app id。
        :type app_id: list[str]
        :param log: 显示当前Batch作业的最后10条记录。
        :type log: list[str]
        :param sc_type: 计算资源类型。用户自定义时返回CUSTOMIZED。
        :type sc_type: str
        :param cluster_name: 会话所在队列。
        :type cluster_name: str
        :param create_time: Batch的创建时间。是单位为“毫秒”的时间戳。
        :type create_time: int
        :param name: 创建时用户指定的批处理名称，不能超过128个字符。
        :type name: str
        :param owner: 批处理作业所属用户
        :type owner: str
        :param proxy_user: 批处理作业所属代理用户（资源租户）。
        :type proxy_user: str
        :param kind: 批处理作业类型，只支持spark类型参数。
        :type kind: str
        :param queue: 用于指定队列，填写已创建DLI的队列名
        :type queue: str
        :param image: 自定义镜像。格式为：组织名/镜像名:镜像版本。
        :type image: str
        :param update_time: 更新时间
        :type update_time: int
        :param feature: 作业特性。表示用户作业使用的Spark镜像类型。  basic：表示使用DLI提供的基础Spark镜像。 custom：表示使用用户自定义的Spark镜像。 ai：表示使用DLI提供的AI镜像。
        :type feature: str
        :param spark_version: 作业使用spark组件的版本号，在“feature”为“basic”或“ai”时填写，若不填写，则使用默认的spark组件版本号2.3.2。
        :type spark_version: str
        """
        
        super(ShowBatchInfoResponse, self).__init__()

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
        if update_time is not None:
            self.update_time = update_time
        if feature is not None:
            self.feature = feature
        if spark_version is not None:
            self.spark_version = spark_version

    @property
    def id(self):
        """Gets the id of this ShowBatchInfoResponse.

        Batch作业的id。

        :return: The id of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowBatchInfoResponse.

        Batch作业的id。

        :param id: The id of this ShowBatchInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        """Gets the state of this ShowBatchInfoResponse.

        Batch作业的状态。包括： starting：正在启动；running：正在执行任务；dead：session已退出；success：session停止成功；recovering：正在恢复。

        :return: The state of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowBatchInfoResponse.

        Batch作业的状态。包括： starting：正在启动；running：正在执行任务；dead：session已退出；success：session停止成功；recovering：正在恢复。

        :param state: The state of this ShowBatchInfoResponse.
        :type state: str
        """
        self._state = state

    @property
    def app_id(self):
        """Gets the app_id of this ShowBatchInfoResponse.

        Batch作业的后台app id。

        :return: The app_id of this ShowBatchInfoResponse.
        :rtype: list[str]
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowBatchInfoResponse.

        Batch作业的后台app id。

        :param app_id: The app_id of this ShowBatchInfoResponse.
        :type app_id: list[str]
        """
        self._app_id = app_id

    @property
    def log(self):
        """Gets the log of this ShowBatchInfoResponse.

        显示当前Batch作业的最后10条记录。

        :return: The log of this ShowBatchInfoResponse.
        :rtype: list[str]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this ShowBatchInfoResponse.

        显示当前Batch作业的最后10条记录。

        :param log: The log of this ShowBatchInfoResponse.
        :type log: list[str]
        """
        self._log = log

    @property
    def sc_type(self):
        """Gets the sc_type of this ShowBatchInfoResponse.

        计算资源类型。用户自定义时返回CUSTOMIZED。

        :return: The sc_type of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._sc_type

    @sc_type.setter
    def sc_type(self, sc_type):
        """Sets the sc_type of this ShowBatchInfoResponse.

        计算资源类型。用户自定义时返回CUSTOMIZED。

        :param sc_type: The sc_type of this ShowBatchInfoResponse.
        :type sc_type: str
        """
        self._sc_type = sc_type

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ShowBatchInfoResponse.

        会话所在队列。

        :return: The cluster_name of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ShowBatchInfoResponse.

        会话所在队列。

        :param cluster_name: The cluster_name of this ShowBatchInfoResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def create_time(self):
        """Gets the create_time of this ShowBatchInfoResponse.

        Batch的创建时间。是单位为“毫秒”的时间戳。

        :return: The create_time of this ShowBatchInfoResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowBatchInfoResponse.

        Batch的创建时间。是单位为“毫秒”的时间戳。

        :param create_time: The create_time of this ShowBatchInfoResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def name(self):
        """Gets the name of this ShowBatchInfoResponse.

        创建时用户指定的批处理名称，不能超过128个字符。

        :return: The name of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowBatchInfoResponse.

        创建时用户指定的批处理名称，不能超过128个字符。

        :param name: The name of this ShowBatchInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this ShowBatchInfoResponse.

        批处理作业所属用户

        :return: The owner of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ShowBatchInfoResponse.

        批处理作业所属用户

        :param owner: The owner of this ShowBatchInfoResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def proxy_user(self):
        """Gets the proxy_user of this ShowBatchInfoResponse.

        批处理作业所属代理用户（资源租户）。

        :return: The proxy_user of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._proxy_user

    @proxy_user.setter
    def proxy_user(self, proxy_user):
        """Sets the proxy_user of this ShowBatchInfoResponse.

        批处理作业所属代理用户（资源租户）。

        :param proxy_user: The proxy_user of this ShowBatchInfoResponse.
        :type proxy_user: str
        """
        self._proxy_user = proxy_user

    @property
    def kind(self):
        """Gets the kind of this ShowBatchInfoResponse.

        批处理作业类型，只支持spark类型参数。

        :return: The kind of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ShowBatchInfoResponse.

        批处理作业类型，只支持spark类型参数。

        :param kind: The kind of this ShowBatchInfoResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def queue(self):
        """Gets the queue of this ShowBatchInfoResponse.

        用于指定队列，填写已创建DLI的队列名

        :return: The queue of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this ShowBatchInfoResponse.

        用于指定队列，填写已创建DLI的队列名

        :param queue: The queue of this ShowBatchInfoResponse.
        :type queue: str
        """
        self._queue = queue

    @property
    def image(self):
        """Gets the image of this ShowBatchInfoResponse.

        自定义镜像。格式为：组织名/镜像名:镜像版本。

        :return: The image of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ShowBatchInfoResponse.

        自定义镜像。格式为：组织名/镜像名:镜像版本。

        :param image: The image of this ShowBatchInfoResponse.
        :type image: str
        """
        self._image = image

    @property
    def update_time(self):
        """Gets the update_time of this ShowBatchInfoResponse.

        更新时间

        :return: The update_time of this ShowBatchInfoResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowBatchInfoResponse.

        更新时间

        :param update_time: The update_time of this ShowBatchInfoResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def feature(self):
        """Gets the feature of this ShowBatchInfoResponse.

        作业特性。表示用户作业使用的Spark镜像类型。  basic：表示使用DLI提供的基础Spark镜像。 custom：表示使用用户自定义的Spark镜像。 ai：表示使用DLI提供的AI镜像。

        :return: The feature of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this ShowBatchInfoResponse.

        作业特性。表示用户作业使用的Spark镜像类型。  basic：表示使用DLI提供的基础Spark镜像。 custom：表示使用用户自定义的Spark镜像。 ai：表示使用DLI提供的AI镜像。

        :param feature: The feature of this ShowBatchInfoResponse.
        :type feature: str
        """
        self._feature = feature

    @property
    def spark_version(self):
        """Gets the spark_version of this ShowBatchInfoResponse.

        作业使用spark组件的版本号，在“feature”为“basic”或“ai”时填写，若不填写，则使用默认的spark组件版本号2.3.2。

        :return: The spark_version of this ShowBatchInfoResponse.
        :rtype: str
        """
        return self._spark_version

    @spark_version.setter
    def spark_version(self, spark_version):
        """Sets the spark_version of this ShowBatchInfoResponse.

        作业使用spark组件的版本号，在“feature”为“basic”或“ai”时填写，若不填写，则使用默认的spark组件版本号2.3.2。

        :param spark_version: The spark_version of this ShowBatchInfoResponse.
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
        if not isinstance(other, ShowBatchInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
