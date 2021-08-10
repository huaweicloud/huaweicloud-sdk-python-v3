# coding: utf-8

import re
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
        'dress': 'list[str]',
        'glass': 'str',
        'gender': 'str',
        'yaw_angle': 'float',
        'roll_angle': 'float',
        'pitch_angle': 'float',
        'hat': 'str',
        'headpose': 'list[float]',
        'age': 'int',
        'smile': 'str',
        'mask': 'str',
        'beard': 'str',
        'skin': 'str',
        'ethnic': 'str',
        'phototype': 'str',
        'quality': 'FaceQuality',
        'hair': 'str',
        'expression': 'AttributesExpression',
        'face_angle': 'int'
    }

    attribute_map = {
        'dress': 'dress',
        'glass': 'glass',
        'gender': 'gender',
        'yaw_angle': 'yaw_angle',
        'roll_angle': 'roll_angle',
        'pitch_angle': 'pitch_angle',
        'hat': 'hat',
        'headpose': 'headpose',
        'age': 'age',
        'smile': 'smile',
        'mask': 'mask',
        'beard': 'beard',
        'skin': 'skin',
        'ethnic': 'ethnic',
        'phototype': 'phototype',
        'quality': 'quality',
        'hair': 'hair',
        'expression': 'expression',
        'face_angle': 'face_angle'
    }

    def __init__(self, dress=None, glass=None, gender=None, yaw_angle=None, roll_angle=None, pitch_angle=None, hat=None, headpose=None, age=None, smile=None, mask=None, beard=None, skin=None, ethnic=None, phototype=None, quality=None, hair=None, expression=None, face_angle=None):
        """Attributes - a model defined in huaweicloud sdk"""
        
        

        self._dress = None
        self._glass = None
        self._gender = None
        self._yaw_angle = None
        self._roll_angle = None
        self._pitch_angle = None
        self._hat = None
        self._headpose = None
        self._age = None
        self._smile = None
        self._mask = None
        self._beard = None
        self._skin = None
        self._ethnic = None
        self._phototype = None
        self._quality = None
        self._hair = None
        self._expression = None
        self._face_angle = None
        self.discriminator = None

        self.dress = dress
        self.glass = glass
        self.gender = gender
        self.yaw_angle = yaw_angle
        self.roll_angle = roll_angle
        self.pitch_angle = pitch_angle
        self.hat = hat
        self.headpose = headpose
        self.age = age
        self.smile = smile
        self.mask = mask
        self.beard = beard
        self.skin = skin
        self.ethnic = ethnic
        self.phototype = phototype
        self.quality = quality
        self.hair = hair
        self.expression = expression
        self.face_angle = face_angle

    @property
    def dress(self):
        """Gets the dress of this Attributes.

        包含glass和hat两个属性结果。

        :return: The dress of this Attributes.
        :rtype: list[str]
        """
        return self._dress

    @dress.setter
    def dress(self, dress):
        """Sets the dress of this Attributes.

        包含glass和hat两个属性结果。

        :param dress: The dress of this Attributes.
        :type: list[str]
        """
        self._dress = dress

    @property
    def glass(self):
        """Gets the glass of this Attributes.

        是否带眼镜： • yes：带眼镜 • dark：带墨镜 • none：未戴眼镜 • unknown：未知

        :return: The glass of this Attributes.
        :rtype: str
        """
        return self._glass

    @glass.setter
    def glass(self, glass):
        """Sets the glass of this Attributes.

        是否带眼镜： • yes：带眼镜 • dark：带墨镜 • none：未戴眼镜 • unknown：未知

        :param glass: The glass of this Attributes.
        :type: str
        """
        self._glass = glass

    @property
    def gender(self):
        """Gets the gender of this Attributes.

        性别： • male：男 • female：女 • unknown：未知

        :return: The gender of this Attributes.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Attributes.

        性别： • male：男 • female：女 • unknown：未知

        :param gender: The gender of this Attributes.
        :type: str
        """
        self._gender = gender

    @property
    def yaw_angle(self):
        """Gets the yaw_angle of this Attributes.

        围绕Y轴旋转，偏航角，范围[-180,180]。

        :return: The yaw_angle of this Attributes.
        :rtype: float
        """
        return self._yaw_angle

    @yaw_angle.setter
    def yaw_angle(self, yaw_angle):
        """Sets the yaw_angle of this Attributes.

        围绕Y轴旋转，偏航角，范围[-180,180]。

        :param yaw_angle: The yaw_angle of this Attributes.
        :type: float
        """
        self._yaw_angle = yaw_angle

    @property
    def roll_angle(self):
        """Gets the roll_angle of this Attributes.

        围绕Z轴旋转，翻滚角，范围[-180,180]。

        :return: The roll_angle of this Attributes.
        :rtype: float
        """
        return self._roll_angle

    @roll_angle.setter
    def roll_angle(self, roll_angle):
        """Sets the roll_angle of this Attributes.

        围绕Z轴旋转，翻滚角，范围[-180,180]。

        :param roll_angle: The roll_angle of this Attributes.
        :type: float
        """
        self._roll_angle = roll_angle

    @property
    def pitch_angle(self):
        """Gets the pitch_angle of this Attributes.

        围绕X轴旋转，俯仰角，范围[-180,180]。

        :return: The pitch_angle of this Attributes.
        :rtype: float
        """
        return self._pitch_angle

    @pitch_angle.setter
    def pitch_angle(self, pitch_angle):
        """Sets the pitch_angle of this Attributes.

        围绕X轴旋转，俯仰角，范围[-180,180]。

        :param pitch_angle: The pitch_angle of this Attributes.
        :type: float
        """
        self._pitch_angle = pitch_angle

    @property
    def hat(self):
        """Gets the hat of this Attributes.

        是否戴帽子： • yes：戴帽子 • none：未戴帽子 • unknown：未知

        :return: The hat of this Attributes.
        :rtype: str
        """
        return self._hat

    @hat.setter
    def hat(self, hat):
        """Sets the hat of this Attributes.

        是否戴帽子： • yes：戴帽子 • none：未戴帽子 • unknown：未知

        :param hat: The hat of this Attributes.
        :type: str
        """
        self._hat = hat

    @property
    def headpose(self):
        """Gets the headpose of this Attributes.

        人脸轮廓坐标值。

        :return: The headpose of this Attributes.
        :rtype: list[float]
        """
        return self._headpose

    @headpose.setter
    def headpose(self, headpose):
        """Sets the headpose of this Attributes.

        人脸轮廓坐标值。

        :param headpose: The headpose of this Attributes.
        :type: list[float]
        """
        self._headpose = headpose

    @property
    def age(self):
        """Gets the age of this Attributes.

        年龄。

        :return: The age of this Attributes.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this Attributes.

        年龄。

        :param age: The age of this Attributes.
        :type: int
        """
        self._age = age

    @property
    def smile(self):
        """Gets the smile of this Attributes.

        笑脸。

        :return: The smile of this Attributes.
        :rtype: str
        """
        return self._smile

    @smile.setter
    def smile(self, smile):
        """Sets the smile of this Attributes.

        笑脸。

        :param smile: The smile of this Attributes.
        :type: str
        """
        self._smile = smile

    @property
    def mask(self):
        """Gets the mask of this Attributes.

        是否戴口罩： • yes：戴口罩 • none：未戴口罩 • unknown：未知

        :return: The mask of this Attributes.
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this Attributes.

        是否戴口罩： • yes：戴口罩 • none：未戴口罩 • unknown：未知

        :param mask: The mask of this Attributes.
        :type: str
        """
        self._mask = mask

    @property
    def beard(self):
        """Gets the beard of this Attributes.

        胡须： • yes：有胡须 • none：无胡须 • unknown：未知

        :return: The beard of this Attributes.
        :rtype: str
        """
        return self._beard

    @beard.setter
    def beard(self, beard):
        """Sets the beard of this Attributes.

        胡须： • yes：有胡须 • none：无胡须 • unknown：未知

        :param beard: The beard of this Attributes.
        :type: str
        """
        self._beard = beard

    @property
    def skin(self):
        """Gets the skin of this Attributes.

        肤色： • brown：棕 • yellow：黄 • white：白 • black：黑 • unknown：未知

        :return: The skin of this Attributes.
        :rtype: str
        """
        return self._skin

    @skin.setter
    def skin(self, skin):
        """Sets the skin of this Attributes.

        肤色： • brown：棕 • yellow：黄 • white：白 • black：黑 • unknown：未知

        :param skin: The skin of this Attributes.
        :type: str
        """
        self._skin = skin

    @property
    def ethnic(self):
        """Gets the ethnic of this Attributes.

        民族： • han：汉族 • other：其他 • unknown：未知

        :return: The ethnic of this Attributes.
        :rtype: str
        """
        return self._ethnic

    @ethnic.setter
    def ethnic(self, ethnic):
        """Sets the ethnic of this Attributes.

        民族： • han：汉族 • other：其他 • unknown：未知

        :param ethnic: The ethnic of this Attributes.
        :type: str
        """
        self._ethnic = ethnic

    @property
    def phototype(self):
        """Gets the phototype of this Attributes.

        图片类型： • idcard：证件照 • monitor：摄像头监控 • internet photo：网络图片

        :return: The phototype of this Attributes.
        :rtype: str
        """
        return self._phototype

    @phototype.setter
    def phototype(self, phototype):
        """Sets the phototype of this Attributes.

        图片类型： • idcard：证件照 • monitor：摄像头监控 • internet photo：网络图片

        :param phototype: The phototype of this Attributes.
        :type: str
        """
        self._phototype = phototype

    @property
    def quality(self):
        """Gets the quality of this Attributes.


        :return: The quality of this Attributes.
        :rtype: FaceQuality
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this Attributes.


        :param quality: The quality of this Attributes.
        :type: FaceQuality
        """
        self._quality = quality

    @property
    def hair(self):
        """Gets the hair of this Attributes.

        发型： • long：长发 • short：短发 • unknown：未知

        :return: The hair of this Attributes.
        :rtype: str
        """
        return self._hair

    @hair.setter
    def hair(self, hair):
        """Sets the hair of this Attributes.

        发型： • long：长发 • short：短发 • unknown：未知

        :param hair: The hair of this Attributes.
        :type: str
        """
        self._hair = hair

    @property
    def expression(self):
        """Gets the expression of this Attributes.


        :return: The expression of this Attributes.
        :rtype: AttributesExpression
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this Attributes.


        :param expression: The expression of this Attributes.
        :type: AttributesExpression
        """
        self._expression = expression

    @property
    def face_angle(self):
        """Gets the face_angle of this Attributes.

        人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转。

        :return: The face_angle of this Attributes.
        :rtype: int
        """
        return self._face_angle

    @face_angle.setter
    def face_angle(self, face_angle):
        """Sets the face_angle of this Attributes.

        人脸图片旋转角（顺时针偏转角度），支持0°、90°、180°和270°图片旋转。

        :param face_angle: The face_angle of this Attributes.
        :type: int
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
