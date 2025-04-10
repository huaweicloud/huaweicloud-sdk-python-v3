# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GrantSecretReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'type': 'str',
        'grantee_type': 'str',
        'grantee_target_id': 'str',
        'validity_time': 'date'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'type': 'type',
        'grantee_type': 'grantee_type',
        'grantee_target_id': 'grantee_target_id',
        'validity_time': 'validity_time'
    }

    def __init__(self, resource_id=None, type=None, grantee_type=None, grantee_target_id=None, validity_time=None):
        r"""GrantSecretReqBody

        The model defined in huaweicloud sdk

        :param resource_id: 资源id
        :type resource_id: str
        :param type: 资源类型（SECRET、GROUP）
        :type type: str
        :param grantee_type: 被授权类型，（0：USER；2：GROUP）个人，群组
        :type grantee_type: str
        :param grantee_target_id: 被授权id
        :type grantee_target_id: str
        :param validity_time: 有效期截止时间
        :type validity_time: date
        """
        
        

        self._resource_id = None
        self._type = None
        self._grantee_type = None
        self._grantee_target_id = None
        self._validity_time = None
        self.discriminator = None

        self.resource_id = resource_id
        self.type = type
        self.grantee_type = grantee_type
        self.grantee_target_id = grantee_target_id
        if validity_time is not None:
            self.validity_time = validity_time

    @property
    def resource_id(self):
        r"""Gets the resource_id of this GrantSecretReqBody.

        资源id

        :return: The resource_id of this GrantSecretReqBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this GrantSecretReqBody.

        资源id

        :param resource_id: The resource_id of this GrantSecretReqBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def type(self):
        r"""Gets the type of this GrantSecretReqBody.

        资源类型（SECRET、GROUP）

        :return: The type of this GrantSecretReqBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GrantSecretReqBody.

        资源类型（SECRET、GROUP）

        :param type: The type of this GrantSecretReqBody.
        :type type: str
        """
        self._type = type

    @property
    def grantee_type(self):
        r"""Gets the grantee_type of this GrantSecretReqBody.

        被授权类型，（0：USER；2：GROUP）个人，群组

        :return: The grantee_type of this GrantSecretReqBody.
        :rtype: str
        """
        return self._grantee_type

    @grantee_type.setter
    def grantee_type(self, grantee_type):
        r"""Sets the grantee_type of this GrantSecretReqBody.

        被授权类型，（0：USER；2：GROUP）个人，群组

        :param grantee_type: The grantee_type of this GrantSecretReqBody.
        :type grantee_type: str
        """
        self._grantee_type = grantee_type

    @property
    def grantee_target_id(self):
        r"""Gets the grantee_target_id of this GrantSecretReqBody.

        被授权id

        :return: The grantee_target_id of this GrantSecretReqBody.
        :rtype: str
        """
        return self._grantee_target_id

    @grantee_target_id.setter
    def grantee_target_id(self, grantee_target_id):
        r"""Sets the grantee_target_id of this GrantSecretReqBody.

        被授权id

        :param grantee_target_id: The grantee_target_id of this GrantSecretReqBody.
        :type grantee_target_id: str
        """
        self._grantee_target_id = grantee_target_id

    @property
    def validity_time(self):
        r"""Gets the validity_time of this GrantSecretReqBody.

        有效期截止时间

        :return: The validity_time of this GrantSecretReqBody.
        :rtype: date
        """
        return self._validity_time

    @validity_time.setter
    def validity_time(self, validity_time):
        r"""Sets the validity_time of this GrantSecretReqBody.

        有效期截止时间

        :param validity_time: The validity_time of this GrantSecretReqBody.
        :type validity_time: date
        """
        self._validity_time = validity_time

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
        if not isinstance(other, GrantSecretReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
