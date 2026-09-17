# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesRequestBody:

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
        'instance_status': 'str',
        'cur_page': 'int',
        'page_size': 'int',
        'instance_type': 'str',
        'engine_version': 'str',
        'transaction_flag': 'bool'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'instance_status': 'instance_status',
        'cur_page': 'cur_page',
        'page_size': 'page_size',
        'instance_type': 'instance_type',
        'engine_version': 'engine_version',
        'transaction_flag': 'transaction_flag'
    }

    def __init__(self, engine_type=None, instance_status=None, cur_page=None, page_size=None, instance_type=None, engine_version=None, transaction_flag=None):
        r"""ListInstancesRequestBody

        The model defined in huaweicloud sdk

        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param instance_status: 实例状态
        :type instance_status: str
        :param cur_page: 页数
        :type cur_page: int
        :param page_size: 页大小
        :type page_size: int
        :param instance_type: 实例类型
        :type instance_type: str
        :param engine_version: 实例版本
        :type engine_version: str
        :param transaction_flag: 历史事务是否开启
        :type transaction_flag: bool
        """
        
        

        self._engine_type = None
        self._instance_status = None
        self._cur_page = None
        self._page_size = None
        self._instance_type = None
        self._engine_version = None
        self._transaction_flag = None
        self.discriminator = None

        if engine_type is not None:
            self.engine_type = engine_type
        if instance_status is not None:
            self.instance_status = instance_status
        if cur_page is not None:
            self.cur_page = cur_page
        if page_size is not None:
            self.page_size = page_size
        if instance_type is not None:
            self.instance_type = instance_type
        if engine_version is not None:
            self.engine_version = engine_version
        if transaction_flag is not None:
            self.transaction_flag = transaction_flag

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ListInstancesRequestBody.

        数据库引擎类型

        :return: The engine_type of this ListInstancesRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ListInstancesRequestBody.

        数据库引擎类型

        :param engine_type: The engine_type of this ListInstancesRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def instance_status(self):
        r"""Gets the instance_status of this ListInstancesRequestBody.

        实例状态

        :return: The instance_status of this ListInstancesRequestBody.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this ListInstancesRequestBody.

        实例状态

        :param instance_status: The instance_status of this ListInstancesRequestBody.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListInstancesRequestBody.

        页数

        :return: The cur_page of this ListInstancesRequestBody.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListInstancesRequestBody.

        页数

        :param cur_page: The cur_page of this ListInstancesRequestBody.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def page_size(self):
        r"""Gets the page_size of this ListInstancesRequestBody.

        页大小

        :return: The page_size of this ListInstancesRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListInstancesRequestBody.

        页大小

        :param page_size: The page_size of this ListInstancesRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def instance_type(self):
        r"""Gets the instance_type of this ListInstancesRequestBody.

        实例类型

        :return: The instance_type of this ListInstancesRequestBody.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this ListInstancesRequestBody.

        实例类型

        :param instance_type: The instance_type of this ListInstancesRequestBody.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ListInstancesRequestBody.

        实例版本

        :return: The engine_version of this ListInstancesRequestBody.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ListInstancesRequestBody.

        实例版本

        :param engine_version: The engine_version of this ListInstancesRequestBody.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def transaction_flag(self):
        r"""Gets the transaction_flag of this ListInstancesRequestBody.

        历史事务是否开启

        :return: The transaction_flag of this ListInstancesRequestBody.
        :rtype: bool
        """
        return self._transaction_flag

    @transaction_flag.setter
    def transaction_flag(self, transaction_flag):
        r"""Sets the transaction_flag of this ListInstancesRequestBody.

        历史事务是否开启

        :param transaction_flag: The transaction_flag of this ListInstancesRequestBody.
        :type transaction_flag: bool
        """
        self._transaction_flag = transaction_flag

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
        if not isinstance(other, ListInstancesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
