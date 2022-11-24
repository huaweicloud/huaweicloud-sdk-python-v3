# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThreatIntel:

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
        'indicator_type': 'str',
        'labels': 'str',
        'confidence': 'int',
        'information_source': 'str',
        'severity': 'int',
        'description': 'str',
        'modified': 'datetime',
        'valid_from': 'str',
        'valid_until': 'str',
        'properties': 'ThreatIntelProperties'
    }

    attribute_map = {
        'id': 'id',
        'indicator_type': 'indicator_type',
        'labels': 'labels',
        'confidence': 'confidence',
        'information_source': 'information_source',
        'severity': 'severity',
        'description': 'description',
        'modified': 'modified',
        'valid_from': 'valid_from',
        'valid_until': 'valid_until',
        'properties': 'properties'
    }

    def __init__(self, id=None, indicator_type=None, labels=None, confidence=None, information_source=None, severity=None, description=None, modified=None, valid_from=None, valid_until=None, properties=None):
        """ThreatIntel

        The model defined in huaweicloud sdk

        :param id: 情报Id。
        :type id: str
        :param indicator_type: 威胁情报类型，Domain、Email_Address、Hash_MD5、Hash_SHA1、Hash_SHA256、 Hash_SHA512、IPv4_Address、IPv6_Address、URL。
        :type indicator_type: str
        :param labels: 标签，如&#39;矿池&#39;,&#39;外联&#39;等，\&quot;Directory Scan|Directory Traversal\&quot;。
        :type labels: str
        :param confidence: 置信度，不同来源目前置信度分值定义不一样（分数）。
        :type confidence: int
        :param information_source: 威胁情报源，最大64个字符。
        :type information_source: str
        :param severity: 严重程度，不同渠道定义值不一样（分数）。
        :type severity: int
        :param description: 威胁情报描述。
        :type description: str
        :param modified: 威胁情报的更新时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。
        :type modified: datetime
        :param valid_from: 有效期开始（可读字符串）。
        :type valid_from: str
        :param valid_until: 有效期结束（可读字符串）。
        :type valid_until: str
        :param properties: 
        :type properties: :class:`huaweicloudsdksa.v1.ThreatIntelProperties`
        """
        
        

        self._id = None
        self._indicator_type = None
        self._labels = None
        self._confidence = None
        self._information_source = None
        self._severity = None
        self._description = None
        self._modified = None
        self._valid_from = None
        self._valid_until = None
        self._properties = None
        self.discriminator = None

        self.id = id
        if indicator_type is not None:
            self.indicator_type = indicator_type
        if labels is not None:
            self.labels = labels
        if confidence is not None:
            self.confidence = confidence
        self.information_source = information_source
        if severity is not None:
            self.severity = severity
        self.description = description
        if modified is not None:
            self.modified = modified
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_until is not None:
            self.valid_until = valid_until
        if properties is not None:
            self.properties = properties

    @property
    def id(self):
        """Gets the id of this ThreatIntel.

        情报Id。

        :return: The id of this ThreatIntel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThreatIntel.

        情报Id。

        :param id: The id of this ThreatIntel.
        :type id: str
        """
        self._id = id

    @property
    def indicator_type(self):
        """Gets the indicator_type of this ThreatIntel.

        威胁情报类型，Domain、Email_Address、Hash_MD5、Hash_SHA1、Hash_SHA256、 Hash_SHA512、IPv4_Address、IPv6_Address、URL。

        :return: The indicator_type of this ThreatIntel.
        :rtype: str
        """
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, indicator_type):
        """Sets the indicator_type of this ThreatIntel.

        威胁情报类型，Domain、Email_Address、Hash_MD5、Hash_SHA1、Hash_SHA256、 Hash_SHA512、IPv4_Address、IPv6_Address、URL。

        :param indicator_type: The indicator_type of this ThreatIntel.
        :type indicator_type: str
        """
        self._indicator_type = indicator_type

    @property
    def labels(self):
        """Gets the labels of this ThreatIntel.

        标签，如'矿池','外联'等，\"Directory Scan|Directory Traversal\"。

        :return: The labels of this ThreatIntel.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ThreatIntel.

        标签，如'矿池','外联'等，\"Directory Scan|Directory Traversal\"。

        :param labels: The labels of this ThreatIntel.
        :type labels: str
        """
        self._labels = labels

    @property
    def confidence(self):
        """Gets the confidence of this ThreatIntel.

        置信度，不同来源目前置信度分值定义不一样（分数）。

        :return: The confidence of this ThreatIntel.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ThreatIntel.

        置信度，不同来源目前置信度分值定义不一样（分数）。

        :param confidence: The confidence of this ThreatIntel.
        :type confidence: int
        """
        self._confidence = confidence

    @property
    def information_source(self):
        """Gets the information_source of this ThreatIntel.

        威胁情报源，最大64个字符。

        :return: The information_source of this ThreatIntel.
        :rtype: str
        """
        return self._information_source

    @information_source.setter
    def information_source(self, information_source):
        """Sets the information_source of this ThreatIntel.

        威胁情报源，最大64个字符。

        :param information_source: The information_source of this ThreatIntel.
        :type information_source: str
        """
        self._information_source = information_source

    @property
    def severity(self):
        """Gets the severity of this ThreatIntel.

        严重程度，不同渠道定义值不一样（分数）。

        :return: The severity of this ThreatIntel.
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ThreatIntel.

        严重程度，不同渠道定义值不一样（分数）。

        :param severity: The severity of this ThreatIntel.
        :type severity: int
        """
        self._severity = severity

    @property
    def description(self):
        """Gets the description of this ThreatIntel.

        威胁情报描述。

        :return: The description of this ThreatIntel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ThreatIntel.

        威胁情报描述。

        :param description: The description of this ThreatIntel.
        :type description: str
        """
        self._description = description

    @property
    def modified(self):
        """Gets the modified of this ThreatIntel.

        威胁情报的更新时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。

        :return: The modified of this ThreatIntel.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ThreatIntel.

        威胁情报的更新时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区。

        :param modified: The modified of this ThreatIntel.
        :type modified: datetime
        """
        self._modified = modified

    @property
    def valid_from(self):
        """Gets the valid_from of this ThreatIntel.

        有效期开始（可读字符串）。

        :return: The valid_from of this ThreatIntel.
        :rtype: str
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this ThreatIntel.

        有效期开始（可读字符串）。

        :param valid_from: The valid_from of this ThreatIntel.
        :type valid_from: str
        """
        self._valid_from = valid_from

    @property
    def valid_until(self):
        """Gets the valid_until of this ThreatIntel.

        有效期结束（可读字符串）。

        :return: The valid_until of this ThreatIntel.
        :rtype: str
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this ThreatIntel.

        有效期结束（可读字符串）。

        :param valid_until: The valid_until of this ThreatIntel.
        :type valid_until: str
        """
        self._valid_until = valid_until

    @property
    def properties(self):
        """Gets the properties of this ThreatIntel.

        :return: The properties of this ThreatIntel.
        :rtype: :class:`huaweicloudsdksa.v1.ThreatIntelProperties`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ThreatIntel.

        :param properties: The properties of this ThreatIntel.
        :type properties: :class:`huaweicloudsdksa.v1.ThreatIntelProperties`
        """
        self._properties = properties

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
        if not isinstance(other, ThreatIntel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
