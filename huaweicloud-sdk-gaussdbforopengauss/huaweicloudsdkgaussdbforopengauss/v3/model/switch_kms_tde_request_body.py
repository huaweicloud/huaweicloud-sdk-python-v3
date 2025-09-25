# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchKmsTdeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kms_tde_key_id': 'str',
        'kms_project_name': 'str',
        'kms_tde_status': 'str'
    }

    attribute_map = {
        'kms_tde_key_id': 'kms_tde_key_id',
        'kms_project_name': 'kms_project_name',
        'kms_tde_status': 'kms_tde_status'
    }

    def __init__(self, kms_tde_key_id=None, kms_project_name=None, kms_tde_status=None):
        r"""SwitchKmsTdeRequestBody

        The model defined in huaweicloud sdk

        :param kms_tde_key_id: **参数解释**: kms主密钥ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type kms_tde_key_id: str
        :param kms_project_name: **参数解释**: GaussDB使用透明加密的KMS主密钥ID所在资源空间名称。 获取方法请参见[获取项目名称](https://support.huaweicloud.com/api-gaussdb/gaussdb_api_196.html)。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type kms_project_name: str
        :param kms_tde_status: **参数解释**: 需要切换的状态：on表示开启。 **约束限制**: 不涉及。 **取值范围**: on: 开启。 **默认取值**: on
        :type kms_tde_status: str
        """
        
        

        self._kms_tde_key_id = None
        self._kms_project_name = None
        self._kms_tde_status = None
        self.discriminator = None

        self.kms_tde_key_id = kms_tde_key_id
        self.kms_project_name = kms_project_name
        self.kms_tde_status = kms_tde_status

    @property
    def kms_tde_key_id(self):
        r"""Gets the kms_tde_key_id of this SwitchKmsTdeRequestBody.

        **参数解释**: kms主密钥ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The kms_tde_key_id of this SwitchKmsTdeRequestBody.
        :rtype: str
        """
        return self._kms_tde_key_id

    @kms_tde_key_id.setter
    def kms_tde_key_id(self, kms_tde_key_id):
        r"""Sets the kms_tde_key_id of this SwitchKmsTdeRequestBody.

        **参数解释**: kms主密钥ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param kms_tde_key_id: The kms_tde_key_id of this SwitchKmsTdeRequestBody.
        :type kms_tde_key_id: str
        """
        self._kms_tde_key_id = kms_tde_key_id

    @property
    def kms_project_name(self):
        r"""Gets the kms_project_name of this SwitchKmsTdeRequestBody.

        **参数解释**: GaussDB使用透明加密的KMS主密钥ID所在资源空间名称。 获取方法请参见[获取项目名称](https://support.huaweicloud.com/api-gaussdb/gaussdb_api_196.html)。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The kms_project_name of this SwitchKmsTdeRequestBody.
        :rtype: str
        """
        return self._kms_project_name

    @kms_project_name.setter
    def kms_project_name(self, kms_project_name):
        r"""Sets the kms_project_name of this SwitchKmsTdeRequestBody.

        **参数解释**: GaussDB使用透明加密的KMS主密钥ID所在资源空间名称。 获取方法请参见[获取项目名称](https://support.huaweicloud.com/api-gaussdb/gaussdb_api_196.html)。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param kms_project_name: The kms_project_name of this SwitchKmsTdeRequestBody.
        :type kms_project_name: str
        """
        self._kms_project_name = kms_project_name

    @property
    def kms_tde_status(self):
        r"""Gets the kms_tde_status of this SwitchKmsTdeRequestBody.

        **参数解释**: 需要切换的状态：on表示开启。 **约束限制**: 不涉及。 **取值范围**: on: 开启。 **默认取值**: on

        :return: The kms_tde_status of this SwitchKmsTdeRequestBody.
        :rtype: str
        """
        return self._kms_tde_status

    @kms_tde_status.setter
    def kms_tde_status(self, kms_tde_status):
        r"""Sets the kms_tde_status of this SwitchKmsTdeRequestBody.

        **参数解释**: 需要切换的状态：on表示开启。 **约束限制**: 不涉及。 **取值范围**: on: 开启。 **默认取值**: on

        :param kms_tde_status: The kms_tde_status of this SwitchKmsTdeRequestBody.
        :type kms_tde_status: str
        """
        self._kms_tde_status = kms_tde_status

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
        if not isinstance(other, SwitchKmsTdeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
