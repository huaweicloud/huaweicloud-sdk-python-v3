# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowStepMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'key': 'str',
        'title': 'str',
        'type': 'str',
        'data': 'dict(str, object)'
    }

    attribute_map = {
        'created_at': 'created_at',
        'key': 'key',
        'title': 'title',
        'type': 'type',
        'data': 'data'
    }

    def __init__(self, created_at=None, key=None, title=None, type=None, data=None):
        r"""WorkflowStepMetric

        The model defined in huaweicloud sdk

        :param created_at: 创建时间。
        :type created_at: str
        :param key: 度量项。
        :type key: str
        :param title: 度量标题。
        :type title: str
        :param type: 度量的类型。
        :type type: str
        :param data: 度量数据。
        :type data: dict(str, object)
        """
        
        

        self._created_at = None
        self._key = None
        self._title = None
        self._type = None
        self._data = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if key is not None:
            self.key = key
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if data is not None:
            self.data = data

    @property
    def created_at(self):
        r"""Gets the created_at of this WorkflowStepMetric.

        创建时间。

        :return: The created_at of this WorkflowStepMetric.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this WorkflowStepMetric.

        创建时间。

        :param created_at: The created_at of this WorkflowStepMetric.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def key(self):
        r"""Gets the key of this WorkflowStepMetric.

        度量项。

        :return: The key of this WorkflowStepMetric.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this WorkflowStepMetric.

        度量项。

        :param key: The key of this WorkflowStepMetric.
        :type key: str
        """
        self._key = key

    @property
    def title(self):
        r"""Gets the title of this WorkflowStepMetric.

        度量标题。

        :return: The title of this WorkflowStepMetric.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this WorkflowStepMetric.

        度量标题。

        :param title: The title of this WorkflowStepMetric.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this WorkflowStepMetric.

        度量的类型。

        :return: The type of this WorkflowStepMetric.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this WorkflowStepMetric.

        度量的类型。

        :param type: The type of this WorkflowStepMetric.
        :type type: str
        """
        self._type = type

    @property
    def data(self):
        r"""Gets the data of this WorkflowStepMetric.

        度量数据。

        :return: The data of this WorkflowStepMetric.
        :rtype: dict(str, object)
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this WorkflowStepMetric.

        度量数据。

        :param data: The data of this WorkflowStepMetric.
        :type data: dict(str, object)
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
        if not isinstance(other, WorkflowStepMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
