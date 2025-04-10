# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cur_org_create_role': 'bool',
        'cur_org_open': 'bool',
        'has_free_trial': 'bool',
        'show_manage': 'bool'
    }

    attribute_map = {
        'cur_org_create_role': 'cur_org_create_role',
        'cur_org_open': 'cur_org_open',
        'has_free_trial': 'has_free_trial',
        'show_manage': 'show_manage'
    }

    def __init__(self, cur_org_create_role=None, cur_org_open=None, has_free_trial=None, show_manage=None):
        r"""AccountStatus

        The model defined in huaweicloud sdk

        :param cur_org_create_role: 是否有创建实例权限
        :type cur_org_create_role: bool
        :param cur_org_open: 帐号所属租户是否开通服务
        :type cur_org_open: bool
        :param has_free_trial: 免费试用
        :type has_free_trial: bool
        :param show_manage: 是否有管理入口的权限
        :type show_manage: bool
        """
        
        

        self._cur_org_create_role = None
        self._cur_org_open = None
        self._has_free_trial = None
        self._show_manage = None
        self.discriminator = None

        if cur_org_create_role is not None:
            self.cur_org_create_role = cur_org_create_role
        if cur_org_open is not None:
            self.cur_org_open = cur_org_open
        if has_free_trial is not None:
            self.has_free_trial = has_free_trial
        if show_manage is not None:
            self.show_manage = show_manage

    @property
    def cur_org_create_role(self):
        r"""Gets the cur_org_create_role of this AccountStatus.

        是否有创建实例权限

        :return: The cur_org_create_role of this AccountStatus.
        :rtype: bool
        """
        return self._cur_org_create_role

    @cur_org_create_role.setter
    def cur_org_create_role(self, cur_org_create_role):
        r"""Sets the cur_org_create_role of this AccountStatus.

        是否有创建实例权限

        :param cur_org_create_role: The cur_org_create_role of this AccountStatus.
        :type cur_org_create_role: bool
        """
        self._cur_org_create_role = cur_org_create_role

    @property
    def cur_org_open(self):
        r"""Gets the cur_org_open of this AccountStatus.

        帐号所属租户是否开通服务

        :return: The cur_org_open of this AccountStatus.
        :rtype: bool
        """
        return self._cur_org_open

    @cur_org_open.setter
    def cur_org_open(self, cur_org_open):
        r"""Sets the cur_org_open of this AccountStatus.

        帐号所属租户是否开通服务

        :param cur_org_open: The cur_org_open of this AccountStatus.
        :type cur_org_open: bool
        """
        self._cur_org_open = cur_org_open

    @property
    def has_free_trial(self):
        r"""Gets the has_free_trial of this AccountStatus.

        免费试用

        :return: The has_free_trial of this AccountStatus.
        :rtype: bool
        """
        return self._has_free_trial

    @has_free_trial.setter
    def has_free_trial(self, has_free_trial):
        r"""Sets the has_free_trial of this AccountStatus.

        免费试用

        :param has_free_trial: The has_free_trial of this AccountStatus.
        :type has_free_trial: bool
        """
        self._has_free_trial = has_free_trial

    @property
    def show_manage(self):
        r"""Gets the show_manage of this AccountStatus.

        是否有管理入口的权限

        :return: The show_manage of this AccountStatus.
        :rtype: bool
        """
        return self._show_manage

    @show_manage.setter
    def show_manage(self, show_manage):
        r"""Sets the show_manage of this AccountStatus.

        是否有管理入口的权限

        :param show_manage: The show_manage of this AccountStatus.
        :type show_manage: bool
        """
        self._show_manage = show_manage

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
        if not isinstance(other, AccountStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
