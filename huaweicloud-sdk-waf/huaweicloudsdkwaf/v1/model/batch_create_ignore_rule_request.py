# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateIgnoreRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'projectid': 'str',
        'policyids': 'str',
        'enterprise_project_id': 'str',
        'body': 'BatchCreateIgnoreRuleRequestBody'
    }

    attribute_map = {
        'projectid': 'projectid',
        'policyids': 'policyids',
        'enterprise_project_id': 'enterprise_project_id',
        'body': 'body'
    }

    def __init__(self, projectid=None, policyids=None, enterprise_project_id=None, body=None):
        r"""BatchCreateIgnoreRuleRequest

        The model defined in huaweicloud sdk

        :param projectid: **参数解释：** 项目ID，对应控制台用户名-&gt;我的凭证-&gt;项目列表-&gt;项目ID。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及
        :type projectid: str
        :param policyids: **参数解释：** 域名id。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及
        :type policyids: str
        :param enterprise_project_id: **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符  **默认取值：** 0
        :type enterprise_project_id: str
        :param body: Body of the BatchCreateIgnoreRuleRequest
        :type body: :class:`huaweicloudsdkwaf.v1.BatchCreateIgnoreRuleRequestBody`
        """
        
        

        self._projectid = None
        self._policyids = None
        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.projectid = projectid
        if policyids is not None:
            self.policyids = policyids
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def projectid(self):
        r"""Gets the projectid of this BatchCreateIgnoreRuleRequest.

        **参数解释：** 项目ID，对应控制台用户名->我的凭证->项目列表->项目ID。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及

        :return: The projectid of this BatchCreateIgnoreRuleRequest.
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        r"""Sets the projectid of this BatchCreateIgnoreRuleRequest.

        **参数解释：** 项目ID，对应控制台用户名->我的凭证->项目列表->项目ID。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及

        :param projectid: The projectid of this BatchCreateIgnoreRuleRequest.
        :type projectid: str
        """
        self._projectid = projectid

    @property
    def policyids(self):
        r"""Gets the policyids of this BatchCreateIgnoreRuleRequest.

        **参数解释：** 域名id。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及

        :return: The policyids of this BatchCreateIgnoreRuleRequest.
        :rtype: str
        """
        return self._policyids

    @policyids.setter
    def policyids(self, policyids):
        r"""Sets the policyids of this BatchCreateIgnoreRuleRequest.

        **参数解释：** 域名id。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及

        :param policyids: The policyids of this BatchCreateIgnoreRuleRequest.
        :type policyids: str
        """
        self._policyids = policyids

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this BatchCreateIgnoreRuleRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符  **默认取值：** 0

        :return: The enterprise_project_id of this BatchCreateIgnoreRuleRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this BatchCreateIgnoreRuleRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符  **默认取值：** 0

        :param enterprise_project_id: The enterprise_project_id of this BatchCreateIgnoreRuleRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        r"""Gets the body of this BatchCreateIgnoreRuleRequest.

        :return: The body of this BatchCreateIgnoreRuleRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.BatchCreateIgnoreRuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCreateIgnoreRuleRequest.

        :param body: The body of this BatchCreateIgnoreRuleRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.BatchCreateIgnoreRuleRequestBody`
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
        if not isinstance(other, BatchCreateIgnoreRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
