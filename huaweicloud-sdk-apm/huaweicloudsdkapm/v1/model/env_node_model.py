# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvNodeModel:

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
        'app_id': 'int',
        'business_name': 'str',
        'inner_domain_id': 'int',
        'name': 'str',
        'is_default': 'bool',
        'app_name': 'str',
        'business_id': 'int',
        'region': 'str'
    }

    attribute_map = {
        'id': 'id',
        'gmt_create': 'gmt_create',
        'gmt_modify': 'gmt_modify',
        'app_id': 'app_id',
        'business_name': 'business_name',
        'inner_domain_id': 'inner_domain_id',
        'name': 'name',
        'is_default': 'is_default',
        'app_name': 'app_name',
        'business_id': 'business_id',
        'region': 'region'
    }

    def __init__(self, id=None, gmt_create=None, gmt_modify=None, app_id=None, business_name=None, inner_domain_id=None, name=None, is_default=None, app_name=None, business_id=None, region=None):
        r"""EnvNodeModel

        The model defined in huaweicloud sdk

        :param id: 环境id。
        :type id: int
        :param gmt_create: 创建时间。
        :type gmt_create: date
        :param gmt_modify: 修改时间。
        :type gmt_modify: date
        :param app_id: 组件id。
        :type app_id: int
        :param business_name: 应用名称。
        :type business_name: str
        :param inner_domain_id: 租户id。
        :type inner_domain_id: int
        :param name: 环境名称。
        :type name: str
        :param is_default: 是否是默认环境。
        :type is_default: bool
        :param app_name: 组件名称。
        :type app_name: str
        :param business_id: 应用id。
        :type business_id: int
        :param region: 区域。
        :type region: str
        """
        
        

        self._id = None
        self._gmt_create = None
        self._gmt_modify = None
        self._app_id = None
        self._business_name = None
        self._inner_domain_id = None
        self._name = None
        self._is_default = None
        self._app_name = None
        self._business_id = None
        self._region = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if gmt_create is not None:
            self.gmt_create = gmt_create
        if gmt_modify is not None:
            self.gmt_modify = gmt_modify
        if app_id is not None:
            self.app_id = app_id
        if business_name is not None:
            self.business_name = business_name
        if inner_domain_id is not None:
            self.inner_domain_id = inner_domain_id
        if name is not None:
            self.name = name
        if is_default is not None:
            self.is_default = is_default
        if app_name is not None:
            self.app_name = app_name
        if business_id is not None:
            self.business_id = business_id
        if region is not None:
            self.region = region

    @property
    def id(self):
        r"""Gets the id of this EnvNodeModel.

        环境id。

        :return: The id of this EnvNodeModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EnvNodeModel.

        环境id。

        :param id: The id of this EnvNodeModel.
        :type id: int
        """
        self._id = id

    @property
    def gmt_create(self):
        r"""Gets the gmt_create of this EnvNodeModel.

        创建时间。

        :return: The gmt_create of this EnvNodeModel.
        :rtype: date
        """
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        r"""Sets the gmt_create of this EnvNodeModel.

        创建时间。

        :param gmt_create: The gmt_create of this EnvNodeModel.
        :type gmt_create: date
        """
        self._gmt_create = gmt_create

    @property
    def gmt_modify(self):
        r"""Gets the gmt_modify of this EnvNodeModel.

        修改时间。

        :return: The gmt_modify of this EnvNodeModel.
        :rtype: date
        """
        return self._gmt_modify

    @gmt_modify.setter
    def gmt_modify(self, gmt_modify):
        r"""Sets the gmt_modify of this EnvNodeModel.

        修改时间。

        :param gmt_modify: The gmt_modify of this EnvNodeModel.
        :type gmt_modify: date
        """
        self._gmt_modify = gmt_modify

    @property
    def app_id(self):
        r"""Gets the app_id of this EnvNodeModel.

        组件id。

        :return: The app_id of this EnvNodeModel.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this EnvNodeModel.

        组件id。

        :param app_id: The app_id of this EnvNodeModel.
        :type app_id: int
        """
        self._app_id = app_id

    @property
    def business_name(self):
        r"""Gets the business_name of this EnvNodeModel.

        应用名称。

        :return: The business_name of this EnvNodeModel.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        r"""Sets the business_name of this EnvNodeModel.

        应用名称。

        :param business_name: The business_name of this EnvNodeModel.
        :type business_name: str
        """
        self._business_name = business_name

    @property
    def inner_domain_id(self):
        r"""Gets the inner_domain_id of this EnvNodeModel.

        租户id。

        :return: The inner_domain_id of this EnvNodeModel.
        :rtype: int
        """
        return self._inner_domain_id

    @inner_domain_id.setter
    def inner_domain_id(self, inner_domain_id):
        r"""Sets the inner_domain_id of this EnvNodeModel.

        租户id。

        :param inner_domain_id: The inner_domain_id of this EnvNodeModel.
        :type inner_domain_id: int
        """
        self._inner_domain_id = inner_domain_id

    @property
    def name(self):
        r"""Gets the name of this EnvNodeModel.

        环境名称。

        :return: The name of this EnvNodeModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnvNodeModel.

        环境名称。

        :param name: The name of this EnvNodeModel.
        :type name: str
        """
        self._name = name

    @property
    def is_default(self):
        r"""Gets the is_default of this EnvNodeModel.

        是否是默认环境。

        :return: The is_default of this EnvNodeModel.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this EnvNodeModel.

        是否是默认环境。

        :param is_default: The is_default of this EnvNodeModel.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def app_name(self):
        r"""Gets the app_name of this EnvNodeModel.

        组件名称。

        :return: The app_name of this EnvNodeModel.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this EnvNodeModel.

        组件名称。

        :param app_name: The app_name of this EnvNodeModel.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def business_id(self):
        r"""Gets the business_id of this EnvNodeModel.

        应用id。

        :return: The business_id of this EnvNodeModel.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        r"""Sets the business_id of this EnvNodeModel.

        应用id。

        :param business_id: The business_id of this EnvNodeModel.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def region(self):
        r"""Gets the region of this EnvNodeModel.

        区域。

        :return: The region of this EnvNodeModel.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this EnvNodeModel.

        区域。

        :param region: The region of this EnvNodeModel.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, EnvNodeModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
