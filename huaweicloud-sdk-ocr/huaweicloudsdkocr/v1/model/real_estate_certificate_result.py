# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RealEstateCertificateResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issuer': 'str',
        'issue_date': 'str',
        'real_estate_certificate_no': 'str',
        'mortgage_seals': 'int',
        'canceled_mortgage_seals': 'int',
        'estate_location': 'str',
        'total_floors': 'str',
        'floor': 'str',
        'year_built': 'str',
        'structure': 'str',
        'area': 'str',
        'revenue_stamps': 'int',
        'ownership_certificate_no': 'str',
        'estate_holder': 'str',
        'obligee': 'str',
        'ownership': 'str',
        'property_unit_no': 'str',
        'right_type': 'str',
        'right_nature': 'str',
        'usage': 'str',
        'intended_usage': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'issuer': 'issuer',
        'issue_date': 'issue_date',
        'real_estate_certificate_no': 'real_estate_certificate_no',
        'mortgage_seals': 'mortgage_seals',
        'canceled_mortgage_seals': 'canceled_mortgage_seals',
        'estate_location': 'estate_location',
        'total_floors': 'total_floors',
        'floor': 'floor',
        'year_built': 'year_built',
        'structure': 'structure',
        'area': 'area',
        'revenue_stamps': 'revenue_stamps',
        'ownership_certificate_no': 'ownership_certificate_no',
        'estate_holder': 'estate_holder',
        'obligee': 'obligee',
        'ownership': 'ownership',
        'property_unit_no': 'property_unit_no',
        'right_type': 'right_type',
        'right_nature': 'right_nature',
        'usage': 'usage',
        'intended_usage': 'intended_usage',
        'confidence': 'confidence'
    }

    def __init__(self, issuer=None, issue_date=None, real_estate_certificate_no=None, mortgage_seals=None, canceled_mortgage_seals=None, estate_location=None, total_floors=None, floor=None, year_built=None, structure=None, area=None, revenue_stamps=None, ownership_certificate_no=None, estate_holder=None, obligee=None, ownership=None, property_unit_no=None, right_type=None, right_nature=None, usage=None, intended_usage=None, confidence=None):
        r"""RealEstateCertificateResult

        The model defined in huaweicloud sdk

        :param issuer: 填发单位。 
        :type issuer: str
        :param issue_date: 填发日期。 
        :type issue_date: str
        :param real_estate_certificate_no: 不动产证编号。 
        :type real_estate_certificate_no: str
        :param mortgage_seals: 抵押印章个数。 
        :type mortgage_seals: int
        :param canceled_mortgage_seals: 注销的抵押印章个数。 
        :type canceled_mortgage_seals: int
        :param estate_location: 房屋坐落。 
        :type estate_location: str
        :param total_floors: 总楼层数。 
        :type total_floors: str
        :param floor: 所在层。 
        :type floor: str
        :param year_built: 建成年份。 
        :type year_built: str
        :param structure: 结构。 
        :type structure: str
        :param area: 建筑面积。 
        :type area: str
        :param revenue_stamps: 印花税票个数。 
        :type revenue_stamps: int
        :param ownership_certificate_no: 产权证号。 
        :type ownership_certificate_no: str
        :param estate_holder: 房屋所有权人。 
        :type estate_holder: str
        :param obligee: 权利人。 
        :type obligee: str
        :param ownership: 共有情况。 
        :type ownership: str
        :param property_unit_no: 不动产单元号。 
        :type property_unit_no: str
        :param right_type: 权利类型。 
        :type right_type: str
        :param right_nature: 权利性质。 
        :type right_nature: str
        :param usage: 使用用途。 
        :type usage: str
        :param intended_usage: 设计、规划用途。 
        :type intended_usage: str
        :param confidence: 各个字段的置信度。 
        :type confidence: object
        """
        
        

        self._issuer = None
        self._issue_date = None
        self._real_estate_certificate_no = None
        self._mortgage_seals = None
        self._canceled_mortgage_seals = None
        self._estate_location = None
        self._total_floors = None
        self._floor = None
        self._year_built = None
        self._structure = None
        self._area = None
        self._revenue_stamps = None
        self._ownership_certificate_no = None
        self._estate_holder = None
        self._obligee = None
        self._ownership = None
        self._property_unit_no = None
        self._right_type = None
        self._right_nature = None
        self._usage = None
        self._intended_usage = None
        self._confidence = None
        self.discriminator = None

        if issuer is not None:
            self.issuer = issuer
        if issue_date is not None:
            self.issue_date = issue_date
        if real_estate_certificate_no is not None:
            self.real_estate_certificate_no = real_estate_certificate_no
        if mortgage_seals is not None:
            self.mortgage_seals = mortgage_seals
        if canceled_mortgage_seals is not None:
            self.canceled_mortgage_seals = canceled_mortgage_seals
        if estate_location is not None:
            self.estate_location = estate_location
        if total_floors is not None:
            self.total_floors = total_floors
        if floor is not None:
            self.floor = floor
        if year_built is not None:
            self.year_built = year_built
        if structure is not None:
            self.structure = structure
        if area is not None:
            self.area = area
        if revenue_stamps is not None:
            self.revenue_stamps = revenue_stamps
        if ownership_certificate_no is not None:
            self.ownership_certificate_no = ownership_certificate_no
        if estate_holder is not None:
            self.estate_holder = estate_holder
        if obligee is not None:
            self.obligee = obligee
        if ownership is not None:
            self.ownership = ownership
        if property_unit_no is not None:
            self.property_unit_no = property_unit_no
        if right_type is not None:
            self.right_type = right_type
        if right_nature is not None:
            self.right_nature = right_nature
        if usage is not None:
            self.usage = usage
        if intended_usage is not None:
            self.intended_usage = intended_usage
        if confidence is not None:
            self.confidence = confidence

    @property
    def issuer(self):
        r"""Gets the issuer of this RealEstateCertificateResult.

        填发单位。 

        :return: The issuer of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        r"""Sets the issuer of this RealEstateCertificateResult.

        填发单位。 

        :param issuer: The issuer of this RealEstateCertificateResult.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def issue_date(self):
        r"""Gets the issue_date of this RealEstateCertificateResult.

        填发日期。 

        :return: The issue_date of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this RealEstateCertificateResult.

        填发日期。 

        :param issue_date: The issue_date of this RealEstateCertificateResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def real_estate_certificate_no(self):
        r"""Gets the real_estate_certificate_no of this RealEstateCertificateResult.

        不动产证编号。 

        :return: The real_estate_certificate_no of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._real_estate_certificate_no

    @real_estate_certificate_no.setter
    def real_estate_certificate_no(self, real_estate_certificate_no):
        r"""Sets the real_estate_certificate_no of this RealEstateCertificateResult.

        不动产证编号。 

        :param real_estate_certificate_no: The real_estate_certificate_no of this RealEstateCertificateResult.
        :type real_estate_certificate_no: str
        """
        self._real_estate_certificate_no = real_estate_certificate_no

    @property
    def mortgage_seals(self):
        r"""Gets the mortgage_seals of this RealEstateCertificateResult.

        抵押印章个数。 

        :return: The mortgage_seals of this RealEstateCertificateResult.
        :rtype: int
        """
        return self._mortgage_seals

    @mortgage_seals.setter
    def mortgage_seals(self, mortgage_seals):
        r"""Sets the mortgage_seals of this RealEstateCertificateResult.

        抵押印章个数。 

        :param mortgage_seals: The mortgage_seals of this RealEstateCertificateResult.
        :type mortgage_seals: int
        """
        self._mortgage_seals = mortgage_seals

    @property
    def canceled_mortgage_seals(self):
        r"""Gets the canceled_mortgage_seals of this RealEstateCertificateResult.

        注销的抵押印章个数。 

        :return: The canceled_mortgage_seals of this RealEstateCertificateResult.
        :rtype: int
        """
        return self._canceled_mortgage_seals

    @canceled_mortgage_seals.setter
    def canceled_mortgage_seals(self, canceled_mortgage_seals):
        r"""Sets the canceled_mortgage_seals of this RealEstateCertificateResult.

        注销的抵押印章个数。 

        :param canceled_mortgage_seals: The canceled_mortgage_seals of this RealEstateCertificateResult.
        :type canceled_mortgage_seals: int
        """
        self._canceled_mortgage_seals = canceled_mortgage_seals

    @property
    def estate_location(self):
        r"""Gets the estate_location of this RealEstateCertificateResult.

        房屋坐落。 

        :return: The estate_location of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._estate_location

    @estate_location.setter
    def estate_location(self, estate_location):
        r"""Sets the estate_location of this RealEstateCertificateResult.

        房屋坐落。 

        :param estate_location: The estate_location of this RealEstateCertificateResult.
        :type estate_location: str
        """
        self._estate_location = estate_location

    @property
    def total_floors(self):
        r"""Gets the total_floors of this RealEstateCertificateResult.

        总楼层数。 

        :return: The total_floors of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._total_floors

    @total_floors.setter
    def total_floors(self, total_floors):
        r"""Sets the total_floors of this RealEstateCertificateResult.

        总楼层数。 

        :param total_floors: The total_floors of this RealEstateCertificateResult.
        :type total_floors: str
        """
        self._total_floors = total_floors

    @property
    def floor(self):
        r"""Gets the floor of this RealEstateCertificateResult.

        所在层。 

        :return: The floor of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._floor

    @floor.setter
    def floor(self, floor):
        r"""Sets the floor of this RealEstateCertificateResult.

        所在层。 

        :param floor: The floor of this RealEstateCertificateResult.
        :type floor: str
        """
        self._floor = floor

    @property
    def year_built(self):
        r"""Gets the year_built of this RealEstateCertificateResult.

        建成年份。 

        :return: The year_built of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._year_built

    @year_built.setter
    def year_built(self, year_built):
        r"""Sets the year_built of this RealEstateCertificateResult.

        建成年份。 

        :param year_built: The year_built of this RealEstateCertificateResult.
        :type year_built: str
        """
        self._year_built = year_built

    @property
    def structure(self):
        r"""Gets the structure of this RealEstateCertificateResult.

        结构。 

        :return: The structure of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._structure

    @structure.setter
    def structure(self, structure):
        r"""Sets the structure of this RealEstateCertificateResult.

        结构。 

        :param structure: The structure of this RealEstateCertificateResult.
        :type structure: str
        """
        self._structure = structure

    @property
    def area(self):
        r"""Gets the area of this RealEstateCertificateResult.

        建筑面积。 

        :return: The area of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        r"""Sets the area of this RealEstateCertificateResult.

        建筑面积。 

        :param area: The area of this RealEstateCertificateResult.
        :type area: str
        """
        self._area = area

    @property
    def revenue_stamps(self):
        r"""Gets the revenue_stamps of this RealEstateCertificateResult.

        印花税票个数。 

        :return: The revenue_stamps of this RealEstateCertificateResult.
        :rtype: int
        """
        return self._revenue_stamps

    @revenue_stamps.setter
    def revenue_stamps(self, revenue_stamps):
        r"""Sets the revenue_stamps of this RealEstateCertificateResult.

        印花税票个数。 

        :param revenue_stamps: The revenue_stamps of this RealEstateCertificateResult.
        :type revenue_stamps: int
        """
        self._revenue_stamps = revenue_stamps

    @property
    def ownership_certificate_no(self):
        r"""Gets the ownership_certificate_no of this RealEstateCertificateResult.

        产权证号。 

        :return: The ownership_certificate_no of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._ownership_certificate_no

    @ownership_certificate_no.setter
    def ownership_certificate_no(self, ownership_certificate_no):
        r"""Sets the ownership_certificate_no of this RealEstateCertificateResult.

        产权证号。 

        :param ownership_certificate_no: The ownership_certificate_no of this RealEstateCertificateResult.
        :type ownership_certificate_no: str
        """
        self._ownership_certificate_no = ownership_certificate_no

    @property
    def estate_holder(self):
        r"""Gets the estate_holder of this RealEstateCertificateResult.

        房屋所有权人。 

        :return: The estate_holder of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._estate_holder

    @estate_holder.setter
    def estate_holder(self, estate_holder):
        r"""Sets the estate_holder of this RealEstateCertificateResult.

        房屋所有权人。 

        :param estate_holder: The estate_holder of this RealEstateCertificateResult.
        :type estate_holder: str
        """
        self._estate_holder = estate_holder

    @property
    def obligee(self):
        r"""Gets the obligee of this RealEstateCertificateResult.

        权利人。 

        :return: The obligee of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._obligee

    @obligee.setter
    def obligee(self, obligee):
        r"""Sets the obligee of this RealEstateCertificateResult.

        权利人。 

        :param obligee: The obligee of this RealEstateCertificateResult.
        :type obligee: str
        """
        self._obligee = obligee

    @property
    def ownership(self):
        r"""Gets the ownership of this RealEstateCertificateResult.

        共有情况。 

        :return: The ownership of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        r"""Sets the ownership of this RealEstateCertificateResult.

        共有情况。 

        :param ownership: The ownership of this RealEstateCertificateResult.
        :type ownership: str
        """
        self._ownership = ownership

    @property
    def property_unit_no(self):
        r"""Gets the property_unit_no of this RealEstateCertificateResult.

        不动产单元号。 

        :return: The property_unit_no of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._property_unit_no

    @property_unit_no.setter
    def property_unit_no(self, property_unit_no):
        r"""Sets the property_unit_no of this RealEstateCertificateResult.

        不动产单元号。 

        :param property_unit_no: The property_unit_no of this RealEstateCertificateResult.
        :type property_unit_no: str
        """
        self._property_unit_no = property_unit_no

    @property
    def right_type(self):
        r"""Gets the right_type of this RealEstateCertificateResult.

        权利类型。 

        :return: The right_type of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._right_type

    @right_type.setter
    def right_type(self, right_type):
        r"""Sets the right_type of this RealEstateCertificateResult.

        权利类型。 

        :param right_type: The right_type of this RealEstateCertificateResult.
        :type right_type: str
        """
        self._right_type = right_type

    @property
    def right_nature(self):
        r"""Gets the right_nature of this RealEstateCertificateResult.

        权利性质。 

        :return: The right_nature of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._right_nature

    @right_nature.setter
    def right_nature(self, right_nature):
        r"""Sets the right_nature of this RealEstateCertificateResult.

        权利性质。 

        :param right_nature: The right_nature of this RealEstateCertificateResult.
        :type right_nature: str
        """
        self._right_nature = right_nature

    @property
    def usage(self):
        r"""Gets the usage of this RealEstateCertificateResult.

        使用用途。 

        :return: The usage of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this RealEstateCertificateResult.

        使用用途。 

        :param usage: The usage of this RealEstateCertificateResult.
        :type usage: str
        """
        self._usage = usage

    @property
    def intended_usage(self):
        r"""Gets the intended_usage of this RealEstateCertificateResult.

        设计、规划用途。 

        :return: The intended_usage of this RealEstateCertificateResult.
        :rtype: str
        """
        return self._intended_usage

    @intended_usage.setter
    def intended_usage(self, intended_usage):
        r"""Sets the intended_usage of this RealEstateCertificateResult.

        设计、规划用途。 

        :param intended_usage: The intended_usage of this RealEstateCertificateResult.
        :type intended_usage: str
        """
        self._intended_usage = intended_usage

    @property
    def confidence(self):
        r"""Gets the confidence of this RealEstateCertificateResult.

        各个字段的置信度。 

        :return: The confidence of this RealEstateCertificateResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this RealEstateCertificateResult.

        各个字段的置信度。 

        :param confidence: The confidence of this RealEstateCertificateResult.
        :type confidence: object
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
        if not isinstance(other, RealEstateCertificateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
