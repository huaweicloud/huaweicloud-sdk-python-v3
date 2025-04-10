# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenTSDBSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric': 'list[OpenTSDBMetric]',
        'timestamp': 'OpenTSDBTimestamp',
        'value': 'OpenTSDBValue',
        'tags': 'list[OpenTSDBTags]'
    }

    attribute_map = {
        'metric': 'metric',
        'timestamp': 'timestamp',
        'value': 'value',
        'tags': 'tags'
    }

    def __init__(self, metric=None, timestamp=None, value=None, tags=None):
        r"""OpenTSDBSchema

        The model defined in huaweicloud sdk

        :param metric: CloudTable集群OpenTSDB数据metric的Schema配置，用于将通道内的JSON数据进行格式转换生成OpenTSDB数据的metric。
        :type metric: list[:class:`huaweicloudsdkdis.v2.OpenTSDBMetric`]
        :param timestamp: 
        :type timestamp: :class:`huaweicloudsdkdis.v2.OpenTSDBTimestamp`
        :param value: 
        :type value: :class:`huaweicloudsdkdis.v2.OpenTSDBValue`
        :param tags: CloudTable集群OpenTSDB数据tags的Schema配置，用于将通道内的JSON数据进行格式转换生成OpenTSDB数据的tags。
        :type tags: list[:class:`huaweicloudsdkdis.v2.OpenTSDBTags`]
        """
        
        

        self._metric = None
        self._timestamp = None
        self._value = None
        self._tags = None
        self.discriminator = None

        self.metric = metric
        self.timestamp = timestamp
        self.value = value
        self.tags = tags

    @property
    def metric(self):
        r"""Gets the metric of this OpenTSDBSchema.

        CloudTable集群OpenTSDB数据metric的Schema配置，用于将通道内的JSON数据进行格式转换生成OpenTSDB数据的metric。

        :return: The metric of this OpenTSDBSchema.
        :rtype: list[:class:`huaweicloudsdkdis.v2.OpenTSDBMetric`]
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this OpenTSDBSchema.

        CloudTable集群OpenTSDB数据metric的Schema配置，用于将通道内的JSON数据进行格式转换生成OpenTSDB数据的metric。

        :param metric: The metric of this OpenTSDBSchema.
        :type metric: list[:class:`huaweicloudsdkdis.v2.OpenTSDBMetric`]
        """
        self._metric = metric

    @property
    def timestamp(self):
        r"""Gets the timestamp of this OpenTSDBSchema.

        :return: The timestamp of this OpenTSDBSchema.
        :rtype: :class:`huaweicloudsdkdis.v2.OpenTSDBTimestamp`
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this OpenTSDBSchema.

        :param timestamp: The timestamp of this OpenTSDBSchema.
        :type timestamp: :class:`huaweicloudsdkdis.v2.OpenTSDBTimestamp`
        """
        self._timestamp = timestamp

    @property
    def value(self):
        r"""Gets the value of this OpenTSDBSchema.

        :return: The value of this OpenTSDBSchema.
        :rtype: :class:`huaweicloudsdkdis.v2.OpenTSDBValue`
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OpenTSDBSchema.

        :param value: The value of this OpenTSDBSchema.
        :type value: :class:`huaweicloudsdkdis.v2.OpenTSDBValue`
        """
        self._value = value

    @property
    def tags(self):
        r"""Gets the tags of this OpenTSDBSchema.

        CloudTable集群OpenTSDB数据tags的Schema配置，用于将通道内的JSON数据进行格式转换生成OpenTSDB数据的tags。

        :return: The tags of this OpenTSDBSchema.
        :rtype: list[:class:`huaweicloudsdkdis.v2.OpenTSDBTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this OpenTSDBSchema.

        CloudTable集群OpenTSDB数据tags的Schema配置，用于将通道内的JSON数据进行格式转换生成OpenTSDB数据的tags。

        :param tags: The tags of this OpenTSDBSchema.
        :type tags: list[:class:`huaweicloudsdkdis.v2.OpenTSDBTags`]
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
        if not isinstance(other, OpenTSDBSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
