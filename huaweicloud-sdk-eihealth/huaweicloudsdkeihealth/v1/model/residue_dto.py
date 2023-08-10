# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResidueDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chain': 'str',
        'name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'chain': 'chain',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, chain=None, name=None, id=None):
        """ResidueDto

        The model defined in huaweicloud sdk

        :param chain: 氨基酸残基或者配体链的名称
        :type chain: str
        :param name: 氨基酸残基或者配体名称
        :type name: str
        :param id: 氨基酸残基或者配体的序列ID
        :type id: int
        """
        
        

        self._chain = None
        self._name = None
        self._id = None
        self.discriminator = None

        self.chain = chain
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def chain(self):
        """Gets the chain of this ResidueDto.

        氨基酸残基或者配体链的名称

        :return: The chain of this ResidueDto.
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this ResidueDto.

        氨基酸残基或者配体链的名称

        :param chain: The chain of this ResidueDto.
        :type chain: str
        """
        self._chain = chain

    @property
    def name(self):
        """Gets the name of this ResidueDto.

        氨基酸残基或者配体名称

        :return: The name of this ResidueDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResidueDto.

        氨基酸残基或者配体名称

        :param name: The name of this ResidueDto.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ResidueDto.

        氨基酸残基或者配体的序列ID

        :return: The id of this ResidueDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResidueDto.

        氨基酸残基或者配体的序列ID

        :param id: The id of this ResidueDto.
        :type id: int
        """
        self._id = id

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
        if not isinstance(other, ResidueDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
