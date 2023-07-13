# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSubsetsToGatewayResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'device_id': 'int',
        'parent_device_id': 'int',
        'product': 'ProductReferer',
        'device_name': 'str',
        'instance_id': 'str',
        'client_id': 'str',
        'node_id': 'str',
        'status': 'int',
        'online_status': 'int',
        'description': 'str',
        'created_user': 'CreatedUser',
        'last_updated_user': 'LastUpdatedUser',
        'created_datetime': 'int',
        'last_updated_datetime': 'int',
        'app_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'device_id': 'device_id',
        'parent_device_id': 'parent_device_id',
        'product': 'product',
        'device_name': 'device_name',
        'instance_id': 'instance_id',
        'client_id': 'client_id',
        'node_id': 'node_id',
        'status': 'status',
        'online_status': 'online_status',
        'description': 'description',
        'created_user': 'created_user',
        'last_updated_user': 'last_updated_user',
        'created_datetime': 'created_datetime',
        'last_updated_datetime': 'last_updated_datetime',
        'app_id': 'app_id'
    }

    def __init__(self, id=None, device_id=None, parent_device_id=None, product=None, device_name=None, instance_id=None, client_id=None, node_id=None, status=None, online_status=None, description=None, created_user=None, last_updated_user=None, created_datetime=None, last_updated_datetime=None, app_id=None):
        """AddSubsetsToGatewayResponseBody

        The model defined in huaweicloud sdk

        :param id: 设备ID
        :type id: int
        :param device_id: 设备ID（兼容20.0）
        :type device_id: int
        :param parent_device_id: 父设备ID
        :type parent_device_id: int
        :param product: 
        :type product: :class:`huaweicloudsdkroma.v2.ProductReferer`
        :param device_name: 设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?&#39;-@%&amp;!, 长度2-64
        :type device_name: str
        :param instance_id: 实例id
        :type instance_id: str
        :param client_id: 设备客户端ID，平台生成的设备唯一标识
        :type client_id: str
        :param node_id: 设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64
        :type node_id: str
        :param status: 设备状态 0-启用 1-禁用
        :type status: int
        :param online_status: 是否在线 0-未连接 1-在线 2-离线
        :type online_status: int
        :param description: 备注
        :type description: str
        :param created_user: 
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        :param last_updated_user: 
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        :param created_datetime: 创建时间，timestamp(ms)，使用UTC时区
        :type created_datetime: int
        :param last_updated_datetime: 最后修改时间，timestamp(ms)，使用UTC时区
        :type last_updated_datetime: int
        :param app_id: 应用ID
        :type app_id: str
        """
        
        

        self._id = None
        self._device_id = None
        self._parent_device_id = None
        self._product = None
        self._device_name = None
        self._instance_id = None
        self._client_id = None
        self._node_id = None
        self._status = None
        self._online_status = None
        self._description = None
        self._created_user = None
        self._last_updated_user = None
        self._created_datetime = None
        self._last_updated_datetime = None
        self._app_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if device_id is not None:
            self.device_id = device_id
        if parent_device_id is not None:
            self.parent_device_id = parent_device_id
        if product is not None:
            self.product = product
        if device_name is not None:
            self.device_name = device_name
        if instance_id is not None:
            self.instance_id = instance_id
        if client_id is not None:
            self.client_id = client_id
        if node_id is not None:
            self.node_id = node_id
        if status is not None:
            self.status = status
        if online_status is not None:
            self.online_status = online_status
        if description is not None:
            self.description = description
        if created_user is not None:
            self.created_user = created_user
        if last_updated_user is not None:
            self.last_updated_user = last_updated_user
        if created_datetime is not None:
            self.created_datetime = created_datetime
        if last_updated_datetime is not None:
            self.last_updated_datetime = last_updated_datetime
        if app_id is not None:
            self.app_id = app_id

    @property
    def id(self):
        """Gets the id of this AddSubsetsToGatewayResponseBody.

        设备ID

        :return: The id of this AddSubsetsToGatewayResponseBody.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddSubsetsToGatewayResponseBody.

        设备ID

        :param id: The id of this AddSubsetsToGatewayResponseBody.
        :type id: int
        """
        self._id = id

    @property
    def device_id(self):
        """Gets the device_id of this AddSubsetsToGatewayResponseBody.

        设备ID（兼容20.0）

        :return: The device_id of this AddSubsetsToGatewayResponseBody.
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this AddSubsetsToGatewayResponseBody.

        设备ID（兼容20.0）

        :param device_id: The device_id of this AddSubsetsToGatewayResponseBody.
        :type device_id: int
        """
        self._device_id = device_id

    @property
    def parent_device_id(self):
        """Gets the parent_device_id of this AddSubsetsToGatewayResponseBody.

        父设备ID

        :return: The parent_device_id of this AddSubsetsToGatewayResponseBody.
        :rtype: int
        """
        return self._parent_device_id

    @parent_device_id.setter
    def parent_device_id(self, parent_device_id):
        """Sets the parent_device_id of this AddSubsetsToGatewayResponseBody.

        父设备ID

        :param parent_device_id: The parent_device_id of this AddSubsetsToGatewayResponseBody.
        :type parent_device_id: int
        """
        self._parent_device_id = parent_device_id

    @property
    def product(self):
        """Gets the product of this AddSubsetsToGatewayResponseBody.

        :return: The product of this AddSubsetsToGatewayResponseBody.
        :rtype: :class:`huaweicloudsdkroma.v2.ProductReferer`
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this AddSubsetsToGatewayResponseBody.

        :param product: The product of this AddSubsetsToGatewayResponseBody.
        :type product: :class:`huaweicloudsdkroma.v2.ProductReferer`
        """
        self._product = product

    @property
    def device_name(self):
        """Gets the device_name of this AddSubsetsToGatewayResponseBody.

        设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?'-@%&!, 长度2-64

        :return: The device_name of this AddSubsetsToGatewayResponseBody.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this AddSubsetsToGatewayResponseBody.

        设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?'-@%&!, 长度2-64

        :param device_name: The device_name of this AddSubsetsToGatewayResponseBody.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def instance_id(self):
        """Gets the instance_id of this AddSubsetsToGatewayResponseBody.

        实例id

        :return: The instance_id of this AddSubsetsToGatewayResponseBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AddSubsetsToGatewayResponseBody.

        实例id

        :param instance_id: The instance_id of this AddSubsetsToGatewayResponseBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def client_id(self):
        """Gets the client_id of this AddSubsetsToGatewayResponseBody.

        设备客户端ID，平台生成的设备唯一标识

        :return: The client_id of this AddSubsetsToGatewayResponseBody.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AddSubsetsToGatewayResponseBody.

        设备客户端ID，平台生成的设备唯一标识

        :param client_id: The client_id of this AddSubsetsToGatewayResponseBody.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def node_id(self):
        """Gets the node_id of this AddSubsetsToGatewayResponseBody.

        设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64

        :return: The node_id of this AddSubsetsToGatewayResponseBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this AddSubsetsToGatewayResponseBody.

        设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64

        :param node_id: The node_id of this AddSubsetsToGatewayResponseBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def status(self):
        """Gets the status of this AddSubsetsToGatewayResponseBody.

        设备状态 0-启用 1-禁用

        :return: The status of this AddSubsetsToGatewayResponseBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AddSubsetsToGatewayResponseBody.

        设备状态 0-启用 1-禁用

        :param status: The status of this AddSubsetsToGatewayResponseBody.
        :type status: int
        """
        self._status = status

    @property
    def online_status(self):
        """Gets the online_status of this AddSubsetsToGatewayResponseBody.

        是否在线 0-未连接 1-在线 2-离线

        :return: The online_status of this AddSubsetsToGatewayResponseBody.
        :rtype: int
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        """Sets the online_status of this AddSubsetsToGatewayResponseBody.

        是否在线 0-未连接 1-在线 2-离线

        :param online_status: The online_status of this AddSubsetsToGatewayResponseBody.
        :type online_status: int
        """
        self._online_status = online_status

    @property
    def description(self):
        """Gets the description of this AddSubsetsToGatewayResponseBody.

        备注

        :return: The description of this AddSubsetsToGatewayResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddSubsetsToGatewayResponseBody.

        备注

        :param description: The description of this AddSubsetsToGatewayResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def created_user(self):
        """Gets the created_user of this AddSubsetsToGatewayResponseBody.

        :return: The created_user of this AddSubsetsToGatewayResponseBody.
        :rtype: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user):
        """Sets the created_user of this AddSubsetsToGatewayResponseBody.

        :param created_user: The created_user of this AddSubsetsToGatewayResponseBody.
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        self._created_user = created_user

    @property
    def last_updated_user(self):
        """Gets the last_updated_user of this AddSubsetsToGatewayResponseBody.

        :return: The last_updated_user of this AddSubsetsToGatewayResponseBody.
        :rtype: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        return self._last_updated_user

    @last_updated_user.setter
    def last_updated_user(self, last_updated_user):
        """Sets the last_updated_user of this AddSubsetsToGatewayResponseBody.

        :param last_updated_user: The last_updated_user of this AddSubsetsToGatewayResponseBody.
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        self._last_updated_user = last_updated_user

    @property
    def created_datetime(self):
        """Gets the created_datetime of this AddSubsetsToGatewayResponseBody.

        创建时间，timestamp(ms)，使用UTC时区

        :return: The created_datetime of this AddSubsetsToGatewayResponseBody.
        :rtype: int
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        """Sets the created_datetime of this AddSubsetsToGatewayResponseBody.

        创建时间，timestamp(ms)，使用UTC时区

        :param created_datetime: The created_datetime of this AddSubsetsToGatewayResponseBody.
        :type created_datetime: int
        """
        self._created_datetime = created_datetime

    @property
    def last_updated_datetime(self):
        """Gets the last_updated_datetime of this AddSubsetsToGatewayResponseBody.

        最后修改时间，timestamp(ms)，使用UTC时区

        :return: The last_updated_datetime of this AddSubsetsToGatewayResponseBody.
        :rtype: int
        """
        return self._last_updated_datetime

    @last_updated_datetime.setter
    def last_updated_datetime(self, last_updated_datetime):
        """Sets the last_updated_datetime of this AddSubsetsToGatewayResponseBody.

        最后修改时间，timestamp(ms)，使用UTC时区

        :param last_updated_datetime: The last_updated_datetime of this AddSubsetsToGatewayResponseBody.
        :type last_updated_datetime: int
        """
        self._last_updated_datetime = last_updated_datetime

    @property
    def app_id(self):
        """Gets the app_id of this AddSubsetsToGatewayResponseBody.

        应用ID

        :return: The app_id of this AddSubsetsToGatewayResponseBody.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AddSubsetsToGatewayResponseBody.

        应用ID

        :param app_id: The app_id of this AddSubsetsToGatewayResponseBody.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, AddSubsetsToGatewayResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
