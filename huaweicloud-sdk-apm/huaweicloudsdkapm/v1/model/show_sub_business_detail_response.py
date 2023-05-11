# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubBusinessDetailResponse(SdkResponse):

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
        'gmt_create': 'date',
        'gmt_modify': 'date',
        'parent_id': 'int',
        'name': 'str',
        'display_name': 'str',
        'business_id': 'int',
        'inner_domain_id': 'int',
        'creator_id': 'int',
        'uuid': 'str',
        'descp': 'str',
        'create_time': 'str',
        'modify_time': 'str',
        'creator_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'gmt_create': 'gmt_create',
        'gmt_modify': 'gmt_modify',
        'parent_id': 'parent_id',
        'name': 'name',
        'display_name': 'display_name',
        'business_id': 'business_id',
        'inner_domain_id': 'inner_domain_id',
        'creator_id': 'creator_id',
        'uuid': 'uuid',
        'descp': 'descp',
        'create_time': 'create_time',
        'modify_time': 'modify_time',
        'creator_name': 'creator_name'
    }

    def __init__(self, id=None, gmt_create=None, gmt_modify=None, parent_id=None, name=None, display_name=None, business_id=None, inner_domain_id=None, creator_id=None, uuid=None, descp=None, create_time=None, modify_time=None, creator_name=None):
        """ShowSubBusinessDetailResponse

        The model defined in huaweicloud sdk

        :param id: 子应用id。
        :type id: int
        :param gmt_create: 创建时间。
        :type gmt_create: date
        :param gmt_modify: 修改时间。
        :type gmt_modify: date
        :param parent_id: 父亲的子应用id。
        :type parent_id: int
        :param name: 子应用的英文名称。
        :type name: str
        :param display_name: 子应用的展示名称。
        :type display_name: str
        :param business_id: 所属应用id。
        :type business_id: int
        :param inner_domain_id: 内部租户id。
        :type inner_domain_id: int
        :param creator_id: 创建者的userId。
        :type creator_id: int
        :param uuid: 应用的UUID。
        :type uuid: str
        :param descp: 应用描述说明。
        :type descp: str
        :param create_time: 创建时间。
        :type create_time: str
        :param modify_time: 修改时间。
        :type modify_time: str
        :param creator_name: 创建者的用户名。
        :type creator_name: str
        """
        
        super(ShowSubBusinessDetailResponse, self).__init__()

        self._id = None
        self._gmt_create = None
        self._gmt_modify = None
        self._parent_id = None
        self._name = None
        self._display_name = None
        self._business_id = None
        self._inner_domain_id = None
        self._creator_id = None
        self._uuid = None
        self._descp = None
        self._create_time = None
        self._modify_time = None
        self._creator_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if gmt_create is not None:
            self.gmt_create = gmt_create
        if gmt_modify is not None:
            self.gmt_modify = gmt_modify
        if parent_id is not None:
            self.parent_id = parent_id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if business_id is not None:
            self.business_id = business_id
        if inner_domain_id is not None:
            self.inner_domain_id = inner_domain_id
        if creator_id is not None:
            self.creator_id = creator_id
        if uuid is not None:
            self.uuid = uuid
        if descp is not None:
            self.descp = descp
        if create_time is not None:
            self.create_time = create_time
        if modify_time is not None:
            self.modify_time = modify_time
        if creator_name is not None:
            self.creator_name = creator_name

    @property
    def id(self):
        """Gets the id of this ShowSubBusinessDetailResponse.

        子应用id。

        :return: The id of this ShowSubBusinessDetailResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowSubBusinessDetailResponse.

        子应用id。

        :param id: The id of this ShowSubBusinessDetailResponse.
        :type id: int
        """
        self._id = id

    @property
    def gmt_create(self):
        """Gets the gmt_create of this ShowSubBusinessDetailResponse.

        创建时间。

        :return: The gmt_create of this ShowSubBusinessDetailResponse.
        :rtype: date
        """
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        """Sets the gmt_create of this ShowSubBusinessDetailResponse.

        创建时间。

        :param gmt_create: The gmt_create of this ShowSubBusinessDetailResponse.
        :type gmt_create: date
        """
        self._gmt_create = gmt_create

    @property
    def gmt_modify(self):
        """Gets the gmt_modify of this ShowSubBusinessDetailResponse.

        修改时间。

        :return: The gmt_modify of this ShowSubBusinessDetailResponse.
        :rtype: date
        """
        return self._gmt_modify

    @gmt_modify.setter
    def gmt_modify(self, gmt_modify):
        """Sets the gmt_modify of this ShowSubBusinessDetailResponse.

        修改时间。

        :param gmt_modify: The gmt_modify of this ShowSubBusinessDetailResponse.
        :type gmt_modify: date
        """
        self._gmt_modify = gmt_modify

    @property
    def parent_id(self):
        """Gets the parent_id of this ShowSubBusinessDetailResponse.

        父亲的子应用id。

        :return: The parent_id of this ShowSubBusinessDetailResponse.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ShowSubBusinessDetailResponse.

        父亲的子应用id。

        :param parent_id: The parent_id of this ShowSubBusinessDetailResponse.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this ShowSubBusinessDetailResponse.

        子应用的英文名称。

        :return: The name of this ShowSubBusinessDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowSubBusinessDetailResponse.

        子应用的英文名称。

        :param name: The name of this ShowSubBusinessDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this ShowSubBusinessDetailResponse.

        子应用的展示名称。

        :return: The display_name of this ShowSubBusinessDetailResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ShowSubBusinessDetailResponse.

        子应用的展示名称。

        :param display_name: The display_name of this ShowSubBusinessDetailResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def business_id(self):
        """Gets the business_id of this ShowSubBusinessDetailResponse.

        所属应用id。

        :return: The business_id of this ShowSubBusinessDetailResponse.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this ShowSubBusinessDetailResponse.

        所属应用id。

        :param business_id: The business_id of this ShowSubBusinessDetailResponse.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def inner_domain_id(self):
        """Gets the inner_domain_id of this ShowSubBusinessDetailResponse.

        内部租户id。

        :return: The inner_domain_id of this ShowSubBusinessDetailResponse.
        :rtype: int
        """
        return self._inner_domain_id

    @inner_domain_id.setter
    def inner_domain_id(self, inner_domain_id):
        """Sets the inner_domain_id of this ShowSubBusinessDetailResponse.

        内部租户id。

        :param inner_domain_id: The inner_domain_id of this ShowSubBusinessDetailResponse.
        :type inner_domain_id: int
        """
        self._inner_domain_id = inner_domain_id

    @property
    def creator_id(self):
        """Gets the creator_id of this ShowSubBusinessDetailResponse.

        创建者的userId。

        :return: The creator_id of this ShowSubBusinessDetailResponse.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this ShowSubBusinessDetailResponse.

        创建者的userId。

        :param creator_id: The creator_id of this ShowSubBusinessDetailResponse.
        :type creator_id: int
        """
        self._creator_id = creator_id

    @property
    def uuid(self):
        """Gets the uuid of this ShowSubBusinessDetailResponse.

        应用的UUID。

        :return: The uuid of this ShowSubBusinessDetailResponse.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ShowSubBusinessDetailResponse.

        应用的UUID。

        :param uuid: The uuid of this ShowSubBusinessDetailResponse.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def descp(self):
        """Gets the descp of this ShowSubBusinessDetailResponse.

        应用描述说明。

        :return: The descp of this ShowSubBusinessDetailResponse.
        :rtype: str
        """
        return self._descp

    @descp.setter
    def descp(self, descp):
        """Sets the descp of this ShowSubBusinessDetailResponse.

        应用描述说明。

        :param descp: The descp of this ShowSubBusinessDetailResponse.
        :type descp: str
        """
        self._descp = descp

    @property
    def create_time(self):
        """Gets the create_time of this ShowSubBusinessDetailResponse.

        创建时间。

        :return: The create_time of this ShowSubBusinessDetailResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowSubBusinessDetailResponse.

        创建时间。

        :param create_time: The create_time of this ShowSubBusinessDetailResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def modify_time(self):
        """Gets the modify_time of this ShowSubBusinessDetailResponse.

        修改时间。

        :return: The modify_time of this ShowSubBusinessDetailResponse.
        :rtype: str
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        """Sets the modify_time of this ShowSubBusinessDetailResponse.

        修改时间。

        :param modify_time: The modify_time of this ShowSubBusinessDetailResponse.
        :type modify_time: str
        """
        self._modify_time = modify_time

    @property
    def creator_name(self):
        """Gets the creator_name of this ShowSubBusinessDetailResponse.

        创建者的用户名。

        :return: The creator_name of this ShowSubBusinessDetailResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ShowSubBusinessDetailResponse.

        创建者的用户名。

        :param creator_name: The creator_name of this ShowSubBusinessDetailResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

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
        if not isinstance(other, ShowSubBusinessDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
