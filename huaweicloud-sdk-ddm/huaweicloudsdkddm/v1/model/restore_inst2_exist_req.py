# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreInst2ExistReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'object',
        'target': 'object',
        'data_node_relations': 'list[DataNodeRelation]'
    }

    attribute_map = {
        'source': 'source',
        'target': 'target',
        'data_node_relations': 'data_node_relations'
    }

    def __init__(self, source=None, target=None, data_node_relations=None):
        r"""RestoreInst2ExistReq

        The model defined in huaweicloud sdk

        :param source: 数据恢复源。
        :type source: object
        :param target: 数据恢复目标。
        :type target: object
        :param data_node_relations: 关联dn。
        :type data_node_relations: list[:class:`huaweicloudsdkddm.v1.DataNodeRelation`]
        """
        
        

        self._source = None
        self._target = None
        self._data_node_relations = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if data_node_relations is not None:
            self.data_node_relations = data_node_relations

    @property
    def source(self):
        r"""Gets the source of this RestoreInst2ExistReq.

        数据恢复源。

        :return: The source of this RestoreInst2ExistReq.
        :rtype: object
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this RestoreInst2ExistReq.

        数据恢复源。

        :param source: The source of this RestoreInst2ExistReq.
        :type source: object
        """
        self._source = source

    @property
    def target(self):
        r"""Gets the target of this RestoreInst2ExistReq.

        数据恢复目标。

        :return: The target of this RestoreInst2ExistReq.
        :rtype: object
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this RestoreInst2ExistReq.

        数据恢复目标。

        :param target: The target of this RestoreInst2ExistReq.
        :type target: object
        """
        self._target = target

    @property
    def data_node_relations(self):
        r"""Gets the data_node_relations of this RestoreInst2ExistReq.

        关联dn。

        :return: The data_node_relations of this RestoreInst2ExistReq.
        :rtype: list[:class:`huaweicloudsdkddm.v1.DataNodeRelation`]
        """
        return self._data_node_relations

    @data_node_relations.setter
    def data_node_relations(self, data_node_relations):
        r"""Sets the data_node_relations of this RestoreInst2ExistReq.

        关联dn。

        :param data_node_relations: The data_node_relations of this RestoreInst2ExistReq.
        :type data_node_relations: list[:class:`huaweicloudsdkddm.v1.DataNodeRelation`]
        """
        self._data_node_relations = data_node_relations

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
        if not isinstance(other, RestoreInst2ExistReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
