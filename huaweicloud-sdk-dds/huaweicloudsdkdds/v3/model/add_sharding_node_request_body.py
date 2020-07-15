# coding: utf-8

import pprint
import re

import six





class AddShardingNodeRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'spec_code': 'str',
        'num': 'int',
        'volume': 'AddShardingNodeVolumeOption'
    }

    attribute_map = {
        'type': 'type',
        'spec_code': 'spec_code',
        'num': 'num',
        'volume': 'volume'
    }

    def __init__(self, type=None, spec_code=None, num=None, volume=None):
        """AddShardingNodeRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._spec_code = None
        self._num = None
        self._volume = None
        self.discriminator = None

        self.type = type
        self.spec_code = spec_code
        self.num = num
        if volume is not None:
            self.volume = volume

    @property
    def type(self):
        """Gets the type of this AddShardingNodeRequestBody.

        待扩容的对象类型。 - 扩容mongos节点时，取值为“mongos”。 - 扩容shard组时，取值为“shard”。

        :return: The type of this AddShardingNodeRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddShardingNodeRequestBody.

        待扩容的对象类型。 - 扩容mongos节点时，取值为“mongos”。 - 扩容shard组时，取值为“shard”。

        :param type: The type of this AddShardingNodeRequestBody.
        :type: str
        """
        self._type = type

    @property
    def spec_code(self):
        """Gets the spec_code of this AddShardingNodeRequestBody.

        资源规格编码。

        :return: The spec_code of this AddShardingNodeRequestBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this AddShardingNodeRequestBody.

        资源规格编码。

        :param spec_code: The spec_code of this AddShardingNodeRequestBody.
        :type: str
        """
        self._spec_code = spec_code

    @property
    def num(self):
        """Gets the num of this AddShardingNodeRequestBody.

        一个社区版集群实例下，最多支持16个mongos节点和16个shard组。

        :return: The num of this AddShardingNodeRequestBody.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this AddShardingNodeRequestBody.

        一个社区版集群实例下，最多支持16个mongos节点和16个shard组。

        :param num: The num of this AddShardingNodeRequestBody.
        :type: int
        """
        self._num = num

    @property
    def volume(self):
        """Gets the volume of this AddShardingNodeRequestBody.


        :return: The volume of this AddShardingNodeRequestBody.
        :rtype: AddShardingNodeVolumeOption
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this AddShardingNodeRequestBody.


        :param volume: The volume of this AddShardingNodeRequestBody.
        :type: AddShardingNodeVolumeOption
        """
        self._volume = volume

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddShardingNodeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
