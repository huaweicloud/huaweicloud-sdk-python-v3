# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRecordSetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'ttl': 'int',
        'records': 'list[str]',
        'line': 'str',
        'weight': 'int',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'ttl': 'ttl',
        'records': 'records',
        'line': 'line',
        'weight': 'weight',
        'type': 'type'
    }

    def __init__(self, name=None, ttl=None, records=None, line=None, weight=None, type=None):
        r"""CreateRecordSetRequestBody

        The model defined in huaweicloud sdk

        :param name: 域名，后缀需以zone name结束且为FQDN（即以“.”号结束的完整主机名）
        :type name: str
        :param ttl: 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位
        :type ttl: int
        :param records: 解析记录的值，不同类型解析记录对应的值的规则不同
        :type records: list[str]
        :param line: 解析线路ID
        :type line: str
        :param weight: 解析记录的权重
        :type weight: int
        :param type: Record Set的类型， 取值范围：A、CNAME
        :type type: str
        """
        
        

        self._name = None
        self._ttl = None
        self._records = None
        self._line = None
        self._weight = None
        self._type = None
        self.discriminator = None

        self.name = name
        self.ttl = ttl
        if records is not None:
            self.records = records
        self.line = line
        if weight is not None:
            self.weight = weight
        if type is not None:
            self.type = type

    @property
    def name(self):
        r"""Gets the name of this CreateRecordSetRequestBody.

        域名，后缀需以zone name结束且为FQDN（即以“.”号结束的完整主机名）

        :return: The name of this CreateRecordSetRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateRecordSetRequestBody.

        域名，后缀需以zone name结束且为FQDN（即以“.”号结束的完整主机名）

        :param name: The name of this CreateRecordSetRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def ttl(self):
        r"""Gets the ttl of this CreateRecordSetRequestBody.

        解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位

        :return: The ttl of this CreateRecordSetRequestBody.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this CreateRecordSetRequestBody.

        解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位

        :param ttl: The ttl of this CreateRecordSetRequestBody.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def records(self):
        r"""Gets the records of this CreateRecordSetRequestBody.

        解析记录的值，不同类型解析记录对应的值的规则不同

        :return: The records of this CreateRecordSetRequestBody.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this CreateRecordSetRequestBody.

        解析记录的值，不同类型解析记录对应的值的规则不同

        :param records: The records of this CreateRecordSetRequestBody.
        :type records: list[str]
        """
        self._records = records

    @property
    def line(self):
        r"""Gets the line of this CreateRecordSetRequestBody.

        解析线路ID

        :return: The line of this CreateRecordSetRequestBody.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this CreateRecordSetRequestBody.

        解析线路ID

        :param line: The line of this CreateRecordSetRequestBody.
        :type line: str
        """
        self._line = line

    @property
    def weight(self):
        r"""Gets the weight of this CreateRecordSetRequestBody.

        解析记录的权重

        :return: The weight of this CreateRecordSetRequestBody.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this CreateRecordSetRequestBody.

        解析记录的权重

        :param weight: The weight of this CreateRecordSetRequestBody.
        :type weight: int
        """
        self._weight = weight

    @property
    def type(self):
        r"""Gets the type of this CreateRecordSetRequestBody.

        Record Set的类型， 取值范围：A、CNAME

        :return: The type of this CreateRecordSetRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateRecordSetRequestBody.

        Record Set的类型， 取值范围：A、CNAME

        :param type: The type of this CreateRecordSetRequestBody.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, CreateRecordSetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
