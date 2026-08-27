# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyObjectDetailInfo:

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
        'object_id': 'str',
        'object_type': 'str',
        'object_name': 'str',
        'object_domain': 'str'
    }

    attribute_map = {
        'id': 'id',
        'object_id': 'object_id',
        'object_type': 'object_type',
        'object_name': 'object_name',
        'object_domain': 'object_domain'
    }

    def __init__(self, id=None, object_id=None, object_type=None, object_name=None, object_domain=None):
        r"""ApplyObjectDetailInfo

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param object_id: 对象id
        :type object_id: str
        :param object_type: 对象类型
        :type object_type: str
        :param object_name: 对象名称
        :type object_name: str
        :param object_domain: 域名称（用户）
        :type object_domain: str
        """
        
        

        self._id = None
        self._object_id = None
        self._object_type = None
        self._object_name = None
        self._object_domain = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if object_id is not None:
            self.object_id = object_id
        if object_type is not None:
            self.object_type = object_type
        if object_name is not None:
            self.object_name = object_name
        if object_domain is not None:
            self.object_domain = object_domain

    @property
    def id(self):
        r"""Gets the id of this ApplyObjectDetailInfo.

        id

        :return: The id of this ApplyObjectDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApplyObjectDetailInfo.

        id

        :param id: The id of this ApplyObjectDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def object_id(self):
        r"""Gets the object_id of this ApplyObjectDetailInfo.

        对象id

        :return: The object_id of this ApplyObjectDetailInfo.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ApplyObjectDetailInfo.

        对象id

        :param object_id: The object_id of this ApplyObjectDetailInfo.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def object_type(self):
        r"""Gets the object_type of this ApplyObjectDetailInfo.

        对象类型

        :return: The object_type of this ApplyObjectDetailInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ApplyObjectDetailInfo.

        对象类型

        :param object_type: The object_type of this ApplyObjectDetailInfo.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def object_name(self):
        r"""Gets the object_name of this ApplyObjectDetailInfo.

        对象名称

        :return: The object_name of this ApplyObjectDetailInfo.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this ApplyObjectDetailInfo.

        对象名称

        :param object_name: The object_name of this ApplyObjectDetailInfo.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def object_domain(self):
        r"""Gets the object_domain of this ApplyObjectDetailInfo.

        域名称（用户）

        :return: The object_domain of this ApplyObjectDetailInfo.
        :rtype: str
        """
        return self._object_domain

    @object_domain.setter
    def object_domain(self, object_domain):
        r"""Sets the object_domain of this ApplyObjectDetailInfo.

        域名称（用户）

        :param object_domain: The object_domain of this ApplyObjectDetailInfo.
        :type object_domain: str
        """
        self._object_domain = object_domain

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
        if not isinstance(other, ApplyObjectDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
