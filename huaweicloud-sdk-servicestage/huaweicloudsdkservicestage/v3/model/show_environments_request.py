# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEnvironmentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'order_by': 'str',
        'order': 'str',
        'name': 'str',
        'environment_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'order_by': 'order_by',
        'order': 'order',
        'name': 'name',
        'environment_id': 'environment_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, limit=None, offset=None, order_by=None, order=None, name=None, environment_id=None, enterprise_project_id=None):
        r"""ShowEnvironmentsRequest

        The model defined in huaweicloud sdk

        :param limit: 指定个数，明确指定的时候用于分页，取值[0, 100]。不指定的时候表示不分页，最多查询1000条记录。
        :type limit: int
        :param offset: 指定查询偏移量，默认偏移量为0.
        :type offset: int
        :param order_by: 排序字段，默认按创建时间排序。  排序字段支持枚举值：create_time、name、update_time。 
        :type order_by: str
        :param order: desc/asc，默认desc。
        :type order: str
        :param name: 环境名称
        :type name: str
        :param environment_id: 环境id
        :type environment_id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._limit = None
        self._offset = None
        self._order_by = None
        self._order = None
        self._name = None
        self._environment_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order
        if name is not None:
            self.name = name
        if environment_id is not None:
            self.environment_id = environment_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowEnvironmentsRequest.

        指定个数，明确指定的时候用于分页，取值[0, 100]。不指定的时候表示不分页，最多查询1000条记录。

        :return: The limit of this ShowEnvironmentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowEnvironmentsRequest.

        指定个数，明确指定的时候用于分页，取值[0, 100]。不指定的时候表示不分页，最多查询1000条记录。

        :param limit: The limit of this ShowEnvironmentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowEnvironmentsRequest.

        指定查询偏移量，默认偏移量为0.

        :return: The offset of this ShowEnvironmentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowEnvironmentsRequest.

        指定查询偏移量，默认偏移量为0.

        :param offset: The offset of this ShowEnvironmentsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def order_by(self):
        r"""Gets the order_by of this ShowEnvironmentsRequest.

        排序字段，默认按创建时间排序。  排序字段支持枚举值：create_time、name、update_time。 

        :return: The order_by of this ShowEnvironmentsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ShowEnvironmentsRequest.

        排序字段，默认按创建时间排序。  排序字段支持枚举值：create_time、name、update_time。 

        :param order_by: The order_by of this ShowEnvironmentsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        r"""Gets the order of this ShowEnvironmentsRequest.

        desc/asc，默认desc。

        :return: The order of this ShowEnvironmentsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ShowEnvironmentsRequest.

        desc/asc，默认desc。

        :param order: The order of this ShowEnvironmentsRequest.
        :type order: str
        """
        self._order = order

    @property
    def name(self):
        r"""Gets the name of this ShowEnvironmentsRequest.

        环境名称

        :return: The name of this ShowEnvironmentsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowEnvironmentsRequest.

        环境名称

        :param name: The name of this ShowEnvironmentsRequest.
        :type name: str
        """
        self._name = name

    @property
    def environment_id(self):
        r"""Gets the environment_id of this ShowEnvironmentsRequest.

        环境id

        :return: The environment_id of this ShowEnvironmentsRequest.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        r"""Sets the environment_id of this ShowEnvironmentsRequest.

        环境id

        :param environment_id: The environment_id of this ShowEnvironmentsRequest.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowEnvironmentsRequest.

        企业项目id

        :return: The enterprise_project_id of this ShowEnvironmentsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowEnvironmentsRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ShowEnvironmentsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowEnvironmentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
