# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomEvaluationDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'evaluation_type_id': 'int',
        'level': 'int',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'evaluation_type_id': 'evaluation_type_id',
        'level': 'level',
        'name': 'name'
    }

    def __init__(self, id=None, evaluation_type_id=None, level=None, name=None):
        r"""CustomEvaluationDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 自定义评价id。
        :type id: int
        :param evaluation_type_id: 评价类型id
        :type evaluation_type_id: int
        :param level: 评价等级
        :type level: int
        :param name: 评价名称
        :type name: str
        """
        
        

        self._id = None
        self._evaluation_type_id = None
        self._level = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if evaluation_type_id is not None:
            self.evaluation_type_id = evaluation_type_id
        if level is not None:
            self.level = level
        if name is not None:
            self.name = name

    @property
    def id(self):
        r"""Gets the id of this CustomEvaluationDto.

        **参数解释：** 自定义评价id。

        :return: The id of this CustomEvaluationDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CustomEvaluationDto.

        **参数解释：** 自定义评价id。

        :param id: The id of this CustomEvaluationDto.
        :type id: int
        """
        self._id = id

    @property
    def evaluation_type_id(self):
        r"""Gets the evaluation_type_id of this CustomEvaluationDto.

        评价类型id

        :return: The evaluation_type_id of this CustomEvaluationDto.
        :rtype: int
        """
        return self._evaluation_type_id

    @evaluation_type_id.setter
    def evaluation_type_id(self, evaluation_type_id):
        r"""Sets the evaluation_type_id of this CustomEvaluationDto.

        评价类型id

        :param evaluation_type_id: The evaluation_type_id of this CustomEvaluationDto.
        :type evaluation_type_id: int
        """
        self._evaluation_type_id = evaluation_type_id

    @property
    def level(self):
        r"""Gets the level of this CustomEvaluationDto.

        评价等级

        :return: The level of this CustomEvaluationDto.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CustomEvaluationDto.

        评价等级

        :param level: The level of this CustomEvaluationDto.
        :type level: int
        """
        self._level = level

    @property
    def name(self):
        r"""Gets the name of this CustomEvaluationDto.

        评价名称

        :return: The name of this CustomEvaluationDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CustomEvaluationDto.

        评价名称

        :param name: The name of this CustomEvaluationDto.
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
        if not isinstance(other, CustomEvaluationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
