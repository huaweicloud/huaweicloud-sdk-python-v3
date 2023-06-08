# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteBlockchainRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blockchain_id': 'str',
        'is_delete_storage': 'bool',
        'is_delete_obs': 'bool',
        'is_delete_resource': 'bool',
        'is_delete_ief': 'bool',
        'is_delete_lightpeer': 'str',
        'ief_nodes_id': 'str'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'is_delete_storage': 'is_delete_storage',
        'is_delete_obs': 'is_delete_obs',
        'is_delete_resource': 'is_delete_resource',
        'is_delete_ief': 'is_delete_ief',
        'is_delete_lightpeer': 'is_delete_lightpeer',
        'ief_nodes_id': 'ief_nodes_id'
    }

    def __init__(self, blockchain_id=None, is_delete_storage=None, is_delete_obs=None, is_delete_resource=None, is_delete_ief=None, is_delete_lightpeer=None, ief_nodes_id=None):
        """DeleteBlockchainRequest

        The model defined in huaweicloud sdk

        :param blockchain_id: bcs 服务id
        :type blockchain_id: str
        :param is_delete_storage: 是否删除存储，IEF模式下不用填写
        :type is_delete_storage: bool
        :param is_delete_obs: 是否删除obs，IEF模式下不用填写
        :type is_delete_obs: bool
        :param is_delete_resource: 是否删除底层CCE资源，IEF模式下不用填写
        :type is_delete_resource: bool
        :param is_delete_ief: 是否删除底层依赖的IEF边缘节点资源，CCE模式下不用填写，IEF模式下必填
        :type is_delete_ief: bool
        :param is_delete_lightpeer: CCE模式下选填：是否删除LightPeer轻节点插件使用的IEF边缘节点资源，若需要删除，则填写对应的IEF编译节点名称，否则无需填写。例如：is_delete_lightpeer&#x3D;ief_node_name_1,ief_node_name_2
        :type is_delete_lightpeer: str
        :param ief_nodes_id: IEF模式下选填：若需要删除IEF边缘集群所使用的IEF边缘节点资源，则填写IEF节点的id，否则无需填写。例如：ief_nodes_id&#x3D;1356f6f0-c448-4ec2-926f-c13b026369d9，0cdacbf9-2002-41e9-8123-2fa13e8d1449
        :type ief_nodes_id: str
        """
        
        

        self._blockchain_id = None
        self._is_delete_storage = None
        self._is_delete_obs = None
        self._is_delete_resource = None
        self._is_delete_ief = None
        self._is_delete_lightpeer = None
        self._ief_nodes_id = None
        self.discriminator = None

        self.blockchain_id = blockchain_id
        if is_delete_storage is not None:
            self.is_delete_storage = is_delete_storage
        if is_delete_obs is not None:
            self.is_delete_obs = is_delete_obs
        if is_delete_resource is not None:
            self.is_delete_resource = is_delete_resource
        if is_delete_ief is not None:
            self.is_delete_ief = is_delete_ief
        if is_delete_lightpeer is not None:
            self.is_delete_lightpeer = is_delete_lightpeer
        if ief_nodes_id is not None:
            self.ief_nodes_id = ief_nodes_id

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this DeleteBlockchainRequest.

        bcs 服务id

        :return: The blockchain_id of this DeleteBlockchainRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this DeleteBlockchainRequest.

        bcs 服务id

        :param blockchain_id: The blockchain_id of this DeleteBlockchainRequest.
        :type blockchain_id: str
        """
        self._blockchain_id = blockchain_id

    @property
    def is_delete_storage(self):
        """Gets the is_delete_storage of this DeleteBlockchainRequest.

        是否删除存储，IEF模式下不用填写

        :return: The is_delete_storage of this DeleteBlockchainRequest.
        :rtype: bool
        """
        return self._is_delete_storage

    @is_delete_storage.setter
    def is_delete_storage(self, is_delete_storage):
        """Sets the is_delete_storage of this DeleteBlockchainRequest.

        是否删除存储，IEF模式下不用填写

        :param is_delete_storage: The is_delete_storage of this DeleteBlockchainRequest.
        :type is_delete_storage: bool
        """
        self._is_delete_storage = is_delete_storage

    @property
    def is_delete_obs(self):
        """Gets the is_delete_obs of this DeleteBlockchainRequest.

        是否删除obs，IEF模式下不用填写

        :return: The is_delete_obs of this DeleteBlockchainRequest.
        :rtype: bool
        """
        return self._is_delete_obs

    @is_delete_obs.setter
    def is_delete_obs(self, is_delete_obs):
        """Sets the is_delete_obs of this DeleteBlockchainRequest.

        是否删除obs，IEF模式下不用填写

        :param is_delete_obs: The is_delete_obs of this DeleteBlockchainRequest.
        :type is_delete_obs: bool
        """
        self._is_delete_obs = is_delete_obs

    @property
    def is_delete_resource(self):
        """Gets the is_delete_resource of this DeleteBlockchainRequest.

        是否删除底层CCE资源，IEF模式下不用填写

        :return: The is_delete_resource of this DeleteBlockchainRequest.
        :rtype: bool
        """
        return self._is_delete_resource

    @is_delete_resource.setter
    def is_delete_resource(self, is_delete_resource):
        """Sets the is_delete_resource of this DeleteBlockchainRequest.

        是否删除底层CCE资源，IEF模式下不用填写

        :param is_delete_resource: The is_delete_resource of this DeleteBlockchainRequest.
        :type is_delete_resource: bool
        """
        self._is_delete_resource = is_delete_resource

    @property
    def is_delete_ief(self):
        """Gets the is_delete_ief of this DeleteBlockchainRequest.

        是否删除底层依赖的IEF边缘节点资源，CCE模式下不用填写，IEF模式下必填

        :return: The is_delete_ief of this DeleteBlockchainRequest.
        :rtype: bool
        """
        return self._is_delete_ief

    @is_delete_ief.setter
    def is_delete_ief(self, is_delete_ief):
        """Sets the is_delete_ief of this DeleteBlockchainRequest.

        是否删除底层依赖的IEF边缘节点资源，CCE模式下不用填写，IEF模式下必填

        :param is_delete_ief: The is_delete_ief of this DeleteBlockchainRequest.
        :type is_delete_ief: bool
        """
        self._is_delete_ief = is_delete_ief

    @property
    def is_delete_lightpeer(self):
        """Gets the is_delete_lightpeer of this DeleteBlockchainRequest.

        CCE模式下选填：是否删除LightPeer轻节点插件使用的IEF边缘节点资源，若需要删除，则填写对应的IEF编译节点名称，否则无需填写。例如：is_delete_lightpeer=ief_node_name_1,ief_node_name_2

        :return: The is_delete_lightpeer of this DeleteBlockchainRequest.
        :rtype: str
        """
        return self._is_delete_lightpeer

    @is_delete_lightpeer.setter
    def is_delete_lightpeer(self, is_delete_lightpeer):
        """Sets the is_delete_lightpeer of this DeleteBlockchainRequest.

        CCE模式下选填：是否删除LightPeer轻节点插件使用的IEF边缘节点资源，若需要删除，则填写对应的IEF编译节点名称，否则无需填写。例如：is_delete_lightpeer=ief_node_name_1,ief_node_name_2

        :param is_delete_lightpeer: The is_delete_lightpeer of this DeleteBlockchainRequest.
        :type is_delete_lightpeer: str
        """
        self._is_delete_lightpeer = is_delete_lightpeer

    @property
    def ief_nodes_id(self):
        """Gets the ief_nodes_id of this DeleteBlockchainRequest.

        IEF模式下选填：若需要删除IEF边缘集群所使用的IEF边缘节点资源，则填写IEF节点的id，否则无需填写。例如：ief_nodes_id=1356f6f0-c448-4ec2-926f-c13b026369d9，0cdacbf9-2002-41e9-8123-2fa13e8d1449

        :return: The ief_nodes_id of this DeleteBlockchainRequest.
        :rtype: str
        """
        return self._ief_nodes_id

    @ief_nodes_id.setter
    def ief_nodes_id(self, ief_nodes_id):
        """Sets the ief_nodes_id of this DeleteBlockchainRequest.

        IEF模式下选填：若需要删除IEF边缘集群所使用的IEF边缘节点资源，则填写IEF节点的id，否则无需填写。例如：ief_nodes_id=1356f6f0-c448-4ec2-926f-c13b026369d9，0cdacbf9-2002-41e9-8123-2fa13e8d1449

        :param ief_nodes_id: The ief_nodes_id of this DeleteBlockchainRequest.
        :type ief_nodes_id: str
        """
        self._ief_nodes_id = ief_nodes_id

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
        if not isinstance(other, DeleteBlockchainRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
