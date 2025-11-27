# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupUpdateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'sync_mode': 'str',
        'sync_rules': 'list[GroupUpdateRequestSyncRules]',
        'relation_configurations': 'list[GroupRelationConfiguration]'
    }

    attribute_map = {
        'name': 'name',
        'sync_mode': 'sync_mode',
        'sync_rules': 'sync_rules',
        'relation_configurations': 'relation_configurations'
    }

    def __init__(self, name=None, sync_mode=None, sync_rules=None, relation_configurations=None):
        r"""GroupUpdateRequest

        The model defined in huaweicloud sdk

        :param name: 分组名称。
        :type name: str
        :param sync_mode: 资源关联方式，MANUAL表示手动，AUTO表示智能。
        :type sync_mode: str
        :param sync_rules: 智能关联规则。
        :type sync_rules: list[:class:`huaweicloudsdkcoc.v1.GroupUpdateRequestSyncRules`]
        :param relation_configurations: 分组配置信息。
        :type relation_configurations: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        """
        
        

        self._name = None
        self._sync_mode = None
        self._sync_rules = None
        self._relation_configurations = None
        self.discriminator = None

        self.name = name
        self.sync_mode = sync_mode
        if sync_rules is not None:
            self.sync_rules = sync_rules
        if relation_configurations is not None:
            self.relation_configurations = relation_configurations

    @property
    def name(self):
        r"""Gets the name of this GroupUpdateRequest.

        分组名称。

        :return: The name of this GroupUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupUpdateRequest.

        分组名称。

        :param name: The name of this GroupUpdateRequest.
        :type name: str
        """
        self._name = name

    @property
    def sync_mode(self):
        r"""Gets the sync_mode of this GroupUpdateRequest.

        资源关联方式，MANUAL表示手动，AUTO表示智能。

        :return: The sync_mode of this GroupUpdateRequest.
        :rtype: str
        """
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, sync_mode):
        r"""Sets the sync_mode of this GroupUpdateRequest.

        资源关联方式，MANUAL表示手动，AUTO表示智能。

        :param sync_mode: The sync_mode of this GroupUpdateRequest.
        :type sync_mode: str
        """
        self._sync_mode = sync_mode

    @property
    def sync_rules(self):
        r"""Gets the sync_rules of this GroupUpdateRequest.

        智能关联规则。

        :return: The sync_rules of this GroupUpdateRequest.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.GroupUpdateRequestSyncRules`]
        """
        return self._sync_rules

    @sync_rules.setter
    def sync_rules(self, sync_rules):
        r"""Sets the sync_rules of this GroupUpdateRequest.

        智能关联规则。

        :param sync_rules: The sync_rules of this GroupUpdateRequest.
        :type sync_rules: list[:class:`huaweicloudsdkcoc.v1.GroupUpdateRequestSyncRules`]
        """
        self._sync_rules = sync_rules

    @property
    def relation_configurations(self):
        r"""Gets the relation_configurations of this GroupUpdateRequest.

        分组配置信息。

        :return: The relation_configurations of this GroupUpdateRequest.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        """
        return self._relation_configurations

    @relation_configurations.setter
    def relation_configurations(self, relation_configurations):
        r"""Sets the relation_configurations of this GroupUpdateRequest.

        分组配置信息。

        :param relation_configurations: The relation_configurations of this GroupUpdateRequest.
        :type relation_configurations: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        """
        self._relation_configurations = relation_configurations

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GroupUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
