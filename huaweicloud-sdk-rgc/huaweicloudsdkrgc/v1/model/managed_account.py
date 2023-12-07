# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManagedAccount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone': 'str',
        'manage_account_id': 'str',
        'account_id': 'str',
        'account_name': 'str',
        'account_email': 'str',
        'account_type': 'str',
        'owner': 'str',
        'state': 'str',
        'message': 'str',
        'parent_organization_unit_id': 'str',
        'parent_organization_unit_name': 'str',
        'identity_store_user_name': 'str',
        'identity_store_email_name': 'str',
        'blueprint_product_id': 'str',
        'blueprint_product_version': 'str',
        'blueprint_status': 'str',
        'regions': 'list[RegionManagedList]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'phone': 'phone',
        'manage_account_id': 'manage_account_id',
        'account_id': 'account_id',
        'account_name': 'account_name',
        'account_email': 'account_email',
        'account_type': 'account_type',
        'owner': 'owner',
        'state': 'state',
        'message': 'message',
        'parent_organization_unit_id': 'parent_organization_unit_id',
        'parent_organization_unit_name': 'parent_organization_unit_name',
        'identity_store_user_name': 'identity_store_user_name',
        'identity_store_email_name': 'identity_store_email_name',
        'blueprint_product_id': 'blueprint_product_id',
        'blueprint_product_version': 'blueprint_product_version',
        'blueprint_status': 'blueprint_status',
        'regions': 'regions',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, phone=None, manage_account_id=None, account_id=None, account_name=None, account_email=None, account_type=None, owner=None, state=None, message=None, parent_organization_unit_id=None, parent_organization_unit_name=None, identity_store_user_name=None, identity_store_email_name=None, blueprint_product_id=None, blueprint_product_version=None, blueprint_status=None, regions=None, created_at=None, updated_at=None):
        """ManagedAccount

        The model defined in huaweicloud sdk

        :param phone: 手机号码。
        :type phone: str
        :param manage_account_id: 管理账号ID。
        :type manage_account_id: str
        :param account_id: 账号ID。
        :type account_id: str
        :param account_name: 账号名称。
        :type account_name: str
        :param account_email: 账号email。
        :type account_email: str
        :param account_type: 账号类型。
        :type account_type: str
        :param owner: 账号的创建来源，包括CUSTOM和RGC。
        :type owner: str
        :param state: 账号状态。
        :type state: str
        :param message: 错误状态描述信息。
        :type message: str
        :param parent_organization_unit_id: 父OU ID。
        :type parent_organization_unit_id: str
        :param parent_organization_unit_name: 父OU名称。
        :type parent_organization_unit_name: str
        :param identity_store_user_name: Identity Center用户名。
        :type identity_store_user_name: str
        :param identity_store_email_name: Identity Center邮箱。
        :type identity_store_email_name: str
        :param blueprint_product_id: 蓝图ID。
        :type blueprint_product_id: str
        :param blueprint_product_version: 蓝图版本。
        :type blueprint_product_version: str
        :param blueprint_status: 蓝图部署状态，包括error, active, in_progress。
        :type blueprint_status: str
        :param regions: region信息。
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionManagedList`]
        :param created_at: 被创建的时间。
        :type created_at: datetime
        :param updated_at: 最后一次更新的时间。
        :type updated_at: datetime
        """
        
        

        self._phone = None
        self._manage_account_id = None
        self._account_id = None
        self._account_name = None
        self._account_email = None
        self._account_type = None
        self._owner = None
        self._state = None
        self._message = None
        self._parent_organization_unit_id = None
        self._parent_organization_unit_name = None
        self._identity_store_user_name = None
        self._identity_store_email_name = None
        self._blueprint_product_id = None
        self._blueprint_product_version = None
        self._blueprint_status = None
        self._regions = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if phone is not None:
            self.phone = phone
        if manage_account_id is not None:
            self.manage_account_id = manage_account_id
        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if account_email is not None:
            self.account_email = account_email
        if account_type is not None:
            self.account_type = account_type
        if owner is not None:
            self.owner = owner
        if state is not None:
            self.state = state
        if message is not None:
            self.message = message
        if parent_organization_unit_id is not None:
            self.parent_organization_unit_id = parent_organization_unit_id
        if parent_organization_unit_name is not None:
            self.parent_organization_unit_name = parent_organization_unit_name
        if identity_store_user_name is not None:
            self.identity_store_user_name = identity_store_user_name
        if identity_store_email_name is not None:
            self.identity_store_email_name = identity_store_email_name
        if blueprint_product_id is not None:
            self.blueprint_product_id = blueprint_product_id
        if blueprint_product_version is not None:
            self.blueprint_product_version = blueprint_product_version
        if blueprint_status is not None:
            self.blueprint_status = blueprint_status
        if regions is not None:
            self.regions = regions
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def phone(self):
        """Gets the phone of this ManagedAccount.

        手机号码。

        :return: The phone of this ManagedAccount.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ManagedAccount.

        手机号码。

        :param phone: The phone of this ManagedAccount.
        :type phone: str
        """
        self._phone = phone

    @property
    def manage_account_id(self):
        """Gets the manage_account_id of this ManagedAccount.

        管理账号ID。

        :return: The manage_account_id of this ManagedAccount.
        :rtype: str
        """
        return self._manage_account_id

    @manage_account_id.setter
    def manage_account_id(self, manage_account_id):
        """Sets the manage_account_id of this ManagedAccount.

        管理账号ID。

        :param manage_account_id: The manage_account_id of this ManagedAccount.
        :type manage_account_id: str
        """
        self._manage_account_id = manage_account_id

    @property
    def account_id(self):
        """Gets the account_id of this ManagedAccount.

        账号ID。

        :return: The account_id of this ManagedAccount.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ManagedAccount.

        账号ID。

        :param account_id: The account_id of this ManagedAccount.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        """Gets the account_name of this ManagedAccount.

        账号名称。

        :return: The account_name of this ManagedAccount.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this ManagedAccount.

        账号名称。

        :param account_name: The account_name of this ManagedAccount.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def account_email(self):
        """Gets the account_email of this ManagedAccount.

        账号email。

        :return: The account_email of this ManagedAccount.
        :rtype: str
        """
        return self._account_email

    @account_email.setter
    def account_email(self, account_email):
        """Sets the account_email of this ManagedAccount.

        账号email。

        :param account_email: The account_email of this ManagedAccount.
        :type account_email: str
        """
        self._account_email = account_email

    @property
    def account_type(self):
        """Gets the account_type of this ManagedAccount.

        账号类型。

        :return: The account_type of this ManagedAccount.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this ManagedAccount.

        账号类型。

        :param account_type: The account_type of this ManagedAccount.
        :type account_type: str
        """
        self._account_type = account_type

    @property
    def owner(self):
        """Gets the owner of this ManagedAccount.

        账号的创建来源，包括CUSTOM和RGC。

        :return: The owner of this ManagedAccount.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ManagedAccount.

        账号的创建来源，包括CUSTOM和RGC。

        :param owner: The owner of this ManagedAccount.
        :type owner: str
        """
        self._owner = owner

    @property
    def state(self):
        """Gets the state of this ManagedAccount.

        账号状态。

        :return: The state of this ManagedAccount.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ManagedAccount.

        账号状态。

        :param state: The state of this ManagedAccount.
        :type state: str
        """
        self._state = state

    @property
    def message(self):
        """Gets the message of this ManagedAccount.

        错误状态描述信息。

        :return: The message of this ManagedAccount.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ManagedAccount.

        错误状态描述信息。

        :param message: The message of this ManagedAccount.
        :type message: str
        """
        self._message = message

    @property
    def parent_organization_unit_id(self):
        """Gets the parent_organization_unit_id of this ManagedAccount.

        父OU ID。

        :return: The parent_organization_unit_id of this ManagedAccount.
        :rtype: str
        """
        return self._parent_organization_unit_id

    @parent_organization_unit_id.setter
    def parent_organization_unit_id(self, parent_organization_unit_id):
        """Sets the parent_organization_unit_id of this ManagedAccount.

        父OU ID。

        :param parent_organization_unit_id: The parent_organization_unit_id of this ManagedAccount.
        :type parent_organization_unit_id: str
        """
        self._parent_organization_unit_id = parent_organization_unit_id

    @property
    def parent_organization_unit_name(self):
        """Gets the parent_organization_unit_name of this ManagedAccount.

        父OU名称。

        :return: The parent_organization_unit_name of this ManagedAccount.
        :rtype: str
        """
        return self._parent_organization_unit_name

    @parent_organization_unit_name.setter
    def parent_organization_unit_name(self, parent_organization_unit_name):
        """Sets the parent_organization_unit_name of this ManagedAccount.

        父OU名称。

        :param parent_organization_unit_name: The parent_organization_unit_name of this ManagedAccount.
        :type parent_organization_unit_name: str
        """
        self._parent_organization_unit_name = parent_organization_unit_name

    @property
    def identity_store_user_name(self):
        """Gets the identity_store_user_name of this ManagedAccount.

        Identity Center用户名。

        :return: The identity_store_user_name of this ManagedAccount.
        :rtype: str
        """
        return self._identity_store_user_name

    @identity_store_user_name.setter
    def identity_store_user_name(self, identity_store_user_name):
        """Sets the identity_store_user_name of this ManagedAccount.

        Identity Center用户名。

        :param identity_store_user_name: The identity_store_user_name of this ManagedAccount.
        :type identity_store_user_name: str
        """
        self._identity_store_user_name = identity_store_user_name

    @property
    def identity_store_email_name(self):
        """Gets the identity_store_email_name of this ManagedAccount.

        Identity Center邮箱。

        :return: The identity_store_email_name of this ManagedAccount.
        :rtype: str
        """
        return self._identity_store_email_name

    @identity_store_email_name.setter
    def identity_store_email_name(self, identity_store_email_name):
        """Sets the identity_store_email_name of this ManagedAccount.

        Identity Center邮箱。

        :param identity_store_email_name: The identity_store_email_name of this ManagedAccount.
        :type identity_store_email_name: str
        """
        self._identity_store_email_name = identity_store_email_name

    @property
    def blueprint_product_id(self):
        """Gets the blueprint_product_id of this ManagedAccount.

        蓝图ID。

        :return: The blueprint_product_id of this ManagedAccount.
        :rtype: str
        """
        return self._blueprint_product_id

    @blueprint_product_id.setter
    def blueprint_product_id(self, blueprint_product_id):
        """Sets the blueprint_product_id of this ManagedAccount.

        蓝图ID。

        :param blueprint_product_id: The blueprint_product_id of this ManagedAccount.
        :type blueprint_product_id: str
        """
        self._blueprint_product_id = blueprint_product_id

    @property
    def blueprint_product_version(self):
        """Gets the blueprint_product_version of this ManagedAccount.

        蓝图版本。

        :return: The blueprint_product_version of this ManagedAccount.
        :rtype: str
        """
        return self._blueprint_product_version

    @blueprint_product_version.setter
    def blueprint_product_version(self, blueprint_product_version):
        """Sets the blueprint_product_version of this ManagedAccount.

        蓝图版本。

        :param blueprint_product_version: The blueprint_product_version of this ManagedAccount.
        :type blueprint_product_version: str
        """
        self._blueprint_product_version = blueprint_product_version

    @property
    def blueprint_status(self):
        """Gets the blueprint_status of this ManagedAccount.

        蓝图部署状态，包括error, active, in_progress。

        :return: The blueprint_status of this ManagedAccount.
        :rtype: str
        """
        return self._blueprint_status

    @blueprint_status.setter
    def blueprint_status(self, blueprint_status):
        """Sets the blueprint_status of this ManagedAccount.

        蓝图部署状态，包括error, active, in_progress。

        :param blueprint_status: The blueprint_status of this ManagedAccount.
        :type blueprint_status: str
        """
        self._blueprint_status = blueprint_status

    @property
    def regions(self):
        """Gets the regions of this ManagedAccount.

        region信息。

        :return: The regions of this ManagedAccount.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.RegionManagedList`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ManagedAccount.

        region信息。

        :param regions: The regions of this ManagedAccount.
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionManagedList`]
        """
        self._regions = regions

    @property
    def created_at(self):
        """Gets the created_at of this ManagedAccount.

        被创建的时间。

        :return: The created_at of this ManagedAccount.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ManagedAccount.

        被创建的时间。

        :param created_at: The created_at of this ManagedAccount.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ManagedAccount.

        最后一次更新的时间。

        :return: The updated_at of this ManagedAccount.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ManagedAccount.

        最后一次更新的时间。

        :param updated_at: The updated_at of this ManagedAccount.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ManagedAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
