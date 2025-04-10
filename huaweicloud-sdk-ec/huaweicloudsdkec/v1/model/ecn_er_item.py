# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EcnErItem:

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
        'er_id': 'str',
        'region_id': 'str',
        'status': 'str',
        'health_status': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'er_id': 'er_id',
        'region_id': 'region_id',
        'status': 'status',
        'health_status': 'health_status',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, er_id=None, region_id=None, status=None, health_status=None, created_at=None):
        r"""EcnErItem

        The model defined in huaweicloud sdk

        :param id: 企业连接网络关联企业路由器ID
        :type id: str
        :param er_id: 企业路由器ID
        :type er_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param status: 状态
        :type status: str
        :param health_status: 健康状态
        :type health_status: str
        :param created_at: 创建时间
        :type created_at: datetime
        """
        
        

        self._id = None
        self._er_id = None
        self._region_id = None
        self._status = None
        self._health_status = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.er_id = er_id
        self.region_id = region_id
        if status is not None:
            self.status = status
        if health_status is not None:
            self.health_status = health_status
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this EcnErItem.

        企业连接网络关联企业路由器ID

        :return: The id of this EcnErItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EcnErItem.

        企业连接网络关联企业路由器ID

        :param id: The id of this EcnErItem.
        :type id: str
        """
        self._id = id

    @property
    def er_id(self):
        r"""Gets the er_id of this EcnErItem.

        企业路由器ID

        :return: The er_id of this EcnErItem.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        r"""Sets the er_id of this EcnErItem.

        企业路由器ID

        :param er_id: The er_id of this EcnErItem.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def region_id(self):
        r"""Gets the region_id of this EcnErItem.

        区域ID

        :return: The region_id of this EcnErItem.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this EcnErItem.

        区域ID

        :param region_id: The region_id of this EcnErItem.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def status(self):
        r"""Gets the status of this EcnErItem.

        状态

        :return: The status of this EcnErItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EcnErItem.

        状态

        :param status: The status of this EcnErItem.
        :type status: str
        """
        self._status = status

    @property
    def health_status(self):
        r"""Gets the health_status of this EcnErItem.

        健康状态

        :return: The health_status of this EcnErItem.
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        r"""Sets the health_status of this EcnErItem.

        健康状态

        :param health_status: The health_status of this EcnErItem.
        :type health_status: str
        """
        self._health_status = health_status

    @property
    def created_at(self):
        r"""Gets the created_at of this EcnErItem.

        创建时间

        :return: The created_at of this EcnErItem.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this EcnErItem.

        创建时间

        :param created_at: The created_at of this EcnErItem.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, EcnErItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
