# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicableInstancesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'entities': 'list[EntityInfo]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'entities': 'entities'
    }

    def __init__(self, instance_id=None, instance_name=None, entities=None):
        r"""ApplicableInstancesInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param entities: 节点组信息或节点信息的列表对象。  当参数模板是集群类型时，如果是shard组或者config组的参数模板，则可应用到的是对应类型的节点组，如果是mongos组的参数模板，则可应用到的是对应类型的的节点。  当参数模板是副本集或单节点类型时，直接应用到对应实例。  例如：一个mongos参数模板可应用到一个或多个mongos节点。
        :type entities: list[:class:`huaweicloudsdkdds.v3.EntityInfo`]
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._entities = None
        self.discriminator = None

        self.instance_id = instance_id
        self.instance_name = instance_name
        self.entities = entities

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ApplicableInstancesInfo.

        实例ID。

        :return: The instance_id of this ApplicableInstancesInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ApplicableInstancesInfo.

        实例ID。

        :param instance_id: The instance_id of this ApplicableInstancesInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ApplicableInstancesInfo.

        实例名称。

        :return: The instance_name of this ApplicableInstancesInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ApplicableInstancesInfo.

        实例名称。

        :param instance_name: The instance_name of this ApplicableInstancesInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def entities(self):
        r"""Gets the entities of this ApplicableInstancesInfo.

        节点组信息或节点信息的列表对象。  当参数模板是集群类型时，如果是shard组或者config组的参数模板，则可应用到的是对应类型的节点组，如果是mongos组的参数模板，则可应用到的是对应类型的的节点。  当参数模板是副本集或单节点类型时，直接应用到对应实例。  例如：一个mongos参数模板可应用到一个或多个mongos节点。

        :return: The entities of this ApplicableInstancesInfo.
        :rtype: list[:class:`huaweicloudsdkdds.v3.EntityInfo`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        r"""Sets the entities of this ApplicableInstancesInfo.

        节点组信息或节点信息的列表对象。  当参数模板是集群类型时，如果是shard组或者config组的参数模板，则可应用到的是对应类型的节点组，如果是mongos组的参数模板，则可应用到的是对应类型的的节点。  当参数模板是副本集或单节点类型时，直接应用到对应实例。  例如：一个mongos参数模板可应用到一个或多个mongos节点。

        :param entities: The entities of this ApplicableInstancesInfo.
        :type entities: list[:class:`huaweicloudsdkdds.v3.EntityInfo`]
        """
        self._entities = entities

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
        if not isinstance(other, ApplicableInstancesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
