# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RowPairDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'before_row': 'object',
        'after_row': 'object'
    }

    attribute_map = {
        'before_row': 'before_row',
        'after_row': 'after_row'
    }

    def __init__(self, before_row=None, after_row=None):
        r"""RowPairDto

        The model defined in huaweicloud sdk

        :param before_row: 变更前的行数据
        :type before_row: object
        :param after_row: 变更后的行数据
        :type after_row: object
        """
        
        

        self._before_row = None
        self._after_row = None
        self.discriminator = None

        if before_row is not None:
            self.before_row = before_row
        if after_row is not None:
            self.after_row = after_row

    @property
    def before_row(self):
        r"""Gets the before_row of this RowPairDto.

        变更前的行数据

        :return: The before_row of this RowPairDto.
        :rtype: object
        """
        return self._before_row

    @before_row.setter
    def before_row(self, before_row):
        r"""Sets the before_row of this RowPairDto.

        变更前的行数据

        :param before_row: The before_row of this RowPairDto.
        :type before_row: object
        """
        self._before_row = before_row

    @property
    def after_row(self):
        r"""Gets the after_row of this RowPairDto.

        变更后的行数据

        :return: The after_row of this RowPairDto.
        :rtype: object
        """
        return self._after_row

    @after_row.setter
    def after_row(self, after_row):
        r"""Sets the after_row of this RowPairDto.

        变更后的行数据

        :param after_row: The after_row of this RowPairDto.
        :type after_row: object
        """
        self._after_row = after_row

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
        if not isinstance(other, RowPairDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
