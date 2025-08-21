# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowManagedAccountResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'landing_zone_version': 'str',
        'manage_account_id': 'str',
        'account_id': 'str',
        'account_name': 'str',
        'account_type': 'str',
        'owner': 'str',
        'state': 'str',
        'message': 'str',
        'parent_organizational_unit_id': 'str',
        'parent_organizational_unit_name': 'str',
        'identity_store_user_name': 'str',
        'blueprint_product_id': 'str',
        'blueprint_product_version': 'str',
        'blueprint_status': 'str',
        'is_blueprint_has_multi_account_resource': 'bool',
        'regions': 'list[RegionManagedList]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'landing_zone_version': 'landing_zone_version',
        'manage_account_id': 'manage_account_id',
        'account_id': 'account_id',
        'account_name': 'account_name',
        'account_type': 'account_type',
        'owner': 'owner',
        'state': 'state',
        'message': 'message',
        'parent_organizational_unit_id': 'parent_organizational_unit_id',
        'parent_organizational_unit_name': 'parent_organizational_unit_name',
        'identity_store_user_name': 'identity_store_user_name',
        'blueprint_product_id': 'blueprint_product_id',
        'blueprint_product_version': 'blueprint_product_version',
        'blueprint_status': 'blueprint_status',
        'is_blueprint_has_multi_account_resource': 'is_blueprint_has_multi_account_resource',
        'regions': 'regions',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, landing_zone_version=None, manage_account_id=None, account_id=None, account_name=None, account_type=None, owner=None, state=None, message=None, parent_organizational_unit_id=None, parent_organizational_unit_name=None, identity_store_user_name=None, blueprint_product_id=None, blueprint_product_version=None, blueprint_status=None, is_blueprint_has_multi_account_resource=None, regions=None, created_at=None, updated_at=None):
        r"""ShowManagedAccountResponse

        The model defined in huaweicloud sdk

        :param landing_zone_version: 纳管账号的Landing Zone版本。
        :type landing_zone_version: str
        :param manage_account_id: 管理员账号ID。
        :type manage_account_id: str
        :param account_id: 纳管账号ID。
        :type account_id: str
        :param account_name: 纳管账号名称。
        :type account_name: str
        :param account_type: 纳管账号类型。
        :type account_type: str
        :param owner: 纳管账号的创建来源，包括CUSTOM和RGC。
        :type owner: str
        :param state: 纳管账号状态。
        :type state: str
        :param message: 错误状态描述信息。
        :type message: str
        :param parent_organizational_unit_id: 父注册OU ID。
        :type parent_organizational_unit_id: str
        :param parent_organizational_unit_name: 父注册OU名称。
        :type parent_organizational_unit_name: str
        :param identity_store_user_name: Identity Center用户名。
        :type identity_store_user_name: str
        :param blueprint_product_id: 模板ID。
        :type blueprint_product_id: str
        :param blueprint_product_version: 模板版本。
        :type blueprint_product_version: str
        :param blueprint_status: 模板部署状态，包括失败, 完成, 进行中。
        :type blueprint_status: str
        :param is_blueprint_has_multi_account_resource: 模板是否包含多账号资源。
        :type is_blueprint_has_multi_account_resource: bool
        :param regions: 区域信息。
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionManagedList`]
        :param created_at: 纳管账号的创建时间。
        :type created_at: datetime
        :param updated_at: 纳管账号的更新时间。
        :type updated_at: datetime
        """
        
        super(ShowManagedAccountResponse, self).__init__()

        self._landing_zone_version = None
        self._manage_account_id = None
        self._account_id = None
        self._account_name = None
        self._account_type = None
        self._owner = None
        self._state = None
        self._message = None
        self._parent_organizational_unit_id = None
        self._parent_organizational_unit_name = None
        self._identity_store_user_name = None
        self._blueprint_product_id = None
        self._blueprint_product_version = None
        self._blueprint_status = None
        self._is_blueprint_has_multi_account_resource = None
        self._regions = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if landing_zone_version is not None:
            self.landing_zone_version = landing_zone_version
        if manage_account_id is not None:
            self.manage_account_id = manage_account_id
        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if account_type is not None:
            self.account_type = account_type
        if owner is not None:
            self.owner = owner
        if state is not None:
            self.state = state
        if message is not None:
            self.message = message
        if parent_organizational_unit_id is not None:
            self.parent_organizational_unit_id = parent_organizational_unit_id
        if parent_organizational_unit_name is not None:
            self.parent_organizational_unit_name = parent_organizational_unit_name
        if identity_store_user_name is not None:
            self.identity_store_user_name = identity_store_user_name
        if blueprint_product_id is not None:
            self.blueprint_product_id = blueprint_product_id
        if blueprint_product_version is not None:
            self.blueprint_product_version = blueprint_product_version
        if blueprint_status is not None:
            self.blueprint_status = blueprint_status
        if is_blueprint_has_multi_account_resource is not None:
            self.is_blueprint_has_multi_account_resource = is_blueprint_has_multi_account_resource
        if regions is not None:
            self.regions = regions
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def landing_zone_version(self):
        r"""Gets the landing_zone_version of this ShowManagedAccountResponse.

        纳管账号的Landing Zone版本。

        :return: The landing_zone_version of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._landing_zone_version

    @landing_zone_version.setter
    def landing_zone_version(self, landing_zone_version):
        r"""Sets the landing_zone_version of this ShowManagedAccountResponse.

        纳管账号的Landing Zone版本。

        :param landing_zone_version: The landing_zone_version of this ShowManagedAccountResponse.
        :type landing_zone_version: str
        """
        self._landing_zone_version = landing_zone_version

    @property
    def manage_account_id(self):
        r"""Gets the manage_account_id of this ShowManagedAccountResponse.

        管理员账号ID。

        :return: The manage_account_id of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._manage_account_id

    @manage_account_id.setter
    def manage_account_id(self, manage_account_id):
        r"""Sets the manage_account_id of this ShowManagedAccountResponse.

        管理员账号ID。

        :param manage_account_id: The manage_account_id of this ShowManagedAccountResponse.
        :type manage_account_id: str
        """
        self._manage_account_id = manage_account_id

    @property
    def account_id(self):
        r"""Gets the account_id of this ShowManagedAccountResponse.

        纳管账号ID。

        :return: The account_id of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this ShowManagedAccountResponse.

        纳管账号ID。

        :param account_id: The account_id of this ShowManagedAccountResponse.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        r"""Gets the account_name of this ShowManagedAccountResponse.

        纳管账号名称。

        :return: The account_name of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this ShowManagedAccountResponse.

        纳管账号名称。

        :param account_name: The account_name of this ShowManagedAccountResponse.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def account_type(self):
        r"""Gets the account_type of this ShowManagedAccountResponse.

        纳管账号类型。

        :return: The account_type of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        r"""Sets the account_type of this ShowManagedAccountResponse.

        纳管账号类型。

        :param account_type: The account_type of this ShowManagedAccountResponse.
        :type account_type: str
        """
        self._account_type = account_type

    @property
    def owner(self):
        r"""Gets the owner of this ShowManagedAccountResponse.

        纳管账号的创建来源，包括CUSTOM和RGC。

        :return: The owner of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ShowManagedAccountResponse.

        纳管账号的创建来源，包括CUSTOM和RGC。

        :param owner: The owner of this ShowManagedAccountResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def state(self):
        r"""Gets the state of this ShowManagedAccountResponse.

        纳管账号状态。

        :return: The state of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowManagedAccountResponse.

        纳管账号状态。

        :param state: The state of this ShowManagedAccountResponse.
        :type state: str
        """
        self._state = state

    @property
    def message(self):
        r"""Gets the message of this ShowManagedAccountResponse.

        错误状态描述信息。

        :return: The message of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowManagedAccountResponse.

        错误状态描述信息。

        :param message: The message of this ShowManagedAccountResponse.
        :type message: str
        """
        self._message = message

    @property
    def parent_organizational_unit_id(self):
        r"""Gets the parent_organizational_unit_id of this ShowManagedAccountResponse.

        父注册OU ID。

        :return: The parent_organizational_unit_id of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._parent_organizational_unit_id

    @parent_organizational_unit_id.setter
    def parent_organizational_unit_id(self, parent_organizational_unit_id):
        r"""Sets the parent_organizational_unit_id of this ShowManagedAccountResponse.

        父注册OU ID。

        :param parent_organizational_unit_id: The parent_organizational_unit_id of this ShowManagedAccountResponse.
        :type parent_organizational_unit_id: str
        """
        self._parent_organizational_unit_id = parent_organizational_unit_id

    @property
    def parent_organizational_unit_name(self):
        r"""Gets the parent_organizational_unit_name of this ShowManagedAccountResponse.

        父注册OU名称。

        :return: The parent_organizational_unit_name of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._parent_organizational_unit_name

    @parent_organizational_unit_name.setter
    def parent_organizational_unit_name(self, parent_organizational_unit_name):
        r"""Sets the parent_organizational_unit_name of this ShowManagedAccountResponse.

        父注册OU名称。

        :param parent_organizational_unit_name: The parent_organizational_unit_name of this ShowManagedAccountResponse.
        :type parent_organizational_unit_name: str
        """
        self._parent_organizational_unit_name = parent_organizational_unit_name

    @property
    def identity_store_user_name(self):
        r"""Gets the identity_store_user_name of this ShowManagedAccountResponse.

        Identity Center用户名。

        :return: The identity_store_user_name of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._identity_store_user_name

    @identity_store_user_name.setter
    def identity_store_user_name(self, identity_store_user_name):
        r"""Sets the identity_store_user_name of this ShowManagedAccountResponse.

        Identity Center用户名。

        :param identity_store_user_name: The identity_store_user_name of this ShowManagedAccountResponse.
        :type identity_store_user_name: str
        """
        self._identity_store_user_name = identity_store_user_name

    @property
    def blueprint_product_id(self):
        r"""Gets the blueprint_product_id of this ShowManagedAccountResponse.

        模板ID。

        :return: The blueprint_product_id of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._blueprint_product_id

    @blueprint_product_id.setter
    def blueprint_product_id(self, blueprint_product_id):
        r"""Sets the blueprint_product_id of this ShowManagedAccountResponse.

        模板ID。

        :param blueprint_product_id: The blueprint_product_id of this ShowManagedAccountResponse.
        :type blueprint_product_id: str
        """
        self._blueprint_product_id = blueprint_product_id

    @property
    def blueprint_product_version(self):
        r"""Gets the blueprint_product_version of this ShowManagedAccountResponse.

        模板版本。

        :return: The blueprint_product_version of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._blueprint_product_version

    @blueprint_product_version.setter
    def blueprint_product_version(self, blueprint_product_version):
        r"""Sets the blueprint_product_version of this ShowManagedAccountResponse.

        模板版本。

        :param blueprint_product_version: The blueprint_product_version of this ShowManagedAccountResponse.
        :type blueprint_product_version: str
        """
        self._blueprint_product_version = blueprint_product_version

    @property
    def blueprint_status(self):
        r"""Gets the blueprint_status of this ShowManagedAccountResponse.

        模板部署状态，包括失败, 完成, 进行中。

        :return: The blueprint_status of this ShowManagedAccountResponse.
        :rtype: str
        """
        return self._blueprint_status

    @blueprint_status.setter
    def blueprint_status(self, blueprint_status):
        r"""Sets the blueprint_status of this ShowManagedAccountResponse.

        模板部署状态，包括失败, 完成, 进行中。

        :param blueprint_status: The blueprint_status of this ShowManagedAccountResponse.
        :type blueprint_status: str
        """
        self._blueprint_status = blueprint_status

    @property
    def is_blueprint_has_multi_account_resource(self):
        r"""Gets the is_blueprint_has_multi_account_resource of this ShowManagedAccountResponse.

        模板是否包含多账号资源。

        :return: The is_blueprint_has_multi_account_resource of this ShowManagedAccountResponse.
        :rtype: bool
        """
        return self._is_blueprint_has_multi_account_resource

    @is_blueprint_has_multi_account_resource.setter
    def is_blueprint_has_multi_account_resource(self, is_blueprint_has_multi_account_resource):
        r"""Sets the is_blueprint_has_multi_account_resource of this ShowManagedAccountResponse.

        模板是否包含多账号资源。

        :param is_blueprint_has_multi_account_resource: The is_blueprint_has_multi_account_resource of this ShowManagedAccountResponse.
        :type is_blueprint_has_multi_account_resource: bool
        """
        self._is_blueprint_has_multi_account_resource = is_blueprint_has_multi_account_resource

    @property
    def regions(self):
        r"""Gets the regions of this ShowManagedAccountResponse.

        区域信息。

        :return: The regions of this ShowManagedAccountResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.RegionManagedList`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this ShowManagedAccountResponse.

        区域信息。

        :param regions: The regions of this ShowManagedAccountResponse.
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionManagedList`]
        """
        self._regions = regions

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowManagedAccountResponse.

        纳管账号的创建时间。

        :return: The created_at of this ShowManagedAccountResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowManagedAccountResponse.

        纳管账号的创建时间。

        :param created_at: The created_at of this ShowManagedAccountResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowManagedAccountResponse.

        纳管账号的更新时间。

        :return: The updated_at of this ShowManagedAccountResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowManagedAccountResponse.

        纳管账号的更新时间。

        :param updated_at: The updated_at of this ShowManagedAccountResponse.
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
        if not isinstance(other, ShowManagedAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
