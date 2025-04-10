# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListContentCompareDifferenceResponse(SdkResponse):

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
        'contents_infos': 'list[CompareJobContentDetailInfo]'
    }

    attribute_map = {
        'count': 'count',
        'target_meta_is_null': 'target_meta_is_null',
        'source_meta_is_null': 'source_meta_is_null',
        'source_target_meta_not_null': 'source_target_meta_not_null',
        'contents_infos': 'contents_infos'
    }

    def __init__(self, count=None, target_meta_is_null=None, source_meta_is_null=None, source_target_meta_not_null=None, contents_infos=None):
        r"""ListContentCompareDifferenceResponse

        The model defined in huaweicloud sdk

        :param count: 总数量。
        :type count: int
        :param target_meta_is_null: 对比不一致详情数量：只有源库存在。
        :type target_meta_is_null: int
        :param source_meta_is_null: 对比不一致详情数量：只有目标库存在。
        :type source_meta_is_null: int
        :param source_target_meta_not_null: 对比不一致详情数量：源和目标端均存在。
        :type source_target_meta_not_null: int
        :param contents_infos: 详细内容信息列表。
        :type contents_infos: list[:class:`huaweicloudsdkdrs.v3.CompareJobContentDetailInfo`]
        """
        
        super(ListContentCompareDifferenceResponse, self).__init__()

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
        r"""Gets the count of this ListContentCompareDifferenceResponse.

        总数量。

        :return: The count of this ListContentCompareDifferenceResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListContentCompareDifferenceResponse.

        总数量。

        :param count: The count of this ListContentCompareDifferenceResponse.
        :type count: int
        """
        self._count = count

    @property
    def target_meta_is_null(self):
        r"""Gets the target_meta_is_null of this ListContentCompareDifferenceResponse.

        对比不一致详情数量：只有源库存在。

        :return: The target_meta_is_null of this ListContentCompareDifferenceResponse.
        :rtype: int
        """
        return self._target_meta_is_null

    @target_meta_is_null.setter
    def target_meta_is_null(self, target_meta_is_null):
        r"""Sets the target_meta_is_null of this ListContentCompareDifferenceResponse.

        对比不一致详情数量：只有源库存在。

        :param target_meta_is_null: The target_meta_is_null of this ListContentCompareDifferenceResponse.
        :type target_meta_is_null: int
        """
        self._target_meta_is_null = target_meta_is_null

    @property
    def source_meta_is_null(self):
        r"""Gets the source_meta_is_null of this ListContentCompareDifferenceResponse.

        对比不一致详情数量：只有目标库存在。

        :return: The source_meta_is_null of this ListContentCompareDifferenceResponse.
        :rtype: int
        """
        return self._source_meta_is_null

    @source_meta_is_null.setter
    def source_meta_is_null(self, source_meta_is_null):
        r"""Sets the source_meta_is_null of this ListContentCompareDifferenceResponse.

        对比不一致详情数量：只有目标库存在。

        :param source_meta_is_null: The source_meta_is_null of this ListContentCompareDifferenceResponse.
        :type source_meta_is_null: int
        """
        self._source_meta_is_null = source_meta_is_null

    @property
    def source_target_meta_not_null(self):
        r"""Gets the source_target_meta_not_null of this ListContentCompareDifferenceResponse.

        对比不一致详情数量：源和目标端均存在。

        :return: The source_target_meta_not_null of this ListContentCompareDifferenceResponse.
        :rtype: int
        """
        return self._source_target_meta_not_null

    @source_target_meta_not_null.setter
    def source_target_meta_not_null(self, source_target_meta_not_null):
        r"""Sets the source_target_meta_not_null of this ListContentCompareDifferenceResponse.

        对比不一致详情数量：源和目标端均存在。

        :param source_target_meta_not_null: The source_target_meta_not_null of this ListContentCompareDifferenceResponse.
        :type source_target_meta_not_null: int
        """
        self._source_target_meta_not_null = source_target_meta_not_null

    @property
    def contents_infos(self):
        r"""Gets the contents_infos of this ListContentCompareDifferenceResponse.

        详细内容信息列表。

        :return: The contents_infos of this ListContentCompareDifferenceResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.CompareJobContentDetailInfo`]
        """
        return self._contents_infos

    @contents_infos.setter
    def contents_infos(self, contents_infos):
        r"""Sets the contents_infos of this ListContentCompareDifferenceResponse.

        详细内容信息列表。

        :param contents_infos: The contents_infos of this ListContentCompareDifferenceResponse.
        :type contents_infos: list[:class:`huaweicloudsdkdrs.v3.CompareJobContentDetailInfo`]
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
        if not isinstance(other, ListContentCompareDifferenceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
