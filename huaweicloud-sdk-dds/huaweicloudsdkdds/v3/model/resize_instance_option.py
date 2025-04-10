# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeInstanceOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_type': 'str',
        'target_id': 'str',
        'target_ids': 'list[str]',
        'target_spec_code': 'str'
    }

    attribute_map = {
        'target_type': 'target_type',
        'target_id': 'target_id',
        'target_ids': 'target_ids',
        'target_spec_code': 'target_spec_code'
    }

    def __init__(self, target_type=None, target_id=None, target_ids=None, target_spec_code=None):
        r"""ResizeInstanceOption

        The model defined in huaweicloud sdk

        :param target_type: 对象类型。 - 对于集群实例，该参数为必选。变更mongos节点规格时，取值为“mongos”；变更单个shard组规格、或者批量变更多个shard组规格时，取值为“shard”，变更config组规格时，取值为\&quot;config\&quot;。 - 对于副本集实例，不传该参数。变更readonly节点规格时,取值为“readonly”。 - 对于单节点实例，不传该参数。
        :type target_type: str
        :param target_id: 待变更规格的节点ID或实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 - 对于集群实例，变更mongos节点规格时，取值为mongos节点ID；变更单个shard组规格时，取值为shard组ID；批量变更多个shard组规格时，不传该参数；变更config组规格时，取值为config组的ID。 - 对于副本集实例，取值为相应的实例ID。变更readonly节点规格时，取值为readonly节点ID。 - 对于单节点实例，取值为相应的实例ID。
        :type target_id: str
        :param target_ids: 待变更规格的节点组ID列表，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 - 对于集群实例，变更mongos节点规格时，不传该参数；变更单个shard组规格时，不传该参数；变更config组规格时，不传该参数；批量变更多个shard组规格时，取值为相应的多个shard组ID，最多支持16个shard组批量变更。 - 对于副本集实例，不传该参数。 - 对于单节点实例，不传该参数。
        :type target_ids: list[str]
        :param target_spec_code: 变更至新规格的资源规格编码。
        :type target_spec_code: str
        """
        
        

        self._target_type = None
        self._target_id = None
        self._target_ids = None
        self._target_spec_code = None
        self.discriminator = None

        if target_type is not None:
            self.target_type = target_type
        if target_id is not None:
            self.target_id = target_id
        if target_ids is not None:
            self.target_ids = target_ids
        self.target_spec_code = target_spec_code

    @property
    def target_type(self):
        r"""Gets the target_type of this ResizeInstanceOption.

        对象类型。 - 对于集群实例，该参数为必选。变更mongos节点规格时，取值为“mongos”；变更单个shard组规格、或者批量变更多个shard组规格时，取值为“shard”，变更config组规格时，取值为\"config\"。 - 对于副本集实例，不传该参数。变更readonly节点规格时,取值为“readonly”。 - 对于单节点实例，不传该参数。

        :return: The target_type of this ResizeInstanceOption.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this ResizeInstanceOption.

        对象类型。 - 对于集群实例，该参数为必选。变更mongos节点规格时，取值为“mongos”；变更单个shard组规格、或者批量变更多个shard组规格时，取值为“shard”，变更config组规格时，取值为\"config\"。 - 对于副本集实例，不传该参数。变更readonly节点规格时,取值为“readonly”。 - 对于单节点实例，不传该参数。

        :param target_type: The target_type of this ResizeInstanceOption.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def target_id(self):
        r"""Gets the target_id of this ResizeInstanceOption.

        待变更规格的节点ID或实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 - 对于集群实例，变更mongos节点规格时，取值为mongos节点ID；变更单个shard组规格时，取值为shard组ID；批量变更多个shard组规格时，不传该参数；变更config组规格时，取值为config组的ID。 - 对于副本集实例，取值为相应的实例ID。变更readonly节点规格时，取值为readonly节点ID。 - 对于单节点实例，取值为相应的实例ID。

        :return: The target_id of this ResizeInstanceOption.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this ResizeInstanceOption.

        待变更规格的节点ID或实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 - 对于集群实例，变更mongos节点规格时，取值为mongos节点ID；变更单个shard组规格时，取值为shard组ID；批量变更多个shard组规格时，不传该参数；变更config组规格时，取值为config组的ID。 - 对于副本集实例，取值为相应的实例ID。变更readonly节点规格时，取值为readonly节点ID。 - 对于单节点实例，取值为相应的实例ID。

        :param target_id: The target_id of this ResizeInstanceOption.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def target_ids(self):
        r"""Gets the target_ids of this ResizeInstanceOption.

        待变更规格的节点组ID列表，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 - 对于集群实例，变更mongos节点规格时，不传该参数；变更单个shard组规格时，不传该参数；变更config组规格时，不传该参数；批量变更多个shard组规格时，取值为相应的多个shard组ID，最多支持16个shard组批量变更。 - 对于副本集实例，不传该参数。 - 对于单节点实例，不传该参数。

        :return: The target_ids of this ResizeInstanceOption.
        :rtype: list[str]
        """
        return self._target_ids

    @target_ids.setter
    def target_ids(self, target_ids):
        r"""Sets the target_ids of this ResizeInstanceOption.

        待变更规格的节点组ID列表，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 - 对于集群实例，变更mongos节点规格时，不传该参数；变更单个shard组规格时，不传该参数；变更config组规格时，不传该参数；批量变更多个shard组规格时，取值为相应的多个shard组ID，最多支持16个shard组批量变更。 - 对于副本集实例，不传该参数。 - 对于单节点实例，不传该参数。

        :param target_ids: The target_ids of this ResizeInstanceOption.
        :type target_ids: list[str]
        """
        self._target_ids = target_ids

    @property
    def target_spec_code(self):
        r"""Gets the target_spec_code of this ResizeInstanceOption.

        变更至新规格的资源规格编码。

        :return: The target_spec_code of this ResizeInstanceOption.
        :rtype: str
        """
        return self._target_spec_code

    @target_spec_code.setter
    def target_spec_code(self, target_spec_code):
        r"""Sets the target_spec_code of this ResizeInstanceOption.

        变更至新规格的资源规格编码。

        :param target_spec_code: The target_spec_code of this ResizeInstanceOption.
        :type target_spec_code: str
        """
        self._target_spec_code = target_spec_code

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
        if not isinstance(other, ResizeInstanceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
