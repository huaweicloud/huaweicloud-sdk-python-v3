# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HouseholdRegisterContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'householder_relationship': 'str',
        'former_name': 'str',
        'sex': 'str',
        'birthplace': 'str',
        'ethnicity': 'str',
        'origin_place': 'str',
        'birth_date': 'str',
        'other_address': 'str',
        'religious_belief': 'str',
        'id_card_number': 'str',
        'height': 'str',
        'blood_type': 'str',
        'education': 'str',
        'marital_status': 'str',
        'military_service_status': 'str',
        'work_place': 'str',
        'occupation': 'str',
        'migrated_to_city': 'str',
        'migrated_to_address': 'str',
        'registrar_signature_seal': 'str',
        'registration_date': 'str',
        'household_type': 'str',
        'household_number': 'str',
        'householder_name': 'str',
        'community': 'str',
        'address': 'str',
        'issue_date': 'str',
        'police_station': 'str'
    }

    attribute_map = {
        'name': 'name',
        'householder_relationship': 'householder_relationship',
        'former_name': 'former_name',
        'sex': 'sex',
        'birthplace': 'birthplace',
        'ethnicity': 'ethnicity',
        'origin_place': 'origin_place',
        'birth_date': 'birth_date',
        'other_address': 'other_address',
        'religious_belief': 'religious_belief',
        'id_card_number': 'id_card_number',
        'height': 'height',
        'blood_type': 'blood_type',
        'education': 'education',
        'marital_status': 'marital_status',
        'military_service_status': 'military_service_status',
        'work_place': 'work_place',
        'occupation': 'occupation',
        'migrated_to_city': 'migrated_to_city',
        'migrated_to_address': 'migrated_to_address',
        'registrar_signature_seal': 'registrar_signature_seal',
        'registration_date': 'registration_date',
        'household_type': 'household_type',
        'household_number': 'household_number',
        'householder_name': 'householder_name',
        'community': 'community',
        'address': 'address',
        'issue_date': 'issue_date',
        'police_station': 'police_station'
    }

    def __init__(self, name=None, householder_relationship=None, former_name=None, sex=None, birthplace=None, ethnicity=None, origin_place=None, birth_date=None, other_address=None, religious_belief=None, id_card_number=None, height=None, blood_type=None, education=None, marital_status=None, military_service_status=None, work_place=None, occupation=None, migrated_to_city=None, migrated_to_address=None, registrar_signature_seal=None, registration_date=None, household_type=None, household_number=None, householder_name=None, community=None, address=None, issue_date=None, police_station=None):
        r"""HouseholdRegisterContent

        The model defined in huaweicloud sdk

        :param name: 姓名。 
        :type name: str
        :param householder_relationship: 户主或与户主关系。 
        :type householder_relationship: str
        :param former_name: 曾用名。 
        :type former_name: str
        :param sex: 性别。 
        :type sex: str
        :param birthplace: 出生地。 
        :type birthplace: str
        :param ethnicity: 民族。 
        :type ethnicity: str
        :param origin_place: 籍贯。 
        :type origin_place: str
        :param birth_date: 出生日期。 
        :type birth_date: str
        :param other_address: 本市(县)其他住址。 
        :type other_address: str
        :param religious_belief: 宗教信仰。 
        :type religious_belief: str
        :param id_card_number: 公民身份证件编号。 
        :type id_card_number: str
        :param height: 身高。 
        :type height: str
        :param blood_type: 血型。 
        :type blood_type: str
        :param education: 文化程度。 
        :type education: str
        :param marital_status: 婚姻状况。   
        :type marital_status: str
        :param military_service_status: 兵役情况。 
        :type military_service_status: str
        :param work_place: 服务处所。 
        :type work_place: str
        :param occupation: 职业。 
        :type occupation: str
        :param migrated_to_city: 何时由何地迁来本市(县)。 
        :type migrated_to_city: str
        :param migrated_to_address: 何时由何地迁来本址。 
        :type migrated_to_address: str
        :param registrar_signature_seal: 承办人签章。 
        :type registrar_signature_seal: str
        :param registration_date: 登记日期。 
        :type registration_date: str
        :param household_type: 户别。 
        :type household_type: str
        :param household_number: 户号。 
        :type household_number: str
        :param householder_name: 户主姓名。当type参数为“首页”时，返回此参数。 
        :type householder_name: str
        :param community: 社区。当type参数为“首页”时，返回此参数。 
        :type community: str
        :param address: 住址。当type参数为“首页”时，返回此参数。 
        :type address: str
        :param issue_date: 签发日期。当type参数为“首页”时，返回此参数。 
        :type issue_date: str
        :param police_station: 户口登记机关。当type参数为“首页”时，返回此参数。 
        :type police_station: str
        """
        
        

        self._name = None
        self._householder_relationship = None
        self._former_name = None
        self._sex = None
        self._birthplace = None
        self._ethnicity = None
        self._origin_place = None
        self._birth_date = None
        self._other_address = None
        self._religious_belief = None
        self._id_card_number = None
        self._height = None
        self._blood_type = None
        self._education = None
        self._marital_status = None
        self._military_service_status = None
        self._work_place = None
        self._occupation = None
        self._migrated_to_city = None
        self._migrated_to_address = None
        self._registrar_signature_seal = None
        self._registration_date = None
        self._household_type = None
        self._household_number = None
        self._householder_name = None
        self._community = None
        self._address = None
        self._issue_date = None
        self._police_station = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if householder_relationship is not None:
            self.householder_relationship = householder_relationship
        if former_name is not None:
            self.former_name = former_name
        if sex is not None:
            self.sex = sex
        if birthplace is not None:
            self.birthplace = birthplace
        if ethnicity is not None:
            self.ethnicity = ethnicity
        if origin_place is not None:
            self.origin_place = origin_place
        if birth_date is not None:
            self.birth_date = birth_date
        if other_address is not None:
            self.other_address = other_address
        if religious_belief is not None:
            self.religious_belief = religious_belief
        if id_card_number is not None:
            self.id_card_number = id_card_number
        if height is not None:
            self.height = height
        if blood_type is not None:
            self.blood_type = blood_type
        if education is not None:
            self.education = education
        if marital_status is not None:
            self.marital_status = marital_status
        if military_service_status is not None:
            self.military_service_status = military_service_status
        if work_place is not None:
            self.work_place = work_place
        if occupation is not None:
            self.occupation = occupation
        if migrated_to_city is not None:
            self.migrated_to_city = migrated_to_city
        if migrated_to_address is not None:
            self.migrated_to_address = migrated_to_address
        if registrar_signature_seal is not None:
            self.registrar_signature_seal = registrar_signature_seal
        if registration_date is not None:
            self.registration_date = registration_date
        if household_type is not None:
            self.household_type = household_type
        if household_number is not None:
            self.household_number = household_number
        if householder_name is not None:
            self.householder_name = householder_name
        if community is not None:
            self.community = community
        if address is not None:
            self.address = address
        if issue_date is not None:
            self.issue_date = issue_date
        if police_station is not None:
            self.police_station = police_station

    @property
    def name(self):
        r"""Gets the name of this HouseholdRegisterContent.

        姓名。 

        :return: The name of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HouseholdRegisterContent.

        姓名。 

        :param name: The name of this HouseholdRegisterContent.
        :type name: str
        """
        self._name = name

    @property
    def householder_relationship(self):
        r"""Gets the householder_relationship of this HouseholdRegisterContent.

        户主或与户主关系。 

        :return: The householder_relationship of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._householder_relationship

    @householder_relationship.setter
    def householder_relationship(self, householder_relationship):
        r"""Sets the householder_relationship of this HouseholdRegisterContent.

        户主或与户主关系。 

        :param householder_relationship: The householder_relationship of this HouseholdRegisterContent.
        :type householder_relationship: str
        """
        self._householder_relationship = householder_relationship

    @property
    def former_name(self):
        r"""Gets the former_name of this HouseholdRegisterContent.

        曾用名。 

        :return: The former_name of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._former_name

    @former_name.setter
    def former_name(self, former_name):
        r"""Sets the former_name of this HouseholdRegisterContent.

        曾用名。 

        :param former_name: The former_name of this HouseholdRegisterContent.
        :type former_name: str
        """
        self._former_name = former_name

    @property
    def sex(self):
        r"""Gets the sex of this HouseholdRegisterContent.

        性别。 

        :return: The sex of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this HouseholdRegisterContent.

        性别。 

        :param sex: The sex of this HouseholdRegisterContent.
        :type sex: str
        """
        self._sex = sex

    @property
    def birthplace(self):
        r"""Gets the birthplace of this HouseholdRegisterContent.

        出生地。 

        :return: The birthplace of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._birthplace

    @birthplace.setter
    def birthplace(self, birthplace):
        r"""Sets the birthplace of this HouseholdRegisterContent.

        出生地。 

        :param birthplace: The birthplace of this HouseholdRegisterContent.
        :type birthplace: str
        """
        self._birthplace = birthplace

    @property
    def ethnicity(self):
        r"""Gets the ethnicity of this HouseholdRegisterContent.

        民族。 

        :return: The ethnicity of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._ethnicity

    @ethnicity.setter
    def ethnicity(self, ethnicity):
        r"""Sets the ethnicity of this HouseholdRegisterContent.

        民族。 

        :param ethnicity: The ethnicity of this HouseholdRegisterContent.
        :type ethnicity: str
        """
        self._ethnicity = ethnicity

    @property
    def origin_place(self):
        r"""Gets the origin_place of this HouseholdRegisterContent.

        籍贯。 

        :return: The origin_place of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._origin_place

    @origin_place.setter
    def origin_place(self, origin_place):
        r"""Sets the origin_place of this HouseholdRegisterContent.

        籍贯。 

        :param origin_place: The origin_place of this HouseholdRegisterContent.
        :type origin_place: str
        """
        self._origin_place = origin_place

    @property
    def birth_date(self):
        r"""Gets the birth_date of this HouseholdRegisterContent.

        出生日期。 

        :return: The birth_date of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        r"""Sets the birth_date of this HouseholdRegisterContent.

        出生日期。 

        :param birth_date: The birth_date of this HouseholdRegisterContent.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def other_address(self):
        r"""Gets the other_address of this HouseholdRegisterContent.

        本市(县)其他住址。 

        :return: The other_address of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._other_address

    @other_address.setter
    def other_address(self, other_address):
        r"""Sets the other_address of this HouseholdRegisterContent.

        本市(县)其他住址。 

        :param other_address: The other_address of this HouseholdRegisterContent.
        :type other_address: str
        """
        self._other_address = other_address

    @property
    def religious_belief(self):
        r"""Gets the religious_belief of this HouseholdRegisterContent.

        宗教信仰。 

        :return: The religious_belief of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._religious_belief

    @religious_belief.setter
    def religious_belief(self, religious_belief):
        r"""Sets the religious_belief of this HouseholdRegisterContent.

        宗教信仰。 

        :param religious_belief: The religious_belief of this HouseholdRegisterContent.
        :type religious_belief: str
        """
        self._religious_belief = religious_belief

    @property
    def id_card_number(self):
        r"""Gets the id_card_number of this HouseholdRegisterContent.

        公民身份证件编号。 

        :return: The id_card_number of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._id_card_number

    @id_card_number.setter
    def id_card_number(self, id_card_number):
        r"""Sets the id_card_number of this HouseholdRegisterContent.

        公民身份证件编号。 

        :param id_card_number: The id_card_number of this HouseholdRegisterContent.
        :type id_card_number: str
        """
        self._id_card_number = id_card_number

    @property
    def height(self):
        r"""Gets the height of this HouseholdRegisterContent.

        身高。 

        :return: The height of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this HouseholdRegisterContent.

        身高。 

        :param height: The height of this HouseholdRegisterContent.
        :type height: str
        """
        self._height = height

    @property
    def blood_type(self):
        r"""Gets the blood_type of this HouseholdRegisterContent.

        血型。 

        :return: The blood_type of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._blood_type

    @blood_type.setter
    def blood_type(self, blood_type):
        r"""Sets the blood_type of this HouseholdRegisterContent.

        血型。 

        :param blood_type: The blood_type of this HouseholdRegisterContent.
        :type blood_type: str
        """
        self._blood_type = blood_type

    @property
    def education(self):
        r"""Gets the education of this HouseholdRegisterContent.

        文化程度。 

        :return: The education of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._education

    @education.setter
    def education(self, education):
        r"""Sets the education of this HouseholdRegisterContent.

        文化程度。 

        :param education: The education of this HouseholdRegisterContent.
        :type education: str
        """
        self._education = education

    @property
    def marital_status(self):
        r"""Gets the marital_status of this HouseholdRegisterContent.

        婚姻状况。   

        :return: The marital_status of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._marital_status

    @marital_status.setter
    def marital_status(self, marital_status):
        r"""Sets the marital_status of this HouseholdRegisterContent.

        婚姻状况。   

        :param marital_status: The marital_status of this HouseholdRegisterContent.
        :type marital_status: str
        """
        self._marital_status = marital_status

    @property
    def military_service_status(self):
        r"""Gets the military_service_status of this HouseholdRegisterContent.

        兵役情况。 

        :return: The military_service_status of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._military_service_status

    @military_service_status.setter
    def military_service_status(self, military_service_status):
        r"""Sets the military_service_status of this HouseholdRegisterContent.

        兵役情况。 

        :param military_service_status: The military_service_status of this HouseholdRegisterContent.
        :type military_service_status: str
        """
        self._military_service_status = military_service_status

    @property
    def work_place(self):
        r"""Gets the work_place of this HouseholdRegisterContent.

        服务处所。 

        :return: The work_place of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._work_place

    @work_place.setter
    def work_place(self, work_place):
        r"""Sets the work_place of this HouseholdRegisterContent.

        服务处所。 

        :param work_place: The work_place of this HouseholdRegisterContent.
        :type work_place: str
        """
        self._work_place = work_place

    @property
    def occupation(self):
        r"""Gets the occupation of this HouseholdRegisterContent.

        职业。 

        :return: The occupation of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        r"""Sets the occupation of this HouseholdRegisterContent.

        职业。 

        :param occupation: The occupation of this HouseholdRegisterContent.
        :type occupation: str
        """
        self._occupation = occupation

    @property
    def migrated_to_city(self):
        r"""Gets the migrated_to_city of this HouseholdRegisterContent.

        何时由何地迁来本市(县)。 

        :return: The migrated_to_city of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._migrated_to_city

    @migrated_to_city.setter
    def migrated_to_city(self, migrated_to_city):
        r"""Sets the migrated_to_city of this HouseholdRegisterContent.

        何时由何地迁来本市(县)。 

        :param migrated_to_city: The migrated_to_city of this HouseholdRegisterContent.
        :type migrated_to_city: str
        """
        self._migrated_to_city = migrated_to_city

    @property
    def migrated_to_address(self):
        r"""Gets the migrated_to_address of this HouseholdRegisterContent.

        何时由何地迁来本址。 

        :return: The migrated_to_address of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._migrated_to_address

    @migrated_to_address.setter
    def migrated_to_address(self, migrated_to_address):
        r"""Sets the migrated_to_address of this HouseholdRegisterContent.

        何时由何地迁来本址。 

        :param migrated_to_address: The migrated_to_address of this HouseholdRegisterContent.
        :type migrated_to_address: str
        """
        self._migrated_to_address = migrated_to_address

    @property
    def registrar_signature_seal(self):
        r"""Gets the registrar_signature_seal of this HouseholdRegisterContent.

        承办人签章。 

        :return: The registrar_signature_seal of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._registrar_signature_seal

    @registrar_signature_seal.setter
    def registrar_signature_seal(self, registrar_signature_seal):
        r"""Sets the registrar_signature_seal of this HouseholdRegisterContent.

        承办人签章。 

        :param registrar_signature_seal: The registrar_signature_seal of this HouseholdRegisterContent.
        :type registrar_signature_seal: str
        """
        self._registrar_signature_seal = registrar_signature_seal

    @property
    def registration_date(self):
        r"""Gets the registration_date of this HouseholdRegisterContent.

        登记日期。 

        :return: The registration_date of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        r"""Sets the registration_date of this HouseholdRegisterContent.

        登记日期。 

        :param registration_date: The registration_date of this HouseholdRegisterContent.
        :type registration_date: str
        """
        self._registration_date = registration_date

    @property
    def household_type(self):
        r"""Gets the household_type of this HouseholdRegisterContent.

        户别。 

        :return: The household_type of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._household_type

    @household_type.setter
    def household_type(self, household_type):
        r"""Sets the household_type of this HouseholdRegisterContent.

        户别。 

        :param household_type: The household_type of this HouseholdRegisterContent.
        :type household_type: str
        """
        self._household_type = household_type

    @property
    def household_number(self):
        r"""Gets the household_number of this HouseholdRegisterContent.

        户号。 

        :return: The household_number of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._household_number

    @household_number.setter
    def household_number(self, household_number):
        r"""Sets the household_number of this HouseholdRegisterContent.

        户号。 

        :param household_number: The household_number of this HouseholdRegisterContent.
        :type household_number: str
        """
        self._household_number = household_number

    @property
    def householder_name(self):
        r"""Gets the householder_name of this HouseholdRegisterContent.

        户主姓名。当type参数为“首页”时，返回此参数。 

        :return: The householder_name of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._householder_name

    @householder_name.setter
    def householder_name(self, householder_name):
        r"""Sets the householder_name of this HouseholdRegisterContent.

        户主姓名。当type参数为“首页”时，返回此参数。 

        :param householder_name: The householder_name of this HouseholdRegisterContent.
        :type householder_name: str
        """
        self._householder_name = householder_name

    @property
    def community(self):
        r"""Gets the community of this HouseholdRegisterContent.

        社区。当type参数为“首页”时，返回此参数。 

        :return: The community of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._community

    @community.setter
    def community(self, community):
        r"""Sets the community of this HouseholdRegisterContent.

        社区。当type参数为“首页”时，返回此参数。 

        :param community: The community of this HouseholdRegisterContent.
        :type community: str
        """
        self._community = community

    @property
    def address(self):
        r"""Gets the address of this HouseholdRegisterContent.

        住址。当type参数为“首页”时，返回此参数。 

        :return: The address of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this HouseholdRegisterContent.

        住址。当type参数为“首页”时，返回此参数。 

        :param address: The address of this HouseholdRegisterContent.
        :type address: str
        """
        self._address = address

    @property
    def issue_date(self):
        r"""Gets the issue_date of this HouseholdRegisterContent.

        签发日期。当type参数为“首页”时，返回此参数。 

        :return: The issue_date of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this HouseholdRegisterContent.

        签发日期。当type参数为“首页”时，返回此参数。 

        :param issue_date: The issue_date of this HouseholdRegisterContent.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def police_station(self):
        r"""Gets the police_station of this HouseholdRegisterContent.

        户口登记机关。当type参数为“首页”时，返回此参数。 

        :return: The police_station of this HouseholdRegisterContent.
        :rtype: str
        """
        return self._police_station

    @police_station.setter
    def police_station(self, police_station):
        r"""Sets the police_station of this HouseholdRegisterContent.

        户口登记机关。当type参数为“首页”时，返回此参数。 

        :param police_station: The police_station of this HouseholdRegisterContent.
        :type police_station: str
        """
        self._police_station = police_station

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
        if not isinstance(other, HouseholdRegisterContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
