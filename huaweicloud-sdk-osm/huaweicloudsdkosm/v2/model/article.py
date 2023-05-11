# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Article:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'code': 'str',
        'name': 'str',
        'url': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'product_type_id': 'str',
        'business_type_id': 'str',
        'problem_type_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'url': 'url',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'product_type_id': 'product_type_id',
        'business_type_id': 'business_type_id',
        'problem_type_id': 'problem_type_id'
    }

    def __init__(self, id=None, code=None, name=None, url=None, create_time=None, update_time=None, product_type_id=None, business_type_id=None, problem_type_id=None):
        """Article

        The model defined in huaweicloud sdk

        :param id: 案例Id
        :type id: str
        :param code: 案例编码
        :type code: str
        :param name: 案例名称
        :type name: str
        :param url: 案例链接
        :type url: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param product_type_id: 产品类型Id
        :type product_type_id: str
        :param business_type_id: 业务类型Id
        :type business_type_id: str
        :param problem_type_id: 问题类型Id
        :type problem_type_id: str
        """
        
        

        self._id = None
        self._code = None
        self._name = None
        self._url = None
        self._create_time = None
        self._update_time = None
        self._product_type_id = None
        self._business_type_id = None
        self._problem_type_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if product_type_id is not None:
            self.product_type_id = product_type_id
        if business_type_id is not None:
            self.business_type_id = business_type_id
        if problem_type_id is not None:
            self.problem_type_id = problem_type_id

    @property
    def id(self):
        """Gets the id of this Article.

        案例Id

        :return: The id of this Article.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Article.

        案例Id

        :param id: The id of this Article.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        """Gets the code of this Article.

        案例编码

        :return: The code of this Article.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Article.

        案例编码

        :param code: The code of this Article.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this Article.

        案例名称

        :return: The name of this Article.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Article.

        案例名称

        :param name: The name of this Article.
        :type name: str
        """
        self._name = name

    @property
    def url(self):
        """Gets the url of this Article.

        案例链接

        :return: The url of this Article.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Article.

        案例链接

        :param url: The url of this Article.
        :type url: str
        """
        self._url = url

    @property
    def create_time(self):
        """Gets the create_time of this Article.

        创建时间

        :return: The create_time of this Article.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Article.

        创建时间

        :param create_time: The create_time of this Article.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Article.

        更新时间

        :return: The update_time of this Article.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Article.

        更新时间

        :param update_time: The update_time of this Article.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def product_type_id(self):
        """Gets the product_type_id of this Article.

        产品类型Id

        :return: The product_type_id of this Article.
        :rtype: str
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """Sets the product_type_id of this Article.

        产品类型Id

        :param product_type_id: The product_type_id of this Article.
        :type product_type_id: str
        """
        self._product_type_id = product_type_id

    @property
    def business_type_id(self):
        """Gets the business_type_id of this Article.

        业务类型Id

        :return: The business_type_id of this Article.
        :rtype: str
        """
        return self._business_type_id

    @business_type_id.setter
    def business_type_id(self, business_type_id):
        """Sets the business_type_id of this Article.

        业务类型Id

        :param business_type_id: The business_type_id of this Article.
        :type business_type_id: str
        """
        self._business_type_id = business_type_id

    @property
    def problem_type_id(self):
        """Gets the problem_type_id of this Article.

        问题类型Id

        :return: The problem_type_id of this Article.
        :rtype: str
        """
        return self._problem_type_id

    @problem_type_id.setter
    def problem_type_id(self, problem_type_id):
        """Sets the problem_type_id of this Article.

        问题类型Id

        :param problem_type_id: The problem_type_id of this Article.
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
        if not isinstance(other, Article):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
