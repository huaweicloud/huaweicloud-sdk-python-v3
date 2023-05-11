# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticsSourceDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_type': 'str',
        'source_id': 'str'
    }

    attribute_map = {
        'source_type': 'source_type',
        'source_id': 'source_id'
    }

    def __init__(self, source_type=None, source_id=None):
        """StatisticsSourceDTO

        The model defined in huaweicloud sdk

        :param source_type: **参数说明**：信息来源的具体类型描述。
        :type source_type: str
        :param source_id: **参数说明**：信息来源的唯一标识码ID。
        :type source_id: str
        """
        
        

        self._source_type = None
        self._source_id = None
        self.discriminator = None

        if source_type is not None:
            self.source_type = source_type
        if source_id is not None:
            self.source_id = source_id

    @property
    def source_type(self):
        """Gets the source_type of this StatisticsSourceDTO.

        **参数说明**：信息来源的具体类型描述。

        :return: The source_type of this StatisticsSourceDTO.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this StatisticsSourceDTO.

        **参数说明**：信息来源的具体类型描述。

        :param source_type: The source_type of this StatisticsSourceDTO.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_id(self):
        """Gets the source_id of this StatisticsSourceDTO.

        **参数说明**：信息来源的唯一标识码ID。

        :return: The source_id of this StatisticsSourceDTO.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this StatisticsSourceDTO.

        **参数说明**：信息来源的唯一标识码ID。

        :param source_id: The source_id of this StatisticsSourceDTO.
        :type source_id: str
        """
        self._source_id = source_id

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
        if not isinstance(other, StatisticsSourceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
