# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CategoryQuotingItemStep:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step_id': 'str',
        'step_no': 'str',
        'step_start': 'decimal.Decimal',
        'start_measure_id': 'int',
        'step_end': 'decimal.Decimal',
        'end_measure_id': 'int',
        'effective_time': 'str',
        'expire_time': 'str',
        'site_code': 'str'
    }

    attribute_map = {
        'step_id': 'step_id',
        'step_no': 'step_no',
        'step_start': 'step_start',
        'start_measure_id': 'start_measure_id',
        'step_end': 'step_end',
        'end_measure_id': 'end_measure_id',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time',
        'site_code': 'site_code'
    }

    def __init__(self, step_id=None, step_no=None, step_start=None, start_measure_id=None, step_end=None, end_measure_id=None, effective_time=None, expire_time=None, site_code=None):
        r"""CategoryQuotingItemStep

        The model defined in huaweicloud sdk

        :param step_id: 阶梯ID
        :type step_id: str
        :param step_no: 阶梯编号
        :type step_no: str
        :param step_start: 阶梯起始值
        :type step_start: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param start_measure_id: 起始值度量单位
        :type start_measure_id: int
        :param step_end: 阶梯结束值
        :type step_end: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param end_measure_id: 结束值度量单位
        :type end_measure_id: int
        :param effective_time: 阶梯生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ
        :type effective_time: str
        :param expire_time: 阶梯失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ
        :type expire_time: str
        :param site_code: 运营站点编码
        :type site_code: str
        """
        
        

        self._step_id = None
        self._step_no = None
        self._step_start = None
        self._start_measure_id = None
        self._step_end = None
        self._end_measure_id = None
        self._effective_time = None
        self._expire_time = None
        self._site_code = None
        self.discriminator = None

        if step_id is not None:
            self.step_id = step_id
        if step_no is not None:
            self.step_no = step_no
        if step_start is not None:
            self.step_start = step_start
        if start_measure_id is not None:
            self.start_measure_id = start_measure_id
        if step_end is not None:
            self.step_end = step_end
        if end_measure_id is not None:
            self.end_measure_id = end_measure_id
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time
        if site_code is not None:
            self.site_code = site_code

    @property
    def step_id(self):
        r"""Gets the step_id of this CategoryQuotingItemStep.

        阶梯ID

        :return: The step_id of this CategoryQuotingItemStep.
        :rtype: str
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        r"""Sets the step_id of this CategoryQuotingItemStep.

        阶梯ID

        :param step_id: The step_id of this CategoryQuotingItemStep.
        :type step_id: str
        """
        self._step_id = step_id

    @property
    def step_no(self):
        r"""Gets the step_no of this CategoryQuotingItemStep.

        阶梯编号

        :return: The step_no of this CategoryQuotingItemStep.
        :rtype: str
        """
        return self._step_no

    @step_no.setter
    def step_no(self, step_no):
        r"""Sets the step_no of this CategoryQuotingItemStep.

        阶梯编号

        :param step_no: The step_no of this CategoryQuotingItemStep.
        :type step_no: str
        """
        self._step_no = step_no

    @property
    def step_start(self):
        r"""Gets the step_start of this CategoryQuotingItemStep.

        阶梯起始值

        :return: The step_start of this CategoryQuotingItemStep.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._step_start

    @step_start.setter
    def step_start(self, step_start):
        r"""Sets the step_start of this CategoryQuotingItemStep.

        阶梯起始值

        :param step_start: The step_start of this CategoryQuotingItemStep.
        :type step_start: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._step_start = step_start

    @property
    def start_measure_id(self):
        r"""Gets the start_measure_id of this CategoryQuotingItemStep.

        起始值度量单位

        :return: The start_measure_id of this CategoryQuotingItemStep.
        :rtype: int
        """
        return self._start_measure_id

    @start_measure_id.setter
    def start_measure_id(self, start_measure_id):
        r"""Sets the start_measure_id of this CategoryQuotingItemStep.

        起始值度量单位

        :param start_measure_id: The start_measure_id of this CategoryQuotingItemStep.
        :type start_measure_id: int
        """
        self._start_measure_id = start_measure_id

    @property
    def step_end(self):
        r"""Gets the step_end of this CategoryQuotingItemStep.

        阶梯结束值

        :return: The step_end of this CategoryQuotingItemStep.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._step_end

    @step_end.setter
    def step_end(self, step_end):
        r"""Sets the step_end of this CategoryQuotingItemStep.

        阶梯结束值

        :param step_end: The step_end of this CategoryQuotingItemStep.
        :type step_end: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._step_end = step_end

    @property
    def end_measure_id(self):
        r"""Gets the end_measure_id of this CategoryQuotingItemStep.

        结束值度量单位

        :return: The end_measure_id of this CategoryQuotingItemStep.
        :rtype: int
        """
        return self._end_measure_id

    @end_measure_id.setter
    def end_measure_id(self, end_measure_id):
        r"""Sets the end_measure_id of this CategoryQuotingItemStep.

        结束值度量单位

        :param end_measure_id: The end_measure_id of this CategoryQuotingItemStep.
        :type end_measure_id: int
        """
        self._end_measure_id = end_measure_id

    @property
    def effective_time(self):
        r"""Gets the effective_time of this CategoryQuotingItemStep.

        阶梯生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The effective_time of this CategoryQuotingItemStep.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this CategoryQuotingItemStep.

        阶梯生效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param effective_time: The effective_time of this CategoryQuotingItemStep.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CategoryQuotingItemStep.

        阶梯失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The expire_time of this CategoryQuotingItemStep.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CategoryQuotingItemStep.

        阶梯失效时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param expire_time: The expire_time of this CategoryQuotingItemStep.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def site_code(self):
        r"""Gets the site_code of this CategoryQuotingItemStep.

        运营站点编码

        :return: The site_code of this CategoryQuotingItemStep.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this CategoryQuotingItemStep.

        运营站点编码

        :param site_code: The site_code of this CategoryQuotingItemStep.
        :type site_code: str
        """
        self._site_code = site_code

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CategoryQuotingItemStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
