# coding: utf-8

import pprint
import re

import six





class ShowCeshierarchyRespDimensions:


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
        'metrics': 'list[str]',
        'key_name': 'list[str]',
        'dim_router': 'list[str]',
        'children': 'list[ShowCeshierarchyRespChildren]'
    }

    attribute_map = {
        'name': 'name',
        'metrics': 'metrics',
        'key_name': 'key_name',
        'dim_router': 'dim_router',
        'children': 'children'
    }

    def __init__(self, name=None, metrics=None, key_name=None, dim_router=None, children=None):
        """ShowCeshierarchyRespDimensions - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._metrics = None
        self._key_name = None
        self._dim_router = None
        self._children = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if metrics is not None:
            self.metrics = metrics
        if key_name is not None:
            self.key_name = key_name
        if dim_router is not None:
            self.dim_router = dim_router
        if children is not None:
            self.children = children

    @property
    def name(self):
        """Gets the name of this ShowCeshierarchyRespDimensions.

        监控维度名称。

        :return: The name of this ShowCeshierarchyRespDimensions.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowCeshierarchyRespDimensions.

        监控维度名称。

        :param name: The name of this ShowCeshierarchyRespDimensions.
        :type: str
        """
        self._name = name

    @property
    def metrics(self):
        """Gets the metrics of this ShowCeshierarchyRespDimensions.

        监控指标名称。请参考[支持的监控指标](https://support.huaweicloud.com/usermanual-kafka/kafka-ug-180413002.html)。

        :return: The metrics of this ShowCeshierarchyRespDimensions.
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ShowCeshierarchyRespDimensions.

        监控指标名称。请参考[支持的监控指标](https://support.huaweicloud.com/usermanual-kafka/kafka-ug-180413002.html)。

        :param metrics: The metrics of this ShowCeshierarchyRespDimensions.
        :type: list[str]
        """
        self._metrics = metrics

    @property
    def key_name(self):
        """Gets the key_name of this ShowCeshierarchyRespDimensions.

        监控查询使用的key。

        :return: The key_name of this ShowCeshierarchyRespDimensions.
        :rtype: list[str]
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this ShowCeshierarchyRespDimensions.

        监控查询使用的key。

        :param key_name: The key_name of this ShowCeshierarchyRespDimensions.
        :type: list[str]
        """
        self._key_name = key_name

    @property
    def dim_router(self):
        """Gets the dim_router of this ShowCeshierarchyRespDimensions.

        监控维度路由。

        :return: The dim_router of this ShowCeshierarchyRespDimensions.
        :rtype: list[str]
        """
        return self._dim_router

    @dim_router.setter
    def dim_router(self, dim_router):
        """Sets the dim_router of this ShowCeshierarchyRespDimensions.

        监控维度路由。

        :param dim_router: The dim_router of this ShowCeshierarchyRespDimensions.
        :type: list[str]
        """
        self._dim_router = dim_router

    @property
    def children(self):
        """Gets the children of this ShowCeshierarchyRespDimensions.

        子维度列表。

        :return: The children of this ShowCeshierarchyRespDimensions.
        :rtype: list[ShowCeshierarchyRespChildren]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ShowCeshierarchyRespDimensions.

        子维度列表。

        :param children: The children of this ShowCeshierarchyRespDimensions.
        :type: list[ShowCeshierarchyRespChildren]
        """
        self._children = children

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowCeshierarchyRespDimensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
