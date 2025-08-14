# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIdentityStoreAssociationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity_store_associations': 'list[IdentityStoreDto]'
    }

    attribute_map = {
        'identity_store_associations': 'identity_store_associations'
    }

    def __init__(self, identity_store_associations=None):
        r"""ListIdentityStoreAssociationResponse

        The model defined in huaweicloud sdk

        :param identity_store_associations: IAM身份中心服务实例关联的身份源配置信息
        :type identity_store_associations: list[:class:`huaweicloudsdkidentitycenter.v1.IdentityStoreDto`]
        """
        
        super(ListIdentityStoreAssociationResponse, self).__init__()

        self._identity_store_associations = None
        self.discriminator = None

        if identity_store_associations is not None:
            self.identity_store_associations = identity_store_associations

    @property
    def identity_store_associations(self):
        r"""Gets the identity_store_associations of this ListIdentityStoreAssociationResponse.

        IAM身份中心服务实例关联的身份源配置信息

        :return: The identity_store_associations of this ListIdentityStoreAssociationResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.IdentityStoreDto`]
        """
        return self._identity_store_associations

    @identity_store_associations.setter
    def identity_store_associations(self, identity_store_associations):
        r"""Sets the identity_store_associations of this ListIdentityStoreAssociationResponse.

        IAM身份中心服务实例关联的身份源配置信息

        :param identity_store_associations: The identity_store_associations of this ListIdentityStoreAssociationResponse.
        :type identity_store_associations: list[:class:`huaweicloudsdkidentitycenter.v1.IdentityStoreDto`]
        """
        self._identity_store_associations = identity_store_associations

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
        if not isinstance(other, ListIdentityStoreAssociationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
