# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudServer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'hps_id': 'str',
        'hps_ecs_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'hps_id': 'hps_id',
        'hps_ecs_id': 'hps_ecs_id'
    }

    def __init__(self, id=None, type=None, hps_id=None, hps_ecs_id=None):
        r"""CloudServer

        The model defined in huaweicloud sdk

        :param id: **参数解释**：服务器资源id，或超节点子节点id。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type id: str
        :param type: **参数解释**：Lite Server服务器类型。 **取值范围**： - BMS：裸金属服务器 - ECS：弹性云服务器 - HPS：超节点服务器
        :type type: str
        :param hps_id: **参数解释**：服务器所属的超节点资源id。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type hps_id: str
        :param hps_ecs_id: **参数解释**：超节点子节点对应服务器资源id。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type hps_ecs_id: str
        """
        
        

        self._id = None
        self._type = None
        self._hps_id = None
        self._hps_ecs_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if hps_id is not None:
            self.hps_id = hps_id
        if hps_ecs_id is not None:
            self.hps_ecs_id = hps_ecs_id

    @property
    def id(self):
        r"""Gets the id of this CloudServer.

        **参数解释**：服务器资源id，或超节点子节点id。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The id of this CloudServer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CloudServer.

        **参数解释**：服务器资源id，或超节点子节点id。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param id: The id of this CloudServer.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this CloudServer.

        **参数解释**：Lite Server服务器类型。 **取值范围**： - BMS：裸金属服务器 - ECS：弹性云服务器 - HPS：超节点服务器

        :return: The type of this CloudServer.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CloudServer.

        **参数解释**：Lite Server服务器类型。 **取值范围**： - BMS：裸金属服务器 - ECS：弹性云服务器 - HPS：超节点服务器

        :param type: The type of this CloudServer.
        :type type: str
        """
        self._type = type

    @property
    def hps_id(self):
        r"""Gets the hps_id of this CloudServer.

        **参数解释**：服务器所属的超节点资源id。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The hps_id of this CloudServer.
        :rtype: str
        """
        return self._hps_id

    @hps_id.setter
    def hps_id(self, hps_id):
        r"""Sets the hps_id of this CloudServer.

        **参数解释**：服务器所属的超节点资源id。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param hps_id: The hps_id of this CloudServer.
        :type hps_id: str
        """
        self._hps_id = hps_id

    @property
    def hps_ecs_id(self):
        r"""Gets the hps_ecs_id of this CloudServer.

        **参数解释**：超节点子节点对应服务器资源id。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The hps_ecs_id of this CloudServer.
        :rtype: str
        """
        return self._hps_ecs_id

    @hps_ecs_id.setter
    def hps_ecs_id(self, hps_ecs_id):
        r"""Sets the hps_ecs_id of this CloudServer.

        **参数解释**：超节点子节点对应服务器资源id。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param hps_ecs_id: The hps_ecs_id of this CloudServer.
        :type hps_ecs_id: str
        """
        self._hps_ecs_id = hps_ecs_id

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
        if not isinstance(other, CloudServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
