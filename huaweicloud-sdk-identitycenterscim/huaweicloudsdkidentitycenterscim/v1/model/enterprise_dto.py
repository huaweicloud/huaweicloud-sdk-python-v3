# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnterpriseDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cost_center': 'str',
        'department': 'str',
        'division': 'str',
        'employee_number': 'str',
        'manager': 'ManagerDto',
        'organization': 'str'
    }

    attribute_map = {
        'cost_center': 'costCenter',
        'department': 'department',
        'division': 'division',
        'employee_number': 'employeeNumber',
        'manager': 'manager',
        'organization': 'organization'
    }

    def __init__(self, cost_center=None, department=None, division=None, employee_number=None, manager=None, organization=None):
        r"""EnterpriseDto

        The model defined in huaweicloud sdk

        :param cost_center: 成本中心
        :type cost_center: str
        :param department: 部门
        :type department: str
        :param division: 分部
        :type division: str
        :param employee_number: 员工编号
        :type employee_number: str
        :param manager: 
        :type manager: :class:`huaweicloudsdkidentitycenterscim.v1.ManagerDto`
        :param organization: 组织
        :type organization: str
        """
        
        

        self._cost_center = None
        self._department = None
        self._division = None
        self._employee_number = None
        self._manager = None
        self._organization = None
        self.discriminator = None

        if cost_center is not None:
            self.cost_center = cost_center
        if department is not None:
            self.department = department
        if division is not None:
            self.division = division
        if employee_number is not None:
            self.employee_number = employee_number
        if manager is not None:
            self.manager = manager
        if organization is not None:
            self.organization = organization

    @property
    def cost_center(self):
        r"""Gets the cost_center of this EnterpriseDto.

        成本中心

        :return: The cost_center of this EnterpriseDto.
        :rtype: str
        """
        return self._cost_center

    @cost_center.setter
    def cost_center(self, cost_center):
        r"""Sets the cost_center of this EnterpriseDto.

        成本中心

        :param cost_center: The cost_center of this EnterpriseDto.
        :type cost_center: str
        """
        self._cost_center = cost_center

    @property
    def department(self):
        r"""Gets the department of this EnterpriseDto.

        部门

        :return: The department of this EnterpriseDto.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        r"""Sets the department of this EnterpriseDto.

        部门

        :param department: The department of this EnterpriseDto.
        :type department: str
        """
        self._department = department

    @property
    def division(self):
        r"""Gets the division of this EnterpriseDto.

        分部

        :return: The division of this EnterpriseDto.
        :rtype: str
        """
        return self._division

    @division.setter
    def division(self, division):
        r"""Sets the division of this EnterpriseDto.

        分部

        :param division: The division of this EnterpriseDto.
        :type division: str
        """
        self._division = division

    @property
    def employee_number(self):
        r"""Gets the employee_number of this EnterpriseDto.

        员工编号

        :return: The employee_number of this EnterpriseDto.
        :rtype: str
        """
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        r"""Sets the employee_number of this EnterpriseDto.

        员工编号

        :param employee_number: The employee_number of this EnterpriseDto.
        :type employee_number: str
        """
        self._employee_number = employee_number

    @property
    def manager(self):
        r"""Gets the manager of this EnterpriseDto.

        :return: The manager of this EnterpriseDto.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.ManagerDto`
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        r"""Sets the manager of this EnterpriseDto.

        :param manager: The manager of this EnterpriseDto.
        :type manager: :class:`huaweicloudsdkidentitycenterscim.v1.ManagerDto`
        """
        self._manager = manager

    @property
    def organization(self):
        r"""Gets the organization of this EnterpriseDto.

        组织

        :return: The organization of this EnterpriseDto.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        r"""Sets the organization of this EnterpriseDto.

        组织

        :param organization: The organization of this EnterpriseDto.
        :type organization: str
        """
        self._organization = organization

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
        if not isinstance(other, EnterpriseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
