# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlterDatasetInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'dataset_format': 'DatasetFileFormat',
        'properties': 'dict(str, str)'
    }

    attribute_map = {
        'description': 'description',
        'dataset_format': 'dataset_format',
        'properties': 'properties'
    }

    def __init__(self, description=None, dataset_format=None, properties=None):
        r"""AlterDatasetInput

        The model defined in huaweicloud sdk

        :param description: 数据集的描述信息
        :type description: str
        :param dataset_format: 
        :type dataset_format: :class:`huaweicloudsdklakeformation.v1.DatasetFileFormat`
        :param properties: 数据集其他属性
        :type properties: dict(str, str)
        """
        
        

        self._description = None
        self._dataset_format = None
        self._properties = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if dataset_format is not None:
            self.dataset_format = dataset_format
        if properties is not None:
            self.properties = properties

    @property
    def description(self):
        r"""Gets the description of this AlterDatasetInput.

        数据集的描述信息

        :return: The description of this AlterDatasetInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlterDatasetInput.

        数据集的描述信息

        :param description: The description of this AlterDatasetInput.
        :type description: str
        """
        self._description = description

    @property
    def dataset_format(self):
        r"""Gets the dataset_format of this AlterDatasetInput.

        :return: The dataset_format of this AlterDatasetInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.DatasetFileFormat`
        """
        return self._dataset_format

    @dataset_format.setter
    def dataset_format(self, dataset_format):
        r"""Sets the dataset_format of this AlterDatasetInput.

        :param dataset_format: The dataset_format of this AlterDatasetInput.
        :type dataset_format: :class:`huaweicloudsdklakeformation.v1.DatasetFileFormat`
        """
        self._dataset_format = dataset_format

    @property
    def properties(self):
        r"""Gets the properties of this AlterDatasetInput.

        数据集其他属性

        :return: The properties of this AlterDatasetInput.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this AlterDatasetInput.

        数据集其他属性

        :param properties: The properties of this AlterDatasetInput.
        :type properties: dict(str, str)
        """
        self._properties = properties

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
        if not isinstance(other, AlterDatasetInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
