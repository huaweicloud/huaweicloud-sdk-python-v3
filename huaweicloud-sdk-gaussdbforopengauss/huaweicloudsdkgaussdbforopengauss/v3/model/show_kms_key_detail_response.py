# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKmsKeyDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'key_alias': 'str',
        'domain_id': 'str',
        'key_state': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'key_alias': 'key_alias',
        'domain_id': 'domain_id',
        'key_state': 'key_state'
    }

    def __init__(self, key_id=None, key_alias=None, domain_id=None, key_state=None):
        r"""ShowKmsKeyDetailResponse

        The model defined in huaweicloud sdk

        :param key_id: **参数解释**: 秘钥ID。 **取值范围**: 不涉及。
        :type key_id: str
        :param key_alias: **参数解释**: 密钥别名。 **取值范围**: 不涉及。
        :type key_alias: str
        :param domain_id: **参数解释**: 用户域ID。 **取值范围**: 不涉及。
        :type domain_id: str
        :param key_state: **参数解释**: 秘钥状态。 **取值范围**: - “1”表示待激活状态。 - “2”表示启用状态。 - “3”表示禁用状态。 - “4”表示计划删除状态。 - “5”表示等待导入状态。
        :type key_state: str
        """
        
        super(ShowKmsKeyDetailResponse, self).__init__()

        self._key_id = None
        self._key_alias = None
        self._domain_id = None
        self._key_state = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if key_alias is not None:
            self.key_alias = key_alias
        if domain_id is not None:
            self.domain_id = domain_id
        if key_state is not None:
            self.key_state = key_state

    @property
    def key_id(self):
        r"""Gets the key_id of this ShowKmsKeyDetailResponse.

        **参数解释**: 秘钥ID。 **取值范围**: 不涉及。

        :return: The key_id of this ShowKmsKeyDetailResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this ShowKmsKeyDetailResponse.

        **参数解释**: 秘钥ID。 **取值范围**: 不涉及。

        :param key_id: The key_id of this ShowKmsKeyDetailResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def key_alias(self):
        r"""Gets the key_alias of this ShowKmsKeyDetailResponse.

        **参数解释**: 密钥别名。 **取值范围**: 不涉及。

        :return: The key_alias of this ShowKmsKeyDetailResponse.
        :rtype: str
        """
        return self._key_alias

    @key_alias.setter
    def key_alias(self, key_alias):
        r"""Sets the key_alias of this ShowKmsKeyDetailResponse.

        **参数解释**: 密钥别名。 **取值范围**: 不涉及。

        :param key_alias: The key_alias of this ShowKmsKeyDetailResponse.
        :type key_alias: str
        """
        self._key_alias = key_alias

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowKmsKeyDetailResponse.

        **参数解释**: 用户域ID。 **取值范围**: 不涉及。

        :return: The domain_id of this ShowKmsKeyDetailResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowKmsKeyDetailResponse.

        **参数解释**: 用户域ID。 **取值范围**: 不涉及。

        :param domain_id: The domain_id of this ShowKmsKeyDetailResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def key_state(self):
        r"""Gets the key_state of this ShowKmsKeyDetailResponse.

        **参数解释**: 秘钥状态。 **取值范围**: - “1”表示待激活状态。 - “2”表示启用状态。 - “3”表示禁用状态。 - “4”表示计划删除状态。 - “5”表示等待导入状态。

        :return: The key_state of this ShowKmsKeyDetailResponse.
        :rtype: str
        """
        return self._key_state

    @key_state.setter
    def key_state(self, key_state):
        r"""Sets the key_state of this ShowKmsKeyDetailResponse.

        **参数解释**: 秘钥状态。 **取值范围**: - “1”表示待激活状态。 - “2”表示启用状态。 - “3”表示禁用状态。 - “4”表示计划删除状态。 - “5”表示等待导入状态。

        :param key_state: The key_state of this ShowKmsKeyDetailResponse.
        :type key_state: str
        """
        self._key_state = key_state

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
        if not isinstance(other, ShowKmsKeyDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
