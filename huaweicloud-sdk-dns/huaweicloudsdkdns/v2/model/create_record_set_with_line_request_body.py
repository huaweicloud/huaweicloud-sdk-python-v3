# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRecordSetWithLineRequestBody:

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
        'description': 'str',
        'type': 'str',
        'status': 'str',
        'ttl': 'int',
        'records': 'list[str]',
        'line': 'str',
        'tags': 'list[Tag]',
        'weight': 'int',
        'alias_target': 'AliasTarget'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'status': 'status',
        'ttl': 'ttl',
        'records': 'records',
        'line': 'line',
        'tags': 'tags',
        'weight': 'weight',
        'alias_target': 'alias_target'
    }

    def __init__(self, name=None, description=None, type=None, status=None, ttl=None, records=None, line=None, tags=None, weight=None, alias_target=None):
        """CreateRecordSetWithLineRequestBody

        The model defined in huaweicloud sdk

        :param name: 域名，后缀需以zone name结束且为FQDN（即以“.”号结束的完整主机名）。
        :type name: str
        :param description: 可选配置，对域名的描述。
        :type description: str
        :param type: Record Set的类型。
        :type type: str
        :param status: 解析记录的状态。默认值为ENABLE。
        :type status: str
        :param ttl: 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。
        :type ttl: int
        :param records: 解析记录的值。不同类型解析记录对应的值的规则不同。
        :type records: list[str]
        :param line: 解析线路ID
        :type line: str
        :param tags:  资源标签
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        :param weight: 解析记录的权重。
        :type weight: int
        :param alias_target: 
        :type alias_target: :class:`huaweicloudsdkdns.v2.AliasTarget`
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._status = None
        self._ttl = None
        self._records = None
        self._line = None
        self._tags = None
        self._weight = None
        self._alias_target = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        if status is not None:
            self.status = status
        if ttl is not None:
            self.ttl = ttl
        if records is not None:
            self.records = records
        if line is not None:
            self.line = line
        if tags is not None:
            self.tags = tags
        if weight is not None:
            self.weight = weight
        if alias_target is not None:
            self.alias_target = alias_target

    @property
    def name(self):
        """Gets the name of this CreateRecordSetWithLineRequestBody.

        域名，后缀需以zone name结束且为FQDN（即以“.”号结束的完整主机名）。

        :return: The name of this CreateRecordSetWithLineRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRecordSetWithLineRequestBody.

        域名，后缀需以zone name结束且为FQDN（即以“.”号结束的完整主机名）。

        :param name: The name of this CreateRecordSetWithLineRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateRecordSetWithLineRequestBody.

        可选配置，对域名的描述。

        :return: The description of this CreateRecordSetWithLineRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRecordSetWithLineRequestBody.

        可选配置，对域名的描述。

        :param description: The description of this CreateRecordSetWithLineRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this CreateRecordSetWithLineRequestBody.

        Record Set的类型。

        :return: The type of this CreateRecordSetWithLineRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateRecordSetWithLineRequestBody.

        Record Set的类型。

        :param type: The type of this CreateRecordSetWithLineRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this CreateRecordSetWithLineRequestBody.

        解析记录的状态。默认值为ENABLE。

        :return: The status of this CreateRecordSetWithLineRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateRecordSetWithLineRequestBody.

        解析记录的状态。默认值为ENABLE。

        :param status: The status of this CreateRecordSetWithLineRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def ttl(self):
        """Gets the ttl of this CreateRecordSetWithLineRequestBody.

        解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :return: The ttl of this CreateRecordSetWithLineRequestBody.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this CreateRecordSetWithLineRequestBody.

        解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :param ttl: The ttl of this CreateRecordSetWithLineRequestBody.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def records(self):
        """Gets the records of this CreateRecordSetWithLineRequestBody.

        解析记录的值。不同类型解析记录对应的值的规则不同。

        :return: The records of this CreateRecordSetWithLineRequestBody.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this CreateRecordSetWithLineRequestBody.

        解析记录的值。不同类型解析记录对应的值的规则不同。

        :param records: The records of this CreateRecordSetWithLineRequestBody.
        :type records: list[str]
        """
        self._records = records

    @property
    def line(self):
        """Gets the line of this CreateRecordSetWithLineRequestBody.

        解析线路ID

        :return: The line of this CreateRecordSetWithLineRequestBody.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this CreateRecordSetWithLineRequestBody.

        解析线路ID

        :param line: The line of this CreateRecordSetWithLineRequestBody.
        :type line: str
        """
        self._line = line

    @property
    def tags(self):
        """Gets the tags of this CreateRecordSetWithLineRequestBody.

         资源标签

        :return: The tags of this CreateRecordSetWithLineRequestBody.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateRecordSetWithLineRequestBody.

         资源标签

        :param tags: The tags of this CreateRecordSetWithLineRequestBody.
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        self._tags = tags

    @property
    def weight(self):
        """Gets the weight of this CreateRecordSetWithLineRequestBody.

        解析记录的权重。

        :return: The weight of this CreateRecordSetWithLineRequestBody.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CreateRecordSetWithLineRequestBody.

        解析记录的权重。

        :param weight: The weight of this CreateRecordSetWithLineRequestBody.
        :type weight: int
        """
        self._weight = weight

    @property
    def alias_target(self):
        """Gets the alias_target of this CreateRecordSetWithLineRequestBody.

        :return: The alias_target of this CreateRecordSetWithLineRequestBody.
        :rtype: :class:`huaweicloudsdkdns.v2.AliasTarget`
        """
        return self._alias_target

    @alias_target.setter
    def alias_target(self, alias_target):
        """Sets the alias_target of this CreateRecordSetWithLineRequestBody.

        :param alias_target: The alias_target of this CreateRecordSetWithLineRequestBody.
        :type alias_target: :class:`huaweicloudsdkdns.v2.AliasTarget`
        """
        self._alias_target = alias_target

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
        if not isinstance(other, CreateRecordSetWithLineRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
