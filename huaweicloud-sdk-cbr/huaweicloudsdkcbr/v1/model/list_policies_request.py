# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_type': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'operation_type': 'operation_type',
        'vault_id': 'vault_id'
    }

    def __init__(self, operation_type=None, vault_id=None):
        r"""ListPoliciesRequest

        The model defined in huaweicloud sdk

        :param operation_type: 策略类型：备份（backup）、复制(replication)
        :type operation_type: str
        :param vault_id: 存储库ID
        :type vault_id: str
        """
        
        

        self._operation_type = None
        self._vault_id = None
        self.discriminator = None

        if operation_type is not None:
            self.operation_type = operation_type
        if vault_id is not None:
            self.vault_id = vault_id

    @property
    def operation_type(self):
        r"""Gets the operation_type of this ListPoliciesRequest.

        策略类型：备份（backup）、复制(replication)

        :return: The operation_type of this ListPoliciesRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this ListPoliciesRequest.

        策略类型：备份（backup）、复制(replication)

        :param operation_type: The operation_type of this ListPoliciesRequest.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def vault_id(self):
        r"""Gets the vault_id of this ListPoliciesRequest.

        存储库ID

        :return: The vault_id of this ListPoliciesRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this ListPoliciesRequest.

        存储库ID

        :param vault_id: The vault_id of this ListPoliciesRequest.
        :type vault_id: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, ListPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
