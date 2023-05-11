# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Bandwidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_type': 'str',
        'charge_mode': 'str',
        'create_time': 'str',
        'id': 'str',
        'name': 'str',
        'operator': 'Operator',
        'publicip_info': 'list[PublicipInfo]',
        'share_type': 'str',
        'site_id': 'str',
        'site_info': 'str',
        'size': 'int',
        'status': 'str',
        'update_time': 'str',
        'pool_id': 'str'
    }

    attribute_map = {
        'bandwidth_type': 'bandwidth_type',
        'charge_mode': 'charge_mode',
        'create_time': 'create_time',
        'id': 'id',
        'name': 'name',
        'operator': 'operator',
        'publicip_info': 'publicip_info',
        'share_type': 'share_type',
        'site_id': 'site_id',
        'site_info': 'site_info',
        'size': 'size',
        'status': 'status',
        'update_time': 'update_time',
        'pool_id': 'pool_id'
    }

    def __init__(self, bandwidth_type=None, charge_mode=None, create_time=None, id=None, name=None, operator=None, publicip_info=None, share_type=None, site_id=None, site_info=None, size=None, status=None, update_time=None, pool_id=None):
        """Bandwidth

        The model defined in huaweicloud sdk

        :param bandwidth_type: 带宽类型。 取值范围： share：共享类型
        :type bandwidth_type: str
        :param charge_mode: 计费模式，当前只支持峰值95计费。  取值范围：  - 95peak_plus：峰值95计费
        :type charge_mode: str
        :param create_time: 创建时间。
        :type create_time: str
        :param id: 带宽ID。
        :type id: str
        :param name: 带宽名称。
        :type name: str
        :param operator: 
        :type operator: :class:`huaweicloudsdkiec.v1.Operator`
        :param publicip_info: 弹性公网IP信息。
        :type publicip_info: list[:class:`huaweicloudsdkiec.v1.PublicipInfo`]
        :param share_type: 共享带宽类型，标识是否是共享带宽。  取值范围：  - WHOLE：共享带宽
        :type share_type: str
        :param site_id: 边缘站点ID。
        :type site_id: str
        :param site_info: 站点信息。
        :type site_info: str
        :param size: 带宽大小。
        :type size: int
        :param status: 带宽的状态。  取值范围：  - FREEZED：冻结  - NORMAL：正常
        :type status: str
        :param update_time: 更新时间。
        :type update_time: str
        :param pool_id: 线路ID。
        :type pool_id: str
        """
        
        

        self._bandwidth_type = None
        self._charge_mode = None
        self._create_time = None
        self._id = None
        self._name = None
        self._operator = None
        self._publicip_info = None
        self._share_type = None
        self._site_id = None
        self._site_info = None
        self._size = None
        self._status = None
        self._update_time = None
        self._pool_id = None
        self.discriminator = None

        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if create_time is not None:
            self.create_time = create_time
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if operator is not None:
            self.operator = operator
        if publicip_info is not None:
            self.publicip_info = publicip_info
        if share_type is not None:
            self.share_type = share_type
        if site_id is not None:
            self.site_id = site_id
        if site_info is not None:
            self.site_info = site_info
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        if update_time is not None:
            self.update_time = update_time
        if pool_id is not None:
            self.pool_id = pool_id

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this Bandwidth.

        带宽类型。 取值范围： share：共享类型

        :return: The bandwidth_type of this Bandwidth.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this Bandwidth.

        带宽类型。 取值范围： share：共享类型

        :param bandwidth_type: The bandwidth_type of this Bandwidth.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this Bandwidth.

        计费模式，当前只支持峰值95计费。  取值范围：  - 95peak_plus：峰值95计费

        :return: The charge_mode of this Bandwidth.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this Bandwidth.

        计费模式，当前只支持峰值95计费。  取值范围：  - 95peak_plus：峰值95计费

        :param charge_mode: The charge_mode of this Bandwidth.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def create_time(self):
        """Gets the create_time of this Bandwidth.

        创建时间。

        :return: The create_time of this Bandwidth.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Bandwidth.

        创建时间。

        :param create_time: The create_time of this Bandwidth.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def id(self):
        """Gets the id of this Bandwidth.

        带宽ID。

        :return: The id of this Bandwidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Bandwidth.

        带宽ID。

        :param id: The id of this Bandwidth.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Bandwidth.

        带宽名称。

        :return: The name of this Bandwidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Bandwidth.

        带宽名称。

        :param name: The name of this Bandwidth.
        :type name: str
        """
        self._name = name

    @property
    def operator(self):
        """Gets the operator of this Bandwidth.

        :return: The operator of this Bandwidth.
        :rtype: :class:`huaweicloudsdkiec.v1.Operator`
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Bandwidth.

        :param operator: The operator of this Bandwidth.
        :type operator: :class:`huaweicloudsdkiec.v1.Operator`
        """
        self._operator = operator

    @property
    def publicip_info(self):
        """Gets the publicip_info of this Bandwidth.

        弹性公网IP信息。

        :return: The publicip_info of this Bandwidth.
        :rtype: list[:class:`huaweicloudsdkiec.v1.PublicipInfo`]
        """
        return self._publicip_info

    @publicip_info.setter
    def publicip_info(self, publicip_info):
        """Sets the publicip_info of this Bandwidth.

        弹性公网IP信息。

        :param publicip_info: The publicip_info of this Bandwidth.
        :type publicip_info: list[:class:`huaweicloudsdkiec.v1.PublicipInfo`]
        """
        self._publicip_info = publicip_info

    @property
    def share_type(self):
        """Gets the share_type of this Bandwidth.

        共享带宽类型，标识是否是共享带宽。  取值范围：  - WHOLE：共享带宽

        :return: The share_type of this Bandwidth.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this Bandwidth.

        共享带宽类型，标识是否是共享带宽。  取值范围：  - WHOLE：共享带宽

        :param share_type: The share_type of this Bandwidth.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def site_id(self):
        """Gets the site_id of this Bandwidth.

        边缘站点ID。

        :return: The site_id of this Bandwidth.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Bandwidth.

        边缘站点ID。

        :param site_id: The site_id of this Bandwidth.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def site_info(self):
        """Gets the site_info of this Bandwidth.

        站点信息。

        :return: The site_info of this Bandwidth.
        :rtype: str
        """
        return self._site_info

    @site_info.setter
    def site_info(self, site_info):
        """Sets the site_info of this Bandwidth.

        站点信息。

        :param site_info: The site_info of this Bandwidth.
        :type site_info: str
        """
        self._site_info = site_info

    @property
    def size(self):
        """Gets the size of this Bandwidth.

        带宽大小。

        :return: The size of this Bandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Bandwidth.

        带宽大小。

        :param size: The size of this Bandwidth.
        :type size: int
        """
        self._size = size

    @property
    def status(self):
        """Gets the status of this Bandwidth.

        带宽的状态。  取值范围：  - FREEZED：冻结  - NORMAL：正常

        :return: The status of this Bandwidth.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Bandwidth.

        带宽的状态。  取值范围：  - FREEZED：冻结  - NORMAL：正常

        :param status: The status of this Bandwidth.
        :type status: str
        """
        self._status = status

    @property
    def update_time(self):
        """Gets the update_time of this Bandwidth.

        更新时间。

        :return: The update_time of this Bandwidth.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Bandwidth.

        更新时间。

        :param update_time: The update_time of this Bandwidth.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def pool_id(self):
        """Gets the pool_id of this Bandwidth.

        线路ID。

        :return: The pool_id of this Bandwidth.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this Bandwidth.

        线路ID。

        :param pool_id: The pool_id of this Bandwidth.
        :type pool_id: str
        """
        self._pool_id = pool_id

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
        if not isinstance(other, Bandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
