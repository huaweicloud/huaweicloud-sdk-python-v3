# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaveImChannelsReq:

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
        'im_channels': 'list[ImChannelConfig]'
    }

    attribute_map = {
        'id': 'id',
        'im_channels': 'im_channels'
    }

    def __init__(self, id=None, im_channels=None):
        r"""SaveImChannelsReq

        The model defined in huaweicloud sdk

        :param id: Agent 实例主键 ID
        :type id: str
        :param im_channels: IM 通道配置列表
        :type im_channels: list[:class:`huaweicloudsdkworkspace.v2.ImChannelConfig`]
        """
        
        

        self._id = None
        self._im_channels = None
        self.discriminator = None

        self.id = id
        self.im_channels = im_channels

    @property
    def id(self):
        r"""Gets the id of this SaveImChannelsReq.

        Agent 实例主键 ID

        :return: The id of this SaveImChannelsReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SaveImChannelsReq.

        Agent 实例主键 ID

        :param id: The id of this SaveImChannelsReq.
        :type id: str
        """
        self._id = id

    @property
    def im_channels(self):
        r"""Gets the im_channels of this SaveImChannelsReq.

        IM 通道配置列表

        :return: The im_channels of this SaveImChannelsReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ImChannelConfig`]
        """
        return self._im_channels

    @im_channels.setter
    def im_channels(self, im_channels):
        r"""Sets the im_channels of this SaveImChannelsReq.

        IM 通道配置列表

        :param im_channels: The im_channels of this SaveImChannelsReq.
        :type im_channels: list[:class:`huaweicloudsdkworkspace.v2.ImChannelConfig`]
        """
        self._im_channels = im_channels

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
        if not isinstance(other, SaveImChannelsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
