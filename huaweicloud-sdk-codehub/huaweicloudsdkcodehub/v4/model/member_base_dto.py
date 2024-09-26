# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberBaseDto:

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
        'iam_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'iam_id': 'iam_id',
        'name': 'name'
    }

    def __init__(self, id=None, iam_id=None, name=None):
        """MemberBaseDto

        The model defined in huaweicloud sdk

        :param id: 用户id
        :type id: str
        :param iam_id: iam_id
        :type iam_id: str
        :param name: 成员名字
        :type name: str
        """
        
        

        self._id = None
        self._iam_id = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if iam_id is not None:
            self.iam_id = iam_id
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this MemberBaseDto.

        用户id

        :return: The id of this MemberBaseDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MemberBaseDto.

        用户id

        :param id: The id of this MemberBaseDto.
        :type id: str
        """
        self._id = id

    @property
    def iam_id(self):
        """Gets the iam_id of this MemberBaseDto.

        iam_id

        :return: The iam_id of this MemberBaseDto.
        :rtype: str
        """
        return self._iam_id

    @iam_id.setter
    def iam_id(self, iam_id):
        """Sets the iam_id of this MemberBaseDto.

        iam_id

        :param iam_id: The iam_id of this MemberBaseDto.
        :type iam_id: str
        """
        self._iam_id = iam_id

    @property
    def name(self):
        """Gets the name of this MemberBaseDto.

        成员名字

        :return: The name of this MemberBaseDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MemberBaseDto.

        成员名字

        :param name: The name of this MemberBaseDto.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, MemberBaseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
