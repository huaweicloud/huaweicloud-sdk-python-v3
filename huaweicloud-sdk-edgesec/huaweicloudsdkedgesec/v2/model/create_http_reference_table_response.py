# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHttpReferenceTableResponse(SdkResponse):

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
        'type': 'str',
        'description': 'str',
        'timestamp': 'int',
        'values': 'list[str]',
        'producer': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'timestamp': 'timestamp',
        'values': 'values',
        'producer': 'producer'
    }

    def __init__(self, id=None, name=None, type=None, description=None, timestamp=None, values=None, producer=None):
        r"""CreateHttpReferenceTableResponse

        The model defined in huaweicloud sdk

        :param id: 引用表id
        :type id: str
        :param name: 引用表名称
        :type name: str
        :param type: 引用表类型
        :type type: str
        :param description: 引用表描述
        :type description: str
        :param timestamp: 引用表时间戳
        :type timestamp: int
        :param values: 引用表的值
        :type values: list[str]
        :param producer: 创建来源
        :type producer: int
        """
        
        super(CreateHttpReferenceTableResponse, self).__init__()

        self._id = None
        self._name = None
        self._type = None
        self._description = None
        self._timestamp = None
        self._values = None
        self._producer = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if timestamp is not None:
            self.timestamp = timestamp
        if values is not None:
            self.values = values
        if producer is not None:
            self.producer = producer

    @property
    def id(self):
        r"""Gets the id of this CreateHttpReferenceTableResponse.

        引用表id

        :return: The id of this CreateHttpReferenceTableResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateHttpReferenceTableResponse.

        引用表id

        :param id: The id of this CreateHttpReferenceTableResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateHttpReferenceTableResponse.

        引用表名称

        :return: The name of this CreateHttpReferenceTableResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateHttpReferenceTableResponse.

        引用表名称

        :param name: The name of this CreateHttpReferenceTableResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CreateHttpReferenceTableResponse.

        引用表类型

        :return: The type of this CreateHttpReferenceTableResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateHttpReferenceTableResponse.

        引用表类型

        :param type: The type of this CreateHttpReferenceTableResponse.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this CreateHttpReferenceTableResponse.

        引用表描述

        :return: The description of this CreateHttpReferenceTableResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateHttpReferenceTableResponse.

        引用表描述

        :param description: The description of this CreateHttpReferenceTableResponse.
        :type description: str
        """
        self._description = description

    @property
    def timestamp(self):
        r"""Gets the timestamp of this CreateHttpReferenceTableResponse.

        引用表时间戳

        :return: The timestamp of this CreateHttpReferenceTableResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this CreateHttpReferenceTableResponse.

        引用表时间戳

        :param timestamp: The timestamp of this CreateHttpReferenceTableResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def values(self):
        r"""Gets the values of this CreateHttpReferenceTableResponse.

        引用表的值

        :return: The values of this CreateHttpReferenceTableResponse.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this CreateHttpReferenceTableResponse.

        引用表的值

        :param values: The values of this CreateHttpReferenceTableResponse.
        :type values: list[str]
        """
        self._values = values

    @property
    def producer(self):
        r"""Gets the producer of this CreateHttpReferenceTableResponse.

        创建来源

        :return: The producer of this CreateHttpReferenceTableResponse.
        :rtype: int
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        r"""Sets the producer of this CreateHttpReferenceTableResponse.

        创建来源

        :param producer: The producer of this CreateHttpReferenceTableResponse.
        :type producer: int
        """
        self._producer = producer

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
        if not isinstance(other, CreateHttpReferenceTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
