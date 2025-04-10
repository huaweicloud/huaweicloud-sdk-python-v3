# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetGroupMembershipIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity_store_id': 'str',
        'membership_id': 'str'
    }

    attribute_map = {
        'identity_store_id': 'identity_store_id',
        'membership_id': 'membership_id'
    }

    def __init__(self, identity_store_id=None, membership_id=None):
        r"""GetGroupMembershipIdResponse

        The model defined in huaweicloud sdk

        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param membership_id: 身份源中用户和组关联关系的全局唯一标识符（ID）
        :type membership_id: str
        """
        
        super(GetGroupMembershipIdResponse, self).__init__()

        self._identity_store_id = None
        self._membership_id = None
        self.discriminator = None

        if identity_store_id is not None:
            self.identity_store_id = identity_store_id
        if membership_id is not None:
            self.membership_id = membership_id

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this GetGroupMembershipIdResponse.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this GetGroupMembershipIdResponse.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this GetGroupMembershipIdResponse.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this GetGroupMembershipIdResponse.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def membership_id(self):
        r"""Gets the membership_id of this GetGroupMembershipIdResponse.

        身份源中用户和组关联关系的全局唯一标识符（ID）

        :return: The membership_id of this GetGroupMembershipIdResponse.
        :rtype: str
        """
        return self._membership_id

    @membership_id.setter
    def membership_id(self, membership_id):
        r"""Sets the membership_id of this GetGroupMembershipIdResponse.

        身份源中用户和组关联关系的全局唯一标识符（ID）

        :param membership_id: The membership_id of this GetGroupMembershipIdResponse.
        :type membership_id: str
        """
        self._membership_id = membership_id

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
        if not isinstance(other, GetGroupMembershipIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
