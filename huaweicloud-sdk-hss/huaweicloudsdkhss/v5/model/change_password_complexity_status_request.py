# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangePasswordComplexityStatusRequest:

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
        'action': 'str',
        'body': 'ChangePasswordComplexityStatusRequestBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'action': 'action',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, action=None, body=None):
        r"""ChangePasswordComplexityStatusRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param action: 动作类型   - ignore ：对口令复杂度检测未通过的主机执行忽略动作    - unignore ：对已忽略的口令复杂度检测未通过的主机执行取消忽略动作
        :type action: str
        :param body: Body of the ChangePasswordComplexityStatusRequest
        :type body: :class:`huaweicloudsdkhss.v5.ChangePasswordComplexityStatusRequestBody`
        """
        
        

        self._enterprise_project_id = None
        self._action = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.action = action
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ChangePasswordComplexityStatusRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ChangePasswordComplexityStatusRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ChangePasswordComplexityStatusRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ChangePasswordComplexityStatusRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def action(self):
        r"""Gets the action of this ChangePasswordComplexityStatusRequest.

        动作类型   - ignore ：对口令复杂度检测未通过的主机执行忽略动作    - unignore ：对已忽略的口令复杂度检测未通过的主机执行取消忽略动作

        :return: The action of this ChangePasswordComplexityStatusRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ChangePasswordComplexityStatusRequest.

        动作类型   - ignore ：对口令复杂度检测未通过的主机执行忽略动作    - unignore ：对已忽略的口令复杂度检测未通过的主机执行取消忽略动作

        :param action: The action of this ChangePasswordComplexityStatusRequest.
        :type action: str
        """
        self._action = action

    @property
    def body(self):
        r"""Gets the body of this ChangePasswordComplexityStatusRequest.

        :return: The body of this ChangePasswordComplexityStatusRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.ChangePasswordComplexityStatusRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ChangePasswordComplexityStatusRequest.

        :param body: The body of this ChangePasswordComplexityStatusRequest.
        :type body: :class:`huaweicloudsdkhss.v5.ChangePasswordComplexityStatusRequestBody`
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
        if not isinstance(other, ChangePasswordComplexityStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
