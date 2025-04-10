# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncryptionConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'kms_key_id': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'kms_key_id': 'kmsKeyID'
    }

    def __init__(self, mode=None, kms_key_id=None):
        r"""EncryptionConfig

        The model defined in huaweicloud sdk

        :param mode: **参数解释**： 加密模式，取值为Default或KMS。默认为Default，即使用cce本地密钥加密。若使用KMS加密模式则使用用户自定义密钥或默认密钥加密secret资源。 若用户在创建时未填写，则集群查询接口中默认会返回Default。 **约束限制**： 不涉及 **取值范围**： 取值范围：[Default, KMS]; **默认取值**： Default
        :type mode: str
        :param kms_key_id: **参数解释**： kms密钥ID - 集群创建API中，如果mode字段设置为Default，无需填写该字段；如果mode字段设置为KMS，则支持填写该字段。若字段为空，则默认使用KMS默认密钥进行填充，默认密钥不存在时云服务将自动为用户创建cce/default默认密钥。 用户需使用真实存在的KMS密钥，并且在集群生命周期结束前，禁止删除、禁用密钥等操作，防止集群功能异常（集群设置该密钥后不允许修改）。  - 集群查询API中，如果mode字段设置为Default，则该字段返回为空；若mode字段设置为KMS，则该字段为具体的密钥ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type kms_key_id: str
        """
        
        

        self._mode = None
        self._kms_key_id = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id

    @property
    def mode(self):
        r"""Gets the mode of this EncryptionConfig.

        **参数解释**： 加密模式，取值为Default或KMS。默认为Default，即使用cce本地密钥加密。若使用KMS加密模式则使用用户自定义密钥或默认密钥加密secret资源。 若用户在创建时未填写，则集群查询接口中默认会返回Default。 **约束限制**： 不涉及 **取值范围**： 取值范围：[Default, KMS]; **默认取值**： Default

        :return: The mode of this EncryptionConfig.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this EncryptionConfig.

        **参数解释**： 加密模式，取值为Default或KMS。默认为Default，即使用cce本地密钥加密。若使用KMS加密模式则使用用户自定义密钥或默认密钥加密secret资源。 若用户在创建时未填写，则集群查询接口中默认会返回Default。 **约束限制**： 不涉及 **取值范围**： 取值范围：[Default, KMS]; **默认取值**： Default

        :param mode: The mode of this EncryptionConfig.
        :type mode: str
        """
        self._mode = mode

    @property
    def kms_key_id(self):
        r"""Gets the kms_key_id of this EncryptionConfig.

        **参数解释**： kms密钥ID - 集群创建API中，如果mode字段设置为Default，无需填写该字段；如果mode字段设置为KMS，则支持填写该字段。若字段为空，则默认使用KMS默认密钥进行填充，默认密钥不存在时云服务将自动为用户创建cce/default默认密钥。 用户需使用真实存在的KMS密钥，并且在集群生命周期结束前，禁止删除、禁用密钥等操作，防止集群功能异常（集群设置该密钥后不允许修改）。  - 集群查询API中，如果mode字段设置为Default，则该字段返回为空；若mode字段设置为KMS，则该字段为具体的密钥ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The kms_key_id of this EncryptionConfig.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        r"""Sets the kms_key_id of this EncryptionConfig.

        **参数解释**： kms密钥ID - 集群创建API中，如果mode字段设置为Default，无需填写该字段；如果mode字段设置为KMS，则支持填写该字段。若字段为空，则默认使用KMS默认密钥进行填充，默认密钥不存在时云服务将自动为用户创建cce/default默认密钥。 用户需使用真实存在的KMS密钥，并且在集群生命周期结束前，禁止删除、禁用密钥等操作，防止集群功能异常（集群设置该密钥后不允许修改）。  - 集群查询API中，如果mode字段设置为Default，则该字段返回为空；若mode字段设置为KMS，则该字段为具体的密钥ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param kms_key_id: The kms_key_id of this EncryptionConfig.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

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
        if not isinstance(other, EncryptionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
