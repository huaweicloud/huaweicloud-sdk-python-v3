# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointBriefInfo:

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
        'error_msg': 'str'
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
        'error_msg': 'error_msg'
    }

    def __init__(self, visibility=None, id=None, name=None, type=None, status=None, description=None, create_time=None, update_time=None, owner=None, cap=None, reserved_resource=None, ray_resource=None, error_code=None, error_msg=None):
        r"""EndpointBriefInfo

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
        """
        
        

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

    @property
    def visibility(self):
        r"""Gets the visibility of this EndpointBriefInfo.

        可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE

        :return: The visibility of this EndpointBriefInfo.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this EndpointBriefInfo.

        可见性：  - PRIVATE：私有  - PUBLIC：公共  默认为PRIVATE

        :param visibility: The visibility of this EndpointBriefInfo.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def id(self):
        r"""Gets the id of this EndpointBriefInfo.

        Endpoint Id，32~36位的英文、数字、短横组合。

        :return: The id of this EndpointBriefInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EndpointBriefInfo.

        Endpoint Id，32~36位的英文、数字、短横组合。

        :param id: The id of this EndpointBriefInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EndpointBriefInfo.

        一个Endpoint名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this EndpointBriefInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EndpointBriefInfo.

        一个Endpoint名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this EndpointBriefInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this EndpointBriefInfo.

        :return: The type of this EndpointBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.EndpointType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EndpointBriefInfo.

        :param type: The type of this EndpointBriefInfo.
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.EndpointType`
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this EndpointBriefInfo.

        :return: The status of this EndpointBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.EndpointStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EndpointBriefInfo.

        :param status: The status of this EndpointBriefInfo.
        :type status: :class:`huaweicloudsdkdataartsfabric.v1.EndpointStatus`
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this EndpointBriefInfo.

        描述信息

        :return: The description of this EndpointBriefInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EndpointBriefInfo.

        描述信息

        :param description: The description of this EndpointBriefInfo.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this EndpointBriefInfo.

        创建时间

        :return: The create_time of this EndpointBriefInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this EndpointBriefInfo.

        创建时间

        :param create_time: The create_time of this EndpointBriefInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this EndpointBriefInfo.

        更新时间

        :return: The update_time of this EndpointBriefInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this EndpointBriefInfo.

        更新时间

        :param update_time: The update_time of this EndpointBriefInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def owner(self):
        r"""Gets the owner of this EndpointBriefInfo.

        :return: The owner of this EndpointBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this EndpointBriefInfo.

        :param owner: The owner of this EndpointBriefInfo.
        :type owner: :class:`huaweicloudsdkdataartsfabric.v1.User`
        """
        self._owner = owner

    @property
    def cap(self):
        r"""Gets the cap of this EndpointBriefInfo.

        :return: The cap of this EndpointBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.CapRef`
        """
        return self._cap

    @cap.setter
    def cap(self, cap):
        r"""Sets the cap of this EndpointBriefInfo.

        :param cap: The cap of this EndpointBriefInfo.
        :type cap: :class:`huaweicloudsdkdataartsfabric.v1.CapRef`
        """
        self._cap = cap

    @property
    def reserved_resource(self):
        r"""Gets the reserved_resource of this EndpointBriefInfo.

        :return: The reserved_resource of this EndpointBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ReservedResource`
        """
        return self._reserved_resource

    @reserved_resource.setter
    def reserved_resource(self, reserved_resource):
        r"""Sets the reserved_resource of this EndpointBriefInfo.

        :param reserved_resource: The reserved_resource of this EndpointBriefInfo.
        :type reserved_resource: :class:`huaweicloudsdkdataartsfabric.v1.ReservedResource`
        """
        self._reserved_resource = reserved_resource

    @property
    def ray_resource(self):
        r"""Gets the ray_resource of this EndpointBriefInfo.

        :return: The ray_resource of this EndpointBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayResourceInfo`
        """
        return self._ray_resource

    @ray_resource.setter
    def ray_resource(self, ray_resource):
        r"""Sets the ray_resource of this EndpointBriefInfo.

        :param ray_resource: The ray_resource of this EndpointBriefInfo.
        :type ray_resource: :class:`huaweicloudsdkdataartsfabric.v1.RayResourceInfo`
        """
        self._ray_resource = ray_resource

    @property
    def error_code(self):
        r"""Gets the error_code of this EndpointBriefInfo.

        失败状态时的错误编码

        :return: The error_code of this EndpointBriefInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this EndpointBriefInfo.

        失败状态时的错误编码

        :param error_code: The error_code of this EndpointBriefInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this EndpointBriefInfo.

        失败状态时的错误信息

        :return: The error_msg of this EndpointBriefInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this EndpointBriefInfo.

        失败状态时的错误信息

        :param error_msg: The error_msg of this EndpointBriefInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, EndpointBriefInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
