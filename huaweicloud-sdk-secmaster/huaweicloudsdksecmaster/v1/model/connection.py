# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Connection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_refer_count': 'int',
        'connection_id': 'str',
        'connection_type': 'str',
        'description': 'str',
        'info': 'str',
        'module_id': 'str',
        'template_title': 'str',
        'title': 'str'
    }

    attribute_map = {
        'channel_refer_count': 'channel_refer_count',
        'connection_id': 'connection_id',
        'connection_type': 'connection_type',
        'description': 'description',
        'info': 'info',
        'module_id': 'module_id',
        'template_title': 'template_title',
        'title': 'title'
    }

    def __init__(self, channel_refer_count=None, connection_id=None, connection_type=None, description=None, info=None, module_id=None, template_title=None, title=None):
        r"""Connection

        The model defined in huaweicloud sdk

        :param channel_refer_count: 数值
        :type channel_refer_count: int
        :param connection_id: UUID
        :type connection_id: str
        :param connection_type: **参数解释**: 连接类型 - FILTER 过滤 - INPUT 输入 - OUTPUT 输出  **约束限制** 不涉及 **取值范围**: - FILTER - INPUT - OUTPUT  **默认值** 不涉及
        :type connection_type: str
        :param description: 描述信息
        :type description: str
        :param info: 描述信息
        :type info: str
        :param module_id: UUID
        :type module_id: str
        :param template_title: 相关标题
        :type template_title: str
        :param title: 相关标题
        :type title: str
        """
        
        

        self._channel_refer_count = None
        self._connection_id = None
        self._connection_type = None
        self._description = None
        self._info = None
        self._module_id = None
        self._template_title = None
        self._title = None
        self.discriminator = None

        if channel_refer_count is not None:
            self.channel_refer_count = channel_refer_count
        if connection_id is not None:
            self.connection_id = connection_id
        if connection_type is not None:
            self.connection_type = connection_type
        if description is not None:
            self.description = description
        if info is not None:
            self.info = info
        if module_id is not None:
            self.module_id = module_id
        if template_title is not None:
            self.template_title = template_title
        if title is not None:
            self.title = title

    @property
    def channel_refer_count(self):
        r"""Gets the channel_refer_count of this Connection.

        数值

        :return: The channel_refer_count of this Connection.
        :rtype: int
        """
        return self._channel_refer_count

    @channel_refer_count.setter
    def channel_refer_count(self, channel_refer_count):
        r"""Sets the channel_refer_count of this Connection.

        数值

        :param channel_refer_count: The channel_refer_count of this Connection.
        :type channel_refer_count: int
        """
        self._channel_refer_count = channel_refer_count

    @property
    def connection_id(self):
        r"""Gets the connection_id of this Connection.

        UUID

        :return: The connection_id of this Connection.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this Connection.

        UUID

        :param connection_id: The connection_id of this Connection.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def connection_type(self):
        r"""Gets the connection_type of this Connection.

        **参数解释**: 连接类型 - FILTER 过滤 - INPUT 输入 - OUTPUT 输出  **约束限制** 不涉及 **取值范围**: - FILTER - INPUT - OUTPUT  **默认值** 不涉及

        :return: The connection_type of this Connection.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        r"""Sets the connection_type of this Connection.

        **参数解释**: 连接类型 - FILTER 过滤 - INPUT 输入 - OUTPUT 输出  **约束限制** 不涉及 **取值范围**: - FILTER - INPUT - OUTPUT  **默认值** 不涉及

        :param connection_type: The connection_type of this Connection.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def description(self):
        r"""Gets the description of this Connection.

        描述信息

        :return: The description of this Connection.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Connection.

        描述信息

        :param description: The description of this Connection.
        :type description: str
        """
        self._description = description

    @property
    def info(self):
        r"""Gets the info of this Connection.

        描述信息

        :return: The info of this Connection.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this Connection.

        描述信息

        :param info: The info of this Connection.
        :type info: str
        """
        self._info = info

    @property
    def module_id(self):
        r"""Gets the module_id of this Connection.

        UUID

        :return: The module_id of this Connection.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this Connection.

        UUID

        :param module_id: The module_id of this Connection.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def template_title(self):
        r"""Gets the template_title of this Connection.

        相关标题

        :return: The template_title of this Connection.
        :rtype: str
        """
        return self._template_title

    @template_title.setter
    def template_title(self, template_title):
        r"""Sets the template_title of this Connection.

        相关标题

        :param template_title: The template_title of this Connection.
        :type template_title: str
        """
        self._template_title = template_title

    @property
    def title(self):
        r"""Gets the title of this Connection.

        相关标题

        :return: The title of this Connection.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this Connection.

        相关标题

        :param title: The title of this Connection.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, Connection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
