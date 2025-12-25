# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AopworkflowInstanceDetailDataclass:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'en_name': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'en_name': 'en_name',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, en_name=None, id=None, name=None):
        r"""AopworkflowInstanceDetailDataclass

        The model defined in huaweicloud sdk

        :param en_name: **参数解释**: 数据类的英文名字 **约束限制**: 不涉及
        :type en_name: str
        :param id: **参数解释**: 数据类的ID **约束限制**: 不涉及
        :type id: str
        :param name: **参数解释**: 数据类的中文名字 **约束限制**: 不涉及
        :type name: str
        """
        
        

        self._en_name = None
        self._id = None
        self._name = None
        self.discriminator = None

        if en_name is not None:
            self.en_name = en_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def en_name(self):
        r"""Gets the en_name of this AopworkflowInstanceDetailDataclass.

        **参数解释**: 数据类的英文名字 **约束限制**: 不涉及

        :return: The en_name of this AopworkflowInstanceDetailDataclass.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        r"""Sets the en_name of this AopworkflowInstanceDetailDataclass.

        **参数解释**: 数据类的英文名字 **约束限制**: 不涉及

        :param en_name: The en_name of this AopworkflowInstanceDetailDataclass.
        :type en_name: str
        """
        self._en_name = en_name

    @property
    def id(self):
        r"""Gets the id of this AopworkflowInstanceDetailDataclass.

        **参数解释**: 数据类的ID **约束限制**: 不涉及

        :return: The id of this AopworkflowInstanceDetailDataclass.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AopworkflowInstanceDetailDataclass.

        **参数解释**: 数据类的ID **约束限制**: 不涉及

        :param id: The id of this AopworkflowInstanceDetailDataclass.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AopworkflowInstanceDetailDataclass.

        **参数解释**: 数据类的中文名字 **约束限制**: 不涉及

        :return: The name of this AopworkflowInstanceDetailDataclass.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AopworkflowInstanceDetailDataclass.

        **参数解释**: 数据类的中文名字 **约束限制**: 不涉及

        :param name: The name of this AopworkflowInstanceDetailDataclass.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, AopworkflowInstanceDetailDataclass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
