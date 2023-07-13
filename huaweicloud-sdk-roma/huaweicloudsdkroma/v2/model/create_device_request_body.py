# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDeviceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_device_id': 'int',
        'product': 'ProductReferer',
        'password': 'str',
        'user_name': 'str',
        'device_name': 'str',
        'node_id': 'str',
        'app_id': 'str',
        'status': 'int',
        'description': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'parent_device_id': 'parent_device_id',
        'product': 'product',
        'password': 'password',
        'user_name': 'user_name',
        'device_name': 'device_name',
        'node_id': 'node_id',
        'app_id': 'app_id',
        'status': 'status',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, parent_device_id=None, product=None, password=None, user_name=None, device_name=None, node_id=None, app_id=None, status=None, description=None, tags=None):
        """CreateDeviceRequestBody

        The model defined in huaweicloud sdk

        :param parent_device_id: 父设备ID，无父设备时不填写，自动向下取整
        :type parent_device_id: int
        :param product: 
        :type product: :class:`huaweicloudsdkroma.v2.ProductReferer`
        :param password: 设备密码，输入要求：至少1数字，1大写字母，1小写字母，1特殊字符(~!@#$%^&amp;*()-_&#x3D;+|[{}];:&lt;&gt;/?)，长度8-32个字符
        :type password: str
        :param user_name: 设备用户名，支持英文大小写、英文符号(-)及数字，长度10-50
        :type user_name: str
        :param device_name: 设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?&#39;-@%&amp;!, 长度2-64
        :type device_name: str
        :param node_id: 设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64
        :type node_id: str
        :param app_id: 应用ID
        :type app_id: str
        :param status: 设备状态 0启用 1禁用，不填时默认为0启用
        :type status: int
        :param description: 备注
        :type description: str
        :param tags: 标签
        :type tags: list[str]
        """
        
        

        self._parent_device_id = None
        self._product = None
        self._password = None
        self._user_name = None
        self._device_name = None
        self._node_id = None
        self._app_id = None
        self._status = None
        self._description = None
        self._tags = None
        self.discriminator = None

        if parent_device_id is not None:
            self.parent_device_id = parent_device_id
        self.product = product
        if password is not None:
            self.password = password
        if user_name is not None:
            self.user_name = user_name
        self.device_name = device_name
        self.node_id = node_id
        self.app_id = app_id
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def parent_device_id(self):
        """Gets the parent_device_id of this CreateDeviceRequestBody.

        父设备ID，无父设备时不填写，自动向下取整

        :return: The parent_device_id of this CreateDeviceRequestBody.
        :rtype: int
        """
        return self._parent_device_id

    @parent_device_id.setter
    def parent_device_id(self, parent_device_id):
        """Sets the parent_device_id of this CreateDeviceRequestBody.

        父设备ID，无父设备时不填写，自动向下取整

        :param parent_device_id: The parent_device_id of this CreateDeviceRequestBody.
        :type parent_device_id: int
        """
        self._parent_device_id = parent_device_id

    @property
    def product(self):
        """Gets the product of this CreateDeviceRequestBody.

        :return: The product of this CreateDeviceRequestBody.
        :rtype: :class:`huaweicloudsdkroma.v2.ProductReferer`
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this CreateDeviceRequestBody.

        :param product: The product of this CreateDeviceRequestBody.
        :type product: :class:`huaweicloudsdkroma.v2.ProductReferer`
        """
        self._product = product

    @property
    def password(self):
        """Gets the password of this CreateDeviceRequestBody.

        设备密码，输入要求：至少1数字，1大写字母，1小写字母，1特殊字符(~!@#$%^&*()-_=+|[{}];:<>/?)，长度8-32个字符

        :return: The password of this CreateDeviceRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateDeviceRequestBody.

        设备密码，输入要求：至少1数字，1大写字母，1小写字母，1特殊字符(~!@#$%^&*()-_=+|[{}];:<>/?)，长度8-32个字符

        :param password: The password of this CreateDeviceRequestBody.
        :type password: str
        """
        self._password = password

    @property
    def user_name(self):
        """Gets the user_name of this CreateDeviceRequestBody.

        设备用户名，支持英文大小写、英文符号(-)及数字，长度10-50

        :return: The user_name of this CreateDeviceRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateDeviceRequestBody.

        设备用户名，支持英文大小写、英文符号(-)及数字，长度10-50

        :param user_name: The user_name of this CreateDeviceRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def device_name(self):
        """Gets the device_name of this CreateDeviceRequestBody.

        设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?'-@%&!, 长度2-64

        :return: The device_name of this CreateDeviceRequestBody.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this CreateDeviceRequestBody.

        设备名称，支持中文、中文标点符号（）。；，：“”、？《》及英文大小写、数字及英文符号()_,#.?'-@%&!, 长度2-64

        :param device_name: The device_name of this CreateDeviceRequestBody.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def node_id(self):
        """Gets the node_id of this CreateDeviceRequestBody.

        设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64

        :return: The node_id of this CreateDeviceRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this CreateDeviceRequestBody.

        设备物理编号，通常使用MAC或者IMEI号，支持英文大小写，数字，下划线和中划线，长度2-64

        :param node_id: The node_id of this CreateDeviceRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def app_id(self):
        """Gets the app_id of this CreateDeviceRequestBody.

        应用ID

        :return: The app_id of this CreateDeviceRequestBody.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateDeviceRequestBody.

        应用ID

        :param app_id: The app_id of this CreateDeviceRequestBody.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def status(self):
        """Gets the status of this CreateDeviceRequestBody.

        设备状态 0启用 1禁用，不填时默认为0启用

        :return: The status of this CreateDeviceRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateDeviceRequestBody.

        设备状态 0启用 1禁用，不填时默认为0启用

        :param status: The status of this CreateDeviceRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this CreateDeviceRequestBody.

        备注

        :return: The description of this CreateDeviceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDeviceRequestBody.

        备注

        :param description: The description of this CreateDeviceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        """Gets the tags of this CreateDeviceRequestBody.

        标签

        :return: The tags of this CreateDeviceRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDeviceRequestBody.

        标签

        :param tags: The tags of this CreateDeviceRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, CreateDeviceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
