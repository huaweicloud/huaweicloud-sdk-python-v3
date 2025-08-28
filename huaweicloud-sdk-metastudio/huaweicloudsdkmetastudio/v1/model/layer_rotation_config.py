# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LayerRotationConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'angle': 'int'
    }

    attribute_map = {
        'angle': 'angle'
    }

    def __init__(self, angle=None):
        r"""LayerRotationConfig

        The model defined in huaweicloud sdk

        :param angle: **参数解释**： 旋转角度。 **取值范围**： 角度范围0-360度。 **默认取值**： 0度。 **约束限制**： 以素材中心点旋转。 视频素材不支持旋转
        :type angle: int
        """
        
        

        self._angle = None
        self.discriminator = None

        if angle is not None:
            self.angle = angle

    @property
    def angle(self):
        r"""Gets the angle of this LayerRotationConfig.

        **参数解释**： 旋转角度。 **取值范围**： 角度范围0-360度。 **默认取值**： 0度。 **约束限制**： 以素材中心点旋转。 视频素材不支持旋转

        :return: The angle of this LayerRotationConfig.
        :rtype: int
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        r"""Sets the angle of this LayerRotationConfig.

        **参数解释**： 旋转角度。 **取值范围**： 角度范围0-360度。 **默认取值**： 0度。 **约束限制**： 以素材中心点旋转。 视频素材不支持旋转

        :param angle: The angle of this LayerRotationConfig.
        :type angle: int
        """
        self._angle = angle

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
        if not isinstance(other, LayerRotationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
