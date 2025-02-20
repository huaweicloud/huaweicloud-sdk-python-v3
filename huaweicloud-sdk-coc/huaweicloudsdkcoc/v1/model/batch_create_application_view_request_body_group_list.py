# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateApplicationViewRequestBodyGroupList:

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
        'region_id': 'str',
        'parent_name': 'str',
        'sync_mode': 'str',
        'cmdb_resource_id_list': 'list[str]',
        'sync_rules': 'list[BatchCreateApplicationViewRequestBodySyncRules]'
    }

    attribute_map = {
        'name': 'name',
        'region_id': 'region_id',
        'parent_name': 'parent_name',
        'sync_mode': 'sync_mode',
        'cmdb_resource_id_list': 'cmdb_resource_id_list',
        'sync_rules': 'sync_rules'
    }

    def __init__(self, name=None, region_id=None, parent_name=None, sync_mode=None, cmdb_resource_id_list=None, sync_rules=None):
        """BatchCreateApplicationViewRequestBodyGroupList

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param region_id: region id
        :type region_id: str
        :param parent_name: 父节点code
        :type parent_name: str
        :param sync_mode: 同步模式
        :type sync_mode: str
        :param cmdb_resource_id_list: 关联的资源id列表
        :type cmdb_resource_id_list: list[str]
        :param sync_rules: 智能关联规则
        :type sync_rules: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodySyncRules`]
        """
        
        

        self._name = None
        self._region_id = None
        self._parent_name = None
        self._sync_mode = None
        self._cmdb_resource_id_list = None
        self._sync_rules = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if region_id is not None:
            self.region_id = region_id
        if parent_name is not None:
            self.parent_name = parent_name
        if sync_mode is not None:
            self.sync_mode = sync_mode
        if cmdb_resource_id_list is not None:
            self.cmdb_resource_id_list = cmdb_resource_id_list
        if sync_rules is not None:
            self.sync_rules = sync_rules

    @property
    def name(self):
        """Gets the name of this BatchCreateApplicationViewRequestBodyGroupList.

        名称

        :return: The name of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchCreateApplicationViewRequestBodyGroupList.

        名称

        :param name: The name of this BatchCreateApplicationViewRequestBodyGroupList.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        """Gets the region_id of this BatchCreateApplicationViewRequestBodyGroupList.

        region id

        :return: The region_id of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this BatchCreateApplicationViewRequestBodyGroupList.

        region id

        :param region_id: The region_id of this BatchCreateApplicationViewRequestBodyGroupList.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def parent_name(self):
        """Gets the parent_name of this BatchCreateApplicationViewRequestBodyGroupList.

        父节点code

        :return: The parent_name of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """Sets the parent_name of this BatchCreateApplicationViewRequestBodyGroupList.

        父节点code

        :param parent_name: The parent_name of this BatchCreateApplicationViewRequestBodyGroupList.
        :type parent_name: str
        """
        self._parent_name = parent_name

    @property
    def sync_mode(self):
        """Gets the sync_mode of this BatchCreateApplicationViewRequestBodyGroupList.

        同步模式

        :return: The sync_mode of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, sync_mode):
        """Sets the sync_mode of this BatchCreateApplicationViewRequestBodyGroupList.

        同步模式

        :param sync_mode: The sync_mode of this BatchCreateApplicationViewRequestBodyGroupList.
        :type sync_mode: str
        """
        self._sync_mode = sync_mode

    @property
    def cmdb_resource_id_list(self):
        """Gets the cmdb_resource_id_list of this BatchCreateApplicationViewRequestBodyGroupList.

        关联的资源id列表

        :return: The cmdb_resource_id_list of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: list[str]
        """
        return self._cmdb_resource_id_list

    @cmdb_resource_id_list.setter
    def cmdb_resource_id_list(self, cmdb_resource_id_list):
        """Sets the cmdb_resource_id_list of this BatchCreateApplicationViewRequestBodyGroupList.

        关联的资源id列表

        :param cmdb_resource_id_list: The cmdb_resource_id_list of this BatchCreateApplicationViewRequestBodyGroupList.
        :type cmdb_resource_id_list: list[str]
        """
        self._cmdb_resource_id_list = cmdb_resource_id_list

    @property
    def sync_rules(self):
        """Gets the sync_rules of this BatchCreateApplicationViewRequestBodyGroupList.

        智能关联规则

        :return: The sync_rules of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodySyncRules`]
        """
        return self._sync_rules

    @sync_rules.setter
    def sync_rules(self, sync_rules):
        """Sets the sync_rules of this BatchCreateApplicationViewRequestBodyGroupList.

        智能关联规则

        :param sync_rules: The sync_rules of this BatchCreateApplicationViewRequestBodyGroupList.
        :type sync_rules: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodySyncRules`]
        """
        self._sync_rules = sync_rules

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
        if not isinstance(other, BatchCreateApplicationViewRequestBodyGroupList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
