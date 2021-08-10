# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCustomerMonthlySumRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bill_cycle': 'str',
        'service_type_code': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'method': 'str',
        'sub_customer_id': 'str'
    }

    attribute_map = {
        'bill_cycle': 'bill_cycle',
        'service_type_code': 'service_type_code',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'method': 'method',
        'sub_customer_id': 'sub_customer_id'
    }

    def __init__(self, bill_cycle=None, service_type_code=None, enterprise_project_id=None, offset=None, limit=None, method=None, sub_customer_id=None):
        """ShowCustomerMonthlySumRequest - a model defined in huaweicloud sdk"""
        
        

        self._bill_cycle = None
        self._service_type_code = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._method = None
        self._sub_customer_id = None
        self.discriminator = None

        self.bill_cycle = bill_cycle
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if method is not None:
            self.method = method
        if sub_customer_id is not None:
            self.sub_customer_id = sub_customer_id

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this ShowCustomerMonthlySumRequest.

        |参数名称：消费时间，格式：yyyy-MM| |参数的约束及描述：|

        :return: The bill_cycle of this ShowCustomerMonthlySumRequest.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this ShowCustomerMonthlySumRequest.

        |参数名称：消费时间，格式：yyyy-MM| |参数的约束及描述：|

        :param bill_cycle: The bill_cycle of this ShowCustomerMonthlySumRequest.
        :type: str
        """
        self._bill_cycle = bill_cycle

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ShowCustomerMonthlySumRequest.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型| |参数的约束及描述：|

        :return: The service_type_code of this ShowCustomerMonthlySumRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ShowCustomerMonthlySumRequest.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型| |参数的约束及描述：|

        :param service_type_code: The service_type_code of this ShowCustomerMonthlySumRequest.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowCustomerMonthlySumRequest.

        |参数名称：企业项目ID。获取方法请参见如何获取企业项目ID。| |参数的约束及描述：|

        :return: The enterprise_project_id of this ShowCustomerMonthlySumRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowCustomerMonthlySumRequest.

        |参数名称：企业项目ID。获取方法请参见如何获取企业项目ID。| |参数的约束及描述：|

        :param enterprise_project_id: The enterprise_project_id of this ShowCustomerMonthlySumRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ShowCustomerMonthlySumRequest.

        |参数名称：偏移量，从0开始，默认为0| |参数的约束及描述：|

        :return: The offset of this ShowCustomerMonthlySumRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowCustomerMonthlySumRequest.

        |参数名称：偏移量，从0开始，默认为0| |参数的约束及描述：|

        :param offset: The offset of this ShowCustomerMonthlySumRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowCustomerMonthlySumRequest.

        |参数名称：每次查询的数量，默认为10| |参数的约束及描述：|

        :return: The limit of this ShowCustomerMonthlySumRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowCustomerMonthlySumRequest.

        |参数名称：每次查询的数量，默认为10| |参数的约束及描述：|

        :param limit: The limit of this ShowCustomerMonthlySumRequest.
        :type: int
        """
        self._limit = limit

    @property
    def method(self):
        """Gets the method of this ShowCustomerMonthlySumRequest.

        |参数名称：查询方式。oneself：自身sub_customer: 企业子客户all:自己和企业子客户| |参数的约束及描述：oneself：自身sub_customer: 企业子客户all:自己和企业子客户|

        :return: The method of this ShowCustomerMonthlySumRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ShowCustomerMonthlySumRequest.

        |参数名称：查询方式。oneself：自身sub_customer: 企业子客户all:自己和企业子客户| |参数的约束及描述：oneself：自身sub_customer: 企业子客户all:自己和企业子客户|

        :param method: The method of this ShowCustomerMonthlySumRequest.
        :type: str
        """
        self._method = method

    @property
    def sub_customer_id(self):
        """Gets the sub_customer_id of this ShowCustomerMonthlySumRequest.

        |参数名称：企业子账号ID。| |参数的约束及描述：注意：method不等于sub_customer的时候，该参数无效，如果method等于sub_customer，该参数不能为空|

        :return: The sub_customer_id of this ShowCustomerMonthlySumRequest.
        :rtype: str
        """
        return self._sub_customer_id

    @sub_customer_id.setter
    def sub_customer_id(self, sub_customer_id):
        """Sets the sub_customer_id of this ShowCustomerMonthlySumRequest.

        |参数名称：企业子账号ID。| |参数的约束及描述：注意：method不等于sub_customer的时候，该参数无效，如果method等于sub_customer，该参数不能为空|

        :param sub_customer_id: The sub_customer_id of this ShowCustomerMonthlySumRequest.
        :type: str
        """
        self._sub_customer_id = sub_customer_id

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
        if not isinstance(other, ShowCustomerMonthlySumRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
