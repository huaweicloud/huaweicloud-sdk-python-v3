# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowManagedOrganizationalUnitResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manage_account_id': 'str',
        'organizational_unit_id': 'str',
        'organizational_unit_name': 'str',
        'organizational_unit_status': 'str',
        'organizational_unit_type': 'OrganizationalUnitType',
        'parent_organizational_unit_id': 'str',
        'parent_organizational_unit_name': 'str',
        'created_at': 'datetime',
        'landing_zone_version': 'str',
        'updated_at': 'datetime',
        'message': 'str'
    }

    attribute_map = {
        'manage_account_id': 'manage_account_id',
        'organizational_unit_id': 'organizational_unit_id',
        'organizational_unit_name': 'organizational_unit_name',
        'organizational_unit_status': 'organizational_unit_status',
        'organizational_unit_type': 'organizational_unit_type',
        'parent_organizational_unit_id': 'parent_organizational_unit_id',
        'parent_organizational_unit_name': 'parent_organizational_unit_name',
        'created_at': 'created_at',
        'landing_zone_version': 'landing_zone_version',
        'updated_at': 'updated_at',
        'message': 'message'
    }

    def __init__(self, manage_account_id=None, organizational_unit_id=None, organizational_unit_name=None, organizational_unit_status=None, organizational_unit_type=None, parent_organizational_unit_id=None, parent_organizational_unit_name=None, created_at=None, landing_zone_version=None, updated_at=None, message=None):
        r"""ShowManagedOrganizationalUnitResponse

        The model defined in huaweicloud sdk

        :param manage_account_id: 管理员账号ID。
        :type manage_account_id: str
        :param organizational_unit_id: 注册OU ID。
        :type organizational_unit_id: str
        :param organizational_unit_name: 注册OU名称。
        :type organizational_unit_name: str
        :param organizational_unit_status: 注册OU状态。
        :type organizational_unit_status: str
        :param organizational_unit_type: 
        :type organizational_unit_type: :class:`huaweicloudsdkrgc.v1.OrganizationalUnitType`
        :param parent_organizational_unit_id: 父注册OU ID。
        :type parent_organizational_unit_id: str
        :param parent_organizational_unit_name: 父注册OU名称。
        :type parent_organizational_unit_name: str
        :param created_at: 注册OU的创建时间。
        :type created_at: datetime
        :param landing_zone_version: 注册OU的Landing Zone版本。
        :type landing_zone_version: str
        :param updated_at: 注册OU的更新时间。
        :type updated_at: datetime
        :param message: 错误信息描述。
        :type message: str
        """
        
        super(ShowManagedOrganizationalUnitResponse, self).__init__()

        self._manage_account_id = None
        self._organizational_unit_id = None
        self._organizational_unit_name = None
        self._organizational_unit_status = None
        self._organizational_unit_type = None
        self._parent_organizational_unit_id = None
        self._parent_organizational_unit_name = None
        self._created_at = None
        self._landing_zone_version = None
        self._updated_at = None
        self._message = None
        self.discriminator = None

        if manage_account_id is not None:
            self.manage_account_id = manage_account_id
        if organizational_unit_id is not None:
            self.organizational_unit_id = organizational_unit_id
        if organizational_unit_name is not None:
            self.organizational_unit_name = organizational_unit_name
        if organizational_unit_status is not None:
            self.organizational_unit_status = organizational_unit_status
        if organizational_unit_type is not None:
            self.organizational_unit_type = organizational_unit_type
        if parent_organizational_unit_id is not None:
            self.parent_organizational_unit_id = parent_organizational_unit_id
        if parent_organizational_unit_name is not None:
            self.parent_organizational_unit_name = parent_organizational_unit_name
        if created_at is not None:
            self.created_at = created_at
        if landing_zone_version is not None:
            self.landing_zone_version = landing_zone_version
        if updated_at is not None:
            self.updated_at = updated_at
        if message is not None:
            self.message = message

    @property
    def manage_account_id(self):
        r"""Gets the manage_account_id of this ShowManagedOrganizationalUnitResponse.

        管理员账号ID。

        :return: The manage_account_id of this ShowManagedOrganizationalUnitResponse.
        :rtype: str
        """
        return self._manage_account_id

    @manage_account_id.setter
    def manage_account_id(self, manage_account_id):
        r"""Sets the manage_account_id of this ShowManagedOrganizationalUnitResponse.

        管理员账号ID。

        :param manage_account_id: The manage_account_id of this ShowManagedOrganizationalUnitResponse.
        :type manage_account_id: str
        """
        self._manage_account_id = manage_account_id

    @property
    def organizational_unit_id(self):
        r"""Gets the organizational_unit_id of this ShowManagedOrganizationalUnitResponse.

        注册OU ID。

        :return: The organizational_unit_id of this ShowManagedOrganizationalUnitResponse.
        :rtype: str
        """
        return self._organizational_unit_id

    @organizational_unit_id.setter
    def organizational_unit_id(self, organizational_unit_id):
        r"""Sets the organizational_unit_id of this ShowManagedOrganizationalUnitResponse.

        注册OU ID。

        :param organizational_unit_id: The organizational_unit_id of this ShowManagedOrganizationalUnitResponse.
        :type organizational_unit_id: str
        """
        self._organizational_unit_id = organizational_unit_id

    @property
    def organizational_unit_name(self):
        r"""Gets the organizational_unit_name of this ShowManagedOrganizationalUnitResponse.

        注册OU名称。

        :return: The organizational_unit_name of this ShowManagedOrganizationalUnitResponse.
        :rtype: str
        """
        return self._organizational_unit_name

    @organizational_unit_name.setter
    def organizational_unit_name(self, organizational_unit_name):
        r"""Sets the organizational_unit_name of this ShowManagedOrganizationalUnitResponse.

        注册OU名称。

        :param organizational_unit_name: The organizational_unit_name of this ShowManagedOrganizationalUnitResponse.
        :type organizational_unit_name: str
        """
        self._organizational_unit_name = organizational_unit_name

    @property
    def organizational_unit_status(self):
        r"""Gets the organizational_unit_status of this ShowManagedOrganizationalUnitResponse.

        注册OU状态。

        :return: The organizational_unit_status of this ShowManagedOrganizationalUnitResponse.
        :rtype: str
        """
        return self._organizational_unit_status

    @organizational_unit_status.setter
    def organizational_unit_status(self, organizational_unit_status):
        r"""Sets the organizational_unit_status of this ShowManagedOrganizationalUnitResponse.

        注册OU状态。

        :param organizational_unit_status: The organizational_unit_status of this ShowManagedOrganizationalUnitResponse.
        :type organizational_unit_status: str
        """
        self._organizational_unit_status = organizational_unit_status

    @property
    def organizational_unit_type(self):
        r"""Gets the organizational_unit_type of this ShowManagedOrganizationalUnitResponse.

        :return: The organizational_unit_type of this ShowManagedOrganizationalUnitResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.OrganizationalUnitType`
        """
        return self._organizational_unit_type

    @organizational_unit_type.setter
    def organizational_unit_type(self, organizational_unit_type):
        r"""Sets the organizational_unit_type of this ShowManagedOrganizationalUnitResponse.

        :param organizational_unit_type: The organizational_unit_type of this ShowManagedOrganizationalUnitResponse.
        :type organizational_unit_type: :class:`huaweicloudsdkrgc.v1.OrganizationalUnitType`
        """
        self._organizational_unit_type = organizational_unit_type

    @property
    def parent_organizational_unit_id(self):
        r"""Gets the parent_organizational_unit_id of this ShowManagedOrganizationalUnitResponse.

        父注册OU ID。

        :return: The parent_organizational_unit_id of this ShowManagedOrganizationalUnitResponse.
        :rtype: str
        """
        return self._parent_organizational_unit_id

    @parent_organizational_unit_id.setter
    def parent_organizational_unit_id(self, parent_organizational_unit_id):
        r"""Sets the parent_organizational_unit_id of this ShowManagedOrganizationalUnitResponse.

        父注册OU ID。

        :param parent_organizational_unit_id: The parent_organizational_unit_id of this ShowManagedOrganizationalUnitResponse.
        :type parent_organizational_unit_id: str
        """
        self._parent_organizational_unit_id = parent_organizational_unit_id

    @property
    def parent_organizational_unit_name(self):
        r"""Gets the parent_organizational_unit_name of this ShowManagedOrganizationalUnitResponse.

        父注册OU名称。

        :return: The parent_organizational_unit_name of this ShowManagedOrganizationalUnitResponse.
        :rtype: str
        """
        return self._parent_organizational_unit_name

    @parent_organizational_unit_name.setter
    def parent_organizational_unit_name(self, parent_organizational_unit_name):
        r"""Sets the parent_organizational_unit_name of this ShowManagedOrganizationalUnitResponse.

        父注册OU名称。

        :param parent_organizational_unit_name: The parent_organizational_unit_name of this ShowManagedOrganizationalUnitResponse.
        :type parent_organizational_unit_name: str
        """
        self._parent_organizational_unit_name = parent_organizational_unit_name

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowManagedOrganizationalUnitResponse.

        注册OU的创建时间。

        :return: The created_at of this ShowManagedOrganizationalUnitResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowManagedOrganizationalUnitResponse.

        注册OU的创建时间。

        :param created_at: The created_at of this ShowManagedOrganizationalUnitResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def landing_zone_version(self):
        r"""Gets the landing_zone_version of this ShowManagedOrganizationalUnitResponse.

        注册OU的Landing Zone版本。

        :return: The landing_zone_version of this ShowManagedOrganizationalUnitResponse.
        :rtype: str
        """
        return self._landing_zone_version

    @landing_zone_version.setter
    def landing_zone_version(self, landing_zone_version):
        r"""Sets the landing_zone_version of this ShowManagedOrganizationalUnitResponse.

        注册OU的Landing Zone版本。

        :param landing_zone_version: The landing_zone_version of this ShowManagedOrganizationalUnitResponse.
        :type landing_zone_version: str
        """
        self._landing_zone_version = landing_zone_version

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowManagedOrganizationalUnitResponse.

        注册OU的更新时间。

        :return: The updated_at of this ShowManagedOrganizationalUnitResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowManagedOrganizationalUnitResponse.

        注册OU的更新时间。

        :param updated_at: The updated_at of this ShowManagedOrganizationalUnitResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def message(self):
        r"""Gets the message of this ShowManagedOrganizationalUnitResponse.

        错误信息描述。

        :return: The message of this ShowManagedOrganizationalUnitResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowManagedOrganizationalUnitResponse.

        错误信息描述。

        :param message: The message of this ShowManagedOrganizationalUnitResponse.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, ShowManagedOrganizationalUnitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
