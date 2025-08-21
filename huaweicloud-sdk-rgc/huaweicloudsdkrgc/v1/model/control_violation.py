# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ControlViolation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'account_name': 'str',
        'display_name': 'str',
        'name': 'str',
        'control_id': 'str',
        'parent_organizational_unit_id': 'str',
        'parent_organizational_unit_name': 'str',
        'region': 'str',
        'resource': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'service': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_name': 'account_name',
        'display_name': 'display_name',
        'name': 'name',
        'control_id': 'control_id',
        'parent_organizational_unit_id': 'parent_organizational_unit_id',
        'parent_organizational_unit_name': 'parent_organizational_unit_name',
        'region': 'region',
        'resource': 'resource',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'service': 'service'
    }

    def __init__(self, account_id=None, account_name=None, display_name=None, name=None, control_id=None, parent_organizational_unit_id=None, parent_organizational_unit_name=None, region=None, resource=None, resource_name=None, resource_type=None, service=None):
        r"""ControlViolation

        The model defined in huaweicloud sdk

        :param account_id: 纳管账号ID。
        :type account_id: str
        :param account_name: 纳管账号名称。
        :type account_name: str
        :param display_name: 控制策略显示名称。
        :type display_name: str
        :param name: 控制策略名称。
        :type name: str
        :param control_id: 控制策略ID。
        :type control_id: str
        :param parent_organizational_unit_id: 父注册OU ID。
        :type parent_organizational_unit_id: str
        :param parent_organizational_unit_name: 父注册OU名称。
        :type parent_organizational_unit_name: str
        :param region: 区域名称。
        :type region: str
        :param resource: 控制策略不合规资源。
        :type resource: str
        :param resource_name: 控制策略不合规资源的名称。
        :type resource_name: str
        :param resource_type: 控制策略不合规资源类型。
        :type resource_type: str
        :param service: 云服务名称。
        :type service: str
        """
        
        

        self._account_id = None
        self._account_name = None
        self._display_name = None
        self._name = None
        self._control_id = None
        self._parent_organizational_unit_id = None
        self._parent_organizational_unit_name = None
        self._region = None
        self._resource = None
        self._resource_name = None
        self._resource_type = None
        self._service = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if display_name is not None:
            self.display_name = display_name
        if name is not None:
            self.name = name
        if control_id is not None:
            self.control_id = control_id
        if parent_organizational_unit_id is not None:
            self.parent_organizational_unit_id = parent_organizational_unit_id
        if parent_organizational_unit_name is not None:
            self.parent_organizational_unit_name = parent_organizational_unit_name
        if region is not None:
            self.region = region
        if resource is not None:
            self.resource = resource
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if service is not None:
            self.service = service

    @property
    def account_id(self):
        r"""Gets the account_id of this ControlViolation.

        纳管账号ID。

        :return: The account_id of this ControlViolation.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this ControlViolation.

        纳管账号ID。

        :param account_id: The account_id of this ControlViolation.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        r"""Gets the account_name of this ControlViolation.

        纳管账号名称。

        :return: The account_name of this ControlViolation.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this ControlViolation.

        纳管账号名称。

        :param account_name: The account_name of this ControlViolation.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def display_name(self):
        r"""Gets the display_name of this ControlViolation.

        控制策略显示名称。

        :return: The display_name of this ControlViolation.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ControlViolation.

        控制策略显示名称。

        :param display_name: The display_name of this ControlViolation.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def name(self):
        r"""Gets the name of this ControlViolation.

        控制策略名称。

        :return: The name of this ControlViolation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ControlViolation.

        控制策略名称。

        :param name: The name of this ControlViolation.
        :type name: str
        """
        self._name = name

    @property
    def control_id(self):
        r"""Gets the control_id of this ControlViolation.

        控制策略ID。

        :return: The control_id of this ControlViolation.
        :rtype: str
        """
        return self._control_id

    @control_id.setter
    def control_id(self, control_id):
        r"""Sets the control_id of this ControlViolation.

        控制策略ID。

        :param control_id: The control_id of this ControlViolation.
        :type control_id: str
        """
        self._control_id = control_id

    @property
    def parent_organizational_unit_id(self):
        r"""Gets the parent_organizational_unit_id of this ControlViolation.

        父注册OU ID。

        :return: The parent_organizational_unit_id of this ControlViolation.
        :rtype: str
        """
        return self._parent_organizational_unit_id

    @parent_organizational_unit_id.setter
    def parent_organizational_unit_id(self, parent_organizational_unit_id):
        r"""Sets the parent_organizational_unit_id of this ControlViolation.

        父注册OU ID。

        :param parent_organizational_unit_id: The parent_organizational_unit_id of this ControlViolation.
        :type parent_organizational_unit_id: str
        """
        self._parent_organizational_unit_id = parent_organizational_unit_id

    @property
    def parent_organizational_unit_name(self):
        r"""Gets the parent_organizational_unit_name of this ControlViolation.

        父注册OU名称。

        :return: The parent_organizational_unit_name of this ControlViolation.
        :rtype: str
        """
        return self._parent_organizational_unit_name

    @parent_organizational_unit_name.setter
    def parent_organizational_unit_name(self, parent_organizational_unit_name):
        r"""Sets the parent_organizational_unit_name of this ControlViolation.

        父注册OU名称。

        :param parent_organizational_unit_name: The parent_organizational_unit_name of this ControlViolation.
        :type parent_organizational_unit_name: str
        """
        self._parent_organizational_unit_name = parent_organizational_unit_name

    @property
    def region(self):
        r"""Gets the region of this ControlViolation.

        区域名称。

        :return: The region of this ControlViolation.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ControlViolation.

        区域名称。

        :param region: The region of this ControlViolation.
        :type region: str
        """
        self._region = region

    @property
    def resource(self):
        r"""Gets the resource of this ControlViolation.

        控制策略不合规资源。

        :return: The resource of this ControlViolation.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this ControlViolation.

        控制策略不合规资源。

        :param resource: The resource of this ControlViolation.
        :type resource: str
        """
        self._resource = resource

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ControlViolation.

        控制策略不合规资源的名称。

        :return: The resource_name of this ControlViolation.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ControlViolation.

        控制策略不合规资源的名称。

        :param resource_name: The resource_name of this ControlViolation.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ControlViolation.

        控制策略不合规资源类型。

        :return: The resource_type of this ControlViolation.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ControlViolation.

        控制策略不合规资源类型。

        :param resource_type: The resource_type of this ControlViolation.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def service(self):
        r"""Gets the service of this ControlViolation.

        云服务名称。

        :return: The service of this ControlViolation.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this ControlViolation.

        云服务名称。

        :param service: The service of this ControlViolation.
        :type service: str
        """
        self._service = service

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
        if not isinstance(other, ControlViolation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
