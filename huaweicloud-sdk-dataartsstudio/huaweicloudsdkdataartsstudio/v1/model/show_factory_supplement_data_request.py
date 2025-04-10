# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFactorySupplementDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'sort': 'str',
        'page': 'str',
        'size': 'str',
        'name': 'str',
        'user_name': 'str',
        'status': 'str',
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'sort': 'sort',
        'page': 'page',
        'size': 'size',
        'name': 'name',
        'user_name': 'user_name',
        'status': 'status',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, workspace=None, sort=None, page=None, size=None, name=None, user_name=None, status=None, start_date=None, end_date=None):
        r"""ShowFactorySupplementDataRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID
        :type workspace: str
        :param sort: 排序字段:desc：创建时间按照降序展示asc ：创建时间按照升序展示默认值：desc
        :type sort: str
        :param page: 分页列表的起始页，默认值为0。取值范围大于等于0。
        :type page: str
        :param size: 分页返回结果，指定每页最大记录数。默认值：10
        :type size: str
        :param name: 补数据名称
        :type name: str
        :param user_name: 用户名
        :type user_name: str
        :param status: 实例状态：SUCCESS：成功RUNNING ：运行中CANCLE：取消
        :type status: str
        :param start_date: 查询作业的开始日期 13位时间戳
        :type start_date: str
        :param end_date: 查询作业的结束日期 13位时间戳
        :type end_date: str
        """
        
        

        self._workspace = None
        self._sort = None
        self._page = None
        self._size = None
        self._name = None
        self._user_name = None
        self._status = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        if sort is not None:
            self.sort = sort
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if name is not None:
            self.name = name
        if user_name is not None:
            self.user_name = user_name
        if status is not None:
            self.status = status
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowFactorySupplementDataRequest.

        工作空间ID

        :return: The workspace of this ShowFactorySupplementDataRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowFactorySupplementDataRequest.

        工作空间ID

        :param workspace: The workspace of this ShowFactorySupplementDataRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def sort(self):
        r"""Gets the sort of this ShowFactorySupplementDataRequest.

        排序字段:desc：创建时间按照降序展示asc ：创建时间按照升序展示默认值：desc

        :return: The sort of this ShowFactorySupplementDataRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ShowFactorySupplementDataRequest.

        排序字段:desc：创建时间按照降序展示asc ：创建时间按照升序展示默认值：desc

        :param sort: The sort of this ShowFactorySupplementDataRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def page(self):
        r"""Gets the page of this ShowFactorySupplementDataRequest.

        分页列表的起始页，默认值为0。取值范围大于等于0。

        :return: The page of this ShowFactorySupplementDataRequest.
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ShowFactorySupplementDataRequest.

        分页列表的起始页，默认值为0。取值范围大于等于0。

        :param page: The page of this ShowFactorySupplementDataRequest.
        :type page: str
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this ShowFactorySupplementDataRequest.

        分页返回结果，指定每页最大记录数。默认值：10

        :return: The size of this ShowFactorySupplementDataRequest.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowFactorySupplementDataRequest.

        分页返回结果，指定每页最大记录数。默认值：10

        :param size: The size of this ShowFactorySupplementDataRequest.
        :type size: str
        """
        self._size = size

    @property
    def name(self):
        r"""Gets the name of this ShowFactorySupplementDataRequest.

        补数据名称

        :return: The name of this ShowFactorySupplementDataRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowFactorySupplementDataRequest.

        补数据名称

        :param name: The name of this ShowFactorySupplementDataRequest.
        :type name: str
        """
        self._name = name

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowFactorySupplementDataRequest.

        用户名

        :return: The user_name of this ShowFactorySupplementDataRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowFactorySupplementDataRequest.

        用户名

        :param user_name: The user_name of this ShowFactorySupplementDataRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def status(self):
        r"""Gets the status of this ShowFactorySupplementDataRequest.

        实例状态：SUCCESS：成功RUNNING ：运行中CANCLE：取消

        :return: The status of this ShowFactorySupplementDataRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowFactorySupplementDataRequest.

        实例状态：SUCCESS：成功RUNNING ：运行中CANCLE：取消

        :param status: The status of this ShowFactorySupplementDataRequest.
        :type status: str
        """
        self._status = status

    @property
    def start_date(self):
        r"""Gets the start_date of this ShowFactorySupplementDataRequest.

        查询作业的开始日期 13位时间戳

        :return: The start_date of this ShowFactorySupplementDataRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this ShowFactorySupplementDataRequest.

        查询作业的开始日期 13位时间戳

        :param start_date: The start_date of this ShowFactorySupplementDataRequest.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        r"""Gets the end_date of this ShowFactorySupplementDataRequest.

        查询作业的结束日期 13位时间戳

        :return: The end_date of this ShowFactorySupplementDataRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this ShowFactorySupplementDataRequest.

        查询作业的结束日期 13位时间戳

        :param end_date: The end_date of this ShowFactorySupplementDataRequest.
        :type end_date: str
        """
        self._end_date = end_date

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
        if not isinstance(other, ShowFactorySupplementDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
