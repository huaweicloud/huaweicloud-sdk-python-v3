# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventForensicInfoAbnormalLoginForensic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'user': 'str',
        'country': 'str',
        'sub_division': 'str',
        'city': 'str',
        'city_id': 'int'
    }

    attribute_map = {
        'ip': 'ip',
        'user': 'user',
        'country': 'country',
        'sub_division': 'sub_division',
        'city': 'city',
        'city_id': 'city_id'
    }

    def __init__(self, ip=None, user=None, country=None, sub_division=None, city=None, city_id=None):
        r"""EventForensicInfoAbnormalLoginForensic

        The model defined in huaweicloud sdk

        :param ip: **参数解释**： IP **取值范围**： 不涉及
        :type ip: str
        :param user: **参数解释**： 用户 **取值范围**： 不涉及
        :type user: str
        :param country: **参数解释**： 国家 **取值范围**： 不涉及
        :type country: str
        :param sub_division: **参数解释**： 省份 **取值范围**： 不涉及
        :type sub_division: str
        :param city: **参数解释**： 城市 **取值范围**： 不涉及
        :type city: str
        :param city_id: **参数解释**： 登录源（映射地名） **取值范围**： 不涉及
        :type city_id: int
        """
        
        

        self._ip = None
        self._user = None
        self._country = None
        self._sub_division = None
        self._city = None
        self._city_id = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if user is not None:
            self.user = user
        if country is not None:
            self.country = country
        if sub_division is not None:
            self.sub_division = sub_division
        if city is not None:
            self.city = city
        if city_id is not None:
            self.city_id = city_id

    @property
    def ip(self):
        r"""Gets the ip of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： IP **取值范围**： 不涉及

        :return: The ip of this EventForensicInfoAbnormalLoginForensic.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： IP **取值范围**： 不涉及

        :param ip: The ip of this EventForensicInfoAbnormalLoginForensic.
        :type ip: str
        """
        self._ip = ip

    @property
    def user(self):
        r"""Gets the user of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： 用户 **取值范围**： 不涉及

        :return: The user of this EventForensicInfoAbnormalLoginForensic.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： 用户 **取值范围**： 不涉及

        :param user: The user of this EventForensicInfoAbnormalLoginForensic.
        :type user: str
        """
        self._user = user

    @property
    def country(self):
        r"""Gets the country of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： 国家 **取值范围**： 不涉及

        :return: The country of this EventForensicInfoAbnormalLoginForensic.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： 国家 **取值范围**： 不涉及

        :param country: The country of this EventForensicInfoAbnormalLoginForensic.
        :type country: str
        """
        self._country = country

    @property
    def sub_division(self):
        r"""Gets the sub_division of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： 省份 **取值范围**： 不涉及

        :return: The sub_division of this EventForensicInfoAbnormalLoginForensic.
        :rtype: str
        """
        return self._sub_division

    @sub_division.setter
    def sub_division(self, sub_division):
        r"""Sets the sub_division of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： 省份 **取值范围**： 不涉及

        :param sub_division: The sub_division of this EventForensicInfoAbnormalLoginForensic.
        :type sub_division: str
        """
        self._sub_division = sub_division

    @property
    def city(self):
        r"""Gets the city of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： 城市 **取值范围**： 不涉及

        :return: The city of this EventForensicInfoAbnormalLoginForensic.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： 城市 **取值范围**： 不涉及

        :param city: The city of this EventForensicInfoAbnormalLoginForensic.
        :type city: str
        """
        self._city = city

    @property
    def city_id(self):
        r"""Gets the city_id of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： 登录源（映射地名） **取值范围**： 不涉及

        :return: The city_id of this EventForensicInfoAbnormalLoginForensic.
        :rtype: int
        """
        return self._city_id

    @city_id.setter
    def city_id(self, city_id):
        r"""Sets the city_id of this EventForensicInfoAbnormalLoginForensic.

        **参数解释**： 登录源（映射地名） **取值范围**： 不涉及

        :param city_id: The city_id of this EventForensicInfoAbnormalLoginForensic.
        :type city_id: int
        """
        self._city_id = city_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventForensicInfoAbnormalLoginForensic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
