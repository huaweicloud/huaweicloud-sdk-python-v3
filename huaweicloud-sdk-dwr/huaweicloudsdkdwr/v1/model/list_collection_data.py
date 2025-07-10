# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectionData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collections': 'list[str]',
        'details': 'list[ListCollectionDetails]'
    }

    attribute_map = {
        'collections': 'collections',
        'details': 'details'
    }

    def __init__(self, collections=None, details=None):
        r"""ListCollectionData

        The model defined in huaweicloud sdk

        :param collections: **参数解释：** 知识仓实例下所有collection名称列表。 **约束限制：** 不涉及。
        :type collections: list[str]
        :param details: **参数解释：** 知识仓实例下所有collection详细信息列表。 **约束限制：** 在指定detail字段为true时生效。
        :type details: list[:class:`huaweicloudsdkdwr.v1.ListCollectionDetails`]
        """
        
        

        self._collections = None
        self._details = None
        self.discriminator = None

        self.collections = collections
        if details is not None:
            self.details = details

    @property
    def collections(self):
        r"""Gets the collections of this ListCollectionData.

        **参数解释：** 知识仓实例下所有collection名称列表。 **约束限制：** 不涉及。

        :return: The collections of this ListCollectionData.
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        r"""Sets the collections of this ListCollectionData.

        **参数解释：** 知识仓实例下所有collection名称列表。 **约束限制：** 不涉及。

        :param collections: The collections of this ListCollectionData.
        :type collections: list[str]
        """
        self._collections = collections

    @property
    def details(self):
        r"""Gets the details of this ListCollectionData.

        **参数解释：** 知识仓实例下所有collection详细信息列表。 **约束限制：** 在指定detail字段为true时生效。

        :return: The details of this ListCollectionData.
        :rtype: list[:class:`huaweicloudsdkdwr.v1.ListCollectionDetails`]
        """
        return self._details

    @details.setter
    def details(self, details):
        r"""Sets the details of this ListCollectionData.

        **参数解释：** 知识仓实例下所有collection详细信息列表。 **约束限制：** 在指定detail字段为true时生效。

        :param details: The details of this ListCollectionData.
        :type details: list[:class:`huaweicloudsdkdwr.v1.ListCollectionDetails`]
        """
        self._details = details

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
        if not isinstance(other, ListCollectionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
