# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeAppWhitelistPolicyProcessStatusRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_status': 'str',
        'process_hash_list': 'list[str]'
    }

    attribute_map = {
        'process_status': 'process_status',
        'process_hash_list': 'process_hash_list'
    }

    def __init__(self, process_status=None, process_hash_list=None):
        r"""ChangeAppWhitelistPolicyProcessStatusRequestInfo

        The model defined in huaweicloud sdk

        :param process_status: **参数解释**： 进程可信状态 **约束限制**: 不涉及 **取值范围**: - trust：可信 - suspicious：可疑 - malicious：恶意 - unknown：未知  **默认取值**: 不涉及 
        :type process_status: str
        :param process_hash_list: 进程hash列表
        :type process_hash_list: list[str]
        """
        
        

        self._process_status = None
        self._process_hash_list = None
        self.discriminator = None

        self.process_status = process_status
        self.process_hash_list = process_hash_list

    @property
    def process_status(self):
        r"""Gets the process_status of this ChangeAppWhitelistPolicyProcessStatusRequestInfo.

        **参数解释**： 进程可信状态 **约束限制**: 不涉及 **取值范围**: - trust：可信 - suspicious：可疑 - malicious：恶意 - unknown：未知  **默认取值**: 不涉及 

        :return: The process_status of this ChangeAppWhitelistPolicyProcessStatusRequestInfo.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this ChangeAppWhitelistPolicyProcessStatusRequestInfo.

        **参数解释**： 进程可信状态 **约束限制**: 不涉及 **取值范围**: - trust：可信 - suspicious：可疑 - malicious：恶意 - unknown：未知  **默认取值**: 不涉及 

        :param process_status: The process_status of this ChangeAppWhitelistPolicyProcessStatusRequestInfo.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def process_hash_list(self):
        r"""Gets the process_hash_list of this ChangeAppWhitelistPolicyProcessStatusRequestInfo.

        进程hash列表

        :return: The process_hash_list of this ChangeAppWhitelistPolicyProcessStatusRequestInfo.
        :rtype: list[str]
        """
        return self._process_hash_list

    @process_hash_list.setter
    def process_hash_list(self, process_hash_list):
        r"""Sets the process_hash_list of this ChangeAppWhitelistPolicyProcessStatusRequestInfo.

        进程hash列表

        :param process_hash_list: The process_hash_list of this ChangeAppWhitelistPolicyProcessStatusRequestInfo.
        :type process_hash_list: list[str]
        """
        self._process_hash_list = process_hash_list

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
        if not isinstance(other, ChangeAppWhitelistPolicyProcessStatusRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
