# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Service:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'product_template_id': 'int',
        'product_id': 'int',
        'service_id': 'int',
        'service_name': 'str',
        'description': 'str',
        'status': 'int',
        'created_user': 'CreatedUser',
        'last_updated_user': 'LastUpdatedUser',
        'created_datetime': 'int',
        'last_updated_datetime': 'int'
    }

    attribute_map = {
        'product_template_id': 'product_template_id',
        'product_id': 'product_id',
        'service_id': 'service_id',
        'service_name': 'service_name',
        'description': 'description',
        'status': 'status',
        'created_user': 'created_user',
        'last_updated_user': 'last_updated_user',
        'created_datetime': 'created_datetime',
        'last_updated_datetime': 'last_updated_datetime'
    }

    def __init__(self, product_template_id=None, product_id=None, service_id=None, service_name=None, description=None, status=None, created_user=None, last_updated_user=None, created_datetime=None, last_updated_datetime=None):
        """Service

        The model defined in huaweicloud sdk

        :param product_template_id: 服务归属的产品模板ID
        :type product_template_id: int
        :param product_id: 服务归属的产品ID
        :type product_id: int
        :param service_id: 服务ID
        :type service_id: int
        :param service_name: 服务名称，支持中文,英文大小写，数字，下划线和中划线,长度2-64
        :type service_name: str
        :param description: 服务描述，长度0-200
        :type description: str
        :param status: 服务状态 0-启用 1-停用
        :type status: int
        :param created_user: 
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        :param last_updated_user: 
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        :param created_datetime: 创建时间止，格式timestamp(ms)，使用UTC时区
        :type created_datetime: int
        :param last_updated_datetime: 最后修改时间止，格式timestamp(ms)，使用UTC时区
        :type last_updated_datetime: int
        """
        
        

        self._product_template_id = None
        self._product_id = None
        self._service_id = None
        self._service_name = None
        self._description = None
        self._status = None
        self._created_user = None
        self._last_updated_user = None
        self._created_datetime = None
        self._last_updated_datetime = None
        self.discriminator = None

        if product_template_id is not None:
            self.product_template_id = product_template_id
        if product_id is not None:
            self.product_id = product_id
        if service_id is not None:
            self.service_id = service_id
        if service_name is not None:
            self.service_name = service_name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if created_user is not None:
            self.created_user = created_user
        if last_updated_user is not None:
            self.last_updated_user = last_updated_user
        if created_datetime is not None:
            self.created_datetime = created_datetime
        if last_updated_datetime is not None:
            self.last_updated_datetime = last_updated_datetime

    @property
    def product_template_id(self):
        """Gets the product_template_id of this Service.

        服务归属的产品模板ID

        :return: The product_template_id of this Service.
        :rtype: int
        """
        return self._product_template_id

    @product_template_id.setter
    def product_template_id(self, product_template_id):
        """Sets the product_template_id of this Service.

        服务归属的产品模板ID

        :param product_template_id: The product_template_id of this Service.
        :type product_template_id: int
        """
        self._product_template_id = product_template_id

    @property
    def product_id(self):
        """Gets the product_id of this Service.

        服务归属的产品ID

        :return: The product_id of this Service.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this Service.

        服务归属的产品ID

        :param product_id: The product_id of this Service.
        :type product_id: int
        """
        self._product_id = product_id

    @property
    def service_id(self):
        """Gets the service_id of this Service.

        服务ID

        :return: The service_id of this Service.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this Service.

        服务ID

        :param service_id: The service_id of this Service.
        :type service_id: int
        """
        self._service_id = service_id

    @property
    def service_name(self):
        """Gets the service_name of this Service.

        服务名称，支持中文,英文大小写，数字，下划线和中划线,长度2-64

        :return: The service_name of this Service.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this Service.

        服务名称，支持中文,英文大小写，数字，下划线和中划线,长度2-64

        :param service_name: The service_name of this Service.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def description(self):
        """Gets the description of this Service.

        服务描述，长度0-200

        :return: The description of this Service.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Service.

        服务描述，长度0-200

        :param description: The description of this Service.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this Service.

        服务状态 0-启用 1-停用

        :return: The status of this Service.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Service.

        服务状态 0-启用 1-停用

        :param status: The status of this Service.
        :type status: int
        """
        self._status = status

    @property
    def created_user(self):
        """Gets the created_user of this Service.


        :return: The created_user of this Service.
        :rtype: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user):
        """Sets the created_user of this Service.


        :param created_user: The created_user of this Service.
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        self._created_user = created_user

    @property
    def last_updated_user(self):
        """Gets the last_updated_user of this Service.


        :return: The last_updated_user of this Service.
        :rtype: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        return self._last_updated_user

    @last_updated_user.setter
    def last_updated_user(self, last_updated_user):
        """Sets the last_updated_user of this Service.


        :param last_updated_user: The last_updated_user of this Service.
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        self._last_updated_user = last_updated_user

    @property
    def created_datetime(self):
        """Gets the created_datetime of this Service.

        创建时间止，格式timestamp(ms)，使用UTC时区

        :return: The created_datetime of this Service.
        :rtype: int
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        """Sets the created_datetime of this Service.

        创建时间止，格式timestamp(ms)，使用UTC时区

        :param created_datetime: The created_datetime of this Service.
        :type created_datetime: int
        """
        self._created_datetime = created_datetime

    @property
    def last_updated_datetime(self):
        """Gets the last_updated_datetime of this Service.

        最后修改时间止，格式timestamp(ms)，使用UTC时区

        :return: The last_updated_datetime of this Service.
        :rtype: int
        """
        return self._last_updated_datetime

    @last_updated_datetime.setter
    def last_updated_datetime(self, last_updated_datetime):
        """Sets the last_updated_datetime of this Service.

        最后修改时间止，格式timestamp(ms)，使用UTC时区

        :param last_updated_datetime: The last_updated_datetime of this Service.
        :type last_updated_datetime: int
        """
        self._last_updated_datetime = last_updated_datetime

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
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
