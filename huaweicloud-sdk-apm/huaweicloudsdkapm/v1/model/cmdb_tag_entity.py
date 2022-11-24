# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CmdbTagEntity:

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
        'business_id': 'int',
        'uuid': 'str',
        'descp': 'str',
        'creator_id': 'int',
        'env_id_list': 'list[int]',
        'id': 'int',
        'gmt_create': 'str',
        'gmt_modify': 'str'
    }

    attribute_map = {
        'name': 'name',
        'business_id': 'business_id',
        'uuid': 'uuid',
        'descp': 'descp',
        'creator_id': 'creator_id',
        'env_id_list': 'env_id_list',
        'id': 'id',
        'gmt_create': 'gmt_create',
        'gmt_modify': 'gmt_modify'
    }

    def __init__(self, name=None, business_id=None, uuid=None, descp=None, creator_id=None, env_id_list=None, id=None, gmt_create=None, gmt_modify=None):
        """CmdbTagEntity

        The model defined in huaweicloud sdk

        :param name: 环境标签名称。
        :type name: str
        :param business_id: 应用id。
        :type business_id: int
        :param uuid: UUID。
        :type uuid: str
        :param descp: 描述信息。
        :type descp: str
        :param creator_id: 创建者id。
        :type creator_id: int
        :param env_id_list: 环境id列表。
        :type env_id_list: list[int]
        :param id: 环境标签id。
        :type id: int
        :param gmt_create: 创建时间。
        :type gmt_create: str
        :param gmt_modify: 修改时间。
        :type gmt_modify: str
        """
        
        

        self._name = None
        self._business_id = None
        self._uuid = None
        self._descp = None
        self._creator_id = None
        self._env_id_list = None
        self._id = None
        self._gmt_create = None
        self._gmt_modify = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if business_id is not None:
            self.business_id = business_id
        if uuid is not None:
            self.uuid = uuid
        if descp is not None:
            self.descp = descp
        if creator_id is not None:
            self.creator_id = creator_id
        if env_id_list is not None:
            self.env_id_list = env_id_list
        if id is not None:
            self.id = id
        if gmt_create is not None:
            self.gmt_create = gmt_create
        if gmt_modify is not None:
            self.gmt_modify = gmt_modify

    @property
    def name(self):
        """Gets the name of this CmdbTagEntity.

        环境标签名称。

        :return: The name of this CmdbTagEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CmdbTagEntity.

        环境标签名称。

        :param name: The name of this CmdbTagEntity.
        :type name: str
        """
        self._name = name

    @property
    def business_id(self):
        """Gets the business_id of this CmdbTagEntity.

        应用id。

        :return: The business_id of this CmdbTagEntity.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this CmdbTagEntity.

        应用id。

        :param business_id: The business_id of this CmdbTagEntity.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def uuid(self):
        """Gets the uuid of this CmdbTagEntity.

        UUID。

        :return: The uuid of this CmdbTagEntity.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this CmdbTagEntity.

        UUID。

        :param uuid: The uuid of this CmdbTagEntity.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def descp(self):
        """Gets the descp of this CmdbTagEntity.

        描述信息。

        :return: The descp of this CmdbTagEntity.
        :rtype: str
        """
        return self._descp

    @descp.setter
    def descp(self, descp):
        """Sets the descp of this CmdbTagEntity.

        描述信息。

        :param descp: The descp of this CmdbTagEntity.
        :type descp: str
        """
        self._descp = descp

    @property
    def creator_id(self):
        """Gets the creator_id of this CmdbTagEntity.

        创建者id。

        :return: The creator_id of this CmdbTagEntity.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this CmdbTagEntity.

        创建者id。

        :param creator_id: The creator_id of this CmdbTagEntity.
        :type creator_id: int
        """
        self._creator_id = creator_id

    @property
    def env_id_list(self):
        """Gets the env_id_list of this CmdbTagEntity.

        环境id列表。

        :return: The env_id_list of this CmdbTagEntity.
        :rtype: list[int]
        """
        return self._env_id_list

    @env_id_list.setter
    def env_id_list(self, env_id_list):
        """Sets the env_id_list of this CmdbTagEntity.

        环境id列表。

        :param env_id_list: The env_id_list of this CmdbTagEntity.
        :type env_id_list: list[int]
        """
        self._env_id_list = env_id_list

    @property
    def id(self):
        """Gets the id of this CmdbTagEntity.

        环境标签id。

        :return: The id of this CmdbTagEntity.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CmdbTagEntity.

        环境标签id。

        :param id: The id of this CmdbTagEntity.
        :type id: int
        """
        self._id = id

    @property
    def gmt_create(self):
        """Gets the gmt_create of this CmdbTagEntity.

        创建时间。

        :return: The gmt_create of this CmdbTagEntity.
        :rtype: str
        """
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        """Sets the gmt_create of this CmdbTagEntity.

        创建时间。

        :param gmt_create: The gmt_create of this CmdbTagEntity.
        :type gmt_create: str
        """
        self._gmt_create = gmt_create

    @property
    def gmt_modify(self):
        """Gets the gmt_modify of this CmdbTagEntity.

        修改时间。

        :return: The gmt_modify of this CmdbTagEntity.
        :rtype: str
        """
        return self._gmt_modify

    @gmt_modify.setter
    def gmt_modify(self, gmt_modify):
        """Sets the gmt_modify of this CmdbTagEntity.

        修改时间。

        :param gmt_modify: The gmt_modify of this CmdbTagEntity.
        :type gmt_modify: str
        """
        self._gmt_modify = gmt_modify

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
        if not isinstance(other, CmdbTagEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
