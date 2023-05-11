# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchArticlesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top': 'int',
        'product_type_id': 'str',
        'business_type_id': 'str',
        'problem_type_id': 'str'
    }

    attribute_map = {
        'top': 'top',
        'product_type_id': 'product_type_id',
        'business_type_id': 'business_type_id',
        'problem_type_id': 'problem_type_id'
    }

    def __init__(self, top=None, product_type_id=None, business_type_id=None, problem_type_id=None):
        """SearchArticlesReq

        The model defined in huaweicloud sdk

        :param top: 返回匹配度最高的数据条数
        :type top: int
        :param product_type_id: 产品类型Id
        :type product_type_id: str
        :param business_type_id: 业务类型Id
        :type business_type_id: str
        :param problem_type_id: 问题类型Id
        :type problem_type_id: str
        """
        
        

        self._top = None
        self._product_type_id = None
        self._business_type_id = None
        self._problem_type_id = None
        self.discriminator = None

        if top is not None:
            self.top = top
        self.product_type_id = product_type_id
        if business_type_id is not None:
            self.business_type_id = business_type_id
        if problem_type_id is not None:
            self.problem_type_id = problem_type_id

    @property
    def top(self):
        """Gets the top of this SearchArticlesReq.

        返回匹配度最高的数据条数

        :return: The top of this SearchArticlesReq.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this SearchArticlesReq.

        返回匹配度最高的数据条数

        :param top: The top of this SearchArticlesReq.
        :type top: int
        """
        self._top = top

    @property
    def product_type_id(self):
        """Gets the product_type_id of this SearchArticlesReq.

        产品类型Id

        :return: The product_type_id of this SearchArticlesReq.
        :rtype: str
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """Sets the product_type_id of this SearchArticlesReq.

        产品类型Id

        :param product_type_id: The product_type_id of this SearchArticlesReq.
        :type product_type_id: str
        """
        self._product_type_id = product_type_id

    @property
    def business_type_id(self):
        """Gets the business_type_id of this SearchArticlesReq.

        业务类型Id

        :return: The business_type_id of this SearchArticlesReq.
        :rtype: str
        """
        return self._business_type_id

    @business_type_id.setter
    def business_type_id(self, business_type_id):
        """Sets the business_type_id of this SearchArticlesReq.

        业务类型Id

        :param business_type_id: The business_type_id of this SearchArticlesReq.
        :type business_type_id: str
        """
        self._business_type_id = business_type_id

    @property
    def problem_type_id(self):
        """Gets the problem_type_id of this SearchArticlesReq.

        问题类型Id

        :return: The problem_type_id of this SearchArticlesReq.
        :rtype: str
        """
        return self._problem_type_id

    @problem_type_id.setter
    def problem_type_id(self, problem_type_id):
        """Sets the problem_type_id of this SearchArticlesReq.

        问题类型Id

        :param problem_type_id: The problem_type_id of this SearchArticlesReq.
        :type problem_type_id: str
        """
        self._problem_type_id = problem_type_id

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
        if not isinstance(other, SearchArticlesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
