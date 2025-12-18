# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DdmNodeInfo:

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
        'status': 'str',
        'name': 'str',
        'az_code': 'str',
        'actions': 'list[ActionInfo]',
        'subnet_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'az_code': 'az_code',
        'actions': 'actions',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, id=None, status=None, name=None, az_code=None, actions=None, subnet_id=None):
        r"""DdmNodeInfo

        The model defined in huaweicloud sdk

        :param id: 节点ID。
        :type id: str
        :param status: 状态。
        :type status: str
        :param name: 名称。
        :type name: str
        :param az_code: 可用区编码。
        :type az_code: str
        :param actions: 锁状态。
        :type actions: list[:class:`huaweicloudsdkddm.v1.ActionInfo`]
        :param subnet_id: 子网ID。
        :type subnet_id: str
        """
        
        

        self._id = None
        self._status = None
        self._name = None
        self._az_code = None
        self._actions = None
        self._subnet_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if az_code is not None:
            self.az_code = az_code
        if actions is not None:
            self.actions = actions
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def id(self):
        r"""Gets the id of this DdmNodeInfo.

        节点ID。

        :return: The id of this DdmNodeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DdmNodeInfo.

        节点ID。

        :param id: The id of this DdmNodeInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this DdmNodeInfo.

        状态。

        :return: The status of this DdmNodeInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DdmNodeInfo.

        状态。

        :param status: The status of this DdmNodeInfo.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this DdmNodeInfo.

        名称。

        :return: The name of this DdmNodeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DdmNodeInfo.

        名称。

        :param name: The name of this DdmNodeInfo.
        :type name: str
        """
        self._name = name

    @property
    def az_code(self):
        r"""Gets the az_code of this DdmNodeInfo.

        可用区编码。

        :return: The az_code of this DdmNodeInfo.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this DdmNodeInfo.

        可用区编码。

        :param az_code: The az_code of this DdmNodeInfo.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def actions(self):
        r"""Gets the actions of this DdmNodeInfo.

        锁状态。

        :return: The actions of this DdmNodeInfo.
        :rtype: list[:class:`huaweicloudsdkddm.v1.ActionInfo`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this DdmNodeInfo.

        锁状态。

        :param actions: The actions of this DdmNodeInfo.
        :type actions: list[:class:`huaweicloudsdkddm.v1.ActionInfo`]
        """
        self._actions = actions

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this DdmNodeInfo.

        子网ID。

        :return: The subnet_id of this DdmNodeInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this DdmNodeInfo.

        子网ID。

        :param subnet_id: The subnet_id of this DdmNodeInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, DdmNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
