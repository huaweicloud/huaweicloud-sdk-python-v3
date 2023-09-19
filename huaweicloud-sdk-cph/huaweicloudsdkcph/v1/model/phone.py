# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Phone:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone_name': 'str',
        'server_id': 'str',
        'phone_id': 'str',
        'phone_model_name': 'str',
        'image_id': 'str',
        'vnc_enable': 'str',
        'status': 'int',
        'type': 'int',
        'metadata': 'PhoneMetadata',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'phone_name': 'phone_name',
        'server_id': 'server_id',
        'phone_id': 'phone_id',
        'phone_model_name': 'phone_model_name',
        'image_id': 'image_id',
        'vnc_enable': 'vnc_enable',
        'status': 'status',
        'type': 'type',
        'metadata': 'metadata',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, phone_name=None, server_id=None, phone_id=None, phone_model_name=None, image_id=None, vnc_enable=None, status=None, type=None, metadata=None, create_time=None, update_time=None):
        """Phone

        The model defined in huaweicloud sdk

        :param phone_name: 云手机的名称，不超过65个字符。
        :type phone_name: str
        :param server_id: 云手机所在的服务器ID，不超过32个字节。
        :type server_id: str
        :param phone_id: 云手机的唯一标识，不超过32个字节。
        :type phone_id: str
        :param phone_model_name: 云手机规格名称，不超过64个字节。
        :type phone_model_name: str
        :param image_id: 云手机镜像ID，不超过32个字节。
        :type image_id: str
        :param vnc_enable: 云手机是否开启VNC服务。 - true：开启 - false：不开启
        :type vnc_enable: str
        :param status: 云手机状态。 - 0: 创建中 - 1：创建中 - 2：运行中 - 3：重置中 - 4：重启中 - 6：冻结 - 7：正在关机 - 8：已关机 - -5：重置失败 - -6：重启失败 - -7：手机异常 - -8：创建失败 - -9：关机失败
        :type status: int
        :param type: 云手机类型。 - 0：普通云手机 - 1：试玩云手机
        :type type: int
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcph.v1.PhoneMetadata`
        :param create_time: 创建时间， 时间格式为UTC。
        :type create_time: str
        :param update_time: 更新时间， 时间格式为UTC。
        :type update_time: str
        """
        
        

        self._phone_name = None
        self._server_id = None
        self._phone_id = None
        self._phone_model_name = None
        self._image_id = None
        self._vnc_enable = None
        self._status = None
        self._type = None
        self._metadata = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if phone_name is not None:
            self.phone_name = phone_name
        if server_id is not None:
            self.server_id = server_id
        if phone_id is not None:
            self.phone_id = phone_id
        if phone_model_name is not None:
            self.phone_model_name = phone_model_name
        if image_id is not None:
            self.image_id = image_id
        if vnc_enable is not None:
            self.vnc_enable = vnc_enable
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if metadata is not None:
            self.metadata = metadata
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def phone_name(self):
        """Gets the phone_name of this Phone.

        云手机的名称，不超过65个字符。

        :return: The phone_name of this Phone.
        :rtype: str
        """
        return self._phone_name

    @phone_name.setter
    def phone_name(self, phone_name):
        """Sets the phone_name of this Phone.

        云手机的名称，不超过65个字符。

        :param phone_name: The phone_name of this Phone.
        :type phone_name: str
        """
        self._phone_name = phone_name

    @property
    def server_id(self):
        """Gets the server_id of this Phone.

        云手机所在的服务器ID，不超过32个字节。

        :return: The server_id of this Phone.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this Phone.

        云手机所在的服务器ID，不超过32个字节。

        :param server_id: The server_id of this Phone.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def phone_id(self):
        """Gets the phone_id of this Phone.

        云手机的唯一标识，不超过32个字节。

        :return: The phone_id of this Phone.
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        """Sets the phone_id of this Phone.

        云手机的唯一标识，不超过32个字节。

        :param phone_id: The phone_id of this Phone.
        :type phone_id: str
        """
        self._phone_id = phone_id

    @property
    def phone_model_name(self):
        """Gets the phone_model_name of this Phone.

        云手机规格名称，不超过64个字节。

        :return: The phone_model_name of this Phone.
        :rtype: str
        """
        return self._phone_model_name

    @phone_model_name.setter
    def phone_model_name(self, phone_model_name):
        """Sets the phone_model_name of this Phone.

        云手机规格名称，不超过64个字节。

        :param phone_model_name: The phone_model_name of this Phone.
        :type phone_model_name: str
        """
        self._phone_model_name = phone_model_name

    @property
    def image_id(self):
        """Gets the image_id of this Phone.

        云手机镜像ID，不超过32个字节。

        :return: The image_id of this Phone.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this Phone.

        云手机镜像ID，不超过32个字节。

        :param image_id: The image_id of this Phone.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def vnc_enable(self):
        """Gets the vnc_enable of this Phone.

        云手机是否开启VNC服务。 - true：开启 - false：不开启

        :return: The vnc_enable of this Phone.
        :rtype: str
        """
        return self._vnc_enable

    @vnc_enable.setter
    def vnc_enable(self, vnc_enable):
        """Sets the vnc_enable of this Phone.

        云手机是否开启VNC服务。 - true：开启 - false：不开启

        :param vnc_enable: The vnc_enable of this Phone.
        :type vnc_enable: str
        """
        self._vnc_enable = vnc_enable

    @property
    def status(self):
        """Gets the status of this Phone.

        云手机状态。 - 0: 创建中 - 1：创建中 - 2：运行中 - 3：重置中 - 4：重启中 - 6：冻结 - 7：正在关机 - 8：已关机 - -5：重置失败 - -6：重启失败 - -7：手机异常 - -8：创建失败 - -9：关机失败

        :return: The status of this Phone.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Phone.

        云手机状态。 - 0: 创建中 - 1：创建中 - 2：运行中 - 3：重置中 - 4：重启中 - 6：冻结 - 7：正在关机 - 8：已关机 - -5：重置失败 - -6：重启失败 - -7：手机异常 - -8：创建失败 - -9：关机失败

        :param status: The status of this Phone.
        :type status: int
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this Phone.

        云手机类型。 - 0：普通云手机 - 1：试玩云手机

        :return: The type of this Phone.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Phone.

        云手机类型。 - 0：普通云手机 - 1：试玩云手机

        :param type: The type of this Phone.
        :type type: int
        """
        self._type = type

    @property
    def metadata(self):
        """Gets the metadata of this Phone.

        :return: The metadata of this Phone.
        :rtype: :class:`huaweicloudsdkcph.v1.PhoneMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Phone.

        :param metadata: The metadata of this Phone.
        :type metadata: :class:`huaweicloudsdkcph.v1.PhoneMetadata`
        """
        self._metadata = metadata

    @property
    def create_time(self):
        """Gets the create_time of this Phone.

        创建时间， 时间格式为UTC。

        :return: The create_time of this Phone.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Phone.

        创建时间， 时间格式为UTC。

        :param create_time: The create_time of this Phone.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Phone.

        更新时间， 时间格式为UTC。

        :return: The update_time of this Phone.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Phone.

        更新时间， 时间格式为UTC。

        :param update_time: The update_time of this Phone.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, Phone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
