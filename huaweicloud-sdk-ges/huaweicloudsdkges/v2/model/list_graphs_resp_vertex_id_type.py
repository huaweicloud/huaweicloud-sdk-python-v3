# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGraphsRespVertexIdType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id_type': 'str',
        'id_length': 'int'
    }

    attribute_map = {
        'id_type': 'id_type',
        'id_length': 'id_length'
    }

    def __init__(self, id_type=None, id_length=None):
        r"""ListGraphsRespVertexIdType

        The model defined in huaweicloud sdk

        :param id_type: id类型，目前支持固定长度fixedLengthString和hash两种点ID类型。  - fixedLengthString：固定长度String格式下，实际点ID直接用于内部存储与计算，用户需指定一长度，实际点ID不可超过此长度。长度过大，可能影响查询性能，建议用户根据数据集状态进行设置。  - hash：哈希格式下，内部计算时将实际点ID转换成哈希码进行存储与计算，对实际点ID长度无限制，但是存在极低的概率(约10^(-43))出现点ID碰撞。若用户无法确定点ID的最大长度，建议选择哈希类型。
        :type id_type: str
        :param id_length: 当id_type取值为fixedLengthString时必填，取值范围：1-128。
        :type id_length: int
        """
        
        

        self._id_type = None
        self._id_length = None
        self.discriminator = None

        self.id_type = id_type
        if id_length is not None:
            self.id_length = id_length

    @property
    def id_type(self):
        r"""Gets the id_type of this ListGraphsRespVertexIdType.

        id类型，目前支持固定长度fixedLengthString和hash两种点ID类型。  - fixedLengthString：固定长度String格式下，实际点ID直接用于内部存储与计算，用户需指定一长度，实际点ID不可超过此长度。长度过大，可能影响查询性能，建议用户根据数据集状态进行设置。  - hash：哈希格式下，内部计算时将实际点ID转换成哈希码进行存储与计算，对实际点ID长度无限制，但是存在极低的概率(约10^(-43))出现点ID碰撞。若用户无法确定点ID的最大长度，建议选择哈希类型。

        :return: The id_type of this ListGraphsRespVertexIdType.
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        r"""Sets the id_type of this ListGraphsRespVertexIdType.

        id类型，目前支持固定长度fixedLengthString和hash两种点ID类型。  - fixedLengthString：固定长度String格式下，实际点ID直接用于内部存储与计算，用户需指定一长度，实际点ID不可超过此长度。长度过大，可能影响查询性能，建议用户根据数据集状态进行设置。  - hash：哈希格式下，内部计算时将实际点ID转换成哈希码进行存储与计算，对实际点ID长度无限制，但是存在极低的概率(约10^(-43))出现点ID碰撞。若用户无法确定点ID的最大长度，建议选择哈希类型。

        :param id_type: The id_type of this ListGraphsRespVertexIdType.
        :type id_type: str
        """
        self._id_type = id_type

    @property
    def id_length(self):
        r"""Gets the id_length of this ListGraphsRespVertexIdType.

        当id_type取值为fixedLengthString时必填，取值范围：1-128。

        :return: The id_length of this ListGraphsRespVertexIdType.
        :rtype: int
        """
        return self._id_length

    @id_length.setter
    def id_length(self, id_length):
        r"""Sets the id_length of this ListGraphsRespVertexIdType.

        当id_type取值为fixedLengthString时必填，取值范围：1-128。

        :param id_length: The id_length of this ListGraphsRespVertexIdType.
        :type id_length: int
        """
        self._id_length = id_length

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
        if not isinstance(other, ListGraphsRespVertexIdType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
