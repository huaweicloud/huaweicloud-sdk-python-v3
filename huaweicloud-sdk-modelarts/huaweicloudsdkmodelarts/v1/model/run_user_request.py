# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunUserRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uid': 'int',
        'gid': 'int'
    }

    attribute_map = {
        'uid': 'uid',
        'gid': 'gid'
    }

    def __init__(self, uid=None, gid=None):
        r"""RunUserRequest

        The model defined in huaweicloud sdk

        :param uid: 容器启动用户的user id
        :type uid: int
        :param gid: 容器启动用户的group id
        :type gid: int
        """
        
        

        self._uid = None
        self._gid = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid

    @property
    def uid(self):
        r"""Gets the uid of this RunUserRequest.

        容器启动用户的user id

        :return: The uid of this RunUserRequest.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this RunUserRequest.

        容器启动用户的user id

        :param uid: The uid of this RunUserRequest.
        :type uid: int
        """
        self._uid = uid

    @property
    def gid(self):
        r"""Gets the gid of this RunUserRequest.

        容器启动用户的group id

        :return: The gid of this RunUserRequest.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        r"""Sets the gid of this RunUserRequest.

        容器启动用户的group id

        :param gid: The gid of this RunUserRequest.
        :type gid: int
        """
        self._gid = gid

    def to_dict(self):
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
        if not isinstance(other, RunUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
