# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeTypes:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'detail': 'list[Detail]',
        'id': 'str',
        'spec_name': 'str'
    }

    attribute_map = {
        'detail': 'detail',
        'id': 'id',
        'spec_name': 'spec_name'
    }

    def __init__(self, detail=None, id=None, spec_name=None):
        """NodeTypes - a model defined in huaweicloud sdk"""
        
        

        self._detail = None
        self._id = None
        self._spec_name = None
        self.discriminator = None

        self.detail = detail
        self.id = id
        self.spec_name = spec_name

    @property
    def detail(self):
        """Gets the detail of this NodeTypes.

        节点类型详细

        :return: The detail of this NodeTypes.
        :rtype: list[Detail]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this NodeTypes.

        节点类型详细

        :param detail: The detail of this NodeTypes.
        :type: list[Detail]
        """
        self._detail = detail

    @property
    def id(self):
        """Gets the id of this NodeTypes.

        节点类型ID

        :return: The id of this NodeTypes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeTypes.

        节点类型ID

        :param id: The id of this NodeTypes.
        :type: str
        """
        self._id = id

    @property
    def spec_name(self):
        """Gets the spec_name of this NodeTypes.


        :return: The spec_name of this NodeTypes.
        :rtype: str
        """
        return self._spec_name

    @spec_name.setter
    def spec_name(self, spec_name):
        """Sets the spec_name of this NodeTypes.


        :param spec_name: The spec_name of this NodeTypes.
        :type: str
        """
        self._spec_name = spec_name

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
        if not isinstance(other, NodeTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
