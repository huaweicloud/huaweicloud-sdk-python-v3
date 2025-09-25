# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'number': 'str',
        'title': 'str',
        'type': 'str',
        'sub_type': 'str',
        'model_code': 'str',
        'room_code': 'str',
        'room_name': 'str',
        'dc_name': 'str',
        'stage': 'str',
        'status': 'str',
        'applicant': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'number': 'number',
        'title': 'title',
        'type': 'type',
        'sub_type': 'sub_type',
        'model_code': 'model_code',
        'room_code': 'room_code',
        'room_name': 'room_name',
        'dc_name': 'dc_name',
        'stage': 'stage',
        'status': 'status',
        'applicant': 'applicant',
        'create_time': 'create_time'
    }

    def __init__(self, number=None, title=None, type=None, sub_type=None, model_code=None, room_code=None, room_name=None, dc_name=None, stage=None, status=None, applicant=None, create_time=None):
        r"""OrderItem

        The model defined in huaweicloud sdk

        :param number: 服务单号
        :type number: str
        :param title: 标题
        :type title: str
        :param type: 服务单类型:IDC运维 设备运维 设备检查 客户陪同
        :type type: str
        :param sub_type: 具体操作类型:设备物理上下电
        :type sub_type: str
        :param model_code: 服务单类型编码
        :type model_code: str
        :param room_code: 机房编码
        :type room_code: str
        :param room_name: 机房编码
        :type room_name: str
        :param dc_name: 机房编码
        :type dc_name: str
        :param stage: 当前阶段.DRAFT草稿、SUMMITED服务申请、IN_PROGRESS服务处理中、ACCEPTANCE服务验收、CLOSED服务关闭
        :type stage: str
        :param status: 当前状态
        :type status: str
        :param applicant: 申请人
        :type applicant: str
        :param create_time: 申请时间/创建时间
        :type create_time: str
        """
        
        

        self._number = None
        self._title = None
        self._type = None
        self._sub_type = None
        self._model_code = None
        self._room_code = None
        self._room_name = None
        self._dc_name = None
        self._stage = None
        self._status = None
        self._applicant = None
        self._create_time = None
        self.discriminator = None

        if number is not None:
            self.number = number
        self.title = title
        if type is not None:
            self.type = type
        if sub_type is not None:
            self.sub_type = sub_type
        self.model_code = model_code
        if room_code is not None:
            self.room_code = room_code
        if room_name is not None:
            self.room_name = room_name
        if dc_name is not None:
            self.dc_name = dc_name
        self.stage = stage
        if status is not None:
            self.status = status
        if applicant is not None:
            self.applicant = applicant
        if create_time is not None:
            self.create_time = create_time

    @property
    def number(self):
        r"""Gets the number of this OrderItem.

        服务单号

        :return: The number of this OrderItem.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this OrderItem.

        服务单号

        :param number: The number of this OrderItem.
        :type number: str
        """
        self._number = number

    @property
    def title(self):
        r"""Gets the title of this OrderItem.

        标题

        :return: The title of this OrderItem.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this OrderItem.

        标题

        :param title: The title of this OrderItem.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this OrderItem.

        服务单类型:IDC运维 设备运维 设备检查 客户陪同

        :return: The type of this OrderItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OrderItem.

        服务单类型:IDC运维 设备运维 设备检查 客户陪同

        :param type: The type of this OrderItem.
        :type type: str
        """
        self._type = type

    @property
    def sub_type(self):
        r"""Gets the sub_type of this OrderItem.

        具体操作类型:设备物理上下电

        :return: The sub_type of this OrderItem.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        r"""Sets the sub_type of this OrderItem.

        具体操作类型:设备物理上下电

        :param sub_type: The sub_type of this OrderItem.
        :type sub_type: str
        """
        self._sub_type = sub_type

    @property
    def model_code(self):
        r"""Gets the model_code of this OrderItem.

        服务单类型编码

        :return: The model_code of this OrderItem.
        :rtype: str
        """
        return self._model_code

    @model_code.setter
    def model_code(self, model_code):
        r"""Sets the model_code of this OrderItem.

        服务单类型编码

        :param model_code: The model_code of this OrderItem.
        :type model_code: str
        """
        self._model_code = model_code

    @property
    def room_code(self):
        r"""Gets the room_code of this OrderItem.

        机房编码

        :return: The room_code of this OrderItem.
        :rtype: str
        """
        return self._room_code

    @room_code.setter
    def room_code(self, room_code):
        r"""Sets the room_code of this OrderItem.

        机房编码

        :param room_code: The room_code of this OrderItem.
        :type room_code: str
        """
        self._room_code = room_code

    @property
    def room_name(self):
        r"""Gets the room_name of this OrderItem.

        机房编码

        :return: The room_name of this OrderItem.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        r"""Sets the room_name of this OrderItem.

        机房编码

        :param room_name: The room_name of this OrderItem.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def dc_name(self):
        r"""Gets the dc_name of this OrderItem.

        机房编码

        :return: The dc_name of this OrderItem.
        :rtype: str
        """
        return self._dc_name

    @dc_name.setter
    def dc_name(self, dc_name):
        r"""Sets the dc_name of this OrderItem.

        机房编码

        :param dc_name: The dc_name of this OrderItem.
        :type dc_name: str
        """
        self._dc_name = dc_name

    @property
    def stage(self):
        r"""Gets the stage of this OrderItem.

        当前阶段.DRAFT草稿、SUMMITED服务申请、IN_PROGRESS服务处理中、ACCEPTANCE服务验收、CLOSED服务关闭

        :return: The stage of this OrderItem.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this OrderItem.

        当前阶段.DRAFT草稿、SUMMITED服务申请、IN_PROGRESS服务处理中、ACCEPTANCE服务验收、CLOSED服务关闭

        :param stage: The stage of this OrderItem.
        :type stage: str
        """
        self._stage = stage

    @property
    def status(self):
        r"""Gets the status of this OrderItem.

        当前状态

        :return: The status of this OrderItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OrderItem.

        当前状态

        :param status: The status of this OrderItem.
        :type status: str
        """
        self._status = status

    @property
    def applicant(self):
        r"""Gets the applicant of this OrderItem.

        申请人

        :return: The applicant of this OrderItem.
        :rtype: str
        """
        return self._applicant

    @applicant.setter
    def applicant(self, applicant):
        r"""Sets the applicant of this OrderItem.

        申请人

        :param applicant: The applicant of this OrderItem.
        :type applicant: str
        """
        self._applicant = applicant

    @property
    def create_time(self):
        r"""Gets the create_time of this OrderItem.

        申请时间/创建时间

        :return: The create_time of this OrderItem.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this OrderItem.

        申请时间/创建时间

        :param create_time: The create_time of this OrderItem.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, OrderItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
