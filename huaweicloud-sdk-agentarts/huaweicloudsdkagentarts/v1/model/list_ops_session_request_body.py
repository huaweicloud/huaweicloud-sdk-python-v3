# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsSessionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'business_id': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'filter': 'list[ListFilterParam]',
        'label_filter': 'list[FilterParam]',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'business_id': 'business_id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'filter': 'filter',
        'label_filter': 'label_filter',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, start_time=None, end_time=None, business_id=None, resource_id=None, resource_type=None, filter=None, label_filter=None, page_no=None, page_size=None):
        r"""ListOpsSessionRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 时间戳
        :type start_time: int
        :param end_time: 时间戳
        :type end_time: int
        :param business_id: 企业id
        :type business_id: str
        :param resource_id: 资源id
        :type resource_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param filter: 过滤条件
        :type filter: list[:class:`huaweicloudsdkagentarts.v1.ListFilterParam`]
        :param label_filter: 标签过滤条件
        :type label_filter: list[:class:`huaweicloudsdkagentarts.v1.FilterParam`]
        :param page_no: 页面序号
        :type page_no: int
        :param page_size: 单页大小
        :type page_size: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._business_id = None
        self._resource_id = None
        self._resource_type = None
        self._filter = None
        self._label_filter = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if business_id is not None:
            self.business_id = business_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if filter is not None:
            self.filter = filter
        if label_filter is not None:
            self.label_filter = label_filter
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def start_time(self):
        r"""Gets the start_time of this ListOpsSessionRequestBody.

        时间戳

        :return: The start_time of this ListOpsSessionRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListOpsSessionRequestBody.

        时间戳

        :param start_time: The start_time of this ListOpsSessionRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListOpsSessionRequestBody.

        时间戳

        :return: The end_time of this ListOpsSessionRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListOpsSessionRequestBody.

        时间戳

        :param end_time: The end_time of this ListOpsSessionRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def business_id(self):
        r"""Gets the business_id of this ListOpsSessionRequestBody.

        企业id

        :return: The business_id of this ListOpsSessionRequestBody.
        :rtype: str
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        r"""Sets the business_id of this ListOpsSessionRequestBody.

        企业id

        :param business_id: The business_id of this ListOpsSessionRequestBody.
        :type business_id: str
        """
        self._business_id = business_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListOpsSessionRequestBody.

        资源id

        :return: The resource_id of this ListOpsSessionRequestBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListOpsSessionRequestBody.

        资源id

        :param resource_id: The resource_id of this ListOpsSessionRequestBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListOpsSessionRequestBody.

        资源类型

        :return: The resource_type of this ListOpsSessionRequestBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListOpsSessionRequestBody.

        资源类型

        :param resource_type: The resource_type of this ListOpsSessionRequestBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def filter(self):
        r"""Gets the filter of this ListOpsSessionRequestBody.

        过滤条件

        :return: The filter of this ListOpsSessionRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ListFilterParam`]
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListOpsSessionRequestBody.

        过滤条件

        :param filter: The filter of this ListOpsSessionRequestBody.
        :type filter: list[:class:`huaweicloudsdkagentarts.v1.ListFilterParam`]
        """
        self._filter = filter

    @property
    def label_filter(self):
        r"""Gets the label_filter of this ListOpsSessionRequestBody.

        标签过滤条件

        :return: The label_filter of this ListOpsSessionRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.FilterParam`]
        """
        return self._label_filter

    @label_filter.setter
    def label_filter(self, label_filter):
        r"""Sets the label_filter of this ListOpsSessionRequestBody.

        标签过滤条件

        :param label_filter: The label_filter of this ListOpsSessionRequestBody.
        :type label_filter: list[:class:`huaweicloudsdkagentarts.v1.FilterParam`]
        """
        self._label_filter = label_filter

    @property
    def page_no(self):
        r"""Gets the page_no of this ListOpsSessionRequestBody.

        页面序号

        :return: The page_no of this ListOpsSessionRequestBody.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListOpsSessionRequestBody.

        页面序号

        :param page_no: The page_no of this ListOpsSessionRequestBody.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListOpsSessionRequestBody.

        单页大小

        :return: The page_size of this ListOpsSessionRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListOpsSessionRequestBody.

        单页大小

        :param page_size: The page_size of this ListOpsSessionRequestBody.
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
        if not isinstance(other, ListOpsSessionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
