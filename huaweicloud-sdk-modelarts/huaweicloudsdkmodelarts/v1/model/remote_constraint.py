# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoteConstraint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_type': 'str',
        'attributes': 'list[dict(str, str)]'
    }

    attribute_map = {
        'data_type': 'data_type',
        'attributes': 'attributes'
    }

    def __init__(self, data_type=None, attributes=None):
        r"""RemoteConstraint

        The model defined in huaweicloud sdk

        :param data_type: 数据输入类型，支持数据存储位置（OBS）、ModelArts数据集两种方式。
        :type data_type: str
        :param attributes: 数据输入为数据集时的相关属性。枚举值：   - data_format：数据格式。   - data_segmentation：数据切分方式。   - dataset_type：标注类型。
        :type attributes: list[dict(str, str)]
        """
        
        

        self._data_type = None
        self._attributes = None
        self.discriminator = None

        if data_type is not None:
            self.data_type = data_type
        if attributes is not None:
            self.attributes = attributes

    @property
    def data_type(self):
        r"""Gets the data_type of this RemoteConstraint.

        数据输入类型，支持数据存储位置（OBS）、ModelArts数据集两种方式。

        :return: The data_type of this RemoteConstraint.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this RemoteConstraint.

        数据输入类型，支持数据存储位置（OBS）、ModelArts数据集两种方式。

        :param data_type: The data_type of this RemoteConstraint.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def attributes(self):
        r"""Gets the attributes of this RemoteConstraint.

        数据输入为数据集时的相关属性。枚举值：   - data_format：数据格式。   - data_segmentation：数据切分方式。   - dataset_type：标注类型。

        :return: The attributes of this RemoteConstraint.
        :rtype: list[dict(str, str)]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this RemoteConstraint.

        数据输入为数据集时的相关属性。枚举值：   - data_format：数据格式。   - data_segmentation：数据切分方式。   - dataset_type：标注类型。

        :param attributes: The attributes of this RemoteConstraint.
        :type attributes: list[dict(str, str)]
        """
        self._attributes = attributes

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
        if not isinstance(other, RemoteConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
