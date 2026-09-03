# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceNodesInfoRequest:

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
        'engine_type': 'str',
        'all_nodes': 'str',
        'show_hidden_nodes': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'engine_type': 'engine_type',
        'all_nodes': 'all_nodes',
        'show_hidden_nodes': 'show_hidden_nodes'
    }

    def __init__(self, instance_id=None, engine_type=None, all_nodes=None, show_hidden_nodes=None):
        r"""ShowInstanceNodesInfoRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param all_nodes: 
        :type all_nodes: str
        :param show_hidden_nodes: 
        :type show_hidden_nodes: str
        """
        
        

        self._instance_id = None
        self._engine_type = None
        self._all_nodes = None
        self._show_hidden_nodes = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if engine_type is not None:
            self.engine_type = engine_type
        if all_nodes is not None:
            self.all_nodes = all_nodes
        if show_hidden_nodes is not None:
            self.show_hidden_nodes = show_hidden_nodes

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceNodesInfoRequest.

        实例ID

        :return: The instance_id of this ShowInstanceNodesInfoRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceNodesInfoRequest.

        实例ID

        :param instance_id: The instance_id of this ShowInstanceNodesInfoRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowInstanceNodesInfoRequest.

        数据库引擎类型

        :return: The engine_type of this ShowInstanceNodesInfoRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowInstanceNodesInfoRequest.

        数据库引擎类型

        :param engine_type: The engine_type of this ShowInstanceNodesInfoRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def all_nodes(self):
        r"""Gets the all_nodes of this ShowInstanceNodesInfoRequest.

        :return: The all_nodes of this ShowInstanceNodesInfoRequest.
        :rtype: str
        """
        return self._all_nodes

    @all_nodes.setter
    def all_nodes(self, all_nodes):
        r"""Sets the all_nodes of this ShowInstanceNodesInfoRequest.

        :param all_nodes: The all_nodes of this ShowInstanceNodesInfoRequest.
        :type all_nodes: str
        """
        self._all_nodes = all_nodes

    @property
    def show_hidden_nodes(self):
        r"""Gets the show_hidden_nodes of this ShowInstanceNodesInfoRequest.

        :return: The show_hidden_nodes of this ShowInstanceNodesInfoRequest.
        :rtype: str
        """
        return self._show_hidden_nodes

    @show_hidden_nodes.setter
    def show_hidden_nodes(self, show_hidden_nodes):
        r"""Sets the show_hidden_nodes of this ShowInstanceNodesInfoRequest.

        :param show_hidden_nodes: The show_hidden_nodes of this ShowInstanceNodesInfoRequest.
        :type show_hidden_nodes: str
        """
        self._show_hidden_nodes = show_hidden_nodes

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
        if not isinstance(other, ShowInstanceNodesInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
