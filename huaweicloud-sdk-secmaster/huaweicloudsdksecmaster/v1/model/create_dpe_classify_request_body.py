# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDpeClassifyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'dataclass_id': 'str',
        'data_source': 'str',
        'description': 'str',
        'classifier': 'DpeClassifyCreate'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'dataclass_id': 'dataclass_id',
        'data_source': 'data_source',
        'description': 'description',
        'classifier': 'classifier'
    }

    def __init__(self, id=None, name=None, dataclass_id=None, data_source=None, description=None, classifier=None):
        r"""CreateDpeClassifyRequestBody

        The model defined in huaweicloud sdk

        :param id: 映射id
        :type id: str
        :param name: 名称
        :type name: str
        :param dataclass_id: 映射id
        :type dataclass_id: str
        :param data_source: 数据源
        :type data_source: str
        :param description: 描述信息
        :type description: str
        :param classifier: 
        :type classifier: :class:`huaweicloudsdksecmaster.v1.DpeClassifyCreate`
        """
        
        

        self._id = None
        self._name = None
        self._dataclass_id = None
        self._data_source = None
        self._description = None
        self._classifier = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.dataclass_id = dataclass_id
        self.data_source = data_source
        self.description = description
        self.classifier = classifier

    @property
    def id(self):
        r"""Gets the id of this CreateDpeClassifyRequestBody.

        映射id

        :return: The id of this CreateDpeClassifyRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateDpeClassifyRequestBody.

        映射id

        :param id: The id of this CreateDpeClassifyRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateDpeClassifyRequestBody.

        名称

        :return: The name of this CreateDpeClassifyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDpeClassifyRequestBody.

        名称

        :param name: The name of this CreateDpeClassifyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this CreateDpeClassifyRequestBody.

        映射id

        :return: The dataclass_id of this CreateDpeClassifyRequestBody.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this CreateDpeClassifyRequestBody.

        映射id

        :param dataclass_id: The dataclass_id of this CreateDpeClassifyRequestBody.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def data_source(self):
        r"""Gets the data_source of this CreateDpeClassifyRequestBody.

        数据源

        :return: The data_source of this CreateDpeClassifyRequestBody.
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        r"""Sets the data_source of this CreateDpeClassifyRequestBody.

        数据源

        :param data_source: The data_source of this CreateDpeClassifyRequestBody.
        :type data_source: str
        """
        self._data_source = data_source

    @property
    def description(self):
        r"""Gets the description of this CreateDpeClassifyRequestBody.

        描述信息

        :return: The description of this CreateDpeClassifyRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDpeClassifyRequestBody.

        描述信息

        :param description: The description of this CreateDpeClassifyRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def classifier(self):
        r"""Gets the classifier of this CreateDpeClassifyRequestBody.

        :return: The classifier of this CreateDpeClassifyRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v1.DpeClassifyCreate`
        """
        return self._classifier

    @classifier.setter
    def classifier(self, classifier):
        r"""Sets the classifier of this CreateDpeClassifyRequestBody.

        :param classifier: The classifier of this CreateDpeClassifyRequestBody.
        :type classifier: :class:`huaweicloudsdksecmaster.v1.DpeClassifyCreate`
        """
        self._classifier = classifier

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
        if not isinstance(other, CreateDpeClassifyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
