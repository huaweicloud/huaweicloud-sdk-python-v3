# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'visibility': 'str',
        'id': 'str',
        'name': 'str',
        'type': 'EndpointType',
        'status': 'EndpointStatus',
        'description': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'owner': 'User',
        'cap': 'CapRef',
        'reserved_resource': 'ReservedResource',
        'ray_resource': 'RayResourceInfo',
        'error_code': 'str',
        'error_msg': 'str',
        'urls': 'list[Url]',
        'log_config': 'LogConfigInfo',
        'business_engine_instance_ids': 'list[str]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'visibility': 'visibility',
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'status': 'status',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'owner': 'owner',
        'cap': 'cap',
        'reserved_resource': 'reserved_resource',
        'ray_resource': 'ray_resource',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'urls': 'urls',
        'log_config': 'log_config',
        'business_engine_instance_ids': 'business_engine_instance_ids',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, visibility=None, id=None, name=None, type=None, status=None, description=None, create_time=None, update_time=None, owner=None, cap=None, reserved_resource=None, ray_resource=None, error_code=None, error_msg=None, urls=None, log_config=None, business_engine_instance_ids=None, x_request_id=None):
        r"""CreateEndpointResponse

        The model defined in huaweicloud sdk

        :param visibility: 可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE
        :type visibility: str
        :param id: Endpoint Id，32~36位的英文、数字、短横组合。
        :type id: str
        :param name: 一个Endpoint名称，只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param type: 
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.EndpointType`
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsfabric.v1.EndpointStatus`
        :param description: 描述信息
        :type description: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param owner: 
        :type owner: :class:`huaweicloudsdkdataartsfabric.v1.User`
        :param cap: 
        :type cap: :class:`huaweicloudsdkdataartsfabric.v1.CapRef`
        :param reserved_resource: 
        :type reserved_resource: :class:`huaweicloudsdkdataartsfabric.v1.ReservedResource`
        :param ray_resource: 
        :type ray_resource: :class:`huaweicloudsdkdataartsfabric.v1.RayResourceInfo`
        :param error_code: 失败状态时的错误编码
        :type error_code: str
        :param error_msg: 失败状态时的错误信息
        :type error_msg: str
        :param urls: 调用地址
        :type urls: list[:class:`huaweicloudsdkdataartsfabric.v1.Url`]
        :param log_config: 
        :type log_config: :class:`huaweicloudsdkdataartsfabric.v1.LogConfigInfo`
        :param business_engine_instance_ids: 引擎实例id列表
        :type business_engine_instance_ids: list[str]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateEndpointResponse, self).__init__()

        self._visibility = None
        self._id = None
        self._name = None
        self._type = None
        self._status = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._owner = None
        self._cap = None
        self._reserved_resource = None
        self._ray_resource = None
        self._error_code = None
        self._error_msg = None
        self._urls = None
        self._log_config = None
        self._business_engine_instance_ids = None
        self._x_request_id = None
        self.discriminator = None

        if visibility is not None:
            self.visibility = visibility
        self.id = id
        self.name = name
        self.type = type
        self.status = status
        if description is not None:
            self.description = description
        self.create_time = create_time
        self.update_time = update_time
        self.owner = owner
        if cap is not None:
            self.cap = cap
        if reserved_resource is not None:
            self.reserved_resource = reserved_resource
        if ray_resource is not None:
            self.ray_resource = ray_resource
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if urls is not None:
            self.urls = urls
        if log_config is not None:
            self.log_config = log_config
        if business_engine_instance_ids is not None:
            self.business_engine_instance_ids = business_engine_instance_ids
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def visibility(self):
        r"""Gets the visibility of this CreateEndpointResponse.

        可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE

        :return: The visibility of this CreateEndpointResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this CreateEndpointResponse.

        可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE

        :param visibility: The visibility of this CreateEndpointResponse.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def id(self):
        r"""Gets the id of this CreateEndpointResponse.

        Endpoint Id，32~36位的英文、数字、短横组合。

        :return: The id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateEndpointResponse.

        Endpoint Id，32~36位的英文、数字、短横组合。

        :param id: The id of this CreateEndpointResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateEndpointResponse.

        一个Endpoint名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this CreateEndpointResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateEndpointResponse.

        一个Endpoint名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this CreateEndpointResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CreateEndpointResponse.

        :return: The type of this CreateEndpointResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.EndpointType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateEndpointResponse.

        :param type: The type of this CreateEndpointResponse.
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.EndpointType`
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this CreateEndpointResponse.

        :return: The status of this CreateEndpointResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.EndpointStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateEndpointResponse.

        :param status: The status of this CreateEndpointResponse.
        :type status: :class:`huaweicloudsdkdataartsfabric.v1.EndpointStatus`
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this CreateEndpointResponse.

        描述信息

        :return: The description of this CreateEndpointResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateEndpointResponse.

        描述信息

        :param description: The description of this CreateEndpointResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateEndpointResponse.

        创建时间

        :return: The create_time of this CreateEndpointResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateEndpointResponse.

        创建时间

        :param create_time: The create_time of this CreateEndpointResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateEndpointResponse.

        更新时间

        :return: The update_time of this CreateEndpointResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateEndpointResponse.

        更新时间

        :param update_time: The update_time of this CreateEndpointResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def owner(self):
        r"""Gets the owner of this CreateEndpointResponse.

        :return: The owner of this CreateEndpointResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this CreateEndpointResponse.

        :param owner: The owner of this CreateEndpointResponse.
        :type owner: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        self._owner = owner

    @property
    def cap(self):
        r"""Gets the cap of this CreateEndpointResponse.

        :return: The cap of this CreateEndpointResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.CapRef`
        """
        return self._cap

    @cap.setter
    def cap(self, cap):
        r"""Sets the cap of this CreateEndpointResponse.

        :param cap: The cap of this CreateEndpointResponse.
        :type cap: :class:`huaweicloudsdkdataartsfabric.v1.CapRef`
        """
        self._cap = cap

    @property
    def reserved_resource(self):
        r"""Gets the reserved_resource of this CreateEndpointResponse.

        :return: The reserved_resource of this CreateEndpointResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ReservedResource`
        """
        return self._reserved_resource

    @reserved_resource.setter
    def reserved_resource(self, reserved_resource):
        r"""Sets the reserved_resource of this CreateEndpointResponse.

        :param reserved_resource: The reserved_resource of this CreateEndpointResponse.
        :type reserved_resource: :class:`huaweicloudsdkdataartsfabric.v1.ReservedResource`
        """
        self._reserved_resource = reserved_resource

    @property
    def ray_resource(self):
        r"""Gets the ray_resource of this CreateEndpointResponse.

        :return: The ray_resource of this CreateEndpointResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayResourceInfo`
        """
        return self._ray_resource

    @ray_resource.setter
    def ray_resource(self, ray_resource):
        r"""Sets the ray_resource of this CreateEndpointResponse.

        :param ray_resource: The ray_resource of this CreateEndpointResponse.
        :type ray_resource: :class:`huaweicloudsdkdataartsfabric.v1.RayResourceInfo`
        """
        self._ray_resource = ray_resource

    @property
    def error_code(self):
        r"""Gets the error_code of this CreateEndpointResponse.

        失败状态时的错误编码

        :return: The error_code of this CreateEndpointResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this CreateEndpointResponse.

        失败状态时的错误编码

        :param error_code: The error_code of this CreateEndpointResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this CreateEndpointResponse.

        失败状态时的错误信息

        :return: The error_msg of this CreateEndpointResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this CreateEndpointResponse.

        失败状态时的错误信息

        :param error_msg: The error_msg of this CreateEndpointResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def urls(self):
        r"""Gets the urls of this CreateEndpointResponse.

        调用地址

        :return: The urls of this CreateEndpointResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.Url`]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        r"""Sets the urls of this CreateEndpointResponse.

        调用地址

        :param urls: The urls of this CreateEndpointResponse.
        :type urls: list[:class:`huaweicloudsdkdataartsfabric.v1.Url`]
        """
        self._urls = urls

    @property
    def log_config(self):
        r"""Gets the log_config of this CreateEndpointResponse.

        :return: The log_config of this CreateEndpointResponse.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.LogConfigInfo`
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        r"""Sets the log_config of this CreateEndpointResponse.

        :param log_config: The log_config of this CreateEndpointResponse.
        :type log_config: :class:`huaweicloudsdkdataartsfabric.v1.LogConfigInfo`
        """
        self._log_config = log_config

    @property
    def business_engine_instance_ids(self):
        r"""Gets the business_engine_instance_ids of this CreateEndpointResponse.

        引擎实例id列表

        :return: The business_engine_instance_ids of this CreateEndpointResponse.
        :rtype: list[str]
        """
        return self._business_engine_instance_ids

    @business_engine_instance_ids.setter
    def business_engine_instance_ids(self, business_engine_instance_ids):
        r"""Sets the business_engine_instance_ids of this CreateEndpointResponse.

        引擎实例id列表

        :param business_engine_instance_ids: The business_engine_instance_ids of this CreateEndpointResponse.
        :type business_engine_instance_ids: list[str]
        """
        self._business_engine_instance_ids = business_engine_instance_ids

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateEndpointResponse.

        :return: The x_request_id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateEndpointResponse.

        :param x_request_id: The x_request_id of this CreateEndpointResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CreateEndpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
