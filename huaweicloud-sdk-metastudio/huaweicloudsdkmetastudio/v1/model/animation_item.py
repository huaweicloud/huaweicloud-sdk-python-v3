# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnimationItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'animation_asset_id': 'str',
        'timestamp': 'float'
    }

    attribute_map = {
        'animation_asset_id': 'animation_asset_id',
        'timestamp': 'timestamp'
    }

    def __init__(self, animation_asset_id=None, timestamp=None):
        """AnimationItem

        The model defined in huaweicloud sdk

        :param animation_asset_id: 动作资产ID。
        :type animation_asset_id: str
        :param timestamp: 时间戳，相对时间戳。  单位秒。  保留3位小数。
        :type timestamp: float
        """
        
        

        self._animation_asset_id = None
        self._timestamp = None
        self.discriminator = None

        if animation_asset_id is not None:
            self.animation_asset_id = animation_asset_id
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def animation_asset_id(self):
        """Gets the animation_asset_id of this AnimationItem.

        动作资产ID。

        :return: The animation_asset_id of this AnimationItem.
        :rtype: str
        """
        return self._animation_asset_id

    @animation_asset_id.setter
    def animation_asset_id(self, animation_asset_id):
        """Sets the animation_asset_id of this AnimationItem.

        动作资产ID。

        :param animation_asset_id: The animation_asset_id of this AnimationItem.
        :type animation_asset_id: str
        """
        self._animation_asset_id = animation_asset_id

    @property
    def timestamp(self):
        """Gets the timestamp of this AnimationItem.

        时间戳，相对时间戳。  单位秒。  保留3位小数。

        :return: The timestamp of this AnimationItem.
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AnimationItem.

        时间戳，相对时间戳。  单位秒。  保留3位小数。

        :param timestamp: The timestamp of this AnimationItem.
        :type timestamp: float
        """
        self._timestamp = timestamp

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
        if not isinstance(other, AnimationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
