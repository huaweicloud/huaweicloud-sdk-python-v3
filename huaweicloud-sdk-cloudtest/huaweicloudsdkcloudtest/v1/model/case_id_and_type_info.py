# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseIdAndTypeInfo:

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
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, id=None, type=None):
        r"""CaseIdAndTypeInfo

        The model defined in huaweicloud sdk

        :param id: 用例id
        :type id: str
        :param type: 用例类型, 对应ServiceType
        :type type: str
        """
        
        

        self._id = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def id(self):
        r"""Gets the id of this CaseIdAndTypeInfo.

        用例id

        :return: The id of this CaseIdAndTypeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CaseIdAndTypeInfo.

        用例id

        :param id: The id of this CaseIdAndTypeInfo.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this CaseIdAndTypeInfo.

        用例类型, 对应ServiceType

        :return: The type of this CaseIdAndTypeInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CaseIdAndTypeInfo.

        用例类型, 对应ServiceType

        :param type: The type of this CaseIdAndTypeInfo.
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
        if not isinstance(other, CaseIdAndTypeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
