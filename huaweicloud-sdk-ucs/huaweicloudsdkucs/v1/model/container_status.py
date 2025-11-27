# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'state': 'object',
        'last_state': 'str',
        'ready': 'bool',
        'restart_count': 'int',
        'image': 'str',
        'image_id': 'str',
        'started': 'str'
    }

    attribute_map = {
        'name': 'name',
        'state': 'state',
        'last_state': 'lastState',
        'ready': 'ready',
        'restart_count': 'restartCount',
        'image': 'image',
        'image_id': 'imageID',
        'started': 'started'
    }

    def __init__(self, name=None, state=None, last_state=None, ready=None, restart_count=None, image=None, image_id=None, started=None):
        r"""ContainerStatus

        The model defined in huaweicloud sdk

        :param name: 容器的唯一名称
        :type name: str
        :param state: 当前容器状态
        :type state: object
        :param last_state: 上次终止时的状态
        :type last_state: str
        :param ready: 容器是否通过就绪检查
        :type ready: bool
        :param restart_count: 容器重启次数
        :type restart_count: int
        :param image: 容器运行的镜像名称
        :type image: str
        :param image_id: 容器运行的镜像ID
        :type image_id: str
        :param started: 容器是否已经成功启动并进入稳定运行阶段
        :type started: str
        """
        
        

        self._name = None
        self._state = None
        self._last_state = None
        self._ready = None
        self._restart_count = None
        self._image = None
        self._image_id = None
        self._started = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if last_state is not None:
            self.last_state = last_state
        if ready is not None:
            self.ready = ready
        if restart_count is not None:
            self.restart_count = restart_count
        if image is not None:
            self.image = image
        if image_id is not None:
            self.image_id = image_id
        if started is not None:
            self.started = started

    @property
    def name(self):
        r"""Gets the name of this ContainerStatus.

        容器的唯一名称

        :return: The name of this ContainerStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ContainerStatus.

        容器的唯一名称

        :param name: The name of this ContainerStatus.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        r"""Gets the state of this ContainerStatus.

        当前容器状态

        :return: The state of this ContainerStatus.
        :rtype: object
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ContainerStatus.

        当前容器状态

        :param state: The state of this ContainerStatus.
        :type state: object
        """
        self._state = state

    @property
    def last_state(self):
        r"""Gets the last_state of this ContainerStatus.

        上次终止时的状态

        :return: The last_state of this ContainerStatus.
        :rtype: str
        """
        return self._last_state

    @last_state.setter
    def last_state(self, last_state):
        r"""Sets the last_state of this ContainerStatus.

        上次终止时的状态

        :param last_state: The last_state of this ContainerStatus.
        :type last_state: str
        """
        self._last_state = last_state

    @property
    def ready(self):
        r"""Gets the ready of this ContainerStatus.

        容器是否通过就绪检查

        :return: The ready of this ContainerStatus.
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        r"""Sets the ready of this ContainerStatus.

        容器是否通过就绪检查

        :param ready: The ready of this ContainerStatus.
        :type ready: bool
        """
        self._ready = ready

    @property
    def restart_count(self):
        r"""Gets the restart_count of this ContainerStatus.

        容器重启次数

        :return: The restart_count of this ContainerStatus.
        :rtype: int
        """
        return self._restart_count

    @restart_count.setter
    def restart_count(self, restart_count):
        r"""Sets the restart_count of this ContainerStatus.

        容器重启次数

        :param restart_count: The restart_count of this ContainerStatus.
        :type restart_count: int
        """
        self._restart_count = restart_count

    @property
    def image(self):
        r"""Gets the image of this ContainerStatus.

        容器运行的镜像名称

        :return: The image of this ContainerStatus.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this ContainerStatus.

        容器运行的镜像名称

        :param image: The image of this ContainerStatus.
        :type image: str
        """
        self._image = image

    @property
    def image_id(self):
        r"""Gets the image_id of this ContainerStatus.

        容器运行的镜像ID

        :return: The image_id of this ContainerStatus.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ContainerStatus.

        容器运行的镜像ID

        :param image_id: The image_id of this ContainerStatus.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def started(self):
        r"""Gets the started of this ContainerStatus.

        容器是否已经成功启动并进入稳定运行阶段

        :return: The started of this ContainerStatus.
        :rtype: str
        """
        return self._started

    @started.setter
    def started(self, started):
        r"""Sets the started of this ContainerStatus.

        容器是否已经成功启动并进入稳定运行阶段

        :param started: The started of this ContainerStatus.
        :type started: str
        """
        self._started = started

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
        if not isinstance(other, ContainerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
