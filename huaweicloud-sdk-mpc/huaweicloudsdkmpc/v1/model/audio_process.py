# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioProcess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume': 'str',
        'volume_expr': 'int'
    }

    attribute_map = {
        'volume': 'volume',
        'volume_expr': 'volume_expr'
    }

    def __init__(self, volume=None, volume_expr=None):
        """AudioProcess

        The model defined in huaweicloud sdk

        :param volume: 音量调整方式： - auto：表示自动调整音量。 - dynamic：表示人为调整，需设定音量调整幅值。 
        :type volume: str
        :param volume_expr: 音量调整幅值，需指定volume为dynamic。  取值范围：[-15,15]  单位：dB 
        :type volume_expr: int
        """
        
        

        self._volume = None
        self._volume_expr = None
        self.discriminator = None

        if volume is not None:
            self.volume = volume
        if volume_expr is not None:
            self.volume_expr = volume_expr

    @property
    def volume(self):
        """Gets the volume of this AudioProcess.

        音量调整方式： - auto：表示自动调整音量。 - dynamic：表示人为调整，需设定音量调整幅值。 

        :return: The volume of this AudioProcess.
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this AudioProcess.

        音量调整方式： - auto：表示自动调整音量。 - dynamic：表示人为调整，需设定音量调整幅值。 

        :param volume: The volume of this AudioProcess.
        :type volume: str
        """
        self._volume = volume

    @property
    def volume_expr(self):
        """Gets the volume_expr of this AudioProcess.

        音量调整幅值，需指定volume为dynamic。  取值范围：[-15,15]  单位：dB 

        :return: The volume_expr of this AudioProcess.
        :rtype: int
        """
        return self._volume_expr

    @volume_expr.setter
    def volume_expr(self, volume_expr):
        """Sets the volume_expr of this AudioProcess.

        音量调整幅值，需指定volume为dynamic。  取值范围：[-15,15]  单位：dB 

        :param volume_expr: The volume_expr of this AudioProcess.
        :type volume_expr: int
        """
        self._volume_expr = volume_expr

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
        if not isinstance(other, AudioProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
