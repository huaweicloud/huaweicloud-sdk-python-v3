# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckPolicyInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'policy_id': 'str',
        'content': 'str',
        'pwd_policy_content': 'PwdCheckTagInfo'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'policy_id': 'policy_id',
        'content': 'content',
        'pwd_policy_content': 'pwd_policy_content'
    }

    def __init__(self, policy_name=None, policy_id=None, content=None, pwd_policy_content=None):
        r"""SecurityCheckPolicyInfoResponseInfo

        The model defined in huaweicloud sdk

        :param policy_name: **参数解释**： 策略名称 **取值范围**： 字符长度1-256位 
        :type policy_name: str
        :param policy_id: **参数解释**： 策略ID **取值范围**： 字符长度0-64位 
        :type policy_id: str
        :param content: 策略详情
        :type content: str
        :param pwd_policy_content: 
        :type pwd_policy_content: :class:`huaweicloudsdkhss.v5.PwdCheckTagInfo`
        """
        
        

        self._policy_name = None
        self._policy_id = None
        self._content = None
        self._pwd_policy_content = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if policy_id is not None:
            self.policy_id = policy_id
        if content is not None:
            self.content = content
        if pwd_policy_content is not None:
            self.pwd_policy_content = pwd_policy_content

    @property
    def policy_name(self):
        r"""Gets the policy_name of this SecurityCheckPolicyInfoResponseInfo.

        **参数解释**： 策略名称 **取值范围**： 字符长度1-256位 

        :return: The policy_name of this SecurityCheckPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this SecurityCheckPolicyInfoResponseInfo.

        **参数解释**： 策略名称 **取值范围**： 字符长度1-256位 

        :param policy_name: The policy_name of this SecurityCheckPolicyInfoResponseInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this SecurityCheckPolicyInfoResponseInfo.

        **参数解释**： 策略ID **取值范围**： 字符长度0-64位 

        :return: The policy_id of this SecurityCheckPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this SecurityCheckPolicyInfoResponseInfo.

        **参数解释**： 策略ID **取值范围**： 字符长度0-64位 

        :param policy_id: The policy_id of this SecurityCheckPolicyInfoResponseInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def content(self):
        r"""Gets the content of this SecurityCheckPolicyInfoResponseInfo.

        策略详情

        :return: The content of this SecurityCheckPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this SecurityCheckPolicyInfoResponseInfo.

        策略详情

        :param content: The content of this SecurityCheckPolicyInfoResponseInfo.
        :type content: str
        """
        self._content = content

    @property
    def pwd_policy_content(self):
        r"""Gets the pwd_policy_content of this SecurityCheckPolicyInfoResponseInfo.

        :return: The pwd_policy_content of this SecurityCheckPolicyInfoResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.PwdCheckTagInfo`
        """
        return self._pwd_policy_content

    @pwd_policy_content.setter
    def pwd_policy_content(self, pwd_policy_content):
        r"""Sets the pwd_policy_content of this SecurityCheckPolicyInfoResponseInfo.

        :param pwd_policy_content: The pwd_policy_content of this SecurityCheckPolicyInfoResponseInfo.
        :type pwd_policy_content: :class:`huaweicloudsdkhss.v5.PwdCheckTagInfo`
        """
        self._pwd_policy_content = pwd_policy_content

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
        if not isinstance(other, SecurityCheckPolicyInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
