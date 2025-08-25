# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_size': 'int',
        'page_num': 'int',
        'app_name': 'str',
        'vpc_name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'page_size': 'page_size',
        'page_num': 'page_num',
        'app_name': 'app_name',
        'vpc_name': 'vpc_name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, page_size=None, page_num=None, app_name=None, vpc_name=None, sort_key=None, sort_dir=None):
        r"""ShowAppListRequest

        The model defined in huaweicloud sdk

        :param page_size: 指定查询返回记录条数，默认值10
        :type page_size: int
        :param page_num: 索引位置，从page_num指定的下一条数据开始查询默认值为0
        :type page_num: int
        :param app_name: 应用名称
        :type app_name: str
        :param vpc_name: 所属的VPC名称
        :type vpc_name: str
        :param sort_key: 排序属性，目前支持以下属性： - **create_time** : 应用的创建时间（默认）
        :type sort_key: str
        :param sort_dir: 排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序
        :type sort_dir: str
        """
        
        

        self._page_size = None
        self._page_num = None
        self._app_name = None
        self._vpc_name = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if page_num is not None:
            self.page_num = page_num
        if app_name is not None:
            self.app_name = app_name
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowAppListRequest.

        指定查询返回记录条数，默认值10

        :return: The page_size of this ShowAppListRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowAppListRequest.

        指定查询返回记录条数，默认值10

        :param page_size: The page_size of this ShowAppListRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_num(self):
        r"""Gets the page_num of this ShowAppListRequest.

        索引位置，从page_num指定的下一条数据开始查询默认值为0

        :return: The page_num of this ShowAppListRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ShowAppListRequest.

        索引位置，从page_num指定的下一条数据开始查询默认值为0

        :param page_num: The page_num of this ShowAppListRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def app_name(self):
        r"""Gets the app_name of this ShowAppListRequest.

        应用名称

        :return: The app_name of this ShowAppListRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ShowAppListRequest.

        应用名称

        :param app_name: The app_name of this ShowAppListRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this ShowAppListRequest.

        所属的VPC名称

        :return: The vpc_name of this ShowAppListRequest.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this ShowAppListRequest.

        所属的VPC名称

        :param vpc_name: The vpc_name of this ShowAppListRequest.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ShowAppListRequest.

        排序属性，目前支持以下属性： - **create_time** : 应用的创建时间（默认）

        :return: The sort_key of this ShowAppListRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ShowAppListRequest.

        排序属性，目前支持以下属性： - **create_time** : 应用的创建时间（默认）

        :param sort_key: The sort_key of this ShowAppListRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ShowAppListRequest.

        排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序

        :return: The sort_dir of this ShowAppListRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ShowAppListRequest.

        排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序

        :param sort_dir: The sort_dir of this ShowAppListRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ShowAppListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
