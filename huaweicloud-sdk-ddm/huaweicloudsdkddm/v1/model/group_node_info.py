# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupNodeInfo:

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
        'az': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'az': 'az'
    }

    def __init__(self, id=None, name=None, az=None):
        r"""GroupNodeInfo

        The model defined in huaweicloud sdk

        :param id: 节点ID。
        :type id: str
        :param name: 节点名称。
        :type name: str
        :param az: 节点所在AZ。
        :type az: str
        """
        
        

        self._id = None
        self._name = None
        self._az = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.az = az

    @property
    def id(self):
        r"""Gets the id of this GroupNodeInfo.

        节点ID。

        :return: The id of this GroupNodeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupNodeInfo.

        节点ID。

        :param id: The id of this GroupNodeInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GroupNodeInfo.

        节点名称。

        :return: The name of this GroupNodeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupNodeInfo.

        节点名称。

        :param name: The name of this GroupNodeInfo.
        :type name: str
        """
        self._name = name

    @property
    def az(self):
        r"""Gets the az of this GroupNodeInfo.

        节点所在AZ。

        :return: The az of this GroupNodeInfo.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this GroupNodeInfo.

        节点所在AZ。

        :param az: The az of this GroupNodeInfo.
        :type az: str
        """
        self._az = az

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
        if not isinstance(other, GroupNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
