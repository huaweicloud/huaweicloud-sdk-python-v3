# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChannelDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_id': 'str',
        'name': 'str',
        'channel': 'str',
        'endpoint': 'str',
        'description': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'name': 'name',
        'channel': 'channel',
        'endpoint': 'endpoint',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, channel_id=None, name=None, channel=None, endpoint=None, description=None, create_time=None, update_time=None):
        r"""ChannelDTO

        The model defined in huaweicloud sdk

        :param channel_id: 规则ID
        :type channel_id: str
        :param name: 规则名称
        :type name: str
        :param channel: 通道
        :type channel: str
        :param endpoint: 推送地址信息
        :type endpoint: str
        :param description: 规则描述
        :type description: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._channel_id = None
        self._name = None
        self._channel = None
        self._endpoint = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if channel_id is not None:
            self.channel_id = channel_id
        if name is not None:
            self.name = name
        if channel is not None:
            self.channel = channel
        if endpoint is not None:
            self.endpoint = endpoint
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def channel_id(self):
        r"""Gets the channel_id of this ChannelDTO.

        规则ID

        :return: The channel_id of this ChannelDTO.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this ChannelDTO.

        规则ID

        :param channel_id: The channel_id of this ChannelDTO.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def name(self):
        r"""Gets the name of this ChannelDTO.

        规则名称

        :return: The name of this ChannelDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ChannelDTO.

        规则名称

        :param name: The name of this ChannelDTO.
        :type name: str
        """
        self._name = name

    @property
    def channel(self):
        r"""Gets the channel of this ChannelDTO.

        通道

        :return: The channel of this ChannelDTO.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        r"""Sets the channel of this ChannelDTO.

        通道

        :param channel: The channel of this ChannelDTO.
        :type channel: str
        """
        self._channel = channel

    @property
    def endpoint(self):
        r"""Gets the endpoint of this ChannelDTO.

        推送地址信息

        :return: The endpoint of this ChannelDTO.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this ChannelDTO.

        推送地址信息

        :param endpoint: The endpoint of this ChannelDTO.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def description(self):
        r"""Gets the description of this ChannelDTO.

        规则描述

        :return: The description of this ChannelDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ChannelDTO.

        规则描述

        :param description: The description of this ChannelDTO.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this ChannelDTO.

        创建时间

        :return: The create_time of this ChannelDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ChannelDTO.

        创建时间

        :param create_time: The create_time of this ChannelDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ChannelDTO.

        更新时间

        :return: The update_time of this ChannelDTO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ChannelDTO.

        更新时间

        :param update_time: The update_time of this ChannelDTO.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ChannelDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
