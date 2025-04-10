# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbCacheMappingsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'source_instance_id': 'str',
        'source_instance_name': 'str',
        'target_instance_id': 'str',
        'target_instance_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'source_instance_id': 'source_instance_id',
        'source_instance_name': 'source_instance_name',
        'target_instance_id': 'target_instance_id',
        'target_instance_name': 'target_instance_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, id=None, name=None, source_instance_id=None, source_instance_name=None, target_instance_id=None, target_instance_name=None, offset=None, limit=None):
        r"""ListDbCacheMappingsRequest

        The model defined in huaweicloud sdk

        :param id: 映射ID，可以调用“查询内存加速映射列表和详情”接口获取。
        :type id: str
        :param name: 映射名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。
        :type name: str
        :param source_instance_id: 源实例ID。
        :type source_instance_id: str
        :param source_instance_name: 源实例名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。
        :type source_instance_name: str
        :param target_instance_id: 目标实例ID。
        :type target_instance_id: str
        :param target_instance_name: 目标实例名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。
        :type target_instance_name: str
        :param offset: 索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询个数上限值。取值范围：1~100。不传该参数时，默认查询前100条信息。
        :type limit: int
        """
        
        

        self._id = None
        self._name = None
        self._source_instance_id = None
        self._source_instance_name = None
        self._target_instance_id = None
        self._target_instance_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if source_instance_id is not None:
            self.source_instance_id = source_instance_id
        if source_instance_name is not None:
            self.source_instance_name = source_instance_name
        if target_instance_id is not None:
            self.target_instance_id = target_instance_id
        if target_instance_name is not None:
            self.target_instance_name = target_instance_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListDbCacheMappingsRequest.

        映射ID，可以调用“查询内存加速映射列表和详情”接口获取。

        :return: The id of this ListDbCacheMappingsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListDbCacheMappingsRequest.

        映射ID，可以调用“查询内存加速映射列表和详情”接口获取。

        :param id: The id of this ListDbCacheMappingsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListDbCacheMappingsRequest.

        映射名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :return: The name of this ListDbCacheMappingsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListDbCacheMappingsRequest.

        映射名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :param name: The name of this ListDbCacheMappingsRequest.
        :type name: str
        """
        self._name = name

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this ListDbCacheMappingsRequest.

        源实例ID。

        :return: The source_instance_id of this ListDbCacheMappingsRequest.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this ListDbCacheMappingsRequest.

        源实例ID。

        :param source_instance_id: The source_instance_id of this ListDbCacheMappingsRequest.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def source_instance_name(self):
        r"""Gets the source_instance_name of this ListDbCacheMappingsRequest.

        源实例名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :return: The source_instance_name of this ListDbCacheMappingsRequest.
        :rtype: str
        """
        return self._source_instance_name

    @source_instance_name.setter
    def source_instance_name(self, source_instance_name):
        r"""Sets the source_instance_name of this ListDbCacheMappingsRequest.

        源实例名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :param source_instance_name: The source_instance_name of this ListDbCacheMappingsRequest.
        :type source_instance_name: str
        """
        self._source_instance_name = source_instance_name

    @property
    def target_instance_id(self):
        r"""Gets the target_instance_id of this ListDbCacheMappingsRequest.

        目标实例ID。

        :return: The target_instance_id of this ListDbCacheMappingsRequest.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        r"""Sets the target_instance_id of this ListDbCacheMappingsRequest.

        目标实例ID。

        :param target_instance_id: The target_instance_id of this ListDbCacheMappingsRequest.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def target_instance_name(self):
        r"""Gets the target_instance_name of this ListDbCacheMappingsRequest.

        目标实例名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :return: The target_instance_name of this ListDbCacheMappingsRequest.
        :rtype: str
        """
        return self._target_instance_name

    @target_instance_name.setter
    def target_instance_name(self, target_instance_name):
        r"""Sets the target_instance_name of this ListDbCacheMappingsRequest.

        目标实例名称。名称以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的名称精确匹配查询。

        :param target_instance_name: The target_instance_name of this ListDbCacheMappingsRequest.
        :type target_instance_name: str
        """
        self._target_instance_name = target_instance_name

    @property
    def offset(self):
        r"""Gets the offset of this ListDbCacheMappingsRequest.

        索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。

        :return: The offset of this ListDbCacheMappingsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDbCacheMappingsRequest.

        索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。

        :param offset: The offset of this ListDbCacheMappingsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDbCacheMappingsRequest.

        查询个数上限值。取值范围：1~100。不传该参数时，默认查询前100条信息。

        :return: The limit of this ListDbCacheMappingsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDbCacheMappingsRequest.

        查询个数上限值。取值范围：1~100。不传该参数时，默认查询前100条信息。

        :param limit: The limit of this ListDbCacheMappingsRequest.
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
        if not isinstance(other, ListDbCacheMappingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
