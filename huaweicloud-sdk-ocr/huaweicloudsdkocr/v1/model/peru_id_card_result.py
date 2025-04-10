# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeruIdCardResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cui_number': 'str',
        'first_surname': 'str',
        'second_surname': 'str',
        'given_name': 'str',
        'sex': 'str',
        'marital_status': 'str',
        'birth_date': 'str',
        'nationality': 'str',
        'issue_date': 'str',
        'expiry_date': 'str',
        'birth_place': 'str',
        'voting_group': 'str',
        'organ_donation': 'str',
        'registration_date': 'str',
        'portrait_image': 'str',
        'portrait_location': 'list[list[int]]',
        'address': 'str',
        'department': 'str',
        'province': 'str',
        'district': 'str',
        'remarks': 'str',
        'machine_code1': 'str',
        'machine_code2': 'str',
        'machine_code3': 'str',
        'duplicate': 'bool',
        'confidence': 'dict(str, float)'
    }

    attribute_map = {
        'cui_number': 'cui_number',
        'first_surname': 'first_surname',
        'second_surname': 'second_surname',
        'given_name': 'given_name',
        'sex': 'sex',
        'marital_status': 'marital_status',
        'birth_date': 'birth_date',
        'nationality': 'nationality',
        'issue_date': 'issue_date',
        'expiry_date': 'expiry_date',
        'birth_place': 'birth_place',
        'voting_group': 'voting_group',
        'organ_donation': 'organ_donation',
        'registration_date': 'registration_date',
        'portrait_image': 'portrait_image',
        'portrait_location': 'portrait_location',
        'address': 'address',
        'department': 'department',
        'province': 'province',
        'district': 'district',
        'remarks': 'remarks',
        'machine_code1': 'machine_code1',
        'machine_code2': 'machine_code2',
        'machine_code3': 'machine_code3',
        'duplicate': 'duplicate',
        'confidence': 'confidence'
    }

    def __init__(self, cui_number=None, first_surname=None, second_surname=None, given_name=None, sex=None, marital_status=None, birth_date=None, nationality=None, issue_date=None, expiry_date=None, birth_place=None, voting_group=None, organ_donation=None, registration_date=None, portrait_image=None, portrait_location=None, address=None, department=None, province=None, district=None, remarks=None, machine_code1=None, machine_code2=None, machine_code3=None, duplicate=None, confidence=None):
        r"""PeruIdCardResult

        The model defined in huaweicloud sdk

        :param cui_number: 身份证号。
        :type cui_number: str
        :param first_surname: 第一姓氏。
        :type first_surname: str
        :param second_surname: 第二姓氏。
        :type second_surname: str
        :param given_name: 名。
        :type given_name: str
        :param sex: 性别。
        :type sex: str
        :param marital_status: 婚姻状况。
        :type marital_status: str
        :param birth_date: 出生日期。
        :type birth_date: str
        :param nationality: 国籍。
        :type nationality: str
        :param issue_date: 发行日期。
        :type issue_date: str
        :param expiry_date: 失效日期。
        :type expiry_date: str
        :param birth_place: 出生地编码。
        :type birth_place: str
        :param voting_group: 投票组。
        :type voting_group: str
        :param organ_donation: 器官捐赠意愿。
        :type organ_donation: str
        :param registration_date: 注册日期。
        :type registration_date: str
        :param portrait_image: 头像的base64编码。当输入参数“return_portrait_image”为“true”时，才返回该参数。
        :type portrait_image: str
        :param portrait_location: 头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type portrait_location: list[list[int]]
        :param address: 地址。
        :type address: str
        :param department: 大区。
        :type department: str
        :param province: 省。
        :type province: str
        :param district: 区。
        :type district: str
        :param remarks: 备注。
        :type remarks: str
        :param machine_code1: 机器码第一行。
        :type machine_code1: str
        :param machine_code2: 机器码第二行。
        :type machine_code2: str
        :param machine_code3: 机器码第三行。
        :type machine_code3: str
        :param duplicate: 是否重新登记过。可选值如下所示： -  true: 已重新登记过 -  false: 未重新登记过 
        :type duplicate: bool
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。
        :type confidence: dict(str, float)
        """
        
        

        self._cui_number = None
        self._first_surname = None
        self._second_surname = None
        self._given_name = None
        self._sex = None
        self._marital_status = None
        self._birth_date = None
        self._nationality = None
        self._issue_date = None
        self._expiry_date = None
        self._birth_place = None
        self._voting_group = None
        self._organ_donation = None
        self._registration_date = None
        self._portrait_image = None
        self._portrait_location = None
        self._address = None
        self._department = None
        self._province = None
        self._district = None
        self._remarks = None
        self._machine_code1 = None
        self._machine_code2 = None
        self._machine_code3 = None
        self._duplicate = None
        self._confidence = None
        self.discriminator = None

        if cui_number is not None:
            self.cui_number = cui_number
        if first_surname is not None:
            self.first_surname = first_surname
        if second_surname is not None:
            self.second_surname = second_surname
        if given_name is not None:
            self.given_name = given_name
        if sex is not None:
            self.sex = sex
        if marital_status is not None:
            self.marital_status = marital_status
        if birth_date is not None:
            self.birth_date = birth_date
        if nationality is not None:
            self.nationality = nationality
        if issue_date is not None:
            self.issue_date = issue_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if birth_place is not None:
            self.birth_place = birth_place
        if voting_group is not None:
            self.voting_group = voting_group
        if organ_donation is not None:
            self.organ_donation = organ_donation
        if registration_date is not None:
            self.registration_date = registration_date
        if portrait_image is not None:
            self.portrait_image = portrait_image
        if portrait_location is not None:
            self.portrait_location = portrait_location
        if address is not None:
            self.address = address
        if department is not None:
            self.department = department
        if province is not None:
            self.province = province
        if district is not None:
            self.district = district
        if remarks is not None:
            self.remarks = remarks
        if machine_code1 is not None:
            self.machine_code1 = machine_code1
        if machine_code2 is not None:
            self.machine_code2 = machine_code2
        if machine_code3 is not None:
            self.machine_code3 = machine_code3
        if duplicate is not None:
            self.duplicate = duplicate
        if confidence is not None:
            self.confidence = confidence

    @property
    def cui_number(self):
        r"""Gets the cui_number of this PeruIdCardResult.

        身份证号。

        :return: The cui_number of this PeruIdCardResult.
        :rtype: str
        """
        return self._cui_number

    @cui_number.setter
    def cui_number(self, cui_number):
        r"""Sets the cui_number of this PeruIdCardResult.

        身份证号。

        :param cui_number: The cui_number of this PeruIdCardResult.
        :type cui_number: str
        """
        self._cui_number = cui_number

    @property
    def first_surname(self):
        r"""Gets the first_surname of this PeruIdCardResult.

        第一姓氏。

        :return: The first_surname of this PeruIdCardResult.
        :rtype: str
        """
        return self._first_surname

    @first_surname.setter
    def first_surname(self, first_surname):
        r"""Sets the first_surname of this PeruIdCardResult.

        第一姓氏。

        :param first_surname: The first_surname of this PeruIdCardResult.
        :type first_surname: str
        """
        self._first_surname = first_surname

    @property
    def second_surname(self):
        r"""Gets the second_surname of this PeruIdCardResult.

        第二姓氏。

        :return: The second_surname of this PeruIdCardResult.
        :rtype: str
        """
        return self._second_surname

    @second_surname.setter
    def second_surname(self, second_surname):
        r"""Sets the second_surname of this PeruIdCardResult.

        第二姓氏。

        :param second_surname: The second_surname of this PeruIdCardResult.
        :type second_surname: str
        """
        self._second_surname = second_surname

    @property
    def given_name(self):
        r"""Gets the given_name of this PeruIdCardResult.

        名。

        :return: The given_name of this PeruIdCardResult.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        r"""Sets the given_name of this PeruIdCardResult.

        名。

        :param given_name: The given_name of this PeruIdCardResult.
        :type given_name: str
        """
        self._given_name = given_name

    @property
    def sex(self):
        r"""Gets the sex of this PeruIdCardResult.

        性别。

        :return: The sex of this PeruIdCardResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this PeruIdCardResult.

        性别。

        :param sex: The sex of this PeruIdCardResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def marital_status(self):
        r"""Gets the marital_status of this PeruIdCardResult.

        婚姻状况。

        :return: The marital_status of this PeruIdCardResult.
        :rtype: str
        """
        return self._marital_status

    @marital_status.setter
    def marital_status(self, marital_status):
        r"""Sets the marital_status of this PeruIdCardResult.

        婚姻状况。

        :param marital_status: The marital_status of this PeruIdCardResult.
        :type marital_status: str
        """
        self._marital_status = marital_status

    @property
    def birth_date(self):
        r"""Gets the birth_date of this PeruIdCardResult.

        出生日期。

        :return: The birth_date of this PeruIdCardResult.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        r"""Sets the birth_date of this PeruIdCardResult.

        出生日期。

        :param birth_date: The birth_date of this PeruIdCardResult.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def nationality(self):
        r"""Gets the nationality of this PeruIdCardResult.

        国籍。

        :return: The nationality of this PeruIdCardResult.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        r"""Sets the nationality of this PeruIdCardResult.

        国籍。

        :param nationality: The nationality of this PeruIdCardResult.
        :type nationality: str
        """
        self._nationality = nationality

    @property
    def issue_date(self):
        r"""Gets the issue_date of this PeruIdCardResult.

        发行日期。

        :return: The issue_date of this PeruIdCardResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this PeruIdCardResult.

        发行日期。

        :param issue_date: The issue_date of this PeruIdCardResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def expiry_date(self):
        r"""Gets the expiry_date of this PeruIdCardResult.

        失效日期。

        :return: The expiry_date of this PeruIdCardResult.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        r"""Sets the expiry_date of this PeruIdCardResult.

        失效日期。

        :param expiry_date: The expiry_date of this PeruIdCardResult.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

    @property
    def birth_place(self):
        r"""Gets the birth_place of this PeruIdCardResult.

        出生地编码。

        :return: The birth_place of this PeruIdCardResult.
        :rtype: str
        """
        return self._birth_place

    @birth_place.setter
    def birth_place(self, birth_place):
        r"""Sets the birth_place of this PeruIdCardResult.

        出生地编码。

        :param birth_place: The birth_place of this PeruIdCardResult.
        :type birth_place: str
        """
        self._birth_place = birth_place

    @property
    def voting_group(self):
        r"""Gets the voting_group of this PeruIdCardResult.

        投票组。

        :return: The voting_group of this PeruIdCardResult.
        :rtype: str
        """
        return self._voting_group

    @voting_group.setter
    def voting_group(self, voting_group):
        r"""Sets the voting_group of this PeruIdCardResult.

        投票组。

        :param voting_group: The voting_group of this PeruIdCardResult.
        :type voting_group: str
        """
        self._voting_group = voting_group

    @property
    def organ_donation(self):
        r"""Gets the organ_donation of this PeruIdCardResult.

        器官捐赠意愿。

        :return: The organ_donation of this PeruIdCardResult.
        :rtype: str
        """
        return self._organ_donation

    @organ_donation.setter
    def organ_donation(self, organ_donation):
        r"""Sets the organ_donation of this PeruIdCardResult.

        器官捐赠意愿。

        :param organ_donation: The organ_donation of this PeruIdCardResult.
        :type organ_donation: str
        """
        self._organ_donation = organ_donation

    @property
    def registration_date(self):
        r"""Gets the registration_date of this PeruIdCardResult.

        注册日期。

        :return: The registration_date of this PeruIdCardResult.
        :rtype: str
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        r"""Sets the registration_date of this PeruIdCardResult.

        注册日期。

        :param registration_date: The registration_date of this PeruIdCardResult.
        :type registration_date: str
        """
        self._registration_date = registration_date

    @property
    def portrait_image(self):
        r"""Gets the portrait_image of this PeruIdCardResult.

        头像的base64编码。当输入参数“return_portrait_image”为“true”时，才返回该参数。

        :return: The portrait_image of this PeruIdCardResult.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        r"""Sets the portrait_image of this PeruIdCardResult.

        头像的base64编码。当输入参数“return_portrait_image”为“true”时，才返回该参数。

        :param portrait_image: The portrait_image of this PeruIdCardResult.
        :type portrait_image: str
        """
        self._portrait_image = portrait_image

    @property
    def portrait_location(self):
        r"""Gets the portrait_location of this PeruIdCardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The portrait_location of this PeruIdCardResult.
        :rtype: list[list[int]]
        """
        return self._portrait_location

    @portrait_location.setter
    def portrait_location(self, portrait_location):
        r"""Sets the portrait_location of this PeruIdCardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param portrait_location: The portrait_location of this PeruIdCardResult.
        :type portrait_location: list[list[int]]
        """
        self._portrait_location = portrait_location

    @property
    def address(self):
        r"""Gets the address of this PeruIdCardResult.

        地址。

        :return: The address of this PeruIdCardResult.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this PeruIdCardResult.

        地址。

        :param address: The address of this PeruIdCardResult.
        :type address: str
        """
        self._address = address

    @property
    def department(self):
        r"""Gets the department of this PeruIdCardResult.

        大区。

        :return: The department of this PeruIdCardResult.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        r"""Sets the department of this PeruIdCardResult.

        大区。

        :param department: The department of this PeruIdCardResult.
        :type department: str
        """
        self._department = department

    @property
    def province(self):
        r"""Gets the province of this PeruIdCardResult.

        省。

        :return: The province of this PeruIdCardResult.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this PeruIdCardResult.

        省。

        :param province: The province of this PeruIdCardResult.
        :type province: str
        """
        self._province = province

    @property
    def district(self):
        r"""Gets the district of this PeruIdCardResult.

        区。

        :return: The district of this PeruIdCardResult.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        r"""Sets the district of this PeruIdCardResult.

        区。

        :param district: The district of this PeruIdCardResult.
        :type district: str
        """
        self._district = district

    @property
    def remarks(self):
        r"""Gets the remarks of this PeruIdCardResult.

        备注。

        :return: The remarks of this PeruIdCardResult.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this PeruIdCardResult.

        备注。

        :param remarks: The remarks of this PeruIdCardResult.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def machine_code1(self):
        r"""Gets the machine_code1 of this PeruIdCardResult.

        机器码第一行。

        :return: The machine_code1 of this PeruIdCardResult.
        :rtype: str
        """
        return self._machine_code1

    @machine_code1.setter
    def machine_code1(self, machine_code1):
        r"""Sets the machine_code1 of this PeruIdCardResult.

        机器码第一行。

        :param machine_code1: The machine_code1 of this PeruIdCardResult.
        :type machine_code1: str
        """
        self._machine_code1 = machine_code1

    @property
    def machine_code2(self):
        r"""Gets the machine_code2 of this PeruIdCardResult.

        机器码第二行。

        :return: The machine_code2 of this PeruIdCardResult.
        :rtype: str
        """
        return self._machine_code2

    @machine_code2.setter
    def machine_code2(self, machine_code2):
        r"""Sets the machine_code2 of this PeruIdCardResult.

        机器码第二行。

        :param machine_code2: The machine_code2 of this PeruIdCardResult.
        :type machine_code2: str
        """
        self._machine_code2 = machine_code2

    @property
    def machine_code3(self):
        r"""Gets the machine_code3 of this PeruIdCardResult.

        机器码第三行。

        :return: The machine_code3 of this PeruIdCardResult.
        :rtype: str
        """
        return self._machine_code3

    @machine_code3.setter
    def machine_code3(self, machine_code3):
        r"""Sets the machine_code3 of this PeruIdCardResult.

        机器码第三行。

        :param machine_code3: The machine_code3 of this PeruIdCardResult.
        :type machine_code3: str
        """
        self._machine_code3 = machine_code3

    @property
    def duplicate(self):
        r"""Gets the duplicate of this PeruIdCardResult.

        是否重新登记过。可选值如下所示： -  true: 已重新登记过 -  false: 未重新登记过 

        :return: The duplicate of this PeruIdCardResult.
        :rtype: bool
        """
        return self._duplicate

    @duplicate.setter
    def duplicate(self, duplicate):
        r"""Sets the duplicate of this PeruIdCardResult.

        是否重新登记过。可选值如下所示： -  true: 已重新登记过 -  false: 未重新登记过 

        :param duplicate: The duplicate of this PeruIdCardResult.
        :type duplicate: bool
        """
        self._duplicate = duplicate

    @property
    def confidence(self):
        r"""Gets the confidence of this PeruIdCardResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。

        :return: The confidence of this PeruIdCardResult.
        :rtype: dict(str, float)
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this PeruIdCardResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。注：置信度由算法给出，不直接等价于对应字段的准确率。

        :param confidence: The confidence of this PeruIdCardResult.
        :type confidence: dict(str, float)
        """
        self._confidence = confidence

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
        if not isinstance(other, PeruIdCardResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
