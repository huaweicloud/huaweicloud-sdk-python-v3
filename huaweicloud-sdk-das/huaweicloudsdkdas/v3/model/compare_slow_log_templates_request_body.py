# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareSlowLogTemplatesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cur_page': 'int',
        'per_page': 'int',
        'comparative_start_time': 'int',
        'comparative_end_time': 'int',
        'base_line_start_time': 'int',
        'base_line_end_time': 'int'
    }

    attribute_map = {
        'cur_page': 'cur_page',
        'per_page': 'per_page',
        'comparative_start_time': 'comparative_start_time',
        'comparative_end_time': 'comparative_end_time',
        'base_line_start_time': 'base_line_start_time',
        'base_line_end_time': 'base_line_end_time'
    }

    def __init__(self, cur_page=None, per_page=None, comparative_start_time=None, comparative_end_time=None, base_line_start_time=None, base_line_end_time=None):
        r"""CompareSlowLogTemplatesRequestBody

        The model defined in huaweicloud sdk

        :param cur_page: 页码
        :type cur_page: int
        :param per_page: 每页记录数
        :type per_page: int
        :param comparative_start_time: 对比日期开始时间（Unix timestamp），单位：毫秒
        :type comparative_start_time: int
        :param comparative_end_time: 对比日期结束时间（Unix timestamp），单位：毫秒
        :type comparative_end_time: int
        :param base_line_start_time: 基线日期开始时间（Unix timestamp），单位：毫秒
        :type base_line_start_time: int
        :param base_line_end_time: 基线日期结束时间（Unix timestamp），单位：毫秒
        :type base_line_end_time: int
        """
        
        

        self._cur_page = None
        self._per_page = None
        self._comparative_start_time = None
        self._comparative_end_time = None
        self._base_line_start_time = None
        self._base_line_end_time = None
        self.discriminator = None

        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page
        if comparative_start_time is not None:
            self.comparative_start_time = comparative_start_time
        if comparative_end_time is not None:
            self.comparative_end_time = comparative_end_time
        if base_line_start_time is not None:
            self.base_line_start_time = base_line_start_time
        if base_line_end_time is not None:
            self.base_line_end_time = base_line_end_time

    @property
    def cur_page(self):
        r"""Gets the cur_page of this CompareSlowLogTemplatesRequestBody.

        页码

        :return: The cur_page of this CompareSlowLogTemplatesRequestBody.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this CompareSlowLogTemplatesRequestBody.

        页码

        :param cur_page: The cur_page of this CompareSlowLogTemplatesRequestBody.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this CompareSlowLogTemplatesRequestBody.

        每页记录数

        :return: The per_page of this CompareSlowLogTemplatesRequestBody.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this CompareSlowLogTemplatesRequestBody.

        每页记录数

        :param per_page: The per_page of this CompareSlowLogTemplatesRequestBody.
        :type per_page: int
        """
        self._per_page = per_page

    @property
    def comparative_start_time(self):
        r"""Gets the comparative_start_time of this CompareSlowLogTemplatesRequestBody.

        对比日期开始时间（Unix timestamp），单位：毫秒

        :return: The comparative_start_time of this CompareSlowLogTemplatesRequestBody.
        :rtype: int
        """
        return self._comparative_start_time

    @comparative_start_time.setter
    def comparative_start_time(self, comparative_start_time):
        r"""Sets the comparative_start_time of this CompareSlowLogTemplatesRequestBody.

        对比日期开始时间（Unix timestamp），单位：毫秒

        :param comparative_start_time: The comparative_start_time of this CompareSlowLogTemplatesRequestBody.
        :type comparative_start_time: int
        """
        self._comparative_start_time = comparative_start_time

    @property
    def comparative_end_time(self):
        r"""Gets the comparative_end_time of this CompareSlowLogTemplatesRequestBody.

        对比日期结束时间（Unix timestamp），单位：毫秒

        :return: The comparative_end_time of this CompareSlowLogTemplatesRequestBody.
        :rtype: int
        """
        return self._comparative_end_time

    @comparative_end_time.setter
    def comparative_end_time(self, comparative_end_time):
        r"""Sets the comparative_end_time of this CompareSlowLogTemplatesRequestBody.

        对比日期结束时间（Unix timestamp），单位：毫秒

        :param comparative_end_time: The comparative_end_time of this CompareSlowLogTemplatesRequestBody.
        :type comparative_end_time: int
        """
        self._comparative_end_time = comparative_end_time

    @property
    def base_line_start_time(self):
        r"""Gets the base_line_start_time of this CompareSlowLogTemplatesRequestBody.

        基线日期开始时间（Unix timestamp），单位：毫秒

        :return: The base_line_start_time of this CompareSlowLogTemplatesRequestBody.
        :rtype: int
        """
        return self._base_line_start_time

    @base_line_start_time.setter
    def base_line_start_time(self, base_line_start_time):
        r"""Sets the base_line_start_time of this CompareSlowLogTemplatesRequestBody.

        基线日期开始时间（Unix timestamp），单位：毫秒

        :param base_line_start_time: The base_line_start_time of this CompareSlowLogTemplatesRequestBody.
        :type base_line_start_time: int
        """
        self._base_line_start_time = base_line_start_time

    @property
    def base_line_end_time(self):
        r"""Gets the base_line_end_time of this CompareSlowLogTemplatesRequestBody.

        基线日期结束时间（Unix timestamp），单位：毫秒

        :return: The base_line_end_time of this CompareSlowLogTemplatesRequestBody.
        :rtype: int
        """
        return self._base_line_end_time

    @base_line_end_time.setter
    def base_line_end_time(self, base_line_end_time):
        r"""Sets the base_line_end_time of this CompareSlowLogTemplatesRequestBody.

        基线日期结束时间（Unix timestamp），单位：毫秒

        :param base_line_end_time: The base_line_end_time of this CompareSlowLogTemplatesRequestBody.
        :type base_line_end_time: int
        """
        self._base_line_end_time = base_line_end_time

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
        if not isinstance(other, CompareSlowLogTemplatesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
