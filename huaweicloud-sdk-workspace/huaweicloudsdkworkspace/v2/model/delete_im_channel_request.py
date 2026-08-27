# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteImChannelRequest:

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
        'platform': 'str'
    }

    attribute_map = {
        'id': 'id',
        'platform': 'platform'
    }

    def __init__(self, id=None, platform=None):
        r"""DeleteImChannelRequest

        The model defined in huaweicloud sdk

        :param id: Agent 实例主键 ID
        :type id: str
        :param platform: IM 平台类型：wecom / feishu / dingtalk-connector
        :type platform: str
        """
        
        

        self._id = None
        self._platform = None
        self.discriminator = None

        self.id = id
        self.platform = platform

    @property
    def id(self):
        r"""Gets the id of this DeleteImChannelRequest.

        Agent 实例主键 ID

        :return: The id of this DeleteImChannelRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteImChannelRequest.

        Agent 实例主键 ID

        :param id: The id of this DeleteImChannelRequest.
        :type id: str
        """
        self._id = id

    @property
    def platform(self):
        r"""Gets the platform of this DeleteImChannelRequest.

        IM 平台类型：wecom / feishu / dingtalk-connector

        :return: The platform of this DeleteImChannelRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this DeleteImChannelRequest.

        IM 平台类型：wecom / feishu / dingtalk-connector

        :param platform: The platform of this DeleteImChannelRequest.
        :type platform: str
        """
        self._platform = platform

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
        if not isinstance(other, DeleteImChannelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
