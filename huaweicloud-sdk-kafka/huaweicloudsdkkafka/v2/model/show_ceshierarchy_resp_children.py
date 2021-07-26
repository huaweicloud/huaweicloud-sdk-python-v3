# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCeshierarchyRespChildren:


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
        'dim_router': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'metrics': 'metrics',
        'key_name': 'key_name',
        'dim_router': 'dim_router'
    }

    def __init__(self, name=None, metrics=None, key_name=None, dim_router=None):
        """ShowCeshierarchyRespChildren - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._metrics = None
        self._key_name = None
        self._dim_router = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if metrics is not None:
            self.metrics = metrics
        if key_name is not None:
            self.key_name = key_name
        if dim_router is not None:
            self.dim_router = dim_router

    @property
    def name(self):
        """Gets the name of this ShowCeshierarchyRespChildren.

        子维度名称。

        :return: The name of this ShowCeshierarchyRespChildren.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowCeshierarchyRespChildren.

        子维度名称。

        :param name: The name of this ShowCeshierarchyRespChildren.
        :type: str
        """
        self._name = name

    @property
    def metrics(self):
        """Gets the metrics of this ShowCeshierarchyRespChildren.

        监控指标名称列表。

        :return: The metrics of this ShowCeshierarchyRespChildren.
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ShowCeshierarchyRespChildren.

        监控指标名称列表。

        :param metrics: The metrics of this ShowCeshierarchyRespChildren.
        :type: list[str]
        """
        self._metrics = metrics

    @property
    def key_name(self):
        """Gets the key_name of this ShowCeshierarchyRespChildren.

        监控查询使用的key。

        :return: The key_name of this ShowCeshierarchyRespChildren.
        :rtype: list[str]
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this ShowCeshierarchyRespChildren.

        监控查询使用的key。

        :param key_name: The key_name of this ShowCeshierarchyRespChildren.
        :type: list[str]
        """
        self._key_name = key_name

    @property
    def dim_router(self):
        """Gets the dim_router of this ShowCeshierarchyRespChildren.

        监控维度路由。

        :return: The dim_router of this ShowCeshierarchyRespChildren.
        :rtype: list[str]
        """
        return self._dim_router

    @dim_router.setter
    def dim_router(self, dim_router):
        """Sets the dim_router of this ShowCeshierarchyRespChildren.

        监控维度路由。

        :param dim_router: The dim_router of this ShowCeshierarchyRespChildren.
        :type: list[str]
        """
        self._dim_router = dim_router

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowCeshierarchyRespChildren):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
