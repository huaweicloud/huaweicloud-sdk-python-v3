# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetailViewConfigModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_set': 'str',
        'filter_prefix': 'str',
        'detail_view_item_list': 'list[DetailViewItem]'
    }

    attribute_map = {
        'metric_set': 'metric_set',
        'filter_prefix': 'filter_prefix',
        'detail_view_item_list': 'detail_view_item_list'
    }

    def __init__(self, metric_set=None, filter_prefix=None, detail_view_item_list=None):
        """DetailViewConfigModel

        The model defined in huaweicloud sdk

        :param metric_set: 视图对应的指标集的名称。
        :type metric_set: str
        :param filter_prefix: 过滤参数。
        :type filter_prefix: str
        :param detail_view_item_list: 视图函数集合。
        :type detail_view_item_list: list[:class:`huaweicloudsdkapm.v1.DetailViewItem`]
        """
        
        

        self._metric_set = None
        self._filter_prefix = None
        self._detail_view_item_list = None
        self.discriminator = None

        if metric_set is not None:
            self.metric_set = metric_set
        if filter_prefix is not None:
            self.filter_prefix = filter_prefix
        if detail_view_item_list is not None:
            self.detail_view_item_list = detail_view_item_list

    @property
    def metric_set(self):
        """Gets the metric_set of this DetailViewConfigModel.

        视图对应的指标集的名称。

        :return: The metric_set of this DetailViewConfigModel.
        :rtype: str
        """
        return self._metric_set

    @metric_set.setter
    def metric_set(self, metric_set):
        """Sets the metric_set of this DetailViewConfigModel.

        视图对应的指标集的名称。

        :param metric_set: The metric_set of this DetailViewConfigModel.
        :type metric_set: str
        """
        self._metric_set = metric_set

    @property
    def filter_prefix(self):
        """Gets the filter_prefix of this DetailViewConfigModel.

        过滤参数。

        :return: The filter_prefix of this DetailViewConfigModel.
        :rtype: str
        """
        return self._filter_prefix

    @filter_prefix.setter
    def filter_prefix(self, filter_prefix):
        """Sets the filter_prefix of this DetailViewConfigModel.

        过滤参数。

        :param filter_prefix: The filter_prefix of this DetailViewConfigModel.
        :type filter_prefix: str
        """
        self._filter_prefix = filter_prefix

    @property
    def detail_view_item_list(self):
        """Gets the detail_view_item_list of this DetailViewConfigModel.

        视图函数集合。

        :return: The detail_view_item_list of this DetailViewConfigModel.
        :rtype: list[:class:`huaweicloudsdkapm.v1.DetailViewItem`]
        """
        return self._detail_view_item_list

    @detail_view_item_list.setter
    def detail_view_item_list(self, detail_view_item_list):
        """Sets the detail_view_item_list of this DetailViewConfigModel.

        视图函数集合。

        :param detail_view_item_list: The detail_view_item_list of this DetailViewConfigModel.
        :type detail_view_item_list: list[:class:`huaweicloudsdkapm.v1.DetailViewItem`]
        """
        self._detail_view_item_list = detail_view_item_list

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
        if not isinstance(other, DetailViewConfigModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
