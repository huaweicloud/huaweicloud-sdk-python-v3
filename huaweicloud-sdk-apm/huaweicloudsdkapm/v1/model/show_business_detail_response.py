# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBusinessDetailResponse(SdkResponse):

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
        'default': 'bool',
        'display_name': 'str',
        'name': 'str',
        'is_default': 'bool',
        'inner_domain_id': 'int',
        'eps_id': 'str',
        'creator_id': 'int',
        'descp': 'str',
        'create_time': 'str',
        'modify_time': 'str',
        'creator_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'gmt_create': 'gmt_create',
        'gmt_modify': 'gmt_modify',
        'default': 'default',
        'display_name': 'display_name',
        'name': 'name',
        'is_default': 'is_default',
        'inner_domain_id': 'inner_domain_id',
        'eps_id': 'eps_id',
        'creator_id': 'creator_id',
        'descp': 'descp',
        'create_time': 'create_time',
        'modify_time': 'modify_time',
        'creator_name': 'creator_name'
    }

    def __init__(self, id=None, gmt_create=None, gmt_modify=None, default=None, display_name=None, name=None, is_default=None, inner_domain_id=None, eps_id=None, creator_id=None, descp=None, create_time=None, modify_time=None, creator_name=None):
        r"""ShowBusinessDetailResponse

        The model defined in huaweicloud sdk

        :param id: 应用id。
        :type id: int
        :param gmt_create: 创建时间。
        :type gmt_create: date
        :param gmt_modify: 修改时间。
        :type gmt_modify: date
        :param default: 是否是默认的应用。
        :type default: bool
        :param display_name: 应用的英文名称。
        :type display_name: str
        :param name: 应用的展示名称。
        :type name: str
        :param is_default: 是否是默认的应用。
        :type is_default: bool
        :param inner_domain_id: 内部租户id。
        :type inner_domain_id: int
        :param eps_id: 企业项目的id。
        :type eps_id: str
        :param creator_id: 创建者的userId。
        :type creator_id: int
        :param descp: 应用描述说明。
        :type descp: str
        :param create_time: 创建时间。
        :type create_time: str
        :param modify_time: 修改时间。
        :type modify_time: str
        :param creator_name: 创建者的用户名。
        :type creator_name: str
        """
        
        super(ShowBusinessDetailResponse, self).__init__()

        self._id = None
        self._gmt_create = None
        self._gmt_modify = None
        self._default = None
        self._display_name = None
        self._name = None
        self._is_default = None
        self._inner_domain_id = None
        self._eps_id = None
        self._creator_id = None
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
        if default is not None:
            self.default = default
        if display_name is not None:
            self.display_name = display_name
        if name is not None:
            self.name = name
        if is_default is not None:
            self.is_default = is_default
        if inner_domain_id is not None:
            self.inner_domain_id = inner_domain_id
        if eps_id is not None:
            self.eps_id = eps_id
        if creator_id is not None:
            self.creator_id = creator_id
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
        r"""Gets the id of this ShowBusinessDetailResponse.

        应用id。

        :return: The id of this ShowBusinessDetailResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowBusinessDetailResponse.

        应用id。

        :param id: The id of this ShowBusinessDetailResponse.
        :type id: int
        """
        self._id = id

    @property
    def gmt_create(self):
        r"""Gets the gmt_create of this ShowBusinessDetailResponse.

        创建时间。

        :return: The gmt_create of this ShowBusinessDetailResponse.
        :rtype: date
        """
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        r"""Sets the gmt_create of this ShowBusinessDetailResponse.

        创建时间。

        :param gmt_create: The gmt_create of this ShowBusinessDetailResponse.
        :type gmt_create: date
        """
        self._gmt_create = gmt_create

    @property
    def gmt_modify(self):
        r"""Gets the gmt_modify of this ShowBusinessDetailResponse.

        修改时间。

        :return: The gmt_modify of this ShowBusinessDetailResponse.
        :rtype: date
        """
        return self._gmt_modify

    @gmt_modify.setter
    def gmt_modify(self, gmt_modify):
        r"""Sets the gmt_modify of this ShowBusinessDetailResponse.

        修改时间。

        :param gmt_modify: The gmt_modify of this ShowBusinessDetailResponse.
        :type gmt_modify: date
        """
        self._gmt_modify = gmt_modify

    @property
    def default(self):
        r"""Gets the default of this ShowBusinessDetailResponse.

        是否是默认的应用。

        :return: The default of this ShowBusinessDetailResponse.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this ShowBusinessDetailResponse.

        是否是默认的应用。

        :param default: The default of this ShowBusinessDetailResponse.
        :type default: bool
        """
        self._default = default

    @property
    def display_name(self):
        r"""Gets the display_name of this ShowBusinessDetailResponse.

        应用的英文名称。

        :return: The display_name of this ShowBusinessDetailResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ShowBusinessDetailResponse.

        应用的英文名称。

        :param display_name: The display_name of this ShowBusinessDetailResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def name(self):
        r"""Gets the name of this ShowBusinessDetailResponse.

        应用的展示名称。

        :return: The name of this ShowBusinessDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowBusinessDetailResponse.

        应用的展示名称。

        :param name: The name of this ShowBusinessDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def is_default(self):
        r"""Gets the is_default of this ShowBusinessDetailResponse.

        是否是默认的应用。

        :return: The is_default of this ShowBusinessDetailResponse.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this ShowBusinessDetailResponse.

        是否是默认的应用。

        :param is_default: The is_default of this ShowBusinessDetailResponse.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def inner_domain_id(self):
        r"""Gets the inner_domain_id of this ShowBusinessDetailResponse.

        内部租户id。

        :return: The inner_domain_id of this ShowBusinessDetailResponse.
        :rtype: int
        """
        return self._inner_domain_id

    @inner_domain_id.setter
    def inner_domain_id(self, inner_domain_id):
        r"""Sets the inner_domain_id of this ShowBusinessDetailResponse.

        内部租户id。

        :param inner_domain_id: The inner_domain_id of this ShowBusinessDetailResponse.
        :type inner_domain_id: int
        """
        self._inner_domain_id = inner_domain_id

    @property
    def eps_id(self):
        r"""Gets the eps_id of this ShowBusinessDetailResponse.

        企业项目的id。

        :return: The eps_id of this ShowBusinessDetailResponse.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this ShowBusinessDetailResponse.

        企业项目的id。

        :param eps_id: The eps_id of this ShowBusinessDetailResponse.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ShowBusinessDetailResponse.

        创建者的userId。

        :return: The creator_id of this ShowBusinessDetailResponse.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ShowBusinessDetailResponse.

        创建者的userId。

        :param creator_id: The creator_id of this ShowBusinessDetailResponse.
        :type creator_id: int
        """
        self._creator_id = creator_id

    @property
    def descp(self):
        r"""Gets the descp of this ShowBusinessDetailResponse.

        应用描述说明。

        :return: The descp of this ShowBusinessDetailResponse.
        :rtype: str
        """
        return self._descp

    @descp.setter
    def descp(self, descp):
        r"""Sets the descp of this ShowBusinessDetailResponse.

        应用描述说明。

        :param descp: The descp of this ShowBusinessDetailResponse.
        :type descp: str
        """
        self._descp = descp

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowBusinessDetailResponse.

        创建时间。

        :return: The create_time of this ShowBusinessDetailResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowBusinessDetailResponse.

        创建时间。

        :param create_time: The create_time of this ShowBusinessDetailResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def modify_time(self):
        r"""Gets the modify_time of this ShowBusinessDetailResponse.

        修改时间。

        :return: The modify_time of this ShowBusinessDetailResponse.
        :rtype: str
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        r"""Sets the modify_time of this ShowBusinessDetailResponse.

        修改时间。

        :param modify_time: The modify_time of this ShowBusinessDetailResponse.
        :type modify_time: str
        """
        self._modify_time = modify_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this ShowBusinessDetailResponse.

        创建者的用户名。

        :return: The creator_name of this ShowBusinessDetailResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this ShowBusinessDetailResponse.

        创建者的用户名。

        :param creator_name: The creator_name of this ShowBusinessDetailResponse.
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
        if not isinstance(other, ShowBusinessDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
