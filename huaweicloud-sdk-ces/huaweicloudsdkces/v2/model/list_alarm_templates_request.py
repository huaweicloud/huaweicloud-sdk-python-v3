# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'namespace': 'str',
        'dim_name': 'str',
        'template_type': 'str',
        'template_name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'namespace': 'namespace',
        'dim_name': 'dim_name',
        'template_type': 'template_type',
        'template_name': 'template_name'
    }

    def __init__(self, offset=None, limit=None, namespace=None, dim_name=None, template_type=None, template_name=None):
        """ListAlarmTemplatesRequest

        The model defined in huaweicloud sdk

        :param offset: 分页查询时查询的起始位置，表示从第几条数据开始，默认为0
        :type offset: int
        :param limit: 查询结果条数的限制值，取值范围为[1,100]，默认值为100
        :type limit: int
        :param namespace: 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”
        :type namespace: str
        :param dim_name: 资源维度，必须以字母开头，多维度用\&quot;,\&quot;分割，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32
        :type dim_name: str
        :param template_type: 模板类型(system代表默认指标模板，custom代表自定义指标模板，system_event代表默认事件模板，custom_event代表自定义事件模板，system_custom_event代表全部事件模板),不传返回全部指标模板
        :type template_type: str
        :param template_name: 告警模板的名称，以字母或汉字开头，可包含字母、数字、汉字、_、-，长度范围[1,128]，支持模糊匹配
        :type template_name: str
        """
        
        

        self._offset = None
        self._limit = None
        self._namespace = None
        self._dim_name = None
        self._template_type = None
        self._template_name = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if namespace is not None:
            self.namespace = namespace
        if dim_name is not None:
            self.dim_name = dim_name
        if template_type is not None:
            self.template_type = template_type
        if template_name is not None:
            self.template_name = template_name

    @property
    def offset(self):
        """Gets the offset of this ListAlarmTemplatesRequest.

        分页查询时查询的起始位置，表示从第几条数据开始，默认为0

        :return: The offset of this ListAlarmTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAlarmTemplatesRequest.

        分页查询时查询的起始位置，表示从第几条数据开始，默认为0

        :param offset: The offset of this ListAlarmTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAlarmTemplatesRequest.

        查询结果条数的限制值，取值范围为[1,100]，默认值为100

        :return: The limit of this ListAlarmTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAlarmTemplatesRequest.

        查询结果条数的限制值，取值范围为[1,100]，默认值为100

        :param limit: The limit of this ListAlarmTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def namespace(self):
        """Gets the namespace of this ListAlarmTemplatesRequest.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :return: The namespace of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListAlarmTemplatesRequest.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :param namespace: The namespace of this ListAlarmTemplatesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dim_name(self):
        """Gets the dim_name of this ListAlarmTemplatesRequest.

        资源维度，必须以字母开头，多维度用\",\"分割，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32

        :return: The dim_name of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._dim_name

    @dim_name.setter
    def dim_name(self, dim_name):
        """Sets the dim_name of this ListAlarmTemplatesRequest.

        资源维度，必须以字母开头，多维度用\",\"分割，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32

        :param dim_name: The dim_name of this ListAlarmTemplatesRequest.
        :type dim_name: str
        """
        self._dim_name = dim_name

    @property
    def template_type(self):
        """Gets the template_type of this ListAlarmTemplatesRequest.

        模板类型(system代表默认指标模板，custom代表自定义指标模板，system_event代表默认事件模板，custom_event代表自定义事件模板，system_custom_event代表全部事件模板),不传返回全部指标模板

        :return: The template_type of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this ListAlarmTemplatesRequest.

        模板类型(system代表默认指标模板，custom代表自定义指标模板，system_event代表默认事件模板，custom_event代表自定义事件模板，system_custom_event代表全部事件模板),不传返回全部指标模板

        :param template_type: The template_type of this ListAlarmTemplatesRequest.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def template_name(self):
        """Gets the template_name of this ListAlarmTemplatesRequest.

        告警模板的名称，以字母或汉字开头，可包含字母、数字、汉字、_、-，长度范围[1,128]，支持模糊匹配

        :return: The template_name of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this ListAlarmTemplatesRequest.

        告警模板的名称，以字母或汉字开头，可包含字母、数字、汉字、_、-，长度范围[1,128]，支持模糊匹配

        :param template_name: The template_name of this ListAlarmTemplatesRequest.
        :type template_name: str
        """
        self._template_name = template_name

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
        if not isinstance(other, ListAlarmTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
