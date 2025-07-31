# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePasswordChangePlanRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor': 'str',
        'resource_provider': 'str',
        'resource_type': 'str',
        'instance_type': 'str',
        'accounts_to_be_changed': 'list[str]',
        'accounts_not_to_be_changed': 'list[str]',
        'accounts_password_change_status': 'list[str]',
        'resources_id': 'list[str]'
    }

    attribute_map = {
        'vendor': 'vendor',
        'resource_provider': 'resource_provider',
        'resource_type': 'resource_type',
        'instance_type': 'instance_type',
        'accounts_to_be_changed': 'accounts_to_be_changed',
        'accounts_not_to_be_changed': 'accounts_not_to_be_changed',
        'accounts_password_change_status': 'accounts_password_change_status',
        'resources_id': 'resources_id'
    }

    def __init__(self, vendor=None, resource_provider=None, resource_type=None, instance_type=None, accounts_to_be_changed=None, accounts_not_to_be_changed=None, accounts_password_change_status=None, resources_id=None):
        r"""CreatePasswordChangePlanRequestBody

        The model defined in huaweicloud sdk

        :param vendor: 云服务厂商
        :type vendor: str
        :param resource_provider: 云服务
        :type resource_provider: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param instance_type: 实例类型
        :type instance_type: str
        :param accounts_to_be_changed: 需要改密的账号
        :type accounts_to_be_changed: list[str]
        :param accounts_not_to_be_changed: 不需要改密的账号，注意：account_to_be_changed不为空时，此字段不生效！！！两者都为空时默认修改所有账号
        :type accounts_not_to_be_changed: list[str]
        :param accounts_password_change_status: 需要改密的账号的状态，枚举值  TO_BE_CHANGED：待改密 FAILED：改密失败 SUCCESSFUL：改密成功 PROCESSING：改密中  不传默认修改所有状态的账号
        :type accounts_password_change_status: list[str]
        :param resources_id: 实例id列表
        :type resources_id: list[str]
        """
        
        

        self._vendor = None
        self._resource_provider = None
        self._resource_type = None
        self._instance_type = None
        self._accounts_to_be_changed = None
        self._accounts_not_to_be_changed = None
        self._accounts_password_change_status = None
        self._resources_id = None
        self.discriminator = None

        self.vendor = vendor
        self.resource_provider = resource_provider
        self.resource_type = resource_type
        self.instance_type = instance_type
        if accounts_to_be_changed is not None:
            self.accounts_to_be_changed = accounts_to_be_changed
        if accounts_not_to_be_changed is not None:
            self.accounts_not_to_be_changed = accounts_not_to_be_changed
        if accounts_password_change_status is not None:
            self.accounts_password_change_status = accounts_password_change_status
        self.resources_id = resources_id

    @property
    def vendor(self):
        r"""Gets the vendor of this CreatePasswordChangePlanRequestBody.

        云服务厂商

        :return: The vendor of this CreatePasswordChangePlanRequestBody.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this CreatePasswordChangePlanRequestBody.

        云服务厂商

        :param vendor: The vendor of this CreatePasswordChangePlanRequestBody.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def resource_provider(self):
        r"""Gets the resource_provider of this CreatePasswordChangePlanRequestBody.

        云服务

        :return: The resource_provider of this CreatePasswordChangePlanRequestBody.
        :rtype: str
        """
        return self._resource_provider

    @resource_provider.setter
    def resource_provider(self, resource_provider):
        r"""Sets the resource_provider of this CreatePasswordChangePlanRequestBody.

        云服务

        :param resource_provider: The resource_provider of this CreatePasswordChangePlanRequestBody.
        :type resource_provider: str
        """
        self._resource_provider = resource_provider

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CreatePasswordChangePlanRequestBody.

        资源类型

        :return: The resource_type of this CreatePasswordChangePlanRequestBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CreatePasswordChangePlanRequestBody.

        资源类型

        :param resource_type: The resource_type of this CreatePasswordChangePlanRequestBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def instance_type(self):
        r"""Gets the instance_type of this CreatePasswordChangePlanRequestBody.

        实例类型

        :return: The instance_type of this CreatePasswordChangePlanRequestBody.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this CreatePasswordChangePlanRequestBody.

        实例类型

        :param instance_type: The instance_type of this CreatePasswordChangePlanRequestBody.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def accounts_to_be_changed(self):
        r"""Gets the accounts_to_be_changed of this CreatePasswordChangePlanRequestBody.

        需要改密的账号

        :return: The accounts_to_be_changed of this CreatePasswordChangePlanRequestBody.
        :rtype: list[str]
        """
        return self._accounts_to_be_changed

    @accounts_to_be_changed.setter
    def accounts_to_be_changed(self, accounts_to_be_changed):
        r"""Sets the accounts_to_be_changed of this CreatePasswordChangePlanRequestBody.

        需要改密的账号

        :param accounts_to_be_changed: The accounts_to_be_changed of this CreatePasswordChangePlanRequestBody.
        :type accounts_to_be_changed: list[str]
        """
        self._accounts_to_be_changed = accounts_to_be_changed

    @property
    def accounts_not_to_be_changed(self):
        r"""Gets the accounts_not_to_be_changed of this CreatePasswordChangePlanRequestBody.

        不需要改密的账号，注意：account_to_be_changed不为空时，此字段不生效！！！两者都为空时默认修改所有账号

        :return: The accounts_not_to_be_changed of this CreatePasswordChangePlanRequestBody.
        :rtype: list[str]
        """
        return self._accounts_not_to_be_changed

    @accounts_not_to_be_changed.setter
    def accounts_not_to_be_changed(self, accounts_not_to_be_changed):
        r"""Sets the accounts_not_to_be_changed of this CreatePasswordChangePlanRequestBody.

        不需要改密的账号，注意：account_to_be_changed不为空时，此字段不生效！！！两者都为空时默认修改所有账号

        :param accounts_not_to_be_changed: The accounts_not_to_be_changed of this CreatePasswordChangePlanRequestBody.
        :type accounts_not_to_be_changed: list[str]
        """
        self._accounts_not_to_be_changed = accounts_not_to_be_changed

    @property
    def accounts_password_change_status(self):
        r"""Gets the accounts_password_change_status of this CreatePasswordChangePlanRequestBody.

        需要改密的账号的状态，枚举值  TO_BE_CHANGED：待改密 FAILED：改密失败 SUCCESSFUL：改密成功 PROCESSING：改密中  不传默认修改所有状态的账号

        :return: The accounts_password_change_status of this CreatePasswordChangePlanRequestBody.
        :rtype: list[str]
        """
        return self._accounts_password_change_status

    @accounts_password_change_status.setter
    def accounts_password_change_status(self, accounts_password_change_status):
        r"""Sets the accounts_password_change_status of this CreatePasswordChangePlanRequestBody.

        需要改密的账号的状态，枚举值  TO_BE_CHANGED：待改密 FAILED：改密失败 SUCCESSFUL：改密成功 PROCESSING：改密中  不传默认修改所有状态的账号

        :param accounts_password_change_status: The accounts_password_change_status of this CreatePasswordChangePlanRequestBody.
        :type accounts_password_change_status: list[str]
        """
        self._accounts_password_change_status = accounts_password_change_status

    @property
    def resources_id(self):
        r"""Gets the resources_id of this CreatePasswordChangePlanRequestBody.

        实例id列表

        :return: The resources_id of this CreatePasswordChangePlanRequestBody.
        :rtype: list[str]
        """
        return self._resources_id

    @resources_id.setter
    def resources_id(self, resources_id):
        r"""Sets the resources_id of this CreatePasswordChangePlanRequestBody.

        实例id列表

        :param resources_id: The resources_id of this CreatePasswordChangePlanRequestBody.
        :type resources_id: list[str]
        """
        self._resources_id = resources_id

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
        if not isinstance(other, CreatePasswordChangePlanRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
