# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagResourceInstancesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'str',
        'limit': 'str',
        'action': 'str',
        'matches': 'list[Match]',
        'not_tags': 'list[Tags]',
        'tags': 'list[Tags]',
        'tags_any': 'list[Tags]',
        'not_tags_any': 'list[Tags]',
        'sys_tags': 'list[Tags]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'action': 'action',
        'matches': 'matches',
        'not_tags': 'not_tags',
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags_any': 'not_tags_any',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, offset=None, limit=None, action=None, matches=None, not_tags=None, tags=None, tags_any=None, not_tags_any=None, sys_tags=None):
        """ListTagResourceInstancesRequestBody

        The model defined in huaweicloud sdk

        :param offset: 索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数（action为count时无此参数）如果action为filter默认为0,必须为数字，不能为负数
        :type offset: str
        :param limit: 查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1
        :type limit: str
        :param action: 操作标识（仅限于filter，count）：filter（过滤），count(查询总条数) 如果是filter就是分页查询，如果是count只需按照条件将总条数返回即可。禁止返回其他字段。
        :type action: str
        :param matches: 搜索字段,key为要匹配的字段，如resource_name等。value为匹配的值。此字段为固定字典值。 根据不同的字段确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配。resource_id为精确匹配。第一期只做resource_name，后续在扩展。
        :type matches: list[:class:`huaweicloudsdkdc.v3.Match`]
        :param not_tags: 不包含标签，最多包含10个key，每个key下面的value最多10个, 结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type not_tags: list[:class:`huaweicloudsdkdc.v3.Tags`]
        :param tags: 包含标签，最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tags`]
        :param tags_any: 包含任意标签，最多包含10个key，每个key下面的value最多10个,结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type tags_any: list[:class:`huaweicloudsdkdc.v3.Tags`]
        :param not_tags_any: 不包含任意标签，最多包含10个key，每个key下面的value最多10个,结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。
        :type not_tags_any: list[:class:`huaweicloudsdkdc.v3.Tags`]
        :param sys_tags: 仅op_service权限可以使用此字段做资源实例过滤条件。目前TMS调用时只包含一个tag结构体。key：_sys_enterprise_project_id，value：企业项目id列表。目前TMS调用时，key下面只包含一个value。0表示默认企业项目。sys_tags和租户标签过滤条件（without_any_tag 、tags、tags_any、not_tags、not_tags_any）不能同时使用。
        :type sys_tags: list[:class:`huaweicloudsdkdc.v3.Tags`]
        """
        
        

        self._offset = None
        self._limit = None
        self._action = None
        self._matches = None
        self._not_tags = None
        self._tags = None
        self._tags_any = None
        self._not_tags_any = None
        self._sys_tags = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.action = action
        if matches is not None:
            self.matches = matches
        if not_tags is not None:
            self.not_tags = not_tags
        if tags is not None:
            self.tags = tags
        if tags_any is not None:
            self.tags_any = tags_any
        if not_tags_any is not None:
            self.not_tags_any = not_tags_any
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def offset(self):
        """Gets the offset of this ListTagResourceInstancesRequestBody.

        索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数（action为count时无此参数）如果action为filter默认为0,必须为数字，不能为负数

        :return: The offset of this ListTagResourceInstancesRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTagResourceInstancesRequestBody.

        索引位置， 从offset指定的下一条数据开始查询。 查询第一页数据时，不需要传入此参数，查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数（action为count时无此参数）如果action为filter默认为0,必须为数字，不能为负数

        :param offset: The offset of this ListTagResourceInstancesRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTagResourceInstancesRequestBody.

        查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1

        :return: The limit of this ListTagResourceInstancesRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTagResourceInstancesRequestBody.

        查询记录数（action为count时无此参数）如果action为filter默认为1000，limit最多为1000,不能为负数，最小值为1

        :param limit: The limit of this ListTagResourceInstancesRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def action(self):
        """Gets the action of this ListTagResourceInstancesRequestBody.

        操作标识（仅限于filter，count）：filter（过滤），count(查询总条数) 如果是filter就是分页查询，如果是count只需按照条件将总条数返回即可。禁止返回其他字段。

        :return: The action of this ListTagResourceInstancesRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListTagResourceInstancesRequestBody.

        操作标识（仅限于filter，count）：filter（过滤），count(查询总条数) 如果是filter就是分页查询，如果是count只需按照条件将总条数返回即可。禁止返回其他字段。

        :param action: The action of this ListTagResourceInstancesRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def matches(self):
        """Gets the matches of this ListTagResourceInstancesRequestBody.

        搜索字段,key为要匹配的字段，如resource_name等。value为匹配的值。此字段为固定字典值。 根据不同的字段确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配。resource_id为精确匹配。第一期只做resource_name，后续在扩展。

        :return: The matches of this ListTagResourceInstancesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListTagResourceInstancesRequestBody.

        搜索字段,key为要匹配的字段，如resource_name等。value为匹配的值。此字段为固定字典值。 根据不同的字段确认是否需要模糊匹配，如resource_name默认为模糊搜索（不区分大小写），如果value为空字符串精确匹配。resource_id为精确匹配。第一期只做resource_name，后续在扩展。

        :param matches: The matches of this ListTagResourceInstancesRequestBody.
        :type matches: list[:class:`huaweicloudsdkdc.v3.Match`]
        """
        self._matches = matches

    @property
    def not_tags(self):
        """Gets the not_tags of this ListTagResourceInstancesRequestBody.

        不包含标签，最多包含10个key，每个key下面的value最多10个, 结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The not_tags of this ListTagResourceInstancesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tags`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ListTagResourceInstancesRequestBody.

        不包含标签，最多包含10个key，每个key下面的value最多10个, 结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回不包含标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param not_tags: The not_tags of this ListTagResourceInstancesRequestBody.
        :type not_tags: list[:class:`huaweicloudsdkdc.v3.Tags`]
        """
        self._not_tags = not_tags

    @property
    def tags(self):
        """Gets the tags of this ListTagResourceInstancesRequestBody.

        包含标签，最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :return: The tags of this ListTagResourceInstancesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListTagResourceInstancesRequestBody.

        包含标签，最多包含10个key，每个key下面的value最多10个，结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回包含所有标签的资源列表，key之间是与的关系，key-value结构中value是或的关系。无tag过滤条件时返回全量数据。

        :param tags: The tags of this ListTagResourceInstancesRequestBody.
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tags`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this ListTagResourceInstancesRequestBody.

        包含任意标签，最多包含10个key，每个key下面的value最多10个,结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The tags_any of this ListTagResourceInstancesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tags`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this ListTagResourceInstancesRequestBody.

        包含任意标签，最多包含10个key，每个key下面的value最多10个,结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param tags_any: The tags_any of this ListTagResourceInstancesRequestBody.
        :type tags_any: list[:class:`huaweicloudsdkdc.v3.Tags`]
        """
        self._tags_any = tags_any

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this ListTagResourceInstancesRequestBody.

        不包含任意标签，最多包含10个key，每个key下面的value最多10个,结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :return: The not_tags_any of this ListTagResourceInstancesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tags`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this ListTagResourceInstancesRequestBody.

        不包含任意标签，最多包含10个key，每个key下面的value最多10个,结构体不能缺失，key不能为空或者空字符串。Key不能重复，同一个key中values不能重复。返回不包含标签的资源列表，key之间是或的关系，key-value结构中value是或的关系。无过滤条件时返回全量数据。

        :param not_tags_any: The not_tags_any of this ListTagResourceInstancesRequestBody.
        :type not_tags_any: list[:class:`huaweicloudsdkdc.v3.Tags`]
        """
        self._not_tags_any = not_tags_any

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ListTagResourceInstancesRequestBody.

        仅op_service权限可以使用此字段做资源实例过滤条件。目前TMS调用时只包含一个tag结构体。key：_sys_enterprise_project_id，value：企业项目id列表。目前TMS调用时，key下面只包含一个value。0表示默认企业项目。sys_tags和租户标签过滤条件（without_any_tag 、tags、tags_any、not_tags、not_tags_any）不能同时使用。

        :return: The sys_tags of this ListTagResourceInstancesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ListTagResourceInstancesRequestBody.

        仅op_service权限可以使用此字段做资源实例过滤条件。目前TMS调用时只包含一个tag结构体。key：_sys_enterprise_project_id，value：企业项目id列表。目前TMS调用时，key下面只包含一个value。0表示默认企业项目。sys_tags和租户标签过滤条件（without_any_tag 、tags、tags_any、not_tags、not_tags_any）不能同时使用。

        :param sys_tags: The sys_tags of this ListTagResourceInstancesRequestBody.
        :type sys_tags: list[:class:`huaweicloudsdkdc.v3.Tags`]
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, ListTagResourceInstancesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
