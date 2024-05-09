# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentDiffDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'target_meta_is_null': 'int',
        'source_meta_is_null': 'int',
        'source_target_meta_not_null': 'int',
        'contents_infos': 'list[ContentDiffDetailVO]'
    }

    attribute_map = {
        'count': 'count',
        'target_meta_is_null': 'target_meta_is_null',
        'source_meta_is_null': 'source_meta_is_null',
        'source_target_meta_not_null': 'source_target_meta_not_null',
        'contents_infos': 'contents_infos'
    }

    def __init__(self, count=None, target_meta_is_null=None, source_meta_is_null=None, source_target_meta_not_null=None, contents_infos=None):
        """ContentDiffDetailInfo

        The model defined in huaweicloud sdk

        :param count: 数量。
        :type count: int
        :param target_meta_is_null: 对比不一致详情：只有源库存在。
        :type target_meta_is_null: int
        :param source_meta_is_null: 对比不一致详情：只有目标库存在。
        :type source_meta_is_null: int
        :param source_target_meta_not_null: 对比不一致详情：源和目标端均存在。
        :type source_target_meta_not_null: int
        :param contents_infos: 信息列表。
        :type contents_infos: list[:class:`huaweicloudsdkdrs.v5.ContentDiffDetailVO`]
        """
        
        

        self._count = None
        self._target_meta_is_null = None
        self._source_meta_is_null = None
        self._source_target_meta_not_null = None
        self._contents_infos = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if target_meta_is_null is not None:
            self.target_meta_is_null = target_meta_is_null
        if source_meta_is_null is not None:
            self.source_meta_is_null = source_meta_is_null
        if source_target_meta_not_null is not None:
            self.source_target_meta_not_null = source_target_meta_not_null
        if contents_infos is not None:
            self.contents_infos = contents_infos

    @property
    def count(self):
        """Gets the count of this ContentDiffDetailInfo.

        数量。

        :return: The count of this ContentDiffDetailInfo.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ContentDiffDetailInfo.

        数量。

        :param count: The count of this ContentDiffDetailInfo.
        :type count: int
        """
        self._count = count

    @property
    def target_meta_is_null(self):
        """Gets the target_meta_is_null of this ContentDiffDetailInfo.

        对比不一致详情：只有源库存在。

        :return: The target_meta_is_null of this ContentDiffDetailInfo.
        :rtype: int
        """
        return self._target_meta_is_null

    @target_meta_is_null.setter
    def target_meta_is_null(self, target_meta_is_null):
        """Sets the target_meta_is_null of this ContentDiffDetailInfo.

        对比不一致详情：只有源库存在。

        :param target_meta_is_null: The target_meta_is_null of this ContentDiffDetailInfo.
        :type target_meta_is_null: int
        """
        self._target_meta_is_null = target_meta_is_null

    @property
    def source_meta_is_null(self):
        """Gets the source_meta_is_null of this ContentDiffDetailInfo.

        对比不一致详情：只有目标库存在。

        :return: The source_meta_is_null of this ContentDiffDetailInfo.
        :rtype: int
        """
        return self._source_meta_is_null

    @source_meta_is_null.setter
    def source_meta_is_null(self, source_meta_is_null):
        """Sets the source_meta_is_null of this ContentDiffDetailInfo.

        对比不一致详情：只有目标库存在。

        :param source_meta_is_null: The source_meta_is_null of this ContentDiffDetailInfo.
        :type source_meta_is_null: int
        """
        self._source_meta_is_null = source_meta_is_null

    @property
    def source_target_meta_not_null(self):
        """Gets the source_target_meta_not_null of this ContentDiffDetailInfo.

        对比不一致详情：源和目标端均存在。

        :return: The source_target_meta_not_null of this ContentDiffDetailInfo.
        :rtype: int
        """
        return self._source_target_meta_not_null

    @source_target_meta_not_null.setter
    def source_target_meta_not_null(self, source_target_meta_not_null):
        """Sets the source_target_meta_not_null of this ContentDiffDetailInfo.

        对比不一致详情：源和目标端均存在。

        :param source_target_meta_not_null: The source_target_meta_not_null of this ContentDiffDetailInfo.
        :type source_target_meta_not_null: int
        """
        self._source_target_meta_not_null = source_target_meta_not_null

    @property
    def contents_infos(self):
        """Gets the contents_infos of this ContentDiffDetailInfo.

        信息列表。

        :return: The contents_infos of this ContentDiffDetailInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ContentDiffDetailVO`]
        """
        return self._contents_infos

    @contents_infos.setter
    def contents_infos(self, contents_infos):
        """Sets the contents_infos of this ContentDiffDetailInfo.

        信息列表。

        :param contents_infos: The contents_infos of this ContentDiffDetailInfo.
        :type contents_infos: list[:class:`huaweicloudsdkdrs.v5.ContentDiffDetailVO`]
        """
        self._contents_infos = contents_infos

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
        if not isinstance(other, ContentDiffDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
