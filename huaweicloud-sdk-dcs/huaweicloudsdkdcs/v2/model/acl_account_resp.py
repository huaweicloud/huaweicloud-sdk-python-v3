# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AclAccountResp:

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
        'account_type': 'str',
        'instance_id': 'str',
        'status': 'str',
        'account_role': 'str',
        'description': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_name': 'account_name',
        'account_type': 'account_type',
        'instance_id': 'instance_id',
        'status': 'status',
        'account_role': 'account_role',
        'description': 'description',
        'error_code': 'error_code'
    }

    def __init__(self, account_id=None, account_name=None, account_type=None, instance_id=None, status=None, account_role=None, description=None, error_code=None):
        r"""AclAccountResp

        The model defined in huaweicloud sdk

        :param account_id: 账号ID
        :type account_id: str
        :param account_name: 账号名
        :type account_name: str
        :param account_type: 账号类型
        :type account_type: str
        :param instance_id: 账号所属实例ID
        :type instance_id: str
        :param status: ACL账号状态 取值范围： - CREATING：账号创建中。 - AVAILABLE：账号可用。 - CREATEFAILED：账号创建失败。 - DELETED：账号已删除。 - DELETEFAILED：账号删除失败。 - DELETING：账号删除中。 - UPDATING：账号更新中。 - ERROR：账号异常。 
        :type status: str
        :param account_role: 账号权限
        :type account_role: str
        :param description: 账号描述
        :type description: str
        :param error_code: 错误码（暂未使用，赋值为null）
        :type error_code: str
        """
        
        

        self._account_id = None
        self._account_name = None
        self._account_type = None
        self._instance_id = None
        self._status = None
        self._account_role = None
        self._description = None
        self._error_code = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if account_type is not None:
            self.account_type = account_type
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if account_role is not None:
            self.account_role = account_role
        if description is not None:
            self.description = description
        if error_code is not None:
            self.error_code = error_code

    @property
    def account_id(self):
        r"""Gets the account_id of this AclAccountResp.

        账号ID

        :return: The account_id of this AclAccountResp.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this AclAccountResp.

        账号ID

        :param account_id: The account_id of this AclAccountResp.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        r"""Gets the account_name of this AclAccountResp.

        账号名

        :return: The account_name of this AclAccountResp.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this AclAccountResp.

        账号名

        :param account_name: The account_name of this AclAccountResp.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def account_type(self):
        r"""Gets the account_type of this AclAccountResp.

        账号类型

        :return: The account_type of this AclAccountResp.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        r"""Sets the account_type of this AclAccountResp.

        账号类型

        :param account_type: The account_type of this AclAccountResp.
        :type account_type: str
        """
        self._account_type = account_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AclAccountResp.

        账号所属实例ID

        :return: The instance_id of this AclAccountResp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AclAccountResp.

        账号所属实例ID

        :param instance_id: The instance_id of this AclAccountResp.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this AclAccountResp.

        ACL账号状态 取值范围： - CREATING：账号创建中。 - AVAILABLE：账号可用。 - CREATEFAILED：账号创建失败。 - DELETED：账号已删除。 - DELETEFAILED：账号删除失败。 - DELETING：账号删除中。 - UPDATING：账号更新中。 - ERROR：账号异常。 

        :return: The status of this AclAccountResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AclAccountResp.

        ACL账号状态 取值范围： - CREATING：账号创建中。 - AVAILABLE：账号可用。 - CREATEFAILED：账号创建失败。 - DELETED：账号已删除。 - DELETEFAILED：账号删除失败。 - DELETING：账号删除中。 - UPDATING：账号更新中。 - ERROR：账号异常。 

        :param status: The status of this AclAccountResp.
        :type status: str
        """
        self._status = status

    @property
    def account_role(self):
        r"""Gets the account_role of this AclAccountResp.

        账号权限

        :return: The account_role of this AclAccountResp.
        :rtype: str
        """
        return self._account_role

    @account_role.setter
    def account_role(self, account_role):
        r"""Sets the account_role of this AclAccountResp.

        账号权限

        :param account_role: The account_role of this AclAccountResp.
        :type account_role: str
        """
        self._account_role = account_role

    @property
    def description(self):
        r"""Gets the description of this AclAccountResp.

        账号描述

        :return: The description of this AclAccountResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AclAccountResp.

        账号描述

        :param description: The description of this AclAccountResp.
        :type description: str
        """
        self._description = description

    @property
    def error_code(self):
        r"""Gets the error_code of this AclAccountResp.

        错误码（暂未使用，赋值为null）

        :return: The error_code of this AclAccountResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this AclAccountResp.

        错误码（暂未使用，赋值为null）

        :param error_code: The error_code of this AclAccountResp.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, AclAccountResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
