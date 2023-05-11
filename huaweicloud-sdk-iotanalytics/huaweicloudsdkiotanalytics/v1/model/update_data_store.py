# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDataStore:

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
        'tags': 'list[Tag]',
        'metrics': 'list[Metric]',
        'properties': 'list[ModelProperty]'
    }

    attribute_map = {
        'name': 'name',
        'tags': 'tags',
        'metrics': 'metrics',
        'properties': 'properties'
    }

    def __init__(self, name=None, tags=None, metrics=None, properties=None):
        """UpdateDataStore

        The model defined in huaweicloud sdk

        :param name: 存储名称
        :type name: str
        :param tags: 标签，更新存储时标签只可新增，不可修改或删除原有标签
        :type tags: list[:class:`huaweicloudsdkiotanalytics.v1.Tag`]
        :param metrics: 指标
        :type metrics: list[:class:`huaweicloudsdkiotanalytics.v1.Metric`]
        :param properties: 属性，更新存储时属性只可新增，不可修改或删除原有属性
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.ModelProperty`]
        """
        
        

        self._name = None
        self._tags = None
        self._metrics = None
        self._properties = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if metrics is not None:
            self.metrics = metrics
        if properties is not None:
            self.properties = properties

    @property
    def name(self):
        """Gets the name of this UpdateDataStore.

        存储名称

        :return: The name of this UpdateDataStore.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDataStore.

        存储名称

        :param name: The name of this UpdateDataStore.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        """Gets the tags of this UpdateDataStore.

        标签，更新存储时标签只可新增，不可修改或删除原有标签

        :return: The tags of this UpdateDataStore.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateDataStore.

        标签，更新存储时标签只可新增，不可修改或删除原有标签

        :param tags: The tags of this UpdateDataStore.
        :type tags: list[:class:`huaweicloudsdkiotanalytics.v1.Tag`]
        """
        self._tags = tags

    @property
    def metrics(self):
        """Gets the metrics of this UpdateDataStore.

        指标

        :return: The metrics of this UpdateDataStore.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.Metric`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this UpdateDataStore.

        指标

        :param metrics: The metrics of this UpdateDataStore.
        :type metrics: list[:class:`huaweicloudsdkiotanalytics.v1.Metric`]
        """
        self._metrics = metrics

    @property
    def properties(self):
        """Gets the properties of this UpdateDataStore.

        属性，更新存储时属性只可新增，不可修改或删除原有属性

        :return: The properties of this UpdateDataStore.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.ModelProperty`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpdateDataStore.

        属性，更新存储时属性只可新增，不可修改或删除原有属性

        :param properties: The properties of this UpdateDataStore.
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.ModelProperty`]
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
        if not isinstance(other, UpdateDataStore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
