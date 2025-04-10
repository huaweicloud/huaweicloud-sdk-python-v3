# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetOffSiteBackupPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_para': 'OffSiteBackupPolicy'
    }

    attribute_map = {
        'policy_para': 'policy_para'
    }

    def __init__(self, policy_para=None):
        r"""SetOffSiteBackupPolicyRequestBody

        The model defined in huaweicloud sdk

        :param policy_para: 
        :type policy_para: :class:`huaweicloudsdkrds.v3.OffSiteBackupPolicy`
        """
        
        

        self._policy_para = None
        self.discriminator = None

        self.policy_para = policy_para

    @property
    def policy_para(self):
        r"""Gets the policy_para of this SetOffSiteBackupPolicyRequestBody.

        :return: The policy_para of this SetOffSiteBackupPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.OffSiteBackupPolicy`
        """
        return self._policy_para

    @policy_para.setter
    def policy_para(self, policy_para):
        r"""Sets the policy_para of this SetOffSiteBackupPolicyRequestBody.

        :param policy_para: The policy_para of this SetOffSiteBackupPolicyRequestBody.
        :type policy_para: :class:`huaweicloudsdkrds.v3.OffSiteBackupPolicy`
        """
        self._policy_para = policy_para

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
        if not isinstance(other, SetOffSiteBackupPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
