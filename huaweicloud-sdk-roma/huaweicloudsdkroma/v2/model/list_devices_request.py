# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevicesRequest:

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
        'offset': 'int',
        'app_id': 'str',
        'product_id': 'int',
        'product_name': 'str',
        'device_name': 'str',
        'client_id': 'str',
        'node_id': 'str',
        'node_type': 'int',
        'online_status': 'str',
        'created_date_start': 'int',
        'created_date_end': 'int',
        'tag': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset',
        'app_id': 'app_id',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'device_name': 'device_name',
        'client_id': 'client_id',
        'node_id': 'node_id',
        'node_type': 'node_type',
        'online_status': 'online_status',
        'created_date_start': 'created_date_start',
        'created_date_end': 'created_date_end',
        'tag': 'tag'
    }

    def __init__(self, instance_id=None, limit=None, offset=None, app_id=None, product_id=None, product_name=None, device_name=None, client_id=None, node_id=None, node_type=None, online_status=None, created_date_start=None, created_date_end=None, tag=None):
        """ListDevicesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param app_id: 应用ID
        :type app_id: str
        :param product_id: 设备归属的产品ID
        :type product_id: int
        :param product_name: 设备归属的产品名称
        :type product_name: str
        :param device_name: 设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?&#39;-@%&amp;!, 长度2-64
        :type device_name: str
        :param client_id: 设备客户端ID，平台生成的设备唯一标识
        :type client_id: str
        :param node_id: 设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64
        :type node_id: str
        :param node_type: 节点类型 0-直连 1-网关 2-子设备，不传默认查询所有
        :type node_type: int
        :param online_status: 是否在线 0-未连接 1-在线 2-离线，支持传入多个值以逗号分隔
        :type online_status: str
        :param created_date_start: 创建时间起始，格式timestamp(ms)，使用UTC时区
        :type created_date_start: int
        :param created_date_end: 创建时间截止，格式timestamp(ms)，使用UTC时区
        :type created_date_end: int
        :param tag: 标签
        :type tag: str
        """
        
        

        self._instance_id = None
        self._limit = None
        self._offset = None
        self._app_id = None
        self._product_id = None
        self._product_name = None
        self._device_name = None
        self._client_id = None
        self._node_id = None
        self._node_type = None
        self._online_status = None
        self._created_date_start = None
        self._created_date_end = None
        self._tag = None
        self.discriminator = None

        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if app_id is not None:
            self.app_id = app_id
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if device_name is not None:
            self.device_name = device_name
        if client_id is not None:
            self.client_id = client_id
        if node_id is not None:
            self.node_id = node_id
        if node_type is not None:
            self.node_type = node_type
        if online_status is not None:
            self.online_status = online_status
        if created_date_start is not None:
            self.created_date_start = created_date_start
        if created_date_end is not None:
            self.created_date_end = created_date_end
        if tag is not None:
            self.tag = tag

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDevicesRequest.

        实例ID

        :return: The instance_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDevicesRequest.

        实例ID

        :param instance_id: The instance_id of this ListDevicesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListDevicesRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ListDevicesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDevicesRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ListDevicesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDevicesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListDevicesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDevicesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListDevicesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def app_id(self):
        """Gets the app_id of this ListDevicesRequest.

        应用ID

        :return: The app_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListDevicesRequest.

        应用ID

        :param app_id: The app_id of this ListDevicesRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def product_id(self):
        """Gets the product_id of this ListDevicesRequest.

        设备归属的产品ID

        :return: The product_id of this ListDevicesRequest.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ListDevicesRequest.

        设备归属的产品ID

        :param product_id: The product_id of this ListDevicesRequest.
        :type product_id: int
        """
        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this ListDevicesRequest.

        设备归属的产品名称

        :return: The product_name of this ListDevicesRequest.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ListDevicesRequest.

        设备归属的产品名称

        :param product_name: The product_name of this ListDevicesRequest.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def device_name(self):
        """Gets the device_name of this ListDevicesRequest.

        设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?'-@%&!, 长度2-64

        :return: The device_name of this ListDevicesRequest.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this ListDevicesRequest.

        设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?'-@%&!, 长度2-64

        :param device_name: The device_name of this ListDevicesRequest.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def client_id(self):
        """Gets the client_id of this ListDevicesRequest.

        设备客户端ID，平台生成的设备唯一标识

        :return: The client_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ListDevicesRequest.

        设备客户端ID，平台生成的设备唯一标识

        :param client_id: The client_id of this ListDevicesRequest.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def node_id(self):
        """Gets the node_id of this ListDevicesRequest.

        设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64

        :return: The node_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ListDevicesRequest.

        设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64

        :param node_id: The node_id of this ListDevicesRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_type(self):
        """Gets the node_type of this ListDevicesRequest.

        节点类型 0-直连 1-网关 2-子设备，不传默认查询所有

        :return: The node_type of this ListDevicesRequest.
        :rtype: int
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this ListDevicesRequest.

        节点类型 0-直连 1-网关 2-子设备，不传默认查询所有

        :param node_type: The node_type of this ListDevicesRequest.
        :type node_type: int
        """
        self._node_type = node_type

    @property
    def online_status(self):
        """Gets the online_status of this ListDevicesRequest.

        是否在线 0-未连接 1-在线 2-离线，支持传入多个值以逗号分隔

        :return: The online_status of this ListDevicesRequest.
        :rtype: str
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        """Sets the online_status of this ListDevicesRequest.

        是否在线 0-未连接 1-在线 2-离线，支持传入多个值以逗号分隔

        :param online_status: The online_status of this ListDevicesRequest.
        :type online_status: str
        """
        self._online_status = online_status

    @property
    def created_date_start(self):
        """Gets the created_date_start of this ListDevicesRequest.

        创建时间起始，格式timestamp(ms)，使用UTC时区

        :return: The created_date_start of this ListDevicesRequest.
        :rtype: int
        """
        return self._created_date_start

    @created_date_start.setter
    def created_date_start(self, created_date_start):
        """Sets the created_date_start of this ListDevicesRequest.

        创建时间起始，格式timestamp(ms)，使用UTC时区

        :param created_date_start: The created_date_start of this ListDevicesRequest.
        :type created_date_start: int
        """
        self._created_date_start = created_date_start

    @property
    def created_date_end(self):
        """Gets the created_date_end of this ListDevicesRequest.

        创建时间截止，格式timestamp(ms)，使用UTC时区

        :return: The created_date_end of this ListDevicesRequest.
        :rtype: int
        """
        return self._created_date_end

    @created_date_end.setter
    def created_date_end(self, created_date_end):
        """Sets the created_date_end of this ListDevicesRequest.

        创建时间截止，格式timestamp(ms)，使用UTC时区

        :param created_date_end: The created_date_end of this ListDevicesRequest.
        :type created_date_end: int
        """
        self._created_date_end = created_date_end

    @property
    def tag(self):
        """Gets the tag of this ListDevicesRequest.

        标签

        :return: The tag of this ListDevicesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListDevicesRequest.

        标签

        :param tag: The tag of this ListDevicesRequest.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ListDevicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
