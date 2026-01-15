# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportPolicyGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'error_detail': 'str',
        'encoded_authorization_message': 'str',
        'policy_group_name_list': 'list[PolicyGroupNameInfo]',
        'failed_policy_group_name_list': 'list[PolicyGroupNameInfo]'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'error_detail': 'error_detail',
        'encoded_authorization_message': 'encoded_authorization_message',
        'policy_group_name_list': 'policy_group_name_list',
        'failed_policy_group_name_list': 'failed_policy_group_name_list'
    }

    def __init__(self, error_code=None, error_msg=None, error_detail=None, encoded_authorization_message=None, policy_group_name_list=None, failed_policy_group_name_list=None):
        r"""ImportPolicyGroupsResponse

        The model defined in huaweicloud sdk

        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误描述。
        :type error_msg: str
        :param error_detail: 错误详情。
        :type error_detail: str
        :param encoded_authorization_message: 加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。
        :type encoded_authorization_message: str
        :param policy_group_name_list: 导入策略组所有名字列表。
        :type policy_group_name_list: list[:class:`huaweicloudsdkworkspace.v2.PolicyGroupNameInfo`]
        :param failed_policy_group_name_list: 导入策略组失败名字列表。
        :type failed_policy_group_name_list: list[:class:`huaweicloudsdkworkspace.v2.PolicyGroupNameInfo`]
        """
        
        super().__init__()

        self._error_code = None
        self._error_msg = None
        self._error_detail = None
        self._encoded_authorization_message = None
        self._policy_group_name_list = None
        self._failed_policy_group_name_list = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if error_detail is not None:
            self.error_detail = error_detail
        if encoded_authorization_message is not None:
            self.encoded_authorization_message = encoded_authorization_message
        if policy_group_name_list is not None:
            self.policy_group_name_list = policy_group_name_list
        if failed_policy_group_name_list is not None:
            self.failed_policy_group_name_list = failed_policy_group_name_list

    @property
    def error_code(self):
        r"""Gets the error_code of this ImportPolicyGroupsResponse.

        错误码。

        :return: The error_code of this ImportPolicyGroupsResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ImportPolicyGroupsResponse.

        错误码。

        :param error_code: The error_code of this ImportPolicyGroupsResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ImportPolicyGroupsResponse.

        错误描述。

        :return: The error_msg of this ImportPolicyGroupsResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ImportPolicyGroupsResponse.

        错误描述。

        :param error_msg: The error_msg of this ImportPolicyGroupsResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def error_detail(self):
        r"""Gets the error_detail of this ImportPolicyGroupsResponse.

        错误详情。

        :return: The error_detail of this ImportPolicyGroupsResponse.
        :rtype: str
        """
        return self._error_detail

    @error_detail.setter
    def error_detail(self, error_detail):
        r"""Sets the error_detail of this ImportPolicyGroupsResponse.

        错误详情。

        :param error_detail: The error_detail of this ImportPolicyGroupsResponse.
        :type error_detail: str
        """
        self._error_detail = error_detail

    @property
    def encoded_authorization_message(self):
        r"""Gets the encoded_authorization_message of this ImportPolicyGroupsResponse.

        加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。

        :return: The encoded_authorization_message of this ImportPolicyGroupsResponse.
        :rtype: str
        """
        return self._encoded_authorization_message

    @encoded_authorization_message.setter
    def encoded_authorization_message(self, encoded_authorization_message):
        r"""Sets the encoded_authorization_message of this ImportPolicyGroupsResponse.

        加密后的详细拒绝原因，用户可以自行调用STS服务的decode-authorization-message接口进行解密。

        :param encoded_authorization_message: The encoded_authorization_message of this ImportPolicyGroupsResponse.
        :type encoded_authorization_message: str
        """
        self._encoded_authorization_message = encoded_authorization_message

    @property
    def policy_group_name_list(self):
        r"""Gets the policy_group_name_list of this ImportPolicyGroupsResponse.

        导入策略组所有名字列表。

        :return: The policy_group_name_list of this ImportPolicyGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.PolicyGroupNameInfo`]
        """
        return self._policy_group_name_list

    @policy_group_name_list.setter
    def policy_group_name_list(self, policy_group_name_list):
        r"""Sets the policy_group_name_list of this ImportPolicyGroupsResponse.

        导入策略组所有名字列表。

        :param policy_group_name_list: The policy_group_name_list of this ImportPolicyGroupsResponse.
        :type policy_group_name_list: list[:class:`huaweicloudsdkworkspace.v2.PolicyGroupNameInfo`]
        """
        self._policy_group_name_list = policy_group_name_list

    @property
    def failed_policy_group_name_list(self):
        r"""Gets the failed_policy_group_name_list of this ImportPolicyGroupsResponse.

        导入策略组失败名字列表。

        :return: The failed_policy_group_name_list of this ImportPolicyGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.PolicyGroupNameInfo`]
        """
        return self._failed_policy_group_name_list

    @failed_policy_group_name_list.setter
    def failed_policy_group_name_list(self, failed_policy_group_name_list):
        r"""Sets the failed_policy_group_name_list of this ImportPolicyGroupsResponse.

        导入策略组失败名字列表。

        :param failed_policy_group_name_list: The failed_policy_group_name_list of this ImportPolicyGroupsResponse.
        :type failed_policy_group_name_list: list[:class:`huaweicloudsdkworkspace.v2.PolicyGroupNameInfo`]
        """
        self._failed_policy_group_name_list = failed_policy_group_name_list

    def to_dict(self):
        import warnings
        warnings.warn("ImportPolicyGroupsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportPolicyGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
