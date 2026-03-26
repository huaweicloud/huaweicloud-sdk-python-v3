# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLockBlockingRelationshipRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'unique_id': 'str',
        'spid': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'unique_id': 'unique_id',
        'spid': 'spid',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, unique_id=None, spid=None, x_language=None):
        r"""ListLockBlockingRelationshipRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param unique_id: 批次ID。
        :type unique_id: str
        :param spid: 会话ID。
        :type spid: int
        :param x_language: 请求语言类型。en-us：英文。 zh-cn：中文。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._unique_id = None
        self._spid = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.unique_id = unique_id
        self.spid = spid
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListLockBlockingRelationshipRequest.

        实例ID。

        :return: The instance_id of this ListLockBlockingRelationshipRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListLockBlockingRelationshipRequest.

        实例ID。

        :param instance_id: The instance_id of this ListLockBlockingRelationshipRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def unique_id(self):
        r"""Gets the unique_id of this ListLockBlockingRelationshipRequest.

        批次ID。

        :return: The unique_id of this ListLockBlockingRelationshipRequest.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        r"""Sets the unique_id of this ListLockBlockingRelationshipRequest.

        批次ID。

        :param unique_id: The unique_id of this ListLockBlockingRelationshipRequest.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def spid(self):
        r"""Gets the spid of this ListLockBlockingRelationshipRequest.

        会话ID。

        :return: The spid of this ListLockBlockingRelationshipRequest.
        :rtype: int
        """
        return self._spid

    @spid.setter
    def spid(self, spid):
        r"""Sets the spid of this ListLockBlockingRelationshipRequest.

        会话ID。

        :param spid: The spid of this ListLockBlockingRelationshipRequest.
        :type spid: int
        """
        self._spid = spid

    @property
    def x_language(self):
        r"""Gets the x_language of this ListLockBlockingRelationshipRequest.

        请求语言类型。en-us：英文。 zh-cn：中文。

        :return: The x_language of this ListLockBlockingRelationshipRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListLockBlockingRelationshipRequest.

        请求语言类型。en-us：英文。 zh-cn：中文。

        :param x_language: The x_language of this ListLockBlockingRelationshipRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListLockBlockingRelationshipRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
