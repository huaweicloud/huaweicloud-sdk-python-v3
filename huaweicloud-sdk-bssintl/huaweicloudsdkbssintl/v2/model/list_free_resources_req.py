# coding: utf-8

import pprint
import re

import six





class ListFreeResourcesReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'region_code': 'str',
        'order_id': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'enterprise_project_id': 'str',
        'status': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'region_code': 'region_code',
        'order_id': 'order_id',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'enterprise_project_id': 'enterprise_project_id',
        'status': 'status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, region_code=None, order_id=None, product_id=None, product_name=None, enterprise_project_id=None, status=None, offset=None, limit=None):
        """ListFreeResourcesReq - a model defined in huaweicloud sdk"""
        
        

        self._region_code = None
        self._order_id = None
        self._product_id = None
        self._product_name = None
        self._enterprise_project_id = None
        self._status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if status is not None:
            self.status = status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def region_code(self):
        """Gets the region_code of this ListFreeResourcesReq.

        |参数名称：区域编码| |参数约束及描述：区域编码|

        :return: The region_code of this ListFreeResourcesReq.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this ListFreeResourcesReq.

        |参数名称：区域编码| |参数约束及描述：区域编码|

        :param region_code: The region_code of this ListFreeResourcesReq.
        :type: str
        """
        self._region_code = region_code

    @property
    def order_id(self):
        """Gets the order_id of this ListFreeResourcesReq.

        |参数名称：订单ID| |参数约束及描述：订单ID|

        :return: The order_id of this ListFreeResourcesReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ListFreeResourcesReq.

        |参数名称：订单ID| |参数约束及描述：订单ID|

        :param order_id: The order_id of this ListFreeResourcesReq.
        :type: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this ListFreeResourcesReq.

        |参数名称：产品ID//资源包ID| |参数约束及描述：产品ID//资源包ID|

        :return: The product_id of this ListFreeResourcesReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ListFreeResourcesReq.

        |参数名称：产品ID//资源包ID| |参数约束及描述：产品ID//资源包ID|

        :param product_id: The product_id of this ListFreeResourcesReq.
        :type: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this ListFreeResourcesReq.

        |参数名称：产品名称，即资源包名称| |参数约束及描述：产品名称，即资源包名称|

        :return: The product_name of this ListFreeResourcesReq.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ListFreeResourcesReq.

        |参数名称：产品名称，即资源包名称| |参数约束及描述：产品名称，即资源包名称|

        :param product_name: The product_name of this ListFreeResourcesReq.
        :type: str
        """
        self._product_name = product_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListFreeResourcesReq.

        |参数名称：企业项目ID| |参数约束及描述：企业项目ID|

        :return: The enterprise_project_id of this ListFreeResourcesReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListFreeResourcesReq.

        |参数名称：企业项目ID| |参数约束及描述：企业项目ID|

        :param enterprise_project_id: The enterprise_project_id of this ListFreeResourcesReq.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def status(self):
        """Gets the status of this ListFreeResourcesReq.

        |参数名称：状态| |参数的约束及描述： 0：未生效 1：生效中 2：已用完3：已失效4：已退订|

        :return: The status of this ListFreeResourcesReq.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListFreeResourcesReq.

        |参数名称：状态| |参数的约束及描述： 0：未生效 1：生效中 2：已用完3：已失效4：已退订|

        :param status: The status of this ListFreeResourcesReq.
        :type: int
        """
        self._status = status

    @property
    def offset(self):
        """Gets the offset of this ListFreeResourcesReq.

        |参数名称：偏移量| |参数的约束及描述：从0开始，默认为0|

        :return: The offset of this ListFreeResourcesReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFreeResourcesReq.

        |参数名称：偏移量| |参数的约束及描述：从0开始，默认为0|

        :param offset: The offset of this ListFreeResourcesReq.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListFreeResourcesReq.

        |参数名称：每次查询的记录数| |参数的约束及描述：默认为10|

        :return: The limit of this ListFreeResourcesReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFreeResourcesReq.

        |参数名称：每次查询的记录数| |参数的约束及描述：默认为10|

        :param limit: The limit of this ListFreeResourcesReq.
        :type: int
        """
        self._limit = limit

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListFreeResourcesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other