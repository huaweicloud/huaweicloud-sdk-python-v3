# coding: utf-8

import pprint
import re

import six





class TranscodeSummary:


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
        'value': 'float'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, type=None, value=None):
        """TranscodeSummary - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._value = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def type(self):
        """Gets the type of this TranscodeSummary.

        转码规格，格式是“编码格式_分辨率档位”（未开启高清低码）和“编码格式_PVC_分辨率档位”（开启高清低码）。  其中编码格式包括H264、H265，分辨率档位包括：  4K（3840 x 2160）及以下，2K（2560 x 1440）及以下，FHD（1920 x 1080）及以下，HD（1280 x 720）及以下，SD（640 x 480）及以下。 

        :return: The type of this TranscodeSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TranscodeSummary.

        转码规格，格式是“编码格式_分辨率档位”（未开启高清低码）和“编码格式_PVC_分辨率档位”（开启高清低码）。  其中编码格式包括H264、H265，分辨率档位包括：  4K（3840 x 2160）及以下，2K（2560 x 1440）及以下，FHD（1920 x 1080）及以下，HD（1280 x 720）及以下，SD（640 x 480）及以下。 

        :param type: The type of this TranscodeSummary.
        :type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this TranscodeSummary.

        总转码时长，单位为分钟，保留两位小数。

        :return: The value of this TranscodeSummary.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TranscodeSummary.

        总转码时长，单位为分钟，保留两位小数。

        :param value: The value of this TranscodeSummary.
        :type: float
        """
        self._value = value

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
        if not isinstance(other, TranscodeSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
