# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSparseBackupPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policies': 'list[SparseBackupPolicy]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'policies': 'policies',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, policies=None, x_request_id=None):
        r"""ListSparseBackupPolicyResponse

        The model defined in huaweicloud sdk

        :param policies: 备份策略集
        :type policies: list[:class:`huaweicloudsdkrds.v3.SparseBackupPolicy`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._policies = None
        self._x_request_id = None
        self.discriminator = None

        if policies is not None:
            self.policies = policies
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def policies(self):
        r"""Gets the policies of this ListSparseBackupPolicyResponse.

        备份策略集

        :return: The policies of this ListSparseBackupPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.SparseBackupPolicy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this ListSparseBackupPolicyResponse.

        备份策略集

        :param policies: The policies of this ListSparseBackupPolicyResponse.
        :type policies: list[:class:`huaweicloudsdkrds.v3.SparseBackupPolicy`]
        """
        self._policies = policies

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListSparseBackupPolicyResponse.

        :return: The x_request_id of this ListSparseBackupPolicyResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListSparseBackupPolicyResponse.

        :param x_request_id: The x_request_id of this ListSparseBackupPolicyResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListSparseBackupPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSparseBackupPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
