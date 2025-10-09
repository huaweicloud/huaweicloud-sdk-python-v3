# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'access_policy_list': 'list[AccessPolicyResp]'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'access_policy_list': 'accessPolicyList'
    }

    def __init__(self, kind=None, api_version=None, access_policy_list=None):
        r"""ListAccessPolicyResponse

        The model defined in huaweicloud sdk

        :param kind: **参数解释：** API类型。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** List
        :type kind: str
        :param api_version: **参数解释：** API版本。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** v3
        :type api_version: str
        :param access_policy_list: 
        :type access_policy_list: list[:class:`huaweicloudsdkcce.v3.AccessPolicyResp`]
        """
        
        super(ListAccessPolicyResponse, self).__init__()

        self._kind = None
        self._api_version = None
        self._access_policy_list = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if access_policy_list is not None:
            self.access_policy_list = access_policy_list

    @property
    def kind(self):
        r"""Gets the kind of this ListAccessPolicyResponse.

        **参数解释：** API类型。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** List

        :return: The kind of this ListAccessPolicyResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListAccessPolicyResponse.

        **参数解释：** API类型。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** List

        :param kind: The kind of this ListAccessPolicyResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this ListAccessPolicyResponse.

        **参数解释：** API版本。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** v3

        :return: The api_version of this ListAccessPolicyResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ListAccessPolicyResponse.

        **参数解释：** API版本。 **约束限制：** 该值不可修改。 **取值范围：** 不涉及 **默认取值：** v3

        :param api_version: The api_version of this ListAccessPolicyResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def access_policy_list(self):
        r"""Gets the access_policy_list of this ListAccessPolicyResponse.

        :return: The access_policy_list of this ListAccessPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.AccessPolicyResp`]
        """
        return self._access_policy_list

    @access_policy_list.setter
    def access_policy_list(self, access_policy_list):
        r"""Sets the access_policy_list of this ListAccessPolicyResponse.

        :param access_policy_list: The access_policy_list of this ListAccessPolicyResponse.
        :type access_policy_list: list[:class:`huaweicloudsdkcce.v3.AccessPolicyResp`]
        """
        self._access_policy_list = access_policy_list

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
        if not isinstance(other, ListAccessPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
