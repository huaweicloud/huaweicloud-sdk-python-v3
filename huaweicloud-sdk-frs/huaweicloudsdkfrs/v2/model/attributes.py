# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Attributes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gender': 'str',
        'dress': 'Dress',
        'glass': 'str',
        'hat': 'str',
        'age': 'int',
        'mask': 'str',
        'beard': 'str',
        'phototype': 'str',
        'quality': 'FaceQuality',
        'hair': 'str',
        'expression': 'AttributesExpression',
        'face_angle': 'int'
    }

    attribute_map = {
        'gender': 'gender',
        'dress': 'dress',
        'glass': 'glass',
        'hat': 'hat',
        'age': 'age',
        'mask': 'mask',
        'beard': 'beard',
        'phototype': 'phototype',
        'quality': 'quality',
        'hair': 'hair',
        'expression': 'expression',
        'face_angle': 'face_angle'
    }

    def __init__(self, gender=None, dress=None, glass=None, hat=None, age=None, mask=None, beard=None, phototype=None, quality=None, hair=None, expression=None, face_angle=None):
        r"""Attributes

        The model defined in huaweicloud sdk

        :param gender: 性别： • male：男性 • female：女性
        :type gender: str
        :param dress: 
        :type dress: :class:`huaweicloudsdkfrs.v2.Dress`
        :param glass: 是否带眼镜： • yes：带眼镜 • dark：带墨镜 • none：未戴眼镜 • unknown：未知
        :type glass: str
        :param hat: 是否戴帽子： • yes：戴帽子 • none：未戴帽子 • unknown：未知
        :type hat: str
        :param age: 年龄。
        :type age: int
        :param mask: 是否戴口罩： • yes：戴口罩 • none：未戴口罩 • unknown：未知
        :type mask: str
        :param beard: 胡须： • yes：有胡须 • none：无胡须 • unknown：未知
        :type beard: str
        :param phototype: 图片类型： • idcard：证件照 • monitor：摄像头监控 • internet photo：网络图片
        :type phototype: str
        :param quality: 
        :type quality: :class:`huaweicloudsdkfrs.v2.FaceQuality`
        :param hair: 发型： • long：长发 • short：短发 • unknown：未知
        :type hair: str
        :param expression: 
        :type expression: :class:`huaweicloudsdkfrs.v2.AttributesExpression`
        :param face_angle: 人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转。
        :type face_angle: int
        """
        
        

        self._gender = None
        self._dress = None
        self._glass = None
        self._hat = None
        self._age = None
        self._mask = None
        self._beard = None
        self._phototype = None
        self._quality = None
        self._hair = None
        self._expression = None
        self._face_angle = None
        self.discriminator = None

        self.gender = gender
        self.dress = dress
        self.glass = glass
        self.hat = hat
        self.age = age
        self.mask = mask
        self.beard = beard
        self.phototype = phototype
        self.quality = quality
        self.hair = hair
        self.expression = expression
        self.face_angle = face_angle

    @property
    def gender(self):
        r"""Gets the gender of this Attributes.

        性别： • male：男性 • female：女性

        :return: The gender of this Attributes.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        r"""Sets the gender of this Attributes.

        性别： • male：男性 • female：女性

        :param gender: The gender of this Attributes.
        :type gender: str
        """
        self._gender = gender

    @property
    def dress(self):
        r"""Gets the dress of this Attributes.

        :return: The dress of this Attributes.
        :rtype: :class:`huaweicloudsdkfrs.v2.Dress`
        """
        return self._dress

    @dress.setter
    def dress(self, dress):
        r"""Sets the dress of this Attributes.

        :param dress: The dress of this Attributes.
        :type dress: :class:`huaweicloudsdkfrs.v2.Dress`
        """
        self._dress = dress

    @property
    def glass(self):
        r"""Gets the glass of this Attributes.

        是否带眼镜： • yes：带眼镜 • dark：带墨镜 • none：未戴眼镜 • unknown：未知

        :return: The glass of this Attributes.
        :rtype: str
        """
        return self._glass

    @glass.setter
    def glass(self, glass):
        r"""Sets the glass of this Attributes.

        是否带眼镜： • yes：带眼镜 • dark：带墨镜 • none：未戴眼镜 • unknown：未知

        :param glass: The glass of this Attributes.
        :type glass: str
        """
        self._glass = glass

    @property
    def hat(self):
        r"""Gets the hat of this Attributes.

        是否戴帽子： • yes：戴帽子 • none：未戴帽子 • unknown：未知

        :return: The hat of this Attributes.
        :rtype: str
        """
        return self._hat

    @hat.setter
    def hat(self, hat):
        r"""Sets the hat of this Attributes.

        是否戴帽子： • yes：戴帽子 • none：未戴帽子 • unknown：未知

        :param hat: The hat of this Attributes.
        :type hat: str
        """
        self._hat = hat

    @property
    def age(self):
        r"""Gets the age of this Attributes.

        年龄。

        :return: The age of this Attributes.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        r"""Sets the age of this Attributes.

        年龄。

        :param age: The age of this Attributes.
        :type age: int
        """
        self._age = age

    @property
    def mask(self):
        r"""Gets the mask of this Attributes.

        是否戴口罩： • yes：戴口罩 • none：未戴口罩 • unknown：未知

        :return: The mask of this Attributes.
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        r"""Sets the mask of this Attributes.

        是否戴口罩： • yes：戴口罩 • none：未戴口罩 • unknown：未知

        :param mask: The mask of this Attributes.
        :type mask: str
        """
        self._mask = mask

    @property
    def beard(self):
        r"""Gets the beard of this Attributes.

        胡须： • yes：有胡须 • none：无胡须 • unknown：未知

        :return: The beard of this Attributes.
        :rtype: str
        """
        return self._beard

    @beard.setter
    def beard(self, beard):
        r"""Sets the beard of this Attributes.

        胡须： • yes：有胡须 • none：无胡须 • unknown：未知

        :param beard: The beard of this Attributes.
        :type beard: str
        """
        self._beard = beard

    @property
    def phototype(self):
        r"""Gets the phototype of this Attributes.

        图片类型： • idcard：证件照 • monitor：摄像头监控 • internet photo：网络图片

        :return: The phototype of this Attributes.
        :rtype: str
        """
        return self._phototype

    @phototype.setter
    def phototype(self, phototype):
        r"""Sets the phototype of this Attributes.

        图片类型： • idcard：证件照 • monitor：摄像头监控 • internet photo：网络图片

        :param phototype: The phototype of this Attributes.
        :type phototype: str
        """
        self._phototype = phototype

    @property
    def quality(self):
        r"""Gets the quality of this Attributes.

        :return: The quality of this Attributes.
        :rtype: :class:`huaweicloudsdkfrs.v2.FaceQuality`
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        r"""Sets the quality of this Attributes.

        :param quality: The quality of this Attributes.
        :type quality: :class:`huaweicloudsdkfrs.v2.FaceQuality`
        """
        self._quality = quality

    @property
    def hair(self):
        r"""Gets the hair of this Attributes.

        发型： • long：长发 • short：短发 • unknown：未知

        :return: The hair of this Attributes.
        :rtype: str
        """
        return self._hair

    @hair.setter
    def hair(self, hair):
        r"""Sets the hair of this Attributes.

        发型： • long：长发 • short：短发 • unknown：未知

        :param hair: The hair of this Attributes.
        :type hair: str
        """
        self._hair = hair

    @property
    def expression(self):
        r"""Gets the expression of this Attributes.

        :return: The expression of this Attributes.
        :rtype: :class:`huaweicloudsdkfrs.v2.AttributesExpression`
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this Attributes.

        :param expression: The expression of this Attributes.
        :type expression: :class:`huaweicloudsdkfrs.v2.AttributesExpression`
        """
        self._expression = expression

    @property
    def face_angle(self):
        r"""Gets the face_angle of this Attributes.

        人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转。

        :return: The face_angle of this Attributes.
        :rtype: int
        """
        return self._face_angle

    @face_angle.setter
    def face_angle(self, face_angle):
        r"""Sets the face_angle of this Attributes.

        人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转。

        :param face_angle: The face_angle of this Attributes.
        :type face_angle: int
        """
        self._face_angle = face_angle

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
        if not isinstance(other, Attributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
