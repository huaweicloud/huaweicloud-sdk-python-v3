# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DescribeGroupMembershipResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'identity_store_id': 'str',
        'member_id': 'MemberIdDto',
        'membership_id': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'identity_store_id': 'identity_store_id',
        'member_id': 'member_id',
        'membership_id': 'membership_id'
    }

    def __init__(self, group_id=None, identity_store_id=None, member_id=None, membership_id=None):
        """DescribeGroupMembershipResponse

        The model defined in huaweicloud sdk

        :param group_id: 身份源中IAM身份中心用户组的全局唯一标识符（ID）
        :type group_id: str
        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param member_id: 
        :type member_id: :class:`huaweicloudsdkidentitycenterstore.v1.MemberIdDto`
        :param membership_id: 身份源中用户和组关联关系的全局唯一标识符（ID）
        :type membership_id: str
        """
        
        super(DescribeGroupMembershipResponse, self).__init__()

        self._group_id = None
        self._identity_store_id = None
        self._member_id = None
        self._membership_id = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if identity_store_id is not None:
            self.identity_store_id = identity_store_id
        if member_id is not None:
            self.member_id = member_id
        if membership_id is not None:
            self.membership_id = membership_id

    @property
    def group_id(self):
        """Gets the group_id of this DescribeGroupMembershipResponse.

        身份源中IAM身份中心用户组的全局唯一标识符（ID）

        :return: The group_id of this DescribeGroupMembershipResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DescribeGroupMembershipResponse.

        身份源中IAM身份中心用户组的全局唯一标识符（ID）

        :param group_id: The group_id of this DescribeGroupMembershipResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def identity_store_id(self):
        """Gets the identity_store_id of this DescribeGroupMembershipResponse.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this DescribeGroupMembershipResponse.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        """Sets the identity_store_id of this DescribeGroupMembershipResponse.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this DescribeGroupMembershipResponse.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def member_id(self):
        """Gets the member_id of this DescribeGroupMembershipResponse.

        :return: The member_id of this DescribeGroupMembershipResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.MemberIdDto`
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this DescribeGroupMembershipResponse.

        :param member_id: The member_id of this DescribeGroupMembershipResponse.
        :type member_id: :class:`huaweicloudsdkidentitycenterstore.v1.MemberIdDto`
        """
        self._member_id = member_id

    @property
    def membership_id(self):
        """Gets the membership_id of this DescribeGroupMembershipResponse.

        身份源中用户和组关联关系的全局唯一标识符（ID）

        :return: The membership_id of this DescribeGroupMembershipResponse.
        :rtype: str
        """
        return self._membership_id

    @membership_id.setter
    def membership_id(self, membership_id):
        """Sets the membership_id of this DescribeGroupMembershipResponse.

        身份源中用户和组关联关系的全局唯一标识符（ID）

        :param membership_id: The membership_id of this DescribeGroupMembershipResponse.
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
        if not isinstance(other, DescribeGroupMembershipResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
