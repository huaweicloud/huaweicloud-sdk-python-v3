# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGroupResponse(SdkResponse):

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
        'identity_store_id': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'identity_store_id': 'identity_store_id'
    }

    def __init__(self, group_id=None, identity_store_id=None):
        """CreateGroupResponse

        The model defined in huaweicloud sdk

        :param group_id: 身份源中IAM身份中心用户组的全局唯一标识符（ID）
        :type group_id: str
        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        """
        
        super(CreateGroupResponse, self).__init__()

        self._group_id = None
        self._identity_store_id = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if identity_store_id is not None:
            self.identity_store_id = identity_store_id

    @property
    def group_id(self):
        """Gets the group_id of this CreateGroupResponse.

        身份源中IAM身份中心用户组的全局唯一标识符（ID）

        :return: The group_id of this CreateGroupResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CreateGroupResponse.

        身份源中IAM身份中心用户组的全局唯一标识符（ID）

        :param group_id: The group_id of this CreateGroupResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def identity_store_id(self):
        """Gets the identity_store_id of this CreateGroupResponse.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this CreateGroupResponse.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        """Sets the identity_store_id of this CreateGroupResponse.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this CreateGroupResponse.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

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
        if not isinstance(other, CreateGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
