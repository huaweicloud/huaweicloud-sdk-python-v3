# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudEvents:

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
        'source': 'str',
        'specversion': 'str',
        'type': 'str',
        'datacontenttype': 'str',
        'dataschema': 'str',
        'data': 'object',
        'time': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'id': 'id',
        'source': 'source',
        'specversion': 'specversion',
        'type': 'type',
        'datacontenttype': 'datacontenttype',
        'dataschema': 'dataschema',
        'data': 'data',
        'time': 'time',
        'subject': 'subject'
    }

    def __init__(self, id=None, source=None, specversion=None, type=None, datacontenttype=None, dataschema=None, data=None, time=None, subject=None):
        """CloudEvents

        The model defined in huaweicloud sdk

        :param id: 事件唯一标识串，同一个事件来源里必须唯一
        :type id: str
        :param source: 事件来源上下文标识串，source+id可以唯一确定一个事件。采用URI-Reference格式，参考https://tools.ietf.org/html/rfc3986#section-4.1
        :type source: str
        :param specversion: CloudEvents协议版本，格式为major.minor
        :type specversion: str
        :param type: 事件类型
        :type type: str
        :param datacontenttype: 事件内容格式，采用MIME格式，遵循RFC2046，参考https://tools.ietf.org/html/rfc2046
        :type datacontenttype: str
        :param dataschema: 事件内容模型定义的URI，遵循RFC3986，参考https://tools.ietf.org/html/rfc3986#section-4.3
        :type dataschema: str
        :param data: 事件的负载内容，采用datacontenttype字段指定的格式，内容字段遵循dataschema字段的描述
        :type data: object
        :param time: 事件发生UTC日期时间，相同来源的事件格式相同，遵循RFC3339，格式需满足2018-04-05T17:31:00Z，参考https://tools.ietf.org/html/rfc3339
        :type time: str
        :param subject: 事件发生的主题或对象，用以标识哪个具体对象发生了当前事件
        :type subject: str
        """
        
        

        self._id = None
        self._source = None
        self._specversion = None
        self._type = None
        self._datacontenttype = None
        self._dataschema = None
        self._data = None
        self._time = None
        self._subject = None
        self.discriminator = None

        self.id = id
        self.source = source
        self.specversion = specversion
        self.type = type
        if datacontenttype is not None:
            self.datacontenttype = datacontenttype
        if dataschema is not None:
            self.dataschema = dataschema
        if data is not None:
            self.data = data
        if time is not None:
            self.time = time
        if subject is not None:
            self.subject = subject

    @property
    def id(self):
        """Gets the id of this CloudEvents.

        事件唯一标识串，同一个事件来源里必须唯一

        :return: The id of this CloudEvents.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudEvents.

        事件唯一标识串，同一个事件来源里必须唯一

        :param id: The id of this CloudEvents.
        :type id: str
        """
        self._id = id

    @property
    def source(self):
        """Gets the source of this CloudEvents.

        事件来源上下文标识串，source+id可以唯一确定一个事件。采用URI-Reference格式，参考https://tools.ietf.org/html/rfc3986#section-4.1

        :return: The source of this CloudEvents.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CloudEvents.

        事件来源上下文标识串，source+id可以唯一确定一个事件。采用URI-Reference格式，参考https://tools.ietf.org/html/rfc3986#section-4.1

        :param source: The source of this CloudEvents.
        :type source: str
        """
        self._source = source

    @property
    def specversion(self):
        """Gets the specversion of this CloudEvents.

        CloudEvents协议版本，格式为major.minor

        :return: The specversion of this CloudEvents.
        :rtype: str
        """
        return self._specversion

    @specversion.setter
    def specversion(self, specversion):
        """Sets the specversion of this CloudEvents.

        CloudEvents协议版本，格式为major.minor

        :param specversion: The specversion of this CloudEvents.
        :type specversion: str
        """
        self._specversion = specversion

    @property
    def type(self):
        """Gets the type of this CloudEvents.

        事件类型

        :return: The type of this CloudEvents.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudEvents.

        事件类型

        :param type: The type of this CloudEvents.
        :type type: str
        """
        self._type = type

    @property
    def datacontenttype(self):
        """Gets the datacontenttype of this CloudEvents.

        事件内容格式，采用MIME格式，遵循RFC2046，参考https://tools.ietf.org/html/rfc2046

        :return: The datacontenttype of this CloudEvents.
        :rtype: str
        """
        return self._datacontenttype

    @datacontenttype.setter
    def datacontenttype(self, datacontenttype):
        """Sets the datacontenttype of this CloudEvents.

        事件内容格式，采用MIME格式，遵循RFC2046，参考https://tools.ietf.org/html/rfc2046

        :param datacontenttype: The datacontenttype of this CloudEvents.
        :type datacontenttype: str
        """
        self._datacontenttype = datacontenttype

    @property
    def dataschema(self):
        """Gets the dataschema of this CloudEvents.

        事件内容模型定义的URI，遵循RFC3986，参考https://tools.ietf.org/html/rfc3986#section-4.3

        :return: The dataschema of this CloudEvents.
        :rtype: str
        """
        return self._dataschema

    @dataschema.setter
    def dataschema(self, dataschema):
        """Sets the dataschema of this CloudEvents.

        事件内容模型定义的URI，遵循RFC3986，参考https://tools.ietf.org/html/rfc3986#section-4.3

        :param dataschema: The dataschema of this CloudEvents.
        :type dataschema: str
        """
        self._dataschema = dataschema

    @property
    def data(self):
        """Gets the data of this CloudEvents.

        事件的负载内容，采用datacontenttype字段指定的格式，内容字段遵循dataschema字段的描述

        :return: The data of this CloudEvents.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CloudEvents.

        事件的负载内容，采用datacontenttype字段指定的格式，内容字段遵循dataschema字段的描述

        :param data: The data of this CloudEvents.
        :type data: object
        """
        self._data = data

    @property
    def time(self):
        """Gets the time of this CloudEvents.

        事件发生UTC日期时间，相同来源的事件格式相同，遵循RFC3339，格式需满足2018-04-05T17:31:00Z，参考https://tools.ietf.org/html/rfc3339

        :return: The time of this CloudEvents.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this CloudEvents.

        事件发生UTC日期时间，相同来源的事件格式相同，遵循RFC3339，格式需满足2018-04-05T17:31:00Z，参考https://tools.ietf.org/html/rfc3339

        :param time: The time of this CloudEvents.
        :type time: str
        """
        self._time = time

    @property
    def subject(self):
        """Gets the subject of this CloudEvents.

        事件发生的主题或对象，用以标识哪个具体对象发生了当前事件

        :return: The subject of this CloudEvents.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CloudEvents.

        事件发生的主题或对象，用以标识哪个具体对象发生了当前事件

        :param subject: The subject of this CloudEvents.
        :type subject: str
        """
        self._subject = subject

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
        if not isinstance(other, CloudEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
