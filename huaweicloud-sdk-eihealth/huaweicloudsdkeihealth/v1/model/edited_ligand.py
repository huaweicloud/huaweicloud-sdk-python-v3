# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditedLigand:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'format': 'str',
        'data': 'str'
    }

    attribute_map = {
        'source': 'source',
        'format': 'format',
        'data': 'data'
    }

    def __init__(self, source=None, format=None, data=None):
        """EditedLigand

        The model defined in huaweicloud sdk

        :param source: 文件来源，仅支持RAW
        :type source: str
        :param format: 文件格式，仅支持CIF
        :type format: str
        :param data: 文件原始数据，仅数据源为RAW时提供
        :type data: str
        """
        
        

        self._source = None
        self._format = None
        self._data = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if format is not None:
            self.format = format
        self.data = data

    @property
    def source(self):
        """Gets the source of this EditedLigand.

        文件来源，仅支持RAW

        :return: The source of this EditedLigand.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this EditedLigand.

        文件来源，仅支持RAW

        :param source: The source of this EditedLigand.
        :type source: str
        """
        self._source = source

    @property
    def format(self):
        """Gets the format of this EditedLigand.

        文件格式，仅支持CIF

        :return: The format of this EditedLigand.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this EditedLigand.

        文件格式，仅支持CIF

        :param format: The format of this EditedLigand.
        :type format: str
        """
        self._format = format

    @property
    def data(self):
        """Gets the data of this EditedLigand.

        文件原始数据，仅数据源为RAW时提供

        :return: The data of this EditedLigand.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EditedLigand.

        文件原始数据，仅数据源为RAW时提供

        :param data: The data of this EditedLigand.
        :type data: str
        """
        self._data = data

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
        if not isinstance(other, EditedLigand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
