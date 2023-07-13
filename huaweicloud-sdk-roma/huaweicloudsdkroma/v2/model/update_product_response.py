# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProductResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permissions': 'list[str]',
        'id': 'int',
        'product_serial': 'str',
        'app_id': 'str',
        'name': 'str',
        'manufacturer_id': 'str',
        'manufacturer_name': 'str',
        'model': 'str',
        'product_type': 'int',
        'description': 'str',
        'protocol_type': 'int',
        'device_type': 'str',
        'version': 'str',
        'created_user': 'CreatedUser',
        'last_updated_user': 'LastUpdatedUser',
        'created_datetime': 'int',
        'app_name': 'str',
        'data_format': 'int'
    }

    attribute_map = {
        'permissions': 'permissions',
        'id': 'id',
        'product_serial': 'product_serial',
        'app_id': 'app_id',
        'name': 'name',
        'manufacturer_id': 'manufacturer_id',
        'manufacturer_name': 'manufacturer_name',
        'model': 'model',
        'product_type': 'product_type',
        'description': 'description',
        'protocol_type': 'protocol_type',
        'device_type': 'device_type',
        'version': 'version',
        'created_user': 'created_user',
        'last_updated_user': 'last_updated_user',
        'created_datetime': 'created_datetime',
        'app_name': 'app_name',
        'data_format': 'data_format'
    }

    def __init__(self, permissions=None, id=None, product_serial=None, app_id=None, name=None, manufacturer_id=None, manufacturer_name=None, model=None, product_type=None, description=None, protocol_type=None, device_type=None, version=None, created_user=None, last_updated_user=None, created_datetime=None, app_name=None, data_format=None):
        """UpdateProductResponse

        The model defined in huaweicloud sdk

        :param permissions: 权限
        :type permissions: list[str]
        :param id: 产品ID
        :type id: int
        :param product_serial: 产品唯一序列（系统唯一值，用于MQS的TOPIC中标记产品）
        :type product_serial: str
        :param app_id: 应用ID
        :type app_id: str
        :param name: 产品名称，创建产品时租户内唯一，长度最大64，仅支持中文，英文字母，数字，下划线和中划线
        :type name: str
        :param manufacturer_id: 产品供应商ID
        :type manufacturer_id: str
        :param manufacturer_name: 厂商名称
        :type manufacturer_name: str
        :param model: 产品型号
        :type model: str
        :param product_type: 产品类型，0-普通产品(不支持子设备) 1-网关产品
        :type product_type: int
        :param description: 产品描述，长度0-200
        :type description: str
        :param protocol_type: 产品的协议类型 0-mqtt 2-modbus 4-opcua
        :type protocol_type: int
        :param device_type: 产品的设备类型（默认Default）
        :type device_type: str
        :param version: 产品版本
        :type version: str
        :param created_user: 
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        :param last_updated_user: 
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        :param created_datetime: 创建时间，timestamp(ms)，使用UTC时区
        :type created_datetime: int
        :param app_name: 应用名称
        :type app_name: str
        :param data_format: data_format 0-JSON 1-USER_DEFINED
        :type data_format: int
        """
        
        super(UpdateProductResponse, self).__init__()

        self._permissions = None
        self._id = None
        self._product_serial = None
        self._app_id = None
        self._name = None
        self._manufacturer_id = None
        self._manufacturer_name = None
        self._model = None
        self._product_type = None
        self._description = None
        self._protocol_type = None
        self._device_type = None
        self._version = None
        self._created_user = None
        self._last_updated_user = None
        self._created_datetime = None
        self._app_name = None
        self._data_format = None
        self.discriminator = None

        if permissions is not None:
            self.permissions = permissions
        if id is not None:
            self.id = id
        if product_serial is not None:
            self.product_serial = product_serial
        if app_id is not None:
            self.app_id = app_id
        if name is not None:
            self.name = name
        if manufacturer_id is not None:
            self.manufacturer_id = manufacturer_id
        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if model is not None:
            self.model = model
        if product_type is not None:
            self.product_type = product_type
        if description is not None:
            self.description = description
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if device_type is not None:
            self.device_type = device_type
        if version is not None:
            self.version = version
        if created_user is not None:
            self.created_user = created_user
        if last_updated_user is not None:
            self.last_updated_user = last_updated_user
        if created_datetime is not None:
            self.created_datetime = created_datetime
        if app_name is not None:
            self.app_name = app_name
        if data_format is not None:
            self.data_format = data_format

    @property
    def permissions(self):
        """Gets the permissions of this UpdateProductResponse.

        权限

        :return: The permissions of this UpdateProductResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this UpdateProductResponse.

        权限

        :param permissions: The permissions of this UpdateProductResponse.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def id(self):
        """Gets the id of this UpdateProductResponse.

        产品ID

        :return: The id of this UpdateProductResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateProductResponse.

        产品ID

        :param id: The id of this UpdateProductResponse.
        :type id: int
        """
        self._id = id

    @property
    def product_serial(self):
        """Gets the product_serial of this UpdateProductResponse.

        产品唯一序列（系统唯一值，用于MQS的TOPIC中标记产品）

        :return: The product_serial of this UpdateProductResponse.
        :rtype: str
        """
        return self._product_serial

    @product_serial.setter
    def product_serial(self, product_serial):
        """Sets the product_serial of this UpdateProductResponse.

        产品唯一序列（系统唯一值，用于MQS的TOPIC中标记产品）

        :param product_serial: The product_serial of this UpdateProductResponse.
        :type product_serial: str
        """
        self._product_serial = product_serial

    @property
    def app_id(self):
        """Gets the app_id of this UpdateProductResponse.

        应用ID

        :return: The app_id of this UpdateProductResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UpdateProductResponse.

        应用ID

        :param app_id: The app_id of this UpdateProductResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def name(self):
        """Gets the name of this UpdateProductResponse.

        产品名称，创建产品时租户内唯一，长度最大64，仅支持中文，英文字母，数字，下划线和中划线

        :return: The name of this UpdateProductResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateProductResponse.

        产品名称，创建产品时租户内唯一，长度最大64，仅支持中文，英文字母，数字，下划线和中划线

        :param name: The name of this UpdateProductResponse.
        :type name: str
        """
        self._name = name

    @property
    def manufacturer_id(self):
        """Gets the manufacturer_id of this UpdateProductResponse.

        产品供应商ID

        :return: The manufacturer_id of this UpdateProductResponse.
        :rtype: str
        """
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        """Sets the manufacturer_id of this UpdateProductResponse.

        产品供应商ID

        :param manufacturer_id: The manufacturer_id of this UpdateProductResponse.
        :type manufacturer_id: str
        """
        self._manufacturer_id = manufacturer_id

    @property
    def manufacturer_name(self):
        """Gets the manufacturer_name of this UpdateProductResponse.

        厂商名称

        :return: The manufacturer_name of this UpdateProductResponse.
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """Sets the manufacturer_name of this UpdateProductResponse.

        厂商名称

        :param manufacturer_name: The manufacturer_name of this UpdateProductResponse.
        :type manufacturer_name: str
        """
        self._manufacturer_name = manufacturer_name

    @property
    def model(self):
        """Gets the model of this UpdateProductResponse.

        产品型号

        :return: The model of this UpdateProductResponse.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this UpdateProductResponse.

        产品型号

        :param model: The model of this UpdateProductResponse.
        :type model: str
        """
        self._model = model

    @property
    def product_type(self):
        """Gets the product_type of this UpdateProductResponse.

        产品类型，0-普通产品(不支持子设备) 1-网关产品

        :return: The product_type of this UpdateProductResponse.
        :rtype: int
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this UpdateProductResponse.

        产品类型，0-普通产品(不支持子设备) 1-网关产品

        :param product_type: The product_type of this UpdateProductResponse.
        :type product_type: int
        """
        self._product_type = product_type

    @property
    def description(self):
        """Gets the description of this UpdateProductResponse.

        产品描述，长度0-200

        :return: The description of this UpdateProductResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateProductResponse.

        产品描述，长度0-200

        :param description: The description of this UpdateProductResponse.
        :type description: str
        """
        self._description = description

    @property
    def protocol_type(self):
        """Gets the protocol_type of this UpdateProductResponse.

        产品的协议类型 0-mqtt 2-modbus 4-opcua

        :return: The protocol_type of this UpdateProductResponse.
        :rtype: int
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this UpdateProductResponse.

        产品的协议类型 0-mqtt 2-modbus 4-opcua

        :param protocol_type: The protocol_type of this UpdateProductResponse.
        :type protocol_type: int
        """
        self._protocol_type = protocol_type

    @property
    def device_type(self):
        """Gets the device_type of this UpdateProductResponse.

        产品的设备类型（默认Default）

        :return: The device_type of this UpdateProductResponse.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this UpdateProductResponse.

        产品的设备类型（默认Default）

        :param device_type: The device_type of this UpdateProductResponse.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def version(self):
        """Gets the version of this UpdateProductResponse.

        产品版本

        :return: The version of this UpdateProductResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateProductResponse.

        产品版本

        :param version: The version of this UpdateProductResponse.
        :type version: str
        """
        self._version = version

    @property
    def created_user(self):
        """Gets the created_user of this UpdateProductResponse.

        :return: The created_user of this UpdateProductResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user):
        """Sets the created_user of this UpdateProductResponse.

        :param created_user: The created_user of this UpdateProductResponse.
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        self._created_user = created_user

    @property
    def last_updated_user(self):
        """Gets the last_updated_user of this UpdateProductResponse.

        :return: The last_updated_user of this UpdateProductResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        return self._last_updated_user

    @last_updated_user.setter
    def last_updated_user(self, last_updated_user):
        """Sets the last_updated_user of this UpdateProductResponse.

        :param last_updated_user: The last_updated_user of this UpdateProductResponse.
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        self._last_updated_user = last_updated_user

    @property
    def created_datetime(self):
        """Gets the created_datetime of this UpdateProductResponse.

        创建时间，timestamp(ms)，使用UTC时区

        :return: The created_datetime of this UpdateProductResponse.
        :rtype: int
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        """Sets the created_datetime of this UpdateProductResponse.

        创建时间，timestamp(ms)，使用UTC时区

        :param created_datetime: The created_datetime of this UpdateProductResponse.
        :type created_datetime: int
        """
        self._created_datetime = created_datetime

    @property
    def app_name(self):
        """Gets the app_name of this UpdateProductResponse.

        应用名称

        :return: The app_name of this UpdateProductResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this UpdateProductResponse.

        应用名称

        :param app_name: The app_name of this UpdateProductResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def data_format(self):
        """Gets the data_format of this UpdateProductResponse.

        data_format 0-JSON 1-USER_DEFINED

        :return: The data_format of this UpdateProductResponse.
        :rtype: int
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this UpdateProductResponse.

        data_format 0-JSON 1-USER_DEFINED

        :param data_format: The data_format of this UpdateProductResponse.
        :type data_format: int
        """
        self._data_format = data_format

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
        if not isinstance(other, UpdateProductResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
