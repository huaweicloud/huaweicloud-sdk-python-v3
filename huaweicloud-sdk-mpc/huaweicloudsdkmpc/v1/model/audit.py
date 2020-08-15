# coding: utf-8

import pprint
import re

import six





class Audit:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'position': 'int',
        'index': 'int'
    }

    attribute_map = {
        'position': 'position',
        'index': 'index'
    }

    def __init__(self, position=None, index=None):
        """Audit - a model defined in huaweicloud sdk"""
        
        

        self._position = None
        self._index = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if index is not None:
            self.index = index

    @property
    def position(self):
        """Gets the position of this Audit.

        内容质检位置。  取值如下： - 1: 表示原始片源检查。 - 2：表示转码后片源检查，转码后的片源分辨率必须为720p及以上，且格式需与原始片源一致。 

        :return: The position of this Audit.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Audit.

        内容质检位置。  取值如下： - 1: 表示原始片源检查。 - 2：表示转码后片源检查，转码后的片源分辨率必须为720p及以上，且格式需与原始片源一致。 

        :param position: The position of this Audit.
        :type: int
        """
        self._position = position

    @property
    def index(self):
        """Gets the index of this Audit.

        转码模板ID索引。此索引必须为TransPresetID中的一个。 index从0开始，表示对应的是第几路的校验，比如一进六出，需要对第4路检查，就输入3。  >- 如对原片源质检，此字段不填。 >- 原始分辨率和转码后的分辨率都必须是1280*720及之上。 >- 若对转码后片源检测，必须和原始分辨率一致。 

        :return: The index of this Audit.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Audit.

        转码模板ID索引。此索引必须为TransPresetID中的一个。 index从0开始，表示对应的是第几路的校验，比如一进六出，需要对第4路检查，就输入3。  >- 如对原片源质检，此字段不填。 >- 原始分辨率和转码后的分辨率都必须是1280*720及之上。 >- 若对转码后片源检测，必须和原始分辨率一致。 

        :param index: The index of this Audit.
        :type: int
        """
        self._index = index

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
        if not isinstance(other, Audit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
