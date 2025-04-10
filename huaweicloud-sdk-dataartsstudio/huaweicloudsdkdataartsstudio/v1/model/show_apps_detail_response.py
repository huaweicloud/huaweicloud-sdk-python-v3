# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppsDetailResponse(SdkResponse):

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
        'name': 'str',
        'call_num': 'int',
        'success_num': 'int',
        'fail_num': 'int',
        'legal_num': 'int',
        'illegal_num': 'int',
        'cost_time_avg': 'float',
        'success_cost_time_avg': 'float',
        'fail_cost_time_avg': 'float',
        'success_rate': 'float',
        'fail_rate': 'float',
        'legal_rate': 'float',
        'illegal_rate': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'call_num': 'call_num',
        'success_num': 'success_num',
        'fail_num': 'fail_num',
        'legal_num': 'legal_num',
        'illegal_num': 'illegal_num',
        'cost_time_avg': 'cost_time_avg',
        'success_cost_time_avg': 'success_cost_time_avg',
        'fail_cost_time_avg': 'fail_cost_time_avg',
        'success_rate': 'success_rate',
        'fail_rate': 'fail_rate',
        'legal_rate': 'legal_rate',
        'illegal_rate': 'illegal_rate'
    }

    def __init__(self, id=None, name=None, call_num=None, success_num=None, fail_num=None, legal_num=None, illegal_num=None, cost_time_avg=None, success_cost_time_avg=None, fail_cost_time_avg=None, success_rate=None, fail_rate=None, legal_rate=None, illegal_rate=None):
        r"""ShowAppsDetailResponse

        The model defined in huaweicloud sdk

        :param id: 统计对象编号
        :type id: str
        :param name: 统计对象名称
        :type name: str
        :param call_num: 调用总量
        :type call_num: int
        :param success_num: 成功调用量(取数成功)
        :type success_num: int
        :param fail_num: 失败调用量(取数失败)
        :type fail_num: int
        :param legal_num: 合法调用量(通过校验)
        :type legal_num: int
        :param illegal_num: 非法调用量(无法通过校验)
        :type illegal_num: int
        :param cost_time_avg: 请求平均时长
        :type cost_time_avg: float
        :param success_cost_time_avg: 成功请求平均时长
        :type success_cost_time_avg: float
        :param fail_cost_time_avg: 失败请求平均时长
        :type fail_cost_time_avg: float
        :param success_rate: 成功率
        :type success_rate: float
        :param fail_rate: 失败率
        :type fail_rate: float
        :param legal_rate: 合法率
        :type legal_rate: float
        :param illegal_rate: 非法率
        :type illegal_rate: float
        """
        
        super(ShowAppsDetailResponse, self).__init__()

        self._id = None
        self._name = None
        self._call_num = None
        self._success_num = None
        self._fail_num = None
        self._legal_num = None
        self._illegal_num = None
        self._cost_time_avg = None
        self._success_cost_time_avg = None
        self._fail_cost_time_avg = None
        self._success_rate = None
        self._fail_rate = None
        self._legal_rate = None
        self._illegal_rate = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if call_num is not None:
            self.call_num = call_num
        if success_num is not None:
            self.success_num = success_num
        if fail_num is not None:
            self.fail_num = fail_num
        if legal_num is not None:
            self.legal_num = legal_num
        if illegal_num is not None:
            self.illegal_num = illegal_num
        if cost_time_avg is not None:
            self.cost_time_avg = cost_time_avg
        if success_cost_time_avg is not None:
            self.success_cost_time_avg = success_cost_time_avg
        if fail_cost_time_avg is not None:
            self.fail_cost_time_avg = fail_cost_time_avg
        if success_rate is not None:
            self.success_rate = success_rate
        if fail_rate is not None:
            self.fail_rate = fail_rate
        if legal_rate is not None:
            self.legal_rate = legal_rate
        if illegal_rate is not None:
            self.illegal_rate = illegal_rate

    @property
    def id(self):
        r"""Gets the id of this ShowAppsDetailResponse.

        统计对象编号

        :return: The id of this ShowAppsDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAppsDetailResponse.

        统计对象编号

        :param id: The id of this ShowAppsDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowAppsDetailResponse.

        统计对象名称

        :return: The name of this ShowAppsDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowAppsDetailResponse.

        统计对象名称

        :param name: The name of this ShowAppsDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def call_num(self):
        r"""Gets the call_num of this ShowAppsDetailResponse.

        调用总量

        :return: The call_num of this ShowAppsDetailResponse.
        :rtype: int
        """
        return self._call_num

    @call_num.setter
    def call_num(self, call_num):
        r"""Sets the call_num of this ShowAppsDetailResponse.

        调用总量

        :param call_num: The call_num of this ShowAppsDetailResponse.
        :type call_num: int
        """
        self._call_num = call_num

    @property
    def success_num(self):
        r"""Gets the success_num of this ShowAppsDetailResponse.

        成功调用量(取数成功)

        :return: The success_num of this ShowAppsDetailResponse.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        r"""Sets the success_num of this ShowAppsDetailResponse.

        成功调用量(取数成功)

        :param success_num: The success_num of this ShowAppsDetailResponse.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def fail_num(self):
        r"""Gets the fail_num of this ShowAppsDetailResponse.

        失败调用量(取数失败)

        :return: The fail_num of this ShowAppsDetailResponse.
        :rtype: int
        """
        return self._fail_num

    @fail_num.setter
    def fail_num(self, fail_num):
        r"""Sets the fail_num of this ShowAppsDetailResponse.

        失败调用量(取数失败)

        :param fail_num: The fail_num of this ShowAppsDetailResponse.
        :type fail_num: int
        """
        self._fail_num = fail_num

    @property
    def legal_num(self):
        r"""Gets the legal_num of this ShowAppsDetailResponse.

        合法调用量(通过校验)

        :return: The legal_num of this ShowAppsDetailResponse.
        :rtype: int
        """
        return self._legal_num

    @legal_num.setter
    def legal_num(self, legal_num):
        r"""Sets the legal_num of this ShowAppsDetailResponse.

        合法调用量(通过校验)

        :param legal_num: The legal_num of this ShowAppsDetailResponse.
        :type legal_num: int
        """
        self._legal_num = legal_num

    @property
    def illegal_num(self):
        r"""Gets the illegal_num of this ShowAppsDetailResponse.

        非法调用量(无法通过校验)

        :return: The illegal_num of this ShowAppsDetailResponse.
        :rtype: int
        """
        return self._illegal_num

    @illegal_num.setter
    def illegal_num(self, illegal_num):
        r"""Sets the illegal_num of this ShowAppsDetailResponse.

        非法调用量(无法通过校验)

        :param illegal_num: The illegal_num of this ShowAppsDetailResponse.
        :type illegal_num: int
        """
        self._illegal_num = illegal_num

    @property
    def cost_time_avg(self):
        r"""Gets the cost_time_avg of this ShowAppsDetailResponse.

        请求平均时长

        :return: The cost_time_avg of this ShowAppsDetailResponse.
        :rtype: float
        """
        return self._cost_time_avg

    @cost_time_avg.setter
    def cost_time_avg(self, cost_time_avg):
        r"""Sets the cost_time_avg of this ShowAppsDetailResponse.

        请求平均时长

        :param cost_time_avg: The cost_time_avg of this ShowAppsDetailResponse.
        :type cost_time_avg: float
        """
        self._cost_time_avg = cost_time_avg

    @property
    def success_cost_time_avg(self):
        r"""Gets the success_cost_time_avg of this ShowAppsDetailResponse.

        成功请求平均时长

        :return: The success_cost_time_avg of this ShowAppsDetailResponse.
        :rtype: float
        """
        return self._success_cost_time_avg

    @success_cost_time_avg.setter
    def success_cost_time_avg(self, success_cost_time_avg):
        r"""Sets the success_cost_time_avg of this ShowAppsDetailResponse.

        成功请求平均时长

        :param success_cost_time_avg: The success_cost_time_avg of this ShowAppsDetailResponse.
        :type success_cost_time_avg: float
        """
        self._success_cost_time_avg = success_cost_time_avg

    @property
    def fail_cost_time_avg(self):
        r"""Gets the fail_cost_time_avg of this ShowAppsDetailResponse.

        失败请求平均时长

        :return: The fail_cost_time_avg of this ShowAppsDetailResponse.
        :rtype: float
        """
        return self._fail_cost_time_avg

    @fail_cost_time_avg.setter
    def fail_cost_time_avg(self, fail_cost_time_avg):
        r"""Sets the fail_cost_time_avg of this ShowAppsDetailResponse.

        失败请求平均时长

        :param fail_cost_time_avg: The fail_cost_time_avg of this ShowAppsDetailResponse.
        :type fail_cost_time_avg: float
        """
        self._fail_cost_time_avg = fail_cost_time_avg

    @property
    def success_rate(self):
        r"""Gets the success_rate of this ShowAppsDetailResponse.

        成功率

        :return: The success_rate of this ShowAppsDetailResponse.
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        r"""Sets the success_rate of this ShowAppsDetailResponse.

        成功率

        :param success_rate: The success_rate of this ShowAppsDetailResponse.
        :type success_rate: float
        """
        self._success_rate = success_rate

    @property
    def fail_rate(self):
        r"""Gets the fail_rate of this ShowAppsDetailResponse.

        失败率

        :return: The fail_rate of this ShowAppsDetailResponse.
        :rtype: float
        """
        return self._fail_rate

    @fail_rate.setter
    def fail_rate(self, fail_rate):
        r"""Sets the fail_rate of this ShowAppsDetailResponse.

        失败率

        :param fail_rate: The fail_rate of this ShowAppsDetailResponse.
        :type fail_rate: float
        """
        self._fail_rate = fail_rate

    @property
    def legal_rate(self):
        r"""Gets the legal_rate of this ShowAppsDetailResponse.

        合法率

        :return: The legal_rate of this ShowAppsDetailResponse.
        :rtype: float
        """
        return self._legal_rate

    @legal_rate.setter
    def legal_rate(self, legal_rate):
        r"""Sets the legal_rate of this ShowAppsDetailResponse.

        合法率

        :param legal_rate: The legal_rate of this ShowAppsDetailResponse.
        :type legal_rate: float
        """
        self._legal_rate = legal_rate

    @property
    def illegal_rate(self):
        r"""Gets the illegal_rate of this ShowAppsDetailResponse.

        非法率

        :return: The illegal_rate of this ShowAppsDetailResponse.
        :rtype: float
        """
        return self._illegal_rate

    @illegal_rate.setter
    def illegal_rate(self, illegal_rate):
        r"""Sets the illegal_rate of this ShowAppsDetailResponse.

        非法率

        :param illegal_rate: The illegal_rate of this ShowAppsDetailResponse.
        :type illegal_rate: float
        """
        self._illegal_rate = illegal_rate

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
        if not isinstance(other, ShowAppsDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
