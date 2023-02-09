# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VaultResourceInstancesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'without_any_tag': 'bool',
        'tags': 'list[TagsReq]',
        'tags_any': 'list[TagsReq]',
        'not_tags': 'list[TagsReq]',
        'not_tags_any': 'list[TagsReq]',
        'sys_tags': 'list[SysTags]',
        'limit': 'str',
        'offset': 'str',
        'action': 'str',
        'matches': 'list[Match]',
        'cloud_type': 'str',
        'object_type': 'str'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any',
        'sys_tags': 'sys_tags',
        'limit': 'limit',
        'offset': 'offset',
        'action': 'action',
        'matches': 'matches',
        'cloud_type': 'cloud_type',
        'object_type': 'object_type'
    }

    def __init__(self, without_any_tag=None, tags=None, tags_any=None, not_tags=None, not_tags_any=None, sys_tags=None, limit=None, offset=None, action=None, matches=None, cloud_type=None, object_type=None):
        """VaultResourceInstancesReq

        The model defined in huaweicloud sdk

        :param without_any_tag: 不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。
        :type without_any_tag: bool
        :param tags: 包含标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  tags中多个key之间是“与”的关系。  结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。
        :type tags: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        :param tags_any: 包含任一标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  结果返回包含任一标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。
        :type tags_any: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        :param not_tags: 不包含标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  结果返回不包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。
        :type not_tags: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        :param not_tags_any: 不包含任一标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  结果返回不包含任一标签的资源列表，key之间是或的关系，key-value结构张value是或的关系。  无过滤条件时返回全量数据。
        :type not_tags_any: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        :param sys_tags: 仅op_service权限可以使用此字段做资源实例过滤条件。  目前TMS调用时只包含一个tag结构体。  * key： _sys_enterprise_project_id  * values：企业项目id列表  目前TMS调用时，key下面只包含一个value，0表示默认企业项目。  sys_tags和租户标签过滤条件（tags、tags_any、not_tags、not_tags_any）不能同时使用。  无sys_tags时按照tag接口处理，无tag过滤条件时返回全量数据。  sys_tags不能为空列表
        :type sys_tags: list[:class:`huaweicloudsdkcbr.v1.SysTags`]
        :param limit: 查询记录数（action为count时无此参数）如果action为filter时，默认为1000，limit最小值为1，limit最大值为1000, 不在范围内报错。返回的结果中记录数不超过limit。
        :type limit: str
        :param offset: 索引位置（action为count时无此参数）如果action为filter时，默认为0，offset最小值为0。返回的结果中第一条记录为符合查询条件的第offset+1条记录。
        :type offset: str
        :param action: 操作标识取值范围为：\&quot;filter\&quot;, \&quot;count\&quot;。如果是filter就是分页查询，如果是count只需按照条件将总条数返回即可
        :type action: str
        :param matches: 资源本身支持的查询条件。  matches中key不允许重复。  数组长度最大值为 1，后续再扩展。
        :type matches: list[:class:`huaweicloudsdkcbr.v1.Match`]
        :param cloud_type: 云类型
        :type cloud_type: str
        :param object_type: 资源类型
        :type object_type: str
        """
        
        

        self._without_any_tag = None
        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self._sys_tags = None
        self._limit = None
        self._offset = None
        self._action = None
        self._matches = None
        self._cloud_type = None
        self._object_type = None
        self.discriminator = None

        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags is not None:
            self.tags = tags
        if tags_any is not None:
            self.tags_any = tags_any
        if not_tags is not None:
            self.not_tags = not_tags
        if not_tags_any is not None:
            self.not_tags_any = not_tags_any
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.action = action
        if matches is not None:
            self.matches = matches
        if cloud_type is not None:
            self.cloud_type = cloud_type
        if object_type is not None:
            self.object_type = object_type

    @property
    def without_any_tag(self):
        """Gets the without_any_tag of this VaultResourceInstancesReq.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。

        :return: The without_any_tag of this VaultResourceInstancesReq.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        """Sets the without_any_tag of this VaultResourceInstancesReq.

        不包含任意一个标签，该字段为true时查询所有不带标签的资源，此时忽略 “tags”、“tags_any”、“not_tags”、“not_tags_any”字段。

        :param without_any_tag: The without_any_tag of this VaultResourceInstancesReq.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        """Gets the tags of this VaultResourceInstancesReq.

        包含标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  tags中多个key之间是“与”的关系。  结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :return: The tags of this VaultResourceInstancesReq.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VaultResourceInstancesReq.

        包含标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  tags中多个key之间是“与”的关系。  结果返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :param tags: The tags of this VaultResourceInstancesReq.
        :type tags: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this VaultResourceInstancesReq.

        包含任一标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  结果返回包含任一标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :return: The tags_any of this VaultResourceInstancesReq.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this VaultResourceInstancesReq.

        包含任一标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  结果返回包含任一标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :param tags_any: The tags_any of this VaultResourceInstancesReq.
        :type tags_any: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        """Gets the not_tags of this VaultResourceInstancesReq.

        不包含标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  结果返回不包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :return: The not_tags of this VaultResourceInstancesReq.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this VaultResourceInstancesReq.

        不包含标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  结果返回不包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。  无过滤条件时返回全量数据。

        :param not_tags: The not_tags of this VaultResourceInstancesReq.
        :type not_tags: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this VaultResourceInstancesReq.

        不包含任一标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  结果返回不包含任一标签的资源列表，key之间是或的关系，key-value结构张value是或的关系。  无过滤条件时返回全量数据。

        :return: The not_tags_any of this VaultResourceInstancesReq.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this VaultResourceInstancesReq.

        不包含任一标签。  tags不允许为空列表。  tags中最多包含10个key。  tags中key不允许重复。  结果返回不包含任一标签的资源列表，key之间是或的关系，key-value结构张value是或的关系。  无过滤条件时返回全量数据。

        :param not_tags_any: The not_tags_any of this VaultResourceInstancesReq.
        :type not_tags_any: list[:class:`huaweicloudsdkcbr.v1.TagsReq`]
        """
        self._not_tags_any = not_tags_any

    @property
    def sys_tags(self):
        """Gets the sys_tags of this VaultResourceInstancesReq.

        仅op_service权限可以使用此字段做资源实例过滤条件。  目前TMS调用时只包含一个tag结构体。  * key： _sys_enterprise_project_id  * values：企业项目id列表  目前TMS调用时，key下面只包含一个value，0表示默认企业项目。  sys_tags和租户标签过滤条件（tags、tags_any、not_tags、not_tags_any）不能同时使用。  无sys_tags时按照tag接口处理，无tag过滤条件时返回全量数据。  sys_tags不能为空列表

        :return: The sys_tags of this VaultResourceInstancesReq.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.SysTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this VaultResourceInstancesReq.

        仅op_service权限可以使用此字段做资源实例过滤条件。  目前TMS调用时只包含一个tag结构体。  * key： _sys_enterprise_project_id  * values：企业项目id列表  目前TMS调用时，key下面只包含一个value，0表示默认企业项目。  sys_tags和租户标签过滤条件（tags、tags_any、not_tags、not_tags_any）不能同时使用。  无sys_tags时按照tag接口处理，无tag过滤条件时返回全量数据。  sys_tags不能为空列表

        :param sys_tags: The sys_tags of this VaultResourceInstancesReq.
        :type sys_tags: list[:class:`huaweicloudsdkcbr.v1.SysTags`]
        """
        self._sys_tags = sys_tags

    @property
    def limit(self):
        """Gets the limit of this VaultResourceInstancesReq.

        查询记录数（action为count时无此参数）如果action为filter时，默认为1000，limit最小值为1，limit最大值为1000, 不在范围内报错。返回的结果中记录数不超过limit。

        :return: The limit of this VaultResourceInstancesReq.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this VaultResourceInstancesReq.

        查询记录数（action为count时无此参数）如果action为filter时，默认为1000，limit最小值为1，limit最大值为1000, 不在范围内报错。返回的结果中记录数不超过limit。

        :param limit: The limit of this VaultResourceInstancesReq.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this VaultResourceInstancesReq.

        索引位置（action为count时无此参数）如果action为filter时，默认为0，offset最小值为0。返回的结果中第一条记录为符合查询条件的第offset+1条记录。

        :return: The offset of this VaultResourceInstancesReq.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this VaultResourceInstancesReq.

        索引位置（action为count时无此参数）如果action为filter时，默认为0，offset最小值为0。返回的结果中第一条记录为符合查询条件的第offset+1条记录。

        :param offset: The offset of this VaultResourceInstancesReq.
        :type offset: str
        """
        self._offset = offset

    @property
    def action(self):
        """Gets the action of this VaultResourceInstancesReq.

        操作标识取值范围为：\"filter\", \"count\"。如果是filter就是分页查询，如果是count只需按照条件将总条数返回即可

        :return: The action of this VaultResourceInstancesReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this VaultResourceInstancesReq.

        操作标识取值范围为：\"filter\", \"count\"。如果是filter就是分页查询，如果是count只需按照条件将总条数返回即可

        :param action: The action of this VaultResourceInstancesReq.
        :type action: str
        """
        self._action = action

    @property
    def matches(self):
        """Gets the matches of this VaultResourceInstancesReq.

        资源本身支持的查询条件。  matches中key不允许重复。  数组长度最大值为 1，后续再扩展。

        :return: The matches of this VaultResourceInstancesReq.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this VaultResourceInstancesReq.

        资源本身支持的查询条件。  matches中key不允许重复。  数组长度最大值为 1，后续再扩展。

        :param matches: The matches of this VaultResourceInstancesReq.
        :type matches: list[:class:`huaweicloudsdkcbr.v1.Match`]
        """
        self._matches = matches

    @property
    def cloud_type(self):
        """Gets the cloud_type of this VaultResourceInstancesReq.

        云类型

        :return: The cloud_type of this VaultResourceInstancesReq.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this VaultResourceInstancesReq.

        云类型

        :param cloud_type: The cloud_type of this VaultResourceInstancesReq.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def object_type(self):
        """Gets the object_type of this VaultResourceInstancesReq.

        资源类型

        :return: The object_type of this VaultResourceInstancesReq.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this VaultResourceInstancesReq.

        资源类型

        :param object_type: The object_type of this VaultResourceInstancesReq.
        :type object_type: str
        """
        self._object_type = object_type

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
        if not isinstance(other, VaultResourceInstancesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
