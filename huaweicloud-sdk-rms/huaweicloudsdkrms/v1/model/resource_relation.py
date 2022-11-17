# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceRelation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relation_type': 'str',
        'from_resource_type': 'str',
        'to_resource_type': 'str',
        'from_resource_id': 'str',
        'to_resource_id': 'str'
    }

    attribute_map = {
        'relation_type': 'relation_type',
        'from_resource_type': 'from_resource_type',
        'to_resource_type': 'to_resource_type',
        'from_resource_id': 'from_resource_id',
        'to_resource_id': 'to_resource_id'
    }

    def __init__(self, relation_type=None, from_resource_type=None, to_resource_type=None, from_resource_id=None, to_resource_id=None):
        """ResourceRelation

        The model defined in huaweicloud sdk

        :param relation_type: 关系类型
        :type relation_type: str
        :param from_resource_type: 源资源类型
        :type from_resource_type: str
        :param to_resource_type: 目的资源类型
        :type to_resource_type: str
        :param from_resource_id: 源资源ID
        :type from_resource_id: str
        :param to_resource_id: 目的资源ID
        :type to_resource_id: str
        """
        
        

        self._relation_type = None
        self._from_resource_type = None
        self._to_resource_type = None
        self._from_resource_id = None
        self._to_resource_id = None
        self.discriminator = None

        if relation_type is not None:
            self.relation_type = relation_type
        if from_resource_type is not None:
            self.from_resource_type = from_resource_type
        if to_resource_type is not None:
            self.to_resource_type = to_resource_type
        if from_resource_id is not None:
            self.from_resource_id = from_resource_id
        if to_resource_id is not None:
            self.to_resource_id = to_resource_id

    @property
    def relation_type(self):
        """Gets the relation_type of this ResourceRelation.

        关系类型

        :return: The relation_type of this ResourceRelation.
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this ResourceRelation.

        关系类型

        :param relation_type: The relation_type of this ResourceRelation.
        :type relation_type: str
        """
        self._relation_type = relation_type

    @property
    def from_resource_type(self):
        """Gets the from_resource_type of this ResourceRelation.

        源资源类型

        :return: The from_resource_type of this ResourceRelation.
        :rtype: str
        """
        return self._from_resource_type

    @from_resource_type.setter
    def from_resource_type(self, from_resource_type):
        """Sets the from_resource_type of this ResourceRelation.

        源资源类型

        :param from_resource_type: The from_resource_type of this ResourceRelation.
        :type from_resource_type: str
        """
        self._from_resource_type = from_resource_type

    @property
    def to_resource_type(self):
        """Gets the to_resource_type of this ResourceRelation.

        目的资源类型

        :return: The to_resource_type of this ResourceRelation.
        :rtype: str
        """
        return self._to_resource_type

    @to_resource_type.setter
    def to_resource_type(self, to_resource_type):
        """Sets the to_resource_type of this ResourceRelation.

        目的资源类型

        :param to_resource_type: The to_resource_type of this ResourceRelation.
        :type to_resource_type: str
        """
        self._to_resource_type = to_resource_type

    @property
    def from_resource_id(self):
        """Gets the from_resource_id of this ResourceRelation.

        源资源ID

        :return: The from_resource_id of this ResourceRelation.
        :rtype: str
        """
        return self._from_resource_id

    @from_resource_id.setter
    def from_resource_id(self, from_resource_id):
        """Sets the from_resource_id of this ResourceRelation.

        源资源ID

        :param from_resource_id: The from_resource_id of this ResourceRelation.
        :type from_resource_id: str
        """
        self._from_resource_id = from_resource_id

    @property
    def to_resource_id(self):
        """Gets the to_resource_id of this ResourceRelation.

        目的资源ID

        :return: The to_resource_id of this ResourceRelation.
        :rtype: str
        """
        return self._to_resource_id

    @to_resource_id.setter
    def to_resource_id(self, to_resource_id):
        """Sets the to_resource_id of this ResourceRelation.

        目的资源ID

        :param to_resource_id: The to_resource_id of this ResourceRelation.
        :type to_resource_id: str
        """
        self._to_resource_id = to_resource_id

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
        if not isinstance(other, ResourceRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
