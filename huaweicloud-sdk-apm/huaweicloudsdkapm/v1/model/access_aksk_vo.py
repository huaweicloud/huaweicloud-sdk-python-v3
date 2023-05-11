# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessAkskVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'gmt_create': 'str',
        'gmt_modify': 'str',
        'inner_domain_id': 'int',
        'ak': 'str',
        'sk': 'str',
        'status': 'str',
        'descp': 'str'
    }

    attribute_map = {
        'id': 'id',
        'gmt_create': 'gmt_create',
        'gmt_modify': 'gmt_modify',
        'inner_domain_id': 'inner_domain_id',
        'ak': 'ak',
        'sk': 'sk',
        'status': 'status',
        'descp': 'descp'
    }

    def __init__(self, id=None, gmt_create=None, gmt_modify=None, inner_domain_id=None, ak=None, sk=None, status=None, descp=None):
        """AccessAkskVO

        The model defined in huaweicloud sdk

        :param id: ak/sk的id。
        :type id: int
        :param gmt_create: ak/sk的生成时间。
        :type gmt_create: str
        :param gmt_modify: ak/sk的修改时间。
        :type gmt_modify: str
        :param inner_domain_id: 内部租户id。
        :type inner_domain_id: int
        :param ak: 生成的ak。
        :type ak: str
        :param sk: 生成的sk。
        :type sk: str
        :param status: ak/sk的状态。
        :type status: str
        :param descp: ak/sk的描述信息。
        :type descp: str
        """
        
        

        self._id = None
        self._gmt_create = None
        self._gmt_modify = None
        self._inner_domain_id = None
        self._ak = None
        self._sk = None
        self._status = None
        self._descp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if gmt_create is not None:
            self.gmt_create = gmt_create
        if gmt_modify is not None:
            self.gmt_modify = gmt_modify
        if inner_domain_id is not None:
            self.inner_domain_id = inner_domain_id
        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk
        if status is not None:
            self.status = status
        if descp is not None:
            self.descp = descp

    @property
    def id(self):
        """Gets the id of this AccessAkskVO.

        ak/sk的id。

        :return: The id of this AccessAkskVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessAkskVO.

        ak/sk的id。

        :param id: The id of this AccessAkskVO.
        :type id: int
        """
        self._id = id

    @property
    def gmt_create(self):
        """Gets the gmt_create of this AccessAkskVO.

        ak/sk的生成时间。

        :return: The gmt_create of this AccessAkskVO.
        :rtype: str
        """
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        """Sets the gmt_create of this AccessAkskVO.

        ak/sk的生成时间。

        :param gmt_create: The gmt_create of this AccessAkskVO.
        :type gmt_create: str
        """
        self._gmt_create = gmt_create

    @property
    def gmt_modify(self):
        """Gets the gmt_modify of this AccessAkskVO.

        ak/sk的修改时间。

        :return: The gmt_modify of this AccessAkskVO.
        :rtype: str
        """
        return self._gmt_modify

    @gmt_modify.setter
    def gmt_modify(self, gmt_modify):
        """Sets the gmt_modify of this AccessAkskVO.

        ak/sk的修改时间。

        :param gmt_modify: The gmt_modify of this AccessAkskVO.
        :type gmt_modify: str
        """
        self._gmt_modify = gmt_modify

    @property
    def inner_domain_id(self):
        """Gets the inner_domain_id of this AccessAkskVO.

        内部租户id。

        :return: The inner_domain_id of this AccessAkskVO.
        :rtype: int
        """
        return self._inner_domain_id

    @inner_domain_id.setter
    def inner_domain_id(self, inner_domain_id):
        """Sets the inner_domain_id of this AccessAkskVO.

        内部租户id。

        :param inner_domain_id: The inner_domain_id of this AccessAkskVO.
        :type inner_domain_id: int
        """
        self._inner_domain_id = inner_domain_id

    @property
    def ak(self):
        """Gets the ak of this AccessAkskVO.

        生成的ak。

        :return: The ak of this AccessAkskVO.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this AccessAkskVO.

        生成的ak。

        :param ak: The ak of this AccessAkskVO.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this AccessAkskVO.

        生成的sk。

        :return: The sk of this AccessAkskVO.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this AccessAkskVO.

        生成的sk。

        :param sk: The sk of this AccessAkskVO.
        :type sk: str
        """
        self._sk = sk

    @property
    def status(self):
        """Gets the status of this AccessAkskVO.

        ak/sk的状态。

        :return: The status of this AccessAkskVO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccessAkskVO.

        ak/sk的状态。

        :param status: The status of this AccessAkskVO.
        :type status: str
        """
        self._status = status

    @property
    def descp(self):
        """Gets the descp of this AccessAkskVO.

        ak/sk的描述信息。

        :return: The descp of this AccessAkskVO.
        :rtype: str
        """
        return self._descp

    @descp.setter
    def descp(self, descp):
        """Sets the descp of this AccessAkskVO.

        ak/sk的描述信息。

        :param descp: The descp of this AccessAkskVO.
        :type descp: str
        """
        self._descp = descp

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
        if not isinstance(other, AccessAkskVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
