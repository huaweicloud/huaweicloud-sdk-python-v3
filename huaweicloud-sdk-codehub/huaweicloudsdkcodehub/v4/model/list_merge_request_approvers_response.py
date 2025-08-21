# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMergeRequestApproversResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'required_approvers_list': 'list[UserBasicDto]',
        'optional_approvers_list': 'list[UserBasicDto]',
        'x_total': 'str'
    }

    attribute_map = {
        'required_approvers_list': 'required_approvers_list',
        'optional_approvers_list': 'optional_approvers_list',
        'x_total': 'X-Total'
    }

    def __init__(self, required_approvers_list=None, optional_approvers_list=None, x_total=None):
        r"""ListMergeRequestApproversResponse

        The model defined in huaweicloud sdk

        :param required_approvers_list: **参数解释：** 必选审核人列表。 **取值范围：** 不涉及。
        :type required_approvers_list: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        :param optional_approvers_list: **参数解释：** 可选审核人列表。 **取值范围：** 不涉及。
        :type optional_approvers_list: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        :param x_total: 
        :type x_total: str
        """
        
        super(ListMergeRequestApproversResponse, self).__init__()

        self._required_approvers_list = None
        self._optional_approvers_list = None
        self._x_total = None
        self.discriminator = None

        if required_approvers_list is not None:
            self.required_approvers_list = required_approvers_list
        if optional_approvers_list is not None:
            self.optional_approvers_list = optional_approvers_list
        if x_total is not None:
            self.x_total = x_total

    @property
    def required_approvers_list(self):
        r"""Gets the required_approvers_list of this ListMergeRequestApproversResponse.

        **参数解释：** 必选审核人列表。 **取值范围：** 不涉及。

        :return: The required_approvers_list of this ListMergeRequestApproversResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        return self._required_approvers_list

    @required_approvers_list.setter
    def required_approvers_list(self, required_approvers_list):
        r"""Sets the required_approvers_list of this ListMergeRequestApproversResponse.

        **参数解释：** 必选审核人列表。 **取值范围：** 不涉及。

        :param required_approvers_list: The required_approvers_list of this ListMergeRequestApproversResponse.
        :type required_approvers_list: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        self._required_approvers_list = required_approvers_list

    @property
    def optional_approvers_list(self):
        r"""Gets the optional_approvers_list of this ListMergeRequestApproversResponse.

        **参数解释：** 可选审核人列表。 **取值范围：** 不涉及。

        :return: The optional_approvers_list of this ListMergeRequestApproversResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        return self._optional_approvers_list

    @optional_approvers_list.setter
    def optional_approvers_list(self, optional_approvers_list):
        r"""Sets the optional_approvers_list of this ListMergeRequestApproversResponse.

        **参数解释：** 可选审核人列表。 **取值范围：** 不涉及。

        :param optional_approvers_list: The optional_approvers_list of this ListMergeRequestApproversResponse.
        :type optional_approvers_list: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        self._optional_approvers_list = optional_approvers_list

    @property
    def x_total(self):
        r"""Gets the x_total of this ListMergeRequestApproversResponse.

        :return: The x_total of this ListMergeRequestApproversResponse.
        :rtype: str
        """
        return self._x_total

    @x_total.setter
    def x_total(self, x_total):
        r"""Sets the x_total of this ListMergeRequestApproversResponse.

        :param x_total: The x_total of this ListMergeRequestApproversResponse.
        :type x_total: str
        """
        self._x_total = x_total

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
        if not isinstance(other, ListMergeRequestApproversResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
