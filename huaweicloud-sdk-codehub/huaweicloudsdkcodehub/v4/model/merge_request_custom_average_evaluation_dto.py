# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestCustomAverageEvaluationDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluation_type_id': 'int',
        'name': 'str',
        'level': 'float'
    }

    attribute_map = {
        'evaluation_type_id': 'evaluation_type_id',
        'name': 'name',
        'level': 'level'
    }

    def __init__(self, evaluation_type_id=None, name=None, level=None):
        r"""MergeRequestCustomAverageEvaluationDto

        The model defined in huaweicloud sdk

        :param evaluation_type_id: **参数解释：** 自定义评价维度id。
        :type evaluation_type_id: int
        :param name: **参数解释：** 自定义评价维度名称。
        :type name: str
        :param level: **参数解释：** 自定义评价维度平均分。
        :type level: float
        """
        
        

        self._evaluation_type_id = None
        self._name = None
        self._level = None
        self.discriminator = None

        if evaluation_type_id is not None:
            self.evaluation_type_id = evaluation_type_id
        if name is not None:
            self.name = name
        if level is not None:
            self.level = level

    @property
    def evaluation_type_id(self):
        r"""Gets the evaluation_type_id of this MergeRequestCustomAverageEvaluationDto.

        **参数解释：** 自定义评价维度id。

        :return: The evaluation_type_id of this MergeRequestCustomAverageEvaluationDto.
        :rtype: int
        """
        return self._evaluation_type_id

    @evaluation_type_id.setter
    def evaluation_type_id(self, evaluation_type_id):
        r"""Sets the evaluation_type_id of this MergeRequestCustomAverageEvaluationDto.

        **参数解释：** 自定义评价维度id。

        :param evaluation_type_id: The evaluation_type_id of this MergeRequestCustomAverageEvaluationDto.
        :type evaluation_type_id: int
        """
        self._evaluation_type_id = evaluation_type_id

    @property
    def name(self):
        r"""Gets the name of this MergeRequestCustomAverageEvaluationDto.

        **参数解释：** 自定义评价维度名称。

        :return: The name of this MergeRequestCustomAverageEvaluationDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MergeRequestCustomAverageEvaluationDto.

        **参数解释：** 自定义评价维度名称。

        :param name: The name of this MergeRequestCustomAverageEvaluationDto.
        :type name: str
        """
        self._name = name

    @property
    def level(self):
        r"""Gets the level of this MergeRequestCustomAverageEvaluationDto.

        **参数解释：** 自定义评价维度平均分。

        :return: The level of this MergeRequestCustomAverageEvaluationDto.
        :rtype: float
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this MergeRequestCustomAverageEvaluationDto.

        **参数解释：** 自定义评价维度平均分。

        :param level: The level of this MergeRequestCustomAverageEvaluationDto.
        :type level: float
        """
        self._level = level

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
        if not isinstance(other, MergeRequestCustomAverageEvaluationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
