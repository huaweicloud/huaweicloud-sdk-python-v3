# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResqTagResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'resource_types': 'list[str]',
        'tags': 'list[Tag]',
        'without_any_tag': 'bool',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'resource_types': 'resource_types',
        'tags': 'tags',
        'without_any_tag': 'without_any_tag',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, resource_types=None, tags=None, without_any_tag=None, offset=None, limit=None):
        """ResqTagResource

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，resource_type为region级别服务时为必选项。
        :type project_id: str
        :param resource_types: 资源类型， 此参数为可输入的值（区分大小写）。例如：ecs,scaling_group, images, disk,vpcs,security-groups, shared_bandwidth,eip, cdn等，具体请参见“附录-标签支持的资源类型”章节。
        :type resource_types: list[str]
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdktms.v1.Tag`]
        :param without_any_tag: 是否仅查询未带标签的资源。该字段为true时查询不带标签的资源。
        :type without_any_tag: bool
        :param offset: 索引位置， 从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0。
        :type offset: int
        :param limit: 查询记录数，不传默认为200，limit最多为200, 最小值为1。
        :type limit: int
        """
        
        

        self._project_id = None
        self._resource_types = None
        self._tags = None
        self._without_any_tag = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        self.resource_types = resource_types
        self.tags = tags
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        """Gets the project_id of this ResqTagResource.

        项目ID，resource_type为region级别服务时为必选项。

        :return: The project_id of this ResqTagResource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ResqTagResource.

        项目ID，resource_type为region级别服务时为必选项。

        :param project_id: The project_id of this ResqTagResource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_types(self):
        """Gets the resource_types of this ResqTagResource.

        资源类型， 此参数为可输入的值（区分大小写）。例如：ecs,scaling_group, images, disk,vpcs,security-groups, shared_bandwidth,eip, cdn等，具体请参见“附录-标签支持的资源类型”章节。

        :return: The resource_types of this ResqTagResource.
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """Sets the resource_types of this ResqTagResource.

        资源类型， 此参数为可输入的值（区分大小写）。例如：ecs,scaling_group, images, disk,vpcs,security-groups, shared_bandwidth,eip, cdn等，具体请参见“附录-标签支持的资源类型”章节。

        :param resource_types: The resource_types of this ResqTagResource.
        :type resource_types: list[str]
        """
        self._resource_types = resource_types

    @property
    def tags(self):
        """Gets the tags of this ResqTagResource.

        标签列表

        :return: The tags of this ResqTagResource.
        :rtype: list[:class:`huaweicloudsdktms.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ResqTagResource.

        标签列表

        :param tags: The tags of this ResqTagResource.
        :type tags: list[:class:`huaweicloudsdktms.v1.Tag`]
        """
        self._tags = tags

    @property
    def without_any_tag(self):
        """Gets the without_any_tag of this ResqTagResource.

        是否仅查询未带标签的资源。该字段为true时查询不带标签的资源。

        :return: The without_any_tag of this ResqTagResource.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        """Sets the without_any_tag of this ResqTagResource.

        是否仅查询未带标签的资源。该字段为true时查询不带标签的资源。

        :param without_any_tag: The without_any_tag of this ResqTagResource.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def offset(self):
        """Gets the offset of this ResqTagResource.

        索引位置， 从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0。

        :return: The offset of this ResqTagResource.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ResqTagResource.

        索引位置， 从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0。

        :param offset: The offset of this ResqTagResource.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ResqTagResource.

        查询记录数，不传默认为200，limit最多为200, 最小值为1。

        :return: The limit of this ResqTagResource.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ResqTagResource.

        查询记录数，不传默认为200，limit最多为200, 最小值为1。

        :param limit: The limit of this ResqTagResource.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ResqTagResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
