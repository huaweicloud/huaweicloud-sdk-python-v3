# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstancePatchItemsResponse(SdkResponse):

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
        'compliance_items': 'list[ComplianceItem]'
    }

    attribute_map = {
        'count': 'count',
        'compliance_items': 'compliance_items'
    }

    def __init__(self, count=None, compliance_items=None):
        r"""ShowInstancePatchItemsResponse

        The model defined in huaweicloud sdk

        :param count: 总条数
        :type count: int
        :param compliance_items: 补丁合规信息
        :type compliance_items: list[:class:`huaweicloudsdkcoc.v1.ComplianceItem`]
        """
        
        super(ShowInstancePatchItemsResponse, self).__init__()

        self._count = None
        self._compliance_items = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if compliance_items is not None:
            self.compliance_items = compliance_items

    @property
    def count(self):
        r"""Gets the count of this ShowInstancePatchItemsResponse.

        总条数

        :return: The count of this ShowInstancePatchItemsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowInstancePatchItemsResponse.

        总条数

        :param count: The count of this ShowInstancePatchItemsResponse.
        :type count: int
        """
        self._count = count

    @property
    def compliance_items(self):
        r"""Gets the compliance_items of this ShowInstancePatchItemsResponse.

        补丁合规信息

        :return: The compliance_items of this ShowInstancePatchItemsResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ComplianceItem`]
        """
        return self._compliance_items

    @compliance_items.setter
    def compliance_items(self, compliance_items):
        r"""Sets the compliance_items of this ShowInstancePatchItemsResponse.

        补丁合规信息

        :param compliance_items: The compliance_items of this ShowInstancePatchItemsResponse.
        :type compliance_items: list[:class:`huaweicloudsdkcoc.v1.ComplianceItem`]
        """
        self._compliance_items = compliance_items

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
        if not isinstance(other, ShowInstancePatchItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
