# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlLimitUserInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'page_num': 'page_num',
        'page_size': 'page_size'
    }

    def __init__(self, engine_type=None, page_num=None, page_size=None):
        r"""ListSqlLimitUserInstanceRequestBody

        The model defined in huaweicloud sdk

        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param page_num: 页码，取值范围 [0, 5000]，默认为 0
        :type page_num: int
        :param page_size: 查询记录数，取值范围 [0, 100]，默认为 20
        :type page_size: int
        """
        
        

        self._engine_type = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None

        self.engine_type = engine_type
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ListSqlLimitUserInstanceRequestBody.

        数据库引擎类型

        :return: The engine_type of this ListSqlLimitUserInstanceRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ListSqlLimitUserInstanceRequestBody.

        数据库引擎类型

        :param engine_type: The engine_type of this ListSqlLimitUserInstanceRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def page_num(self):
        r"""Gets the page_num of this ListSqlLimitUserInstanceRequestBody.

        页码，取值范围 [0, 5000]，默认为 0

        :return: The page_num of this ListSqlLimitUserInstanceRequestBody.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ListSqlLimitUserInstanceRequestBody.

        页码，取值范围 [0, 5000]，默认为 0

        :param page_num: The page_num of this ListSqlLimitUserInstanceRequestBody.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this ListSqlLimitUserInstanceRequestBody.

        查询记录数，取值范围 [0, 100]，默认为 20

        :return: The page_size of this ListSqlLimitUserInstanceRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListSqlLimitUserInstanceRequestBody.

        查询记录数，取值范围 [0, 100]，默认为 20

        :param page_size: The page_size of this ListSqlLimitUserInstanceRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ListSqlLimitUserInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
