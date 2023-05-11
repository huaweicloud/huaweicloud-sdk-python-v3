# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResqEpResouce:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'projects': 'list[str]',
        'resource_types': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'matches': 'list[Match]'
    }

    attribute_map = {
        'projects': 'projects',
        'resource_types': 'resource_types',
        'offset': 'offset',
        'limit': 'limit',
        'matches': 'matches'
    }

    def __init__(self, projects=None, resource_types=None, offset=None, limit=None, matches=None):
        """ResqEpResouce

        The model defined in huaweicloud sdk

        :param projects: 项目ID列表。resource_types中包含region级别服务时为必选项。
        :type projects: list[str]
        :param resource_types: 资源类型列表， 此参数为可输入的值（区分大小写）。例如：ecs,scaling_group, images, disk, vpcs,security-groups, shared_bandwidth, eip, cdn等。
        :type resource_types: list[str]
        :param offset: 索引位置， 从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0。
        :type offset: int
        :param limit: 查询记录数，不传默认为1000，limit最多为1000, 最小值为1。
        :type limit: int
        :param matches: 搜索字段，key为要匹配的字段，固定为resource_name，value为匹配的值，不传则表示无匹配条件。
        :type matches: list[:class:`huaweicloudsdkeps.v1.Match`]
        """
        
        

        self._projects = None
        self._resource_types = None
        self._offset = None
        self._limit = None
        self._matches = None
        self.discriminator = None

        if projects is not None:
            self.projects = projects
        self.resource_types = resource_types
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if matches is not None:
            self.matches = matches

    @property
    def projects(self):
        """Gets the projects of this ResqEpResouce.

        项目ID列表。resource_types中包含region级别服务时为必选项。

        :return: The projects of this ResqEpResouce.
        :rtype: list[str]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this ResqEpResouce.

        项目ID列表。resource_types中包含region级别服务时为必选项。

        :param projects: The projects of this ResqEpResouce.
        :type projects: list[str]
        """
        self._projects = projects

    @property
    def resource_types(self):
        """Gets the resource_types of this ResqEpResouce.

        资源类型列表， 此参数为可输入的值（区分大小写）。例如：ecs,scaling_group, images, disk, vpcs,security-groups, shared_bandwidth, eip, cdn等。

        :return: The resource_types of this ResqEpResouce.
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """Sets the resource_types of this ResqEpResouce.

        资源类型列表， 此参数为可输入的值（区分大小写）。例如：ecs,scaling_group, images, disk, vpcs,security-groups, shared_bandwidth, eip, cdn等。

        :param resource_types: The resource_types of this ResqEpResouce.
        :type resource_types: list[str]
        """
        self._resource_types = resource_types

    @property
    def offset(self):
        """Gets the offset of this ResqEpResouce.

        索引位置， 从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0。

        :return: The offset of this ResqEpResouce.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ResqEpResouce.

        索引位置， 从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0。

        :param offset: The offset of this ResqEpResouce.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ResqEpResouce.

        查询记录数，不传默认为1000，limit最多为1000, 最小值为1。

        :return: The limit of this ResqEpResouce.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ResqEpResouce.

        查询记录数，不传默认为1000，limit最多为1000, 最小值为1。

        :param limit: The limit of this ResqEpResouce.
        :type limit: int
        """
        self._limit = limit

    @property
    def matches(self):
        """Gets the matches of this ResqEpResouce.

        搜索字段，key为要匹配的字段，固定为resource_name，value为匹配的值，不传则表示无匹配条件。

        :return: The matches of this ResqEpResouce.
        :rtype: list[:class:`huaweicloudsdkeps.v1.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ResqEpResouce.

        搜索字段，key为要匹配的字段，固定为resource_name，value为匹配的值，不传则表示无匹配条件。

        :param matches: The matches of this ResqEpResouce.
        :type matches: list[:class:`huaweicloudsdkeps.v1.Match`]
        """
        self._matches = matches

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
        if not isinstance(other, ResqEpResouce):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
