# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryResourceResultDTO:

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
        'type_id': 'str',
        'type_desc': 'str',
        'vmr_mode': 'int',
        'count': 'int',
        'expire_date': 'int',
        'order_id': 'str',
        'status': 'int',
        'editable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'type_id': 'typeId',
        'type_desc': 'typeDesc',
        'vmr_mode': 'vmrMode',
        'count': 'count',
        'expire_date': 'expireDate',
        'order_id': 'orderId',
        'status': 'status',
        'editable': 'editable'
    }

    def __init__(self, id=None, type=None, type_id=None, type_desc=None, vmr_mode=None, count=None, expire_date=None, order_id=None, status=None, editable=None):
        """QueryResourceResultDTO

        The model defined in huaweicloud sdk

        :param id: 唯一标识若携带则以携带为准，企业内保证唯一，否则后台自动生成UUID。
        :type id: str
        :param type: 资源类型。 - VMR        - 云会议室 - CONF_CALL  - 会议并发数 - HARD_1080P - 1080P硬终端 - HARD_720P  - 720P硬终端 - SOFT       - 软终端用户数 - ROOM       - 大屏软终端 - LIVE       - 直播推流 - RECORD     - 录播空间 - HARD_THIRD_PARTY - 第三方硬终端帐号 - HUAWEI_VISION -智慧屏 - IDEA_HUB   - ideahub
        :type type: str
        :param type_id: 资源标识，比如资源类型为VMR，则该参数为vmrPkgId。
        :type type_id: str
        :param type_desc: 资源标识对应的回显描述,比如资源类型为VMR，则该参数为vmrPkgName。
        :type type_desc: str
        :param vmr_mode: VMR模式。 - 0：个人会议ID - 1：云会议室 - 2：网络研讨会
        :type vmr_mode: int
        :param count: 资源数量。
        :type count: int
        :param expire_date: 到期时间,utc时间戳。
        :type expire_date: int
        :param order_id: 资源对应的订单id。
        :type order_id: str
        :param status: 资源状态: - 0：正常 - 1：到期 - 2：停用
        :type status: int
        :param editable: 标识资源是否可以编辑或删除。
        :type editable: bool
        """
        
        

        self._id = None
        self._type = None
        self._type_id = None
        self._type_desc = None
        self._vmr_mode = None
        self._count = None
        self._expire_date = None
        self._order_id = None
        self._status = None
        self._editable = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if type_id is not None:
            self.type_id = type_id
        if type_desc is not None:
            self.type_desc = type_desc
        if vmr_mode is not None:
            self.vmr_mode = vmr_mode
        if count is not None:
            self.count = count
        if expire_date is not None:
            self.expire_date = expire_date
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status
        if editable is not None:
            self.editable = editable

    @property
    def id(self):
        """Gets the id of this QueryResourceResultDTO.

        唯一标识若携带则以携带为准，企业内保证唯一，否则后台自动生成UUID。

        :return: The id of this QueryResourceResultDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryResourceResultDTO.

        唯一标识若携带则以携带为准，企业内保证唯一，否则后台自动生成UUID。

        :param id: The id of this QueryResourceResultDTO.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this QueryResourceResultDTO.

        资源类型。 - VMR        - 云会议室 - CONF_CALL  - 会议并发数 - HARD_1080P - 1080P硬终端 - HARD_720P  - 720P硬终端 - SOFT       - 软终端用户数 - ROOM       - 大屏软终端 - LIVE       - 直播推流 - RECORD     - 录播空间 - HARD_THIRD_PARTY - 第三方硬终端帐号 - HUAWEI_VISION -智慧屏 - IDEA_HUB   - ideahub

        :return: The type of this QueryResourceResultDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QueryResourceResultDTO.

        资源类型。 - VMR        - 云会议室 - CONF_CALL  - 会议并发数 - HARD_1080P - 1080P硬终端 - HARD_720P  - 720P硬终端 - SOFT       - 软终端用户数 - ROOM       - 大屏软终端 - LIVE       - 直播推流 - RECORD     - 录播空间 - HARD_THIRD_PARTY - 第三方硬终端帐号 - HUAWEI_VISION -智慧屏 - IDEA_HUB   - ideahub

        :param type: The type of this QueryResourceResultDTO.
        :type type: str
        """
        self._type = type

    @property
    def type_id(self):
        """Gets the type_id of this QueryResourceResultDTO.

        资源标识，比如资源类型为VMR，则该参数为vmrPkgId。

        :return: The type_id of this QueryResourceResultDTO.
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this QueryResourceResultDTO.

        资源标识，比如资源类型为VMR，则该参数为vmrPkgId。

        :param type_id: The type_id of this QueryResourceResultDTO.
        :type type_id: str
        """
        self._type_id = type_id

    @property
    def type_desc(self):
        """Gets the type_desc of this QueryResourceResultDTO.

        资源标识对应的回显描述,比如资源类型为VMR，则该参数为vmrPkgName。

        :return: The type_desc of this QueryResourceResultDTO.
        :rtype: str
        """
        return self._type_desc

    @type_desc.setter
    def type_desc(self, type_desc):
        """Sets the type_desc of this QueryResourceResultDTO.

        资源标识对应的回显描述,比如资源类型为VMR，则该参数为vmrPkgName。

        :param type_desc: The type_desc of this QueryResourceResultDTO.
        :type type_desc: str
        """
        self._type_desc = type_desc

    @property
    def vmr_mode(self):
        """Gets the vmr_mode of this QueryResourceResultDTO.

        VMR模式。 - 0：个人会议ID - 1：云会议室 - 2：网络研讨会

        :return: The vmr_mode of this QueryResourceResultDTO.
        :rtype: int
        """
        return self._vmr_mode

    @vmr_mode.setter
    def vmr_mode(self, vmr_mode):
        """Sets the vmr_mode of this QueryResourceResultDTO.

        VMR模式。 - 0：个人会议ID - 1：云会议室 - 2：网络研讨会

        :param vmr_mode: The vmr_mode of this QueryResourceResultDTO.
        :type vmr_mode: int
        """
        self._vmr_mode = vmr_mode

    @property
    def count(self):
        """Gets the count of this QueryResourceResultDTO.

        资源数量。

        :return: The count of this QueryResourceResultDTO.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this QueryResourceResultDTO.

        资源数量。

        :param count: The count of this QueryResourceResultDTO.
        :type count: int
        """
        self._count = count

    @property
    def expire_date(self):
        """Gets the expire_date of this QueryResourceResultDTO.

        到期时间,utc时间戳。

        :return: The expire_date of this QueryResourceResultDTO.
        :rtype: int
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this QueryResourceResultDTO.

        到期时间,utc时间戳。

        :param expire_date: The expire_date of this QueryResourceResultDTO.
        :type expire_date: int
        """
        self._expire_date = expire_date

    @property
    def order_id(self):
        """Gets the order_id of this QueryResourceResultDTO.

        资源对应的订单id。

        :return: The order_id of this QueryResourceResultDTO.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this QueryResourceResultDTO.

        资源对应的订单id。

        :param order_id: The order_id of this QueryResourceResultDTO.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def status(self):
        """Gets the status of this QueryResourceResultDTO.

        资源状态: - 0：正常 - 1：到期 - 2：停用

        :return: The status of this QueryResourceResultDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryResourceResultDTO.

        资源状态: - 0：正常 - 1：到期 - 2：停用

        :param status: The status of this QueryResourceResultDTO.
        :type status: int
        """
        self._status = status

    @property
    def editable(self):
        """Gets the editable of this QueryResourceResultDTO.

        标识资源是否可以编辑或删除。

        :return: The editable of this QueryResourceResultDTO.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this QueryResourceResultDTO.

        标识资源是否可以编辑或删除。

        :param editable: The editable of this QueryResourceResultDTO.
        :type editable: bool
        """
        self._editable = editable

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
        if not isinstance(other, QueryResourceResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
