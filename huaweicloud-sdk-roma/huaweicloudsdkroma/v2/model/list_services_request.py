# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServicesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'limit': 'int',
        'service_id': 'int',
        'service_name': 'str',
        'product_template_id': 'int',
        'product_id': 'int',
        'created_user_name': 'str',
        'created_date_start': 'int',
        'created_date_end': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'service_id': 'service_id',
        'service_name': 'service_name',
        'product_template_id': 'product_template_id',
        'product_id': 'product_id',
        'created_user_name': 'created_user_name',
        'created_date_start': 'created_date_start',
        'created_date_end': 'created_date_end',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, limit=None, service_id=None, service_name=None, product_template_id=None, product_id=None, created_user_name=None, created_date_start=None, created_date_end=None, offset=None):
        r"""ListServicesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param service_id: 服务ID
        :type service_id: int
        :param service_name: 服务名称
        :type service_name: str
        :param product_template_id: 归属产品模板ID，product_template_id和product_id二选一
        :type product_template_id: int
        :param product_id: 归属产品ID，product_template_id和product_id二选一
        :type product_id: int
        :param created_user_name: 创建用户名
        :type created_user_name: str
        :param created_date_start: 创建时间起始，格式timestamp(ms)，使用UTC时区
        :type created_date_start: int
        :param created_date_end: 创建时间截止，格式timestamp(ms)。使用UTC时区
        :type created_date_end: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        """
        
        

        self._instance_id = None
        self._limit = None
        self._service_id = None
        self._service_name = None
        self._product_template_id = None
        self._product_id = None
        self._created_user_name = None
        self._created_date_start = None
        self._created_date_end = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if service_id is not None:
            self.service_id = service_id
        if service_name is not None:
            self.service_name = service_name
        if product_template_id is not None:
            self.product_template_id = product_template_id
        if product_id is not None:
            self.product_id = product_id
        if created_user_name is not None:
            self.created_user_name = created_user_name
        if created_date_start is not None:
            self.created_date_start = created_date_start
        if created_date_end is not None:
            self.created_date_end = created_date_end
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListServicesRequest.

        实例ID

        :return: The instance_id of this ListServicesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListServicesRequest.

        实例ID

        :param instance_id: The instance_id of this ListServicesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ListServicesRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ListServicesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListServicesRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ListServicesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def service_id(self):
        r"""Gets the service_id of this ListServicesRequest.

        服务ID

        :return: The service_id of this ListServicesRequest.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ListServicesRequest.

        服务ID

        :param service_id: The service_id of this ListServicesRequest.
        :type service_id: int
        """
        self._service_id = service_id

    @property
    def service_name(self):
        r"""Gets the service_name of this ListServicesRequest.

        服务名称

        :return: The service_name of this ListServicesRequest.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ListServicesRequest.

        服务名称

        :param service_name: The service_name of this ListServicesRequest.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def product_template_id(self):
        r"""Gets the product_template_id of this ListServicesRequest.

        归属产品模板ID，product_template_id和product_id二选一

        :return: The product_template_id of this ListServicesRequest.
        :rtype: int
        """
        return self._product_template_id

    @product_template_id.setter
    def product_template_id(self, product_template_id):
        r"""Sets the product_template_id of this ListServicesRequest.

        归属产品模板ID，product_template_id和product_id二选一

        :param product_template_id: The product_template_id of this ListServicesRequest.
        :type product_template_id: int
        """
        self._product_template_id = product_template_id

    @property
    def product_id(self):
        r"""Gets the product_id of this ListServicesRequest.

        归属产品ID，product_template_id和product_id二选一

        :return: The product_id of this ListServicesRequest.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ListServicesRequest.

        归属产品ID，product_template_id和product_id二选一

        :param product_id: The product_id of this ListServicesRequest.
        :type product_id: int
        """
        self._product_id = product_id

    @property
    def created_user_name(self):
        r"""Gets the created_user_name of this ListServicesRequest.

        创建用户名

        :return: The created_user_name of this ListServicesRequest.
        :rtype: str
        """
        return self._created_user_name

    @created_user_name.setter
    def created_user_name(self, created_user_name):
        r"""Sets the created_user_name of this ListServicesRequest.

        创建用户名

        :param created_user_name: The created_user_name of this ListServicesRequest.
        :type created_user_name: str
        """
        self._created_user_name = created_user_name

    @property
    def created_date_start(self):
        r"""Gets the created_date_start of this ListServicesRequest.

        创建时间起始，格式timestamp(ms)，使用UTC时区

        :return: The created_date_start of this ListServicesRequest.
        :rtype: int
        """
        return self._created_date_start

    @created_date_start.setter
    def created_date_start(self, created_date_start):
        r"""Sets the created_date_start of this ListServicesRequest.

        创建时间起始，格式timestamp(ms)，使用UTC时区

        :param created_date_start: The created_date_start of this ListServicesRequest.
        :type created_date_start: int
        """
        self._created_date_start = created_date_start

    @property
    def created_date_end(self):
        r"""Gets the created_date_end of this ListServicesRequest.

        创建时间截止，格式timestamp(ms)。使用UTC时区

        :return: The created_date_end of this ListServicesRequest.
        :rtype: int
        """
        return self._created_date_end

    @created_date_end.setter
    def created_date_end(self, created_date_end):
        r"""Sets the created_date_end of this ListServicesRequest.

        创建时间截止，格式timestamp(ms)。使用UTC时区

        :param created_date_end: The created_date_end of this ListServicesRequest.
        :type created_date_end: int
        """
        self._created_date_end = created_date_end

    @property
    def offset(self):
        r"""Gets the offset of this ListServicesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListServicesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListServicesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListServicesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListServicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
