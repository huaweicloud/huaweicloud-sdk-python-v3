# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceUsageRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'bill_cycle': 'str',
        'service_type_code': 'str',
        'resource_type_code': 'str',
        'usage_type': 'str',
        'resource_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'bill_cycle': 'bill_cycle',
        'service_type_code': 'service_type_code',
        'resource_type_code': 'resource_type_code',
        'usage_type': 'usage_type',
        'resource_id': 'resource_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, bill_cycle=None, service_type_code=None, resource_type_code=None, usage_type=None, resource_id=None, offset=None, limit=None):
        """ListResourceUsageRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._bill_cycle = None
        self._service_type_code = None
        self._resource_type_code = None
        self._usage_type = None
        self._resource_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.bill_cycle = bill_cycle
        self.service_type_code = service_type_code
        self.resource_type_code = resource_type_code
        self.usage_type = usage_type
        self.resource_id = resource_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListResourceUsageRequest.

        |语言。en_US：英文；zh_CN：中文。默认：zh_CN：中文|

        :return: The x_language of this ListResourceUsageRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListResourceUsageRequest.

        |语言。en_US：英文；zh_CN：中文。默认：zh_CN：中文|

        :param x_language: The x_language of this ListResourceUsageRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this ListResourceUsageRequest.

        账期，格式为yyyy-MM。

        :return: The bill_cycle of this ListResourceUsageRequest.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this ListResourceUsageRequest.

        账期，格式为yyyy-MM。

        :param bill_cycle: The bill_cycle of this ListResourceUsageRequest.
        :type: str
        """
        self._bill_cycle = bill_cycle

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ListResourceUsageRequest.

        云服务类型，当前仅支持：hws.service.type.cdn：内容分发网络hws.service.type.obs：对象存储服务

        :return: The service_type_code of this ListResourceUsageRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ListResourceUsageRequest.

        云服务类型，当前仅支持：hws.service.type.cdn：内容分发网络hws.service.type.obs：对象存储服务

        :param service_type_code: The service_type_code of this ListResourceUsageRequest.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this ListResourceUsageRequest.

        资源类型编码，当前仅支持：hws.resource.type.cdn：CDNhws.resource.type.obs：云存储资源类型和云服务类型的对应关系可调用根据云服务类型查询资源列表接口获取。

        :return: The resource_type_code of this ListResourceUsageRequest.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this ListResourceUsageRequest.

        资源类型编码，当前仅支持：hws.resource.type.cdn：CDNhws.resource.type.obs：云存储资源类型和云服务类型的对应关系可调用根据云服务类型查询资源列表接口获取。

        :param resource_type_code: The resource_type_code of this ListResourceUsageRequest.
        :type: str
        """
        self._resource_type_code = resource_type_code

    @property
    def usage_type(self):
        """Gets the usage_type of this ListResourceUsageRequest.

        使用量类型编码，当前仅支持：95Peak：中国大陆月95峰值带宽_1024进制95peak_1000：中国大陆月95峰值带宽_1000进制bandwidth95peak：95峰值带宽资源类型和使用量类型的对应关系可调用查询使用量类型列表接口获取。

        :return: The usage_type of this ListResourceUsageRequest.
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this ListResourceUsageRequest.

        使用量类型编码，当前仅支持：95Peak：中国大陆月95峰值带宽_1024进制95peak_1000：中国大陆月95峰值带宽_1000进制bandwidth95peak：95峰值带宽资源类型和使用量类型的对应关系可调用查询使用量类型列表接口获取。

        :param usage_type: The usage_type of this ListResourceUsageRequest.
        :type: str
        """
        self._usage_type = usage_type

    @property
    def resource_id(self):
        """Gets the resource_id of this ListResourceUsageRequest.

        资源ID，您可以调用查询资源用量汇总接口获取。

        :return: The resource_id of this ListResourceUsageRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListResourceUsageRequest.

        资源ID，您可以调用查询资源用量汇总接口获取。

        :param resource_id: The resource_id of this ListResourceUsageRequest.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def offset(self):
        """Gets the offset of this ListResourceUsageRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListResourceUsageRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListResourceUsageRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListResourceUsageRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListResourceUsageRequest.

        每次查询的数量限制。默认值为10。

        :return: The limit of this ListResourceUsageRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourceUsageRequest.

        每次查询的数量限制。默认值为10。

        :param limit: The limit of this ListResourceUsageRequest.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListResourceUsageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other