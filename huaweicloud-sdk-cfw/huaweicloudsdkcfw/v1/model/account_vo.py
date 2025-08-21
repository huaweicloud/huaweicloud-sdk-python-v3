# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountVO:

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
        'eip_count_protected': 'int',
        'eip_count_total': 'int',
        'eip_count_unprotected': 'int',
        'organization_id': 'str',
        'project_id': 'str',
        'project_name': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_name': 'account_name',
        'eip_count_protected': 'eip_count_protected',
        'eip_count_total': 'eip_count_total',
        'eip_count_unprotected': 'eip_count_unprotected',
        'organization_id': 'organization_id',
        'project_id': 'project_id',
        'project_name': 'project_name'
    }

    def __init__(self, account_id=None, account_name=None, eip_count_protected=None, eip_count_total=None, eip_count_unprotected=None, organization_id=None, project_id=None, project_name=None):
        r"""AccountVO

        The model defined in huaweicloud sdk

        :param account_id: **参数解释**： 账号ID **取值范围**： 不涉及
        :type account_id: str
        :param account_name: **参数解释**： 账号名称 **取值范围**： 不涉及
        :type account_name: str
        :param eip_count_protected: **参数解释**： 防护的EIP数量 **取值范围**： 不涉及
        :type eip_count_protected: int
        :param eip_count_total: **参数解释**： EIP总数 **取值范围**： 不涉及
        :type eip_count_total: int
        :param eip_count_unprotected: **参数解释**： 未开启防护的EIP数量 **取值范围**： 不涉及
        :type eip_count_unprotected: int
        :param organization_id: **参数解释**： 组织ID **取值范围**： 不涉及
        :type organization_id: str
        :param project_id: **参数解释**： 项目ID **取值范围**： 不涉及
        :type project_id: str
        :param project_name: **参数解释**： 项目名称 **取值范围**： 不涉及
        :type project_name: str
        """
        
        

        self._account_id = None
        self._account_name = None
        self._eip_count_protected = None
        self._eip_count_total = None
        self._eip_count_unprotected = None
        self._organization_id = None
        self._project_id = None
        self._project_name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if eip_count_protected is not None:
            self.eip_count_protected = eip_count_protected
        if eip_count_total is not None:
            self.eip_count_total = eip_count_total
        if eip_count_unprotected is not None:
            self.eip_count_unprotected = eip_count_unprotected
        if organization_id is not None:
            self.organization_id = organization_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name

    @property
    def account_id(self):
        r"""Gets the account_id of this AccountVO.

        **参数解释**： 账号ID **取值范围**： 不涉及

        :return: The account_id of this AccountVO.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this AccountVO.

        **参数解释**： 账号ID **取值范围**： 不涉及

        :param account_id: The account_id of this AccountVO.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        r"""Gets the account_name of this AccountVO.

        **参数解释**： 账号名称 **取值范围**： 不涉及

        :return: The account_name of this AccountVO.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this AccountVO.

        **参数解释**： 账号名称 **取值范围**： 不涉及

        :param account_name: The account_name of this AccountVO.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def eip_count_protected(self):
        r"""Gets the eip_count_protected of this AccountVO.

        **参数解释**： 防护的EIP数量 **取值范围**： 不涉及

        :return: The eip_count_protected of this AccountVO.
        :rtype: int
        """
        return self._eip_count_protected

    @eip_count_protected.setter
    def eip_count_protected(self, eip_count_protected):
        r"""Sets the eip_count_protected of this AccountVO.

        **参数解释**： 防护的EIP数量 **取值范围**： 不涉及

        :param eip_count_protected: The eip_count_protected of this AccountVO.
        :type eip_count_protected: int
        """
        self._eip_count_protected = eip_count_protected

    @property
    def eip_count_total(self):
        r"""Gets the eip_count_total of this AccountVO.

        **参数解释**： EIP总数 **取值范围**： 不涉及

        :return: The eip_count_total of this AccountVO.
        :rtype: int
        """
        return self._eip_count_total

    @eip_count_total.setter
    def eip_count_total(self, eip_count_total):
        r"""Sets the eip_count_total of this AccountVO.

        **参数解释**： EIP总数 **取值范围**： 不涉及

        :param eip_count_total: The eip_count_total of this AccountVO.
        :type eip_count_total: int
        """
        self._eip_count_total = eip_count_total

    @property
    def eip_count_unprotected(self):
        r"""Gets the eip_count_unprotected of this AccountVO.

        **参数解释**： 未开启防护的EIP数量 **取值范围**： 不涉及

        :return: The eip_count_unprotected of this AccountVO.
        :rtype: int
        """
        return self._eip_count_unprotected

    @eip_count_unprotected.setter
    def eip_count_unprotected(self, eip_count_unprotected):
        r"""Sets the eip_count_unprotected of this AccountVO.

        **参数解释**： 未开启防护的EIP数量 **取值范围**： 不涉及

        :param eip_count_unprotected: The eip_count_unprotected of this AccountVO.
        :type eip_count_unprotected: int
        """
        self._eip_count_unprotected = eip_count_unprotected

    @property
    def organization_id(self):
        r"""Gets the organization_id of this AccountVO.

        **参数解释**： 组织ID **取值范围**： 不涉及

        :return: The organization_id of this AccountVO.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this AccountVO.

        **参数解释**： 组织ID **取值范围**： 不涉及

        :param organization_id: The organization_id of this AccountVO.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def project_id(self):
        r"""Gets the project_id of this AccountVO.

        **参数解释**： 项目ID **取值范围**： 不涉及

        :return: The project_id of this AccountVO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AccountVO.

        **参数解释**： 项目ID **取值范围**： 不涉及

        :param project_id: The project_id of this AccountVO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this AccountVO.

        **参数解释**： 项目名称 **取值范围**： 不涉及

        :return: The project_name of this AccountVO.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this AccountVO.

        **参数解释**： 项目名称 **取值范围**： 不涉及

        :param project_name: The project_name of this AccountVO.
        :type project_name: str
        """
        self._project_name = project_name

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
        if not isinstance(other, AccountVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
