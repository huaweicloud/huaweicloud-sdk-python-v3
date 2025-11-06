# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventForensicInfoAutoLaunchForensic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event': 'int',
        'type': 'int',
        'owner': 'str',
        'name': 'str',
        'run_interval': 'str',
        'hash': 'str',
        'mtime': 'str',
        'description': 'str',
        'path': 'str'
    }

    attribute_map = {
        'event': 'event',
        'type': 'type',
        'owner': 'owner',
        'name': 'name',
        'run_interval': 'run_interval',
        'hash': 'hash',
        'mtime': 'mtime',
        'description': 'description',
        'path': 'path'
    }

    def __init__(self, event=None, type=None, owner=None, name=None, run_interval=None, hash=None, mtime=None, description=None, path=None):
        r"""EventForensicInfoAutoLaunchForensic

        The model defined in huaweicloud sdk

        :param event: **参数解释**： 事件 **取值范围**： 不涉及
        :type event: int
        :param type: **参数解释**： 类型 **取值范围**： 不涉及
        :type type: int
        :param owner: **参数解释**： 用户 **取值范围**： 不涉及
        :type owner: str
        :param name: **参数解释**： 命令 **取值范围**： 不涉及
        :type name: str
        :param run_interval: **参数解释**： 运行间隔 **取值范围**： 不涉及
        :type run_interval: str
        :param hash: **参数解释**： hash **取值范围**： 不涉及
        :type hash: str
        :param mtime: **参数解释**： hash **取值范围**： 不涉及
        :type mtime: str
        :param description: **参数解释**： 自启动项信息 **取值范围**： 不涉及
        :type description: str
        :param path: **参数解释**： 进程文件命令行 **取值范围**： 不涉及
        :type path: str
        """
        
        

        self._event = None
        self._type = None
        self._owner = None
        self._name = None
        self._run_interval = None
        self._hash = None
        self._mtime = None
        self._description = None
        self._path = None
        self.discriminator = None

        if event is not None:
            self.event = event
        if type is not None:
            self.type = type
        if owner is not None:
            self.owner = owner
        if name is not None:
            self.name = name
        if run_interval is not None:
            self.run_interval = run_interval
        if hash is not None:
            self.hash = hash
        if mtime is not None:
            self.mtime = mtime
        if description is not None:
            self.description = description
        if path is not None:
            self.path = path

    @property
    def event(self):
        r"""Gets the event of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 事件 **取值范围**： 不涉及

        :return: The event of this EventForensicInfoAutoLaunchForensic.
        :rtype: int
        """
        return self._event

    @event.setter
    def event(self, event):
        r"""Sets the event of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 事件 **取值范围**： 不涉及

        :param event: The event of this EventForensicInfoAutoLaunchForensic.
        :type event: int
        """
        self._event = event

    @property
    def type(self):
        r"""Gets the type of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 类型 **取值范围**： 不涉及

        :return: The type of this EventForensicInfoAutoLaunchForensic.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 类型 **取值范围**： 不涉及

        :param type: The type of this EventForensicInfoAutoLaunchForensic.
        :type type: int
        """
        self._type = type

    @property
    def owner(self):
        r"""Gets the owner of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 用户 **取值范围**： 不涉及

        :return: The owner of this EventForensicInfoAutoLaunchForensic.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 用户 **取值范围**： 不涉及

        :param owner: The owner of this EventForensicInfoAutoLaunchForensic.
        :type owner: str
        """
        self._owner = owner

    @property
    def name(self):
        r"""Gets the name of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 命令 **取值范围**： 不涉及

        :return: The name of this EventForensicInfoAutoLaunchForensic.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 命令 **取值范围**： 不涉及

        :param name: The name of this EventForensicInfoAutoLaunchForensic.
        :type name: str
        """
        self._name = name

    @property
    def run_interval(self):
        r"""Gets the run_interval of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 运行间隔 **取值范围**： 不涉及

        :return: The run_interval of this EventForensicInfoAutoLaunchForensic.
        :rtype: str
        """
        return self._run_interval

    @run_interval.setter
    def run_interval(self, run_interval):
        r"""Sets the run_interval of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 运行间隔 **取值范围**： 不涉及

        :param run_interval: The run_interval of this EventForensicInfoAutoLaunchForensic.
        :type run_interval: str
        """
        self._run_interval = run_interval

    @property
    def hash(self):
        r"""Gets the hash of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： hash **取值范围**： 不涉及

        :return: The hash of this EventForensicInfoAutoLaunchForensic.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： hash **取值范围**： 不涉及

        :param hash: The hash of this EventForensicInfoAutoLaunchForensic.
        :type hash: str
        """
        self._hash = hash

    @property
    def mtime(self):
        r"""Gets the mtime of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： hash **取值范围**： 不涉及

        :return: The mtime of this EventForensicInfoAutoLaunchForensic.
        :rtype: str
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        r"""Sets the mtime of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： hash **取值范围**： 不涉及

        :param mtime: The mtime of this EventForensicInfoAutoLaunchForensic.
        :type mtime: str
        """
        self._mtime = mtime

    @property
    def description(self):
        r"""Gets the description of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 自启动项信息 **取值范围**： 不涉及

        :return: The description of this EventForensicInfoAutoLaunchForensic.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 自启动项信息 **取值范围**： 不涉及

        :param description: The description of this EventForensicInfoAutoLaunchForensic.
        :type description: str
        """
        self._description = description

    @property
    def path(self):
        r"""Gets the path of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 进程文件命令行 **取值范围**： 不涉及

        :return: The path of this EventForensicInfoAutoLaunchForensic.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this EventForensicInfoAutoLaunchForensic.

        **参数解释**： 进程文件命令行 **取值范围**： 不涉及

        :param path: The path of this EventForensicInfoAutoLaunchForensic.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, EventForensicInfoAutoLaunchForensic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
