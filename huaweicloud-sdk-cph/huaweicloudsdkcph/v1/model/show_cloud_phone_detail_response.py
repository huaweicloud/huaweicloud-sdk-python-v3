# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCloudPhoneDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'phone_name': 'str',
        'server_id': 'str',
        'phone_id': 'str',
        'image_id': 'str',
        'vnc_enable': 'str',
        'phone_model_name': 'str',
        'status': 'int',
        'access_infos': 'list[object]',
        '_property': 'str',
        'metadata': 'object',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'phone_name': 'phone_name',
        'server_id': 'server_id',
        'phone_id': 'phone_id',
        'image_id': 'image_id',
        'vnc_enable': 'vnc_enable',
        'phone_model_name': 'phone_model_name',
        'status': 'status',
        'access_infos': 'access_infos',
        '_property': 'property',
        'metadata': 'metadata',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, request_id=None, phone_name=None, server_id=None, phone_id=None, image_id=None, vnc_enable=None, phone_model_name=None, status=None, access_infos=None, _property=None, metadata=None, create_time=None, update_time=None):
        """ShowCloudPhoneDetailResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID
        :type request_id: str
        :param phone_name: 云手机名称，不超过65个字符
        :type phone_name: str
        :param server_id: 云手机服务器ID，不超过32个字节
        :type server_id: str
        :param phone_id: 云手机的唯一标识，不超过32个字节
        :type phone_id: str
        :param image_id: 云手机镜像ID，不超过32个字节
        :type image_id: str
        :param vnc_enable: 云手机是否开启VNC服务 - true：开启 - false：关闭
        :type vnc_enable: str
        :param phone_model_name: 云手机规格名称，不超过64个字节
        :type phone_model_name: str
        :param status: 云手机状态 - 0：创建中 - 1：创建中 - 2：运行中 - 3：重置中 - 4：重启中 - 6：冻结 - 7：正在关机 - 8：已关机 - -5：重置失败 - -6：重启失败 - -7：手机异常 - -8：创建失败 - -9：关机失败
        :type status: int
        :param access_infos: 云手机访问信息
        :type access_infos: list[object]
        :param _property: 云手机属性字符串，不超过2048个字节
        :type _property: str
        :param metadata: 订单以及产品相关信息
        :type metadata: :class:`huaweicloudsdkcph.v1.object`
        :param create_time: 创建时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ
        :type create_time: str
        :param update_time: 更新时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。
        :type update_time: str
        """
        
        super(ShowCloudPhoneDetailResponse, self).__init__()

        self._request_id = None
        self._phone_name = None
        self._server_id = None
        self._phone_id = None
        self._image_id = None
        self._vnc_enable = None
        self._phone_model_name = None
        self._status = None
        self._access_infos = None
        self.__property = None
        self._metadata = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.request_id = request_id
        self.phone_name = phone_name
        self.server_id = server_id
        self.phone_id = phone_id
        self.image_id = image_id
        self.vnc_enable = vnc_enable
        self.phone_model_name = phone_model_name
        self.status = status
        self.access_infos = access_infos
        self._property = _property
        self.metadata = metadata
        self.create_time = create_time
        self.update_time = update_time

    @property
    def request_id(self):
        """Gets the request_id of this ShowCloudPhoneDetailResponse.

        请求的唯一标识ID

        :return: The request_id of this ShowCloudPhoneDetailResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowCloudPhoneDetailResponse.

        请求的唯一标识ID

        :param request_id: The request_id of this ShowCloudPhoneDetailResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def phone_name(self):
        """Gets the phone_name of this ShowCloudPhoneDetailResponse.

        云手机名称，不超过65个字符

        :return: The phone_name of this ShowCloudPhoneDetailResponse.
        :rtype: str
        """
        return self._phone_name

    @phone_name.setter
    def phone_name(self, phone_name):
        """Sets the phone_name of this ShowCloudPhoneDetailResponse.

        云手机名称，不超过65个字符

        :param phone_name: The phone_name of this ShowCloudPhoneDetailResponse.
        :type phone_name: str
        """
        self._phone_name = phone_name

    @property
    def server_id(self):
        """Gets the server_id of this ShowCloudPhoneDetailResponse.

        云手机服务器ID，不超过32个字节

        :return: The server_id of this ShowCloudPhoneDetailResponse.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ShowCloudPhoneDetailResponse.

        云手机服务器ID，不超过32个字节

        :param server_id: The server_id of this ShowCloudPhoneDetailResponse.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def phone_id(self):
        """Gets the phone_id of this ShowCloudPhoneDetailResponse.

        云手机的唯一标识，不超过32个字节

        :return: The phone_id of this ShowCloudPhoneDetailResponse.
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        """Sets the phone_id of this ShowCloudPhoneDetailResponse.

        云手机的唯一标识，不超过32个字节

        :param phone_id: The phone_id of this ShowCloudPhoneDetailResponse.
        :type phone_id: str
        """
        self._phone_id = phone_id

    @property
    def image_id(self):
        """Gets the image_id of this ShowCloudPhoneDetailResponse.

        云手机镜像ID，不超过32个字节

        :return: The image_id of this ShowCloudPhoneDetailResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ShowCloudPhoneDetailResponse.

        云手机镜像ID，不超过32个字节

        :param image_id: The image_id of this ShowCloudPhoneDetailResponse.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def vnc_enable(self):
        """Gets the vnc_enable of this ShowCloudPhoneDetailResponse.

        云手机是否开启VNC服务 - true：开启 - false：关闭

        :return: The vnc_enable of this ShowCloudPhoneDetailResponse.
        :rtype: str
        """
        return self._vnc_enable

    @vnc_enable.setter
    def vnc_enable(self, vnc_enable):
        """Sets the vnc_enable of this ShowCloudPhoneDetailResponse.

        云手机是否开启VNC服务 - true：开启 - false：关闭

        :param vnc_enable: The vnc_enable of this ShowCloudPhoneDetailResponse.
        :type vnc_enable: str
        """
        self._vnc_enable = vnc_enable

    @property
    def phone_model_name(self):
        """Gets the phone_model_name of this ShowCloudPhoneDetailResponse.

        云手机规格名称，不超过64个字节

        :return: The phone_model_name of this ShowCloudPhoneDetailResponse.
        :rtype: str
        """
        return self._phone_model_name

    @phone_model_name.setter
    def phone_model_name(self, phone_model_name):
        """Sets the phone_model_name of this ShowCloudPhoneDetailResponse.

        云手机规格名称，不超过64个字节

        :param phone_model_name: The phone_model_name of this ShowCloudPhoneDetailResponse.
        :type phone_model_name: str
        """
        self._phone_model_name = phone_model_name

    @property
    def status(self):
        """Gets the status of this ShowCloudPhoneDetailResponse.

        云手机状态 - 0：创建中 - 1：创建中 - 2：运行中 - 3：重置中 - 4：重启中 - 6：冻结 - 7：正在关机 - 8：已关机 - -5：重置失败 - -6：重启失败 - -7：手机异常 - -8：创建失败 - -9：关机失败

        :return: The status of this ShowCloudPhoneDetailResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowCloudPhoneDetailResponse.

        云手机状态 - 0：创建中 - 1：创建中 - 2：运行中 - 3：重置中 - 4：重启中 - 6：冻结 - 7：正在关机 - 8：已关机 - -5：重置失败 - -6：重启失败 - -7：手机异常 - -8：创建失败 - -9：关机失败

        :param status: The status of this ShowCloudPhoneDetailResponse.
        :type status: int
        """
        self._status = status

    @property
    def access_infos(self):
        """Gets the access_infos of this ShowCloudPhoneDetailResponse.

        云手机访问信息

        :return: The access_infos of this ShowCloudPhoneDetailResponse.
        :rtype: list[object]
        """
        return self._access_infos

    @access_infos.setter
    def access_infos(self, access_infos):
        """Sets the access_infos of this ShowCloudPhoneDetailResponse.

        云手机访问信息

        :param access_infos: The access_infos of this ShowCloudPhoneDetailResponse.
        :type access_infos: list[object]
        """
        self._access_infos = access_infos

    @property
    def _property(self):
        """Gets the _property of this ShowCloudPhoneDetailResponse.

        云手机属性字符串，不超过2048个字节

        :return: The _property of this ShowCloudPhoneDetailResponse.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this ShowCloudPhoneDetailResponse.

        云手机属性字符串，不超过2048个字节

        :param _property: The _property of this ShowCloudPhoneDetailResponse.
        :type _property: str
        """
        self.__property = _property

    @property
    def metadata(self):
        """Gets the metadata of this ShowCloudPhoneDetailResponse.

        订单以及产品相关信息

        :return: The metadata of this ShowCloudPhoneDetailResponse.
        :rtype: :class:`huaweicloudsdkcph.v1.object`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ShowCloudPhoneDetailResponse.

        订单以及产品相关信息

        :param metadata: The metadata of this ShowCloudPhoneDetailResponse.
        :type metadata: :class:`huaweicloudsdkcph.v1.object`
        """
        self._metadata = metadata

    @property
    def create_time(self):
        """Gets the create_time of this ShowCloudPhoneDetailResponse.

        创建时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ

        :return: The create_time of this ShowCloudPhoneDetailResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowCloudPhoneDetailResponse.

        创建时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ

        :param create_time: The create_time of this ShowCloudPhoneDetailResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowCloudPhoneDetailResponse.

        更新时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :return: The update_time of this ShowCloudPhoneDetailResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowCloudPhoneDetailResponse.

        更新时间 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :param update_time: The update_time of this ShowCloudPhoneDetailResponse.
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
        if not isinstance(other, ShowCloudPhoneDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
