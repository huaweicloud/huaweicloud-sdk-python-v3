# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDataStore:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_store_id': 'str',
        'name': 'str',
        'group_id': 'str',
        'tags': 'list[Tag]',
        'metrics': 'list[Metric]',
        'properties': 'list[ModelProperty]',
        'created_time': 'str',
        'modified_time': 'str'
    }

    attribute_map = {
        'data_store_id': 'data_store_id',
        'name': 'name',
        'group_id': 'group_id',
        'tags': 'tags',
        'metrics': 'metrics',
        'properties': 'properties',
        'created_time': 'created_time',
        'modified_time': 'modified_time'
    }

    def __init__(self, data_store_id=None, name=None, group_id=None, tags=None, metrics=None, properties=None, created_time=None, modified_time=None):
        r"""GetDataStore

        The model defined in huaweicloud sdk

        :param data_store_id: 存储 ID
        :type data_store_id: str
        :param name: 存储名称
        :type name: str
        :param group_id: 存储 ID
        :type group_id: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkiotanalytics.v1.Tag`]
        :param metrics: 指标
        :type metrics: list[:class:`huaweicloudsdkiotanalytics.v1.Metric`]
        :param properties: 属性
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.ModelProperty`]
        :param created_time: 创建时间
        :type created_time: str
        :param modified_time: 更新时间
        :type modified_time: str
        """
        
        

        self._data_store_id = None
        self._name = None
        self._group_id = None
        self._tags = None
        self._metrics = None
        self._properties = None
        self._created_time = None
        self._modified_time = None
        self.discriminator = None

        if data_store_id is not None:
            self.data_store_id = data_store_id
        if name is not None:
            self.name = name
        if group_id is not None:
            self.group_id = group_id
        if tags is not None:
            self.tags = tags
        if metrics is not None:
            self.metrics = metrics
        if properties is not None:
            self.properties = properties
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time

    @property
    def data_store_id(self):
        r"""Gets the data_store_id of this GetDataStore.

        存储 ID

        :return: The data_store_id of this GetDataStore.
        :rtype: str
        """
        return self._data_store_id

    @data_store_id.setter
    def data_store_id(self, data_store_id):
        r"""Sets the data_store_id of this GetDataStore.

        存储 ID

        :param data_store_id: The data_store_id of this GetDataStore.
        :type data_store_id: str
        """
        self._data_store_id = data_store_id

    @property
    def name(self):
        r"""Gets the name of this GetDataStore.

        存储名称

        :return: The name of this GetDataStore.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetDataStore.

        存储名称

        :param name: The name of this GetDataStore.
        :type name: str
        """
        self._name = name

    @property
    def group_id(self):
        r"""Gets the group_id of this GetDataStore.

        存储 ID

        :return: The group_id of this GetDataStore.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this GetDataStore.

        存储 ID

        :param group_id: The group_id of this GetDataStore.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def tags(self):
        r"""Gets the tags of this GetDataStore.

        标签

        :return: The tags of this GetDataStore.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this GetDataStore.

        标签

        :param tags: The tags of this GetDataStore.
        :type tags: list[:class:`huaweicloudsdkiotanalytics.v1.Tag`]
        """
        self._tags = tags

    @property
    def metrics(self):
        r"""Gets the metrics of this GetDataStore.

        指标

        :return: The metrics of this GetDataStore.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.Metric`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this GetDataStore.

        指标

        :param metrics: The metrics of this GetDataStore.
        :type metrics: list[:class:`huaweicloudsdkiotanalytics.v1.Metric`]
        """
        self._metrics = metrics

    @property
    def properties(self):
        r"""Gets the properties of this GetDataStore.

        属性

        :return: The properties of this GetDataStore.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.ModelProperty`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this GetDataStore.

        属性

        :param properties: The properties of this GetDataStore.
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.ModelProperty`]
        """
        self._properties = properties

    @property
    def created_time(self):
        r"""Gets the created_time of this GetDataStore.

        创建时间

        :return: The created_time of this GetDataStore.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this GetDataStore.

        创建时间

        :param created_time: The created_time of this GetDataStore.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this GetDataStore.

        更新时间

        :return: The modified_time of this GetDataStore.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this GetDataStore.

        更新时间

        :param modified_time: The modified_time of this GetDataStore.
        :type modified_time: str
        """
        self._modified_time = modified_time

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
        if not isinstance(other, GetDataStore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
