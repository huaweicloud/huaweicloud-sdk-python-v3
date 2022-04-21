# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRecordSetReq:

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
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'status': 'status',
        'ttl': 'ttl',
        'records': 'records',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, type=None, status=None, ttl=None, records=None, tags=None):
        """CreateRecordSetReq

        The model defined in huaweicloud sdk

        :param name: 域名，后缀需以zone name结束且为FQDN（即以“.”号结束的完整主机名）。
        :type name: str
        :param description: 
        :type description: str
        :param type: Record Set的类型。  取值范围：A、AAAA、MX、CNAME、TXT、NS、SRV、CAA。
        :type type: str
        :param status: 
        :type status: str
        :param ttl: 
        :type ttl: int
        :param records: 解析记录的值。不同类型解析记录对应的值的规则不同。
        :type records: list[str]
        :param tags: 资源标签。
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._status = None
        self._ttl = None
        self._records = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        if status is not None:
            self.status = status
        if ttl is not None:
            self.ttl = ttl
        self.records = records
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateRecordSetReq.

        域名，后缀需以zone name结束且为FQDN（即以“.”号结束的完整主机名）。

        :return: The name of this CreateRecordSetReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRecordSetReq.

        域名，后缀需以zone name结束且为FQDN（即以“.”号结束的完整主机名）。

        :param name: The name of this CreateRecordSetReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateRecordSetReq.


        :return: The description of this CreateRecordSetReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRecordSetReq.


        :param description: The description of this CreateRecordSetReq.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this CreateRecordSetReq.

        Record Set的类型。  取值范围：A、AAAA、MX、CNAME、TXT、NS、SRV、CAA。

        :return: The type of this CreateRecordSetReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateRecordSetReq.

        Record Set的类型。  取值范围：A、AAAA、MX、CNAME、TXT、NS、SRV、CAA。

        :param type: The type of this CreateRecordSetReq.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this CreateRecordSetReq.


        :return: The status of this CreateRecordSetReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateRecordSetReq.


        :param status: The status of this CreateRecordSetReq.
        :type status: str
        """
        self._status = status

    @property
    def ttl(self):
        """Gets the ttl of this CreateRecordSetReq.


        :return: The ttl of this CreateRecordSetReq.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this CreateRecordSetReq.


        :param ttl: The ttl of this CreateRecordSetReq.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def records(self):
        """Gets the records of this CreateRecordSetReq.

        解析记录的值。不同类型解析记录对应的值的规则不同。

        :return: The records of this CreateRecordSetReq.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this CreateRecordSetReq.

        解析记录的值。不同类型解析记录对应的值的规则不同。

        :param records: The records of this CreateRecordSetReq.
        :type records: list[str]
        """
        self._records = records

    @property
    def tags(self):
        """Gets the tags of this CreateRecordSetReq.

        资源标签。

        :return: The tags of this CreateRecordSetReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateRecordSetReq.

        资源标签。

        :param tags: The tags of this CreateRecordSetReq.
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateRecordSetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
