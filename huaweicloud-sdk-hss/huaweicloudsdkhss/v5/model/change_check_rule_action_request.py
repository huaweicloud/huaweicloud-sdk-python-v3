# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeCheckRuleActionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'host_id': 'str',
        'check_cce': 'bool',
        'action': 'str',
        'body': 'CheckRuleIdListRequestInfo'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'check_cce': 'check_cce',
        'action': 'action',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, host_id=None, check_cce=None, action=None, body=None):
        r"""ChangeCheckRuleActionRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param host_id: 主机ID，不赋值时，查租户所有主机
        :type host_id: str
        :param check_cce: 是否校验cce
        :type check_cce: bool
        :param action: 动作 - \&quot;ignore\&quot; - \&quot;unignore\&quot; - \&quot;fix\&quot; - \&quot;verify\&quot;
        :type action: str
        :param body: Body of the ChangeCheckRuleActionRequest
        :type body: :class:`huaweicloudsdkhss.v5.CheckRuleIdListRequestInfo`
        """
        
        

        self._enterprise_project_id = None
        self._host_id = None
        self._check_cce = None
        self._action = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_id is not None:
            self.host_id = host_id
        if check_cce is not None:
            self.check_cce = check_cce
        self.action = action
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ChangeCheckRuleActionRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ChangeCheckRuleActionRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ChangeCheckRuleActionRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ChangeCheckRuleActionRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ChangeCheckRuleActionRequest.

        主机ID，不赋值时，查租户所有主机

        :return: The host_id of this ChangeCheckRuleActionRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ChangeCheckRuleActionRequest.

        主机ID，不赋值时，查租户所有主机

        :param host_id: The host_id of this ChangeCheckRuleActionRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def check_cce(self):
        r"""Gets the check_cce of this ChangeCheckRuleActionRequest.

        是否校验cce

        :return: The check_cce of this ChangeCheckRuleActionRequest.
        :rtype: bool
        """
        return self._check_cce

    @check_cce.setter
    def check_cce(self, check_cce):
        r"""Sets the check_cce of this ChangeCheckRuleActionRequest.

        是否校验cce

        :param check_cce: The check_cce of this ChangeCheckRuleActionRequest.
        :type check_cce: bool
        """
        self._check_cce = check_cce

    @property
    def action(self):
        r"""Gets the action of this ChangeCheckRuleActionRequest.

        动作 - \"ignore\" - \"unignore\" - \"fix\" - \"verify\"

        :return: The action of this ChangeCheckRuleActionRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ChangeCheckRuleActionRequest.

        动作 - \"ignore\" - \"unignore\" - \"fix\" - \"verify\"

        :param action: The action of this ChangeCheckRuleActionRequest.
        :type action: str
        """
        self._action = action

    @property
    def body(self):
        r"""Gets the body of this ChangeCheckRuleActionRequest.

        :return: The body of this ChangeCheckRuleActionRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.CheckRuleIdListRequestInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ChangeCheckRuleActionRequest.

        :param body: The body of this ChangeCheckRuleActionRequest.
        :type body: :class:`huaweicloudsdkhss.v5.CheckRuleIdListRequestInfo`
        """
        self._body = body

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
        if not isinstance(other, ChangeCheckRuleActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
