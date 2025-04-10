# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KnowledgePointInfo:

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
        'sequence': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'sequence': 'sequence'
    }

    def __init__(self, id=None, name=None, sequence=None):
        r"""KnowledgePointInfo

        The model defined in huaweicloud sdk

        :param id: 知识点id
        :type id: str
        :param name: 知识点名称
        :type name: str
        :param sequence: 知识点顺序编号
        :type sequence: int
        """
        
        

        self._id = None
        self._name = None
        self._sequence = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.sequence = sequence

    @property
    def id(self):
        r"""Gets the id of this KnowledgePointInfo.

        知识点id

        :return: The id of this KnowledgePointInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this KnowledgePointInfo.

        知识点id

        :param id: The id of this KnowledgePointInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this KnowledgePointInfo.

        知识点名称

        :return: The name of this KnowledgePointInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KnowledgePointInfo.

        知识点名称

        :param name: The name of this KnowledgePointInfo.
        :type name: str
        """
        self._name = name

    @property
    def sequence(self):
        r"""Gets the sequence of this KnowledgePointInfo.

        知识点顺序编号

        :return: The sequence of this KnowledgePointInfo.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this KnowledgePointInfo.

        知识点顺序编号

        :param sequence: The sequence of this KnowledgePointInfo.
        :type sequence: int
        """
        self._sequence = sequence

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
        if not isinstance(other, KnowledgePointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
