# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductsRequest:

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
        'app_id': 'str',
        'id': 'str',
        'name': 'str',
        'manufacturer_id': 'str',
        'manufacturer_name': 'str',
        'model': 'str',
        'device_type': 'str',
        'product_type': 'int',
        'protocol_type': 'int',
        'created_user_name': 'str',
        'created_date_start': 'int',
        'created_date_end': 'int',
        'offset': 'int',
        'app_name': 'str',
        'product_serial': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'app_id': 'app_id',
        'id': 'id',
        'name': 'name',
        'manufacturer_id': 'manufacturer_id',
        'manufacturer_name': 'manufacturer_name',
        'model': 'model',
        'device_type': 'device_type',
        'product_type': 'product_type',
        'protocol_type': 'protocol_type',
        'created_user_name': 'created_user_name',
        'created_date_start': 'created_date_start',
        'created_date_end': 'created_date_end',
        'offset': 'offset',
        'app_name': 'app_name',
        'product_serial': 'product_serial'
    }

    def __init__(self, instance_id=None, limit=None, app_id=None, id=None, name=None, manufacturer_id=None, manufacturer_name=None, model=None, device_type=None, product_type=None, protocol_type=None, created_user_name=None, created_date_start=None, created_date_end=None, offset=None, app_name=None, product_serial=None):
        """ListProductsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param app_id: 应用ID
        :type app_id: str
        :param id: 产品ID
        :type id: str
        :param name: 产品名称
        :type name: str
        :param manufacturer_id: 厂商ID
        :type manufacturer_id: str
        :param manufacturer_name: 厂商名称
        :type manufacturer_name: str
        :param model: 型号
        :type model: str
        :param device_type: 产品的设备类型，默认Default
        :type device_type: str
        :param product_type: 产品类型，0-普通产品(不支持子设备) 1-网关产品
        :type product_type: int
        :param protocol_type: 产品的协议类型 0-mqtt 2-modbus 4-opcua
        :type protocol_type: int
        :param created_user_name: 创建用户
        :type created_user_name: str
        :param created_date_start: 创建时间起始，格式timestamp(ms)，使用UTC时区
        :type created_date_start: int
        :param created_date_end: 创建时间截止，格式timestamp(ms)，使用UTC时区
        :type created_date_end: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param app_name: 应用名称
        :type app_name: str
        :param product_serial: 产品唯一序列（系统唯一值，用于MQS的TOPIC中标记产品）
        :type product_serial: str
        """
        
        

        self._instance_id = None
        self._limit = None
        self._app_id = None
        self._id = None
        self._name = None
        self._manufacturer_id = None
        self._manufacturer_name = None
        self._model = None
        self._device_type = None
        self._product_type = None
        self._protocol_type = None
        self._created_user_name = None
        self._created_date_start = None
        self._created_date_end = None
        self._offset = None
        self._app_name = None
        self._product_serial = None
        self.discriminator = None

        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if app_id is not None:
            self.app_id = app_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if manufacturer_id is not None:
            self.manufacturer_id = manufacturer_id
        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if model is not None:
            self.model = model
        if device_type is not None:
            self.device_type = device_type
        if product_type is not None:
            self.product_type = product_type
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if created_user_name is not None:
            self.created_user_name = created_user_name
        if created_date_start is not None:
            self.created_date_start = created_date_start
        if created_date_end is not None:
            self.created_date_end = created_date_end
        if offset is not None:
            self.offset = offset
        if app_name is not None:
            self.app_name = app_name
        if product_serial is not None:
            self.product_serial = product_serial

    @property
    def instance_id(self):
        """Gets the instance_id of this ListProductsRequest.

        实例ID

        :return: The instance_id of this ListProductsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListProductsRequest.

        实例ID

        :param instance_id: The instance_id of this ListProductsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListProductsRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ListProductsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProductsRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ListProductsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def app_id(self):
        """Gets the app_id of this ListProductsRequest.

        应用ID

        :return: The app_id of this ListProductsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListProductsRequest.

        应用ID

        :param app_id: The app_id of this ListProductsRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def id(self):
        """Gets the id of this ListProductsRequest.

        产品ID

        :return: The id of this ListProductsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListProductsRequest.

        产品ID

        :param id: The id of this ListProductsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListProductsRequest.

        产品名称

        :return: The name of this ListProductsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListProductsRequest.

        产品名称

        :param name: The name of this ListProductsRequest.
        :type name: str
        """
        self._name = name

    @property
    def manufacturer_id(self):
        """Gets the manufacturer_id of this ListProductsRequest.

        厂商ID

        :return: The manufacturer_id of this ListProductsRequest.
        :rtype: str
        """
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        """Sets the manufacturer_id of this ListProductsRequest.

        厂商ID

        :param manufacturer_id: The manufacturer_id of this ListProductsRequest.
        :type manufacturer_id: str
        """
        self._manufacturer_id = manufacturer_id

    @property
    def manufacturer_name(self):
        """Gets the manufacturer_name of this ListProductsRequest.

        厂商名称

        :return: The manufacturer_name of this ListProductsRequest.
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """Sets the manufacturer_name of this ListProductsRequest.

        厂商名称

        :param manufacturer_name: The manufacturer_name of this ListProductsRequest.
        :type manufacturer_name: str
        """
        self._manufacturer_name = manufacturer_name

    @property
    def model(self):
        """Gets the model of this ListProductsRequest.

        型号

        :return: The model of this ListProductsRequest.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ListProductsRequest.

        型号

        :param model: The model of this ListProductsRequest.
        :type model: str
        """
        self._model = model

    @property
    def device_type(self):
        """Gets the device_type of this ListProductsRequest.

        产品的设备类型，默认Default

        :return: The device_type of this ListProductsRequest.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ListProductsRequest.

        产品的设备类型，默认Default

        :param device_type: The device_type of this ListProductsRequest.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def product_type(self):
        """Gets the product_type of this ListProductsRequest.

        产品类型，0-普通产品(不支持子设备) 1-网关产品

        :return: The product_type of this ListProductsRequest.
        :rtype: int
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this ListProductsRequest.

        产品类型，0-普通产品(不支持子设备) 1-网关产品

        :param product_type: The product_type of this ListProductsRequest.
        :type product_type: int
        """
        self._product_type = product_type

    @property
    def protocol_type(self):
        """Gets the protocol_type of this ListProductsRequest.

        产品的协议类型 0-mqtt 2-modbus 4-opcua

        :return: The protocol_type of this ListProductsRequest.
        :rtype: int
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this ListProductsRequest.

        产品的协议类型 0-mqtt 2-modbus 4-opcua

        :param protocol_type: The protocol_type of this ListProductsRequest.
        :type protocol_type: int
        """
        self._protocol_type = protocol_type

    @property
    def created_user_name(self):
        """Gets the created_user_name of this ListProductsRequest.

        创建用户

        :return: The created_user_name of this ListProductsRequest.
        :rtype: str
        """
        return self._created_user_name

    @created_user_name.setter
    def created_user_name(self, created_user_name):
        """Sets the created_user_name of this ListProductsRequest.

        创建用户

        :param created_user_name: The created_user_name of this ListProductsRequest.
        :type created_user_name: str
        """
        self._created_user_name = created_user_name

    @property
    def created_date_start(self):
        """Gets the created_date_start of this ListProductsRequest.

        创建时间起始，格式timestamp(ms)，使用UTC时区

        :return: The created_date_start of this ListProductsRequest.
        :rtype: int
        """
        return self._created_date_start

    @created_date_start.setter
    def created_date_start(self, created_date_start):
        """Sets the created_date_start of this ListProductsRequest.

        创建时间起始，格式timestamp(ms)，使用UTC时区

        :param created_date_start: The created_date_start of this ListProductsRequest.
        :type created_date_start: int
        """
        self._created_date_start = created_date_start

    @property
    def created_date_end(self):
        """Gets the created_date_end of this ListProductsRequest.

        创建时间截止，格式timestamp(ms)，使用UTC时区

        :return: The created_date_end of this ListProductsRequest.
        :rtype: int
        """
        return self._created_date_end

    @created_date_end.setter
    def created_date_end(self, created_date_end):
        """Sets the created_date_end of this ListProductsRequest.

        创建时间截止，格式timestamp(ms)，使用UTC时区

        :param created_date_end: The created_date_end of this ListProductsRequest.
        :type created_date_end: int
        """
        self._created_date_end = created_date_end

    @property
    def offset(self):
        """Gets the offset of this ListProductsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListProductsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProductsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListProductsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def app_name(self):
        """Gets the app_name of this ListProductsRequest.

        应用名称

        :return: The app_name of this ListProductsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListProductsRequest.

        应用名称

        :param app_name: The app_name of this ListProductsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def product_serial(self):
        """Gets the product_serial of this ListProductsRequest.

        产品唯一序列（系统唯一值，用于MQS的TOPIC中标记产品）

        :return: The product_serial of this ListProductsRequest.
        :rtype: str
        """
        return self._product_serial

    @product_serial.setter
    def product_serial(self, product_serial):
        """Sets the product_serial of this ListProductsRequest.

        产品唯一序列（系统唯一值，用于MQS的TOPIC中标记产品）

        :param product_serial: The product_serial of this ListProductsRequest.
        :type product_serial: str
        """
        self._product_serial = product_serial

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
        if not isinstance(other, ListProductsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
