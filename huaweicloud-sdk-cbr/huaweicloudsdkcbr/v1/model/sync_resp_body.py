# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncRespBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_log_id': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'operation_log_id': 'operation_log_id',
        'vault_id': 'vault_id'
    }

    def __init__(self, operation_log_id=None, vault_id=None):
        r"""SyncRespBody

        The model defined in huaweicloud sdk

        :param operation_log_id: 是否自动触发
        :type operation_log_id: str
        :param vault_id: 混合云vault id
        :type vault_id: str
        """
        
        

        self._operation_log_id = None
        self._vault_id = None
        self.discriminator = None

        self.operation_log_id = operation_log_id
        self.vault_id = vault_id

    @property
    def operation_log_id(self):
        r"""Gets the operation_log_id of this SyncRespBody.

        是否自动触发

        :return: The operation_log_id of this SyncRespBody.
        :rtype: str
        """
        return self._operation_log_id

    @operation_log_id.setter
    def operation_log_id(self, operation_log_id):
        r"""Sets the operation_log_id of this SyncRespBody.

        是否自动触发

        :param operation_log_id: The operation_log_id of this SyncRespBody.
        :type operation_log_id: str
        """
        self._operation_log_id = operation_log_id

    @property
    def vault_id(self):
        r"""Gets the vault_id of this SyncRespBody.

        混合云vault id

        :return: The vault_id of this SyncRespBody.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this SyncRespBody.

        混合云vault id

        :param vault_id: The vault_id of this SyncRespBody.
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
        if not isinstance(other, SyncRespBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
