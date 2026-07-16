# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAutoSearchTrialsItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'header': 'list[str]',
        'data': 'list[list[str]]'
    }

    attribute_map = {
        'header': 'header',
        'data': 'data'
    }

    def __init__(self, header=None, data=None):
        r"""ListAutoSearchTrialsItems

        The model defined in huaweicloud sdk

        :param header: 超参搜索所有trial结果的字段信息。
        :type header: list[str]
        :param data: 超参搜索所有trial结果的每条数据列表。
        :type data: list[list[str]]
        """
        
        

        self._header = None
        self._data = None
        self.discriminator = None

        if header is not None:
            self.header = header
        if data is not None:
            self.data = data

    @property
    def header(self):
        r"""Gets the header of this ListAutoSearchTrialsItems.

        超参搜索所有trial结果的字段信息。

        :return: The header of this ListAutoSearchTrialsItems.
        :rtype: list[str]
        """
        return self._header

    @header.setter
    def header(self, header):
        r"""Sets the header of this ListAutoSearchTrialsItems.

        超参搜索所有trial结果的字段信息。

        :param header: The header of this ListAutoSearchTrialsItems.
        :type header: list[str]
        """
        self._header = header

    @property
    def data(self):
        r"""Gets the data of this ListAutoSearchTrialsItems.

        超参搜索所有trial结果的每条数据列表。

        :return: The data of this ListAutoSearchTrialsItems.
        :rtype: list[list[str]]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListAutoSearchTrialsItems.

        超参搜索所有trial结果的每条数据列表。

        :param data: The data of this ListAutoSearchTrialsItems.
        :type data: list[list[str]]
        """
        self._data = data

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
        if not isinstance(other, ListAutoSearchTrialsItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
