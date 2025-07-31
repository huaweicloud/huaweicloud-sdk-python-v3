# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupVaultsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'vault_name': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'vault_name': 'vault_name',
        'vault_id': 'vault_id'
    }

    def __init__(self, offset=None, limit=None, vault_name=None, vault_id=None):
        r"""ListBackupVaultsRequest

        The model defined in huaweicloud sdk

        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param vault_name: 备份存储库名称
        :type vault_name: str
        :param vault_id: 备份存储库id
        :type vault_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._vault_name = None
        self._vault_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if vault_name is not None:
            self.vault_name = vault_name
        if vault_id is not None:
            self.vault_id = vault_id

    @property
    def offset(self):
        r"""Gets the offset of this ListBackupVaultsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListBackupVaultsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBackupVaultsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListBackupVaultsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListBackupVaultsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListBackupVaultsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBackupVaultsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListBackupVaultsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def vault_name(self):
        r"""Gets the vault_name of this ListBackupVaultsRequest.

        备份存储库名称

        :return: The vault_name of this ListBackupVaultsRequest.
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        r"""Sets the vault_name of this ListBackupVaultsRequest.

        备份存储库名称

        :param vault_name: The vault_name of this ListBackupVaultsRequest.
        :type vault_name: str
        """
        self._vault_name = vault_name

    @property
    def vault_id(self):
        r"""Gets the vault_id of this ListBackupVaultsRequest.

        备份存储库id

        :return: The vault_id of this ListBackupVaultsRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this ListBackupVaultsRequest.

        备份存储库id

        :param vault_id: The vault_id of this ListBackupVaultsRequest.
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
        if not isinstance(other, ListBackupVaultsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
