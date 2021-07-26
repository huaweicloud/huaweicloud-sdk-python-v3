# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneListPermissionsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'domain_id': 'str',
        'page': 'int',
        'per_page': 'int',
        'permission_type': 'str',
        'display_name': 'str',
        'type': 'str',
        'catalog': 'str'
    }

    attribute_map = {
        'name': 'name',
        'domain_id': 'domain_id',
        'page': 'page',
        'per_page': 'per_page',
        'permission_type': 'permission_type',
        'display_name': 'display_name',
        'type': 'type',
        'catalog': 'catalog'
    }

    def __init__(self, name=None, domain_id=None, page=None, per_page=None, permission_type=None, display_name=None, type=None, catalog=None):
        """KeystoneListPermissionsRequest - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._domain_id = None
        self._page = None
        self._per_page = None
        self._permission_type = None
        self._display_name = None
        self._type = None
        self._catalog = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if domain_id is not None:
            self.domain_id = domain_id
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page
        if permission_type is not None:
            self.permission_type = permission_type
        if display_name is not None:
            self.display_name = display_name
        if type is not None:
            self.type = type
        if catalog is not None:
            self.catalog = catalog

    @property
    def name(self):
        """Gets the name of this KeystoneListPermissionsRequest.

        系统内部呈现的权限名称。如云目录服务CCS普通用户权限CCS User的name为ccs_user。 建议您传参display_name，不传name参数。

        :return: The name of this KeystoneListPermissionsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeystoneListPermissionsRequest.

        系统内部呈现的权限名称。如云目录服务CCS普通用户权限CCS User的name为ccs_user。 建议您传参display_name，不传name参数。

        :param name: The name of this KeystoneListPermissionsRequest.
        :type: str
        """
        self._name = name

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoneListPermissionsRequest.

        账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。 > - 如果填写此参数，则返回账号下所有自定义策略。 > - 如果不填写此参数，则返回所有系统权限（包含系统策略和系统角色）。

        :return: The domain_id of this KeystoneListPermissionsRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoneListPermissionsRequest.

        账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。 > - 如果填写此参数，则返回账号下所有自定义策略。 > - 如果不填写此参数，则返回所有系统权限（包含系统策略和系统角色）。

        :param domain_id: The domain_id of this KeystoneListPermissionsRequest.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def page(self):
        """Gets the page of this KeystoneListPermissionsRequest.

        分页查询时数据的页数，查询值最小为1。需要与per_page同时存在。传入domain_id参数查询自定义策略时，可配套使用。

        :return: The page of this KeystoneListPermissionsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this KeystoneListPermissionsRequest.

        分页查询时数据的页数，查询值最小为1。需要与per_page同时存在。传入domain_id参数查询自定义策略时，可配套使用。

        :param page: The page of this KeystoneListPermissionsRequest.
        :type: int
        """
        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this KeystoneListPermissionsRequest.

        分页查询时每页的数据个数，取值范围为[1,300]，默认值为300。需要与page同时存在。不传page和per_page参数时，每页最多返回300个权限。

        :return: The per_page of this KeystoneListPermissionsRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this KeystoneListPermissionsRequest.

        分页查询时每页的数据个数，取值范围为[1,300]，默认值为300。需要与page同时存在。不传page和per_page参数时，每页最多返回300个权限。

        :param per_page: The per_page of this KeystoneListPermissionsRequest.
        :type: int
        """
        self._per_page = per_page

    @property
    def permission_type(self):
        """Gets the permission_type of this KeystoneListPermissionsRequest.

        区分系统权限类型的参数。当domain_id参数为空时生效。 > - policy：返回系统策略。 > - role：返回系统角色。

        :return: The permission_type of this KeystoneListPermissionsRequest.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this KeystoneListPermissionsRequest.

        区分系统权限类型的参数。当domain_id参数为空时生效。 > - policy：返回系统策略。 > - role：返回系统角色。

        :param permission_type: The permission_type of this KeystoneListPermissionsRequest.
        :type: str
        """
        self._permission_type = permission_type

    @property
    def display_name(self):
        """Gets the display_name of this KeystoneListPermissionsRequest.

        过滤权限名称。如传参为Administrator，则返回满足条件的所有管理员权限。

        :return: The display_name of this KeystoneListPermissionsRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this KeystoneListPermissionsRequest.

        过滤权限名称。如传参为Administrator，则返回满足条件的所有管理员权限。

        :param display_name: The display_name of this KeystoneListPermissionsRequest.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """Gets the type of this KeystoneListPermissionsRequest.

        过滤权限的显示模式。取值范围：domain,project,all。type为domain时，返回type=AA或AX的权限；type为project时，返回type=AA或XA的权限；type为all时返回type为AA、AX、XA的权限。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - AA表示在domain和project层均显示。 > - XX表示在domain和project层均不显示。

        :return: The type of this KeystoneListPermissionsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this KeystoneListPermissionsRequest.

        过滤权限的显示模式。取值范围：domain,project,all。type为domain时，返回type=AA或AX的权限；type为project时，返回type=AA或XA的权限；type为all时返回type为AA、AX、XA的权限。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - AA表示在domain和project层均显示。 > - XX表示在domain和project层均不显示。

        :param type: The type of this KeystoneListPermissionsRequest.
        :type: str
        """
        self._type = type

    @property
    def catalog(self):
        """Gets the catalog of this KeystoneListPermissionsRequest.

        权限所在目录。catalog值精确匹配策略的catalog字段(可以过滤服务的策略、或者自定义策略)。

        :return: The catalog of this KeystoneListPermissionsRequest.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this KeystoneListPermissionsRequest.

        权限所在目录。catalog值精确匹配策略的catalog字段(可以过滤服务的策略、或者自定义策略)。

        :param catalog: The catalog of this KeystoneListPermissionsRequest.
        :type: str
        """
        self._catalog = catalog

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KeystoneListPermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
