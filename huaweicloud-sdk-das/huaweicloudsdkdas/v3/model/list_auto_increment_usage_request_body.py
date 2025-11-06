# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAutoIncrementUsageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ratio': 'str',
        'real_time': 'bool',
        'offsite': 'str',
        'limit': 'str',
        'database': 'list[str]'
    }

    attribute_map = {
        'ratio': 'ratio',
        'real_time': 'real_time',
        'offsite': 'offsite',
        'limit': 'limit',
        'database': 'database'
    }

    def __init__(self, ratio=None, real_time=None, offsite=None, limit=None, database=None):
        r"""ListAutoIncrementUsageRequestBody

        The model defined in huaweicloud sdk

        :param ratio: 自增 ID 使用比例过滤值，只返回超过该比例的自增 ID 使用数据。取值为 0~1 的小数，默认为0
        :type ratio: str
        :param real_time: 是否获取实时数据： true：实时查询实例上数据并计算。最小查询时间粒度为 10 分钟，即有 10 分钟内的数据时，即使传递 true 也不进行实时查询。 false：当有近两小时的数据时，返回该数据，否则查询实例上最新数据。
        :type real_time: bool
        :param offsite: 偏移值
        :type offsite: str
        :param limit: 每次获取的数量
        :type limit: str
        :param database: 数据库名。传入此参数时，查询指定数据库中表自增 ID 使用情况，不传入时查询实例上所有数据库的表自增 ID 使用情况。
        :type database: list[str]
        """
        
        

        self._ratio = None
        self._real_time = None
        self._offsite = None
        self._limit = None
        self._database = None
        self.discriminator = None

        self.ratio = ratio
        self.real_time = real_time
        if offsite is not None:
            self.offsite = offsite
        if limit is not None:
            self.limit = limit
        if database is not None:
            self.database = database

    @property
    def ratio(self):
        r"""Gets the ratio of this ListAutoIncrementUsageRequestBody.

        自增 ID 使用比例过滤值，只返回超过该比例的自增 ID 使用数据。取值为 0~1 的小数，默认为0

        :return: The ratio of this ListAutoIncrementUsageRequestBody.
        :rtype: str
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        r"""Sets the ratio of this ListAutoIncrementUsageRequestBody.

        自增 ID 使用比例过滤值，只返回超过该比例的自增 ID 使用数据。取值为 0~1 的小数，默认为0

        :param ratio: The ratio of this ListAutoIncrementUsageRequestBody.
        :type ratio: str
        """
        self._ratio = ratio

    @property
    def real_time(self):
        r"""Gets the real_time of this ListAutoIncrementUsageRequestBody.

        是否获取实时数据： true：实时查询实例上数据并计算。最小查询时间粒度为 10 分钟，即有 10 分钟内的数据时，即使传递 true 也不进行实时查询。 false：当有近两小时的数据时，返回该数据，否则查询实例上最新数据。

        :return: The real_time of this ListAutoIncrementUsageRequestBody.
        :rtype: bool
        """
        return self._real_time

    @real_time.setter
    def real_time(self, real_time):
        r"""Sets the real_time of this ListAutoIncrementUsageRequestBody.

        是否获取实时数据： true：实时查询实例上数据并计算。最小查询时间粒度为 10 分钟，即有 10 分钟内的数据时，即使传递 true 也不进行实时查询。 false：当有近两小时的数据时，返回该数据，否则查询实例上最新数据。

        :param real_time: The real_time of this ListAutoIncrementUsageRequestBody.
        :type real_time: bool
        """
        self._real_time = real_time

    @property
    def offsite(self):
        r"""Gets the offsite of this ListAutoIncrementUsageRequestBody.

        偏移值

        :return: The offsite of this ListAutoIncrementUsageRequestBody.
        :rtype: str
        """
        return self._offsite

    @offsite.setter
    def offsite(self, offsite):
        r"""Sets the offsite of this ListAutoIncrementUsageRequestBody.

        偏移值

        :param offsite: The offsite of this ListAutoIncrementUsageRequestBody.
        :type offsite: str
        """
        self._offsite = offsite

    @property
    def limit(self):
        r"""Gets the limit of this ListAutoIncrementUsageRequestBody.

        每次获取的数量

        :return: The limit of this ListAutoIncrementUsageRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAutoIncrementUsageRequestBody.

        每次获取的数量

        :param limit: The limit of this ListAutoIncrementUsageRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def database(self):
        r"""Gets the database of this ListAutoIncrementUsageRequestBody.

        数据库名。传入此参数时，查询指定数据库中表自增 ID 使用情况，不传入时查询实例上所有数据库的表自增 ID 使用情况。

        :return: The database of this ListAutoIncrementUsageRequestBody.
        :rtype: list[str]
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ListAutoIncrementUsageRequestBody.

        数据库名。传入此参数时，查询指定数据库中表自增 ID 使用情况，不传入时查询实例上所有数据库的表自增 ID 使用情况。

        :param database: The database of this ListAutoIncrementUsageRequestBody.
        :type database: list[str]
        """
        self._database = database

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
        if not isinstance(other, ListAutoIncrementUsageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
