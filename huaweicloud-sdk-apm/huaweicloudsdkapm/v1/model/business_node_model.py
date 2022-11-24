# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessNodeModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default': 'bool',
        'display_name': 'str',
        'eps_id': 'str',
        'gmt_create': 'date',
        'gmt_modify': 'date',
        'id': 'int',
        'inner_domain_id': 'int',
        'is_default': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'default': 'default',
        'display_name': 'display_name',
        'eps_id': 'eps_id',
        'gmt_create': 'gmt_create',
        'gmt_modify': 'gmt_modify',
        'id': 'id',
        'inner_domain_id': 'inner_domain_id',
        'is_default': 'is_default',
        'name': 'name'
    }

    def __init__(self, default=None, display_name=None, eps_id=None, gmt_create=None, gmt_modify=None, id=None, inner_domain_id=None, is_default=None, name=None):
        """BusinessNodeModel

        The model defined in huaweicloud sdk

        :param default: 默认应用。
        :type default: bool
        :param display_name: 应用展示名称。
        :type display_name: str
        :param eps_id: 企业项目的id。
        :type eps_id: str
        :param gmt_create: 创建时间。
        :type gmt_create: date
        :param gmt_modify: 修改时间。
        :type gmt_modify: date
        :param id: 应用id。
        :type id: int
        :param inner_domain_id: 内部租户id。
        :type inner_domain_id: int
        :param is_default: 是否是默认的应用。
        :type is_default: bool
        :param name: 应用的英文名称。
        :type name: str
        """
        
        

        self._default = None
        self._display_name = None
        self._eps_id = None
        self._gmt_create = None
        self._gmt_modify = None
        self._id = None
        self._inner_domain_id = None
        self._is_default = None
        self._name = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if display_name is not None:
            self.display_name = display_name
        if eps_id is not None:
            self.eps_id = eps_id
        if gmt_create is not None:
            self.gmt_create = gmt_create
        if gmt_modify is not None:
            self.gmt_modify = gmt_modify
        if id is not None:
            self.id = id
        if inner_domain_id is not None:
            self.inner_domain_id = inner_domain_id
        if is_default is not None:
            self.is_default = is_default
        if name is not None:
            self.name = name

    @property
    def default(self):
        """Gets the default of this BusinessNodeModel.

        默认应用。

        :return: The default of this BusinessNodeModel.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this BusinessNodeModel.

        默认应用。

        :param default: The default of this BusinessNodeModel.
        :type default: bool
        """
        self._default = default

    @property
    def display_name(self):
        """Gets the display_name of this BusinessNodeModel.

        应用展示名称。

        :return: The display_name of this BusinessNodeModel.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BusinessNodeModel.

        应用展示名称。

        :param display_name: The display_name of this BusinessNodeModel.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def eps_id(self):
        """Gets the eps_id of this BusinessNodeModel.

        企业项目的id。

        :return: The eps_id of this BusinessNodeModel.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        """Sets the eps_id of this BusinessNodeModel.

        企业项目的id。

        :param eps_id: The eps_id of this BusinessNodeModel.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def gmt_create(self):
        """Gets the gmt_create of this BusinessNodeModel.

        创建时间。

        :return: The gmt_create of this BusinessNodeModel.
        :rtype: date
        """
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        """Sets the gmt_create of this BusinessNodeModel.

        创建时间。

        :param gmt_create: The gmt_create of this BusinessNodeModel.
        :type gmt_create: date
        """
        self._gmt_create = gmt_create

    @property
    def gmt_modify(self):
        """Gets the gmt_modify of this BusinessNodeModel.

        修改时间。

        :return: The gmt_modify of this BusinessNodeModel.
        :rtype: date
        """
        return self._gmt_modify

    @gmt_modify.setter
    def gmt_modify(self, gmt_modify):
        """Sets the gmt_modify of this BusinessNodeModel.

        修改时间。

        :param gmt_modify: The gmt_modify of this BusinessNodeModel.
        :type gmt_modify: date
        """
        self._gmt_modify = gmt_modify

    @property
    def id(self):
        """Gets the id of this BusinessNodeModel.

        应用id。

        :return: The id of this BusinessNodeModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BusinessNodeModel.

        应用id。

        :param id: The id of this BusinessNodeModel.
        :type id: int
        """
        self._id = id

    @property
    def inner_domain_id(self):
        """Gets the inner_domain_id of this BusinessNodeModel.

        内部租户id。

        :return: The inner_domain_id of this BusinessNodeModel.
        :rtype: int
        """
        return self._inner_domain_id

    @inner_domain_id.setter
    def inner_domain_id(self, inner_domain_id):
        """Sets the inner_domain_id of this BusinessNodeModel.

        内部租户id。

        :param inner_domain_id: The inner_domain_id of this BusinessNodeModel.
        :type inner_domain_id: int
        """
        self._inner_domain_id = inner_domain_id

    @property
    def is_default(self):
        """Gets the is_default of this BusinessNodeModel.

        是否是默认的应用。

        :return: The is_default of this BusinessNodeModel.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this BusinessNodeModel.

        是否是默认的应用。

        :param is_default: The is_default of this BusinessNodeModel.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def name(self):
        """Gets the name of this BusinessNodeModel.

        应用的英文名称。

        :return: The name of this BusinessNodeModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BusinessNodeModel.

        应用的英文名称。

        :param name: The name of this BusinessNodeModel.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, BusinessNodeModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
