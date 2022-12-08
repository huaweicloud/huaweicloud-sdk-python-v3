# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelationSimpleInfo:

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
        'name': 'str',
        'path': 'str',
        'risk_level': 'int',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'path': 'path',
        'risk_level': 'risk_level',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, path=None, risk_level=None, type=None):
        """RelationSimpleInfo

        The model defined in huaweicloud sdk

        :param id: 关系信息ID
        :type id: str
        :param name: 关系信息名称
        :type name: str
        :param path: 关系信息路径
        :type path: str
        :param risk_level: 风险等级
        :type risk_level: int
        :param type: 关系信息类型
        :type type: str
        """
        
        

        self._id = None
        self._name = None
        self._path = None
        self._risk_level = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if risk_level is not None:
            self.risk_level = risk_level
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this RelationSimpleInfo.

        关系信息ID

        :return: The id of this RelationSimpleInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelationSimpleInfo.

        关系信息ID

        :param id: The id of this RelationSimpleInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this RelationSimpleInfo.

        关系信息名称

        :return: The name of this RelationSimpleInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RelationSimpleInfo.

        关系信息名称

        :param name: The name of this RelationSimpleInfo.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        """Gets the path of this RelationSimpleInfo.

        关系信息路径

        :return: The path of this RelationSimpleInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RelationSimpleInfo.

        关系信息路径

        :param path: The path of this RelationSimpleInfo.
        :type path: str
        """
        self._path = path

    @property
    def risk_level(self):
        """Gets the risk_level of this RelationSimpleInfo.

        风险等级

        :return: The risk_level of this RelationSimpleInfo.
        :rtype: int
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """Sets the risk_level of this RelationSimpleInfo.

        风险等级

        :param risk_level: The risk_level of this RelationSimpleInfo.
        :type risk_level: int
        """
        self._risk_level = risk_level

    @property
    def type(self):
        """Gets the type of this RelationSimpleInfo.

        关系信息类型

        :return: The type of this RelationSimpleInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RelationSimpleInfo.

        关系信息类型

        :param type: The type of this RelationSimpleInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, RelationSimpleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
