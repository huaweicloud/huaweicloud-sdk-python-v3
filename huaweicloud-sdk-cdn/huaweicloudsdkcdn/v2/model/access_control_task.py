# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessControlTask:

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
        'urls': 'list[str]',
        'status': 'str',
        'action': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'urls': 'urls',
        'status': 'status',
        'action': 'action',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, urls=None, status=None, action=None, create_time=None):
        r"""AccessControlTask

        The model defined in huaweicloud sdk

        :param id: 任务id。
        :type id: str
        :param urls: url列表。
        :type urls: list[str]
        :param status: 任务状态，状态类型：processing：处理中；succeed：完成；failed：失败。
        :type status: str
        :param action: 任务类型，unban：解禁任务；ban：封禁任务。
        :type action: str
        :param create_time: 创建时间戳（毫秒）。
        :type create_time: int
        """
        
        

        self._id = None
        self._urls = None
        self._status = None
        self._action = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if urls is not None:
            self.urls = urls
        if status is not None:
            self.status = status
        if action is not None:
            self.action = action
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this AccessControlTask.

        任务id。

        :return: The id of this AccessControlTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AccessControlTask.

        任务id。

        :param id: The id of this AccessControlTask.
        :type id: str
        """
        self._id = id

    @property
    def urls(self):
        r"""Gets the urls of this AccessControlTask.

        url列表。

        :return: The urls of this AccessControlTask.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        r"""Sets the urls of this AccessControlTask.

        url列表。

        :param urls: The urls of this AccessControlTask.
        :type urls: list[str]
        """
        self._urls = urls

    @property
    def status(self):
        r"""Gets the status of this AccessControlTask.

        任务状态，状态类型：processing：处理中；succeed：完成；failed：失败。

        :return: The status of this AccessControlTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AccessControlTask.

        任务状态，状态类型：processing：处理中；succeed：完成；failed：失败。

        :param status: The status of this AccessControlTask.
        :type status: str
        """
        self._status = status

    @property
    def action(self):
        r"""Gets the action of this AccessControlTask.

        任务类型，unban：解禁任务；ban：封禁任务。

        :return: The action of this AccessControlTask.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this AccessControlTask.

        任务类型，unban：解禁任务；ban：封禁任务。

        :param action: The action of this AccessControlTask.
        :type action: str
        """
        self._action = action

    @property
    def create_time(self):
        r"""Gets the create_time of this AccessControlTask.

        创建时间戳（毫秒）。

        :return: The create_time of this AccessControlTask.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AccessControlTask.

        创建时间戳（毫秒）。

        :param create_time: The create_time of this AccessControlTask.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, AccessControlTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
