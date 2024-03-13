# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo:

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
        'ingress_size': 'int',
        'charge_mode': 'str',
        'size': 'int',
        'name': 'str',
        'tags': 'list[AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfoTags]',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ingress_size': 'ingress_size',
        'charge_mode': 'charge_mode',
        'size': 'size',
        'name': 'name',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, id=None, ingress_size=None, charge_mode=None, size=None, name=None, tags=None, type=None):
        """BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param ingress_size: 全域公网带宽大小（入云方向）
        :type ingress_size: int
        :param charge_mode: 计费模式
        :type charge_mode: str
        :param size: 全域公网带宽大小（出云方向）
        :type size: int
        :param name: 资源名称
        :type name: str
        :param tags: 全域弹性公网IP标签
        :type tags: list[:class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfoTags`]
        :param type: 全域公网带宽类型
        :type type: str
        """
        
        

        self._id = None
        self._ingress_size = None
        self._charge_mode = None
        self._size = None
        self._name = None
        self._tags = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ingress_size is not None:
            self.ingress_size = ingress_size
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if size is not None:
            self.size = size
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        ID

        :return: The id of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        ID

        :param id: The id of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :type id: str
        """
        self._id = id

    @property
    def ingress_size(self):
        """Gets the ingress_size of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        全域公网带宽大小（入云方向）

        :return: The ingress_size of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :rtype: int
        """
        return self._ingress_size

    @ingress_size.setter
    def ingress_size(self, ingress_size):
        """Sets the ingress_size of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        全域公网带宽大小（入云方向）

        :param ingress_size: The ingress_size of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :type ingress_size: int
        """
        self._ingress_size = ingress_size

    @property
    def charge_mode(self):
        """Gets the charge_mode of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        计费模式

        :return: The charge_mode of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        计费模式

        :param charge_mode: The charge_mode of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def size(self):
        """Gets the size of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        全域公网带宽大小（出云方向）

        :return: The size of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        全域公网带宽大小（出云方向）

        :param size: The size of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :type size: int
        """
        self._size = size

    @property
    def name(self):
        """Gets the name of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        资源名称

        :return: The name of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        资源名称

        :param name: The name of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        """Gets the tags of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        全域弹性公网IP标签

        :return: The tags of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfoTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        全域弹性公网IP标签

        :param tags: The tags of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :type tags: list[:class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfoTags`]
        """
        self._tags = tags

    @property
    def type(self):
        """Gets the type of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        全域公网带宽类型

        :return: The type of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.

        全域公网带宽类型

        :param type: The type of this BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, BatchCreateGlobalEipRequestBodyGlobalEipInternetBandwidthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
