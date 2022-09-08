# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBatchJobResponse(SdkResponse):

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
        """CreateBatchJobResponse

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
        :param duration: 作业运行时长，单位毫秒。
        :type duration: int
        """
        
        super(CreateBatchJobResponse, self).__init__()

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
        """Gets the id of this CreateBatchJobResponse.

        Batch作业的id。

        :return: The id of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateBatchJobResponse.

        Batch作业的id。

        :param id: The id of this CreateBatchJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        """Gets the state of this CreateBatchJobResponse.

        Batch作业的状态。包括： starting：正在启动；running：正在执行任务；dead：session已退出；success：session停止成功；recovering：正在恢复。

        :return: The state of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreateBatchJobResponse.

        Batch作业的状态。包括： starting：正在启动；running：正在执行任务；dead：session已退出；success：session停止成功；recovering：正在恢复。

        :param state: The state of this CreateBatchJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def app_id(self):
        """Gets the app_id of this CreateBatchJobResponse.

        Batch作业的后台app id。

        :return: The app_id of this CreateBatchJobResponse.
        :rtype: list[str]
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateBatchJobResponse.

        Batch作业的后台app id。

        :param app_id: The app_id of this CreateBatchJobResponse.
        :type app_id: list[str]
        """
        self._app_id = app_id

    @property
    def log(self):
        """Gets the log of this CreateBatchJobResponse.

        显示当前Batch作业的最后10条记录。

        :return: The log of this CreateBatchJobResponse.
        :rtype: list[str]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this CreateBatchJobResponse.

        显示当前Batch作业的最后10条记录。

        :param log: The log of this CreateBatchJobResponse.
        :type log: list[str]
        """
        self._log = log

    @property
    def sc_type(self):
        """Gets the sc_type of this CreateBatchJobResponse.

        计算资源类型。用户自定义时返回CUSTOMIZED。

        :return: The sc_type of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._sc_type

    @sc_type.setter
    def sc_type(self, sc_type):
        """Sets the sc_type of this CreateBatchJobResponse.

        计算资源类型。用户自定义时返回CUSTOMIZED。

        :param sc_type: The sc_type of this CreateBatchJobResponse.
        :type sc_type: str
        """
        self._sc_type = sc_type

    @property
    def cluster_name(self):
        """Gets the cluster_name of this CreateBatchJobResponse.

        会话所在队列。

        :return: The cluster_name of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this CreateBatchJobResponse.

        会话所在队列。

        :param cluster_name: The cluster_name of this CreateBatchJobResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def create_time(self):
        """Gets the create_time of this CreateBatchJobResponse.

        Batch的创建时间。是单位为“毫秒”的时间戳。

        :return: The create_time of this CreateBatchJobResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateBatchJobResponse.

        Batch的创建时间。是单位为“毫秒”的时间戳。

        :param create_time: The create_time of this CreateBatchJobResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def name(self):
        """Gets the name of this CreateBatchJobResponse.

        创建时用户指定的批处理名称，不能超过128个字符。

        :return: The name of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateBatchJobResponse.

        创建时用户指定的批处理名称，不能超过128个字符。

        :param name: The name of this CreateBatchJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this CreateBatchJobResponse.

        批处理作业所属用户

        :return: The owner of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CreateBatchJobResponse.

        批处理作业所属用户

        :param owner: The owner of this CreateBatchJobResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def proxy_user(self):
        """Gets the proxy_user of this CreateBatchJobResponse.

        批处理作业所属代理用户（资源租户）。

        :return: The proxy_user of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._proxy_user

    @proxy_user.setter
    def proxy_user(self, proxy_user):
        """Sets the proxy_user of this CreateBatchJobResponse.

        批处理作业所属代理用户（资源租户）。

        :param proxy_user: The proxy_user of this CreateBatchJobResponse.
        :type proxy_user: str
        """
        self._proxy_user = proxy_user

    @property
    def kind(self):
        """Gets the kind of this CreateBatchJobResponse.

        批处理作业类型，只支持spark类型参数。

        :return: The kind of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this CreateBatchJobResponse.

        批处理作业类型，只支持spark类型参数。

        :param kind: The kind of this CreateBatchJobResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def queue(self):
        """Gets the queue of this CreateBatchJobResponse.

        用于指定队列，填写已创建DLI的队列名

        :return: The queue of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this CreateBatchJobResponse.

        用于指定队列，填写已创建DLI的队列名

        :param queue: The queue of this CreateBatchJobResponse.
        :type queue: str
        """
        self._queue = queue

    @property
    def image(self):
        """Gets the image of this CreateBatchJobResponse.

        自定义镜像。格式为：组织名/镜像名:镜像版本。

        :return: The image of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CreateBatchJobResponse.

        自定义镜像。格式为：组织名/镜像名:镜像版本。

        :param image: The image of this CreateBatchJobResponse.
        :type image: str
        """
        self._image = image

    @property
    def update_time(self):
        """Gets the update_time of this CreateBatchJobResponse.

        更新时间

        :return: The update_time of this CreateBatchJobResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateBatchJobResponse.

        更新时间

        :param update_time: The update_time of this CreateBatchJobResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def duration(self):
        """Gets the duration of this CreateBatchJobResponse.

        作业运行时长，单位毫秒。

        :return: The duration of this CreateBatchJobResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this CreateBatchJobResponse.

        作业运行时长，单位毫秒。

        :param duration: The duration of this CreateBatchJobResponse.
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
        if not isinstance(other, CreateBatchJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
