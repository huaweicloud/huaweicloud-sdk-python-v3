# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TranscodeSpecCount:


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
        'count': 'int'
    }

    attribute_map = {
        'type': 'type',
        'count': 'count'
    }

    def __init__(self, type=None, count=None):
        """TranscodeSpecCount - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._count = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if count is not None:
            self.count = count

    @property
    def type(self):
        """Gets the type of this TranscodeSpecCount.

        转码规格，具体格式如下： - 若未开启高清低码，则格式为：编码格式_分辨率档位。 - 若已开启高清低码，则格式为：编码格式_PVC_分辨率档位。  其中，编码格式包括H264、H265，分辨率档位包括： - 4K：3840 x 2160及以下 - 2K：2560 x 1440及以下 - FHD：1920 x 1080及以下 - HD：1280 x 720及以下 - SD：640 x 480及以下  示例：若编码格式为H264，分辨率档位为FHD，则转码规格为H264_FHD。 

        :return: The type of this TranscodeSpecCount.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TranscodeSpecCount.

        转码规格，具体格式如下： - 若未开启高清低码，则格式为：编码格式_分辨率档位。 - 若已开启高清低码，则格式为：编码格式_PVC_分辨率档位。  其中，编码格式包括H264、H265，分辨率档位包括： - 4K：3840 x 2160及以下 - 2K：2560 x 1440及以下 - FHD：1920 x 1080及以下 - HD：1280 x 720及以下 - SD：640 x 480及以下  示例：若编码格式为H264，分辨率档位为FHD，则转码规格为H264_FHD。 

        :param type: The type of this TranscodeSpecCount.
        :type: str
        """
        self._type = type

    @property
    def count(self):
        """Gets the count of this TranscodeSpecCount.

        采样时间点转码任务数。

        :return: The count of this TranscodeSpecCount.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TranscodeSpecCount.

        采样时间点转码任务数。

        :param count: The count of this TranscodeSpecCount.
        :type: int
        """
        self._count = count

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
        if not isinstance(other, TranscodeSpecCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
