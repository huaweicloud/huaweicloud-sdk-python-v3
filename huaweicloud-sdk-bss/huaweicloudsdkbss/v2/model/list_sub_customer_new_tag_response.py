# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubCustomerNewTagResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_customer_tags': 'list[NewCustomerTagItem]'
    }

    attribute_map = {
        'new_customer_tags': 'new_customer_tags'
    }

    def __init__(self, new_customer_tags=None):
        r"""ListSubCustomerNewTagResponse

        The model defined in huaweicloud sdk

        :param new_customer_tags: 新客标签信息列表。只有成功的时候才返回。 此列表不包含非子客户的数据。批量查询客户新客标签时，若入参携带了非子客户，会被过滤。 具体请参见表1 NewCustomerTagItem。
        :type new_customer_tags: list[:class:`huaweicloudsdkbss.v2.NewCustomerTagItem`]
        """
        
        super(ListSubCustomerNewTagResponse, self).__init__()

        self._new_customer_tags = None
        self.discriminator = None

        if new_customer_tags is not None:
            self.new_customer_tags = new_customer_tags

    @property
    def new_customer_tags(self):
        r"""Gets the new_customer_tags of this ListSubCustomerNewTagResponse.

        新客标签信息列表。只有成功的时候才返回。 此列表不包含非子客户的数据。批量查询客户新客标签时，若入参携带了非子客户，会被过滤。 具体请参见表1 NewCustomerTagItem。

        :return: The new_customer_tags of this ListSubCustomerNewTagResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.NewCustomerTagItem`]
        """
        return self._new_customer_tags

    @new_customer_tags.setter
    def new_customer_tags(self, new_customer_tags):
        r"""Sets the new_customer_tags of this ListSubCustomerNewTagResponse.

        新客标签信息列表。只有成功的时候才返回。 此列表不包含非子客户的数据。批量查询客户新客标签时，若入参携带了非子客户，会被过滤。 具体请参见表1 NewCustomerTagItem。

        :param new_customer_tags: The new_customer_tags of this ListSubCustomerNewTagResponse.
        :type new_customer_tags: list[:class:`huaweicloudsdkbss.v2.NewCustomerTagItem`]
        """
        self._new_customer_tags = new_customer_tags

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
        if not isinstance(other, ListSubCustomerNewTagResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
