# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MyanmarIdcardConfidence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nrc_id': 'float',
        'issue_date': 'float',
        'name': 'float',
        'birth': 'float',
        'bloodlines_religion': 'float',
        'height': 'float',
        'blood_group': 'float',
        'card_id': 'float',
        'nrc_id_back': 'float',
        'profession': 'float',
        'address': 'float'
    }

    attribute_map = {
        'nrc_id': 'nrc_id',
        'issue_date': 'issue_date',
        'name': 'name',
        'birth': 'birth',
        'bloodlines_religion': 'bloodlines_religion',
        'height': 'height',
        'blood_group': 'blood_group',
        'card_id': 'card_id',
        'nrc_id_back': 'nrc_id_back',
        'profession': 'profession',
        'address': 'address'
    }

    def __init__(self, nrc_id=None, issue_date=None, name=None, birth=None, bloodlines_religion=None, height=None, blood_group=None, card_id=None, nrc_id_back=None, profession=None, address=None):
        """MyanmarIdcardConfidence

        The model defined in huaweicloud sdk

        :param nrc_id: 身份证号码置信度。 
        :type nrc_id: float
        :param issue_date: 签发日期置信度。 
        :type issue_date: float
        :param name: 姓名置信度。 
        :type name: float
        :param birth: 出生日期置信度。 
        :type birth: float
        :param bloodlines_religion: 族群或宗教置信度。 
        :type bloodlines_religion: float
        :param height: 身高置信度。 
        :type height: float
        :param blood_group: 血型置信度。 
        :type blood_group: float
        :param card_id: 身份证的卡号（背面）置信度。 
        :type card_id: float
        :param nrc_id_back: 背面的身份证号码。 
        :type nrc_id_back: float
        :param profession: 职业置信度。 
        :type profession: float
        :param address: 地址置信度。 
        :type address: float
        """
        
        

        self._nrc_id = None
        self._issue_date = None
        self._name = None
        self._birth = None
        self._bloodlines_religion = None
        self._height = None
        self._blood_group = None
        self._card_id = None
        self._nrc_id_back = None
        self._profession = None
        self._address = None
        self.discriminator = None

        if nrc_id is not None:
            self.nrc_id = nrc_id
        if issue_date is not None:
            self.issue_date = issue_date
        if name is not None:
            self.name = name
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

    @property
    def nrc_id(self):
        """Gets the nrc_id of this MyanmarIdcardConfidence.

        身份证号码置信度。 

        :return: The nrc_id of this MyanmarIdcardConfidence.
        :rtype: float
        """
        return self._nrc_id

    @nrc_id.setter
    def nrc_id(self, nrc_id):
        """Sets the nrc_id of this MyanmarIdcardConfidence.

        身份证号码置信度。 

        :param nrc_id: The nrc_id of this MyanmarIdcardConfidence.
        :type nrc_id: float
        """
        self._nrc_id = nrc_id

    @property
    def issue_date(self):
        """Gets the issue_date of this MyanmarIdcardConfidence.

        签发日期置信度。 

        :return: The issue_date of this MyanmarIdcardConfidence.
        :rtype: float
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this MyanmarIdcardConfidence.

        签发日期置信度。 

        :param issue_date: The issue_date of this MyanmarIdcardConfidence.
        :type issue_date: float
        """
        self._issue_date = issue_date

    @property
    def name(self):
        """Gets the name of this MyanmarIdcardConfidence.

        姓名置信度。 

        :return: The name of this MyanmarIdcardConfidence.
        :rtype: float
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MyanmarIdcardConfidence.

        姓名置信度。 

        :param name: The name of this MyanmarIdcardConfidence.
        :type name: float
        """
        self._name = name

    @property
    def birth(self):
        """Gets the birth of this MyanmarIdcardConfidence.

        出生日期置信度。 

        :return: The birth of this MyanmarIdcardConfidence.
        :rtype: float
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this MyanmarIdcardConfidence.

        出生日期置信度。 

        :param birth: The birth of this MyanmarIdcardConfidence.
        :type birth: float
        """
        self._birth = birth

    @property
    def bloodlines_religion(self):
        """Gets the bloodlines_religion of this MyanmarIdcardConfidence.

        族群或宗教置信度。 

        :return: The bloodlines_religion of this MyanmarIdcardConfidence.
        :rtype: float
        """
        return self._bloodlines_religion

    @bloodlines_religion.setter
    def bloodlines_religion(self, bloodlines_religion):
        """Sets the bloodlines_religion of this MyanmarIdcardConfidence.

        族群或宗教置信度。 

        :param bloodlines_religion: The bloodlines_religion of this MyanmarIdcardConfidence.
        :type bloodlines_religion: float
        """
        self._bloodlines_religion = bloodlines_religion

    @property
    def height(self):
        """Gets the height of this MyanmarIdcardConfidence.

        身高置信度。 

        :return: The height of this MyanmarIdcardConfidence.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this MyanmarIdcardConfidence.

        身高置信度。 

        :param height: The height of this MyanmarIdcardConfidence.
        :type height: float
        """
        self._height = height

    @property
    def blood_group(self):
        """Gets the blood_group of this MyanmarIdcardConfidence.

        血型置信度。 

        :return: The blood_group of this MyanmarIdcardConfidence.
        :rtype: float
        """
        return self._blood_group

    @blood_group.setter
    def blood_group(self, blood_group):
        """Sets the blood_group of this MyanmarIdcardConfidence.

        血型置信度。 

        :param blood_group: The blood_group of this MyanmarIdcardConfidence.
        :type blood_group: float
        """
        self._blood_group = blood_group

    @property
    def card_id(self):
        """Gets the card_id of this MyanmarIdcardConfidence.

        身份证的卡号（背面）置信度。 

        :return: The card_id of this MyanmarIdcardConfidence.
        :rtype: float
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this MyanmarIdcardConfidence.

        身份证的卡号（背面）置信度。 

        :param card_id: The card_id of this MyanmarIdcardConfidence.
        :type card_id: float
        """
        self._card_id = card_id

    @property
    def nrc_id_back(self):
        """Gets the nrc_id_back of this MyanmarIdcardConfidence.

        背面的身份证号码。 

        :return: The nrc_id_back of this MyanmarIdcardConfidence.
        :rtype: float
        """
        return self._nrc_id_back

    @nrc_id_back.setter
    def nrc_id_back(self, nrc_id_back):
        """Sets the nrc_id_back of this MyanmarIdcardConfidence.

        背面的身份证号码。 

        :param nrc_id_back: The nrc_id_back of this MyanmarIdcardConfidence.
        :type nrc_id_back: float
        """
        self._nrc_id_back = nrc_id_back

    @property
    def profession(self):
        """Gets the profession of this MyanmarIdcardConfidence.

        职业置信度。 

        :return: The profession of this MyanmarIdcardConfidence.
        :rtype: float
        """
        return self._profession

    @profession.setter
    def profession(self, profession):
        """Sets the profession of this MyanmarIdcardConfidence.

        职业置信度。 

        :param profession: The profession of this MyanmarIdcardConfidence.
        :type profession: float
        """
        self._profession = profession

    @property
    def address(self):
        """Gets the address of this MyanmarIdcardConfidence.

        地址置信度。 

        :return: The address of this MyanmarIdcardConfidence.
        :rtype: float
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MyanmarIdcardConfidence.

        地址置信度。 

        :param address: The address of this MyanmarIdcardConfidence.
        :type address: float
        """
        self._address = address

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
        if not isinstance(other, MyanmarIdcardConfidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
