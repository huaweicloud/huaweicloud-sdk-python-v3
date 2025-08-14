# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateProfileReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'accessor_type': 'str',
        'identity_store_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'accessor_type': 'accessor_type',
        'identity_store_id': 'identity_store_id'
    }

    def __init__(self, id=None, accessor_type=None, identity_store_id=None):
        r"""DisassociateProfileReqBody

        The model defined in huaweicloud sdk

        :param id: 用户或用户组的唯一标识ID
        :type id: str
        :param accessor_type: 解除绑定的实体类型，可为用户或者用户组
        :type accessor_type: str
        :param identity_store_id: 关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。
        :type identity_store_id: str
        """
        
        

        self._id = None
        self._accessor_type = None
        self._identity_store_id = None
        self.discriminator = None

        self.id = id
        self.accessor_type = accessor_type
        self.identity_store_id = identity_store_id

    @property
    def id(self):
        r"""Gets the id of this DisassociateProfileReqBody.

        用户或用户组的唯一标识ID

        :return: The id of this DisassociateProfileReqBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DisassociateProfileReqBody.

        用户或用户组的唯一标识ID

        :param id: The id of this DisassociateProfileReqBody.
        :type id: str
        """
        self._id = id

    @property
    def accessor_type(self):
        r"""Gets the accessor_type of this DisassociateProfileReqBody.

        解除绑定的实体类型，可为用户或者用户组

        :return: The accessor_type of this DisassociateProfileReqBody.
        :rtype: str
        """
        return self._accessor_type

    @accessor_type.setter
    def accessor_type(self, accessor_type):
        r"""Sets the accessor_type of this DisassociateProfileReqBody.

        解除绑定的实体类型，可为用户或者用户组

        :param accessor_type: The accessor_type of this DisassociateProfileReqBody.
        :type accessor_type: str
        """
        self._accessor_type = accessor_type

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this DisassociateProfileReqBody.

        关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。

        :return: The identity_store_id of this DisassociateProfileReqBody.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this DisassociateProfileReqBody.

        关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。

        :param identity_store_id: The identity_store_id of this DisassociateProfileReqBody.
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
        if not isinstance(other, DisassociateProfileReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
