# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTargetFlavorsResponse(SdkResponse):

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
        'flavors': 'list[FlavorInfoResponse]'
    }

    attribute_map = {
        'count': 'count',
        'flavors': 'flavors'
    }

    def __init__(self, count=None, flavors=None):
        r"""ListTargetFlavorsResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释**： 规格数量。 **取值范围**： 不涉及。
        :type count: int
        :param flavors: **参数解释**： 规格详情列表。接口返回的规格列表最多为20条。 **取值范围**： 不涉及。
        :type flavors: list[:class:`huaweicloudsdkdws.v2.FlavorInfoResponse`]
        """
        
        super(ListTargetFlavorsResponse, self).__init__()

        self._count = None
        self._flavors = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if flavors is not None:
            self.flavors = flavors

    @property
    def count(self):
        r"""Gets the count of this ListTargetFlavorsResponse.

        **参数解释**： 规格数量。 **取值范围**： 不涉及。

        :return: The count of this ListTargetFlavorsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListTargetFlavorsResponse.

        **参数解释**： 规格数量。 **取值范围**： 不涉及。

        :param count: The count of this ListTargetFlavorsResponse.
        :type count: int
        """
        self._count = count

    @property
    def flavors(self):
        r"""Gets the flavors of this ListTargetFlavorsResponse.

        **参数解释**： 规格详情列表。接口返回的规格列表最多为20条。 **取值范围**： 不涉及。

        :return: The flavors of this ListTargetFlavorsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.FlavorInfoResponse`]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        r"""Sets the flavors of this ListTargetFlavorsResponse.

        **参数解释**： 规格详情列表。接口返回的规格列表最多为20条。 **取值范围**： 不涉及。

        :param flavors: The flavors of this ListTargetFlavorsResponse.
        :type flavors: list[:class:`huaweicloudsdkdws.v2.FlavorInfoResponse`]
        """
        self._flavors = flavors

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
        if not isinstance(other, ListTargetFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
