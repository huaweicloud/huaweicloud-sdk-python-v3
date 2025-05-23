# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailOfChannelRequest:

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
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, channel_id=None, enterprise_project_id=None):
        r"""ShowDetailOfChannelRequest

        The model defined in huaweicloud sdk

        :param channel_id: 指定查询的事件通道ID
        :type channel_id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._channel_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.channel_id = channel_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def channel_id(self):
        r"""Gets the channel_id of this ShowDetailOfChannelRequest.

        指定查询的事件通道ID

        :return: The channel_id of this ShowDetailOfChannelRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this ShowDetailOfChannelRequest.

        指定查询的事件通道ID

        :param channel_id: The channel_id of this ShowDetailOfChannelRequest.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDetailOfChannelRequest.

        企业项目id

        :return: The enterprise_project_id of this ShowDetailOfChannelRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDetailOfChannelRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ShowDetailOfChannelRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowDetailOfChannelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
