# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBatchCreateRecordSetsTaskErrorItem:

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
        'type': 'str',
        'line': 'str',
        'ttl': 'int',
        'weight': 'int',
        'records': 'list[str]',
        'status': 'str',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'line': 'line',
        'ttl': 'ttl',
        'weight': 'weight',
        'records': 'records',
        'status': 'status',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, name=None, type=None, line=None, ttl=None, weight=None, records=None, status=None, error_code=None, error_message=None):
        r"""ShowBatchCreateRecordSetsTaskErrorItem

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 域名。 **取值范围：** 不涉及。
        :type name: str
        :param type: **参数解释：** 记录集的类型。 **取值范围：** - 公网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、NS、CAA、REDIRECT_URL、FORWARD_URL。 - 内网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、PTR。
        :type type: str
        :param line: **参数解释：** 解析线路ID。 **取值范围：** 不涉及。
        :type line: str
        :param ttl: **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **取值范围：** 1~2147483647。
        :type ttl: int
        :param weight: **参数解释：** 解析记录的权重。 **取值范围：** 0~1000。
        :type weight: int
        :param records: **参数解释：** 域名解析后的值。 **取值范围：** 不涉及。
        :type records: list[str]
        :param status: **参数解释：** 记录集状态。 **取值范围：** - ERROR：失败
        :type status: str
        :param error_code: **参数解释：** 错误码。 **取值范围：** 不涉及。
        :type error_code: str
        :param error_message: **参数解释：** 错误信息。 **取值范围：** 不涉及。
        :type error_message: str
        """
        
        

        self._name = None
        self._type = None
        self._line = None
        self._ttl = None
        self._weight = None
        self._records = None
        self._status = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if line is not None:
            self.line = line
        if ttl is not None:
            self.ttl = ttl
        if weight is not None:
            self.weight = weight
        if records is not None:
            self.records = records
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def name(self):
        r"""Gets the name of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 域名。 **取值范围：** 不涉及。

        :return: The name of this ShowBatchCreateRecordSetsTaskErrorItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 域名。 **取值范围：** 不涉及。

        :param name: The name of this ShowBatchCreateRecordSetsTaskErrorItem.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 记录集的类型。 **取值范围：** - 公网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、NS、CAA、REDIRECT_URL、FORWARD_URL。 - 内网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、PTR。

        :return: The type of this ShowBatchCreateRecordSetsTaskErrorItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 记录集的类型。 **取值范围：** - 公网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、NS、CAA、REDIRECT_URL、FORWARD_URL。 - 内网域名的记录类型: A、CNAME、MX、AAAA、TXT、SRV、PTR。

        :param type: The type of this ShowBatchCreateRecordSetsTaskErrorItem.
        :type type: str
        """
        self._type = type

    @property
    def line(self):
        r"""Gets the line of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 解析线路ID。 **取值范围：** 不涉及。

        :return: The line of this ShowBatchCreateRecordSetsTaskErrorItem.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 解析线路ID。 **取值范围：** 不涉及。

        :param line: The line of this ShowBatchCreateRecordSetsTaskErrorItem.
        :type line: str
        """
        self._line = line

    @property
    def ttl(self):
        r"""Gets the ttl of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **取值范围：** 1~2147483647。

        :return: The ttl of this ShowBatchCreateRecordSetsTaskErrorItem.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。 **取值范围：** 1~2147483647。

        :param ttl: The ttl of this ShowBatchCreateRecordSetsTaskErrorItem.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def weight(self):
        r"""Gets the weight of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 解析记录的权重。 **取值范围：** 0~1000。

        :return: The weight of this ShowBatchCreateRecordSetsTaskErrorItem.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 解析记录的权重。 **取值范围：** 0~1000。

        :param weight: The weight of this ShowBatchCreateRecordSetsTaskErrorItem.
        :type weight: int
        """
        self._weight = weight

    @property
    def records(self):
        r"""Gets the records of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 域名解析后的值。 **取值范围：** 不涉及。

        :return: The records of this ShowBatchCreateRecordSetsTaskErrorItem.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 域名解析后的值。 **取值范围：** 不涉及。

        :param records: The records of this ShowBatchCreateRecordSetsTaskErrorItem.
        :type records: list[str]
        """
        self._records = records

    @property
    def status(self):
        r"""Gets the status of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 记录集状态。 **取值范围：** - ERROR：失败

        :return: The status of this ShowBatchCreateRecordSetsTaskErrorItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 记录集状态。 **取值范围：** - ERROR：失败

        :param status: The status of this ShowBatchCreateRecordSetsTaskErrorItem.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        r"""Gets the error_code of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 错误码。 **取值范围：** 不涉及。

        :return: The error_code of this ShowBatchCreateRecordSetsTaskErrorItem.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 错误码。 **取值范围：** 不涉及。

        :param error_code: The error_code of this ShowBatchCreateRecordSetsTaskErrorItem.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 错误信息。 **取值范围：** 不涉及。

        :return: The error_message of this ShowBatchCreateRecordSetsTaskErrorItem.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ShowBatchCreateRecordSetsTaskErrorItem.

        **参数解释：** 错误信息。 **取值范围：** 不涉及。

        :param error_message: The error_message of this ShowBatchCreateRecordSetsTaskErrorItem.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, ShowBatchCreateRecordSetsTaskErrorItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
