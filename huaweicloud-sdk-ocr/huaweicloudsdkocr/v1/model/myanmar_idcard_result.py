# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MyanmarIdcardResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'side': 'str',
        '_class': 'str',
        'nrc_id': 'str',
        'issue_date': 'str',
        'name': 'str',
        'father_name': 'str',
        'birth': 'str',
        'bloodlines_religion': 'str',
        'height': 'str',
        'blood_group': 'str',
        'card_id': 'str',
        'nrc_id_back': 'str',
        'profession': 'str',
        'address': 'str',
        'confidence': 'MyanmarIdcardConfidence',
        'portrait_image': 'str',
        'portrait_location': 'list[list[int]]',
        'idcard_type': 'str'
    }

    attribute_map = {
        'side': 'side',
        '_class': 'class',
        'nrc_id': 'nrc_id',
        'issue_date': 'issue_date',
        'name': 'name',
        'father_name': 'father_name',
        'birth': 'birth',
        'bloodlines_religion': 'bloodlines_religion',
        'height': 'height',
        'blood_group': 'blood_group',
        'card_id': 'card_id',
        'nrc_id_back': 'nrc_id_back',
        'profession': 'profession',
        'address': 'address',
        'confidence': 'confidence',
        'portrait_image': 'portrait_image',
        'portrait_location': 'portrait_location',
        'idcard_type': 'idcard_type'
    }

    def __init__(self, side=None, _class=None, nrc_id=None, issue_date=None, name=None, father_name=None, birth=None, bloodlines_religion=None, height=None, blood_group=None, card_id=None, nrc_id_back=None, profession=None, address=None, confidence=None, portrait_image=None, portrait_location=None, idcard_type=None):
        """MyanmarIdcardResult

        The model defined in huaweicloud sdk

        :param side: 标示正面还是反面，取值为front或back。 
        :type side: str
        :param _class: 身份证类型。取值如下所示： - new_version：新版身份证 - old_version：旧版 
        :type _class: str
        :param nrc_id: 身份证号码。 
        :type nrc_id: str
        :param issue_date: 签发日期。 
        :type issue_date: str
        :param name: 姓名。 
        :type name: str
        :param father_name: 父亲名字。 
        :type father_name: str
        :param birth: 出生日期。 
        :type birth: str
        :param bloodlines_religion: 族群或宗教。 
        :type bloodlines_religion: str
        :param height: 身高。 
        :type height: str
        :param blood_group: 血型。 
        :type blood_group: str
        :param card_id: 身份证的卡号（背面）。 
        :type card_id: str
        :param nrc_id_back: 背面的身份证号码。 
        :type nrc_id_back: str
        :param profession: 职业。 
        :type profession: str
        :param address: 地址。 
        :type address: str
        :param confidence: 
        :type confidence: :class:`huaweicloudsdkocr.v1.MyanmarIdcardConfidence`
        :param portrait_image: 头像的base64编码。 当输入参数“return_portrait_image”为“true”时，才返回该参数。 
        :type portrait_image: str
        :param portrait_location: 头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向 
        :type portrait_location: list[list[int]]
        :param idcard_type: 身份证的类型。取值如下所示： - normal：身份证原件 - copy：复印的身份证 当输入参数“return_idcard_type”为“true”时，才返回该参数。 
        :type idcard_type: str
        """
        
        

        self._side = None
        self.__class = None
        self._nrc_id = None
        self._issue_date = None
        self._name = None
        self._father_name = None
        self._birth = None
        self._bloodlines_religion = None
        self._height = None
        self._blood_group = None
        self._card_id = None
        self._nrc_id_back = None
        self._profession = None
        self._address = None
        self._confidence = None
        self._portrait_image = None
        self._portrait_location = None
        self._idcard_type = None
        self.discriminator = None

        if side is not None:
            self.side = side
        if _class is not None:
            self._class = _class
        if nrc_id is not None:
            self.nrc_id = nrc_id
        if issue_date is not None:
            self.issue_date = issue_date
        if name is not None:
            self.name = name
        if father_name is not None:
            self.father_name = father_name
        if birth is not None:
            self.birth = birth
        if bloodlines_religion is not None:
            self.bloodlines_religion = bloodlines_religion
        if height is not None:
            self.height = height
        if blood_group is not None:
            self.blood_group = blood_group
        if card_id is not None:
            self.card_id = card_id
        if nrc_id_back is not None:
            self.nrc_id_back = nrc_id_back
        if profession is not None:
            self.profession = profession
        if address is not None:
            self.address = address
        if confidence is not None:
            self.confidence = confidence
        if portrait_image is not None:
            self.portrait_image = portrait_image
        if portrait_location is not None:
            self.portrait_location = portrait_location
        if idcard_type is not None:
            self.idcard_type = idcard_type

    @property
    def side(self):
        """Gets the side of this MyanmarIdcardResult.

        标示正面还是反面，取值为front或back。 

        :return: The side of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this MyanmarIdcardResult.

        标示正面还是反面，取值为front或back。 

        :param side: The side of this MyanmarIdcardResult.
        :type side: str
        """
        self._side = side

    @property
    def _class(self):
        """Gets the _class of this MyanmarIdcardResult.

        身份证类型。取值如下所示： - new_version：新版身份证 - old_version：旧版 

        :return: The _class of this MyanmarIdcardResult.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this MyanmarIdcardResult.

        身份证类型。取值如下所示： - new_version：新版身份证 - old_version：旧版 

        :param _class: The _class of this MyanmarIdcardResult.
        :type _class: str
        """
        self.__class = _class

    @property
    def nrc_id(self):
        """Gets the nrc_id of this MyanmarIdcardResult.

        身份证号码。 

        :return: The nrc_id of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._nrc_id

    @nrc_id.setter
    def nrc_id(self, nrc_id):
        """Sets the nrc_id of this MyanmarIdcardResult.

        身份证号码。 

        :param nrc_id: The nrc_id of this MyanmarIdcardResult.
        :type nrc_id: str
        """
        self._nrc_id = nrc_id

    @property
    def issue_date(self):
        """Gets the issue_date of this MyanmarIdcardResult.

        签发日期。 

        :return: The issue_date of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this MyanmarIdcardResult.

        签发日期。 

        :param issue_date: The issue_date of this MyanmarIdcardResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def name(self):
        """Gets the name of this MyanmarIdcardResult.

        姓名。 

        :return: The name of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MyanmarIdcardResult.

        姓名。 

        :param name: The name of this MyanmarIdcardResult.
        :type name: str
        """
        self._name = name

    @property
    def father_name(self):
        """Gets the father_name of this MyanmarIdcardResult.

        父亲名字。 

        :return: The father_name of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._father_name

    @father_name.setter
    def father_name(self, father_name):
        """Sets the father_name of this MyanmarIdcardResult.

        父亲名字。 

        :param father_name: The father_name of this MyanmarIdcardResult.
        :type father_name: str
        """
        self._father_name = father_name

    @property
    def birth(self):
        """Gets the birth of this MyanmarIdcardResult.

        出生日期。 

        :return: The birth of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this MyanmarIdcardResult.

        出生日期。 

        :param birth: The birth of this MyanmarIdcardResult.
        :type birth: str
        """
        self._birth = birth

    @property
    def bloodlines_religion(self):
        """Gets the bloodlines_religion of this MyanmarIdcardResult.

        族群或宗教。 

        :return: The bloodlines_religion of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._bloodlines_religion

    @bloodlines_religion.setter
    def bloodlines_religion(self, bloodlines_religion):
        """Sets the bloodlines_religion of this MyanmarIdcardResult.

        族群或宗教。 

        :param bloodlines_religion: The bloodlines_religion of this MyanmarIdcardResult.
        :type bloodlines_religion: str
        """
        self._bloodlines_religion = bloodlines_religion

    @property
    def height(self):
        """Gets the height of this MyanmarIdcardResult.

        身高。 

        :return: The height of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this MyanmarIdcardResult.

        身高。 

        :param height: The height of this MyanmarIdcardResult.
        :type height: str
        """
        self._height = height

    @property
    def blood_group(self):
        """Gets the blood_group of this MyanmarIdcardResult.

        血型。 

        :return: The blood_group of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._blood_group

    @blood_group.setter
    def blood_group(self, blood_group):
        """Sets the blood_group of this MyanmarIdcardResult.

        血型。 

        :param blood_group: The blood_group of this MyanmarIdcardResult.
        :type blood_group: str
        """
        self._blood_group = blood_group

    @property
    def card_id(self):
        """Gets the card_id of this MyanmarIdcardResult.

        身份证的卡号（背面）。 

        :return: The card_id of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this MyanmarIdcardResult.

        身份证的卡号（背面）。 

        :param card_id: The card_id of this MyanmarIdcardResult.
        :type card_id: str
        """
        self._card_id = card_id

    @property
    def nrc_id_back(self):
        """Gets the nrc_id_back of this MyanmarIdcardResult.

        背面的身份证号码。 

        :return: The nrc_id_back of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._nrc_id_back

    @nrc_id_back.setter
    def nrc_id_back(self, nrc_id_back):
        """Sets the nrc_id_back of this MyanmarIdcardResult.

        背面的身份证号码。 

        :param nrc_id_back: The nrc_id_back of this MyanmarIdcardResult.
        :type nrc_id_back: str
        """
        self._nrc_id_back = nrc_id_back

    @property
    def profession(self):
        """Gets the profession of this MyanmarIdcardResult.

        职业。 

        :return: The profession of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._profession

    @profession.setter
    def profession(self, profession):
        """Sets the profession of this MyanmarIdcardResult.

        职业。 

        :param profession: The profession of this MyanmarIdcardResult.
        :type profession: str
        """
        self._profession = profession

    @property
    def address(self):
        """Gets the address of this MyanmarIdcardResult.

        地址。 

        :return: The address of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MyanmarIdcardResult.

        地址。 

        :param address: The address of this MyanmarIdcardResult.
        :type address: str
        """
        self._address = address

    @property
    def confidence(self):
        """Gets the confidence of this MyanmarIdcardResult.

        :return: The confidence of this MyanmarIdcardResult.
        :rtype: :class:`huaweicloudsdkocr.v1.MyanmarIdcardConfidence`
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this MyanmarIdcardResult.

        :param confidence: The confidence of this MyanmarIdcardResult.
        :type confidence: :class:`huaweicloudsdkocr.v1.MyanmarIdcardConfidence`
        """
        self._confidence = confidence

    @property
    def portrait_image(self):
        """Gets the portrait_image of this MyanmarIdcardResult.

        头像的base64编码。 当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :return: The portrait_image of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        """Sets the portrait_image of this MyanmarIdcardResult.

        头像的base64编码。 当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :param portrait_image: The portrait_image of this MyanmarIdcardResult.
        :type portrait_image: str
        """
        self._portrait_image = portrait_image

    @property
    def portrait_location(self):
        """Gets the portrait_location of this MyanmarIdcardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向 

        :return: The portrait_location of this MyanmarIdcardResult.
        :rtype: list[list[int]]
        """
        return self._portrait_location

    @portrait_location.setter
    def portrait_location(self, portrait_location):
        """Sets the portrait_location of this MyanmarIdcardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向 

        :param portrait_location: The portrait_location of this MyanmarIdcardResult.
        :type portrait_location: list[list[int]]
        """
        self._portrait_location = portrait_location

    @property
    def idcard_type(self):
        """Gets the idcard_type of this MyanmarIdcardResult.

        身份证的类型。取值如下所示： - normal：身份证原件 - copy：复印的身份证 当输入参数“return_idcard_type”为“true”时，才返回该参数。 

        :return: The idcard_type of this MyanmarIdcardResult.
        :rtype: str
        """
        return self._idcard_type

    @idcard_type.setter
    def idcard_type(self, idcard_type):
        """Sets the idcard_type of this MyanmarIdcardResult.

        身份证的类型。取值如下所示： - normal：身份证原件 - copy：复印的身份证 当输入参数“return_idcard_type”为“true”时，才返回该参数。 

        :param idcard_type: The idcard_type of this MyanmarIdcardResult.
        :type idcard_type: str
        """
        self._idcard_type = idcard_type

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
        if not isinstance(other, MyanmarIdcardResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
