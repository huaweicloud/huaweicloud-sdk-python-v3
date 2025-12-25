# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsapResourceDisplaySetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'columns': 'list[IsapResourceDisplaySettingColumns]',
        'format': 'str'
    }

    attribute_map = {
        'columns': 'columns',
        'format': 'format'
    }

    def __init__(self, columns=None, format=None):
        r"""IsapResourceDisplaySetting

        The model defined in huaweicloud sdk

        :param columns: 列
        :type columns: list[:class:`huaweicloudsdksecmaster.v1.IsapResourceDisplaySettingColumns`]
        :param format: 显示格式，例如 TABLE
        :type format: str
        """
        
        

        self._columns = None
        self._format = None
        self.discriminator = None

        if columns is not None:
            self.columns = columns
        if format is not None:
            self.format = format

    @property
    def columns(self):
        r"""Gets the columns of this IsapResourceDisplaySetting.

        列

        :return: The columns of this IsapResourceDisplaySetting.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.IsapResourceDisplaySettingColumns`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this IsapResourceDisplaySetting.

        列

        :param columns: The columns of this IsapResourceDisplaySetting.
        :type columns: list[:class:`huaweicloudsdksecmaster.v1.IsapResourceDisplaySettingColumns`]
        """
        self._columns = columns

    @property
    def format(self):
        r"""Gets the format of this IsapResourceDisplaySetting.

        显示格式，例如 TABLE

        :return: The format of this IsapResourceDisplaySetting.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this IsapResourceDisplaySetting.

        显示格式，例如 TABLE

        :param format: The format of this IsapResourceDisplaySetting.
        :type format: str
        """
        self._format = format

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
        if not isinstance(other, IsapResourceDisplaySetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
