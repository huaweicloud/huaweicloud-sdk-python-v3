# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkOrderDetailVo:

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
        'sim_type': 'int',
        'status': 'int',
        'cid': 'str',
        'sim_card_id': 'int',
        'create_time': 'datetime',
        'finish_time': 'datetime',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sim_type': 'sim_type',
        'status': 'status',
        'cid': 'cid',
        'sim_card_id': 'sim_card_id',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'description': 'description'
    }

    def __init__(self, id=None, sim_type=None, status=None, cid=None, sim_card_id=None, create_time=None, finish_time=None, description=None):
        r"""WorkOrderDetailVo

        The model defined in huaweicloud sdk

        :param id: 业务受理ID
        :type id: int
        :param sim_type: SIM卡类型:3.实体卡
        :type sim_type: int
        :param status: 业务受理明细状态：1成功、2处理中、3失败
        :type status: int
        :param cid: 容器ID
        :type cid: str
        :param sim_card_id: SIM卡标识
        :type sim_card_id: int
        :param create_time: 创建时间
        :type create_time: datetime
        :param finish_time: 完成时间
        :type finish_time: datetime
        :param description: 描述
        :type description: str
        """
        
        

        self._id = None
        self._sim_type = None
        self._status = None
        self._cid = None
        self._sim_card_id = None
        self._create_time = None
        self._finish_time = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sim_type is not None:
            self.sim_type = sim_type
        if status is not None:
            self.status = status
        if cid is not None:
            self.cid = cid
        if sim_card_id is not None:
            self.sim_card_id = sim_card_id
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this WorkOrderDetailVo.

        业务受理ID

        :return: The id of this WorkOrderDetailVo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkOrderDetailVo.

        业务受理ID

        :param id: The id of this WorkOrderDetailVo.
        :type id: int
        """
        self._id = id

    @property
    def sim_type(self):
        r"""Gets the sim_type of this WorkOrderDetailVo.

        SIM卡类型:3.实体卡

        :return: The sim_type of this WorkOrderDetailVo.
        :rtype: int
        """
        return self._sim_type

    @sim_type.setter
    def sim_type(self, sim_type):
        r"""Sets the sim_type of this WorkOrderDetailVo.

        SIM卡类型:3.实体卡

        :param sim_type: The sim_type of this WorkOrderDetailVo.
        :type sim_type: int
        """
        self._sim_type = sim_type

    @property
    def status(self):
        r"""Gets the status of this WorkOrderDetailVo.

        业务受理明细状态：1成功、2处理中、3失败

        :return: The status of this WorkOrderDetailVo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WorkOrderDetailVo.

        业务受理明细状态：1成功、2处理中、3失败

        :param status: The status of this WorkOrderDetailVo.
        :type status: int
        """
        self._status = status

    @property
    def cid(self):
        r"""Gets the cid of this WorkOrderDetailVo.

        容器ID

        :return: The cid of this WorkOrderDetailVo.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        r"""Sets the cid of this WorkOrderDetailVo.

        容器ID

        :param cid: The cid of this WorkOrderDetailVo.
        :type cid: str
        """
        self._cid = cid

    @property
    def sim_card_id(self):
        r"""Gets the sim_card_id of this WorkOrderDetailVo.

        SIM卡标识

        :return: The sim_card_id of this WorkOrderDetailVo.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        r"""Sets the sim_card_id of this WorkOrderDetailVo.

        SIM卡标识

        :param sim_card_id: The sim_card_id of this WorkOrderDetailVo.
        :type sim_card_id: int
        """
        self._sim_card_id = sim_card_id

    @property
    def create_time(self):
        r"""Gets the create_time of this WorkOrderDetailVo.

        创建时间

        :return: The create_time of this WorkOrderDetailVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WorkOrderDetailVo.

        创建时间

        :param create_time: The create_time of this WorkOrderDetailVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this WorkOrderDetailVo.

        完成时间

        :return: The finish_time of this WorkOrderDetailVo.
        :rtype: datetime
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this WorkOrderDetailVo.

        完成时间

        :param finish_time: The finish_time of this WorkOrderDetailVo.
        :type finish_time: datetime
        """
        self._finish_time = finish_time

    @property
    def description(self):
        r"""Gets the description of this WorkOrderDetailVo.

        描述

        :return: The description of this WorkOrderDetailVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WorkOrderDetailVo.

        描述

        :param description: The description of this WorkOrderDetailVo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, WorkOrderDetailVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
