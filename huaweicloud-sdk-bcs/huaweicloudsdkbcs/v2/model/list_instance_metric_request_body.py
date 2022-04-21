# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceMetricRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'entity_name': 'str',
        'instance_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'entity_name': 'entity_name',
        'instance_name': 'instance_name'
    }

    def __init__(self, type=None, entity_name=None, instance_name=None):
        """ListInstanceMetricRequestBody

        The model defined in huaweicloud sdk

        :param type: 实体类型，[可选值如下 org     # 节点组织 plugin  # 插件](tag:online) 默认为org 
        :type type: str
        :param entity_name: 所属实体的名称
        :type entity_name: str
        :param instance_name: 具体实例的名称
        :type instance_name: str
        """
        
        

        self._type = None
        self._entity_name = None
        self._instance_name = None
        self.discriminator = None

        self.type = type
        self.entity_name = entity_name
        self.instance_name = instance_name

    @property
    def type(self):
        """Gets the type of this ListInstanceMetricRequestBody.

        实体类型，[可选值如下 org     # 节点组织 plugin  # 插件](tag:online) 默认为org 

        :return: The type of this ListInstanceMetricRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListInstanceMetricRequestBody.

        实体类型，[可选值如下 org     # 节点组织 plugin  # 插件](tag:online) 默认为org 

        :param type: The type of this ListInstanceMetricRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def entity_name(self):
        """Gets the entity_name of this ListInstanceMetricRequestBody.

        所属实体的名称

        :return: The entity_name of this ListInstanceMetricRequestBody.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this ListInstanceMetricRequestBody.

        所属实体的名称

        :param entity_name: The entity_name of this ListInstanceMetricRequestBody.
        :type entity_name: str
        """
        self._entity_name = entity_name

    @property
    def instance_name(self):
        """Gets the instance_name of this ListInstanceMetricRequestBody.

        具体实例的名称

        :return: The instance_name of this ListInstanceMetricRequestBody.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ListInstanceMetricRequestBody.

        具体实例的名称

        :param instance_name: The instance_name of this ListInstanceMetricRequestBody.
        :type instance_name: str
        """
        self._instance_name = instance_name

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
        if not isinstance(other, ListInstanceMetricRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
